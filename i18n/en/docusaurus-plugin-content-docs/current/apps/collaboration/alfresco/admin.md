---
sidebar_position: 3
slug: /alfresco/admin
tags:
  - Alfresco
  - Collaboration and Productivity
  - ERP
---

# Alfresco Maintenance

This chapter is special guide for Alfresco maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Alfresco Backup 

Refer to official documentation：[Back up and restore](https://docs.alfresco.com/content-services/community/admin/backup-restore/)

## Troubleshoot{#troubleshoot}

In addition to the Alfresco issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### 中文 Markdown 格式预览乱码？

故障描述：【在浏览器中查看】不乱码，但是在 Alfreco 内置 document-details 中乱码  
问题原因：未知  
解决方案：暂无  

## FAQ{#faq}

#### Does Alfresco support multiple languages?

Yes, it automatically adapt according to the browser

#### What's different between Alfresco Content Services Enterprise and Alfresco Community Edition?

Alfresco Community Edition is the open source edition of Alfresco Content Services Enterprise, refer to [Comparison chart](https://www.alfresco.com/alfresco-content-services-enterprise-vs-alfresco-community-edition)

#### What file formats does Alfresco support?

Refer to [Alfresco-formats](https://www.alfresco.com.cn/alfresco-formats)

#### How was Alfresco installed in this solution?

Docker

#### Alfresco 数据存储目录在哪？

dir.root 目录中（有待进一步调研）

#### Alfresco 支持 Office 文档编辑与预览吗？

支持几十种格式的文件预览，也支持文本文件的在线编辑。  

但是针对 Office 文档，Alfresco 只能[离线编辑或集成 Google Docs](https://docs.alfresco.com/content-services/community/using/content/files-folders/)

#### 什么是 Alfresco 站点？

Alfresco 站点是用户的一个主页，可邀请其他用户在这个主页中创建和分享文档。

#### 什么是 Alfreco 元数据文件？

Alfreco 会自动对上传的文件提取一个[元数据文件](https://docs.alfresco.com/content-services/latest/develop/repo-ext-points/metadata-extractors/)，例如：如果有一个名为 的文件IMG_1967.jpg，会生产一个“影子”元数据文件 IMG_1967.jpg.metadata.properties.xml。