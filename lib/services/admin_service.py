"""
Administration service.
This service is for administration level users to pull (and in some times, modify) data from the various different models in the database.
"""
from typing import Any, Dict, List, Union

from lib.db.surreal import AsyncDbController, DbController
from lib.models.clinic import Clinic, ClinicType
from lib.models.organization import Organization
from lib.services.user_service import UserService


class AdminService:
    """
    AdminService provides methods to manage and retrieve data for administrative purposes.
    """
    def __init__(self, db: Union[DbController, AsyncDbController]) -> None:
        """
        Initialize the AdminService.
        :param db: The database controller to use.
        :type db: Union[DbController, AsyncDbController]
        :return: None
        """
        self.db = db

        if isinstance(self.db, AsyncDbController):
            raise TypeError("Async not yet supported in AdminService")

    def get_organizations(self) -> List[Organization]:
        """
        Fetch all organizations from the database.
        """
        # If you have a function to fetch all organizations, use it here.
        # For now, do a direct query using DbController.
        if isinstance(self.db, AsyncDbController):
            raise TypeError("Async not yet supported in AdminService")

        self.db.connect()
        results = self.db.select_many('organization')
        orgs: List[Organization] = []
        for org_data in results:
            orgs.append(Organization.from_dict(org_data))
        return orgs

    def get_clinics(self, organization_id: str) -> List[ClinicType]:
        """
        Fetch all clinics for a specific organization from the database.
        """
        if isinstance(self.db, AsyncDbController):
            raise TypeError("Async not yet supported in AdminService")

        self.db.connect()
        # Query clinics with organization_id
        query = "SELECT * FROM clinic WHERE organization_id = $organization_id"
        params = {"organization_id": organization_id}
        results = self.db.query(query, params)
        clinics: List[ClinicType] = []
        # Handle SurrealDB result structure
        if results and len(results) > 0:
            if 'result' in results[0]:
                clinic_data_list = results[0]['result']
            else:
                clinic_data_list = results
            for clinic_data in clinic_data_list:
                clinics.append(Clinic.from_db(clinic_data).to_dict())
        return clinics

    def get_patients(self, organization_id: str) -> List[Dict[str, Any]]:
        """
        Fetch all patients for a specific organization from the database.
        """
        self.db.connect()
        query = "SELECT * FROM patient WHERE organization_id = $organization_id"
        params = {"organization_id": organization_id}
        results = self.db.query(query, params)
        patients: List[Dict[str, Any]] = []
        # If results is a coroutine, resolve it
        import asyncio
        if asyncio.iscoroutine(results):
            results = asyncio.run(results)
        if results and len(results) > 0:
            if 'result' in results[0]:
                patient_data_list = results[0]['result']
            else:
                patient_data_list = results
            for patient_data in patient_data_list:
                patients.append(patient_data)
        return patients

    def get_providers(self, organization_id: str) -> List[Dict[str, Any]]:
        """
        Fetch all users with role 'provider' for a specific organization.
        """
        if isinstance(self.db, AsyncDbController):
            raise TypeError("Async not yet supported in AdminService")

        self.db.connect()
        user_service = UserService(self.db)
        user_service.connect()
        users = user_service.get_all_users()
        providers = [u.to_dict() for u in users if getattr(u, 'role', None) == 'provider' and getattr(u, 'organization_id', None) == organization_id]
        return providers

    def get_administrators(self, organization_id: str) -> List[Dict[str, Any]]:
        """
        Fetch all users with role 'admin' for a specific organization.
        """
        if isinstance(self.db, AsyncDbController):
            raise TypeError("Async not yet supported in AdminService")

        self.db.connect()
        user_service = UserService(self.db)
        user_service.connect()
        users = user_service.get_all_users()
        admins = [u.to_dict() for u in users if getattr(u, 'role', None) == 'admin' and getattr(u, 'organization_id', None) == organization_id]
        return admins