---
sidebar_position: 3
slug: /onlyoffice/admin
tags:
  - ONLYOFFICE Workspace
  - 企业管理
  - CRM
---

# ONLYOFFICE Maintenance

This chapter is special guide for ONLYOFFICE maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

## Troubleshoot{#troubleshoot}

In addition to the ONLYOFFICE issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### ONLYOFFICE displays 502 Bad Gateway?

First run the command `sudo docker logs onlyofficecommunityserver` to check if there's error logs.  

Generally, it's caused by the lack of file permission or the failure of data connection.

#### Can't run ONLYOFFICE after re-installing database?

ONLYOFFICE has strict rules for database configuration, ensure you meet the following requirements:

```
echo "[mysqld]
sql_mode = 'NO_ENGINE_SUBSTITUTION'
max_connections = 1000
max_allowed_packet = 1048576000
group_concat_max_len = 2048
log-error = /var/log/mysql/error.log" > /app/onlyoffice/mysql/conf.d/onlyoffice.cnf
```

## FAQ{#faq}

#### Does ONLYOFFICE support multiple languages?

Yes, you can switch language online.

#### Community Edition vs Enterprise Edition？

Refer to [Compare Community Edition and Enterprise Edition](https://github.com/ONLYOFFICE/CommunityServer#compare-community-edition-and-enterprise-edition)

#### What's the relationship between various edition of ONLYOFFICE?

ONLYOFFICE offers different versions:

* ENTERPRISE EDITION
* COMMUNITY EDITION
* INTEGRATION EDITION
* DEVELOPER EDITION

Each edition consists of: Community Server, Document Server, Mail Server.  

COMMUNITY EDITION is free, while [DEVELOPER EDITION](https://www.onlyoffice.com/en/developer-edition-prices.aspx) is a paid version for developers.

#### ONLYOFFICE 开源版并发连接数有限制吗？

并发连接数不超过 20个（Up to 20 Simultaneous connections）

#### ONLYOFFICE Docs 并发连接数是什么？

参阅：[ONLYOFFCE Docs](../onlyofficedocs/admin#onlyofficedocsmaxconn) 相关文档

#### ONLYOFFICE 默认支持文档编辑与预览吗？

默认已经配置好，无需任何设置即可使用

#### 本应用是否可以对外提供文档服务？

可以，*http://服务器公网IP:9002* 即文档预览与编辑服务地址

