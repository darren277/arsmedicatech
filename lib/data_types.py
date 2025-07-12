"""
Type definitions for the application.
"""

class UserID(str):
    """
    Custom UserID type for better type safety.
    Inherits from str to allow direct string usage.

    Format: `User:{user_id}`
    """
    pass


class PatientID(str):
    """
    Custom PatientID type for better type safety.
    Inherits from str to allow direct string usage.

    Format: `Patient:{patient_id}`
    """
    pass


class EventData:
    """
    Custom EventData type for better type safety.
    """
    def __init__(self, event_type: str, conversation_id: str, sender: str, text: str, timestamp: str) -> None:
        """
        Initialize an EventData instance.
        """
        self.event_type = event_type
        self.conversation_id = conversation_id
        self.sender = sender
        self.text = text
        self.timestamp = timestamp
