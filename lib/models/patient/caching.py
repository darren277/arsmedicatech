"""
Caching module for entity extraction results in SurrealDB.
"""
import datetime
from typing import Any, Dict, List, Optional, Union

from lib.db.surreal import AsyncDbController, DbController
from settings import logger


def store_entity_cache(db: Union[DbController, AsyncDbController], text_hash: str, entities: List[Dict[str, Any]], note_type: str = 'text') -> bool:
    """
    Store entity extraction results in SurrealDB for caching.
    
    :param db: DbController instance connected to SurrealDB.
    :param text_hash: SHA256 hash of the original text for cache key
    :param entities: List of extracted entities (without position data)
    :param note_type: Type of note (soap or text)
    :return: True if successful, False otherwise
    """
    try:
        # Remove position data for storage (keep only the essential entity info)
        entities_for_storage = []
        for entity in entities:
            entity_copy = {
                "text": entity.get("text", ""),
                "label": entity.get("label", ""),
                "cui": entity.get("cui"),
                "icd10cm": entity.get("icd10cm"),
                "icd10cm_name": entity.get("icd10cm_name")
            }
            entities_for_storage.append(entity_copy)
        
        cache_data = {
            "text_hash": text_hash,
            "entities": entities_for_storage,
            "note_type": note_type,
            "created_at": datetime.datetime.utcnow().isoformat(),
            "entity_count": len(entities_for_storage)
        }
        
        # Store in SurrealDB
        result = db.query(
            "CREATE entity_cache CONTENT $cache_data",
            {"cache_data": cache_data}
        )
        
        logger.debug(f"Stored entity cache for hash: {text_hash}")
        return True
        
    except Exception as e:
        logger.error(f"Error storing entity cache: {e}")
        return False


def get_entity_cache(db: Union[DbController, AsyncDbController], text_hash: str) -> Optional[Dict[str, Any]]:
    """
    Retrieve entity extraction results from SurrealDB cache.
    
    :param db: DbController instance connected to SurrealDB
    :param text_hash: SHA256 hash of the original text
    :return: Cached entity data if found, None otherwise
    """
    if isinstance(db, AsyncDbController):
        logger.error("AsyncDbController not supported for get_entity_cache")
        return None
    try:
        result = db.query(
            "SELECT * FROM entity_cache WHERE text_hash = $text_hash LIMIT 1",
            {"text_hash": text_hash}
        )
        
        if result and len(result) > 0 and result[0].get("result"):
            cache_data = result[0]["result"][0]
            logger.debug(f"Retrieved entity cache for hash: {text_hash}")
            return cache_data
        
        return None
        
    except Exception as e:
        logger.error(f"Error retrieving entity cache: {e}")
        return None


def create_text_hash(text: str) -> str:
    """
    Create a SHA256 hash of the text for cache key.
    
    :param text: Text to hash
    :return: SHA256 hash string
    """
    import hashlib
    return hashlib.sha256(text.encode('utf-8')).hexdigest()
