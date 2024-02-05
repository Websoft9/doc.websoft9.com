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



   ![Neo4j Browser](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-connectfirst-websoft9.png)

#### 命令行连接

### 详细步骤

1. 使用 **SSH** 客户端连接 Neo4j 所在的服务器，输入 `cypher-shell` 命令，并登录（[不知道密码？](./user/credentials)）

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

### 图形化工具

Neo4j 提供了多种图形化工具，有基于 Web 的版本，也有支持 Windows, Linux, macOS 等桌面版本。

在使用图形化工具之前，请确保[开启了远程访问](#remote)。

#### Neo4j Browser{#browser}

Neo4j Browser 是开发人员与图形进行交互的工具。它是Neo4j数据库的企业版和社区版的默认界面。

1. 本地浏览器访问：*http://域名* 或 *http://服务器公网IP*, 访问 Neo4j Browser
![Neo4j Browser](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-connectfirst-websoft9.png)

2. 选择【bolt://】的URL模式，输入用户名和密码（[不知道密码？](./user/credentials)），可能还需提示立即修改密码
![修改Neo4j密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-snewpw-websoft9.png)

> Pick neo4j:// for a routed connection, bolt:// for a direct connection to a DBMS. 选择 bolt:// 速度更快

3. 系统登录到控制台，初始化安装完成
![Neo4j 控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-ssui-websoft9.png)

4. 通过:【Database Information】>【server user add】 增加新用户
![Neo4j 增加用户](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-adduser-websoft9.png)

5. 通过:【Cloud Services】>【Clear local data】 退出 Neo4j Browser 
![Neo4j 增加用户](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-loginout-websoft9.png)

#### Neo4j Desktop{#desktop}

[Neo4j Desktop](https://neo4j.com/download-center/) 是开发人员使用本地Neo4j数据库的便捷方式。

1. [下载](https://neo4j.com/download-thanks-deskto)

2. 双击安装至完成，然后到 Neo4j 官网上注册，获取一个秘钥

3. 激活 Neo4j Desktop

4. 连接到远程 Neo4j 数据库，开始使用

#### Neo4j Bloom

探索和可视化图形数据，这是一个付费的工具。

### 用户管理

Neo4j 提供了详细的用户管理和角色管理功能（仅企业版支持）

```
# 显示所有用户
SHOW USERS;
CALL dbms.security.listUsers();

# 创建新用户，第三个参数表示 requridchangepassword 
CALL dbms.security.createUser('username','password',false);

# 删除用户
CALL dbms.security.deleteUser('username');   
```

详情参考官网文档：[User and role management](https://neo4j.com/docs/cypher-manual/current/administration/security/users-and-roles/#administration-security-users)

## 配置选项{#configs}
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

可通过配置文件临时去掉验证（增加一段 `dbms.security.auth_enabled=false` ），然后设置密码，再复原的方法找回密码。  

详情参考：[Password and user recovery](https://neo4j.com/docs/operations-manual/current/configuration/password-and-user-recovery/)


## 故障

#### 更改域名导致无法访问 Neo4j ？

#### 访问 Neo4j 出现 502 错误？{#502}