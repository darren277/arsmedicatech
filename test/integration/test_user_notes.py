"""
Integration test for User Notes functionality
"""

import os
import sys

# Add the parent directory to the path so we can import from lib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.services.user_notes_service import UserNotesService


def test_user_notes():
    """Test user notes functionality"""
    print("🧪 Testing User Notes Functionality")
    
    # Create user notes service
    user_notes_service = UserNotesService()
    
    try:
        print("\n1. Connecting to database...")
        user_notes_service.connect()
        print("✅ Database connected")
        
        # Test user ID
        test_user_id = "test_user_123"
        
        print("\n2. Creating a test note...")
        success, message, note = user_notes_service.create_note(
            user_id=test_user_id,
            title="Test Note",
            content="# Test Note\n\nThis is a **test note** with markdown content.",
            note_type="private",
            tags=["test", "integration"]
        )
        
        if success and note and note.id:
            note_id = note.id
            print(f"✅ Note created successfully: {note_id}")
            print(f"   Title: {note.title}")
            print(f"   Type: {note.note_type}")
            print(f"   Tags: {note.tags}")
        else:
            print(f"❌ Failed to create note: {message}")
            return False
        
        print("\n3. Retrieving the note...")
        retrieved_note = user_notes_service.get_note_by_id(note_id, test_user_id)
        
        if retrieved_note:
            print(f"✅ Note retrieved successfully")
            print(f"   Content: {retrieved_note.content[:50]}...")
        else:
            print("❌ Failed to retrieve note")
            return False
        
        print("\n4. Updating the note...")
        success, message, updated_note = user_notes_service.update_note(
            note_id=note_id,
            user_id=test_user_id,
            title="Updated Test Note",
            content="# Updated Test Note\n\nThis note has been **updated** with new content.",
            tags=["test", "integration", "updated"]
        )
        
        if success and updated_note:
            print(f"✅ Note updated successfully")
            print(f"   New title: {updated_note.title}")
            print(f"   New tags: {updated_note.tags}")
        else:
            print(f"❌ Failed to update note: {message}")
            return False
        
        print("\n5. Getting all user notes...")
        all_notes = user_notes_service.get_user_notes(test_user_id)
        print(f"✅ Found {len(all_notes)} notes for user")
        
        for i, user_note in enumerate(all_notes, 1):
            print(f"   {i}. {user_note.title} ({user_note.note_type})")
        
        print("\n6. Searching notes...")
        search_results = user_notes_service.search_notes(test_user_id, "updated")
        print(f"✅ Found {len(search_results)} notes matching 'updated'")
        
        print("\n7. Deleting the test note...")
        success, message = user_notes_service.delete_note(note_id, test_user_id)
        
        if success:
            print("✅ Note deleted successfully")
        else:
            print(f"❌ Failed to delete note: {message}")
            return False
        
        print("\n8. Verifying note is deleted...")
        deleted_note = user_notes_service.get_note_by_id(note_id, test_user_id)
        
        if deleted_note is None:
            print("✅ Note successfully deleted (not found)")
        else:
            print("❌ Note still exists after deletion")
            return False
        
        print("\n🎉 All user notes tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        return False
    finally:
        user_notes_service.close()


if __name__ == "__main__":
    success = test_user_notes()
    if success:
        print("\n✅ User Notes integration test completed successfully")
        sys.exit(0)
    else:
        print("\n❌ User Notes integration test failed")
        sys.exit(1) 