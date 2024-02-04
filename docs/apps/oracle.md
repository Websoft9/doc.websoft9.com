---
title: Oracle Database
slug: /oracle
tags:
  - Oracle
  - 关系型数据库
  - 云原生数据库
---

import Meta from './_include/oracle.md';

<Meta name="meta" />

## 入门指南{#guide}

### 申明

Oracle Database XE 对安装主机的规模和 CPU 数量不作限制（每台计算机一个数据库），但 XE 将最多存储 11GB 的用户数据，最多使用 1GB 内存，使用主机上的一个 CPU。  

在使用软件之前，建议阅读[ Oracle Database 快捷版 11*g* 第 2 版的 OTN 许可协议](http://www.oracle.com/technetwork/licenses/database-11g-express-license-459621.html)

### 初始化{#wizard}

Websoft9 控制台安装 Oracle Database 后，通过【我的应用】进入它的编辑窗口，在**访问**标签页中获取登录地址和账号。  

#### 在线获取镜像（可选）

针对于 **Oracle Database 企业版或标准版**，用户需自行操作获取镜像的步骤：

   - 到 Oracle 官方网站[注册](https://profile.oracle.com/myprofile/account/create-account.jspx)一个免费用户账号

   - 登录 [Oracle Database Repositories](https://container-registry.oracle.com/) 网站，阅读并同意 **Oracle Standard Terms and Restrictions**

      ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-registryagree-websoft9.png)
      ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-registryagreess-websoft9.png)

   - 连接到云服务器，运行下面的命令，拉取并启动 Oracle 数据库镜像
     ```
     cd /data/apps/oracle
     docker login container-registry.oracle.com/database/enterprise
     docker compose up -d
     ```
   > 因为企业版镜像超过10G，云服务器需要较高的带宽，建议使用 100M 的带宽；拉取镜像需要较长的时间，请耐心等待镜像下载完成

#### 连接数据库

1. 本地浏览器访问 EM 登录界面 

   > 必须使用 https 访问

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-emlogin-websoft9.png)

2. 输入默认用户密码和密码后，进入 Oracle EM 控制台

   ![Oracle EM 登录](http://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-emgui-websoft9.png)

3. 完成以上步骤，即表明 Oracle 服务运行正常。 

4. 进入 Oracle 数据库容器中，运行下面的命令测试可用性
   ```
   sqlplus SYS  AS SYSDBA
   ```

### Web 可视化管理

我们推荐使用 [CloudBeaver](./cloudbeaver) 作为 Oracle 数据库的可视化管理平台：

1. 新建一个 Oracle 数据库连接
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-cloudbeaver001-websoft9.png)

2. 连接成功的界面
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-cloudbeaver002-websoft9.png)


### 获取 SID 或 Servce Name{#getsid}

1. 在 Oracle 容器中运行 sqlplus 命令
    ```
    sqlplus / as sysdba 
    ```

2. 运行查询实例信息的 SQL 命令，instance_name 即所需的信息
    ```
    SQL> show parameter instance

    NAME                                 TYPE        VALUE
    ------------------------------------ ----------- ------------------------------
    active_instance_count                integer
    instance_abort_delay_time            integer     0
    instance_groups                      string
    instance_mode                        string      READ-WRITE
    instance_name                        string      XE
    instance_number                      integer     0
    instance_type                        string      RDBMS
    open_links_per_instance              integer     4
    parallel_instance_group              string
    ```

## 配置选项{#configs}

- 容器端口

  | 端口号 | 用途                                          | 必要性 |
  | ------ | --------------------------------------------- | ------ |
  | 1521   | 远程连接 Oracle Database | 可选   |
  | 5500   | HTTPS 访问 Oracle EM  | 可选   |

- Oracle Database 配置文件路径：*/path/dbconfig*  

- 重置密码命令：`./setPassword.sh <your_password>`

- 客户端命令：

  - `sqlplus / as sysdba`
  - expdp 导出
  - impdp 导出
  - rman 备份与恢复

- Oracle 连接信息

  * 用户名: sys
  * Role：SYSDBA
  * Port: 1521 或 其他自定义的端口
  * [服务名称或 SID](#getsid)

- SQL Developer：SQL Developer是 SQL*Plus 的图形版

- [APEX](./apex) 是用于 Oracle 数据库的 Web 应用程序开发工具。

- [Oracle REST Data Services](https://www.oracle.com/database/technologies/appdev/rest.html)

- Oracle GoldenGate 是一种异步、基于日志的实时数据复制产品。

- Oracle Clusterware 是实现 Oracle Real Application Clusters (Oracle RAC) 的工具。  

## 管理维护{#administrator}

### 备份与恢复

Oracle 备份与恢复主要通过 Recovery Manager (RMAN) 实现。  

  ```
  $ docker exec -it oracle rman

  Recovery Manager: Release 21.0.0.0.0 - Production on Fri Jul 8 03:52:17 2022
  Version 21.3.0.0.0

  Copyright (c) 1982, 2021, Oracle and/or its affiliates.  All rights reserved.

  RMAN>
  ```


## 故障

#### Error "ORA-28040: No matching authentication protocol"？

问题原因： 客户端与服务端的协议版本不一致   
解决方案： 升级客户端

####  ORA-28009: connection as SYS should be as SYSDBA or SYSOPER？

问题原因： 连接数据库时用户与默认的 role 不匹配    
解决方案： 连接信息中的 role  选择为 SYSDBA or SYSOPER

####  创建用户时，ORA-00440: Message 440 not found;product=RDBMS;facility=ORA？

问题原因： 登陆的sysdba权限的sys用户在root库上，需要连接到数据PDB库    
解决方案： 连接到 ORCLPDB1 库即可，下图通过 Oracle SQL Developer 客户端演示

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-connectpdb-websoft9.png)

 > 如果在连接ORCLCDB时需要创建用户，Oracle用户名必须带前缀"C##"


## 问答{#faq}

#### Oracle 企业版或标准版免费吗？

不免费，需获得 Oracle 官方授权方可使用

#### Oracle 多数据库架构？

从 12c 之后，Oracle 开始支持多个数据库实例，并逐渐演化成现在的多租户架构。  

![](https://docs.oracle.com/en/database/oracle/oracle-database/21/cncpt/img/cncpt389.png)

* 从 Oracle Database 21c 开始，“数据库”特指多租户容器数据库 (CDB)、可插拔数据库 (PDB)或应用程序容器的数据文件。
* CDB 是 Oracle 对数据库（PDB）的逻辑分组，多个数据库在逻辑上可以组合成一个 CDB。

#### SID 和 Service Name 区别？

SID 是数据库实例唯一的名称。 Service Name 是向监听（TNS）注册后的别名。可以给同一个数据库实例配置多个 Service Name。  

所以，大多数情况下， SID 和 Service Name 名称是相同的。  

#### 如何导入dump文件？

```
sudo docker cp dumpfile oracle:/tmp/dumpfile
sudo docker exec -it oracle bash
imp user/password@ORCLPDB1 file="dump文件路径" full=y ignore=y;
```

#### 表空间和模式对象（ Segment）？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-concepttablespaces-websoft9.jpg)

* 表空间：对数据库的逻辑划分，每个表空间包含一个或多个物理的数据库文件。表空间是 Oracle 数据库恢复的最小单位，容纳着许多数据库实体，如表、视图、索引、聚簇、回退段和临时段等。
* 模式对象：数据库用户拥有一个与用户名同名的数据库模式。

#### Oracle 数据库有哪些可视化管理工具？

* EM：企业管理器，主要是监控作用
* Oracle SQL Developer：可以导入导出、编写 SQL 脚本等
* ORDS：是 Oracle Web 化的中间件，提供 API，PL/SQL 等能力，集成了 Oracle SQL Developer
* APEX：是基于 ORDS 的一个无代码开发平台

#### PL/SQL 是什么？

PL/SQL 是 Oracle 服务端的存储过程编程语言

#### Oracle 网络服务必须配置吗？

Oracle 网络服务在分布式异构计算环境中提供企业范围的连接解决方​​案。Oracle Net 是 Oracle Net Services 的一个组件，它支持从客户端应用程序到数据库的网络会话。  

所以，在单机环境下，它不是必须的配置。  

#### Oracle 用户信息保存在哪里？

保存在 sys 下的 user$ 表里面：

```
select * from sys.user$;
```
