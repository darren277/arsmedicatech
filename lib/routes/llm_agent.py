"""
LLM Agent Endpoint
"""
import asyncio
from typing import Any, Dict, Optional, Tuple, cast

from flask import Response, g, jsonify, request, session

from lib.data_types import UserID
from lib.llm.agent import LLMAgent, LLMModel
from lib.services.llm_chat_service import LLMChatService
from lib.services.openai_security import get_openai_security_service
from settings import MCP_URL, logger


def llm_agent_endpoint_route() -> Tuple[Response, int]:
    """
    Route for the LLM agent endpoint.
    :return: Response object with JSON data or error message.
    """
    logger.debug('[DEBUG] /api/llm_chat called')
    logger.debug('[DEBUG] Request headers: %s', str(dict(request.headers)))
    current_user_id: Optional[str] = None
    session: Dict[str, Any]  # Explicitly define this for type-checking
    if hasattr(g, 'user') and g.user:
        current_user_id = g.user.user_id
    elif 'user_id' in session: # type: ignore
        user_id: Optional[str] = cast(Optional[str], session.get("user_id")) # type: ignore
        if not user_id:
            logger.debug('[DEBUG] No user_id in session')
            return jsonify({"error": "Not authenticated"}), 401
        current_user_id = str(user_id)
    else:
        logger.debug('[DEBUG] Not authenticated in /api/llm_chat')
        return jsonify({"error": "Not authenticated"}), 401

    llm_chat_service = LLMChatService()
    llm_chat_service.connect()
    try:
        if request.method == 'GET':
            chats = llm_chat_service.get_llm_chats_for_user(UserID(current_user_id))
            return jsonify([chat.to_dict() for chat in chats]), 200
        elif request.method == 'POST':
            data: Optional[Dict[str, Any]] = request.json
            if data is None:
                return jsonify({"error": "Invalid JSON data"}), 400
                
            assistant_id = data.get('assistant_id', 'ai-assistant')
            prompt = data.get('prompt')
            if not prompt:
                return jsonify({"error": "No prompt provided"}), 400

            # Get user's OpenAI API key with security validation
            security_service = get_openai_security_service()
            openai_api_key, error = security_service.get_user_api_key_with_validation(str(current_user_id))
            
            if not openai_api_key:
                return jsonify({"error": error}), 400

            # Add user message to persistent chat
            chat = llm_chat_service.add_message(UserID(current_user_id), assistant_id, 'Me', prompt)

            agent = asyncio.run(
                LLMAgent.from_mcp(
                    mcp_url=MCP_URL,
                    api_key=openai_api_key,
                    model={"name": LLMModel.GPT_4_1_NANO.value},  # Pass as keyword argument
                )
            )

            # Use the persistent chat history as context
            history: list[Dict[str, Any]] = chat.messages
            print(f"History: {history}")  # Debugging line to check history content
            # You may want to format this for your LLM
            response = asyncio.run(agent.complete(prompt))  # Remove history parameter as it's not supported
            logger.debug('response', type(response), response)

            # Log API usage
            if current_user_id is None:
                logger.error("current_user_id is None when logging API usage")
                return jsonify({"error": "User ID is missing"}), 400
            security_service.log_api_usage(str(current_user_id), str(LLMModel.GPT_4_1_NANO))

            # Add assistant response to persistent chat
            chat = llm_chat_service.add_message(UserID(current_user_id), assistant_id, 'AI Assistant',
                                                response.get('response', ''))

            # Save updated agent state to session
            session['agent_data'] = agent.to_dict() # type: ignore

            return jsonify(chat.to_dict()), 200
        else:
            return jsonify({"error": "Method not allowed"}), 405
    except Exception as e:
        logger.error(f"Error in llm_agent_endpoint: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        llm_chat_service.close()
