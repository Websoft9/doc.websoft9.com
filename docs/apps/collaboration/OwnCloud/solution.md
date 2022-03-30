---
sidebar_position: 2
slug: /owncloud/solution
tags:
  - ownCloud
  - 网盘
  - 知识管理
  - 团队协作
---

# 场景方案

ownCloud 可以与其他的软件平台**集成**一起使用，解决 构建企业网盘系统 过程中的各种[场景问题](https://owncloud.com/owncloud-and-microsoft/)。

## 集成 ONLYOFFICE Docs 实现文档编辑{#onlyoffice}

ownCloud 自身是不能对 Office 文件进行预览或编辑的，需要集成外部的 Office 文档编辑和预览服务才可以具备这样的功能。  

Websoft9 提供的 ownCloud 部署包内置了 OnlyOffice Document Server(Docker版) ，此软件为 OwnCloud 提供文档预览与编辑服务，具体设置步骤如下：

1. 在云控制台安全组中，检查 **TCP:9002** 端口是否开启

2. 使用本地电脑浏览器测试文档服务是否可用：打开网址：*http://服务器公网IP:9002*，会看到 OnlyOffice Document Server 正在运行的提示 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-dkisrunning-websoft9.png)
   
   > 如果计划使用 HTTPS 访问 OnlyOffice Document Server，需给它绑定域名并设置 HTTPS

3. 登录到 OwnCloud ，单击左上角进入【Market】页面
	![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-preview-1-websoft9.png)

4. 找到【ONLYOFFICE】插件，安装它

5. 打开：【admin】>【设置】>【...Additional】，对 ONLYOFFICE 插件进行如图所示的设置([更多说明](https://api.onlyoffice.com/editors/owncloud))
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-preview-2-websoft9.png)

   > 图中 Document Editing Service address 处应修改为**服务器公网IP:9002**

6. 返回到首页，刷新或重新登录，然后单击 Office 文件即可在线预览和编辑。

## ownCloud 集成 LDAP

当企业网盘与多个人使用的时候，用户需要与内部域控集成，以保证用户可以通过Windows账号集成。

OwnCloud提供了 LDAP 集成工具，具体参考官方方案：*[User Authentication with LDAP](https://doc.owncloud.org/server/admin_manual/configuration/user/user_auth_ldap.html)*