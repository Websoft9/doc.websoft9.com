---
sidebar_position: 3
slug: /neo4j/admin
tags:
  - Neo4j 
  - Cloud Native Database
---

# Neo4j Maintenance

This chapter is special guide for Neo4j maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide


### Neo4j Backup

Please refer to [Neo4j's Backup Docs](https://neo4j.com/docs/operations-manual/current/backup/)

### Neo4j Upgrade

Neo4j Upgrade is not easy, please refer to [Neo4j's Upgrade Docs](https://neo4j.com/docs/operations-manual/current/upgrade/)

升级对象一般指的是：Neo4j 4.1.2 to Neo4j 4.2.0，下面说明主要步骤：

1. 停止 Neo4j 服务之后，安装指定的版本
    ```
    sudo systemctl stop neo4j
    sudo apt-get update
    sudo sudo apt-get install neo4j=1:4.2.2
    ```
2. 修改 Neo4j 配置文件，取消 `dbms.allow_upgrade=true` 前面的 # 号

3. 运行 Neo4j 启动服务的命令
    ```
    sudo systemctl start neo4j
    ```
4. 系统升级开始

5. 升级完成之后，恢复 `dbms.allow_upgrade=true`之前的 # 号


## Troubleshoot{#troubleshoot}

In addition to the Neo4j issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

## FAQ{#faq}

#### Neo4j support multiply languages?

Yes

#### Neo4j Community Edition vs Neo4j Enterprise Edition?

Please refer to [Neo4j edition details](https://neo4j.com/docs/operations-manual/current/introduction/#edition-details)

#### How many connection protocol on Neo4j?

Bolt, HTTP, HTTPS

#### What's Neo4j Browser? 

The Neo4j browser is a graphical user interface (GUI) that can be run through a web browser. The Neo4j browser can be used for adding data, running queries, creating relationships, and more. It also provides an easy way to visualise the data in the database.

#### Is there a web-base GUI database management tools?

Yes, Neo4j Browser is on it, visit by *http://Internet IP*

#### How to disable Neo4j Browser access?

Disable port 80 of the server security group

#### Cypher？

Cypher is Neo4j’s graph query language that allows users to store and retrieve data from the graph database. Neo4j wanted to make querying graph data easy to learn, understand, and use for everyone, but also incorporate the power and functionality of other standard data access languages.

#### One Neo4j instance support multiply databases?

Yes, but only for Neo4j Enterprise Edition

#### Is there have line and column for Neo4j?

Yes, but it storage for relationship of Node