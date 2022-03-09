---
sidebar_position: 3
slug: /mediawiki/study
tags:
  - Mediawiki
  - CMS
  - 建站系统
  - 博客系统
---

# 原理学习

[MediaWiki](https://www.mediawiki.org) 是全球著名的开源wiki程序，采用 PHP+MySQL 开发。适合用于构建百科、知识库、在线文档、个人笔记等应用。超过数万个站点使用，大名鼎鼎的“维基百科”网站是基于这个软件而构建。MediaWiki的开发得到维基媒体基金会的支持。MediaWiki的最大作用在于对知识的归档，可用于构建企业/个人知识库，WIKI系统的思想是经过越多的人的编辑，结果就越趋于正确（完美）。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mediawiki/MediaWiki_UI.png)

## 指南

支撑 MediaWiki 运行的环境组件包括：PHP, MySQL, Apache or Nginx等，请根据不同的部署包分别查看对应的手册，完成更多配置。

| 部署包名称 | 说明| 参考项 |
| --- | --- | --- |
| MediaWiki(LAMP) | Apache+MySQL+PHP on Linux | [《LAMP管理员手册》](https://support.websoft9.com/docs/lamp/zh) |
| MediaWiki(LNMP)| Nginx+MySQL+PHP on Linux |[《LNMP管理员手册》](https://support.websoft9.com/docs/lnmp/zh)|

## 环境是什么？

除了使用 MediaWiki 部署包的默认设置之外，你可能需要在服务器上完成更多任务：

- 修改PHP配置文件
- 增加更多网站
- 配置HTTPS证书等
- 修改网站路径
- 绑定域名
- ...

完成这些任务，你都需要参考[环境指南](/zh/admin-runtime.md#指南)  

另外，你可能会思考，MediaWiki 是如何在这些环境下运行的呢？ 请参考下图的层次结构图

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/php-infra-websoft9.png)


## 演示

MediaWiki 官网提供了试用环境，您可以直接试用

* 演示地址：https://www.mediawiki.org/wiki/MediaWiki

> 免责说明：此处仅提供MediaWiki官方的演示，不保证与 Websoft9 部署包功能完全一致，若演示过程中若需要填写个人资料、获取Cookie等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此可能存在的商业纠纷与我司无关。

