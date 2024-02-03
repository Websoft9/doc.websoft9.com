---
title: SQLite
slug: /sqlite
tags:
  - 云数据库
  - SQL
---

import Meta from './_include/sqlite.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 SQLite 后，通过【我的应用】进入它的编辑窗口，在**访问**标签页中获取登录地址和账号。  

1. exec 到容器

2. 运行 `sqlite3` 命令，显然类型下面的结果，即表明运行正常
   ```
   [root@VM-0-11-centos ~]# sqlite3
   SQLite version 3.29.0 2019-07-10 17:32:03
   Enter ".help" for usage hints.
   Connected to a transient in-memory database.
   Use ".open FILENAME" to reopen on a persistent database.
   sqlite>
   ```

3. 验证 [SQLite 可视化](#gui)管理工具

### 程序连接

开发需要连接 SQLite，首先需要保证已经安装了对应的 SQlite 连接模块：

* PHP 默认安装并启用了 SQLite 扩展
* Python  默认安装了 SQLite 模块
* Java 需自行安装[SQLite JDBC Driver](https://github.com/xerial/sqlite-jdbc/releases)

下面是一个典型的 PHP 连接 SQLite 的程序段：

    ```
    <?php
      class MyDB extends SQLite3
      {
          function __construct()
          {
            $this->open('test.db');
          }
      }
      $db = new MyDB();
      if(!$db){
          echo $db->lastErrorMsg();
      } else {
          echo "Opened database successfully\n";
      }
    ?>
    ```

### 图形化工具{#gui}

SQLite 数据库管理工具建议使用 `CloudBeaver` 。  

下面我们完成的介绍如何使用可视化工具管理 SQLite。

#### 准备

1. 使用 SSH 连接 SQLite 所在的服务器，在 [SQLite 数据文件目录](#path)下创建一个数据库
   ```
   # 创建数据库
   cd /data/apps/cloudbeaver/volumes
   sqlite3 testDB.db
   
   # 增加表
   sqlite> CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
   )
   ```

2. 登录云控制台，开启服务器 安全组 9090 端口

3. 完成 [CloudBeaver 初始化](./cloudbeaver)


#### 配置

完成上述准备工作后，我们开始连接 SQLite 数据库：  

1. 登录 CloudBeaver 控制台，打开：【Connection】>【Manual】，选择 **SQLite**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-openconn-websoft9.png)

2. 参考下面的建议，设置连接信息，然后点击【Save】

   - Driver 保持默认的 SQLite
   - Connection Name 设置为一个便于识别的名字即可
   - Database 为 SQLite 数据库文件的路径，路径前缀必须是：**/opt/cloudbeaver/workspace/**，再接上文件名称

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-openconnsqlite-websoft9.png)

3. 设置信息保存后，使用这个 SQLite 连接，输入数据库的账号和密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-conlogin-websoft9.png)

4. 成功连接到 SQLite，发现可以看到之前创建的 Company 表
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-listtable-websoft9.png)


### 常用命令

SQLite 提供了强大的的命令行工具 `sqlite3`  

#### 程序命令行

```
# 创建数据库
sqlite3 testDB.db

# 查看帮助
sqlite3 --help

# 查看版本
sqlite3 --version
```

#### 交互式命令行

以 `sqlite3 testDB.db` 命令，进入 SQLite 运行状态后，开始使用数据库交互式命令行

```
# 获取帮助
sqlite> .help

# 查询数据库列表
sqlite> .database

# 附件一个数据库。
# 数据库名称 main 和 temp 被保留用于主数据库和存储临时表及其他临时数据对象的数据库，不可用于附加
sqlite> ATTACH DATABASE 'myDB.db' as 'TEST'

# 创建表
sqlite> CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
)

# 查询表
sqlite> .tables

````


## 管理维护{#administrator}

### SQLite 备份

通过 SFTP 将 SQLite 数据库文件（一般以 .db 结尾）下载到本地

### SQLite 升级

如果系统仓库中的 SQLite 版本比较低，又想升级到指定的版本，可以参考如下教程： 

> 升级之前请确保您已经完成了服务器的镜像（快照）备份

1. 找到所需 SQLite 目标版本的[下载地址](https://www.sqlite.org/chronology.html)

2. 分别运行如下的升级命令
   ```
   # 下载 SQLite 源码（自行替换）
   wget https://www.sqlite.org/2019/sqlite-autoconf-3290000.tar.gz

   # 编译
   tar zxvf sqlite-autoconf-3290000.tar.gz 
   cd sqlite-autoconf-3290000/
   ./configure --prefix=/usr/local
   make && make install
   
   # 替换旧版本
   mv /usr/bin/sqlite3  /usr/bin/sqlite3_old
   ln -s /usr/local/bin/sqlite3   /usr/bin/sqlite3
   echo "/usr/local/lib" > /etc/ld.so.conf.d/sqlite3.conf
   ldconfig
   sqlite3 -version
   ```


## 故障

#### SQLite 不支持用户名和密码验证？

不支持