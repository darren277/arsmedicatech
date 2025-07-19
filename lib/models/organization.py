"""
This module defines a Organization class and provides functions to interact with a SurrealDB database.
"""
import json
from datetime import datetime, timezone
from typing import Any, Dict, Optional

from surrealdb import Surreal  # type: ignore

from lib.db.surreal import DbController
from settings import logger


class Organization:
    """
    Represents an organization in the system.
    """
    def __init__(
        self,
        name: str,
        org_type: str,  # e.g., 'individual', 'provider', 'admin'
        created_by: str,  # user id
        created_at: Optional[str] = None,
        id: Optional[str] = None,
        description: Optional[str] = None,
        country: Optional[str] = None,
        clinic_ids: Optional[list[str]] = None,
    ) -> None:
        self.name = name
        self.org_type = org_type
        self.created_by = created_by
        self.created_at = created_at or datetime.now(timezone.utc).isoformat()
        self.id = id
        self.description = description or ""
        self.country = country or ""
        self.clinic_ids = clinic_ids or []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": str(self.id) if self.id else None,
            "name": self.name,
            "org_type": self.org_type,
            "created_by": self.created_by,
            "created_at": self.created_at,
            "description": self.description,
            "country": self.country,
            "clinic_ids": self.clinic_ids,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Organization":
        # Handle RecordID objects from SurrealDB
        org_id = data.get("id")
        if org_id is not None:
            # Convert RecordID to string if it's not already a string
            if hasattr(org_id, '__str__'):
                org_id = str(org_id)
        
        return cls(
            name=data.get("name", ""),
            org_type=data.get("org_type", ""),
            created_by=data.get("created_by", ""),
            created_at=data.get("created_at"),
            id=org_id,
            description=data.get("description", ""),
            country=data.get("country", ""),
            clinic_ids=data.get("clinic_ids", []),
        )

def generate_surrealql_create_query(org: Organization, table_name: str = "organization") -> str:
    data_to_set = org.to_dict()
    # Remove id if present, so SurrealDB generates it
    data_to_set.pop("id", None)
    set_clause = json.dumps(data_to_set, indent=4)
    query = f"CREATE {table_name} CONTENT {set_clause};"
    return query

def create_organization(org: Organization) -> Optional[str]:
    """
    Create an organization in the database using DbController.
    """
    db = DbController()
    db.connect()
    try:
        query = generate_surrealql_create_query(org)
        result = db.query(query)
        logger.debug('Organization create result type:', type(result))
        logger.debug('Organization create result:', result)
        
        # Handle the query result structure
        if result and len(result) > 0:
            first_result = result[0]
            logger.debug('First result type:', type(first_result))
            logger.debug('First result:', first_result)
            
            # Check if result has a 'result' key (common in SurrealDB responses)
            if 'result' in first_result:
                logger.debug('Found result key in first_result')
                if first_result['result'] and len(first_result['result']) > 0:
                    created_record = first_result['result'][0]
                    logger.debug('Created record:', created_record)
                    if 'id' in created_record:
                        logger.debug('Found id in created_record:', created_record['id'])
                        return str(created_record['id'])
            # If no 'result' key, check if the first result has an 'id'
            elif 'id' in first_result:
                logger.debug('Found id directly in first_result:', first_result['id'])
                return str(first_result['id'])
            else:
                logger.debug('No result or id keys found in first_result')
        else:
            logger.debug('No result or empty result list')
        
        logger.warning("No valid result found in query response")
        return None
    except Exception as e:
        logger.error(f"Error creating organization: {e}")
        raise
    finally:
        db.close()
