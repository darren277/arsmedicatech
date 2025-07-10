from typing import Optional, Dict, Any, List
from lib.models.user import User, UserSession
from lib.models.user_settings import UserSettings
from lib.db.surreal import DbController


class UserService:
    def __init__(self, db_controller: DbController = None):
        self.db = db_controller or DbController()
        self.active_sessions: Dict[str, UserSession] = {}
    
    def connect(self):
        """Connect to database"""
        print("[DEBUG] Connecting to database...")
        try:
            print(f"[DEBUG] Database controller type: {type(self.db)}")
            print(f"[DEBUG] Database controller has connect method: {hasattr(self.db, 'connect')}")
            
            if hasattr(self.db, 'connect'):
                self.db.connect()
                print("[DEBUG] Database connection successful")
            else:
                print("[DEBUG] Database controller does not have connect method - using mock mode")
        except Exception as e:
            print(f"[DEBUG] Database connection error: {e}")
            print("[DEBUG] Continuing with mock database mode")
            # Don't raise the exception, continue with mock mode
    
    def close(self):
        """Close database connection"""
        self.db.close()
    
    def create_user(self, username: str, email: str, password: str, 
                   first_name: str = None, last_name: str = None, 
                   role: str = "patient") -> tuple[bool, str, Optional[User]]:
        """
        Create a new user account
        
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
            print(f"[DEBUG] Creating user with data: {user.to_dict()}")
            
            # For testing, use a mock database if SurrealDB is not available
            if not hasattr(self.db, 'create') or self.db is None:
                print("[DEBUG] Using mock database for user creation")
                # Mock user storage (in-memory for testing)
                if not hasattr(self, '_mock_users'):
                    self._mock_users = {}
                    print("[DEBUG] Mock users storage initialized")
                
                # Generate a mock ID
                user.id = f"user_{len(self._mock_users) + 1}"
                self._mock_users[user.username] = user
                print(f"[DEBUG] User created successfully with ID: {user.id}")
                print(f"[DEBUG] Mock users now available: {list(self._mock_users.keys())}")
                print(f"[DEBUG] User data: {user.to_dict()}")
                
                # If the user is a patient, create a corresponding Patient record
                if user.role == "patient" and user.id:
                    try:
                        from lib.models.patient import create_patient
                        user_id = str(user.id)
                        if ':' in user_id:
                            patient_id = user_id.split(':', 1)[1]
                        else:
                            patient_id = user_id
                        patient_data = {
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
                            print(f"[ERROR] Failed to create patient record for user: {user.id}")
                    except Exception as e:
                        print(f"[ERROR] Exception during patient record creation: {e}")
                return True, "User created successfully", user
            
            result = self.db.create('User', user.to_dict())
            print(f"[DEBUG] Database create result: {result}")
            print(f"[DEBUG] Database create result type: {type(result)}")
            if result and isinstance(result, dict) and result.get('id'):
                user.id = result['id']
                print(f"[DEBUG] User created successfully with ID: {user.id}")
                print(f"[DEBUG] User ID type: {type(user.id)}")
                
                # Test if we can immediately retrieve the user
                print(f"[DEBUG] Testing immediate user retrieval...")
                test_user = self.get_user_by_id(user.id)
                if test_user:
                    print(f"[DEBUG] ✅ User can be retrieved immediately: {test_user.username}")
                else:
                    print(f"[DEBUG] ❌ User cannot be retrieved immediately")
                
                # If the user is a patient, create a corresponding Patient record
                if user.role == "patient" and user.id:
                    try:
                        from lib.models.patient import create_patient
                        user_id = str(user.id)
                        if ':' in user_id:
                            patient_id = user_id.split(':', 1)[1]
                        else:
                            patient_id = user_id
                        patient_data = {
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
                            print(f"[ERROR] Failed to create patient record for user: {user.id}")
                    except Exception as e:
                        print(f"[ERROR] Exception during patient record creation: {e}")
                return True, "User created successfully", user
            else:
                print(f"[DEBUG] Failed to create user. Result: {result}")
                return False, "Failed to create user in database", None
                
        except Exception as e:
            return False, f"Error creating user: {str(e)}", None
    
    def authenticate_user(self, username: str, password: str) -> tuple[bool, str, Optional[UserSession]]:
        """
        Authenticate a user with username and password
        
        :return: (success, message, session_object)
        """
        try:
            # Get user by username
            print(f"[DEBUG] Authenticating user: {username}")
            user = self.get_user_by_username(username)
            print(f"[DEBUG] User lookup result: {user}")
            if not user:
                return False, "Invalid username or password", None
            
            # Check if user is active
            if not user.is_active:
                return False, "Account is deactivated", None
            
            # Verify password
            print(f"[DEBUG] Verifying password for user: {user.username}")
            password_valid = user.verify_password(password)
            print(f"[DEBUG] Password verification result: {password_valid}")
            if not password_valid:
                return False, "Invalid username or password", None
            
            # Create session
            print(f"[DEBUG] Creating session for user: {user.username}")
            print(f"[DEBUG] User ID being stored in session: {user.id}")
            session = UserSession(
                user_id=user.id,
                username=user.username,
                role=user.role
            )
            print(f"[DEBUG] Session created with user_id: {session.user_id}")
            
            # Store session in database
            try:
                self.db.create('Session', session.to_dict())
                print(f"[DEBUG] Session stored in database: {session.token[:10]}...")
                
                # Also keep in memory for faster access
                self.active_sessions[session.token] = session
            except Exception as e:
                print(f"[DEBUG] Error storing session in database: {e}")
                # Fallback to memory-only storage
                self.active_sessions[session.token] = session
            
            return True, "Authentication successful", session
            
        except Exception as e:
            return False, f"Authentication error: {str(e)}", None
    
    def get_user_by_username(self, username: str) -> Optional[User]:
        """Get user by username"""
        try:
            print(f"[DEBUG] get_user_by_username - username: {username}")

            result = self.db.query(
                "SELECT * FROM User WHERE username = $username",
                {"username": username}
            )
            
            print(f"[DEBUG] Raw query result: {result}")
            
            if result and isinstance(result, list) and len(result) > 0:
                print(f"[DEBUG] Found {len(result)} users with username '{username}'")
                # If multiple users exist, use the most recent one (latest created_at)
                if len(result) > 1:
                    # Sort by created_at timestamp (newest first)
                    sorted_results = sorted(result, key=lambda x: x.get('created_at', ''), reverse=True)
                    user_dict = sorted_results[0]
                    print(f"[DEBUG] Using most recent user: {user_dict.get('created_at')}")
                else:
                    user_dict = result[0]
                
                print(f"[DEBUG] User dict: {user_dict}")
                return User.from_dict(user_dict)
            return None
            
        except Exception as e:
            print(f"Error getting user by username: {e}")
            return None
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        try:
            result = self.db.query(
                "SELECT * FROM User WHERE email = $email",
                {"email": email}
            )
            
            if result and isinstance(result, list) and len(result) > 0:
                # The query result contains user data directly, not nested in a 'result' field
                user_dict = result[0]
                return User.from_dict(user_dict)
            return None
            
        except Exception as e:
            print(f"Error getting user by email: {e}")
            return None
    
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        """Get user by ID"""
        try:
            result = self.db.select(f"User:{user_id}")
            if result and isinstance(result, dict):
                return User.from_dict(result)
            return None
            
        except Exception as e:
            print(f"Error getting user by ID: {e}")
            return None
    
    def validate_session(self, token: str) -> Optional[UserSession]:
        """Validate session token and return session if valid"""
        print(f"[DEBUG] validate_session - token: {token[:10] if token else 'None'}...")
        
        # First check memory cache
        session = self.active_sessions.get(token)
        if session and not session.is_expired():
            print(f"[DEBUG] Session found in memory cache for user: {session.username}")
            print(f"[DEBUG] Session user_id: {session.user_id}")
            return session
        elif session and session.is_expired():
            # Remove expired session
            print(f"[DEBUG] Removing expired session from memory cache")
            del self.active_sessions[token]
        
        # If not in memory, check database
        try:
            result = self.db.query(
                "SELECT * FROM Session WHERE token = $session_token",
                {"session_token": token}
            )
            
            if result and isinstance(result, list) and len(result) > 0:
                session_data = result[0]
                print(f"[DEBUG] Session data from database: {session_data}")
                session = UserSession.from_dict(session_data)
                print(f"[DEBUG] Session user_id from database: {session.user_id}")
                
                if session.is_expired():
                    # Remove expired session from database
                    self.db.delete(f"Session:{session_data.get('id')}")
                    return None
                
                # Add to memory cache
                self.active_sessions[token] = session
                return session
        except Exception as e:
            print(f"[DEBUG] Error validating session from database: {e}")
        
        return None
    
    def logout(self, token: str) -> bool:
        """Logout user by removing session"""
        # Remove from memory
        if token in self.active_sessions:
            del self.active_sessions[token]
        
        # Remove from database
        try:
            result = self.db.query(
                "SELECT * FROM Session WHERE token = $session_token",
                {"session_token": token}
            )
            
            if result and isinstance(result, list) and len(result) > 0:
                session_data = result[0]
                self.db.delete(f"Session:{session_data.get('id')}")
                return True
        except Exception as e:
            print(f"[DEBUG] Error removing session from database: {e}")
        
        return True
    
    def get_all_users(self) -> List[User]:
        """Get all users (admin only)"""
        try:
            print("[DEBUG] Getting all users from database...")
            results = self.db.select_many('User')
            print(f"[DEBUG] Raw results: {results}")
            users = []
            for user_data in results:
                if isinstance(user_data, dict):
                    # Remove password hash for security
                    user_data.pop('password_hash', None)
                    users.append(User.from_dict(user_data))
            print(f"[DEBUG] Processed {len(users)} users")
            return users
            
        except Exception as e:
            print(f"Error getting all users: {e}")
            return []
    
    def update_user(self, user_id: str, updates: Dict[str, Any]) -> tuple[bool, str]:
        """Update user information"""
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
        """Change user password"""
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
            new_hash = user._hash_password(new_password)
            
            # Update password
            result = self.db.update(f"User:{user_id}", {"password_hash": new_hash})
            if result:
                return True, "Password changed successfully"
            else:
                return False, "Failed to change password"
                
        except Exception as e:
            return False, f"Error changing password: {str(e)}"
    
    def deactivate_user(self, user_id: str) -> tuple[bool, str]:
        """Deactivate a user account"""
        try:
            result = self.db.update(f"User:{user_id}", {"is_active": False})
            if result:
                return True, "User deactivated successfully"
            else:
                return False, "Failed to deactivate user"
                
        except Exception as e:
            return False, f"Error deactivating user: {str(e)}"
    
    def activate_user(self, user_id: str) -> tuple[bool, str]:
        """Activate a user account"""
        try:
            result = self.db.update(f"User:{user_id}", {"is_active": True})
            if result:
                return True, "User activated successfully"
            else:
                return False, "Failed to activate user"
                
        except Exception as e:
            return False, f"Error activating user: {str(e)}"
    
    def create_default_admin(self) -> tuple[bool, str]:
        """Create a default admin user if no users exist"""
        try:
            # Check if any users exist
            users = self.get_all_users()
            if users:
                return True, "Users already exist, skipping default admin creation"
            
            # Create default admin
            success, message, user = self.create_user(
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
        """Get user settings"""
        try:
            result = self.db.query(
                "SELECT * FROM UserSettings WHERE user_id = $user_id",
                {"user_id": user_id}
            )
            
            if result and isinstance(result, list) and len(result) > 0:
                settings_data = result[0]
                return UserSettings.from_dict(settings_data)
            
            # If no settings exist, create default settings
            return UserSettings(user_id=user_id)
            
        except Exception as e:
            print(f"[ERROR] Error getting user settings: {e}")
            return None
    
    def save_user_settings(self, user_id: str, settings: UserSettings) -> tuple[bool, str]:
        """Save user settings"""
        try:
            print(f"[DEBUG] Saving settings for user: {user_id}")
            
            # Check if settings already exist
            existing_settings = self.get_user_settings(user_id)
            print(f"[DEBUG] Existing settings: {existing_settings.id if existing_settings else 'None'}")
            
            if existing_settings and existing_settings.id:
                # Update existing settings
                print(f"[DEBUG] Updating existing settings: {existing_settings.id}")
                
                # Construct the record ID properly
                if existing_settings.id.startswith('UserSettings:'):
                    record_id = existing_settings.id
                else:
                    record_id = f"UserSettings:{existing_settings.id}"
                
                print(f"[DEBUG] Using record ID: {record_id}")
                result = self.db.update(record_id, settings.to_dict())
                print(f"[DEBUG] Update result: {result}")
                print(f"[DEBUG] Update result type: {type(result)}")
                print(f"[DEBUG] Update result is None: {result is None}")
                print(f"[DEBUG] Update result is empty list: {result == []}")
                print(f"[DEBUG] Update result is empty dict: {result == {}}")
                # Check if result is truthy (not None, not empty, etc.)
                if result is not None and result != [] and result != {}:
                    return True, "Settings updated successfully"
                else:
                    return False, "Failed to update settings"
            else:
                # Create new settings
                print(f"[DEBUG] Creating new settings")
                result = self.db.create('UserSettings', settings.to_dict())
                print(f"[DEBUG] Create result: {result}")
                if result and isinstance(result, dict) and result.get('id'):
                    settings.id = result['id']
                    return True, "Settings created successfully"
                else:
                    return False, "Failed to create settings"
                    
        except Exception as e:
            print(f"[ERROR] Error saving settings: {e}")
            return False, f"Error saving settings: {str(e)}"
    
    def update_openai_api_key(self, user_id: str, api_key: str) -> tuple[bool, str]:
        """Update user's OpenAI API key"""
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
        """Get user's decrypted OpenAI API key"""
        try:
            settings = self.get_user_settings(user_id)
            if settings:
                return settings.get_openai_api_key()
            return ""
        except Exception as e:
            print(f"[ERROR] Error getting API key: {e}")
            return ""
    
    def has_openai_api_key(self, user_id: str) -> bool:
        """Check if user has a valid OpenAI API key"""
        try:
            settings = self.get_user_settings(user_id)
            if settings:
                return settings.has_openai_api_key()
            return False
        except Exception as e:
            print(f"[ERROR] Error checking API key: {e}")
            return False 