---
sidebar_position: 3
slug: /sqlserver/admin
tags:
  - SQL Server
  - Cloude Native Database
---

# SQLServer Express Maintenance

This chapter is special guide for SQLServer Express maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### SQL Server Upgrade{#upgrade}

SQLServer更新只能是卸载旧版本，然后下载最新的安装包重新安装

### SQL Server Migration{#migration}

SQLServer 数据库存储目录更改:

1. 打开服务列表，先将 SQL Server (MSSQLSERVER) 服务停止；

 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-1-websoft9.png)

2. 将默认的数据库文件拷贝到新的存放位置；
 ```默认存放目录为：C:\Program Files\Microsoft SQL Server\MSSQL11.MSSQLSERVER\MSSQL```

3. 再次启动服务，打开SQL客户端，找到实例，右键实例选择属性；

 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-2-websoft9.png)

4. 在属性中选择 数据库设置，修改数据的存放目录；

 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-3-websoft9.png)

5. 最后重启 SQL Server (MSSQLSERVER) 服务，新建一个数据库测试是否在新的存放目录下生成该数据库；
6. 确保新目录生效后，再将原来的目录下的数据库文件删除。

### SQL Server Manual Backup{#backup}

通用的手动备份操作步骤如下：

1. 访问SQLServer企业管理器，在需要备份的数据库上点右键，选择任务->备份，弹出备份数据库窗口。
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-backup-websoft9.png)
2. 根据备份向导逐步完成备份工作

### SQL Server Express Auto Backup{#autobackup}

SQL Server Express的数据库由于没有SQL Server Agent服务，所以也就不支持维护计划功能，自动备份数据库就成了一个十分麻烦的问题。

**引入 SQL Backup Master**

经过研究，我们建议采用第三方工具 [SQL Backup Master](https://www.sqlbackupmaster.com/)  实现自动备份。SQL Backup Master 是一款免费可靠的 SQL Server 数据库备份工具，主要特性:

* 支持完整备份,差异备份,事务日志备份
* 简单强大的计划任务
* 内置邮件通知
* 支持备份到本地/网络文件夹/网络存储
* 支持备份到FTP/SFTP/FTPS服务器
* 支持备份到Dropbox，Google Drive，Box，Amazon S3，OneDrive和Azure
* 支持操作系统: Windows 10, 8, 7, Vista 和 Windows Server 2008/2012/2016
* 支持SQL Server版本 : SQL Server 2017, 2016, 2014, 2012, 2008, 2005

**SQL Backup Master 指南**

1. 从官网下载安装好 SQL Server Master，双击【运行程序】。

2. 创建数据库备份任务  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak-websoft9.png)

3. 选择数据库,并连接数据库
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak2-websoft9.png.png)

4. 选择需要备份的数据库,并进行设置  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak3-websoft9.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak4-websoft9.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak5-websoft9.png.png)

1. 设置计划任务  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak6-websoft9.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak7-websoft9.png)

2. 保存设置  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak8-websoft9.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak9-websoft9.png)

**备选方案：计划任务**

除了使用 SQL Backup Master 这个工具之外，也可以采用服务器系统的任务计划和备份数据库的存储过程来实现，参考：

* [How to schedule and automate backups of SQL Server databases in SQL Server Express](https://support.microsoft.com/en-us/kb/2019698)

* [创建 SQL Server Express自动备份数据库功能](http://shiyousan.com/post/635612483753095970)

* [在 Windows Server 2012中实现SQL SERVER EXPRESS自动备份数据库](http://shiyousan.com/post/635615192184858364)

## Troubleshoot{#troubleshoot}

In addition to the SQL Server Express issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### 应用程序无法连接 SQLServer数据库？

当您在安装应用程序的时候，首先保证数据库密码和用户名没有错，请确保登录界面服务器名称需要填写成您的`云服务器名称或(local)`。

服务器名称获取方法：“这台电脑”右键>“属性”中的“计算机名”。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver2008express/sqlserver-servnames-websoft9.png)

#### 备份失败：确保正确的介质...？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-backuperror001-websoft9.png)

问题原因：这个不是数据库自身的故障，而是备份的用法有问题。  
解决办法：去掉一个备份文件，每次备份在已有备份中覆盖即可

#### 系统盘满，导致无法启动？

由于 SQL Server Express 程序较大，一般系统盘只剩 10-20G 左右，加上系统运行以及数据存储，很容导致系统盘容量步骤。  

可以扩容系统盘，也可以[迁移](#migration)至数据盘。

## FAQ{#faq}

#### 什么是 SQL Server 企业管理器？

SQL Server Management Studio (SSMS) 是用于管理任何 SQL 基础结构的集成环境。 使用 SSMS，可以访问、配置、管理和开发 SQL Server、Azure SQL 数据库和 SQL 数据仓库的所有组件。 SSMS 在一个综合实用工具中汇集了大量图形工具和丰富的脚本编辑器，为各种技能水平的开发者和数据库管理员提供对 SQL Server 的访问权限。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/ssms.png)

本部署方案默认已经安装SQLServer企业管理器

#### SQL Server Express 有自动备份功能吗？

不包含，但本部署包提供了一个免费的自动备份软件，参考本文档的 [SQLServer自动备份](#autobackup)相关章节

#### 浏览器访问 Management Studio？

SQL Server Management Studio 托管一个 Microsoft Internet Explorer 版本。 此 Web 浏览器允许您浏览 URL，并查看 MSDN Library 帮助主题，而无需离开 SQL Server Management Studio。 您可以通过指向视图菜单上的 Web 浏览器，然后单击显示浏览器来访问 Web 浏览器。 参考：[https://docs.microsoft.com/en-us/sql/ssms/sql-server-management-studio-web-browser?view=sql-server-ver15](https://docs.microsoft.com/en-us/sql/ssms/sql-server-management-studio-web-browser?view=sql-server-ver15)

#### SQL Server 有哪些发行版？

以SQLServer2016为例，介绍 SQL Server的各个版本的差异

| 版本 | 定义                                                         |
| :-------------- | :----------------------------------------------------------- |
| Enterprise      | 作为高级版本，SQL Server Enterprise 版提供了全面的高端数据中心功能，性能极为快捷、虚拟化不受限制，还具有端到端的商业智能，可为关键任务工作负荷提供较高服务级别，支持最终用户访问深层数据。 |
| Standard        | SQL Server Standard 版提供了基本数据管理和商业智能数据库，使部门和小型组织能够顺利运行其应用程序并支持将常用开发工具用于内部部署和云部署，有助于以最少的 IT 资源获得高效的数据库管理。 |
| Web             | 对于 Web 主机托管服务提供商和 Web VAP 而言，SQL Server Web 版本是一项总拥有成本较低的选择，它可针对从小规模到大规模 Web 资产等内容提供可伸缩性、经济性和可管理性能力。 |
| 开发人员        | SQL Server Developer 版支持开发人员基于 SQL Server构建任意类型的应用程序。 它包括 Enterprise 版的所有功能，但有许可限制，只能用作开发和测试系统，而不能用作生产服务器。 SQL Server Developer 是构建 SQL Server 和测试应用程序的人员的理想之选。 |
| Express 版本    | Express 版本是入门级的免费数据库，是学习和构建桌面及小型服务器数据驱动应用程序的理想选择。 它是独立软件供应商、开发人员和热衷于构建客户端应用程序的人员的最佳选择。 如果您需要使用更高级的数据库功能，则可以将 SQL ServerExpress 无缝升级到其他更高端的 SQL Server版本。 SQL Server Express LocalDB 是 Express 的一种轻量级版本，它具备 Express 的所有可编程性功能，但在用户模式下运行，还具有零配置快速安装和必备组件要求较少的特点。 |

#### 可否关闭 SQLServer 的账号密码登录？

可以，关闭之后保留Windows身份登录模式即可

#### Express 版本如何升级企业版？

可以，参考官方提供的方案：[升级到 SQL Server 的其他版本（安装程序）](https://docs.microsoft.com/zh-cn/sql/database-engine/install-windows/upgrade-to-a-different-edition-of-sql-server-setup?view=sql-server-ver15)

#### 修改 SQL Server 默认的数据存储路径？

可以。SQL Server 企业管理器中：【属性】>【数据库设置】修改
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-3-websoft9.png)
