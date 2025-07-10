import { useCallback, useState } from 'react';

export const useSignupPopup = () => {
  const [isPopupOpen, setIsPopupOpen] = useState(false);

  const showSignupPopup = useCallback(() => {
    setIsPopupOpen(true);
  }, []);

  const hideSignupPopup = useCallback(() => {
    setIsPopupOpen(false);
  }, []);

  return {
    isPopupOpen,
    showSignupPopup,
    hideSignupPopup,
  };
};
