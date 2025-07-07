import React, { useState, useEffect, useRef } from 'react';
import SearchBox      from "./SearchBox";
import { ProfilePanel }   from "./ProfilePanel";
import authService from '../services/auth';
import { useSignupPopup } from '../hooks/useSignupPopup';
import SignupPopup from './SignupPopup';


/*
interface Props {
    query: string;
    onQueryChange(q: string): void;
    results: any[];
    loading: boolean;
}
*/

//export default function Topbar(props: Props) {
export default function Topbar(props) {
    const isAuthenticated = authService.isAuthenticated();
    const { isPopupOpen, showSignupPopup, hideSignupPopup } = useSignupPopup();

    return (
        <>
            <header className="topbar">
                <div className="search-container">
                    <SearchBox value={props.query} onChange={props.onQueryChange} loading={props.loading} />
                </div>

                <div className="auth-status">
                    {isAuthenticated ? (
                        <ProfilePanel />
                    ) : (
                        <div className="guest-auth">
                            <span className="guest-label">Guest User</span>
                            <button onClick={showSignupPopup} className="auth-button">
                                Sign Up / Login
                            </button>
                        </div>
                    )}
                </div>
            </header>
            <SignupPopup 
                isOpen={isPopupOpen} 
                onClose={hideSignupPopup}
            />
        </>
    );
}
