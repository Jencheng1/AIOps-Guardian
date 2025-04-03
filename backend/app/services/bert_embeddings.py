from typing import List, Dict, Any, Optional, Tuple
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from langchain.embeddings.base import Embeddings
from enum import Enum
import time
import datetime
import boto3
import logging

logger = logging.getLogger(__name__)

class BERTModelType(Enum):
    BERT_BASE = "bert-base-uncased"
    BERT_LARGE = "bert-large-uncased"
    ROBERTA = "roberta-base"
    DISTILBERT = "distilbert-base-uncased"

class BERTEmbeddings(Embeddings):
    def __init__(self, model_type: BERTModelType = BERTModelType.BERT_BASE):
        """Initialize BERT embeddings with specified model"""
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model_type = model_type
        self.tokenizer = AutoTokenizer.from_pretrained(model_type.value)
        self.model = AutoModel.from_pretrained(model_type.value).to(self.device)
        self.model.eval()
        
    def _get_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a list of texts using BERT"""
        embeddings = []
        
        with torch.no_grad():
            for text in texts:
                # Tokenize and prepare input
                inputs = self.tokenizer(
                    text,
                    padding=True,
                    truncation=True,
                    max_length=512,
                    return_tensors="pt"
                ).to(self.device)
                
                # Get BERT outputs
                outputs = self.model(**inputs)
                
                # Use CLS token embedding (first token)
                cls_embedding = outputs.last_hidden_state[0][0].cpu().numpy()
                
                # Normalize embedding
                normalized_embedding = cls_embedding / np.linalg.norm(cls_embedding)
                embeddings.append(normalized_embedding.tolist())
        
        return embeddings
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for documents"""
        return self._get_embeddings(texts)
    
    def embed_query(self, text: str) -> List[float]:
        """Generate embedding for a single query"""
        return self._get_embeddings([text])[0]

class BERTVectorSearch:
    def __init__(self, model_type: BERTModelType = BERTModelType.BERT_BASE):
        """Initialize BERT-based vector search"""
        self.embeddings = BERTEmbeddings(model_type)
        self.vector_store = None
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('AIOpsGuardian-Incidents')
        self.cloudwatch = boto3.client('cloudwatch')
        
    def _prepare_documents(self, incidents: List[Dict[str, Any]]) -> List[str]:
        """Prepare incident documents for BERT embedding"""
        documents = []
        for incident in incidents:
            # Create a rich text representation optimized for BERT
            doc = f"""
            Incident: {incident.get('Title', '')}
            Description: {incident.get('Description', '')}
            Root Cause: {incident.get('RootCause', '')}
            Resolution: {incident.get('Resolution', '')}
            Impact: {incident.get('Impact', '')}
            Severity: {incident.get('Severity', '')}
            Status: {incident.get('Status', '')}
            """
            documents.append(doc)
        return documents
    
    def build_index(self):
        """Build or update the BERT-based vector index"""
        start_time = time.time()
        incidents = self._load_incidents()
        documents = self._prepare_documents(incidents)
        
        # Create or update vector store with BERT embeddings
        if self.vector_store is None:
            self.vector_store = FAISS.from_documents(
                documents=documents,
                embedding=self.embeddings
            )
        else:
            self.vector_store.add_documents(documents)
            
        # Log performance metrics
        duration = time.time() - start_time
        self._log_metrics({
            'IndexBuildDuration': duration,
            'DocumentCount': len(documents),
            'ModelType': self.embeddings.model_type.value
        })
    
    def search_similar_incidents(
        self, 
        query: str, 
        k: int = 5,
        use_hybrid: bool = False,
        hybrid_weight: float = 0.7
    ) -> List[Dict[str, Any]]:
        """Search for similar incidents using BERT embeddings with hybrid search option"""
        if self.vector_store is None:
            self.build_index()
        
        start_time = time.time()
        
        # Perform BERT-based search
        bert_docs = self.vector_store.similarity_search(query, k=k)
        bert_scores = [doc.metadata.get('score', 0) for doc in bert_docs]
        
        if use_hybrid:
            # Perform traditional search
            traditional_docs = self.traditional_search(query, k=k)
            traditional_scores = [doc.metadata.get('score', 0) for doc in traditional_docs]
            
            # Combine scores using weighted average
            combined_scores = [
                hybrid_weight * bert_score + (1 - hybrid_weight) * trad_score
                for bert_score, trad_score in zip(bert_scores, traditional_scores)
            ]
            
            # Sort by combined scores
            docs_and_scores = list(zip(bert_docs, combined_scores))
            docs_and_scores.sort(key=lambda x: x[1], reverse=True)
            docs = [doc for doc, _ in docs_and_scores]
        else:
            docs = bert_docs
        
        # Extract incident IDs and fetch full details
        incident_ids = []
        for doc in docs:
            content = doc.page_content
            incident_id = content.split("Incident ID: ")[1].split("\n")[0]
            incident_ids.append(incident_id)
        
        similar_incidents = []
        for incident_id in incident_ids:
            response = self.table.get_item(Key={'IncidentId': incident_id})
            if 'Item' in response:
                similar_incidents.append(response['Item'])
        
        # Log performance metrics
        duration = time.time() - start_time
        self._log_metrics({
            'SearchDuration': duration,
            'ResultCount': len(similar_incidents),
            'QueryLength': len(query),
            'UseHybrid': use_hybrid,
            'HybridWeight': hybrid_weight
        })
        
        return similar_incidents
    
    def get_embedding_similarity(self, text1: str, text2: str) -> float:
        """Calculate similarity between two texts using BERT embeddings"""
        start_time = time.time()
        
        embedding1 = self.embeddings.embed_query(text1)
        embedding2 = self.embeddings.embed_query(text2)
        
        # Calculate cosine similarity
        similarity = np.dot(embedding1, embedding2) / (
            np.linalg.norm(embedding1) * np.linalg.norm(embedding2)
        )
        
        # Log performance metrics
        duration = time.time() - start_time
        self._log_metrics({
            'SimilarityCalculationDuration': duration,
            'Text1Length': len(text1),
            'Text2Length': len(text2),
            'SimilarityScore': float(similarity)
        })
        
        return float(similarity)
        
    def _log_metrics(self, metrics: Dict[str, Any]):
        """Log metrics to CloudWatch"""
        try:
            self.cloudwatch.put_metric_data(
                Namespace='AIOpsGuardian/BERT',
                MetricData=[
                    {
                        'MetricName': name,
                        'Value': value,
                        'Unit': 'Count' if isinstance(value, (int, float)) else 'None',
                        'Timestamp': datetime.datetime.now()
                    }
                    for name, value in metrics.items()
                ]
            )
        except Exception as e:
            logger.error(f"Failed to log metrics to CloudWatch: {str(e)}") 