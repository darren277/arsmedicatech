import { useEffect, useState } from 'react';
import apiService from '../services/api';
import logger from '../services/logging';
import { Conversation } from '../types';

function useChat(isLLM = false) {
  // Initialize conversations from localStorage if available
  const getInitialConversations = (): Conversation[] => {
    try {
      const stored = localStorage.getItem('chat-conversations');
      return stored ? JSON.parse(stored) : [];
    } catch (error) {
      console.error('Error loading conversations from localStorage:', error);
      return [];
    }
  };

  const [conversations, setConversations] = useState<Conversation[]>(
    getInitialConversations
  );
  // Initialize selected conversation ID from localStorage if available
  const getInitialSelectedId = (): number | string | null => {
    try {
      const stored = localStorage.getItem('chat-selected-conversation');
      return stored ? JSON.parse(stored) : conversations[0]?.id || null;
    } catch (error) {
      console.error(
        'Error loading selected conversation from localStorage:',
        error
      );
      return conversations[0]?.id || null;
    }
  };

  const [selectedConversationId, setSelectedConversationId] = useState<
    number | string | null
  >(getInitialSelectedId);
  const [newMessage, setNewMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  // Save conversations to localStorage whenever they change
  const saveConversationsToStorage = (conversations: Conversation[]) => {
    try {
      localStorage.setItem('chat-conversations', JSON.stringify(conversations));
    } catch (error) {
      console.error('Error saving conversations to localStorage:', error);
    }
  };

  // Save selected conversation ID to localStorage
  const saveSelectedConversationToStorage = (id: number | string | null) => {
    try {
      localStorage.setItem('chat-selected-conversation', JSON.stringify(id));
    } catch (error) {
      console.error(
        'Error saving selected conversation to localStorage:',
        error
      );
    }
  };

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

          // For multiple AI conversations, we don't automatically create one
          // Users will create new AI conversations as needed
          aiConversations = [];
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
          saveConversationsToStorage(updatedConversations);
          return updatedConversations;
        });

        // Only set selected conversation if none is currently selected
        setSelectedConversationId(currentId => {
          const newId =
            !currentId && allConversations.length > 0
              ? allConversations[0].id
              : currentId;
          saveSelectedConversationToStorage(newId);
          return newId;
        });
      } catch (error) {
        console.error('Error fetching conversations:', error);
        if (isMounted) {
          // Fallback to empty array if fetch fails
          saveConversationsToStorage([]);
          setConversations([]);
          saveSelectedConversationToStorage(null);
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
    saveSelectedConversationToStorage(id);
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

    // For AI conversations, generate a unique ID using timestamp
    // For user conversations, use the participantId
    const conversationId = isAI ? `ai-assistant-${Date.now()}` : participantId;

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

    setConversations(prev => {
      const updatedConversations = [newConversation, ...prev];
      saveConversationsToStorage(updatedConversations);
      return updatedConversations;
    });
    saveSelectedConversationToStorage(newConversation.id);
    setSelectedConversationId(newConversation.id);
    setNewMessage('');
  };

  const handleSend = async () => {
    if (!newMessage.trim()) return;

    setIsLoading(true);

    try {
      if (isLLM) {
        // For LLM chat, send the message to the LLM endpoint using apiService
        // Use the selected conversation ID for AI conversations
        const conversationId =
          selectedConversationId?.toString() || 'ai-assistant';
        const llmResponse = await apiService.sendLLMMessage(
          conversationId,
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

        saveConversationsToStorage(updatedConversations);
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

        saveConversationsToStorage(updatedConversations);
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
      saveConversationsToStorage(updatedConversations);
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
