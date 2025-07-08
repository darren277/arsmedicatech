from datetime import datetime
from typing import List, Dict, Any, Optional

class LLMChat:
    def __init__(self, user_id: str, assistant_id: str = "ai-assistant", messages: Optional[List[Dict[str, Any]]] = None, created_at: Optional[str] = None, id: Optional[str] = None):
        self.user_id = user_id
        self.assistant_id = assistant_id
        self.messages = messages or []
        self.created_at = created_at or datetime.utcnow().isoformat()
        self.id = id

    def to_dict(self) -> Dict[str, Any]:
        return {
            "user_id": self.user_id,
            "assistant_id": self.assistant_id,
            "messages": self.messages,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'LLMChat':
        chat_id = data.get('id')
        if hasattr(chat_id, '__str__'):
            chat_id = str(chat_id)
        return cls(
            user_id=data.get('user_id'),
            assistant_id=data.get('assistant_id', 'ai-assistant'),
            messages=data.get('messages', []),
            created_at=data.get('created_at'),
            id=chat_id
        )

    def add_message(self, sender: str, text: str):
        self.messages.append({
            "sender": sender,
            "text": text,
            "timestamp": datetime.utcnow().isoformat()
        }) 