---
sidebar_position: 3
slug: /drupal/study
tags:
  - Drupal
  - CMS
  - 建站系统
---

# 原理学习

[Drupal](https://www.drupal.org) 是全球三大开源内容管理系统之一，约3%的网站使用。Drupal也是一个开发框架，逻辑性强、一块块积木，搭起来以后使页面层层分明，它的内核中的有功能强大的PHP类库、函数库和API，能够通过二次化开发来构建复杂多用的企业级应用。Drupal有良好的商业生态，众多高端优质客户使用进一步推动了开源社区的发展。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-gui-websoft9.png)

## 指南

支撑 Drupal 运行的环境组件包括：PHP, MySQL, Apache or Nginx等，请根据不同的部署包分别查看对应的手册，完成更多配置。

| 部署包名称 | 说明| 参考项 |
| --- | --- | --- |
| Drupal(LAMP) | Apache+MySQL+PHP on Linux | [《LAMP管理员手册》](https://support.websoft9.com/docs/lamp/zh) |
| Drupal(LNMP)| Nginx+MySQL+PHP on Linux |[《LNMP管理员手册》](https://support.websoft9.com/docs/lnmp/zh)|

## 环境是什么？

除了使用 Drupal 部署包的默认设置之外，你可能需要在服务器上完成更多任务：

- 修改PHP配置文件
- 增加更多网站
- 配置HTTPS证书等
- 修改网站路径
- 绑定域名
- ...

完成这些任务，你都需要参考[环境指南](/zh/admin-runtime.md#指南)  

另外，你可能会思考，Drupal 是如何在这些环境下运行的呢？ 请参考下图的层次结构图

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/php-infra-websoft9.png)


## 演示

Drupal 官网提供了试用环境，您可以直接试用

* 演示地址：https://www.drupal.org/try-drupal

> 免责说明：此处仅提供 Drupal 官方的演示，不保证与 Websoft9 部署包功能完全一致，若演示过程中若需要填写个人资料、获取Cookie等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此可能存在的商业纠纷与我司无关。

## CLI

本项目默认已经安装 Drupal 的命令行工具：[Drush,Drupal Console](https://www.drupal.org/docs/user_guide/en/install-tools.html#s-what-are-command-line-tools)

使用 SSH 连接服务器，便可以直接使用：

```
# Drush 所有命令行
dcg  
drush  
php-parse 
psysh  
release  
robo  
security-checker  
var-dump-server

# Drupal Console 所有命令行
drupal  
php-parse  
psysh  
var-dump-server
```