---
sidebar_position: 3
slug: /memcached/admin
tags:
  - Memcached 
  - Cloud Native Database
---

# Memcached Maintenance

This chapter is special guide for Memcached maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

## Troubleshoot{#troubleshoot}

In addition to the Memcached issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  


## FAQ{#faq}

#### What is the Memcached client?

Memcached does not provide specific client. However, standard tools like telnet are enough to test container. Under Linux it is possible to connect by CLI command. We can invoke telnet from host machine, to connect to running Memcached server


#### Does Memcached need a password to log in?

No password authentication required

#### Is there a web-GUI tool for Memcached?

Yes

#### 如何修改 Memcached-admin 控制台密码？

参考： [Nginx auth_basic](../nginx#authbasic)


#### Memcached 是否开启密码验证？

没有开启

