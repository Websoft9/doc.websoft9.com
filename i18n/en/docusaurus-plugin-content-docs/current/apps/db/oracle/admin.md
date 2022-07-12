---
sidebar_position: 3
slug: /oracle/admin
tags:
  - Oracle
---


# Oracle Maintenance

This chapter is special guide for Oracle maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Oracle export and import

Oracle Data Pump 支持将数据和元数据从一个数据库高速移动到另一个数据库。 

导出和导入命令如下：  

* expdp
* impdp

### Oracle Backup and Restore

Oracle 备份与恢复主要通过 Recovery Manager (RMAN) 实现。  

```
$ docker exec -it oracle rman

Recovery Manager: Release 21.0.0.0.0 - Production on Fri Jul 8 03:52:17 2022
Version 21.3.0.0.0

Copyright (c) 1982, 2021, Oracle and/or its affiliates.  All rights reserved.

RMAN>
```

### Oracle Upgrade

本应用基于 Docker 安装，其升级采用通用的 Docker 应用升级方案即可。

### Oracle 数据库复制

Oracle GoldenGate 是一种异步、基于日志的实时数据复制产品。

### Oracle 集群

Oracle 集群又称之为 Oracle Real Application Clusters (Oracle RAC)，它支持多个实例共享对 Oracle 数据库的访问。  

Oracle Clusterware 是实现 Oracle RAC 的工具。

## Troubleshoot{#troubleshoot}

In addition to the Oracle issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  


#### Error "ORA-28040: No matching authentication protocol"?

问题原因： 客户端与服务端的协议版本不一致   
解决方案： 升级客户端

####  ORA-28009: connection as SYS should be as SYSDBA or SYSOPER?

问题原因： 连接数据库时用户与默认的 role 不匹配    
解决方案： 连接信息中的 role  选择为 SYSDBA or SYSOPER

## FAQ{#faq}

#### Is Oracle Enterprise or Standard free?

No, you should buy it

