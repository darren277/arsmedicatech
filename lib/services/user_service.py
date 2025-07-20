"""
User Service for managing user accounts, authentication, and settings.
"""
from typing import Any, Dict, List, Optional

from lib.db.surreal import DbController
from lib.models.user import User, UserSession
from lib.models.user_settings import UserSettings
from settings import logger


class UserService:
    """
    Service for managing user accounts, authentication, and settings.
    """
    def __init__(self, db_controller: Optional[DbController] = None) -> None:
        """
        Initialize UserService with a database controller.
        :param db_controller: Optional DbController instance. If None, a default DbController will be used.
        :type db_controller: DbController
        :return: None
        """
        self.db = db_controller or DbController()
        self.active_sessions: Dict[str, UserSession] = {}
    
    def connect(self) -> None:
        """
        Connect to database
        This method attempts to connect to the database using the provided DbController.
        If the DbController does not have a connect method, it will log a message and continue in mock mode.
        :return: None
        """
        logger.debug("Connecting to database...")
        try:
            logger.debug(f"Database controller type: {type(self.db)}")
            logger.debug(f"Database controller has connect method: {hasattr(self.db, 'connect')}")
            
            if hasattr(self.db, 'connect'):
                self.db.connect()
                logger.debug("Database connection successful")
            else:
                logger.debug("Database controller does not have connect method - using mock mode")
        except Exception as e:
            logger.debug(f"Database connection error: {e}")
            logger.debug("Continuing with mock database mode")
            # Don't raise the exception, continue with mock mode
    
    def close(self) -> None:
        """
        Close database connection
        This method attempts to close the database connection using the provided DbController.
        If the DbController does not have a close method, it will log a message and continue in mock mode.
        :return: None
        """
        self.db.close()
    
    def create_user(
            self,
            username: str,
            email: str,
            password: str,
            first_name: Optional[str] = None,
            last_name: Optional[str] = None,
            role: str = "patient"
    ) -> tuple[bool, str, Optional[User]]:
        """
        Create a new user account

        :param username: Username for the new user
        :param email: Email address for the new user
        :param password: Password for the new user
        :param first_name: First name of the user (optional)
        :param last_name: Last name of the user (optional)
        :param role: Role of the user (default is "patient")
        
        :return: (success, message, user_object)
        """
        try:
            # Validate input
            valid, msg = User.validate_username(username)
            if not valid:
                return False, msg, None
            
            valid, msg = User.validate_email(email)
            if not valid:
                return False, msg, None
            
            valid, msg = User.validate_password(password)
            if not valid:
                return False, msg, None
            
            # Check if username already exists
            existing_user = self.get_user_by_username(username)
            if existing_user:
                return False, "Username already exists", None
            
            # Check if email already exists
            existing_user = self.get_user_by_email(email)
            if existing_user:
                return False, "Email already exists", None
            
            # Create user
            user = User(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                role=role
            )
            
            # Save to database
            logger.debug(f"Creating user with data: {user.to_dict()}")
            
            result = self.db.create('User', user.to_dict())
            logger.debug(f"Database create result: {result}")
            logger.debug(f"Database create result type: {type(result)}")
            if result and result.get('id'):
                user.id = result['id']
                logger.debug(f"User created successfully with ID: {user.id}")
                logger.debug(f"User ID type: {type(user.id)}")
                
                # Test if we can immediately retrieve the user
                logger.debug(f"Testing immediate user retrieval...")
                test_user = self.get_user_by_id(user.id)
                if test_user:
                    logger.debug(f"User can be retrieved immediately: {test_user.username}")
                else:
                    logger.debug(f"User cannot be retrieved immediately")
                
                # If the user is a patient, create a corresponding Patient record
                if user.role == "patient" and user.id:
                    try:
                        from lib.models.patient.patient_crud import \
                            create_patient
                        user_id = str(user.id)
                        if ':' in user_id:
                            patient_id = user_id.split(':', 1)[1]
                        else:
                            patient_id = user_id
                        patient_data: Dict[str, Any] = {
                            "demographic_no": patient_id,
                            "first_name": user.first_name,
                            "last_name": user.last_name,
                            "email": user.email,
                            "date_of_birth": "",
                            "sex": "",
                            "phone": "",
                            "location": [],
                            # Add more fields as needed
                        }
                        # Replace None with empty string for all string fields
                        for key in patient_data:
                            if key != "location" and patient_data[key] is None:
                                patient_data[key] = ""
                        patient_result = create_patient(patient_data)
                        if not patient_result:
                            logger.error(f"Failed to create patient record for user: {user.id}")
                    except Exception as e:
                        logger.error(f"Exception during patient record creation: {e}")
                return True, "User created successfully", user
            else:
                logger.debug(f"Failed to create user. Result: {result}")
                return False, "Failed to create user in database", None
                
        except Exception as e:
            return False, f"Error creating user: {str(e)}", None
    
    def authenticate_user(self, username: str, password: str) -> tuple[bool, str, Optional[UserSession]]:
        """
        Authenticate a user with username and password

        :param username: Username of the user
        :param password: Password of the user
        
        :return: (success, message, session_object)
        """
        try:
            # Get user by username
            logger.debug(f"Authenticating user: {username}")
            user = self.get_user_by_username(username)
            logger.debug(f"User lookup result: {user}")
            if not user:
                return False, "Invalid username or password", None
            
            # Check if user is active
            if not user.is_active:
                return False, "Account is deactivated", None
            
            # Verify password
            logger.debug(f"Verifying password for user: {user.username}")
            password_valid = user.verify_password(password)
            logger.debug(f"Password verification result: {password_valid}")
            if not password_valid:
                return False, "Invalid username or password", None
            
            # Create session
            logger.debug(f"Creating session for user: {user.username}")
            logger.debug(f"User ID being stored in session: {user.id}")
            session = UserSession(
                user_id=user.id if user.id is not None else "",
                username=user.username,
                role=user.role
            )
            logger.debug(f"Session created with user_id: {session.user_id}")
            
            # Store session in database
            try:
                self.db.create('Session', session.to_dict())
                logger.debug(f"Session stored in database: {session.token[:10]}...")
                
                # Also keep in memory for faster access
                self.active_sessions[session.token] = session
            except Exception as e:
                logger.debug(f"Error storing session in database: {e}")
                # Fallback to memory-only storage
                self.active_sessions[session.token] = session
            
            return True, "Authentication successful", session
            
        except Exception as e:
            return False, f"Authentication error: {str(e)}", None
    
    def get_user_by_username(self, username: str) -> Optional[User]:
        """
        Get user by username
        :param username: Username of the user to retrieve
        :return: User object if found, None otherwise
        """
        try:
            logger.debug(f"get_user_by_username - username: {username}")

            result = self.db.query(
                "SELECT * FROM User WHERE username = $username",
                {"username": username}
            )
            
            if result and len(result) > 0:
                user_data = result[0]
                return User.from_dict(user_data)
            
            return None
            
        except Exception as e:
            logger.error(f"Error getting user by username: {e}")
            return None
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Get user by email

        :param email: Email address of the user to retrieve
        :return: User object if found, None otherwise
        """
        try:
            result = self.db.query(
                "SELECT * FROM User WHERE email = $email",
                {"email": email}
            )
            
            if result and len(result) > 0:
                # The query result contains user data directly, not nested in a 'result' field
                user_dict = result[0]
                return User.from_dict(user_dict)
            return None
            
        except Exception as e:
            logger.error(f"Error getting user by email: {e}")
            return None
    
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        """
        Get user by ID
        :param user_id: ID of the user to retrieve
        :return: User object if found, None otherwise
        """
        try:
            logger.debug(f"get_user_by_id - user_id: {user_id}")
            logger.debug(f"get_user_by_id - user_id type: {type(user_id)}")
            
            # Use a simple approach: get all users and find the one with matching ID
            logger.debug("Getting all users to find by ID...")
            all_users = self.get_all_users()
            logger.debug(f"Found {len(all_users)} users")
            
            for user in all_users:
                logger.debug(f"Checking user: {user.username} (ID: {user.id})")
                if user.id == user_id:
                    logger.debug(f"Found matching user: {user.username}")
                    return user
            
            logger.debug(f"No user found for ID: {user_id}")
            return None
            
        except Exception as e:
            logger.error(f"Error getting user by ID: {e}")
            return None
    
    def validate_session(self, token: str) -> Optional[UserSession]:
        """
        Validate session token and return session if valid
        :param token: Session token to validate
        :return: UserSession object if valid, None otherwise
        """
        logger.debug(f"validate_session - token: {token[:10] if token else 'None'}...")
        
        # First check memory cache
        session = self.active_sessions.get(token)
        if session and not session.is_expired():
            logger.debug(f"Session found in memory cache for user: {session.username}")
            logger.debug(f"Session user_id: {session.user_id}")
            return session
        elif session and session.is_expired():
            # Remove expired session
            logger.debug(f"Removing expired session from memory cache")
            del self.active_sessions[token]
        
        # If not in memory, check database
        try:
            result = self.db.query(
                "SELECT * FROM Session WHERE token = $session_token",
                {"session_token": token}
            )
            
            if result and len(result) > 0:
                session_data = result[0]
                logger.debug(f"Session data from database: {session_data}")
                session = UserSession.from_dict(session_data)
                logger.debug(f"Session user_id from database: {session.user_id}")
                
                if session.is_expired():
                    # Remove expired session from database
                    self.db.delete(f"Session:{session_data.get('id')}")
                    return None
                
                # Add to memory cache
                self.active_sessions[token] = session
                return session
        except Exception as e:
            logger.debug(f"Error validating session from database: {e}")
        
        return None
    
    def logout(self, token: str) -> bool:
        """
        Logout user by removing session
        :param token: Session token to remove
        :return: True if logout successful, False otherwise
        """
        # Remove from memory
        if token in self.active_sessions:
            del self.active_sessions[token]
        
        # Remove from database
        try:
            result = self.db.query(
                "SELECT * FROM Session WHERE token = $session_token",
                {"session_token": token}
            )
            
            if result and len(result) > 0:
                session_data = result[0]
                self.db.delete(f"Session:{session_data.get('id')}")
                return True
        except Exception as e:
            logger.debug(f"Error removing session from database: {e}")
        
        return True
    
    def get_all_users(self) -> List[User]:
        """
        Get all users (admin only)
        :return: List of User objects
        """
        try:
            logger.debug("Getting all users from database...")
            results = self.db.select_many('User')
            logger.debug(f"Raw results: {results}")
            users: List[User] = []
            for user_data in results:
                # Remove password hash for security
                user_data.pop('password_hash', None)
                users.append(User.from_dict(user_data))
            logger.debug(f"Processed {len(users)} users")
            return users
            
        except Exception as e:
            logger.error(f"Error getting all users: {e}")
            return []
    
    def update_user(self, user_id: str, updates: Dict[str, Any]) -> tuple[bool, str]:
        """
        Update user information
        :param user_id: ID of the user to update
        :param updates: Dictionary of fields to update
        :return: (success, message)
        """
        try:
            # Remove sensitive fields that shouldn't be updated directly
            updates.pop('password_hash', None)
            updates.pop('id', None)
            updates.pop('created_at', None)
            
            result = self.db.update(f"User:{user_id}", updates)
            if result:
                return True, "User updated successfully"
            else:
                return False, "Failed to update user"
                
        except Exception as e:
            return False, f"Error updating user: {str(e)}"
    
    def change_password(self, user_id: str, current_password: str, new_password: str) -> tuple[bool, str]:
        """
        Change user password

        :param user_id: ID of the user whose password is to be changed
        :param current_password: Current password of the user
        :param new_password: New password to set for the user
        :return: (success, message)
        """
        try:
            # Get user
            user = self.get_user_by_id(user_id)
            if not user:
                return False, "User not found"
            
            # Verify current password
            if not user.verify_password(current_password):
                return False, "Current password is incorrect"
            
            # Validate new password
            valid, msg = User.validate_password(new_password)
            if not valid:
                return False, msg
            
            # Hash new password
            new_hash = User.hash_password(new_password)
            
            # Update password
            result = self.db.update(f"User:{user_id}", {"password_hash": new_hash})
            if result:
                return True, "Password changed successfully"
            else:
                return False, "Failed to change password"
                
        except Exception as e:
            return False, f"Error changing password: {str(e)}"
    
    def deactivate_user(self, user_id: str) -> tuple[bool, str]:
        """
        Deactivate a user account
        :param user_id: ID of the user to deactivate
        :return: (success, message)
        """
        try:
            result = self.db.update(f"User:{user_id}", {"is_active": False})
            if result:
                return True, "User deactivated successfully"
            else:
                return False, "Failed to deactivate user"
                
        except Exception as e:
            return False, f"Error deactivating user: {str(e)}"
    
    def activate_user(self, user_id: str) -> tuple[bool, str]:
        """
        Activate a user account

        :param user_id: ID of the user to activate
        :return: (success, message)
        """
        try:
            result = self.db.update(f"User:{user_id}", {"is_active": True})
            if result:
                return True, "User activated successfully"
            else:
                return False, "Failed to activate user"
                
        except Exception as e:
            return False, f"Error activating user: {str(e)}"
    
    def create_default_admin(self) -> tuple[bool, str]:
        """
        Create a default admin user if no users exist

        :return: (success, message)
        """
        try:
            # Check if any users exist
            users = self.get_all_users()
            if users:
                return True, "Users already exist, skipping default admin creation"
            
            # Create default admin
            success, message, _ = self.create_user(
                username="admin",
                email="admin@arsmedicatech.com",
                password="Admin123!",
                first_name="System",
                last_name="Administrator",
                role="admin"
            )
            
            if success:
                return True, "Default admin user created successfully"
            else:
                return False, f"Failed to create default admin: {message}"
                
        except Exception as e:
            return False, f"Error creating default admin: {str(e)}"
    
    def get_user_settings(self, user_id: str) -> Optional[UserSettings]:
        """
        Get user settings

        :param user_id: ID of the user whose settings to retrieve
        :return: UserSettings object if found, None otherwise
        """
        try:
            result = self.db.query(
                "SELECT * FROM UserSettings WHERE user_id = $user_id",
                {"user_id": user_id}
            )
            
            if result and len(result) > 0:
                settings_data = result[0]
                return UserSettings.from_dict(settings_data)
            
            # If no settings exist, create default settings
            return UserSettings(user_id=user_id)
            
        except Exception as e:
            logger.error(f"Error getting user settings: {e}")
            return None
    
    def save_user_settings(self, user_id: str, settings: UserSettings) -> tuple[bool, str]:
        """
        Save user settings

        :param user_id: ID of the user whose settings to save
        :param settings: UserSettings object containing the settings to save
        :return: (success, message)
        """
        try:
            logger.debug(f"Saving settings for user: {user_id}")
            
            # Check if settings already exist
            existing_settings = self.get_user_settings(user_id)
            logger.debug(f"Existing settings: {existing_settings.id if existing_settings else 'None'}")
            
            if existing_settings and existing_settings.id:
                # Update existing settings
                logger.debug(f"Updating existing settings: {existing_settings.id}")
                
                # Construct the record ID properly
                if existing_settings.id.startswith('UserSettings:'):
                    record_id = existing_settings.id
                else:
                    record_id = f"UserSettings:{existing_settings.id}"
                
                logger.debug(f"Using record ID: {record_id}")
                result = self.db.update(record_id, settings.to_dict())
                logger.debug(f"Update result: {result}")
                logger.debug(f"Update result type: {type(result)}")
                logger.debug(f"Update result is empty dict: {result == {}}")
                # Check if result is not empty
                if result != {}:
                    return True, "Settings updated successfully"
                else:
                    return False, "Failed to update settings"
            else:
                # Create new settings
                logger.debug(f"Creating new settings")
                result = self.db.create('UserSettings', settings.to_dict())
                logger.debug(f"Create result: {result}")
                if result and result.get('id'):
                    settings.id = result['id']
                    return True, "Settings created successfully"
                else:
                    return False, "Failed to create settings"
                    
        except Exception as e:
            logger.error(f"Error saving settings: {e}")
            return False, f"Error saving settings: {str(e)}"
    
    def update_openai_api_key(self, user_id: str, api_key: str) -> tuple[bool, str]:
        """
        Update user's OpenAI API key

        :param user_id: ID of the user whose API key to update
        :param api_key: New OpenAI API key to set for the user
        :return: (success, message)
        """
        try:
            # Allow empty string to remove API key
            if api_key == "":
                # Get or create settings
                settings = self.get_user_settings(user_id)
                if not settings:
                    settings = UserSettings(user_id=user_id)
                
                # Clear API key
                settings.set_openai_api_key("")
                
                # Save settings
                return self.save_user_settings(user_id, settings)
            
            # Validate API key if not empty
            valid, msg = UserSettings.validate_openai_api_key(api_key)
            if not valid:
                return False, msg
            
            # Get or create settings
            settings = self.get_user_settings(user_id)
            if not settings:
                settings = UserSettings(user_id=user_id)
            
            # Update API key
            settings.set_openai_api_key(api_key)
            
            # Save settings
            return self.save_user_settings(user_id, settings)
            
        except Exception as e:
            return False, f"Error updating API key: {str(e)}"
    
    def get_openai_api_key(self, user_id: str) -> str:
        """
        Get user's decrypted OpenAI API key

        :param user_id: ID of the user whose API key to retrieve
        :return: OpenAI API key if found, empty string otherwise
        """
        try:
            settings = self.get_user_settings(user_id)
            if settings:
                return settings.get_openai_api_key()
            return ""
        except Exception as e:
            logger.error(f"Error getting API key: {e}")
            return ""
    
    def has_openai_api_key(self, user_id: str) -> bool:
        """
        Check if user has a valid OpenAI API key

        :param user_id: ID of the user to check
        :return: True if user has a valid OpenAI API key, False otherwise
        """
        try:
            settings = self.get_user_settings(user_id)
            if settings:
                return settings.has_openai_api_key()
            return False
        except Exception as e:
            logger.error(f"Error checking API key: {e}")
            return False
    
    def update_optimal_api_key(self, user_id: str, api_key: str) -> tuple[bool, str]:
        """
        Update user's Optimal API key

        :param user_id: ID of the user whose API key to update
        :param api_key: New Optimal API key to set for the user
        :return: (success, message)
        """
        try:
            # Allow empty string to remove API key
            if api_key == "":
                # Get or create settings
                settings = self.get_user_settings(user_id)
                if not settings:
                    settings = UserSettings(user_id=user_id)
                
                # Clear API key
                settings.set_optimal_api_key("")
                
                # Save settings
                return self.save_user_settings(user_id, settings)
            
            # Validate API key if not empty
            valid, msg = UserSettings.validate_optimal_api_key(api_key)
            if not valid:
                return False, msg
            
            # Get or create settings
            settings = self.get_user_settings(user_id)
            if not settings:
                settings = UserSettings(user_id=user_id)
            
            # Update API key
            settings.set_optimal_api_key(api_key)
            
            # Save settings
            return self.save_user_settings(user_id, settings)
            
        except Exception as e:
            return False, f"Error updating Optimal API key: {str(e)}"
    
    def get_optimal_api_key(self, user_id: str) -> str:
        """
        Get user's decrypted Optimal API key

        :param user_id: ID of the user whose API key to retrieve
        :return: Optimal API key if found, empty string otherwise
        """
        try:
            settings = self.get_user_settings(user_id)
            if settings:
                return settings.get_optimal_api_key()
            return ""
        except Exception as e:
            logger.error(f"Error getting Optimal API key: {e}")
            return ""
    
    def has_optimal_api_key(self, user_id: str) -> bool:
        """
        Check if user has a valid Optimal API key

        :param user_id: ID of the user to check
        :return: True if user has a valid Optimal API key, False otherwise
        """
        try:
            settings = self.get_user_settings(user_id)
            if settings:
                return settings.has_optimal_api_key()
            return False
        except Exception as e:
            logger.error(f"Error checking Optimal API key: {e}")
            return False
