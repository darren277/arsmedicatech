import { useState, useEffect } from 'react';
import API_URL from '../env_vars';

const DUMMY_CONVERSATIONS = [
  {
    id: 1,
    name: 'Jane Smith',
    lastMessage: 'Sounds good!',
    avatar: 'https://via.placeholder.com/40', // placeholder image if you like
    messages: [
      { sender: 'Jane Smith', text: 'Hi Dr. Carvolth, can we schedule an appointment?' },
      { sender: 'Me', text: 'Sure, does tomorrow at 3pm work?' },
      { sender: 'Jane Smith', text: 'Sounds good!' },
    ],
  },
  {
    id: 2,
    name: 'John Doe',
    lastMessage: 'Alright, thank you so much!',
    avatar: 'https://via.placeholder.com/40',
    messages: [
      { sender: 'John Doe', text: 'Hello Dr. Carvolth, I have a question about my medication.' },
      { sender: 'Me', text: 'Sure, what\'s on your mind?' },
      { sender: 'John Doe', text: 'Should I continue at the same dose?' },
      { sender: 'Me', text: 'Yes, please stay on the same dose until our next check-up.' },
      { sender: 'John Doe', text: 'Alright, thank you so much!' },
    ],
  },
  {
    id: 3,
    name: 'Emily Johnson',
    lastMessage: 'Will do, thanks!',
    avatar: 'https://via.placeholder.com/40',
    messages: [
      { sender: 'Emily Johnson', text: 'Dr. Carvolth, when is my next appointment?' },
      { sender: 'Me', text: 'Next Tuesday at 2 PM, does that still work?' },
      { sender: 'Emily Johnson', text: 'Yes, that\'s perfect! Thank you!' },
      { sender: 'Me', text: 'Great, see you then.' },
      { sender: 'Emily Johnson', text: 'Will do, thanks!' },
    ],
  },
];

const CHAT_ENDPOINT = '/api/chat';
const LLM_CHAT_ENDPOINT = API_URL + '/llm_chat';

function useChat(isLLM = false) {
    const [conversations, setConversations] = useState(DUMMY_CONVERSATIONS);
    const [selectedConversationId, setSelectedConversationId] = useState(conversations[0].id);
    const [newMessage, setNewMessage] = useState('');

    // Fetch conversations from the server (if applicable)
    useEffect(() => {
        const fetchConversations = async () => {
            try {
                const response = await fetch(isLLM ? LLM_CHAT_ENDPOINT : CHAT_ENDPOINT);
                if (!response.ok) throw new Error('Failed to fetch conversations');
                const data = await response.json();
                console.log('data', data);
                setConversations(data);
            } catch (error) {
                console.error('Error fetching conversations:', error);
            }
        }

        fetchConversations();
    }, []);

    // Save to server
    useEffect(() => {
        const saveConversations = async () => {
            try {
                const response = await fetch(CHAT_ENDPOINT, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(conversations),
                });
                if (!response.ok) throw new Error('Failed to save conversations');
            } catch (error) {
                console.error('Error saving conversations:', error);
            }
        };

        saveConversations();
    }, [conversations]);

    const selectedConversation = conversations.find((conv) => conv.id === selectedConversationId);

    const handleSelectConversation = (id) => {
        setSelectedConversationId(id);
        setNewMessage(''); // Clear out the message box
    };

    const handleSend = () => {
        if (!newMessage.trim()) return; // do nothing if empty

        const updatedConversations = conversations.map((conv) => {
            if (conv.id === selectedConversationId) {
                return {...conv, messages: [...conv.messages, { sender: 'Me', text: newMessage }], lastMessage: newMessage};
            }
            return conv;
        });

        setConversations(updatedConversations);
        setNewMessage(''); // Clear the input field
    };

    return {conversations, selectedConversation, selectedConversationId, newMessage, setNewMessage, handleSelectConversation, handleSend};
}

export { useChat };
