"""
Migration script to update existing clinics and organizations with new fields.

This script:
1. Adds country field to existing clinics (defaults to "USA")
2. Adds country and clinic_ids fields to existing organizations
3. Updates the database schema for new fields
"""

import os
import sys

# Add the parent directory to the path so we can import lib modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.db.surreal import DbController
from settings import logger


def update_clinics_with_country():
    """Add country field to existing clinics."""
    db = DbController()
    db.connect()
    
    try:
        # Get all existing clinics
        clinics = db.select_many('clinic')
        logger.info(f"Found {len(clinics) if clinics else 0} clinics to update")
        
        if not clinics:
            logger.info("No clinics found to update")
            return
        
        updated_count = 0
        for clinic in clinics:
            clinic_id = clinic.get('id')
            if not clinic_id:
                continue
                
            # Check if clinic already has country field
            if 'address' in clinic and 'country' in clinic['address']:
                logger.debug(f"Clinic {clinic_id} already has country field")
                continue
            
            # Add country field to address
            if 'address' not in clinic:
                clinic['address'] = {}
            
            clinic['address']['country'] = 'USA'  # Default country
            
            # Update the clinic
            db.update(f'clinic:{clinic_id}', clinic)
            updated_count += 1
            logger.info(f"Updated clinic {clinic_id} with country field")
        
        logger.info(f"Successfully updated {updated_count} clinics with country field")
        
    except Exception as e:
        logger.error(f"Error updating clinics: {e}")
        raise
    finally:
        db.close()


def update_organizations_with_new_fields():
    """Add country and clinic_ids fields to existing organizations."""
    db = DbController()
    db.connect()
    
    try:
        # Get all existing organizations
        organizations = db.select_many('organization')
        logger.info(f"Found {len(organizations) if organizations else 0} organizations to update")
        
        if not organizations:
            logger.info("No organizations found to update")
            return
        
        updated_count = 0
        for org in organizations:
            org_id = org.get('id')
            if not org_id:
                continue
            
            # Check if organization already has new fields
            has_country = 'country' in org
            has_clinic_ids = 'clinic_ids' in org
            
            if has_country and has_clinic_ids:
                logger.debug(f"Organization {org_id} already has new fields")
                continue
            
            # Add missing fields
            if not has_country:
                org['country'] = ''  # Default empty country
            
            if not has_clinic_ids:
                org['clinic_ids'] = []  # Default empty clinic list
            
            # Update the organization
            db.update(f'organization:{org_id}', org)
            updated_count += 1
            logger.info(f"Updated organization {org_id} with new fields")
        
        logger.info(f"Successfully updated {updated_count} organizations with new fields")
        
    except Exception as e:
        logger.error(f"Error updating organizations: {e}")
        raise
    finally:
        db.close()


def run_migration():
    """Run the complete migration."""
    logger.info("Starting clinic and organization field migration...")
    
    try:
        # Update clinics first
        logger.info("Step 1: Updating clinics with country field...")
        update_clinics_with_country()
        
        # Update organizations
        logger.info("Step 2: Updating organizations with new fields...")
        update_organizations_with_new_fields()
        
        logger.info("Migration completed successfully!")
        
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    run_migration() 