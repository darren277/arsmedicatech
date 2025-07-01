import React, { useState, useEffect, useRef } from 'react';
import SearchBox      from "./SearchBox";
import { ProfilePanel }   from "./ProfilePanel";


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
    return (
        <header className="topbar">
            <div className="search-container">
                <SearchBox value={props.query} onChange={props.onQueryChange} loading={props.loading} />
            </div>

            <ProfilePanel />
        </header>
    );
}
