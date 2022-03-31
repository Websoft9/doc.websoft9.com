---
sidebar_position: 4
slug: /neo4j/study
tags:
  - Neo4j 
  - Cloud Native Database
---

# 原理学习

Neo4j 是目前主流的图数据库（graph database）产品，图数据库用于存在数据关系，更有利于关系的优化管理，存储和遍历节点和关系。  

对于 Neo4j 管理员来说，需要掌握的知识点包括：

* 图数据库核心思想
* Neo4j 架构
* 可视化管理：Neo4j Browser, Neo4j Desktop等
* 高级管理技术：升级、客户端工具使用、日志管理、备份恢复、监控
* 优化技术：负载均衡、集群
* 安全技术：授权与认证，用户管理

## 概念

### 什么是图数据库？

使用过传统关系型数据库（例如：MySQL）的同学非常明确，一个数据库 **大约等于** 多个数据表+表之间的关系。而图数据库（Graph database）理解起来却没那么直观，首先要明确的是图数据库与图片没有关系，即它不是用来存储图片的，也不是以图片的形式存储数据的。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/graphdatabasearchitecture-vs-sql-websoft9.png)
图. 关系型数据库 vs  图数据库

关系型数据库重点在于管理多个表，以及表中海量的数据，虽然名称为**关系型**，但实际上关系不是重点，重点是一行一行的数据。  

图数据库恰恰相反，图数据库的重点是**管理一对一对的关系**。  

可能有些同学有疑问，难道关系也需要用到数据库来管理？当然，看看下面的场景：

### 应用场景

* **社交领域**：Facebook, Linkedin 分析每个用户的好友信息，进一步管理社交关系，实现好友推荐
* **零售领域**：零售商和电商平台构建商品之间的关系模型链（读读[《啤酒与尿布》](https://book.douban.com/subject/3283973/)），便于做商品推荐
* **金融领域**：从用户手机通讯录或爬取社交关系，为用户构建一个关系网画像，便于风控和催收
* **汽车制造领域**：汽车制造商零部件供应商的关系图谱，有效降低单台汽车2万个零部件的供应链风险
* **电信领域**：电信运营商公司管理分布全球的复杂网络设施拓扑图，便于更有效的运维。  
* **知识图谱领域**：企查查、天眼查等对于公司和人的关系的知识图谱，可以理解为关系搜索引擎。
* **公共领域**：类似新冠疫情患者出行轨迹的关系图谱，可以更好做出精准排查。

可见，图数据库就用来存储：**人-人， 物-物， 人-物** 之间的关系，用于推荐、知识图谱、效率等目的。  

在内卷化及其严重的今天，通过对各行各业关系的研究和分析，获取知识，从其中挖潜“数据金矿”，不失为一种差异化竞争的途径。

### 如何存储数据？

图数据库的数据存储相关概念有：节点（标签，属性），关系（关系，关系类型）。  

以下图为例：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-graphdata-websoft9.png)  

* 一共有三个节点（两个 Person 节点，一个 Movie 节点），两个关系（两条边）
* 一共两个关系类型：ACTED_IN 和 DIRECTED
* 一共两个标签（节点类型或节点分组）：Person 和 Movie
* Person 类型节点有两个属性：name 和 born
* Movie 类型节点有两个属性：title 和 released
* 关系类型 ACTED_IN 有一个属性 roles
* 两个关系中有方向，也称之路径（Path）

学术上属性图的基本概念：一个属性图是由顶点（Vertex），边（Edge），标签（Lable），关系类型和属性（Property）组成的**有向图**。

### 数据库特征

Neo4j 作为一个数据库管理系统，与其他数据库管理系统有非常类似的基本[数据库定义](https://neo4j.com/docs/operations-manual/current/manage-databases/introduction/)

* 数据库管理系统：Neo4j是一个数据库管理系统（DBMS），能够管理多个数据库。DBMS可以管理因果群集中的独立服务器或一组服务器。

* 数据库：目录或文件夹内组织的文件的物理结构，具有与数据库相同的名称。从逻辑上讲，数据库是一个或多个图形的容器。  
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/manage-dbs-community.png)  

  Neo4j 4.2的默认安装包含两个数据库：

  * system-系统数据库，包含DBMS上的元数据和安全性配置。
  * neo4j-默认数据库，用于存储用户数据的数据库。

* Graph：数据库中的数据模型，每个数据中只有一个Graph（图）

下面是数据库管理的命令：

| 命令                       | 描述                         |
| :------------------------- | :--------------------------- |
| `CREATE DATABASE name [企业版]` | 创建并启动一个新的数据库。   |
| `DROP DATABASE name [企业版]`   | 删除（删除）现有数据库。     |
| `START DATABASE name`      | 启动已停止的数据库。         |
| `STOP DATABASE name`       | 关闭数据库。                 |
| `SHOW DATABASE name`       | 显示特定数据库的状态。       |
| `SHOW DATABASES`           | 显示所有数据库的名称和状态。 |
| `SHOW DEFAULT DATABASE`    | 显示默认数据库的名称和状态。 |
| `:use neo4j;`    | 切换到 neo4j 库 |

## 安装

Neo4j 是基于 Java 开发，因此运行它需要预先安装 JDK。  

* Linux：官方提供 rpm/deb 包的安装方式
* Windows/macOS：官方提供了一键安装包
* Docker：DockerHub上有一个官方的 [Neo4j 映像](https://hub.docker.com/_/neo4j/)

另外，官方提供无需安装的 [Neo4j Aura](https://neo4j.com/cloud/aura/?ref=menu) 托管平台，让用户专注于在线使用。  

## 集群

参考官方文档：[Clustering](https://neo4j.com/docs/operations-manual/current/clustering/)  

> 仅企业版支持集群

## Fabric

Neo4j Fabric 类型视图的概念，使用单个Cypher查询在多个数据库中存储和检索数据的方法。  

参考官方文档：[Neo4j Fabric](https://neo4j.com/docs/operations-manual/current/fabric/introduction/#fabric-introduction)

## 认证与授权

参考官方文档：[Authentication and authorization](https://neo4j.com/docs/operations-manual/current/authentication-authorization/)

## 安全

参考官方文档：[Neo4j Security](https://neo4j.com/docs/operations-manual/current/security/)

## 监控与维护

参考官方文档：[Monitoring](https://neo4j.com/docs/operations-manual/current/monitoring/)

## 性能

参考官方文档：[Performance](https://neo4j.com/docs/operations-manual/current/performance/)