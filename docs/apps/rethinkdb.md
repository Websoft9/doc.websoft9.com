---
title: RethinkDB
slug: /rethinkdb
tags:
  - RethinkDB
  - Cloud Native Database
---

import Meta from './_include/rethinkdb.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 RethinkDB 后，通过【我的应用】进入它的编辑窗口，在**访问**标签页中获取登录地址和账号。  

1. 使用本地电脑的浏览器后，准备登陆 RethinkDB 控制台

2. 输入用户名和密码，成功登录到 RethinkDB 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-gui-websoft9.png)

### 增加 Database 和 Table

下面以 **演示如何增加 Database 和 Table** 作为一个任务，帮助用户快速入门：

1. 依次打开：【Tables】>【Add Database】，增加一个数据库
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-adddb-websoft9.png)

2. 打开数据库，点击【Add Table】增加表
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-addtable-websoft9.png)


## 管理维护{#administrator}

### 远程访问{#remote}

RethinkDB 远程访问的开关存储在：*/etc/rethinkdb/instances.d/instance.conf* 文件中(容器内部)。  

只需执行下面命令，然后重启服务，即可开启远程访问。

```
sudo sed -n "s/^#bind=/bind=0.0.0.0/g" /etc/rethinkdb/instances.d/instance.conf
```
### 用户管理

下面以**新增用户、密码和重置密码**作为范例进行说明：


1. 以 `admin` 用户身份连接数据库（只有 admin 用户具有用户系统表的访问权限，因此必须以 admin 用户连接到数据库）
   ```
   from rethinkdb import r

   # 无密码连接
   r.connect('localhost', 28015).repl()

   # 有密码连接
   r.connect('localhost', 28015, password='123456').repl()
   ```

2. 新增用户名和密码（用户信息存储在 **users** [系统表](https://rethinkdb.com/docs/system-tables/)中）
   ```
   r.db('rethinkdb').table('users').insert({id: 'bob', password: 'secret'})
   ```

3. 重置指定用户的密码

    ```
    # 重置为新密码
    r.db('rethinkdb').table('users').get('username').update({password: newpassword})

    # 重置为空密码
    r.db('rethinkdb').table('users').get('username').update({password: false})
    ```

### 重置密码

常用的 RethinkDB 重置密码相关的操作主要有修改密码和清空密码（将密码设置为空）两种方式。  

1. 登录 RethinkDB Web 界面，在【Data explorer】下输入所需的命令

   ```
   # 修改密码命令
   r.db('rethinkdb').table('users').get('admin').update({password: 'newpassword'})

   # 清空密码命令
   r.db('rethinkdb').table('users').get('admin').update({password: false})
   ```
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-editpassword-websoft9.png)

2. 点击【run】后生效


### 图形化工具

RethinkDB 可视化控制台是它的重要组成部分，是其重要的产品特征。  

1. 使用本地电脑的浏览器访问网址：*`http://服务器公网IP:9090`*，准备登陆 RethinkDB 控制台

2. 输入用户名和密码（[不知道账号密码？](./user/credentials)）

3. 成功登录到 RethinkDB 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-ok-websoft9.png)

4. 依次打开：【Tables】>【Add Database】，增加一个数据库
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-adddb-websoft9.png)

5. 打开数据库，点击【Add Table】增加表
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-addtable-websoft9.png)


### 客户端

RethinkDB 官方没有客户端 CLI，但提供了Python, Java, Node 等开发语言的 [RethinkDB client drivers](https://rethinkdb.com/docs/install-drivers/)。  

用户通过这些 drivers 以程序的方式连接 RethinkDB 服务，然后进行场景的数据库操作。  

下面以 Python 为例描述如何具体使用：

1. 安装 rethinkdb 驱动
   ```
   pip3 install rethinkdb
   ```

2. 编写 Python 程序，连接 RethinkDB 服务器
   ```
   from rethinkdb import r
   r.connect('localhost', 28015).repl()
   r.db('test').table_create('tv_shows').run()
   r.table('tv_shows').insert({ 'name': 'Star Trek TNG' }).run()
   ```

### 命令行

RethinkDB 提供了强大的的**服务端**命令行工具 `rethinkdb`  

### 备份
RethinkDB 主要通过导出的实现备份，通过导入实现恢复：

```
# 导出普通数据库文件
rethinkdb export abc.db

# 导出压缩格式数据库文件
rethinkdb dump [options]
```

### 恢复

```
rethinkdb import -d [options]
```

### 升级

官方没有提供版本升级命令，只提供了一个升级后的数据迁移方案：[Migrating](https://rethinkdb.com/docs/migration/)

## 故障

## 问答


#### 是否有 RethinkDB 的 CLI 工具？

有，安装后存在cli命令，通过 `rethinkdb -h`查看使用详细

#### `rethinkdb repl` 命令如何密码登录？

```
rethinkdb repl --password-file /tmp/pw
```

其中 /tmp/pw 为存放密码明文的文件。

#### RethinkDB 提供哪些驱动？

我们提供 Ruby，Python，Java和JavaScript / Node.js的官方驱动程序。社区支持的驱动程序支持十多种其他语言，包括C＃/。NET，Go和PHP。

#### 可否命令行修改 RethinkDB 控制台密码？

参考：[Nginx auth_basic](../nginx#authbasic)

#### 通过端口可直接访问 RethinkDB 吗？

不可以，为了安全考量默认仅支持 127.0.0.1 访问，所以需通过 Nginx 转发。

#### RethinkDB 使用的是什么查询语言？

RethinkDB 不支持传统是数据库语言 SQL 。但是，RethinkDB的查询语言 [ReQL](https://rethinkdb.com/docs/introduction-to-reql/) 几乎可以执行 SQL 所能做的一切，包括表联接和聚合功能，并且功能强大，表达力强且易于学习。  
 
ReQL还可以完成SQL无法完成的许多工作，包括将查询与JavaScript表达式和map-reduce混合使用。

#### RethinkDB 权限如何控制？

权限存储在 permissions 系统表中。虽然您可以通过修改该表中的文档来更改权限，但使用grant命令要方便得多。

默认支持四种权限：

* read
* write
* config
* connect

有三种权限范围：  

* 表（仅影响表）
* 数据库（影响数据库和其中的表）
* 全局（影响所有数据库和其中的表）

#### RethinkDB 系统表有什么作用？

RethinkDB 维护特殊的[系统表](https://rethinkdb.com/docs/system-tables/)，其中包含有关服务器、数据库、单个表和集群问题的配置和状态信息。

#### RethinkDB vs MongoDB？

RethinkDB 是一个与 MongoDB 对标的开源数据库，RethinkDB 定位于实时数据库应用：

- 协作式Web和移动应用程序
- 流分析应用
- 多人游戏
- 实时市场
- 连接的设备

#### 如何设置 RethinkDB 的初始密码？

默认管理员用户名为 `admin`，密码为空。通过服务端命令行，可以很方便的设置管理员密码：

```
rethinkdb --initial-password yourpassword
```