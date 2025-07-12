"""
Conversation Service
"""
from typing import List, Optional, Tuple

from lib.db.surreal import DbController
from lib.models.conversation import Conversation, Message
from settings import logger


class ConversationService:
    """
    Service for managing conversations and messages
    """
    def __init__(self, db_controller: Optional[DbController] = None) -> None:
        """
        Initialize the ConversationService
        :param db_controller: Optional DbController instance
        If not provided, a new DbController will be created.
        :return: None
        """
        self.db = db_controller or DbController()
    
    def connect(self) -> None:
        """
        Connect to database

        :return: None
        """
        try:
            self.db.connect()
        except Exception as e:
            logger.error(f"Error connecting to database: {e}")
            raise e
    
    def close(self) -> None:
        """
        Close database connection

        :return: None
        """
        self.db.close()
    
    def create_conversation(self, participants: List[str], conversation_type: str = "user_to_user") -> Tuple[bool, str, Optional[Conversation]]:
        """
        Create a new conversation
        
        :param participants: List of user IDs participating in the conversation
        :param conversation_type: Type of conversation ("user_to_user", "ai_assistant")
        :return: (success, message, conversation_object)
        """
        try:
            logger.debug(f"Creating conversation with participants: {participants}")
            logger.debug(f"Conversation type: {conversation_type}")
            
            # Validate participants
            if len(participants) < 2:
                return False, "At least 2 participants are required", None
            
            # Check if conversation already exists between these participants
            existing_conv = self.get_conversation_by_participants(participants)
            if existing_conv:
                logger.debug(f"Found existing conversation: {existing_conv.id}")
                return True, "Conversation already exists", existing_conv
            
            # Create new conversation
            conversation = Conversation(participants, conversation_type)
            logger.debug(f"Creating conversation in DB with data: {conversation.to_dict()}")
            logger.debug(f"Created conversation object: {conversation.to_dict()}")
            
            # Save to database
            result = self.db.create('Conversation', conversation.to_dict())
            logger.debug(f"Database create result: {result}")
            if result:
                conversation.id = result.get('id')
                logger.debug(f"Set conversation ID to: {conversation.id}")
                
                # Verify the conversation was saved by trying to retrieve it
                logger.debug(f"Verifying conversation was saved...")
                verification = self.get_conversation_by_id(conversation.id)
                if verification:
                    logger.debug(f"Conversation verification successful: {verification.id}")
                else:
                    logger.debug(f"Conversation verification failed - could not retrieve saved conversation")
                    
                    # Let's check what's actually in the database
                    logger.debug(f"Checking all conversations in database...")
                    all_conversations = self.db.query("SELECT * FROM Conversation")
                    logger.debug(f"All conversations: {all_conversations}")
                    
                    # Also try to get conversations by participants
                    logger.debug(f"Checking conversations by participants...")
                    participant_conversations = self.db.query(
                        "SELECT * FROM Conversation WHERE $user_id IN participants",
                        {"user_id": participants[0]}
                    )
                    logger.debug(f"Conversations for participant {participants[0]}: {participant_conversations}")
                
                return True, "Conversation created successfully", conversation
            else:
                logger.debug(f"Database create failed: {result}")
                return False, "Failed to create conversation", None
                
        except Exception as e:
            logger.debug(f"Exception in create_conversation: {e}")
            return False, f"Error creating conversation: {str(e)}", None
    
    def get_conversation_by_id(self, conversation_id: str) -> Optional[Conversation]:
        """
        Get conversation by ID

        :param conversation_id: ID of the conversation
        :return: Conversation object or None if not found
        """
        try:
            # Extract the record_id part from the conversation_id
            if conversation_id.startswith('Conversation:'):
                record_id = conversation_id.split(':', 1)[1]
            else:
                record_id = conversation_id

            record_id_expr = f"Conversation:{record_id}"
            logger.debug(f"Looking for conversation with record_id_expr: {record_id_expr}")

            # Use SurrealQL RecordID syntax (no quotes)
            query = f"SELECT * FROM Conversation WHERE id = {record_id_expr}"
            query_result = self.db.query(query)
            logger.debug(f"Query result: {query_result}")

            if query_result and isinstance(query_result, list) and len(query_result) > 0:
                if isinstance(query_result[0], dict):
                    conv = Conversation.from_dict(query_result[0])
                    logger.debug(f"Found conversation: {conv.id}")
                    return conv

            logger.debug(f"No conversation found with ID: {conversation_id}")
            return None

        except Exception as e:
            logger.error(f"Error getting conversation by ID: {e}")
            return None
    
    def get_conversation_by_participants(self, participants: List[str]) -> Optional[Conversation]:
        """
        Get conversation by participants (for user-to-user conversations)

        :param participants: List of user IDs participating in the conversation
        :return: Conversation object or None if not found
        """
        try:
            # Sort participants to ensure consistent ordering
            sorted_participants = sorted(participants)
            
            # Query for conversations with these exact participants
            result = self.db.query(
                "SELECT * FROM Conversation WHERE participants = $participants",
                {"participants": sorted_participants}
            )
            
            if result and isinstance(result, list) and len(result) > 0:
                return Conversation.from_dict(result[0])
            return None
            
        except Exception as e:
            logger.error(f"Error getting conversation by participants: {e}")
            return None
    
    def get_user_conversations(self, user_id: str) -> List[Conversation]:
        """
        Get all conversations for a user

        :param user_id: ID of the user
        :return: List of Conversation objects
        """
        try:
            result = self.db.query(
                "SELECT * FROM Conversation WHERE $user_id IN participants",
                {"user_id": user_id}
            )
            
            conversations = []
            if result and isinstance(result, list):
                for conv_data in result:
                    if isinstance(conv_data, dict):
                        conversations.append(Conversation.from_dict(conv_data))
            
            return conversations
            
        except Exception as e:
            logger.error(f"Error getting user conversations: {e}")
            return []
    
    def add_message(self, conversation_id: str, sender_id: str, text: str) -> Tuple[bool, str, Optional[Message]]:
        """
        Add a message to a conversation
        
        :param conversation_id: ID of the conversation
        :param sender_id: ID of the user sending the message
        :param text: Message text
        :return: (success, message, message_object)
        """
        try:
            # Verify conversation exists and user is a participant
            conversation = self.get_conversation_by_id(conversation_id)
            if not conversation:
                return False, "Conversation not found", None
            
            if not conversation.is_participant(sender_id):
                return False, "User is not a participant in this conversation", None
            
            # Create message
            message = Message(conversation_id, sender_id, text)
            
            # Save message to database
            result = self.db.create('Message', message.to_dict())
            logger.debug(f"Message create result: {result}")
            if isinstance(result, tuple):
                result = result[0]
            if isinstance(result, list) and len(result) > 0:
                result = result[0]
            if result and isinstance(result, dict):
                message.id = result.get('id')
                
                # Merge update: fetch full conversation, update last_message_at, write back
                conv_data = self.db.select(f"Conversation:{conversation_id}")
                logger.debug(f"Conversation data before update: {conv_data}")
                if conv_data and isinstance(conv_data, dict):
                    conv_data["last_message_at"] = message.created_at
                    update_result = self.db.update(f"Conversation:{conversation_id}", conv_data)
                    logger.debug(f"Conversation update result: {update_result}")
                    if isinstance(update_result, tuple):
                        update_result = update_result[0]
                    if isinstance(update_result, list) and len(update_result) > 0:
                        update_result = update_result[0]
                else:
                    logger.debug(f"Could not fetch conversation for safe update, skipping merge update.")
                
                return True, "Message sent successfully", message
            else:
                return False, "Failed to send message", None
                
        except Exception as e:
            return False, f"Error sending message: {str(e)}", None
    
    def get_conversation_messages(self, conversation_id: str, limit: int = 50) -> List[Message]:
        """
        Get messages for a conversation

        :param conversation_id: ID of the conversation
        :param limit: Maximum number of messages to retrieve
        :return: List of Message objects
        """
        try:
            result = self.db.query(
                "SELECT * FROM Message WHERE conversation_id = $conversation_id ORDER BY created_at DESC LIMIT $limit",
                {"conversation_id": conversation_id, "limit": limit}
            )
            
            messages = []
            if result and isinstance(result, list):
                for msg_data in result:
                    if isinstance(msg_data, dict):
                        messages.append(Message.from_dict(msg_data))
            
            # Reverse to get chronological order
            messages.reverse()
            return messages
            
        except Exception as e:
            logger.error(f"Error getting conversation messages: {e}")
            return []
    
    def mark_messages_as_read(self, conversation_id: str, user_id: str) -> bool:
        """
        Mark all messages in a conversation as read for a user

        :param conversation_id: ID of the conversation
        :param user_id: ID of the user marking messages as read
        :return: True if successful, False otherwise
        """
        try:
            result = self.db.query(
                "UPDATE Message SET is_read = true WHERE conversation_id = $conversation_id AND sender_id != $user_id",
                {"conversation_id": conversation_id, "user_id": user_id}
            )
            return True
            
        except Exception as e:
            logger.error(f"Error marking messages as read: {e}")
            return False
    
    def delete_conversation(self, conversation_id: str, user_id: str) -> Tuple[bool, str]:
        """
        Delete a conversation (only if user is a participant)

        :param conversation_id: ID of the conversation to delete
        :param user_id: ID of the user requesting the deletion
        :return: (success, message)
        """
        try:
            conversation = self.get_conversation_by_id(conversation_id)
            if not conversation:
                return False, "Conversation not found"
            
            if not conversation.is_participant(user_id):
                return False, "User is not a participant in this conversation"
            
            # Delete all messages first
            self.db.query(
                "DELETE FROM Message WHERE conversation_id = $conversation_id",
                {"conversation_id": conversation_id}
            )
            
            # Delete conversation
            self.db.delete(f"Conversation:{conversation_id}")
            
            return True, "Conversation deleted successfully"
            
        except Exception as e:
            return False, f"Error deleting conversation: {str(e)}" 