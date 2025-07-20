"""
Cache service for managing entity extraction results.
"""
from typing import Any, Dict, List, Optional, Union

from lib.db.surreal import AsyncDbController, DbController
from lib.models.patient import (create_text_hash, get_entity_cache,
                                store_entity_cache)
from settings import logger


class EntityCacheService:
    """
    Service for managing entity extraction cache.
    """
    
    @staticmethod
    def get_cached_entities(db: Union[DbController, AsyncDbController], text: str) -> Optional[Dict[str, Any]]:
        """
        Get cached entities for a given text.
        
        :param db: Database controller instance
        :param text: The text to look up in cache
        :return: Cached entity data if found, None otherwise
        """
        text_hash = create_text_hash(text)
        return get_entity_cache(db, text_hash)
    
    @staticmethod
    def store_entities(db: Union[DbController, AsyncDbController], text: str, entities: List[Dict[str, Any]], note_type: str = 'text') -> bool:
        """
        Store entities in cache for a given text.
        
        :param db: Database controller instance
        :param text: The original text
        :param entities: List of entities to cache
        :param note_type: Type of note (soap or text)
        :return: True if successful, False otherwise
        """
        text_hash = create_text_hash(text)
        return store_entity_cache(db, text_hash, entities, note_type)
    
    @staticmethod
    def is_cached(db: Union[DbController, AsyncDbController], text: str) -> bool:
        """
        Check if entities for a given text are cached.
        
        :param db: Database controller instance
        :param text: The text to check
        :return: True if cached, False otherwise
        """
        return get_entity_cache(db, create_text_hash(text)) is not None
    
    @staticmethod
    def get_cache_stats(db: Union[DbController, AsyncDbController]) -> Dict[str, Any]:
        """
        Get cache statistics.
        
        :param db: Database controller instance
        :return: Dictionary with cache statistics
        """
        if isinstance(db, AsyncDbController):
            logger.error("AsyncDbController not supported for get_entity_cache")
            raise NotImplementedError("AsyncDbController not supported for get_entity_cache")
        try:
            result = db.query("SELECT count() as total FROM entity_cache")
            if result and len(result) > 0 and result[0].get("result"):
                total_count = result[0]["result"][0].get("total", 0)
                return {
                    "total_cached_entities": total_count,
                    "cache_enabled": True
                }
        except Exception as e:
            logger.error(f"Error getting cache stats: {e}")
        
        return {
            "total_cached_entities": 0,
            "cache_enabled": False
        } 