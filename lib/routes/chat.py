"""
Chat routes for managing conversations and messages.
"""
from typing import Tuple

from flask import request, jsonify, Response

from lib.services.auth_decorators import get_current_user
from lib.services.conversation_service import ConversationService
from lib.services.user_service import UserService
from lib.services.notifications import publish_event_with_buffer

from settings import logger


def create_conversation_route() -> Tuple[Response, int]:
    """
    Create a new conversation

    This endpoint allows users to create a new conversation with one or more participants.
    It ensures the current user is included in the participants and handles different conversation types.
    Participants must be provided in the request body, and at least two participants are required.
    The endpoint returns the conversation ID upon successful creation.
    If the request is invalid or the conversation cannot be created, an error message is returned.

    Example request body:
    {
        "participants": ["user1_id", "user2_id"],
        "type": "user_to_user"  # or "group", "ai_assistant", etc.
    }
    Example response:
    {
        "message": "Conversation created successfully",
        "conversation_id": "conv12345"
    }

    Error responses:
    {
        "error": "No data provided"
    }
    {
        "error": "At least 2 participants are required"
    }
    {
        "error": "Conversation creation failed: <reason>"
    }

    400 Bad Request if the request is invalid or conversation cannot be created.
    201 Created if the conversation is successfully created.

    :return: JSON response with success message and conversation ID or error message.
    """
    logger.debug(f"===== CONVERSATION CREATION ENDPOINT CALLED =====")
    current_user = get_current_user()
    if not current_user:
        logger.debug("Unauthorized access - no current user found")
        return jsonify({"error": "Unauthorized"}), 403

    current_user_id = current_user.user_id
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

def send_message_route(conversation_id: str) -> Tuple[Response, int]:
    """
    Send a message in a conversation

    This endpoint allows users to send a message in a specific conversation.
    It verifies that the conversation exists and that the user is a participant.
    The message text must be provided in the request body.
    If successful, it returns the message ID and timestamp.
    If the conversation does not exist or the user is not a participant, it returns an error.

    Example request body:
    {
        "text": "Hello, this is a message!"
    }

    Example response:
    {
        "message": "Message sent successfully",
        "message_id": "msg12345",
        "timestamp": "2023-10-01T12:00:00Z"
    }

    Error responses:
    {
        "error": "Message text is required"
    }
    {
        "error": "Conversation not found"
    }
    {
        "error": "Access denied"
    }
    {
        "error": "Failed to send message: <reason>"
    }

    200 OK if the message is sent successfully.
    400 Bad Request if the request is invalid or message cannot be sent.
    404 Not Found if the conversation does not exist.
    403 Forbidden if the user is not a participant in the conversation.

    :param conversation_id: The ID of the conversation to send the message in.
    :return: JSON response with success message and message details or error message.
    """
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

def get_conversation_messages_route(conversation_id: str) -> Tuple[Response, int]:
    """
    Get messages for a specific conversation

    This endpoint retrieves all messages in a specified conversation.
    It verifies that the conversation exists and that the user is a participant.
    If successful, it returns a list of messages with sender information and timestamps.
    If the conversation does not exist or the user is not a participant, it returns an error.

    Example response:
    {
        "messages": [
            {
                "id": "msg12345",
                "sender": "John Doe",
                "text": "Hello, this is a message!",
                "timestamp": "2023-10-01T12:00:00Z",
                "is_read": true
            },
            ...
        ]
    }

    Error responses:
    {
        "error": "Conversation not found"
    }
    {
        "error": "Access denied"
    }

    403 Forbidden if the user is not a participant in the conversation.
    404 Not Found if the conversation does not exist.
    200 OK if the messages are retrieved successfully.

    :param conversation_id: The ID of the conversation to retrieve messages from.
    :return: JSON response with a list of messages or an error message.
    """
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

def get_user_conversations_route() -> Tuple[Response, int]:
    """
    Get all conversations for the current user

    This endpoint retrieves all conversations that the current user is a participant in.
    It returns a list of conversations with basic details such as participants, last message preview,
    and conversation type (e.g., user-to-user, group, AI assistant).
    If the user has no conversations, it returns an empty list.
    If the user is not authenticated, it returns an error.

    Example response:
    {
        "conversations": [
            {
                "id": "conv12345",
                "name": "John Doe",
                "lastMessage": "Hello, this is a message!",
                "avatar": "https://ui-avatars.com/api/?name=John+Doe&background=random",
                "participantId": "user123",
                "isAI": false,
                "last_message_at": "2023-10-01T12:00:00Z"
            },
            ...
        ]
    }

    Error responses:
    {
        "error": "User not authenticated"
    }

    200 OK if conversations are retrieved successfully.
    403 Forbidden if the user is not authenticated.

    :return: JSON response with a list of conversations or an error message.
    """
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

