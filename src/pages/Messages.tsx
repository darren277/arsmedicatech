import { useCallback, useEffect, useState } from 'react';
import NewConversationModal from '../components/NewConversationModal';
import { useNotificationContext } from '../components/NotificationContext';
import NotificationTest from '../components/NotificationTest';
import SignupPopup from '../components/SignupPopup';
import { Conversation, useChat } from '../hooks/useChat';
import useEvents from '../hooks/useEvents';
import { useNewConversationModal } from '../hooks/useNewConversationModal';
import { useSignupPopup } from '../hooks/useSignupPopup';
import apiService from '../services/api';
import authService from '../services/auth';
import './Messages.css';

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

const Messages = () => {
  const isAuthenticated = authService.isAuthenticated();
  const { isPopupOpen, showSignupPopup, hideSignupPopup } = useSignupPopup();
  const { isModalOpen, showModal, hideModal } = useNewConversationModal();
  const [selectedMessages, setSelectedMessages] = useState<
    { sender: string; text: string }[]
  >([]);

  // Initialize notification system
  const {
    notifications,
    unreadCount,
    addNotification,
    markAsRead,
    markAllAsRead,
    clearNotification,
    clearAllNotifications,
    getRecentNotifications,
  } = useNotificationContext();

  const {
    conversations,
    setConversations,
    selectedConversation,
    selectedConversationId,
    handleSelectConversation,
    newMessage,
    setNewMessage,
    handleSend,
    createNewConversation,
    isLoading,
  } = useChat(false); // Default to regular chat, will be overridden per conversation

  // Handle real-time notifications
  const handleNewMessage = useCallback(
    (data: any) => {
      console.log('Received new message notification:', data);

      // Add notification for new message
      addNotification({
        type: 'new_message',
        title: 'New Message',
        message: data.text,
        timestamp: data.timestamp,
        data: {
          sender: data.sender,
          conversation_id: data.conversation_id,
        },
      });

      // Update conversation list with new message
      setConversations(prevConversations =>
        prevConversations.map(conv => {
          if (conv.id.toString() === data.conversation_id) {
            return {
              ...conv,
              lastMessage: data.text,
            };
          }
          return conv;
        })
      );

      // If this conversation is currently selected, refresh messages
      if (selectedConversationId?.toString() === data.conversation_id) {
        // Refresh messages for the current conversation
        const fetchMessages = async () => {
          try {
            const response = await apiService.getConversationMessages(
              selectedConversationId.toString()
            );
            setSelectedMessages(
              (response.messages || []).map((msg: any) => ({
                sender: msg.sender,
                text: msg.text,
              }))
            );
          } catch (error) {
            console.error('Error refreshing messages:', error);
          }
        };
        fetchMessages();
      }
    },
    [selectedConversationId, setConversations, addNotification]
  );

  const handleAppointmentReminder = useCallback(
    (data: any) => {
      console.log('Received appointment reminder:', data);

      // Add notification for appointment reminder
      addNotification({
        type: 'appointment_reminder',
        title: 'Appointment Reminder',
        message: data.content,
        timestamp: data.timestamp,
        data: {
          appointmentId: data.appointmentId,
          time: data.time,
        },
      });
    },
    [addNotification]
  );

  const handleSystemNotification = useCallback(
    (data: any) => {
      console.log('Received system notification:', data);

      // Add notification for system notification
      addNotification({
        type: 'system_notification',
        title: 'System Notification',
        message: data.content,
        timestamp: data.timestamp,
        data: data,
      });
    },
    [addNotification]
  );

  // Initialize SSE connection
  useEvents({
    onNewMessage: handleNewMessage,
    onAppointmentReminder: handleAppointmentReminder,
    onSystemNotification: handleSystemNotification,
  });

  // Fetch messages when a conversation is selected
  useEffect(() => {
    const fetchMessages = async () => {
      if (!selectedConversationId || !selectedConversation) return;
      if (selectedConversation.isAI) {
        // For AI assistant, fetch from LLM chat history endpoint
        try {
          const assistantId =
            selectedConversation.participantId || 'ai-assistant';
          const response = await apiService.getLLMChatHistory(assistantId);
          setSelectedMessages(response.messages || []);
        } catch (error) {
          console.error('Error fetching LLM messages:', error);
          setSelectedMessages([]);
        }
        return;
      }
      try {
        const response = await apiService.getConversationMessages(
          selectedConversationId.toString()
        );
        // The backend returns { messages: [...] }
        setSelectedMessages(
          (response.messages || []).map((msg: any) => ({
            sender: msg.sender,
            text: msg.text,
          }))
        );
      } catch (error) {
        console.error('Error fetching messages:', error);
        setSelectedMessages([]);
      }
    };
    fetchMessages();
  }, [selectedConversationId, selectedConversation]);

  const handleSendMessage = async () => {
    if (!isAuthenticated) {
      showSignupPopup();
      return;
    }

    // Check if this is an AI conversation or user-to-user conversation
    if (selectedConversation?.isAI) {
      // Use LLM chat for AI conversations
      if (!newMessage.trim()) return;
      try {
        const assistantId =
          selectedConversation.participantId || 'ai-assistant';
        // Send message to LLM endpoint
        await apiService.sendLLMMessage(assistantId, newMessage);
        // Fetch updated LLM chat history for this assistant
        const response = await apiService.getLLMChatHistory(assistantId);
        setSelectedMessages(response.messages || []);
        setNewMessage('');
      } catch (error) {
        console.error('Error sending LLM message:', error);
      }
    } else {
      // Use regular chat for user-to-user conversations
      handleSendUserMessage();
    }
  };

  const handleSendUserMessage = async () => {
    if (!newMessage.trim() || !selectedConversation) return;

    const messageText = newMessage;
    setNewMessage(''); // Clear input immediately

    console.log(
      '[DEBUG] Sending user message to conversation:',
      selectedConversation.id
    );
    console.log('[DEBUG] Selected conversation:', selectedConversation);

    // Add message locally first for immediate feedback
    const updatedConversations = conversations.map(conv => {
      if (conv.id === selectedConversationId) {
        return {
          ...conv,
          messages: [...conv.messages, { sender: 'Me', text: messageText }],
          lastMessage: messageText,
        };
      }
      return conv;
    });

    // Update conversations state immediately for UI feedback
    // We need to update the conversations state since useChat doesn't handle user-to-user messages
    setConversations(updatedConversations);

    // Send message to backend
    try {
      await apiService.sendMessage(
        selectedConversation.id.toString(),
        messageText
      );
      console.log(
        'Message sent successfully to conversation:',
        selectedConversation.id
      );
    } catch (error) {
      console.error('Error sending message:', error);
      // In a real app, you might want to show an error message to the user
      // and potentially revert the local state change
    }
  };

  const handleStartChatbot = () => {
    // Create AI Assistant conversation
    createNewConversation(
      'ai-assistant',
      'AI Assistant',
      'https://ui-avatars.com/api/?name=AI&background=random',
      true
    );
  };

  const handleStartUserChat = async (
    userId: string,
    userInfo?: { display_name: string; avatar: string }
  ) => {
    console.log('[DEBUG] Starting user chat with:', userId, userInfo);
    try {
      // Create conversation in database
      console.log('[DEBUG] Creating conversation in database...');
      const response = await apiService.createConversation(
        [userId],
        'user_to_user'
      );
      console.log('[DEBUG] Conversation creation response:', response);

      if (response.conversation_id) {
        console.log(
          '[DEBUG] Creating conversation in frontend with ID:',
          response.conversation_id
        );
        // Create conversation in frontend with the database ID
        createNewConversation(
          response.conversation_id,
          userInfo?.display_name || 'Unknown User',
          userInfo?.avatar ||
            'https://ui-avatars.com/api/?name=User&background=random',
          false
        );
      } else {
        console.error('Failed to create conversation:', response);
      }
    } catch (error) {
      console.error('Error creating conversation:', error);
      // Fallback: create conversation locally
      console.log('[DEBUG] Falling back to local conversation creation');
      createNewConversation(
        userId,
        userInfo?.display_name || 'Unknown User',
        userInfo?.avatar ||
          'https://ui-avatars.com/api/?name=User&background=random',
        false
      );
    }
  };

  const handleNewConversation = () => {
    if (!isAuthenticated) {
      showSignupPopup();
      return;
    }
    showModal();
  };

  return (
    <>
      <div className="messages-container">
        {/* Left sidebar: conversation list */}
        <div className="conversations-list">
          <div className="conversation-list-header">
            <h3 className="conversation-list-title">Conversations</h3>
            <button
              className="new-conversation-button"
              onClick={handleNewConversation}
              title="Start new conversation"
            >
              <span className="button-icon">+</span>
            </button>
          </div>
          <ul>
            {conversations.map(conv => (
              <li
                key={conv.id}
                onClick={() => handleSelectConversation(conv.id)}
                className={
                  conv.id === selectedConversationId
                    ? 'conversation active'
                    : 'conversation'
                }
              >
                <img className="avatar" src={conv.avatar} alt={conv.name} />
                <div className="conversation-info">
                  <p className="conversation-name">{conv.name}</p>
                  <p className="conversation-last">{conv.lastMessage}</p>
                </div>
              </li>
            ))}
          </ul>
        </div>

        {/* Right side: chat window */}
        <div className="chat-window">
          {selectedConversation && (
            <>
              <div className="chat-header">
                <h3>{selectedConversation.name}</h3>
              </div>
              <div className="messages-list">
                {selectedMessages.map((msg, index) => (
                  <div
                    key={index}
                    className={msg.sender === 'Me' ? 'message me' : 'message'}
                  >
                    <div className="message-sender">{msg.sender}</div>
                    <div className="message-text">{msg.text}</div>
                  </div>
                ))}
                {isLoading && (
                  <div className="message">
                    <div className="message-sender">AI Assistant</div>
                    <div className="message-text">
                      <div className="loading-indicator">Thinking...</div>
                    </div>
                  </div>
                )}
              </div>
              <div className="message-input-container">
                <input
                  type="text"
                  placeholder={
                    isAuthenticated
                      ? 'Type a message...'
                      : 'Sign up to send messages...'
                  }
                  value={newMessage}
                  onChange={e => setNewMessage(e.target.value)}
                  onKeyPress={e => {
                    if (e.key === 'Enter' && !isLoading) {
                      handleSendMessage();
                    }
                  }}
                  disabled={isLoading || !isAuthenticated}
                />
                <button
                  onClick={handleSendMessage}
                  disabled={isLoading || !newMessage.trim() || !isAuthenticated}
                  className={!isAuthenticated ? 'send-button-disabled' : ''}
                >
                  {isLoading
                    ? 'Sending...'
                    : isAuthenticated
                      ? 'Send'
                      : 'Sign Up to Send'}
                </button>
              </div>
            </>
          )}
        </div>
      </div>

      {/* SSE Notification Test Component */}
      <NotificationTest />

      <SignupPopup isOpen={isPopupOpen} onClose={hideSignupPopup} />
      <NewConversationModal
        isOpen={isModalOpen}
        onClose={hideModal}
        onStartChatbot={handleStartChatbot}
        onStartUserChat={handleStartUserChat}
      />
    </>
  );
};

export default Messages;
