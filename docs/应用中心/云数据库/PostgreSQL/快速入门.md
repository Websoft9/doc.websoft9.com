---
sidebar_position: 1
slug: /postgresql
tags:
  - PostgreSQL
  - Cloud Native Database
---

# 快速入门

[PostgreSQL](https://www.postgresql.org/) 是一个功能强大的开源对象关系数据库系统（RDBMS），经过30多年的积极开发，在可靠性，功能强大和性能方面赢得了极高的声誉。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin4-websoft9.png)

在云服务器上部署 PostgreSQL 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 如果想从本地客户端远程连接 PostgreSQL，登录云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:5432** 端口是否开启
3. 如果想使用可视化管理工具 phpPgAdmin，登录云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:9090** 端口是否开启

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### PostgreSQL

- Linux 系统

   * 管理员账号：*`postgres`*
   * 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

- Window 系统

     **密码存储路径**：*C:/credentials/password.txt*     
     **获取方式**： 远程桌面到服务器，打开此文件即可   

 > 需要登录PostgreSQL，请参考图形化工具 [phpPgAdmin](/zh/solution-phppgadmin.md) 或 [PgAdmin](/zh/solution-pgadmin.md)

### phpPgAdmin

phpPgAdmin 共用 PostgreSQL 的账号密码

### pgAdmin 

pgAdmin 有自己的账号密码体系：

* 管理员账号: `user@domain.com`
* 管理员密码: `存储在您的服务器中的文件中 */credentials/password.txt*  

> 登录 pgAdmin 之后请务必修改它的密码

## PostgreSQL 入门向导

部署 PostgreSQL 之后，依次完成下面的步骤，验证其可用性

### 检测 PostgreSQL 安装

1. 使用 SSH 连接 PostgreSQL 所在的服务器，运行下面的命令，查看 PostgreSQL 的安装信息和运行状态
   ```
   sudo systemctl status postgresql
   ```
2. 运行服务状态查询命令，PostgreSQL 正常运行会得到 " Active: active (running)... " 的反馈

镜像安装完成后，PostgreSQL就可以使用了。使用PostgreSQL有两种方式方式

### 命令方式连接 PostgreSQL

先切换到 postgre 用户，在运行 `psql` 命令，即可使用 psql 连接数据库

```
sudo -i -u postgres
psql

psql (12.3)
Type "help" for help.

postgres=#
```

### 图形化工具连接 PostgreSQL

如果部署方案中包含 phpPgAdmin 或 pgAdmin 图形化工具，使用就更加便捷方便：

#### phpPgAdmin

1. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入 phpPgAdmin
   ![登录phpPgAdmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin.png)
   图1. phpPgAdmin 界面

2. 输入数据库用户名和密码([不知道密码？](/zh/stack-accounts.md#postgresql))

3. 开始管理数据库
   ![phpPgadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/phppgadmin-gui-websoft9.png)

#### pgAdmin

1. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入 pgAdmin
   ![登录pgAdmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-loginui-websoft9.png)

2. 输入 pgAdmin 管理员的用户名和密码([查看账号密码](/zh/stack-accounts.md#postgresql))之后，进入控制台
   ![pgAdmin 控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-console-websoft9.png)

2. 点击【Server】>【添加服务器】，使用 pgAdmin 连接 PostgreSQL 数据库([不知道密码？](/zh/stack-accounts.md#postgresql))
   ![pgAdmin 连接服务器](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-createserver-websoft9.png)

3. 开始管理数据库
   ![pgAdmin 管理数据库](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-serverss-websoft9.png)

4. 修改密码
   ![pgAdmin 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin-modifypw-websoft9.png)

> 需要了解更多使用，请参考本文档 [phpPgAdmin 章节](/zh/solution-phppgadmin.md) 或  [pgAdmin 章节](/zh/solution-pgadmin.md) 

## 常用操作

### 设置远程访问

当你想通过本地的电脑的 PostgreSQL 客户端（例如：Navicat/pgAdmin）连接服务器上的 PostgreSQL 的时候，就需要设置 PostgreSQL 的远程访问。

数据库是高安全应用，设置远程访问，最少两个独立的步骤：

#### 云控制台放通 5432 端口

一般来说，PostgreSQL使用的是 **5432** 端口。

首先，我们要登录到云控制台，打开云服务器所在的安全组中，保证3306端口是开启的。

#### 修改 PostgreSQL 配置文件

安全组开启后，还没有完成 PostgreSQL 远程方案的设置。 接下来，还需要对 PostgreSQL 配置文件进行设置，以便其接受外部网络的访问

1. 修改 [postgresql.conf](/zh/components.md#postgresql) 文件
   ```
   #listen_addresses = 'localhost'

   修改为

   listen_addresses = '*'
   ```

2. 修改 [pg_hba.conf]((/zh/components.md#postgresql)) 文件，增加如下一行到文件末尾
   ```
   host    all             all             0.0.0.0/0            md5
   ```

3. 重启 PostgreSQL 后生效
   ```
   systemctl restart postgresql
   ```

### 密码管理

对于 PostgreSQL 来说，由于可以通过 Unix 套字节在无需验证的情况下登录数据库，因此修改密码和重置密码都是同样的操作：

```
# 切换到 postgres 用户
sudo -u postgres psql

# 修改密码
ALTER USER postgres WITH PASSWORD 'postgres';

#exit psql
\q
```

### 更换数据文件路径

1. 备份 */data/postgresql/pgdata* 目录下的所有数据
2. 根据不同的操作系统分别设置

   * RedHat/CentOS  修改 **postgreql.service** 文件中数据目录的环境变量
      ```
      # 查看postgresql.service位置
      systemctl cat postgreql.service 

      # 在 postgresql.servce 中找到下面这行，修改之
      Environment=PGDATA=/var/lib/pgsql/11/data/
      ```
   * Ubuntu  修改 **postgresql.conf** 文件中数据目录
     ```
     data_directory =
     ```
3. 恢复数据到新的目录
4. 重启 PostgreSQL 服务



## 异常处理

#### 浏览器无法访问图形化界面（白屏没有结果）？

您的服务器对应的安全组 9090 端口没有开启（入规则），导致浏览器无法它

#### phpPgAdmin 或 pgAdmin 是如何安装的？

采用 Docker 安装，保证 PostgreSQL 环境具有良好的隔离性。

#### 为什么我的系统中没有 pgAdmin ？

由于产品设计原因，我们从 2021年2月之后的产品中才包含 pgAdmin
