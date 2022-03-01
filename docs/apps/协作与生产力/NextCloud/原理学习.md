---
sidebar_position: 3
slug: /nextcloud/study
tags:
  - Nextcloud
  - 网盘
  - 知识管理
  - 团队协作
---

# 原理学习

[Nextcloud](https://nextcloud.com) 是 ownCloud 创始人发起的分支项目，是一款用于自建私有网盘的云存储开源软件，采用PHP+MySQL开发，提供了PC、IOS和Android三个同步客户端支持多种设备访问，用户可以很方便地与服务器上存储的文件、日程安排、通讯录、书签等重要数据保持同步，还支持其他同步来源：Amazon S3、Dropbox、FTP、Google Drive、OpenStack Object Storage、SMB、WebDAV、SFTP。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-gui-websoft9.png)

## 指南

支撑 Nextcloud 运行的环境组件包括：PHP, MySQL, Apache or Nginx等，请根据不同的部署包分别查看对应的手册，完成更多配置。

| 部署包名称 | 说明| 参考项 |
| --- | --- | --- |
| Nextcloud(LAMP) | Apache+MySQL+PHP on Linux | [《LAMP管理员手册》](https://support.websoft9.com/docs/lamp/zh) |
| Nextcloud(LNMP)| Nginx+MySQL+PHP on Linux |[《LNMP管理员手册》](https://support.websoft9.com/docs/lnmp/zh)|

## 环境是什么？

除了使用 Nextcloud 部署包的默认设置之外，你可能需要在服务器上完成更多任务：

- 修改PHP配置文件
- 增加更多网站
- 配置HTTPS证书等
- 修改网站路径
- 绑定域名
- ...

完成这些任务，你都需要参考[环境指南](/zh/admin-runtime.md#指南)  

另外，你可能会思考，Nextcloud 是如何在这些环境下运行的呢？ 请参考下图的层次结构图

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/php-infra-websoft9.png)

## 演示

Nextcloud 官网提供了演示环境，您可以直接[访问演示地址](https://try.nextcloud.com/)

> 免责说明：此处仅提供 Nextcloud 官方的演示地址，不保证与 Websoft9 镜像功能完全一致，若演示过程中若需要填写个人资料、获取Cookie、显示广告等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此产生的可能存在的商业纠纷与我们司无关。