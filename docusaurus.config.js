// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

// const lightCodeTheme = require('prism-react-renderer/themes/github');
// const darkCodeTheme = require('prism-react-renderer/themes/dracula');

const { themes } = require('prism-react-renderer');
const lightTheme = themes.github;
const darkTheme = themes.dracula;

const fs = require('fs');
const path = require('path'); // 确保引入 path 模块

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Websoft9',
  tagline: '多应用自托管平台，可视化一键部署软件',
  url: 'https://support.websoft9.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'throw',
  onDuplicateRoutes: 'throw',
  favicon: 'img/favicon.ico',
  organizationName: 'Websoft9', // Usually your GitHub org/user name.
  deploymentBranch: 'main',
  projectName: 'doc.websoft9.com', // Usually your repo name.
  i18n: {
    defaultLocale: 'zh-cn',
    locales: ['zh-cn', 'en'],
  },

  plugins: [
    [
      '@docusaurus/plugin-client-redirects',
      {
        redirects: [
          {
            to: './elasticsearch',
            from: ['/docs/elk', '/docs/elastic'],
          },
          {
            to: './php',
            from: ['/docs/phpfpmapache', '/docs/phpfpmnginx'],
          }
        ],
      },
    ],
  ],


  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          showLastUpdateTime: true,
          sidebarPath: require.resolve('./sidebars.js'),
          lastVersion: '2.0',
          includeCurrentVersion: false,
          // Please change this to your repo.
          editUrl: 'https://github.com/websoft9/doc.websoft9.com/tree/dev',
          // exclude: ['**/apps/**']
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/websoft9/doc.websoft9.com/tree/main/blog',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],
  // themes: ['docusaurus-theme-search-typesense'],
  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Websoft9',
        logo: {
          alt: 'Websoft9 Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'doc',
            docId: 'readme',
            position: 'left',
            label: '文档',
          },

          { to: 'https://support.websoft9.com/apidocs', label: 'API', position: 'left' },

          {
            type: 'doc',
            docId: 'business/helpdesk',
            position: 'left',
            label: '技术支持',
          },

          {
            type: 'docsVersionDropdown',
            position: 'right',
          },

          { type: 'localeDropdown', position: 'right', },

          {
            href: 'https://github.com/websoft9/doc.websoft9.com',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      // typesense: {
      //   typesenseCollectionName: 'websoft9', // Replace with your own doc site's name. Should match the collection name in the scraper settings.
      //   // typesenseCollectionName: 'docusaurus-2',
      //   typesenseServerConfig: {
      //     nodes: [
      //       {
      //         host: 'search.www.websoft9.com',
      //         port: 443,
      //         protocol: 'https',
      //       },
      //     ],
      //     apiKey: 'cJ9XqddokC3OCRdx1SFQRv+uFj5QHYOT',
      //   },
      //   // Optional: Typesense search parameters: https://typesense.org/docs/0.21.0/api/documents.md#search-parameters
      //   typesenseSearchParameters: {},

      //   // Optional
      //   contextualSearch: true,
      // },
      algolia: {
        // The application ID provided by Algolia
        appId: 'NA4GDUSQ4H',

        // Public API key: it is safe to commit it
        apiKey: 'b08bd00265bc22ae49e3a6acd38868c8',

        indexName: 'support-websoft9',

        // Optional: see doc section below
        contextualSearch: true,

        // Optional: Specify domains where the navigation should occur through window.location instead on history.push. Useful when our Algolia config crawls multiple documentation sites and we want to navigate with window.location.href to them.
        externalUrlRegex: 'external\\.com|domain\\.com',

        // Optional: Replace parts of the item URLs from Algolia. Useful when using the same search index for multiple deployments using a different baseUrl. You can use regexp or string in the `from` param. For example: localhost:3000 vs myCompany.com/docs
        // replaceSearchResultPathname: {
        //   from: '/docs/', // or as RegExp: /\/docs\//
        //   to: '/',
        // },

        // Optional: Algolia search parameters
        searchParameters: {},

        // Optional: path for search page that enabled by default (`false` to disable it)
        searchPagePath: 'search',

        // Optional: whether the insights feature is enabled or not on Docsearch (`false` by default)
        insights: false,

        //... other Algolia params
      },


      footer: {
        style: 'dark',
        links: [
          {
            title: '产品与服务',
            items: [
              {
                label: '应用',
                to: 'https://www.websoft9.com/apps',
              },
              {
                label: '解决方案',
                to: 'https://www.websoft9.com/solutions',
              },
              {
                label: '技术服务',
                to: 'https://www.websoft9.com/services',
              },
              {
                label: '分发服务',
                to: 'https://www.websoft9.com/services/business-process-outsourcing/cloud-distribution-for-isv',
              },


            ],
          },
          {
            title: '技术支持',
            items: [
              {
                label: '文档 ',
                href: '/',
              },

              {
                label: 'FAQ ',
                href: '/docs/faq',
              },
              {
                label: '7×24 工单',
                href: 'https://www.websoft9.com/ticket',
              },
              {
                label: '人工支持',
                href: 'https://www.websoft9.com/contact-us',
              },
            ],
          },
          {
            title: '资源',
            items: [
              {
                label: '博客',
                to: 'https://www.websoft9.com/blog',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/websoft9',
              },
            ],
          },
        ],

        logo: {
          alt: 'Websoft9 Open Source Logo',
          src: 'img/logo.svg',
          width: 160,
          height: 51,
          href: 'https://www.websoft9.com',
        },
        copyright: `Copyright ©2014- ${new Date().getFullYear()} 长沙网久软件有限公司 备案：湘ICP备16009117号`,
      },

      // prism: {
      //   theme: lightCodeTheme,
      //   darkTheme: darkCodeTheme,
      // },
      prism: {
        additionalLanguages: ['bash', 'diff', 'json'],
      },
      tableOfContents: {
        minHeadingLevel: 2,
        maxHeadingLevel: 4
      }
    }),
};

module.exports = config;
