---
sidebar_position: 1
slug: /oracle
tags:
  - Oracle Database
  - Cloude Native Database
---

# 快速入门

Oracle Database 11*g* 快捷版 ([Oracle Database XE](http://www.oracle.com/technetwork/cn/database/database-technologies/express-edition/index.html)) 是一款基于 Oracle Database 11*g* 第 2 版代码库的小型入门级数据库，它具备以下优点：免费开发、部署和分发；下载速度快；并且管理简单。Oracle Database XE 是一款优秀的入门级数据库，可供以下用户使用:

*   致力于 PHP、Java、.NET、XML 和开源应用程序的开发人员
*   需要免费的入门级数据库进行培训和部署的 DBA
*   需要入门级数据库进行免费分发的独立软件供应商 (ISV) 和硬件供应商
*   需要在课程中使用免费数据库的教育机构和学生

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle_database/oracle-database-1024x410.jpg)

现在，利用 Oracle Database XE，您可以使用强大的、公认的、行业领先的基础架构来开发和部署应用程序，然后在必要时进行升级而不必进行昂贵和复杂的迁移。Oracle Database XE 对安装主机的规模和 CPU 数量不作限制（每台计算机一个数据库），但 XE 将最多存储 11GB 的用户数据，最多使用 1GB 内存，使用主机上的一个 CPU。版权说明：在使用软件之前，建议阅读[ Oracle Database 快捷版 11*g* 第 2 版的 OTN 许可协议](http://www.oracle.com/technetwork/licenses/database-11g-express-license-459621.html)

在云服务器上部署 Oracle Database 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 如果想从本地客户端远程连接 Oracle Database，登录云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:1521** 端口是否开启


## 账号密码

使用 Oracle Database，可能会用到的几组账号密码如下：

### Oracle Database

Oracle 的 system 账户默认密码已优化为强随机密码，查看方式：

1. 使用 [SFTP远程管理工具](http://support.websoft9.com/docs/linux-sftp/) 连接到服务器；
2. 找到 **password.txt** 文件 ( **/root/password.txt** )，打开即可查看 Oracle Database 数据库用户名和密码；
3. 若无 **password.txt** 文件，则为旧版镜像，其 Oracle Database 默认用户名和密码为 ：`system/123456`；
4. 查看密码后，可自行访问 http://公网IP/phpmyadmin 管理数据库相关信息。
   
  >[danger] 默认的 “123456” 请务必修改为强密码，类似于：f@N7eUUm25xAjP!$ ，这样有助于提高数据库的安全性，减少数据库密码被破解的风险。


## Oracle Database 入门向导

### 可视化管理 Oracle Database

Oracle Database支持第三方可视化数据库管理工具，例如Navicat,Maestro,Oracle企业管理器等。下面以使用最为广泛的Navicat为例来说明如何管理本镜像的数据库：

1.  [下载](http://www.navicat.com.cn/download/navicat-for-oracle)并安装Navicat For Oracle
2.  新建一个Oracle连接，填写好连接参数（用户名为：system，密码为：123456；端口1521不能更改，另外请确保云服务器控制台上的安全组打开了TCP:1521），点击“连接测试”，成功标明参数没有问题。
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle_database/oracle11gex-conn-websoft9.png)
3.  点击确认后，进入数据库管理界面
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle_database/oracle11gex-ui-websoft9.png)

### 通过 SSH 管理 Oracle Database？

通过SSH管理Oracle数据库是一种常见的使用方式，以Putty为例：

1.  以root账号登录服务器
2.  输入sqlpus命令，根据系统要求输入账号（system/123456），数据库登录成功
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle_database/oracle11gex-sqlrun-websoft9.png)
3.  运行一条命令测试可用性，例如：select * from v$version;  （查询数据库版本信息）


## 常用操作

### 开启 Oracle Database 远程连接

镜像默认已经设置好了远程连接，只需开启安全组 `TCP:1521` 端口即可启用远程访问

### 启停 Oracle Database 服务

使用本镜像，可能需要用到的命令如下：

>启动数据库服务
service start oracle
>查看监听状态
在Oracle用户下执行：lsnrctl status
然后使用Oracle工具连接数据库。
>关闭数据库和监听
service stop oracle

## 异常处理

#### 浏览器无法访问 phpMyAdmin（白屏没有结果）？

您的服务器对应的安全组9090端口没有开启（入规则），导致浏览器无法它

#### phpMyAdmin 是如何安装的？

采用 Docker 安装，保证 Oracle Database 环境具有良好的隔离性。