// src/theme/Layout.js
import { useLocation } from '@docusaurus/router';
import OriginalLayout from '@theme-original/Layout';
import React, { useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

function useRemoveTrailingSlash() {
    const { i18n } = useDocusaurusContext();
    const location = useLocation();
    const history = useHistory();

    useEffect(() => {
        const { pathname, search, hash } = location;

        // 跳过多语言根路径（如 /en/、/zh-cn/）
        const isI18nRootPath = new RegExp(`^/(${i18n.locales.join('|')})/$`).test(pathname);
        if (isI18nRootPath) {
            return; // 保留多语言根路径的尾部斜杠
        }

        // 仅处理非多语言根路径的尾部斜杠
        if (pathname.length > 1 && pathname.endsWith('/')) {
            const newPath = pathname.slice(0, -1) + search + hash;
            console.log(`Redirecting from ${pathname} to ${newPath}`);
            history.replace(newPath);
        }
    }, [location, history, i18n.locales]);
}

export default function Layout(props) {
    useRemoveTrailingSlash();
    return <OriginalLayout {...props} />;
}