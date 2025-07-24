"""
Database migration script to set up UserNote table schema
"""

import os
import sys

# Add the lib directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from db.surreal import DbController  # type: ignore

from settings import SURREALDB_DATABASE, SURREALDB_NAMESPACE, logger


def setup_user_notes_schema() -> bool:
    """
    Set up UserNote table schema in SurrealDB

    This function connects to the SurrealDB instance, defines the UserNote table schema,
    and creates a test record to verify the schema setup.
    Returns:
        bool: True if schema setup is successful, False otherwise.
    """
    logger.debug("🔧 Setting up UserNote table schema...")
    
    db = None
    try:
        # Connect to database
        db = DbController()
        db.connect()
        
        # Define UserNote table schema
        schema_definition = f"""
        -- Switch to namespace and database
        USE ns {SURREALDB_NAMESPACE} DB {SURREALDB_DATABASE};
        
        -- Define UserNote table
        DEFINE TABLE UserNote SCHEMAFULL;
        
        -- Define fields
        DEFINE FIELD user_id ON UserNote TYPE string;
        DEFINE FIELD title ON UserNote TYPE string;
        DEFINE FIELD content ON UserNote TYPE string;
        DEFINE FIELD note_type ON UserNote TYPE string;
        DEFINE FIELD tags ON UserNote TYPE array;
        DEFINE FIELD date_created ON UserNote TYPE string;
        DEFINE FIELD date_updated ON UserNote TYPE string;
        
        -- Define indexes
        DEFINE INDEX idx_user_id ON UserNote FIELDS user_id;
        DEFINE INDEX idx_note_type ON UserNote FIELDS note_type;
        DEFINE INDEX idx_date_updated ON UserNote FIELDS date_updated;
        
        -- Define permissions (users can only access their own notes or shared notes)
        DEFINE TABLE UserNote PERMISSIONS 
            FOR select WHERE auth.id = user_id OR note_type = 'shared'
            FOR create WHERE auth.id = user_id
            FOR update WHERE auth.id = user_id
            FOR delete WHERE auth.id = user_id;
        """
        
        logger.debug("📝 Executing schema definition...")
        result = db.query(schema_definition)
        logger.debug(f"Schema definition result: {result}")
        
        # Create a test record to verify the schema
        logger.debug("🧪 Creating test record...")
        test_note = {
            'user_id': 'test_user',
            'title': 'Test Note',
            'content': '# Test Note\n\nThis is a test note with **markdown** content.',
            'note_type': 'private',
            'tags': ['test', 'migration'],
            'date_created': '2023-01-01T00:00:00Z',
            'date_updated': '2023-01-01T00:00:00Z'
        }
        
        test_result = db.create('UserNote', test_note)
        logger.debug(f"Test record creation result: {test_result}")
        
        if test_result:
            logger.info("✅ UserNote table schema setup completed successfully")
            return True
        else:
            logger.error("❌ Failed to create test record")
            return False
            
    except Exception as e:
        logger.error(f"❌ Error setting up UserNote table schema: {e}")
        return False
    finally:
        try:
            if db is not None:
                db.close()
        except:
            pass


if __name__ == "__main__":
    success = setup_user_notes_schema()
    if success:
        print("✅ UserNote table schema setup completed successfully")
        sys.exit(0)
    else:
        print("❌ UserNote table schema setup failed")
        sys.exit(1) 