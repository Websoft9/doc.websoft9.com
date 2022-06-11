---
sidebar_position: 1
slug: /couchdb
tags:
  - CouchDB
  - Cloud Native Database
---

# CouchDB Getting Started

[CouchDB](https://couchdb.apache.org/) is a terrific single-node database that works just like any other database behind an application server of your choice.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/couchdb/couchdb-gui-websoft9.png)

If you have installed Websoft9 CouchDB, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for CouchDB
4. [Get](./user/credentials) default username and password of CouchDB

## CouchDB Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://DNS/_utils* or *http://Internet IP/_utils*, you will enter installation wizard of CouchDB
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/couchdb/couchdb-init-websoft9.png)

2. Log in to CouchDB web console([Don't have password?](./user/credentials))  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/couchdb/couchdb-bk-websoft9.png)

3. Set you new password from: 【Users】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/couchdb/couchdb-pw-websoft9.png)

> More useful CouchDB guide, please refer to [CouchDB Documentation](https://docs.couchdb.org)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## CouchDB QuickStart

> 需要了解更多 CouchDB 的使用，请参考官方文档：[CouchDB Documentation](https://docs.couchdb.org)

## CouchDB Setup

### Enable Remote Connection{#remote}

1. Use **SSH** to connect CouchDB server and modify the CouchDB [configuration file](#path): */opt/couchdb/etc/default.ini*
   ```
   #1 set bindIP to 0.0.0.0
      #bind_address = 127.0.0.1
      bind_address = 0.0.0.0
   ```
   > 0.0.0.0 means any Internet IP can connect your CouchDB

2. [Restart CouchDB service](#service)
   ```
   systemctl restart couchdb
   ```

### Authentication Configuration

1. Modify the CouchDB configuration file */opt/couchdb/etc/default.ini*
   ```
  When this option is set to true, no requests are allowed from anonymous users. Everyone must be authenticated.
   [chttpd]
   require_valid_user = false
   ```

2. [Restart CouchDB service](#service)
   ```
   systemctl restart couchdb
   ```

### Reset Password

Reset password is the process of resetting a new password through special solutions in case the password has been forgotten.

1. Use **SSH** to connect CouchDB server and modify the CouchDB configuration file: */opt/couchdb/etc/local.ini*
   ```
   admin = $new_password
   ```
2. Restart the CouchDB service
   ```
   systemctl restart couchdb
   ```


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage CouchDB 


通过运行`docker ps`，可以查看到 CouchDB 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 CouchDB 本身的参数：

### Path{#path}

CouchDB 配置文件： */opt/couchdb/etc/default.ini* 和 */opt/couchdb/etc/local.ini*  
CouchDB installation directory： */data/couchdb*  
CouchDB 日志目录： */data/logs/couchdb*  

### URL

CouchDB 控制台： *http://域名/_utils*  

### Port

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 5984   | CouchDB 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


### Version

```shell
cat path/couchdb/releases/*/couchdb.rel  |sed -n 3p | awk -F '"' '{print $4}'
```

### Service

```shell
sudo systemctl start | stop | restart | status couchdb
```

### CLI

CouchDB 是 API 驱动的数据库，官方没有提供额外的 CLI，而是建议用户通过 `curl` 的方式操作数据。  

### API

The CouchDB [API](https://docs.couchdb.org/en/stable/api/index.html) is the primary method of interfacing to a CouchDB instance. Requests are made using HTTP and requests are used to request information from the database, store new data, and perform views and formatting of the information stored within the documents.Requests to the API can be categorised by the different areas of the CouchDB system that you are accessing, and the HTTP method used to send the request. Different methods imply different operations, for example retrieval of information from the database is typically handled by the GET operation, while updates are handled by either a POST or PUT request.

**Request Format and Responses**

- GET
Request the specified item. As with normal HTTP requests, the format of the URL defines what is returned. With CouchDB this can include static items, database documents, and configuration and statistical information. In most cases the information is returned in the form of a JSON document.

- HEAD
The HEAD method is used to get the HTTP header of a GET request without the body of the response.

- POST
Upload data. Within CouchDB POST is used to set values, including uploading documents, setting document values, and starting certain administration commands.

- PUT
Used to put a specified resource. In CouchDB PUT is used to create new objects, including databases, documents, views and design documents.

- DELETE
Deletes the specified resource, including documents, views, and design documents.

**Request Example**

Visit http://ip:5984/_active_tasks, return response like this:

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
