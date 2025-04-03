from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any, Optional
from ..services.vector_search import VectorSearchService
from ..services.bert_embeddings import BERTVectorSearch, BERTModelType
from pydantic import BaseModel, Field

router = APIRouter()
vector_search = VectorSearchService()
bert_search = BERTVectorSearch()

class SearchQuery(BaseModel):
    query: str
    k: int = 5
    use_bert: bool = False
    model_type: Optional[BERTModelType] = BERTModelType.BERT_BASE
    use_hybrid: bool = False
    hybrid_weight: float = Field(default=0.7, ge=0.0, le=1.0)

class Incident(BaseModel):
    IncidentId: str
    Title: str
    Description: str
    RootCause: str = ""
    Resolution: str = ""
    Impact: str = ""
    Severity: str
    Status: str

class SimilarityQuery(BaseModel):
    text1: str
    text2: str
    model_type: Optional[BERTModelType] = BERTModelType.BERT_BASE

@router.post("/search", response_model=List[Dict[str, Any]])
async def search_similar_incidents(search_query: SearchQuery):
    """Search for similar incidents using vector similarity"""
    try:
        if search_query.use_bert:
            # Initialize BERT search with specified model
            bert_search = BERTVectorSearch(model_type=search_query.model_type)
            similar_incidents = bert_search.search_similar_incidents(
                query=search_query.query,
                k=search_query.k,
                use_hybrid=search_query.use_hybrid,
                hybrid_weight=search_query.hybrid_weight
            )
        else:
            similar_incidents = vector_search.search_similar_incidents(
                query=search_query.query,
                k=search_query.k
            )
        return similar_incidents
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/similarity", response_model=float)
async def calculate_similarity(similarity_query: SimilarityQuery):
    """Calculate similarity between two texts using BERT embeddings"""
    try:
        # Initialize BERT search with specified model
        bert_search = BERTVectorSearch(model_type=similarity_query.model_type)
        similarity = bert_search.get_embedding_similarity(
            similarity_query.text1,
            similarity_query.text2
        )
        return similarity
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/incidents", response_model=Dict[str, Any])
async def add_incident(incident: Incident):
    """Add a new incident to the vector store"""
    try:
        # Add to both vector stores
        vector_search.add_incident(incident.dict())
        bert_search.add_incident(incident.dict())
        return {"message": "Incident added successfully", "incident_id": incident.IncidentId}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/incidents/{incident_id}", response_model=Dict[str, Any])
async def update_incident(incident_id: str, updates: Dict[str, Any]):
    """Update an incident in the vector store"""
    try:
        # Update in both vector stores
        vector_search.update_incident(incident_id, updates)
        bert_search.update_incident(incident_id, updates)
        return {"message": "Incident updated successfully", "incident_id": incident_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/rebuild-index", response_model=Dict[str, Any])
async def rebuild_index(model_type: Optional[BERTModelType] = BERTModelType.BERT_BASE):
    """Rebuild the vector index"""
    try:
        vector_search.build_index()
        bert_search = BERTVectorSearch(model_type=model_type)
        bert_search.build_index()
        return {"message": "Vector indices rebuilt successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 