---
title: CouchDB
slug: /couchdb
tags:
  - 数据库
  - JASON
  - 文档数据库
  - 云原生
---

import Meta from './_include/couchdb.md';

<Meta name="meta" />

## 入门指南{#guide}

Websoft9 控制台安装 CouchDB 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

### 功能一览{#wizard}

- 进入初始化页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/couchdb/couchdb-init-websoft9.png)

- CouchDB 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/couchdb/couchdb-admin-websoft9.png)

- 【Users】设置新密码  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/couchdb/couchdb-pw-websoft9.png)


## 配置选项{#configs}

- 容器配置文件：/opt/couchdb/etc/local.d  
  ```
  bind_address = 0.0.0.0 #任意公网 IP 均可访问
  require_valid_user = false #用户认证
  admin="passwo
  ...
  ```

- 命令行：CouchDB 是 API 驱动，通过 `curl` 的方式操作数据

- [API](https://docs.couchdb.org/en/stable/api/index.html) 

- [分区](https://docs.couchdb.org/en/stable/partitioned-dbs/index.html#partitioned-databases)

- 最大连接数：2048

## 管理维护{#administrator}

### 备份

CouchDB备份涉及到3种不同的文件：数据库文件，配置文件，日志文件。  

详情参考官方备份文档：[Backing up CouchDB](https://docs.couchdb.org/en/latest/maintenance/backups.html)

### 升级

详情参考官方升级文档：[Upgrading CouchDB](https://docs.couchdb.org/en/latest/install/upgrading.html)

## 故障