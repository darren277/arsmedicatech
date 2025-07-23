from flask import g, jsonify

from lib.db.surreal import DbController
from lib.services.admin_service import AdminService
from lib.services.auth_decorators import require_auth

# Helper to get AdminService instance

def get_admin_service():
    db = DbController()
    return AdminService(db)

@require_auth
def get_organizations_route():
    # Only allow admin or superadmin
    if getattr(g, 'user_role', None) not in ('admin', 'superadmin'):
        return jsonify({"error": "Unauthorized"}), 403
    service = get_admin_service()
    orgs = service.get_organizations()
    return jsonify([o.to_dict() for o in orgs])

@require_auth
def get_clinics_route():
    if getattr(g, 'user_role', None) not in ('admin', 'superadmin'):
        return jsonify({"error": "Unauthorized"}), 403
    service = get_admin_service()
    import asyncio
    clinics = asyncio.run(service.get_clinics())
    return jsonify(clinics)

@require_auth
def get_patients_route():
    if getattr(g, 'user_role', None) not in ('admin', 'superadmin'):
        return jsonify({"error": "Unauthorized"}), 403
    service = get_admin_service()
    patients = service.get_patients()
    return jsonify(patients)

@require_auth
def get_providers_route():
    if getattr(g, 'user_role', None) not in ('admin', 'superadmin'):
        return jsonify({"error": "Unauthorized"}), 403
    service = get_admin_service()
    providers = service.get_providers()
    return jsonify(providers)

@require_auth
def get_administrators_route():
    if getattr(g, 'user_role', None) not in ('admin', 'superadmin'):
        return jsonify({"error": "Unauthorized"}), 403
    service = get_admin_service()
    admins = service.get_administrators()
    return jsonify(admins) 