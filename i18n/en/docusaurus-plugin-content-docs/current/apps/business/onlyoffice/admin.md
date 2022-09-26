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

#### Is there a limit to the number of concurrent connections in ONLYOFFICE open source version?

Up to 20 Simultaneous connections

#### ONLYOFFICE Docs What is the number of concurrent connections?

See: [ONLYOFFCE Docs](../onlyofficedocs/admin#onlyofficedocsmaxconn) related documentation

#### Does ONLYOFFICE support document editing and previewing by default?

It is already configured by default and can be used without any settings

#### Can this application provide external document services?

Yes, *http://server public IP:9002* is the document preview and editing service address

