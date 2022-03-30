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


Nextcloud 自身是不能对 Office 文件进行预览或编辑的，需要集成外部的 Office 文档编辑和预览服务才可以具备这样的功能。  

Websoft9 提供的 Nextcloud 部署包内置了 OnlyOffice Document Server(Docker版) ，此软件为 Nextcloud 提供文档预览与编辑服务，具体设置步骤如下：

1. 在云控制台安全组中，检查 **TCP:9002** 端口是否开启

2. 使用本地电脑浏览器测试文档服务是否可用：打开网址：*http://服务器公网IP:9002*，会看到 OnlyOffice Document Server 正在运行的提示 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-dkisrunning-websoft9.png)
   
   > 如果计划使用 HTTPS 访问 OnlyOffice Document Server，需给它绑定域名并设置 HTTPS

3. 登录到 Nextcloud ，单击右上角上角齿轮图标，点击【应用】
	![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-olpreview-1-websoft9.png)

4. 找到【ONLYOFFICE】插件，安装它

  > 可能因为服务器位于中国大陆地区，网络原因在上述第 3 步不能显示应用列表，需手动安装 ONLYOffice 插件：
  > - 可以到 Nextcloud [官方应用商店](https://apps.nextcloud.com/apps/onlyoffice/releases?platform=22#22)下载
  > - 下载到本地后，解压，通过FTP上传到服务器 Nextcloud 应用目录：/data/wwwroot/nextcloud/apps
  > - 登录Nextcloud后台，进入应用中心，启用 ONLYOffice 即可进入下一步操作，开启文档在线预览和编辑
  > ![onlyoffice](https://libs.websoft9.com/Websoft9/blog/tmp/nextcloud/zh/nextcloud-onlyoffice-enable-websoft9.png)

5. 安装完成后，找到**设置**页面，对 ONLYOFFICE 进行如图所示的设置（[参考官方文档](https://api.onlyoffice.com/editors/nextcloud)）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-setonlyoffice-websoft9.png)

   > 图中涂抹处应修改为**服务器公网IP**

6. 返回到首页，刷新或重新登录，然后单击 Office 文件即可在线预览和编辑。

如果连接 ONLYOFFICE 时，Nextcloud 强制要求 ONLYOFFICE 需配置 HTTPS，请参考：[OnlyOffice Document Server 域名绑定和 HTTPS](../onlyoffice#dns) 相关章节。

## 集成 LDAP

当企业网盘与多个人使用的时候，用户需要与内部域控集成，以保证用户可以通过Windows账号集成。

Nextcloud提供了 LDAP 集成工具，具体参考官方方案：*[User Authentication with LDAP](https://docs.nextcloud.com/server/latest/admin_manual/configuration_user/user_auth_ldap.html)*