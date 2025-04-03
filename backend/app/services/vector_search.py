from typing import List, Dict, Any
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import JSONLoader
import json
import boto3
from datetime import datetime

class VectorSearchService:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
        self.vector_store = None
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('AIOpsGuardian-Incidents')
        
    def _load_incidents(self) -> List[Dict[str, Any]]:
        """Load incidents from DynamoDB"""
        response = self.table.scan()
        return response.get('Items', [])
    
    def _prepare_documents(self, incidents: List[Dict[str, Any]]) -> List[str]:
        """Prepare incident documents for embedding"""
        documents = []
        for incident in incidents:
            # Create a rich text representation of the incident
            doc = f"""
            Incident ID: {incident.get('IncidentId', '')}
            Title: {incident.get('Title', '')}
            Description: {incident.get('Description', '')}
            Root Cause: {incident.get('RootCause', '')}
            Resolution: {incident.get('Resolution', '')}
            Impact: {incident.get('Impact', '')}
            Severity: {incident.get('Severity', '')}
            Status: {incident.get('Status', '')}
            Created: {incident.get('CreatedAt', '')}
            """
            documents.append(doc)
        return documents
    
    def build_index(self):
        """Build or update the vector index"""
        incidents = self._load_incidents()
        documents = self._prepare_documents(incidents)
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        texts = text_splitter.create_documents(documents)
        
        # Create or update vector store
        if self.vector_store is None:
            self.vector_store = FAISS.from_documents(texts, self.embeddings)
        else:
            self.vector_store.add_documents(texts)
    
    def search_similar_incidents(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        """Search for similar incidents"""
        if self.vector_store is None:
            self.build_index()
        
        # Search for similar documents
        docs = self.vector_store.similarity_search(query, k=k)
        
        # Extract incident IDs from the documents
        incident_ids = []
        for doc in docs:
            # Extract incident ID from the document content
            content = doc.page_content
            incident_id = content.split("Incident ID: ")[1].split("\n")[0]
            incident_ids.append(incident_id)
        
        # Fetch full incident details from DynamoDB
        similar_incidents = []
        for incident_id in incident_ids:
            response = self.table.get_item(Key={'IncidentId': incident_id})
            if 'Item' in response:
                similar_incidents.append(response['Item'])
        
        return similar_incidents
    
    def add_incident(self, incident: Dict[str, Any]):
        """Add a new incident to the vector store"""
        # Add to DynamoDB
        incident['CreatedAt'] = datetime.utcnow().isoformat()
        self.table.put_item(Item=incident)
        
        # Update vector store
        documents = self._prepare_documents([incident])
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        texts = text_splitter.create_documents(documents)
        
        if self.vector_store is None:
            self.vector_store = FAISS.from_documents(texts, self.embeddings)
        else:
            self.vector_store.add_documents(texts)
    
    def update_incident(self, incident_id: str, updates: Dict[str, Any]):
        """Update an incident in both DynamoDB and vector store"""
        # Update DynamoDB
        update_expression = "SET " + ", ".join([f"#{k} = :{k}" for k in updates.keys()])
        expression_attribute_names = {f"#{k}": k for k in updates.keys()}
        expression_attribute_values = {f":{k}": v for k, v in updates.items()}
        
        self.table.update_item(
            Key={'IncidentId': incident_id},
            UpdateExpression=update_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values
        )
        
        # Rebuild index to include updates
        self.build_index() 