---
sidebar_position: 1
slug: /couchdb
tags:
  - CouchDB
  - Cloud Native Database
---

# 快速入门

[Apache CouchDB™](https://couchdb.apache.org/) 是一个原生 HTTP/JSON API 驱动的文档数据库，可以作为**后端即服务**使用。CouchDB 的目标具有高度可伸缩性，提供了高可用性和高可靠性，即使运行在容易出现故障的硬件上也是如此。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/couchdb/couchdb-gui-websoft9.png)

## 准备

部署 Websoft9 提供的 CouchDB 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 CouchDB 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  CouchDB，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程


## CouchDB 初始化向导

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名/_utils* 或 *http://服务器公网 IP/_utils*, 进入初始化页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/couchdb/couchdb-init-websoft9.png)

2. 输入[账号密码](./user/credentials)，成功登录到 CouchDB 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/couchdb/couchdb-admin-websoft9.png)

3. 登录后通过：【Users】设置新密码  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/couchdb/couchdb-pw-websoft9.png)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## CouchDB 使用入门

> 需要了解更多 CouchDB 的使用，请参考官方文档：[CouchDB Documentation](https://docs.couchdb.org)

## CouchDB 常用操作

### 开启远程访问

1. 修改 CouchDB [配置文件](#path)
   ```
      将 bindIP 修改为 0.0.0.0 或 本地电脑公网IP
      #bind_address = 127.0.0.1
      bind_address = 0.0.0.0
   ```
   > 0.0.0.0 代表任意公网IP均可访问

2. [重启 CouchDB 服务](#service)后生效


### 开启用户认证

1. 修改 CouchDB 配置文件 */opt/couchdb/etc/default.ini*
   ```
  将 require_valid_user 的值设置为 false， 则每个人都必须经过身份验证。
   [chttpd]
   require_valid_user = false
   ```

2. CouchDB
   ```
   systemctl restart couchdb

### 重置密码

已经忘记密码的情况下，需通过特殊方法重新设置新密码：  

1. 修改 CouchDB [配置文件](#path)，将下面的$new_password替换成新密码
   ```
   admin = $new_password
   ```
2. [重启 CouchDB 服务](#service)后生效


## CouchDB 参数

CouchDB 应用中包含 Nginx, Docker 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 CouchDB 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 CouchDB 本身的参数：

### 路径{#path}

CouchDB 配置文件： */opt/couchdb/etc/default.ini* 和 */opt/couchdb/etc/local.ini*  
CouchDB 安装目录： */data/couchdb*  
CouchDB 日志目录： */data/logs/couchdb*  

### 网址

CouchDB 控制台： *http://域名/_utils*  

### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 5984   | CouchDB 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


### 版本

```shell
cat path/couchdb/releases/*/couchdb.rel  |sed -n 3p | awk -F '"' '{print $4}'
```

### 服务

```shell
sudo systemctl start | stop | restart | status couchdb
```

### 命令行

CouchDB 是 API 驱动的数据库，官方没有提供额外的 CLI，而是建议用户通过 `curl` 的方式操作数据。  

### API

CouchDB 是 [API](https://docs.couchdb.org/en/stable/api/index.html) 驱动的数据库，天生为 API 而生。它的请求格式包括：  

- GET：要求指定的物品。与普通的HTTP请求一样，URL的格式定义了返回的内容。使用CouchDB，它可以包括静态项目，数据库文档以及配置和统计信息。在大多数情况下，信息以JSON文档的形式返回。

- HEAD：该HEAD方法用于获取GET没有响应主体的请求的HTTP标头。

- POST：上传数据。在CouchDBPOST中，用于设置值，包括上载文档，设置文档值和启动某些管理命令。

- PUT：用于放置指定的资源。在CouchDBPUT中用于创建新对象，包括数据库，文档，视图和设计文档。

- DELETE：删除指定的资源，包括文档，视图和设计文档。


运行命令 `curl http://URL:5984/_active_tasks` 访问，将返回查询结果。

```Request
GET /_active_tasks HTTP/1.1
Accept: application/json
Host: localhost:5984
```

```Response
HTTP/1.1 200 OK
Cache-Control: must-revalidate
Content-Length: 1690
Content-Type: application/json
Date: Sat, 10 Aug 2013 06:37:31 GMT
Server: CouchDB (Erlang/OTP)

[
    {
        "changes_done": 64438,
        "database": "mailbox",
        "pid": "<0.12986.1>",
        "progress": 84,
        "started_on": 1376116576,
        "total_changes": 76215,
        "type": "database_compaction",
        "updated_on": 1376116619
    },
    {
        "changes_done": 14443,
        "database": "mailbox",
        "design_document": "c9753817b3ba7c674d92361f24f59b9f",
        "pid": "<0.10461.3>",
        "progress": 18,
        "started_on": 1376116621,
        "total_changes": 76215,
        "type": "indexer",
        "updated_on": 1376116650
    },
    {
        "changes_done": 5454,
        "database": "mailbox",
        "design_document": "_design/meta",
        "pid": "<0.6838.4>",
        "progress": 7,
        "started_on": 1376116632,
        "total_changes": 76215,
        "type": "indexer",
        "updated_on": 1376116651
    },
    {
        "checkpointed_source_seq": 68585,
        "continuous": false,
        "doc_id": null,
        "doc_write_failures": 0,
        "docs_read": 4524,
        "docs_written": 4524,
        "missing_revisions_found": 4524,
        "pid": "<0.1538.5>",
        "progress": 44,
        "replication_id": "9bc1727d74d49d9e157e260bb8bbd1d5",
        "revisions_checked": 4524,
        "source": "mailbox",
        "source_seq": 154419,
        "started_on": 1376116644,
        "target": "http://mailsrv:5984/mailbox",
        "type": "replication",
        "updated_on": 1376116651
    }
]
```

