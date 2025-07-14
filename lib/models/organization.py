"""
This module defines a Organization class and provides functions to interact with a SurrealDB database.
"""
import json
from typing import Any, Dict, Optional

from surrealdb import Surreal  # type: ignore

from lib.db.surreal import AsyncDbController
from settings import logger
from datetime import datetime, timezone

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
    ) -> None:
        self.name = name
        self.org_type = org_type
        self.created_by = created_by
        self.created_at = created_at or datetime.now(timezone.utc).isoformat()
        self.id = id
        self.description = description or ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "org_type": self.org_type,
            "created_by": self.created_by,
            "created_at": self.created_at,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Organization":
        org_id = data.get("id")
        if hasattr(org_id, "__str__"):
            org_id = str(org_id)
        return cls(
            name=data.get("name", ""),
            org_type=data.get("org_type", ""),
            created_by=data.get("created_by", ""),
            created_at=data.get("created_at"),
            id=org_id,
            description=data.get("description", ""),
        )

def generate_surrealql_create_query(org: Organization, table_name: str = "organization") -> str:
    data_to_set = org.to_dict()
    set_clause = json.dumps(data_to_set, indent=4)
    record_id = org.name.lower().replace(" ", "_").replace("'", "")
    query = f"CREATE {table_name}:{record_id} CONTENT {set_clause};"
    return query

client = AsyncDbController()

async def create_organization(org: Organization) -> Optional[str]:
    query = generate_surrealql_create_query(org)
    result = await client.query(query)
    logger.debug('Organization create result', type(result), result)
    return result[0]['id'] if result else None
