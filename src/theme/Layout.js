// src/theme/Layout.js
import { useLocation } from '@docusaurus/router';
import OriginalLayout from '@theme-original/Layout';
import React, { useEffect } from 'react';

function useRemoveTrailingSlash() {
    const location = useLocation();

    useEffect(() => {
        const { pathname, search, hash } = location;
        if (pathname.length > 1 && pathname.endsWith('/')) {
            const newPath = pathname.slice(0, -1) + search + hash;
            window.history.replaceState(null, '', newPath);
        }
    }, [location]);
}

export default function Layout(props) {
    useRemoveTrailingSlash();

    return <OriginalLayout {...props} />;
}
