---
sidebar_position: 2
slug: /sqlserver/admin
tags:
  - SQL Server
  - Cloude Native Database
---

# 维护参考

## 系统参数

SQLServer 预装包包含 SQLServer 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### SQLServer

以SQL Server 2014为例，集成包中包括 SQL Server 2014 数据库引擎和 SQL Server Management Studio Express，具体包括：

* 操作系统： Windows Server系统
* 软件版本： SQL Server2014 R2 SP2 Express Edition,SQL Server Management Studio, Microsoft .Net Framework 4.6,IIS7
* 软件目录： C:\Program Files\Microsoft SQL Server
* 数据库引擎数据目录：C:\Program Files (x86)\Microsoft SQL Server\MSSQL12.MSSQLSERVER\MSSQL\DATA

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver2014/sqlserver2014-install-websoft9.png)

#### 其他

除了 SQLServer Management Studio 之外，目前没有安装其他核心组件

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

本环境可能需要开启的端口如下：

| 类型 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 80/443 | 通过 HTTP/HTTPS 访问网站 | 可选 |
| TCP | 1433 | 远程访问 SQLServer | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本请登录云服务器查看

### 服务

使用由Websoft9提供的 SQLServer 部署方案，可能需要用到的服务如下：

#### SQLServer

进入Windows的系统管理管理，将mssqlserver服务设置为自动启动或手动启动。参考下图：

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver2008express/sqlserver-services-websoft9.png)

也可以使用cmd工具，通过命令的方式启动或关闭数据库

*   快速启动命令：net start mssqlserver
*   关闭服务：net stop mssqlserver
*   SQL Server 管理器打开的命令是：ssms

#### IIS

## 备份

### 全局自动备份

所有的云平台都提供了全局自动备份功能，基本原理是基于**磁盘快照**：快照是针对于服务器的磁盘来说的，它可以记录磁盘在指定时间点的数据，将其全部备份起来，并可以实现一键恢复。

```
- 备份范围: 将操作系统、运行环境、数据库和应用程序
- 备份效果: 非常好
- 备份频率: 按小时、天、周备份均可
- 恢复方式: 云平台一键恢复
- 技能要求：非常容易
- 自动化：设置策略后全自动备份
```

不同云平台的自动备份方案有一定的差异，详情参考 [云平台备份方案](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

### 程序手工备份

程序手工本地备份是通过**下载应用程序源码和导出数据库文件**实现最小化的备份方案。

下面以列表的方式介绍这种备份：
```
- 备份范围: 数据库和应用程序
- 备份效果: 一般
- 备份频率: 一周最低1次，备份保留30天
- 恢复方式: 重新导入
- 技能要求：非常容易
- 自动化：无
```
通用的手动备份操作步骤如下：

1. 访问SQLServer企业管理器，在需要备份的数据库上点右键，选择任务->备份，弹出备份数据库窗口。 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-backup-websoft9.png)
2. 根据备份向导逐步完成备份工作
通用的手动备份操作步骤如下：

1. 访问SQLServer企业管理器，在需要备份的数据库上点右键，选择任务->备份，弹出备份数据库窗口。 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-backup-websoft9.png)
2. 根据备份向导逐步完成备份工作

### SQLServer Express 自动备份

SQL Server Express的数据库由于没有SQL Server Agent服务，所以也就不支持维护计划功能，自动备份数据库就成了一个十分麻烦的问题。

#### 如何实现SQLServer Express自动备份？

经过研究，我们建议采用第三方工具 [SQL Backup Master](https://www.sqlbackupmaster.com/)  实现自动备份。SQL Backup Master 是一款免费可靠的 SQL Server 数据库备份工具，主要特性:

* 支持完整备份,差异备份,事务日志备份
* 简单强大的计划任务
* 内置邮件通知
* 支持备份到本地/网络文件夹/网络存储
* 支持备份到FTP/SFTP/FTPS服务器
* 支持备份到Dropbox，Google Drive，Box，Amazon S3，OneDrive和Azure
* 支持操作系统: Windows 10, 8, 7, Vista 和 Windows Server 2008/2012/2016
* 支持SQL Server版本 : SQL Server 2017, 2016, 2014, 2012, 2008, 2005


#### SQL Backup Master使用教程

1. 从官网下载安装好 SQL Server Master ,双击运行程序.
2. 创建数据库备份任务
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak-websoft9.png)
3. 选择数据库,并连接数据库 
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak2-websoft9.png.png)
4. 选择需要备份的数据库,并进行设置
	![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak3-websoft9.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak4-websoft9.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak5-websoft9.png.png)
 5. 设置计划任务
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak6-websoft9.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak7-websoft9.png)
    
 6. 保存设置
 	![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak8-websoft9.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-bak9-websoft9.png)
    
####  备选方案

除了使用SQL Backup Master这个工具之外，也可以采用服务器系统的任务计划和备份数据库的存储过程来实现，参考下面三篇文章：

* [How to schedule and automate backups of SQL Server databases in SQL Server Express](https://support.microsoft.com/en-us/kb/2019698)
* [创建 SQL Server Express自动备份数据库功能](http://shiyousan.com/post/635612483753095970)
* [在windows server 2012中实现SQL SERVER EXPRESS自动备份数据库](http://shiyousan.com/post/635615192184858364)


## 恢复

## 升级

SQLServer 完整的更新升级包括：系统级更新（操作系统和运行环境）和 SQLServer 程序升级两种类型

### Windows 更新

Windows服务器的更新与本地电脑类似，手动找到更新管理程序，设置自动下载自动更新即可。

### SQLServer更新

SQLServer更新只能是卸载旧版本，然后下载最新的安装包重新安装


## 故障处理

此处收集使用 SQLServer 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 应用程序无法连接SQLServer数据库？

当您在安装应用程序的时候，首先保证数据库密码和用户名没有错，请确保登录界面服务器名称需要填写成您的`云服务器名称或(local)`。

服务器名称获取方法：“这台电脑”右键>“属性”中的“计算机名”。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver2008express/sqlserver-servnames-websoft9.png)

#### 错误：媒体集有 2 个媒体簇，但只提供了 1 个？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-backuperror001-websoft9.png)

问题原因：这个不是数据库自身的故障，而是备份的用法有问题。  
解决办法：去掉一个备份文件，每次备份在已有备份中覆盖即可

## 常见问题

#### SQLServer Express 是否包含自动备份功能？

不包含，但本部署包提供了一个免费的自动备份软件，参考本文档的 [SQLServer自动备份](/zh/solution-backup.md#sqlserver-express-自动备份)相关章节

#### SQL Server Management Studio 是否支持浏览器访问？

SQL Server Management Studio 托管一个 Microsoft Internet Explorer 版本。 此 Web 浏览器允许您浏览 URL，并查看 MSDN Library 帮助主题，而无需离开 SQL Server Management Studio。 您可以通过指向视图菜单上的 Web 浏览器，然后单击显示浏览器来访问 Web 浏览器。 参考：https://docs.microsoft.com/en-us/sql/ssms/sql-server-management-studio-web-browser?view=sql-server-ver15

#### SQLServer各个发行版有什么功能区别？

以SQLServer2016为例，介绍 SQL Server的各个版本的差异

| 版本 | 定义                                                         |
| :-------------- | :----------------------------------------------------------- |
| Enterprise      | 作为高级版本，SQL Server Enterprise 版提供了全面的高端数据中心功能，性能极为快捷、虚拟化不受限制，还具有端到端的商业智能，可为关键任务工作负荷提供较高服务级别，支持最终用户访问深层数据。 |
| Standard        | SQL Server Standard 版提供了基本数据管理和商业智能数据库，使部门和小型组织能够顺利运行其应用程序并支持将常用开发工具用于内部部署和云部署，有助于以最少的 IT 资源获得高效的数据库管理。 |
| Web             | 对于 Web 主机托管服务提供商和 Web VAP 而言，SQL Server Web 版本是一项总拥有成本较低的选择，它可针对从小规模到大规模 Web 资产等内容提供可伸缩性、经济性和可管理性能力。 |
| 开发人员        | SQL Server Developer 版支持开发人员基于 SQL Server构建任意类型的应用程序。 它包括 Enterprise 版的所有功能，但有许可限制，只能用作开发和测试系统，而不能用作生产服务器。 SQL Server Developer 是构建 SQL Server 和测试应用程序的人员的理想之选。 |
| Express 版本    | Express 版本是入门级的免费数据库，是学习和构建桌面及小型服务器数据驱动应用程序的理想选择。 它是独立软件供应商、开发人员和热衷于构建客户端应用程序的人员的最佳选择。 如果您需要使用更高级的数据库功能，则可以将 SQL ServerExpress 无缝升级到其他更高端的 SQL Server版本。 SQL Server Express LocalDB 是 Express 的一种轻量级版本，它具备 Express 的所有可编程性功能，但在用户模式下运行，还具有零配置快速安装和必备组件要求较少的特点。 |

#### 是否可以关闭SQLServer的账号密码登录模式？

可以，关闭之后保留Windows身份登录模式即可

#### SQLServer Express 版本是否可以升级到 SQLServer 企业版？

可以，参考官方提供的方案：[升级到 SQL Server 的其他版本（安装程序）](https://docs.microsoft.com/zh-cn/sql/database-engine/install-windows/upgrade-to-a-different-edition-of-sql-server-setup?view=sql-server-ver15)

#### 是否可以修改SQLServer的源码路径？

不可以