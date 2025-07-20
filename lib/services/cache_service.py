"""
Cache service for managing entity extraction results.
"""
from typing import Any, Dict, List, Optional, Union

from lib.db.surreal import AsyncDbController, DbController
from lib.models.patient.caching import (create_text_hash, get_entity_cache,
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
    def get_cached_entity(db: Union[DbController, AsyncDbController], entity_text: str, entity_type: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Get cached individual entity by text and type.
        
        :param db: Database controller instance
        :param entity_text: The entity text to look up
        :param entity_type: The entity type (optional, for more specific lookup)
        :return: Cached entity data if found, None otherwise
        """
        try:
            if isinstance(db, AsyncDbController):
                logger.error("AsyncDbController not supported for individual entity cache")
                return None
                
            # Create a hash for the entity text
            entity_hash = create_text_hash(entity_text.lower().strip())
            
            # Build query based on whether entity_type is provided
            if entity_type:
                query = "SELECT * FROM entity_cache WHERE entity_hash = $entity_hash AND entity_type = $entity_type LIMIT 1"
                result = db.query(query, {"entity_hash": entity_hash, "entity_type": entity_type})
            else:
                query = "SELECT * FROM entity_cache WHERE entity_hash = $entity_hash LIMIT 1"
                result = db.query(query, {"entity_hash": entity_hash})
            
            if result and len(result) > 0 and result[0].get("result"):
                return result[0]["result"][0]
            return None
            
        except Exception as e:
            logger.error(f"Error getting cached entity: {e}")
            return None
    
    @staticmethod
    def store_individual_entity(db: Union[DbController, AsyncDbController], entity_text: str, entity_data: Dict[str, Any], entity_type: Optional[str] = None) -> bool:
        """
        Store individual entity in cache.
        
        :param db: Database controller instance
        :param entity_text: The entity text
        :param entity_data: The entity data to cache
        :param entity_type: The entity type (optional)
        :return: True if successful, False otherwise
        """
        try:
            if isinstance(db, AsyncDbController):
                logger.error("AsyncDbController not supported for individual entity cache")
                return False
                
            # Create a hash for the entity text
            entity_hash = create_text_hash(entity_text.lower().strip())
            
            # Prepare the data to store
            cache_data: Dict[str, Any] = {
                "entity_hash": entity_hash,
                "entity_text": entity_text,
                "entity_data": entity_data,
                "cached_at": "now()"  # Use SurrealDB's now() function
            }
            
            # Add entity_type if provided
            if entity_type:
                cache_data["entity_type"] = entity_type
            
            # Store in database
            result = db.create("entity_cache", cache_data)
            return bool(result)
            
        except Exception as e:
            logger.error(f"Error storing individual entity: {e}")
            return False
    
    @staticmethod
    def get_or_cache_entity(db: Union[DbController, AsyncDbController], entity_text: str, entity_data: Dict[str, Any], entity_type: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Get cached entity or store it if not found.
        
        :param db: Database controller instance
        :param entity_text: The entity text
        :param entity_data: The entity data to cache if not found
        :param entity_type: The entity type (optional)
        :return: Cached entity data
        """
        # Try to get from cache first
        cached_entity = EntityCacheService.get_cached_entity(db, entity_text, entity_type)
        if cached_entity:
            return cached_entity.get("entity_data")
        
        # If not found, store it
        if EntityCacheService.store_individual_entity(db, entity_text, entity_data, entity_type):
            return entity_data
        
        return None
    
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
    def is_entity_cached(db: Union[DbController, AsyncDbController], entity_text: str, entity_type: Optional[str] = None) -> bool:
        """
        Check if individual entity is cached.
        
        :param db: Database controller instance
        :param entity_text: The entity text to check
        :param entity_type: The entity type (optional)
        :return: True if cached, False otherwise
        """
        return EntityCacheService.get_cached_entity(db, entity_text, entity_type) is not None
    
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
            # Get total count
            result = db.query("SELECT count() as total FROM entity_cache")
            total_count = 0
            if result and len(result) > 0 and result[0].get("result"):
                total_count = result[0]["result"][0].get("total", 0)
            
            # Get count by type (if entity_type field exists)
            type_stats = {}
            try:
                type_result = db.query("SELECT entity_type, count() as count FROM entity_cache GROUP BY entity_type")
                if type_result and len(type_result) > 0 and type_result[0].get("result"):
                    for item in type_result[0]["result"]:
                        entity_type = item.get("entity_type", "unknown")
                        count = item.get("count", 0)
                        type_stats[entity_type] = count
            except Exception:
                # entity_type field might not exist in older cache entries
                pass
            
            return {
                "total_cached_entities": total_count,
                "cache_enabled": True,
                "by_type": type_stats
            }
        except Exception as e:
            logger.error(f"Error getting cache stats: {e}")
        
        return {
            "total_cached_entities": 0,
            "cache_enabled": False,
            "by_type": {}
        }
