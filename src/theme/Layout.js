// // src/theme/Layout.js
// import { useLocation } from '@docusaurus/router';
// import OriginalLayout from '@theme-original/Layout';
// import React, { useEffect } from 'react';
// import { useHistory } from 'react-router-dom';

// function useRemoveTrailingSlash() {
//     const location = useLocation();
//     const history = useHistory();

//     useEffect(() => {
//         const { pathname, search, hash } = location;
//         if (pathname.length > 1 && pathname.endsWith('/')) {
//             const newPath = pathname.slice(0, -1) + search + hash;
//             console.log(`old pathname: ${pathname}, Redirecting to: ${newPath}`);
//             // 使用 history.replace 以避免页面刷新
//             history.replace(newPath);
//         }
//     }, [location, history]);
// }

// export default function Layout(props) {
//     useRemoveTrailingSlash();

//     return <OriginalLayout {...props} />;
// }

// //window.history.replaceState(null, '', newPath);
// //window.location.replace(newPath);
