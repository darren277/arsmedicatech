from typing import List, Optional
from lib.db.surreal import DbController
from lib.models.llm_chat import LLMChat

class LLMChatService:
    def __init__(self, db_controller: DbController = None):
        self.db = db_controller or DbController()

    def connect(self):
        self.db.connect()

    def close(self):
        self.db.close()

    def get_llm_chats_for_user(self, user_id: str) -> List[LLMChat]:
        """Get all LLM chats for a user"""
        result = self.db.query(
            "SELECT * FROM LLMChat WHERE user_id = $user_id",
            {"user_id": user_id}
        )
        chats = []
        if result and isinstance(result, list):
            for chat_data in result:
                if isinstance(chat_data, dict):
                    chats.append(LLMChat.from_dict(chat_data))
        return chats

    def get_llm_chat(self, user_id: str, assistant_id: str) -> Optional[LLMChat]:
        """Get a specific LLM chat for a user and assistant"""
        result = self.db.query(
            "SELECT * FROM LLMChat WHERE user_id = $user_id AND assistant_id = $assistant_id",
            {"user_id": user_id, "assistant_id": assistant_id}
        )
        if result and isinstance(result, list) and len(result) > 0:
            return LLMChat.from_dict(result[0])
        return None

    def create_llm_chat(self, user_id: str, assistant_id: str) -> LLMChat:
        """Create a new LLM chat for a user and assistant"""
        chat = LLMChat(user_id=user_id, assistant_id=assistant_id)
        result = self.db.create('LLMChat', chat.to_dict())
        if result and isinstance(result, dict):
            chat.id = result.get('id')
        return chat

    def add_message(self, user_id: str, assistant_id: str, sender: str, text: str) -> LLMChat:
        """Add a message to the LLM chat, creating the chat if needed"""
        chat = self.get_llm_chat(user_id, assistant_id)
        if not chat:
            chat = self.create_llm_chat(user_id, assistant_id)
        chat.add_message(sender, text)
        # Save updated chat
        self.db.update(f"LLMChat:{chat.id.split(':', 1)[1]}", chat.to_dict())
        return chat 