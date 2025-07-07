import SignupPopup from '../components/SignupPopup';
import { useChat } from '../hooks/useChat';
import { useSignupPopup } from '../hooks/useSignupPopup';
import authService from '../services/auth';
import './Messages.css';

const DUMMY_CONVERSATIONS = [
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
  const isLLM = true;
  const isAuthenticated = authService.isAuthenticated();
  const { isPopupOpen, showSignupPopup, hideSignupPopup } = useSignupPopup();

  const {
    conversations,
    selectedConversation,
    selectedConversationId,
    handleSelectConversation,
    newMessage,
    setNewMessage,
    handleSend,
    isLoading,
  } = useChat(isLLM);

  const handleSendMessage = () => {
    if (!isAuthenticated) {
      showSignupPopup();
      return;
    }
    handleSend();
  };

  return (
    <>
      <div className="messages-container">
        {/* Left sidebar: conversation list */}
        <div className="conversations-list">
          <h3 className="conversation-list-title">Conversations</h3>
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
                {selectedConversation.messages.map((msg, index) => (
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
      <SignupPopup isOpen={isPopupOpen} onClose={hideSignupPopup} />
    </>
  );
};

export default Messages;
