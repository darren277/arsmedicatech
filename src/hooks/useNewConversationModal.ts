import { useState } from 'react';

export const useNewConversationModal = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const showModal = () => {
    setIsModalOpen(true);
  };

  const hideModal = () => {
    setIsModalOpen(false);
  };

  return {
    isModalOpen,
    showModal,
    hideModal,
  };
};
