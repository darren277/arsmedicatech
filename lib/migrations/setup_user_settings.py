"""
Database migration script to set up UserSettings table schema
"""

import os
import sys

# Add the lib directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from db.surreal import DbController
from settings import SURREALDB_NAMESPACE, SURREALDB_DATABASE

from settings import logger


def setup_user_settings_schema():
    """Set up UserSettings table schema in SurrealDB"""
    logger.debug("🔧 Setting up UserSettings table schema...")
    
    try:
        # Connect to database
        db = DbController()
        db.connect()
        
        # Define UserSettings table schema
        schema_definition = f"""
        -- Switch to namespace and database
        USE ns {SURREALDB_NAMESPACE} DB {SURREALDB_DATABASE};
        
        -- Define UserSettings table
        DEFINE TABLE UserSettings SCHEMAFULL;
        
        -- Define fields
        DEFINE FIELD user_id ON UserSettings TYPE string;
        DEFINE FIELD openai_api_key ON UserSettings TYPE string;
        DEFINE FIELD created_at ON UserSettings TYPE string;
        DEFINE FIELD updated_at ON UserSettings TYPE string;
        
        -- Define indexes
        DEFINE INDEX idx_user_id ON UserSettings FIELDS user_id;
        
        -- Define permissions (only authenticated users can access their own settings)
        DEFINE TABLE UserSettings PERMISSIONS 
            FOR select WHERE auth.id = user_id
            FOR create WHERE auth.id = user_id
            FOR update WHERE auth.id = user_id
            FOR delete WHERE auth.id = user_id;
        """
        
        logger.debug("📝 Executing schema definition...")
        result = db.query(schema_definition)
        logger.debug(f"✅ Schema setup result: {result}")
        
        # Test the schema by creating a test record
        logger.debug("\n🧪 Testing schema with a test record...")
        test_data = {
            'user_id': 'test-user-123',
            'openai_api_key': 'encrypted-test-key',
            'created_at': '2024-01-01T00:00:00',
            'updated_at': '2024-01-01T00:00:00'
        }
        
        # Create test record
        create_result = db.create('UserSettings', test_data)
        logger.debug(f"✅ Test record created: {create_result}")
        
        # Query test record
        query_result = db.query(
            "SELECT * FROM UserSettings WHERE user_id = $user_id",
            {"user_id": "test-user-123"}
        )
        logger.debug(f"✅ Test record queried: {query_result}")
        
        # Clean up test record
        if create_result and isinstance(create_result, dict) and create_result.get('id'):
            delete_result = db.delete(create_result['id'])
            logger.debug(f"✅ Test record cleaned up: {delete_result}")
        
        db.close()
        logger.debug("\n🎉 UserSettings schema setup completed successfully!")
        return True
        
    except Exception as e:
        logger.debug(f"❌ Error setting up UserSettings schema: {e}")
        import traceback
        traceback.print_exc()
        return False

def check_existing_schema():
    """Check if UserSettings table already exists"""
    logger.debug("🔍 Checking existing UserSettings schema...")
    
    try:
        db = DbController()
        db.connect()
        
        # Try to query the table structure
        result = db.query("INFO FOR TABLE UserSettings")
        logger.debug(f"📋 Existing schema info: {result}")
        
        db.close()
        return True
        
    except Exception as e:
        logger.debug(f"⚠️  UserSettings table may not exist: {e}")
        return False

def main():
    """Main migration function"""
    logger.debug("🚀 UserSettings Database Migration")
    logger.debug("=" * 50)
    
    # Check if schema already exists
    if check_existing_schema():
        logger.debug("✅ UserSettings table already exists")
        return True
    
    # Set up schema
    return setup_user_settings_schema()

if __name__ == "__main__":
    success = main()
    if success:
        logger.debug("\n✅ Migration completed successfully!")
        logger.debug("\n💡 The UserSettings table is now ready for use.")
    else:
        logger.debug("\n❌ Migration failed!")
        logger.debug("   Check the errors above and try again.")