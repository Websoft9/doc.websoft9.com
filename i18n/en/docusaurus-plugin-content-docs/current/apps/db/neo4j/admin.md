---
sidebar_position: 3
slug: /neo4j/admin
tags:
  - Neo4j 
  - Cloud Native Database
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

## 备份

### Neo4j 备份

请参考 [Neo4j's Backup Docs](https://neo4j.com/docs/operations-manual/current/backup/)

### Neo4j 升级

Neo4j 升级有一定的复杂性，请参考[官方升级文档](https://neo4j.com/docs/operations-manual/current/upgrade/)

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


## 故障排除{#troubleshooting}

除以下列出的 Neo4j 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

## 问题解答

#### Neo4j 支持多语言吗？

支持多语言（包含中文），系统默认根据浏览器自动选择语言 

#### 社区版 vs 企业版？

参考：[Neo4j 功能细节对比](https://neo4j.com/docs/operations-manual/current/introduction/#edition-details)

#### Neo4j 支持哪些连接协议？

Neo4j 支持三种不同的连接方式：Bolt、HTTP、HTTPS。

#### Neo4j browser 是什么？

Neo4j浏览器是一个可以通过Web浏览器运行的图形用户界面（GUI）。 Neo4j浏览器可用于添加数据，运行查询，创建关系等。 它还提供了一种可视化数据库中数据的简便方法。

#### Neo4j 一个实例支持多个数据库吗？

支持，但社区版仅支持一个默认的系统库和用户库

#### Neo4j 有行和列的概念吗？

有，但存储的是数据节点以及节点之间的关系

#### Cypher 是什么？

Cypher是操作Neo4j的语句，等同于SQL

#### 如何禁止 Neo4j Browser 访问？

关闭服务器安全组的 80 端口即可禁止