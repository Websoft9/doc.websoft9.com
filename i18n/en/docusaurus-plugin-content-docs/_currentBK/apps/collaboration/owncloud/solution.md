---
sidebar_position: 2
slug: /owncloud/solution
tags:
  - OwnCloud
  - 网盘
  - 知识管理
  - 团队协作
---

# OwnCloud Solution

OwnCloud  can be used with other software platforms **integrated** to solve various [scenario problems] in the process of building an enterprise network disk system(https://owncloud.com/owncloud-and-microsoft/)。

## Integrate ONLYOFFICE Doc for Document Editing{#onlyoffice}

Nextcloud can't preview and edit Office document itself, you need to integrate Document Server service for OwnCloud to implement this function:

1. Enable the **TCP:9002** port on ,and check that [OnlyOffice Docs](../onlyofficedocs) is available
2. Log in to OwnCloud console, go to 【Market】page
	![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-preview-1-websoft9.png)
3. Find the application【ONLYOFFICE】 and install it
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-preview-2-websoft9.png)
   > The smear in the figure should be modified to **Internet IP**
4. Set the 【ONLYOFFICE】
5. Refresh the OwnCloud, test the preview and edit function of documentation.

## Integrate LDAP

Refer to *[User Authentication with LDAP](https://doc.owncloud.org/server/admin_manual/configuration/user/user_auth_ldap.html)*