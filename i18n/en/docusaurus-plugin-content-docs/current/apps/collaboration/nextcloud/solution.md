---
sidebar_position: 2
slug: /nextcloud/solution
tags:
  - Nextcloud
  - 网盘
  - 知识管理
  - 团队协作
---

# Nextcloud Solution

Nextcloud 可以与其他的软件平台**集成**一起使用，解决 构建企业网盘系统 过程中的各种[场景问题](https://nextcloud.com/industries/)。

## Integrate ONLYOFFICE Doc for Document Editing{#onlyoffice}

Nextcloud can't preview and edit Office document itself, you need to integrate Document Server service for Nextcloud to implement this function:

1. Enable the **TCP:9002** port on ,and check that [OnlyOffice Docs](../onlyofficedocs) is available
2. Log in to Nextcloud console, go to 【Apps】page
	 ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-olpreview-1-websoft9.png)
3. Find the app【ONLYOFFICE】 and install it
4. Set the 【ONLYOFFICE】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-setonlyoffice-websoft9.png)
   > The smear in the figure should be modified to **Internet IP**
5. Refresh the Nextcloud, test the preview and edit function of documentation.

## Integrate LDAP

Refer to *[User Authentication with LDAP](https://docs.nextcloud.com/server/latest/admin_manual/configuration_user/user_auth_ldap.html)*