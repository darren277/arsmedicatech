""""""
import asyncio

from flask import request, jsonify, session, g

from lib.llm.agent import LLMAgent, LLMModel, MCP_URL
from lib.services.llm_chat_service import LLMChatService

# TODO: Attach this to use via user settings UI:
from settings import OPENAI_API_KEY


def llm_agent_endpoint_route():
    print('[DEBUG] /api/llm_chat called')
    print('[DEBUG] Request headers:', dict(request.headers))
    print('[DEBUG] Session:', dict(session))
    current_user_id = None
    if hasattr(g, 'user') and g.user:
        current_user_id = g.user.user_id
    elif 'user_id' in session:
        current_user_id = session['user_id']
    else:
        print('[DEBUG] Not authenticated in /api/llm_chat')
        return jsonify({"error": "Not authenticated"}), 401

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
                return jsonify({"error": "No prompt provided"}), 400

            # Add user message to persistent chat
            chat = llm_chat_service.add_message(current_user_id, assistant_id, 'Me', prompt)

            agent = asyncio.run(
                LLMAgent.from_mcp(
                    mcp_url=MCP_URL,
                    api_key=OPENAI_API_KEY,
                    model=LLMModel.GPT_4_1_NANO,
                )
            )

            # Use the persistent chat history as context
            history = chat.messages
            # You may want to format this for your LLM
            response = agent.complete(prompt, history=history)

            # Add assistant response to persistent chat
            chat = llm_chat_service.add_message(current_user_id, assistant_id, 'AI Assistant',
                                                response.get('response', ''))

            # Save updated agent state to session
            session['agent_data'] = agent.to_dict()

            return jsonify(chat.to_dict())
    finally:
        llm_chat_service.close()
