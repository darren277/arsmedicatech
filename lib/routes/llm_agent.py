"""
LLM Agent Endpoint
"""
import asyncio

from flask import request, jsonify, session, g, Response

from settings import MCP_URL

from lib.llm.agent import LLMAgent, LLMModel
from lib.services.llm_chat_service import LLMChatService
from lib.services.openai_security import get_openai_security_service

from settings import logger


def llm_agent_endpoint_route() -> Response:
    """
    Route for the LLM agent endpoint.
    :return: Response object with JSON data or error message.
    """
    logger.debug('[DEBUG] /api/llm_chat called')
    logger.debug('[DEBUG] Request headers:', dict(request.headers))
    logger.debug('[DEBUG] Session:', dict(session))
    current_user_id = None
    if hasattr(g, 'user') and g.user:
        current_user_id = g.user.user_id
    elif 'user_id' in session:
        current_user_id = session['user_id']
    else:
        logger.debug('[DEBUG] Not authenticated in /api/llm_chat')
        return jsonify({"error": "Not authenticated"}, 401)

    llm_chat_service = LLMChatService()
    llm_chat_service.connect()
    try:
        if request.method == 'GET':
            chats = llm_chat_service.get_llm_chats_for_user(current_user_id)
            return jsonify([chat.to_dict() for chat in chats])
        elif request.method == 'POST':
            data = request.json
            assistant_id = data.get('assistant_id', 'ai-assistant')
            prompt = data.get('prompt')
            if not prompt:
                return jsonify({"error": "No prompt provided"}, 400)

            # Get user's OpenAI API key with security validation
            security_service = get_openai_security_service()
            openai_api_key, error = security_service.get_user_api_key_with_validation(current_user_id)
            
            if not openai_api_key:
                return jsonify({"error": error}, 400)

            # Add user message to persistent chat
            chat = llm_chat_service.add_message(current_user_id, assistant_id, 'Me', prompt)

            agent = asyncio.run(
                LLMAgent.from_mcp(
                    mcp_url=MCP_URL,
                    api_key=openai_api_key,
                    model=LLMModel.GPT_4_1_NANO,
                )
            )

            # Use the persistent chat history as context
            history = chat.messages
            # You may want to format this for your LLM
            response = asyncio.run(agent.complete(prompt, history=history))
            logger.debug('response', type(response), response)

            # Log API usage
            security_service.log_api_usage(current_user_id, str(LLMModel.GPT_4_1_NANO))

            # Add assistant response to persistent chat
            chat = llm_chat_service.add_message(current_user_id, assistant_id, 'AI Assistant',
                                                response.get('response', ''))

            # Save updated agent state to session
            session['agent_data'] = agent.to_dict()

            return jsonify(chat.to_dict())
    finally:
        llm_chat_service.close()
