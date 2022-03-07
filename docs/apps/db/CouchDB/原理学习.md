---
sidebar_position: 3
slug: /couchdb/study
tags:
  - CouchDB
  - Cloud Native Database
---

# 原理学习

## CouchDB API

CouchDB API是与CouchDB实例接口的主要方法。使用HTTP发出请求，请求用于从数据库请求信息，存储新数据以及对文档中存储的信息进行查看和格式化。
对API的请求可以按照您正在访问的CouchDB系统的不同区域以及用于发送请求的HTTP方法进行分类。不同的方法意味着不同的操作，例如，从数据库中检
索信息通常由该GET操作处理，而更新则由POST或PUT请求处理。不同方法必须提供的信息之间存在一些差异。

### 请求格式和响应

- GET
要求指定的物品。与普通的HTTP请求一样，URL的格式定义了返回的内容。使用CouchDB，它可以包括静态项目，数据库文档以及配置和统计信息。在大多数情况下，信息以JSON文档的形式返回。

- HEAD
该HEAD方法用于获取GET没有响应主体的请求的HTTP标头。

- POST
上传数据。在CouchDBPOST中，用于设置值，包括上载文档，设置文档值和启动某些管理命令。

- PUT
用于放置指定的资源。在CouchDBPUT中用于创建新对象，包括数据库，文档，视图和设计文档。

- DELETE
删除指定的资源，包括文档，视图和设计文档。

### 请求实例

通过url http://ip:5984/_active_tasks访问，将返回查询结果。

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
