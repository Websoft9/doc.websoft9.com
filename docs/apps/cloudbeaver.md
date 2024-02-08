---
title: CloudBeaver
slug: /cloudbeaver
tags:
  - 数据库管理
  - 可视化
  - Web界面
  - MySQL
  - Postgres
  - Oracle
---

import Meta from './_include/cloudbeaver.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 CloudBeaver 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 使用本地电脑浏览器访问，进入初始化页面
   ![初始化 CloudBeaver](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-wizard001-websoft9.png)

2. 设置用户名和密码，然后点击【Next】进入下一步
   ![初始化 CloudBeaver](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-wizard002-websoft9.png)

3. 继续点击【Next】进入下一步，最后点击【FINISH】完成初始化
   ![初始化 CloudBeaver](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-wizard003-websoft9.png)

4. 默认已经存在一个 SQlite 的演示连接
   ![初始化 CloudBeaver](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-wizard004-websoft9.png)

5. 通过：【Administrator】>【Connection Management】，删除【SQLite - Chinook (Sample)】，避免遭受 SQL 注入攻击
   ![初始化 CloudBeaver](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-wizard005-websoft9.png)

6. 再回到主页，默认的 SQLite 演示连接已经不存在


### 管理数据库

#### MySQL{#mysql}

提前准备 MySQL 服务并确保远程访问已开放。如果没有准备，可以通过 Websoft9 应用商店安装一个 MySQL

1. 登录 CloudBeaver 控制台，点击右上角【Settings】图标，选择【Administration】>【Connection Management】，添加对应数据库，进行连接管理  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-connection-websoft9.png)

2. 设置连接信息：主机地址、端口、账号密码（可以勾选是否保存），然后点击【Save】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conmysql002-websoft9.png)

3. 设置信息保存后，使用这个 MySQL 连接，输入数据库的账号和密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conmysql003-websoft9.png)

4. 成功连接到 MySQL，可以开始管理工作
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conmysql004-websoft9.png)

#### PostgreSQL{#postgresql}

提前准备 PostgreSQL 服务并确保远程访问已开放。如果没有准备，可以通过 Websoft9 应用商店安装一个 PostgreSQL

1. 登录 CloudBeaver 控制台，点击右上角【Settings】图标，选择【Administration】>【Connection Management】，添加对应数据库，进行连接管理  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-connection-websoft9.png)

2. 设置连接信息：主机地址、端口、账号密码（可以勾选是否保存），然后点击【Save】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-connsetting-websoft9.png)

3. 设置信息保存后，使用这个 PostgreSQL 连接，输入数据库的账号和密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. 成功连接到 PostgreSQL，可以开始管理工作

#### SQLServer{#sqlserver}

提前准备 SQLServer 服务并确保远程访问已开放。如果没有准备，可以通过 Websoft9 应用商店安装一个 SQLServer

1. 登录 CloudBeaver 控制台，点击右上角【Settings】图标，选择【Administration】>【Connection Management】，添加对应数据库，进行连接管理  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-connection-websoft9.png)

2. 设置连接信息：主机地址、端口、账号密码（可以勾选是否保存），然后点击【Save】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-connsetting-websoft9.png)

3. 设置信息保存后，使用这个 SQLServer 连接，输入数据库的账号和密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. 成功连接到 SQLServer，可以开始管理工作

#### SQLite{#sqlite}

提前准备 SQLite 服务并确保远程访问已开放。如果没有准备，可以通过 Websoft9 应用商店安装一个 SQLite

1. 登录 CloudBeaver 控制台，点击右上角【Settings】图标，选择【Administration】>【Connection Management】，添加对应数据库，进行连接管理  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-connection-websoft9.png)

2. 设置连接信息：主机地址、端口、账号密码（可以勾选是否保存），然后点击【Save】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-openconnsqlite-websoft9.png)

3. 设置信息保存后，使用这个 SQLite 连接，输入数据库的账号和密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. 成功连接到 SQLite，可以开始管理工作

#### Oracle Database{#oracle}

提前准备 Oracle Database 服务并确保远程访问已开放。如果没有准备，可以通过 Websoft9 应用商店安装一个 Oracle Database

1. 登录 CloudBeaver 控制台，点击右上角【Settings】图标，选择【Administration】>【Connection Management】，添加对应数据库，进行连接管理   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-connection-websoft9.png)

2. 设置连接信息：主机地址、端口、账号密码（可以勾选是否保存），然后点击【Save】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-connsetting-websoft9.png)

3. 设置信息保存后，使用这个 Oracle 连接，输入数据库的账号和密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. 成功连接到 Oracle，可以开始管理工作

### 共享数据连接

共享数据连接是指管理员可以通过更改连接配置来向用户团队授予共享连接访问权限。

1. 配置连接为 Shared（共享）

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-share-set-websoft9.png)

2. 向用户授权

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-access-set-websoft9.png)


## 配置选项{#configs}

- 多语言（✅）：不支持中文
- 数据库连接驱动：JDBC
- 配置文件：/path/GlobalConfiguration/.dbeaver/data-sources.json
- [支持的数据库](https://dbeaver.com/databases/)

## 管理维护{#administrator}

### 驱动管理

[Driver managements](https://cloudbeaver.io/docs/Driver-managements/)

### 导出数据

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-exportdata-websoft9.png)

## 故障

#### 连接 Oracle 数据库失败？

如果账号准确无误，仍然无法连接 Oracle 数据库。此时，考虑 CloudBeaver 数据库驱动是否与 Oracle 版本匹配。 