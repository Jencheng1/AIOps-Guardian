from typing import List, Dict, Any, Optional
import json
import logging
from datetime import datetime
from pydantic import BaseModel
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

logger = logging.getLogger(__name__)

class KnowledgeEntry(BaseModel):
    id: str
    incident_id: str
    content: Dict[str, Any]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime

class KnowledgeBase:
    def __init__(self):
        self.entries: List[KnowledgeEntry] = []
        self.vectorizer = TfidfVectorizer()
        self.vectors = None
        self._load_knowledge_base()

    def _load_knowledge_base(self):
        try:
            # Load from persistent storage (implementation needed)
            pass
        except Exception as e:
            logger.error(f"Error loading knowledge base: {str(e)}")
            self.entries = []

    def _save_knowledge_base(self):
        try:
            # Save to persistent storage (implementation needed)
            pass
        except Exception as e:
            logger.error(f"Error saving knowledge base: {str(e)}")

    def add_entry(self, incident_id: str, content: Dict[str, Any], metadata: Dict[str, Any]) -> KnowledgeEntry:
        entry = KnowledgeEntry(
            id=f"kb_{len(self.entries) + 1}",
            incident_id=incident_id,
            content=content,
            metadata=metadata,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        self.entries.append(entry)
        self._update_vectors()
        self._save_knowledge_base()
        return entry

    def update_entry(self, entry_id: str, content: Dict[str, Any], metadata: Dict[str, Any]) -> Optional[KnowledgeEntry]:
        for entry in self.entries:
            if entry.id == entry_id:
                entry.content = content
                entry.metadata = metadata
                entry.updated_at = datetime.utcnow()
                self._update_vectors()
                self._save_knowledge_base()
                return entry
        return None

    def get_entry(self, entry_id: str) -> Optional[KnowledgeEntry]:
        for entry in self.entries:
            if entry.id == entry_id:
                return entry
        return None

    def search_similar_incidents(self, query: Dict[str, Any], top_k: int = 5) -> List[Dict[str, Any]]:
        try:
            # Convert query to text representation
            query_text = self._dict_to_text(query)
            
            # Transform query using the vectorizer
            query_vector = self.vectorizer.transform([query_text])
            
            # Calculate similarities
            similarities = cosine_similarity(query_vector, self.vectors).flatten()
            
            # Get top k similar entries
            top_indices = similarities.argsort()[-top_k:][::-1]
            
            results = []
            for idx in top_indices:
                entry = self.entries[idx]
                results.append({
                    "entry_id": entry.id,
                    "incident_id": entry.incident_id,
                    "similarity_score": float(similarities[idx]),
                    "content": entry.content,
                    "metadata": entry.metadata
                })
            
            return results
        except Exception as e:
            logger.error(f"Error searching similar incidents: {str(e)}")
            return []

    def _dict_to_text(self, data: Dict[str, Any]) -> str:
        # Convert dictionary to text representation for vectorization
        text_parts = []
        for key, value in data.items():
            if isinstance(value, (str, int, float)):
                text_parts.append(f"{key}: {value}")
            elif isinstance(value, dict):
                text_parts.append(f"{key}: {self._dict_to_text(value)}")
            elif isinstance(value, list):
                text_parts.append(f"{key}: {' '.join(str(item) for item in value)}")
        return " ".join(text_parts)

    def _update_vectors(self):
        try:
            # Convert all entries to text
            texts = [self._dict_to_text(entry.content) for entry in self.entries]
            
            # Fit and transform using TF-IDF
            if texts:
                self.vectors = self.vectorizer.fit_transform(texts)
            else:
                self.vectors = None
        except Exception as e:
            logger.error(f"Error updating vectors: {str(e)}")
            self.vectors = None

    def get_statistics(self) -> Dict[str, Any]:
        return {
            "total_entries": len(self.entries),
            "last_updated": datetime.utcnow().isoformat(),
            "categories": self._get_categories(),
            "top_incidents": self._get_top_incidents()
        }

    def _get_categories(self) -> Dict[str, int]:
        categories = {}
        for entry in self.entries:
            category = entry.metadata.get("category", "unknown")
            categories[category] = categories.get(category, 0) + 1
        return categories

    def _get_top_incidents(self, top_k: int = 5) -> List[Dict[str, Any]]:
        # Sort entries by update time and get top k
        sorted_entries = sorted(self.entries, key=lambda x: x.updated_at, reverse=True)
        return [
            {
                "entry_id": entry.id,
                "incident_id": entry.incident_id,
                "updated_at": entry.updated_at.isoformat(),
                "category": entry.metadata.get("category", "unknown")
            }
            for entry in sorted_entries[:top_k]
        ] 