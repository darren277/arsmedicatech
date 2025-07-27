import { useEffect, useState } from 'react';
import apiService from '../services/api';
import logger from '../services/logging';
import { Conversation } from '../types';

const DUMMY_CONVERSATIONS: Conversation[] = [
  {
    id: 1,
    name: 'Jane Smith',
    lastMessage: 'Sounds good!',
    avatar: 'https://via.placeholder.com/40', // placeholder image if you like
    messages: [
      {
        sender: 'Jane Smith',
        text: 'Hi Dr. Carvolth, can we schedule an appointment?',
      },
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
      {
        sender: 'John Doe',
        text: 'Hello Dr. Carvolth, I have a question about my medication.',
      },
      { sender: 'Me', text: "Sure, what's on your mind?" },
      { sender: 'John Doe', text: 'Should I continue at the same dose?' },
      {
        sender: 'Me',
        text: 'Yes, please stay on the same dose until our next check-up.',
      },
      { sender: 'John Doe', text: 'Alright, thank you so much!' },
    ],
  },
  {
    id: 3,
    name: 'Emily Johnson',
    lastMessage: 'Will do, thanks!',
    avatar: 'https://via.placeholder.com/40',
    messages: [
      {
        sender: 'Emily Johnson',
        text: 'Dr. Carvolth, when is my next appointment?',
      },
      { sender: 'Me', text: 'Next Tuesday at 2 PM, does that still work?' },
      { sender: 'Emily Johnson', text: "Yes, that's perfect! Thank you!" },
      { sender: 'Me', text: 'Great, see you then.' },
      { sender: 'Emily Johnson', text: 'Will do, thanks!' },
    ],
  },
];

function useChat(isLLM = false) {
  const [conversations, setConversations] =
    useState<Conversation[]>(DUMMY_CONVERSATIONS);
  const [selectedConversationId, setSelectedConversationId] = useState<
    number | string | null
  >(conversations[0]?.id || null);
  const [newMessage, setNewMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  // Fetch conversations from the server
  useEffect(() => {
    let isMounted = true;

    const fetchConversations = async () => {
      try {
        let data: any;
        let aiConversations: any[] = [];

        if (isLLM) {
          data = await apiService.getLLMChatHistory('ai-assistant');
        } else {
          // Fetch both user conversations and AI conversations
          const [userConversations, llmChats] = await Promise.all([
            apiService.getUserConversations(),
            apiService.getLLMChatHistory('ai-assistant'),
          ]);

          data = userConversations;

          // Transform LLM chats into conversation format
          if (llmChats && llmChats.messages && llmChats.messages.length > 0) {
            aiConversations = [
              {
                id: 'ai-assistant',
                name: 'AI Assistant',
                lastMessage:
                  llmChats.messages[llmChats.messages.length - 1]?.text ||
                  'No messages yet',
                avatar: 'https://ui-avatars.com/api/?name=AI&background=random',
                messages: llmChats.messages || [],
                isAI: true,
                participantId: 'ai-assistant',
              },
            ];
          } else {
            // Always include AI Assistant conversation, even if no messages
            aiConversations = [
              {
                id: 'ai-assistant',
                name: 'AI Assistant',
                lastMessage: 'No messages yet',
                avatar: 'https://ui-avatars.com/api/?name=AI&background=random',
                messages: [],
                isAI: true,
                participantId: 'ai-assistant',
              },
            ];
          }
        }

        if (!isMounted) return;

        logger.debug('Fetched conversations:', data);
        logger.debug('Fetched AI conversations:', aiConversations);

        // Transform the data to match the frontend format
        let transformedData: any[] = [];
        if (data && Array.isArray(data)) {
          transformedData = data.map((conv: any) => ({
            id: conv.id,
            name: conv.name || 'Unknown User',
            lastMessage: conv.lastMessage || 'No messages yet',
            avatar:
              conv.avatar ||
              'https://ui-avatars.com/api/?name=User&background=random',
            messages: conv.messages || [],
            isAI: conv.isAI || false,
          }));
        }

        // Combine user conversations with AI conversations
        const allConversations = [...aiConversations, ...transformedData];

        if (!isMounted) return;

        // Preserve existing messages when updating conversations
        setConversations(prevConversations => {
          const updatedConversations = allConversations.map((newConv: any) => {
            // Find existing conversation with the same ID
            const existingConv = prevConversations.find(
              prev => prev.id === newConv.id
            );
            if (
              existingConv &&
              existingConv.messages &&
              existingConv.messages.length > 0
            ) {
              // Preserve existing messages
              return {
                ...newConv,
                messages: existingConv.messages,
              };
            }
            return newConv;
          });
          return updatedConversations;
        });

        // Only set selected conversation if none is currently selected
        setSelectedConversationId(currentId => {
          if (!currentId && allConversations.length > 0) {
            return allConversations[0].id;
          }
          return currentId;
        });
      } catch (error) {
        console.error('Error fetching conversations:', error);
        if (isMounted) {
          // Fallback to empty array if fetch fails
          setConversations([]);
          setSelectedConversationId(null);
        }
      }
    };

    fetchConversations();

    // Cleanup function to prevent memory leaks
    return () => {
      isMounted = false;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [isLLM]); // Only depend on isLLM to prevent infinite loops

  const selectedConversation = conversations.find(
    conv => conv.id === selectedConversationId
  );

  const handleSelectConversation = (id: number | string | null): void => {
    setSelectedConversationId(id);
    setNewMessage('');
  };

  const createNewConversation = (
    participantId: string,
    participantName: string,
    participantAvatar: string,
    isAI: boolean = false
  ) => {
    logger.debug(
      '[DEBUG] Creating new conversation with participantId:',
      participantId
    );

    // For database conversation IDs, we need to use the full ID string
    // For AI conversations, we use a timestamp
    const conversationId = isAI ? Date.now() : participantId;

    logger.debug('Using conversation ID:', conversationId);

    const newConversation: Conversation = {
      id: conversationId,
      name: isAI ? 'AI Assistant' : participantName,
      lastMessage: 'New conversation',
      avatar: participantAvatar,
      messages: [],
      participantId: participantId,
      isAI: isAI,
    };

    setConversations(prev => [newConversation, ...prev]);
    setSelectedConversationId(newConversation.id);
    setNewMessage('');
  };

  const handleSend = async () => {
    if (!newMessage.trim()) return;

    setIsLoading(true);

    try {
      if (isLLM) {
        // For LLM chat, send the message to the LLM endpoint using apiService
        const llmResponse = await apiService.sendLLMMessage(
          'ai-assistant',
          newMessage
        );
        logger.debug('LLM Response:', llmResponse);

        // Add both user message and LLM response to the conversation
        const updatedConversations = conversations.map(conv => {
          if (conv.id === selectedConversationId) {
            return {
              ...conv,
              messages: [
                ...conv.messages,
                { sender: 'Me', text: newMessage },
                {
                  sender: 'AI Assistant',
                  text:
                    llmResponse.response ||
                    llmResponse.message ||
                    'I received your message.',
                },
              ],
              lastMessage: newMessage,
            };
          }
          return conv;
        });

        setConversations(updatedConversations);
      } else {
        // For regular chat, add the message locally and send to server using apiService
        const updatedConversations = conversations.map(conv => {
          if (conv.id === selectedConversationId) {
            return {
              ...conv,
              messages: [...conv.messages, { sender: 'Me', text: newMessage }],
              lastMessage: newMessage,
            };
          }
          return conv;
        });

        setConversations(updatedConversations);

        // Save to server
        await apiService.sendChatMessage(newMessage);
      }
    } catch (error) {
      console.error('Error sending message:', error);
      // Still add the message locally even if server call fails
      const updatedConversations = conversations.map(conv => {
        if (conv.id === selectedConversationId) {
          return {
            ...conv,
            messages: [...conv.messages, { sender: 'Me', text: newMessage }],
            lastMessage: newMessage,
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
    setConversations,
    selectedConversation,
    selectedConversationId,
    newMessage,
    setNewMessage,
    handleSelectConversation,
    handleSend,
    createNewConversation,
    isLoading,
  };
}

export { useChat };
