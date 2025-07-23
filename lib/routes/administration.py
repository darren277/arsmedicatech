"""
Administration routes for managing organizations, clinics, patients, providers, and administrators.
"""
from typing import List, Tuple

from flask import Response, g, jsonify

from lib.db.surreal import DbController
from lib.models.clinic import ClinicType
from lib.services.admin_service import AdminService
from lib.services.auth_decorators import require_auth

# Helper to get AdminService instance

def get_admin_service() -> AdminService:
    """
    Get an instance of AdminService.
    :return: AdminService instance
    """
    db = DbController()
    return AdminService(db)

@require_auth
def get_organizations_route() -> Tuple[Response, int]:
    """
    Route to get all organizations.
    :return: Tuple containing JSON response and HTTP status code
    """
    # Only allow admin or superadmin
    if getattr(g, 'user_role', None) not in ('admin', 'superadmin'):
        return jsonify({"error": "Unauthorized"}), 403
    service = get_admin_service()
    orgs = service.get_organizations()
    return jsonify([o.to_dict() for o in orgs]), 200

@require_auth
def get_clinics_route(organization_id: str) -> Tuple[Response, int]:
    """
    Route to get all clinics.
    :return: Tuple containing JSON response and HTTP status code
    """
    if getattr(g, 'user_role', None) not in ('admin', 'administrator', 'superadmin'):
        return jsonify({"error": "Unauthorized"}), 403
    service = get_admin_service()
    clinics: List[ClinicType] = service.get_clinics(organization_id)
    return jsonify(clinics), 200

@require_auth
def get_patients_route(organization_id: str) -> Tuple[Response, int]:
    """
    Route to get all patients.
    :return: Tuple containing JSON response and HTTP status code
    """
    if getattr(g, 'user_role', None) not in ('admin', 'administrator', 'superadmin'):
        return jsonify({"error": "Unauthorized"}), 403
    service = get_admin_service()
    patients = service.get_patients(organization_id)
    return jsonify(patients), 200

@require_auth
def get_providers_route(organization_id: str) -> Tuple[Response, int]:
    """
    Route to get all providers.
    :return: Tuple containing JSON response and HTTP status code
    """
    if getattr(g, 'user_role', None) not in ('admin', 'administrator', 'superadmin'):
        return jsonify({"error": "Unauthorized"}), 403
    service = get_admin_service()
    providers = service.get_providers(organization_id)
    return jsonify(providers), 200

@require_auth
def get_administrators_route(organization_id: str) -> Tuple[Response, int]:
    """
    Route to get all administrators.
    :return: Tuple containing JSON response and HTTP status code
    """
    if getattr(g, 'user_role', None) not in ('admin', 'administrator', 'superadmin'):
        return jsonify({"error": "Unauthorized"}), 403
    service = get_admin_service()
    admins = service.get_administrators(organization_id)
    return jsonify(admins), 200