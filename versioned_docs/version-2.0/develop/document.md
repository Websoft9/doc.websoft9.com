---
sidebar_position: 3.1
slug: /document
---

# 文档规范

文档规范又可以称之为文档风格指南（Style Guide），它有助于保持文档整体风格的统一，给用户呈现一个一致的形象。  

技术写作者们真早就认识到了规范的重要性，像 [Write the Docs](https://www.writethedocs.org/guide/) 这样的社区，汇聚写作者的集体智慧，围绕创建软件文档的最佳实践。  


## 关键要点

Websoft9 文档是由集体创作，使用 Markdown 格式，由 [Docusaurus](https://docusaurus.io/) 生成，并遵循 DevOps 的持续集成原则。

下面是参与 Websoft9 文档需要注意的重要事项：

- 修改文档需提交 PR，等待审查与合并
- 涉及到第三方产品，优先明确功能的有无（点到即止），其次引用链接，避免编写指南
- 文档中已经存在答案，必须使用链接
- 尽量使用文字阐述清楚，减少截图的使用
- 力求使用统一的排版风格和[标准化词汇](./glossary)
- 文档主语言需考虑被翻译成其他语言，让 AI 和机器翻译工作更轻松、结果更准确

## 自动化

Websoft9 文档中的大多数页面都是用 Markdown 手动编写的。但是，某些页面是由自动化流程创建的。  

目前由两个 GitHub Action 自动化生产页面：

- GitHub Action 自动化生产页面：json2md.yml, app_header.yml
- 静态网站生成器自动化产生导航：左侧主导航、页面内容导航 

## 图片

图片存储位置存放各个语言的 docs 目录下的一级目录中的 assets 目录中，例如：

- 应用目录的图片存储目录：*docs/apps/assets*
- 程序环境目录的图片存储路径：*docs/runtime/assets*

图片名称约定：

- 应用图片名称：appname_xx_xx_websoft9.pnn
- Websoft9 平台的图片名称：websoft9_xx_xx_version.png

## 翻译

翻译的基本原则是对主语言进行内容同步与翻译，不包含基于主语言原版的扩展、删减或演绎等。  

翻译的基本流程：

1. 主语言的每一个页面的更改，都需要自动产生对应翻译页面的 Issue

2. 翻译文档的内容
   - 文字内容借助 AI和机器翻译（中译英时，要求 AI 限制单词数量往往会得到极高的翻译结果）
   - 图片需根据语言进行替换

## 应用文档

应用来自第三方，故编写应用文档时，主要目标是帮助用户立即上手使用，其次是方向指引。   

遵循的原则：

- 基于模板创建 md 文件
- 快速入门章节，针对于**初始化、快速使用、登录后台**等帮助用户立即上手的说明
- 配置选项章节，定位于告知用户准确的关于**功能有或无** 的信息，并提供准确的配置信息
- 管理维护章节，定位于通过准确的、简短的、点到即止的指引，帮助用户自行操作时有准确的方向
- 企业版章节，定位于 Websoft9 提供软件代理采购服务的指引
- 配置选项和管理维护章节，都不建议再增加下级标题


## 参考

以上未列出的规范，默认遵循以下的标准：   

- [Microsoft Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome)
- [GitLab Style Guide](https://docs.gitlab.com/ee/development/documentation/styleguide)
- [The Grand Unified Theory of Documentation](https://docs.divio.com/)
