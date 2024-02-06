---
title: Neo4j
slug: /neo4j
tags:
  - 图数据库
  - 关系分析
---

import Meta from './_include/neo4j.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Neo4j 后，通过【我的应用】进入它的编辑窗口，在**访问**标签页中获取登录地址和账号。  

#### 图形化管理

Neo4j 提供了多种图形化工具，有基于 Web 的版本，也有支持 Windows, Linux, macOS 等 [Desktop](https://neo4j.com/download-center/) 版本。

Neo4j Browser 是开发人员与图形进行交互的工具。它是Neo4j数据库的企业版和社区版的默认界面。

1. 本地浏览器访问 Neo4j Browser
![Neo4j Browser](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-connectfirst-websoft9.png)

2. 选择【bolt://】的URL模式，输入用户名和密码
![修改Neo4j密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-snewpw-websoft9.png)

> Pick neo4j:// for a routed connection, bolt:// for a direct connection to a DBMS. 选择 bolt:// 速度更快

3. 系统登录到控制台，初始化安装完成
![Neo4j 控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-ssui-websoft9.png)

4. 通过:【Database Information】>【server user add】 增加新用户
![Neo4j 增加用户](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-adduser-websoft9.png)

5. 通过:【Cloud Services】>【Clear local data】 退出 Neo4j Browser 
![Neo4j 增加用户](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-loginout-websoft9.png)


#### 命令行连接

1. 进入 Neo4j 容器所在的服务器，输入 `cypher-shell` 命令，并登录

   ```
   $cypher-shell
   username: neo4j
   password: *****
   Connected to Neo4j 4.1.0 at neo4j://localhost:7687 as user neo4j.
   Type :help for a list of available commands or :exit to exit the shell.
   Note that Cypher queries must end with a semicolon.
   neo4j@neo4j>
   ```

2. 输入命令 `CALL dbms.showCurrentUser();` 查看当前用户

   ```
   neo4j@neo4j> CALL dbms.showCurrentUser();
   +--------------------------+
   | username | roles | flags |
   +--------------------------+
   | "neo4j"  | admin  | []    |
   +--------------------------+
   1 row available after 22 ms, consumed after another 1 ms
   ```

### 用户管理

Neo4j 提供了详细的 [User and role management](https://neo4j.com/docs/cypher-manual/current/administration/security/users-and-roles/#administration-security-users) 功能（仅企业版支持）

```
# 显示所有用户
SHOW USERS;
CALL dbms.security.listUsers();

# 创建新用户，第三个参数表示 requridchangepassword 
CALL dbms.security.createUser('username','password',false);

# 删除用户
CALL dbms.security.deleteUser('username');   
```

### Cypher Shell

Neo4j 提供了默认的命令行工具[Cypher Shell](https://neo4j.com/docs/operations-manual/current/tools/cypher-shell/)，Cypher Shell用于运行查询和执行管理任务。它通过加密的二进制协议Bolt进行通信。

```
root@neo4j-test:~# cypher-shell
username: neo4j
password: *****
Connected to Neo4j 3.5.14 at bolt://localhost:7687 as user neo4j.
Type :help for a list of available commands or :exit to exit the shell.
Note that Cypher queries must end with a semicolon.
neo4j>
```


### neo4j-admin

[Neo4j Admin](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/) is the primary tool for managing your Neo4j instance. It is a command-line tool that is installed as part of the product and can be executed with a number of commands. Some of the commands are described in more detail in separate sections.

## 配置选项{#configs}

- 开启远程访问：配置文件中增加配置段 `dbms.default_listen_address=0.0.0.0`
- [配置文件](https://neo4j.com/docs/operations-manual/current/configuration)：*/path/neo4j.conf*
- 端口说明：[Port on Configuration file](https://neo4j.com/docs/operations-manual/current/configuration/ports/)
- 命令行：[Neo4j Tools](https://neo4j.com/docs/operations-manual/current/tools/)
- [The Neo4j REST API Documentation](https://neo4j.com/docs/rest-docs/current/)

## 管理维护{#administrator}

### 修改密码

修改密码只需登录服务器后运行一条命令即可：  

下面的示例是将旧密码`neo4j`更改为新密码`neo4j123`：

  ```
  echo "
  ALTER CURRENT USER SET PASSWORD FROM 'neo4j' TO 'neo4j123';
  " | cypher-shell -u neo4j  -p neo4j  -d system
  ```

### 找回密码

Neo4j 官方提供 [Password and user recovery](https://neo4j.com/docs/operations-manual/current/configuration/password-and-user-recovery/) 方案：

1. 配置文件临时去掉验证（增加配置段 `dbms.security.auth_enabled=false` ）
2. 设置密码，再复原配置文件  


## 故障

#### 连接数据库报错？ 

问题描述：Neo4j Browser 连接数据库报错。
原因分析：您的服务器对应的**安全组端口**没有开启（入规则），导致无法连接数据库  

#### Roles 显示为空？

Neo4j 社区版不支持 Roles，故显示为空

## 原理学习

Neo4j 是目前主流的图数据库（graph database）产品，图数据库用于存在数据关系，更有利于关系的优化管理，存储和遍历节点和关系。  

对于 Neo4j 管理员来说，需要掌握的知识点包括：

* 图数据库核心思想
* Neo4j 架构
* 可视化管理：Neo4j Browser, Neo4j Desktop等
* 高级管理技术：升级、客户端工具使用、日志管理、备份恢复、监控
* 优化技术：负载均衡、集群
* 安全技术：授权与认证，用户管理

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

### 部署

Neo4j 是基于 Java 开发，因此运行它需要预先安装 JDK。  

* Linux：官方提供 rpm/deb 包的安装方式
* Windows/macOS：官方提供了一键安装包
* Docker：DockerHub上有一个官方的 [Neo4j 映像](https://hub.docker.com/_/neo4j/)

另外，官方提供无需安装的 [Neo4j Aura](https://neo4j.com/cloud/aura/?ref=menu) 托管平台，让用户专注于在线使用。  

### 集群

参考官方文档：[Clustering](https://neo4j.com/docs/operations-manual/current/clustering/)  

> 仅企业版支持集群

### Fabric

Neo4j Fabric 类型视图的概念，使用单个Cypher查询在多个数据库中存储和检索数据的方法。  

参考官方文档：[Neo4j Fabric](https://neo4j.com/docs/operations-manual/current/fabric/introduction/#fabric-introduction)

### 认证与授权

参考官方文档：[Authentication and authorization](https://neo4j.com/docs/operations-manual/current/authentication-authorization/)

### 安全

参考官方文档：[Neo4j Security](https://neo4j.com/docs/operations-manual/current/security/)

### 监控与维护

参考官方文档：[Monitoring](https://neo4j.com/docs/operations-manual/current/monitoring/)

### 性能

参考官方文档：[Performance](https://neo4j.com/docs/operations-manual/current/performance/)