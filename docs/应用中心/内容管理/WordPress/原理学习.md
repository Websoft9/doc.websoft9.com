---
sidebar_position: 3
slug: /wordpress/study
tags:
  - WordPress
  - CMS
  - 建站系统
  - 博客系统
---

# 原理学习

[WordPress](https://wordpress.org) 简称WP，最初是一款博客系统，后逐步演化成一款功能强大的企业级 CMS（内容管理/建站系统），目前是公认的全球最佳建站系统，互联网上有34%的网站都基于 WordPress构建。这套系统因易用性、易扩展性（ 插件 、模板、二次开发）、功能强大、美观、搜索引擎友好等而全世界著名。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-product-screenshot.png)

## 指南

支撑 WordPress 运行的环境组件包括：PHP, MySQL, Apache or Nginx等，请根据不同的部署包分别查看对应的手册，完成更多配置。

| 部署包名称 | 说明| 参考项 |
| --- | --- | --- |
| WordPress(LAMP) | Apache+MySQL+PHP on Linux | [《LAMP管理员手册》](https://support.websoft9.com/docs/lamp/zh) |
| WordPress(LNMP)| Nginx+MySQL+PHP on Linux |[《LNMP管理员手册》](https://support.websoft9.com/docs/lnmp/zh)|
| WordPress(IIS)| IIS+MySQL+PHP on Windows |[《IIS 管理员手册》](https://support.websoft9.com/docs/windows/zh)|
| WordPress(WAMP)| Apache+MySQL+PHP on Windows |[《WAMPServer 管理员手册》](https://support.websoft9.com/docs/wampserver/zh/)|

## 环境是什么？

除了使用 WordPress 部署包的默认设置之外，你可能需要在服务器上完成更多任务：

- 修改PHP配置文件
- 增加更多网站
- 配置HTTPS证书等
- 修改网站路径
- 绑定域名
- ...

完成这些任务，你都需要参考[环境指南](/zh/admin-runtime.md#指南)  

另外，你可能会思考，WordPress 是如何在这些环境下运行的呢？ 请参考下图的层次结构图

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/php-infra-websoft9.png)


## 演示

WordPress 官方提供了大量免费的主题和插件，你可以在线查看演示或安装

- [官方插件演示](https://wordpress.org/plugins/)
- [官方主题演示](https://wordpress.org/themes/)

