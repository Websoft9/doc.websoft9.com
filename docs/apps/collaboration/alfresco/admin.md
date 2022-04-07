---
sidebar_position: 3
slug: /alfresco/admin
tags:
  - Alfresco
  - 企业管理
  - ERP
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

### 备份

参考官方文档：[Back up and restore](https://docs.alfresco.com/content-services/community/admin/backup-restore/)

## 故障排除

#### 中文 Markdown 格式预览乱码？

故障描述：【在浏览器中查看】不乱码，但是在 Alfreco 内置 document-details 中乱码  
问题原因：未知  
解决方案：暂无  

## 问题解答

#### Alfresco 是否支持多语言？

支持（包含中文），后台可以自行切换

#### Alfresco Content Services Enterprise 和 Alfresco Community Edition 区别？

Alfresco Community Edition 是 Alfresco Content Services Enterprise 的开源版本，参考[对比](https://www.alfresco.com/alfresco-content-services-enterprise-vs-alfresco-community-edition)

#### Alfresco 支持哪些文件格式？

参考[Alfresco支持所有文件格式](https://www.alfresco.com.cn/alfresco-formats)

#### 本项目中 Alfresco 采用何种安装方式？

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