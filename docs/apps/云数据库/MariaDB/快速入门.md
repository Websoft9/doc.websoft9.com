---
sidebar_position: 1
slug: /mariadb
tags:
  - MariaDB 
  - Cloude Native Database
---

# 快速入门

[MariaDB](https://mariadb.org/) 是一个在全球广受欢迎的关系型数据库系统。它由 MySQL 创始人 Michael Widenius 于2014年联合旧部在芬兰创立，这个名称来自他的女儿 Maria 的名字。MariaDB最初被设计为MySQL的增强，直接替代品，之所以被使用是因为它具有快速，可扩展和强大的功能，并具有丰富的存储引擎，插件和许多其他工具生态系统，因此对于各种用例都非常通用。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mariadb/mariadb-gui-websoft9.png)

在云服务器上部署 MariaDB 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:3306** 和 **TCP:9090** 端口是否开启

> 3306 端口用于远程连接 MariaDB，9090 端口用于访问 phpMyAdmin

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

如果是 Windows 服务，打开桌面上的 password 快捷方式（路径：C:/credentials/password.txt）

### MariaDB

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

 > 需要登录MariaDB，请参考 [图形化工具：phpMyAdmin](/zh/solution-phpmyadmin.md)


## MariaDB 入门向导

部署 MariaDB 之后，依次完成下面的步骤，验证其可用性

1. 使用 SSH 连接 MariaDB 所在的服务器，运行下面的命令，查看 MariaDB 的安装信息和运行状态
   ```
   sudo systemctl status mariadb
   ```
2. 运行服务状态查询命令，MariaDB 正常运行会得到 " Active: active (running)... " 的反馈

3. 镜像安装完成后，MariaDB就可以使用了。
   ```
   # 查看使用 MariaDB 使用手册
   man mariadb
   ```
   
镜像安装完成后，MariaDB 就可以使用了。使用 MariaDB 有两种方式:

### 命令方式连接 MySQL

1. 使用 SFTP 或 SSH 客户端连接服务器，运行下面的命令：
   ```
   # 获取数据库密码
   cat /credentials/password.txt

   # 登录数据库，并输入密码后登录
   mariadb -uroot –p
   ```

2. 连接成功后显示的信息
   ```
   Welcome to the MariaDB monitor.  Commands end with ; or \g.
   Your MariaDB connection id is 14
   Server version: 10.4.17-MariaDB MariaDB Server
   Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.
   Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
   MariaDB [(none)]>
   ```

### phpMyAdmin 连接 MariaDB

我们的部署方案中包含 phpMyAdmin 图形化工具，使用它管理 MariaDB 简单快捷：

1. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)

2. 输入数据库用户名和密码([不知道密码？](/zh/stack-accounts.md#mariadb))

3. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 需要了解更多 phpMyAdmin 的使用，请参考本文档 [phpMyAdmin 章节](/zh/solution-phpmyadmin.md)


## 常用操作

### 修改密码

常用的 MariaDB 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码

可以通过 MariaDB 可视化管理工具修改密码，也通过命令行修改密码

* 通过 phpMyAdmin 修改密码
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/websoft9-modifymysqlpw.gif)

* 通过命令行修改密码
   ```
   mysqladmin -u 用户名 -p 旧密码 password '新密码' 
   ```

#### 找回密码

如果忘记了 root 密码，就需要通过命令操作，实现MariaDB密码重置。  

为了用户使用方便，我们已经将 MariaDB 重置密码写成脚本，使用只需两步：

1. 使用SSH远程连接到 MariaDB 服务器
2. 运行如下命令，按提示输入新密码即可。
   ```
   wget -N https://raw.githubusercontent.com/websoft9dev/role_mariadb/master/tools/reset_password.sh; bash reset_password.sh
   ```


### 远程访问

当你想通过本地的电脑的MariaDB客户端（例如：Navicat）连接服务器上的MariaDB的时候，就需要设置 MariaDB 的远程访问。

数据库是高安全应用，设置远程访问，最少两个独立的步骤：

#### 安全组放通3306端口

一般来说，MariaDB使用的是3306端口。

首先，我们要登录到云控制台，打开云服务器所在的安全组中，保证3306端口是开启的。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/mysql3306-websoft9.png)


#### 开启MariaDB远程连接

安全组开启后，还没有完成MariaDB远程方案的设置。  

接下来，还需要对 MariaDB 自身进行设置，以便其接受外部网络的访问

我们提供两种开启MariaDB的远程连接的方案，第一种是可视化方式，第二种是命令方式：  

##### 可视化开启（推荐）

在phpMyAdmin中开启远程只需要将root账号的访问方式改成“任意方式访问”，具体如下：

1. 打开账户->找到主机名为127.0.0.1的root用户，点击“修改权限”
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/mysql-openremote001-websoft9.png)
2. 在“登录信息”选项卡中，将“主机名”下拉菜单选项更改为“任意主机”，点击执行
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/mysql-openremote002-websoft9.png)
3. 以上两步就完成了开启远程连接的工作

##### 命令开启

如果您的镜像中没有安装phpMyAdmin，那么就需要通过命令方式开启远程连接。具体如下：

1. 使用SSH连接到服务器，登录到MariaDB
   ```
   mysql -u root -p 数据库root密码
   ```
 
2. 写入SQL语句,开启远程访问
   ```
   mysql>  use mysql;
   mysql>  update user set host = '%' where user = 'root';
   ```

3. 运行下面的语句，查看设置是否生效（显示%的值）
   ```
   select host,user from user where user='root'
   ```
4. 退出MariaDB命令，回到Linux命名模式，重启MariaDB
   ```
   systemctl restart mariadb
   ```
   > 本步骤是必须的，否则在用Navicat Premium/MariaDB-Front等工具测试远程的时候会报错误信息

### 更换 MariaDB 数据目录

MySQL 的数据目录默认设置为 */data/mariadb*。 想修改 MySQL 数据目录，按以下步骤操作：

1. 停止 MySQL 服务
   ```shell
   sudo sytemctl stop mariadb
   ```
2. 将 */data/mariadb* 移动到目标新目录，例如 */data/mariadb2*
3. 修改配置文件`/etc/my.cnf`文件的 datadir 配置：
   ```shell
   datadir=/data/mariadb2
   ```
4. 重启服务
   ```shell
   sudo sytemctl start mariadb
   ```


### 设置 Binary Log

二进制日志包含描述数据库更改的“操作”，例如创建表操作或更改表数据。 它还包含可能已进行更改的语句的操作（例如，不匹配任何行的 DELETE）。 二进制日志还包含有关每条语句使用更新数据的时间信息。

#### 二进制日志配置

修改 MySQL 配置  /etc/my.cnf 以更改二进制日志的设置

```
log_bin = mysql-bin      # enable Binary log
binlog_format = mixed    # Binary log format
expire_logs_days = 7     # Binary log expire time
```

#### 二进制日志文件大小

有时候，数据库发生了很多事件，二进制日志文件大小增长非常快，你的磁盘空间可能不够用，如果磁盘上没有空间，MySQL 服务就无法启动。

如果您的二进制日志文件太大，建议将 expire_logs_day 更改为更小，定时清理日志文件。

### 权限设置

###  图形化工具：phpMyAdmin

phpMyAdmin是很受欢迎的MariaDB数据库管理工具，下面介绍常见的phpMyAdmin操作

## 修改root密码

1. 登录phpMyAdmin后，默认页面-常规设置，点击“修改密码” 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-modifypw-websoft9.png)
2. 修改密码-&gt;保存-&gt;退出登录，刷新浏览器后便可以使用新密码登录了

## 新增数据库

1. 登录phpMyAdmin后，点击左侧菜单栏的“新建”，进入如下的数据库创建界面 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)
2. 填写数据库名-&gt;点击创建按钮，一个新的数据库变建立成功
3. 默认情况下，root拥有新建的数据库的全部权限

## 新增数据库用户

> 数据库用户与数据库是分离的，是“多对多”的关系。可以通过关联使得某个用户具有某个数据库的权限

1. 登录phpMyAdmin后，点击左侧菜单栏中新打算对其新增用户的数据库（例如：mywebsoft9）
2. 点击顶部菜单栏的“权限”，找到“新增用户账户”，如下新增用户界面 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adduser-websoft9.png)
3. 根据上图填写用户名、主机地址和密码，然后关联对应的数据库和勾选权限设置
4. 点击“执行”，就完成新增用户和数据库关联了

说明：也可以登录phpMyAdmin的默认页面后，点击顶部菜单上“账户”，对用户和权限进行管理

## 数据库导入和导出

> 导出即备份数据库，导入即恢复数据库。这个两个操作对phpMyAdmin来说比较简单，具体如下：

1. 登录phpMyAdmin后，选择您需要操作的数据库后，点击顶部菜单栏的“导出” 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)
2. 选择导出方式（默认为“快速”）和格式（默认为“SQL”），点击“执行”按钮
3. 数据库备份文件（.sql后缀）生成后，保存到本地完成导出工具
4. 恢复数据库，对应的是“导入”操作，具体参考下图 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-import-websoft9.png)
5. 导入文件特别要注意字符集兼容性

## phpMyAdmin 限制特定 IP 访问

把 phpMyAdmin.conf（```/etc/httpd/conf.d/phpmyAdmin.conf```）文件中的：  
     ```Require all granted``` 
改为：  
     ```Require ip xxx.xxx.xxx.xxx```  
这样，只有指定 IP 的主机能访问 phpMyAdmin，IP还可以缩写：192.168.*.* 这样则表示以 192.168 开头的 IP 段都能访问。 修改完成后需要重启 Apache

## 设置支持多个数据库实例

phpMyAdmin 支持多个数据库实例，只需要修改 docker-compose 文件的对应的环境变量（PMA_HOST 更改为 PMA_HOSTS）即可  
```
version: "3.7"
services:
  phpmyadmin:
      image: phpmyadmin/phpmyadmin
      container_name: "phpmyadmin"
      environment:
       - PMA_HOSTS=172.17.0.1,172.17.0.2
       - PMA_PORTS=3306
       - UPLOAD_LIMIT=20M 
      restart: always
      ports:
       - 9092:80
      volumes:
       - "/data/apps/phpmyadmin/config.user.inc.php:/etc/phpmyadmin/config.user.inc.php"

networks:
  default:
    external:
      name: "apps"
```

### 图形化工具：Navicat

如果你已经开启服务器安全组3306端口，并设置完成 MariaDB 远程连接，可以参考如下的步骤使用 Navicat：

1. 打开Navicat Premium，点击顶部菜单栏， 【文件】>【新建连接】>【MariaDB】
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/websoft9-mysql-navcaittest.png)

2. 自定义连接名，将localhost更改为数据库所在的主机公网IP地址

3. 输入账号和密码（[不知道账号密码？](/zh/stack-accounts.md)）

3. 点击“测试连接”，系统提示：连接成功 ! 即表示成功连接
    


## 异常处理

#### 浏览器无法访问 phpMyAdmin（白屏没有结果）？

您的服务器对应的安全组 9090 端口没有开启（入规则），导致浏览器无法它

#### phpMyAdmin 是如何安装的？

采用 Docker 安装，保证 MariaDB 环境具有良好的隔离性。