"""
Administration service.
This service is for administration level users to pull (and in some times, modify) data from the various different models in the database.
"""

from typing import List, Union

from lib.db.surreal import AsyncDbController, DbController
from lib.models.clinic import get_all_clinics
from lib.models.organization import Organization
from lib.models.patient.patient_crud import get_all_patients
from lib.services.user_service import UserService


class AdminService:
    def __init__(self, db: Union[DbController, AsyncDbController]) -> None:
        """
        Initialize the AdminService.
        :param db: The database controller to use.
        :type db: Union[DbController, AsyncDbController]
        :return: None
        """
        self.db = db

    def get_organizations(self) -> List[Organization]:
        """
        Fetch all organizations from the database.
        """
        # If you have a function to fetch all organizations, use it here.
        # For now, do a direct query using DbController.
        self.db.connect()
        results = self.db.select_many('organization')
        orgs: List[Organization] = []
        for org_data in results:
            orgs.append(Organization.from_dict(org_data))
        return orgs

    async def get_clinics(self) -> List[dict]:
        """
        Fetch all clinics from the database (async).
        """
        return await get_all_clinics()

    def get_patients(self) -> List[dict]:
        """
        Fetch all patients from the database.
        """
        return get_all_patients()

    def get_providers(self) -> List[dict]:
        """
        Fetch all users with role 'provider'.
        """
        user_service = UserService(self.db)
        user_service.connect()
        users = user_service.get_all_users()
        providers = [u.to_dict() for u in users if getattr(u, 'role', None) == 'provider']
        return providers

    def get_administrators(self) -> List[dict]:
        """
        Fetch all users with role 'admin'.
        """
        user_service = UserService(self.db)
        user_service.connect()
        users = user_service.get_all_users()
        admins = [u.to_dict() for u in users if getattr(u, 'role', None) == 'admin']
        return admins