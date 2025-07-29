"""
Migration script to update user organization limits.

This script provides utilities to easily update the max_organizations field
for users in the database. This allows for easy configuration of organization
limits without code changes.

Usage:
    python -m lib.migrations.update_org_limits
"""
from typing import Optional

from lib.db.surreal import DbController
from lib.models.user.user import User
from settings import logger


def update_user_org_limit(user_id: str, new_limit: int) -> bool:
    """
    Update a specific user's organization limit.
    
    :param user_id: The user ID to update
    :param new_limit: New maximum number of organizations allowed
    :return: True if successful, False otherwise
    """
    db = DbController()
    db.connect()
    try:
        # Fetch current user data
        user_data = db.select(f'user:{user_id}')
        if not user_data:
            logger.error(f"User {user_id} not found")
            return False
        
        # Create user object and update limit
        user = User.from_dict(user_data)
        user.max_organizations = new_limit
        
        # Save updated user
        update_data = user.to_dict()
        db.update(f'user:{user_id}', update_data)
        
        logger.info(f"Updated user {user_id} organization limit to {new_limit}")
        return True
        
    except Exception as e:
        logger.error(f"Error updating user {user_id}: {e}")
        return False
    finally:
        db.close()


def bulk_update_org_limits(new_limit: int, role_filter: Optional[str] = None) -> dict:
    """
    Bulk update organization limits for multiple users.
    
    :param new_limit: New maximum number of organizations allowed
    :param role_filter: Optional role filter (e.g., 'admin', 'provider', 'patient')
    :return: Dictionary with results
    """
    db = DbController()
    db.connect()
    try:
        # Build query based on role filter
        if role_filter:
            query = f"SELECT * FROM user WHERE role = '{role_filter}';"
        else:
            query = "SELECT * FROM user;"
        
        result = db.query(query)
        
        if not result or len(result) == 0:
            logger.warning("No users found")
            return {"success": 0, "failed": 0, "total": 0}
        
        # Process results
        users_data = result[0].get('result', []) if 'result' in result[0] else result
        
        success_count = 0
        failed_count = 0
        
        for user_data in users_data:
            try:
                user = User.from_dict(user_data)
                user.max_organizations = new_limit
                
                update_data = user.to_dict()
                db.update(f"user:{user.id}", update_data)
                
                logger.info(f"Updated user {user.username} ({user.id}) organization limit to {new_limit}")
                success_count += 1
                
            except Exception as e:
                logger.error(f"Failed to update user {user_data.get('username', 'unknown')}: {e}")
                failed_count += 1
        
        total = success_count + failed_count
        logger.info(f"Bulk update complete: {success_count} successful, {failed_count} failed out of {total} total")
        
        return {
            "success": success_count,
            "failed": failed_count,
            "total": total
        }
        
    except Exception as e:
        logger.error(f"Error in bulk update: {e}")
        return {"success": 0, "failed": 0, "total": 0, "error": str(e)}
    finally:
        db.close()


def get_user_org_info(user_id: Optional[str] = None) -> dict:
    """
    Get organization limit information for users.
    
    :param user_id: Optional specific user ID, if None returns all users
    :return: Dictionary with user organization information
    """
    db = DbController()
    db.connect()
    try:
        if user_id:
            # Get specific user
            user_data = db.select(f'user:{user_id}')
            if not user_data:
                return {"error": f"User {user_id} not found"}
            
            user = User.from_dict(user_data)
            return {
                "user_id": user.id,
                "username": user.username,
                "role": user.role,
                "max_organizations": user.max_organizations,
                "user_organizations": user.user_organizations,
                "remaining_slots": user.get_remaining_organization_slots()
            }
        else:
            # Get all users
            result = db.query("SELECT * FROM user;")
            
            if not result or len(result) == 0:
                return {"users": []}
            
            users_data = result[0].get('result', []) if 'result' in result[0] else result
            users_info = []
            
            for user_data in users_data:
                try:
                    user = User.from_dict(user_data)
                    users_info.append({
                        "user_id": user.id,
                        "username": user.username,
                        "role": user.role,
                        "max_organizations": user.max_organizations,
                        "user_organizations": user.user_organizations,
                        "remaining_slots": user.get_remaining_organization_slots()
                    })
                except Exception as e:
                    logger.error(f"Error processing user data: {e}")
            
            return {"users": users_info}
            
    except Exception as e:
        logger.error(f"Error getting user org info: {e}")
        return {"error": str(e)}
    finally:
        db.close()


if __name__ == "__main__":
    """
    Example usage of the migration functions.
    Uncomment and modify as needed.
    """
    
    # Example 1: Update a specific user's limit
    # success = update_user_org_limit("User:abc123", 5)
    # print(f"Update specific user: {'Success' if success else 'Failed'}")
    
    # Example 2: Bulk update all admin users to allow 10 organizations
    # results = bulk_update_org_limits(10, "admin")
    # print(f"Bulk update results: {results}")
    
    # Example 3: Get organization info for all users
    # info = get_user_org_info()
    # print(f"User organization info: {info}")
    
    print("Organization limit migration utilities loaded.")
    print("Use the functions in this module to update user organization limits.")
    print("\nAvailable functions:")
    print("- update_user_org_limit(user_id, new_limit)")
    print("- bulk_update_org_limits(new_limit, role_filter)")
    print("- get_user_org_info(user_id)") 