""""""
from flask import request, jsonify

from lib.services.auth_decorators import get_current_user
from lib.services.conversation_service import ConversationService
from lib.services.user_service import UserService
from lib.services.notifications import publish_event_with_buffer

from settings import logger


def create_conversation_route():
    """Create a new conversation"""
    logger.debug(f"===== CONVERSATION CREATION ENDPOINT CALLED =====")
    current_user_id = get_current_user().user_id
    data = request.json

    logger.debug(f"Creating conversation - current user: {current_user_id}")
    logger.debug(f"Request data: {data}")

    if not data:
        return jsonify({"error": "No data provided"}), 400

    participants = data.get('participants', [])
    conversation_type = data.get('type', 'user_to_user')

    logger.debug(f"Participants: {participants}")
    logger.debug(f"Conversation type: {conversation_type}")

    # Ensure current user is included in participants
    if current_user_id not in participants:
        participants.append(current_user_id)

    logger.debug(f"Final participants: {participants}")

    if len(participants) < 2:
        return jsonify({"error": "At least 2 participants are required"}), 400

    conversation_service = ConversationService()
    conversation_service.connect()
    try:
        success, message, conversation = conversation_service.create_conversation(participants, conversation_type)

        logger.debug(f"Conversation creation result - success: {success}, message: {message}")
        logger.debug(f"Conversation object: {conversation.to_dict() if conversation else None}")

        if success and conversation:
            return jsonify({
                "message": "Conversation created successfully",
                "conversation_id": conversation.id
            }), 201
        else:
            return jsonify({"error": message}), 400

    finally:
        conversation_service.close()

def send_message_route(conversation_id):
    """Send a message in a conversation"""
    logger.debug(f"===== SEND MESSAGE ENDPOINT CALLED =====")
    current_user_id = get_current_user().user_id
    data = request.json

    logger.debug(f"Sending message to conversation: {conversation_id}")
    logger.debug(f"Current user: {current_user_id}")
    logger.debug(f"Message data: {data}")

    if not data or 'text' not in data:
        return jsonify({"error": "Message text is required"}), 400

    message_text = data['text']

    conversation_service = ConversationService()
    conversation_service.connect()
    try:
        # Verify conversation exists and user is a participant
        logger.debug(f"Looking up conversation: {conversation_id}")
        conversation = conversation_service.get_conversation_by_id(conversation_id)
        if not conversation:
            logger.debug(f"Conversation not found: {conversation_id}")
            return jsonify({"error": "Conversation not found"}), 404

        logger.debug(f"Found conversation: {conversation.id}")
        if not conversation.is_participant(current_user_id):
            return jsonify({"error": "Access denied"}), 403

        # Add message
        logger.debug(f"Adding message to conversation")
        success, message, msg_obj = conversation_service.add_message(conversation_id, current_user_id, message_text)

        if success and msg_obj:
            logger.debug(f"Message sent successfully: {msg_obj.id}")
            
            # Publish notification to all other participants
            for participant_id in conversation.participants:
                if participant_id != current_user_id:
                    # Get sender info for notification
                    user_service = UserService()
                    user_service.connect()
                    try:
                        sender = user_service.get_user_by_id(current_user_id)
                        sender_name = sender.get_full_name() if sender else "Unknown User"
                    finally:
                        user_service.close()
                    
                    event_data = {
                        "type": "new_message",
                        "conversation_id": conversation_id,
                        "sender": sender_name,
                        "text": message_text,
                        "timestamp": str(msg_obj.created_at)
                    }
                    publish_event_with_buffer(participant_id, event_data)
            
            return jsonify({
                "message": "Message sent successfully",
                "message_id": msg_obj.id,
                "timestamp": msg_obj.created_at
            }), 200
        else:
            logger.debug(f"Failed to send message: {message}")
            return jsonify({"error": message}), 400

    finally:
        conversation_service.close()

def get_conversation_messages_route(conversation_id):
    """Get messages for a specific conversation"""
    current_user_id = get_current_user().user_id

    conversation_service = ConversationService()
    conversation_service.connect()
    try:
        # Verify user is a participant in this conversation
        conversation = conversation_service.get_conversation_by_id(conversation_id)
        if not conversation:
            return jsonify({"error": "Conversation not found"}), 404

        if not conversation.is_participant(current_user_id):
            return jsonify({"error": "Access denied"}), 403

        # Get messages
        messages = conversation_service.get_conversation_messages(conversation_id, limit=100)

        # Mark messages as read
        conversation_service.mark_messages_as_read(conversation_id, current_user_id)

        # Convert to frontend format
        message_list = []
        for msg in messages:
            # Get sender info
            user_service = UserService()
            user_service.connect()
            try:
                sender = user_service.get_user_by_id(msg.sender_id)
                sender_name = sender.get_full_name() if sender else "Unknown User"
            finally:
                user_service.close()

            message_list.append({
                "id": msg.id,
                "sender": sender_name if msg.sender_id != current_user_id else "Me",
                "text": msg.text,
                "timestamp": msg.created_at,
                "is_read": msg.is_read
            })

        return jsonify({"messages": message_list}), 200

    finally:
        conversation_service.close()

def get_user_conversations_route():
    """Get all conversations for the current user"""
    current_user_id = get_current_user().user_id

    logger.debug(f"Getting conversations for user: {current_user_id}")

    conversation_service = ConversationService()
    conversation_service.connect()
    try:
        conversations = conversation_service.get_user_conversations(current_user_id)
        logger.debug(f"Found {len(conversations)} conversations")
        for conv in conversations:
            logger.debug(f"Conversation: {conv.id} - {conv.participants} - {conv.conversation_type}")

        # Convert to frontend format
        conversation_list = []
        for conv in conversations:
            # Get the other participant's name for display
            other_participant_id = None
            for participant_id in conv.participants:
                if participant_id != current_user_id:
                    other_participant_id = participant_id
                    break

            # Get user info for the other participant
            user_service = UserService()
            user_service.connect()
            try:
                other_user = user_service.get_user_by_id(other_participant_id) if other_participant_id else None
                display_name = other_user.get_full_name() if other_user else "Unknown User"
                avatar = f"https://ui-avatars.com/api/?name={display_name}&background=random"
            finally:
                user_service.close()

            # Get last message for preview
            messages = conversation_service.get_conversation_messages(conv.id, limit=1)
            last_message = messages[-1].text if messages else "No messages yet"

            conversation_list.append({
                "id": conv.id,
                "name": display_name,
                "lastMessage": last_message,
                "avatar": avatar,
                "participantId": other_participant_id,
                "isAI": conv.conversation_type == "ai_assistant",
                "last_message_at": conv.last_message_at
            })

        return jsonify(conversation_list), 200

    finally:
        conversation_service.close()

