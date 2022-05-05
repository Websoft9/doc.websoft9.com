---
sidebar_position: 2
slug: /nextcloud/solution
tags:
  - Nextcloud
  - 网盘
  - 知识管理
  - 团队协作
---

# 场景方案

Nextcloud 可以与其他的软件平台**集成**一起使用，解决 构建企业网盘系统 过程中的各种[场景问题](https://nextcloud.com/industries/)。

## 集成 ONLYOFFICE Doc 实现文档编辑{#onlyoffice}

Nextcloud 自身是不能对 Office 文件进行预览或编辑的，需要集成 **第三方文档中间件** 才可以具备这样的功能。  

所幸，Websoft9 提供的 Nextcloud 部署包内置文档中间件 [OnlyOffice Docs](../onlyofficedocs)，下面介绍如何使用：

1. 在云控制台安全组中，确保 **TCP:9002** 端口开启，并检查 [OnlyOffice Docs](../onlyofficedocs) 可用

2. 登录到 Nextcloud ，单击右上角上角齿轮图标，点击【应用】
	 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-olpreview-1-websoft9.png)

4. 找到【ONLYOFFICE】插件，安装并启用它
   ![onlyoffice](https://libs.websoft9.com/Websoft9/blog/tmp/nextcloud/zh/nextcloud-onlyoffice-enable-websoft9.png)

5. 安装完成后，找到**设置**页面，对 ONLYOFFICE 进行如图所示的设置（[参考官方文档](https://api.onlyoffice.com/editors/nextcloud)）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-setonlyoffice-websoft9.png)

   > 图中涂抹处应修改为**服务器公网IP**

6. 返回到首页，刷新或重新登录，然后单击 Office 文件即可在线预览和编辑。

## 集成 LDAP

当企业网盘与多个人使用的时候，用户需要与内部域控集成，以保证用户可以通过Windows账号集成。

Nextcloud提供了 LDAP 集成工具，具体参考官方方案：*[User Authentication with LDAP](https://docs.nextcloud.com/server/latest/admin_manual/configuration_user/user_auth_ldap.html)*