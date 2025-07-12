"""
Dummy data for testing purposes
"""

id, name, lastMessage, avatar, messages, sender, text = 'id', 'name', 'lastMessage', 'avatar', 'messages', 'sender', 'text'

DUMMY_CONVERSATIONS = [
  {
    "id": 1,
    "name": "Jane Smith",
    "lastMessage": "Sounds good!",
    "avatar": "https://via.placeholder.com/40",
    "messages": [
      { "sender": "Jane Smith", "text": "Hi Dr. Carvolth, can we schedule an appointment?" },
      { "sender": "Me", "text": "Sure, does tomorrow at 3pm work?" },
      { "sender": "Jane Smith", "text": "Sounds good!" },
    ],
  },
  {
    "id": 2,
    "name": "John Doe",
    "lastMessage": "Alright, thank you so much!",
    "avatar": "https://via.placeholder.com/40",
    "messages": [
      { "sender": "John Doe", "text": "Hello Dr. Carvolth, I have a question about my medication." },
      { "sender": "Me", "text": "Sure, what's on your mind?" },
      { "sender": "John Doe", "text": "Should I continue at the same dose?" },
      { "sender": "Me", "text": "Yes, please stay on the same dose until our next check-up." },
      { "sender": "John Doe", "text": "Alright, thank you so much!" },
    ],
  },
  {
    "id": 3,
    "name": "Emily Johnson",
    "lastMessage": "Will do, thanks!",
    "avatar": "https://via.placeholder.com/40",
    "messages": [
      { "sender": "Emily Johnson", "text": "Dr. Carvolth, when is my next appointment?" },
      { "sender": "Me", "text": "Next Tuesday at 2 PM, does that still work?" },
      { "sender": "Emily Johnson", "text": "Yes, that's perfect! Thank you!" },
      { "sender": "Me", "text": "Great, see you then." },
      { "sender": "Emily Johnson", "text": "Will do, thanks!" },
    ],
  }
]


john_doe_history = [
    {"date": "2021-01-01", "note": "Patient has a fever."},
    {"date": "2021-01-02", "note": "Patient has a cough."},
    {"date": "2021-01-03", "note": "Patient has a headache."}
]

jane_doe_history = [
    {"date": "2021-01-01", "note": "Patient has a fever."},
    {"date": "2021-01-02", "note": "Patient has a cough."},
    {"date": "2021-01-03", "note": "Patient has a headache."}
]

