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
    def __init__(self, event_type: str, data: dict):
        self.event_type = event_type
        self.data = data
