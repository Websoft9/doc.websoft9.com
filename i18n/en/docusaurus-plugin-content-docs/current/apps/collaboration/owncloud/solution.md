---
sidebar_position: 2
slug: /owncloud/solution
tags:
  - ownCloud
  - 网盘
  - 知识管理
  - 团队协作
---

# ownCloud Solution

ownCloud 可以与其他的软件平台**集成**一起使用，解决 构建企业网盘系统 过程中的各种[场景问题](https://owncloud.com/owncloud-and-microsoft/)。

## Integrate ONLYOFFICE Doc for Document Editing{#onlyoffice}

Nextcloud can't preview and edit Office document itself, you need to integrate Document Server service for ownCloud to implement this function:

1. Enable the **TCP:9002** port on ,and check that [OnlyOffice Docs](../onlyofficedocs) is available
2. Log in to OwnCloud console, go to 【Market】page
	![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-preview-1-websoft9.png)
3. Find the application【ONLYOFFICE】 and install it
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-preview-2-websoft9.png)
   > The smear in the figure should be modified to **Internet IP**
4. Set the 【ONLYOFFICE】
5. Refresh the ownCloud, test the preview and edit function of documentation.

## Integrate LDAP

Refer to *[User Authentication with LDAP](https://doc.owncloud.org/server/admin_manual/configuration/user/user_auth_ldap.html)*