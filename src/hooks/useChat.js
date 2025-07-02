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

const CHAT_ENDPOINT = API_URL + '/api/chat';
const LLM_CHAT_ENDPOINT = API_URL + '/api/llm_chat';

function useChat(isLLM = false) {
    const [conversations, setConversations] = useState(DUMMY_CONVERSATIONS);
    const [selectedConversationId, setSelectedConversationId] = useState(conversations[0]?.id || 1);
    const [newMessage, setNewMessage] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    // Fetch conversations from the server
    useEffect(() => {
        const fetchConversations = async () => {
            try {
                const endpoint = isLLM ? LLM_CHAT_ENDPOINT : CHAT_ENDPOINT;
                const response = await fetch(endpoint);
                if (!response.ok) throw new Error('Failed to fetch conversations');
                const data = await response.json();
                console.log('Fetched conversations:', data);
                setConversations(data);
                if (data.length > 0 && !selectedConversationId) {
                    setSelectedConversationId(data[0].id);
                }
            } catch (error) {
                console.error('Error fetching conversations:', error);
                // Fallback to dummy data if fetch fails
                setConversations(DUMMY_CONVERSATIONS);
            }
        }

        fetchConversations();
    }, [isLLM]);

    const selectedConversation = conversations.find((conv) => conv.id === selectedConversationId);

    const handleSelectConversation = (id) => {
        setSelectedConversationId(id);
        setNewMessage('');
    };

    const handleSend = async () => {
        if (!newMessage.trim()) return;

        setIsLoading(true);

        try {
            if (isLLM) {
                // For LLM chat, send the message to the LLM endpoint
                const response = await fetch(LLM_CHAT_ENDPOINT, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ prompt: newMessage }),
                });

                if (!response.ok) throw new Error('Failed to get LLM response');
                
                const llmResponse = await response.json();
                console.log('LLM Response:', llmResponse);

                // Add both user message and LLM response to the conversation
                const updatedConversations = conversations.map((conv) => {
                    if (conv.id === selectedConversationId) {
                        return {
                            ...conv,
                            messages: [
                                ...conv.messages,
                                { sender: 'Me', text: newMessage },
                                { sender: 'AI Assistant', text: llmResponse.response || llmResponse.message || 'I received your message.' }
                            ],
                            lastMessage: newMessage
                        };
                    }
                    return conv;
                });

                setConversations(updatedConversations);
            } else {
                // For regular chat, just add the message locally
                const updatedConversations = conversations.map((conv) => {
                    if (conv.id === selectedConversationId) {
                        return {
                            ...conv,
                            messages: [...conv.messages, { sender: 'Me', text: newMessage }],
                            lastMessage: newMessage
                        };
                    }
                    return conv;
                });

                setConversations(updatedConversations);

                // Save to server
                await fetch(CHAT_ENDPOINT, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(updatedConversations),
                });
            }
        } catch (error) {
            console.error('Error sending message:', error);
            // Still add the message locally even if server call fails
            const updatedConversations = conversations.map((conv) => {
                if (conv.id === selectedConversationId) {
                    return {
                        ...conv,
                        messages: [...conv.messages, { sender: 'Me', text: newMessage }],
                        lastMessage: newMessage
                    };
                }
                return conv;
            });
            setConversations(updatedConversations);
        } finally {
            setIsLoading(false);
            setNewMessage('');
        }
    };

    return {
        conversations,
        selectedConversation,
        selectedConversationId,
        newMessage,
        setNewMessage,
        handleSelectConversation,
        handleSend,
        isLoading
    };
}

export { useChat };
