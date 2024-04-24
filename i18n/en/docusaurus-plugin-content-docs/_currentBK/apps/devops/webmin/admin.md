---
sidebar_position: 3
slug: /webmin/admin
tags:
  - Webmin
  - Virtual Desktop
  - Web visualization Linux Administrator Tool
---

# Webmin Maintenance

This chapter is special guide for Webmin maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Webmin Upgrade

Webmin have the interface for upgrade, it very easy for you

![Webmin upgrade](https://libs.websoft9.com/Websoft9/DocsPicture/en/webmin/webmin-upgrade-websoft9.png)

### 卸载

暂无方案

## Troubleshoot{#troubleshoot}

In addition to the Webmin issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  


## FAQ{#faq}

#### Does Webmin support multiple languages?

Yes, you can change language from Webmin console

#### What kind of installation method does Webmin use in this project?

Use rpm/deb

#### Is Apache included in Webmin?

Does not contain. But in this deployment plan, we have additionally installed Apache

#### Why is the newly installed Webmin module still displayed under the Un-used Modules menu?

You should click【Refresh module】after the installation of new module

#### What is the function of HTTP Tunnel?

To be studied

#### How to disable Webmin inherit the Linux system user?

You can 【Unix验证】 更改为 【设置为】，同时设置新密码和用户

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/webmin/webmin-usermode-websoft9.png)

#### Can I reset password of Webmin by command? 

Webmin uses the server root password, so use the `passwd` system command