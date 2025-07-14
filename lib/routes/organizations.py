"""
This module defines the routes for the organizations API.

They are imported by the main app.py file and wrapped with Flask routing decorators.
"""
from typing import Tuple

from flask import Response, jsonify, request
import asyncio

from lib.models.organization import Organization, create_organization
from lib.db.surreal import DbController


def get_organizations_route() -> Tuple[Response, int]:
    """
    Return a list of all organizations as JSON.
    """
    db = DbController()
    db.connect()
    try:
        results = db.select_many('organization')
        # Handle result structure
        if results and len(results) > 0:
            if 'result' in results[0]:
                orgs = results[0]['result']
            else:
                orgs = results
            orgs_list = [Organization.from_dict(org).to_dict() for org in orgs]
        else:
            orgs_list = []
        return jsonify({'organizations': orgs_list}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def create_organization_route() -> Tuple[Response, int]:
    """
    API endpoint to create a new organization.
    Accepts JSON body with: name, org_type, created_by, (optional) description.
    Returns the created organization or error.
    """
    if request.method != 'POST':
        return jsonify({"error": "Method not allowed"}), 405

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get('name')
    org_type = data.get('org_type')
    created_by = data.get('created_by')
    description = data.get('description', "")

    if not all([name, org_type, created_by]):
        return jsonify({"error": "Missing required fields: name, org_type, created_by"}), 400

    org = Organization(
        name=name,
        org_type=org_type,
        created_by=created_by,
        description=description
    )

    try:
        org_id = asyncio.run(create_organization(org))
        if org_id:
            org.id = org_id
            return jsonify({"organization": org.to_dict(), "id": org_id}), 201
        else:
            return jsonify({"error": "Failed to create organization"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_organization_route(org_id: str) -> Tuple[Response, int]:
    """
    Update an existing organization by its ID.
    Accepts JSON body with updated fields.
    Returns the updated organization or error.
    """
    if request.method != 'PUT':
        return jsonify({"error": "Method not allowed"}), 405
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    db = DbController()
    db.connect()
    try:
        # Fetch existing org
        org_data = db.select(f'organization:{org_id}')
        if not org_data:
            return jsonify({"error": "Organization not found"}), 404
        org = Organization.from_dict(org_data)
        # Update fields
        for key in ['name', 'org_type', 'description']:
            if key in data:
                setattr(org, key, data[key])
        # Save updated org
        update_data = org.to_dict()
        db.update(f'organization:{org_id}', update_data)
        return jsonify({"organization": org.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()


