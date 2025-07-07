from typing import Optional, Dict, Any, List
from lib.models.user import User, UserSession
from lib.db.surreal import DbController


class UserService:
    def __init__(self, db_controller: DbController = None):
        self.db = db_controller or DbController()
        self.active_sessions: Dict[str, UserSession] = {}
    
    def connect(self):
        """Connect to database"""
        self.db.connect()
    
    def close(self):
        """Close database connection"""
        self.db.close()
    
    def create_user(self, username: str, email: str, password: str, 
                   first_name: str = None, last_name: str = None, 
                   role: str = "user") -> tuple[bool, str, Optional[User]]:
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
                
                # Generate a mock ID
                user.id = f"user_{len(self._mock_users) + 1}"
                self._mock_users[user.username] = user
                print(f"[DEBUG] User created successfully with ID: {user.id}")
                return True, "User created successfully", user
            
            result = self.db.create('User', user.to_dict())
            print(f"[DEBUG] Database create result: {result}")
            if result and isinstance(result, dict) and result.get('id'):
                user.id = result['id']
                print(f"[DEBUG] User created successfully with ID: {user.id}")
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
            session = UserSession(
                user_id=user.id,
                username=user.username,
                role=user.role
            )
            
            # Store session
            self.active_sessions[session.token] = session
            
            return True, "Authentication successful", session
            
        except Exception as e:
            return False, f"Authentication error: {str(e)}", None
    
    def get_user_by_username(self, username: str) -> Optional[User]:
        """Get user by username"""
        try:
            # For testing, use a mock database if SurrealDB is not available
            if not hasattr(self.db, 'query') or self.db is None:
                print("[DEBUG] Using mock database for user lookup")
                # Mock user storage (in-memory for testing)
                if not hasattr(self, '_mock_users'):
                    self._mock_users = {}
                return self._mock_users.get(username)
            
            # First, let's see all users in the database
            all_users = self.db.select_many('User')
            print(f"[DEBUG] All users in database: {all_users}")
            
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
        session = self.active_sessions.get(token)
        if session and not session.is_expired():
            return session
        elif session and session.is_expired():
            # Remove expired session
            del self.active_sessions[token]
        return None
    
    def logout(self, token: str) -> bool:
        """Logout user by removing session"""
        if token in self.active_sessions:
            del self.active_sessions[token]
            return True
        return False
    
    def get_all_users(self) -> List[User]:
        """Get all users (admin only)"""
        try:
            results = self.db.select_many('User')
            users = []
            for user_data in results:
                if isinstance(user_data, dict):
                    # Remove password hash for security
                    user_data.pop('password_hash', None)
                    users.append(User.from_dict(user_data))
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