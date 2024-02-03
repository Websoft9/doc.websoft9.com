---
title: SQLServer
slug: /sqlserver
tags:
  - SQL Server
  - 云数据库
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

import Meta from './_include/sqlserver.md';

<Meta name="meta" />

### 申明{#license}

本文档中所涉及的 SQLServer 均为 Express 版本，可以免费使用或分发。详情参考官方：[许可条款](https://www.microsoft.com/zh-cn/download/details.aspx?id=29693)

产品 License 清单： 

* [license_Expr_2005.rtf](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/license/license_Expr_2005.rtf)
* [license_Expr_2008R2.rtf](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/license/license_Expr_2008R2.rtf)
* [license_Expr_2008.rtf](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/license/license_Expr_2008.rtf)
* [license_Expr_2012.rtf](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/license/license_Expr_2012.rtf)

Express版本与企业版相比，功能更少（例：[SQLServer 2016 各个版本功能对比](https://docs.microsoft.com/zh-cn/sql/sql-server/editions-and-components-of-sql-server-2016?view=sql-server-ver15#Cross-BoxScaleLimits)）。另外，它针对服务器有如下的限制：不超过1个处理器，不超过10G数据存储

## 入门指南{#guide}


### 初始化{#wizard}

Websoft9 控制台安装 SQLServer 后，通过【我的应用】进入它的编辑窗口，在**访问**标签页中获取登录地址和账号。  

<Tabs>
<TabItem value="linuxinit" label="Linux" default>

Linux环境下使用 CloudBeaver 来验证 SQL Server 数据库：

1. 使用本地电脑浏览器访问：*`http://域名:9090`* 或 *`http://服务器公网IP:9090`*, 进入初始化页面
   ![初始化 CloudBeaver](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-wizard001-websoft9.png)

2. 设置用户名和密码，然后点击【Next】进入下一步
   ![初始化 CloudBeaver](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-wizard002-websoft9.png)

3. 继续点击【Next】进入下一步，最后点击【FINISH】完成初始化
   ![初始化 CloudBeaver](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-wizard003-websoft9.png)

4. 连接【SQL SERVER】，管理数据库：点击右上角【Settings】图标，选择【Administration】>【Connection Management】，添加 SQL SERVER
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cloudbeaver/cloudbeaver-connection-websoft9.png)

5. 填写数据库基本信息（[不知道账号密码？](./user/credentials)），点击【Create】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/cloudbeaver-connsetting-websoft9.png)

6. 点击左上角 Cloud Beaver 图标，SQL Server 数据库连接成功，可以方便管理数据库
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cloudbeaver/sqlserver-main-websoft9.png)

</TabItem>
<TabItem value="wininit" label="Windows">

1. 使用本地电脑的 **远程桌面**工具，登录到服务器  
2. 打开 **SQLServer企业管理器**，通过：【服务器名称】>【浏览更多...】选择服务器，并以【Windows身份】登录数据库  

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-getsqlserver-websoft9.png)

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-getsqlserver2-websoft9.png)
   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-winlogin-websoft9.png)

3. [启用密码（开启 SQL Server 身份验证模式）](#enablepw)（可选）
4. [重启 SQL Server 服务](#service)，使配置生效。

</TabItem>
</Tabs>


### 获取服务器名称（ID）

使用 SQLServer 企业管理器 连接数据库时，除了填写 `.` 或 `(local)` 之外，也可以直接填写服务器名称（ID）。

这个 ID 获取的方式有两种：

* 从 **Windows 系统**中获取：【我的电脑】>【属性】，计算机名即我们所需的 ID

  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver2008express/sqlserver-servnames-websoft9.png)

2. 从 **SQLServer企业管理器**获取：【服务器名称】>【浏览更多...】选择服务器，并以【Windows身份】登录数据库  

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-getsqlserver-websoft9.png)

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-getsqlserver2-websoft9.png)



### 启用密码（SQL Server 身份验证模式）{#enablepw}

默认没有启用密码登录方式（SQL Server 身份验证模式），参考下面的步骤设置：

1. SQLServer 企业管理器中：通过【属性】>【安全性】>【服务器身份验证】，选择 **SQLServer 和 Windows 身份验证模式**  

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-winlogin-pw1-websoft9.png)
   
2. 启用 sa 账户，并设置密码：依次展开【安全性】、【登录名】，找到默认登录名【sa】，右键【属性】，在弹出的窗口中点击【状态】，将登录选项选择【已启用】，也可以在【常规】选项卡里设置你的登录密码，点击确认保存.  

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-winlogin-pw2-websoft9.png)

3. [重启 SQL Server 服务](#service)，使配置生效。


## 管理维护{#administrator}

### 开启远程访问{#remote}

通过本地电脑远程访问 SQLServer，需完成如下设置：  

#### SQLServer 服务端开启远程连接{#remotess}

本镜像默认完成了SQLServer远程访问的配置，但为了能够顺利访问，SQLServer所在的服务器还需完成如下两个设置：

1. 打开**SQLServer企业管理器**工具，在服务器【连接】属性中，勾选【允许远程连接到本服务器】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-remote1-websoft9.png)
   
2. 打开**SQL Server 配置管理器**工具，在网络配置中，启用【TCP/IP】协议
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-remote2-websoft9.png)

#### Windows 服务器设置防火墙和端口{#remotefirewall}
   
1. 在Windows服务器防火墙设置中开启远程访问：【控制面板】>【系统和安全】>【Windows防火墙】>【允许程序或功能通过Windows防火墙】  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver2014/sqlserver-firewall001-websoft9.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver2014/sqlserver-firewall002-websoft9.png)

2. 在云控制台中，开启服务器安全组的**1433端口**  

#### 客户端工具范例{#navicat}

设置完成上面的服务器之后，下面以Navicat为例来说明如何在本地电脑访问并管理SQLServer

1. [下载](http://www.navicat.com.cn/download)并安装Navicat

2. 在Windows服务器防火墙设置中开启远程访问（请见上一章）

3. 在Navicat->新建一个SQLServer连接，填写好连接参数
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver2008express/sqlserver2008-navicat-websoft9.png)

4.  点击【连接测试】，成功表明参数没有问题。

5.  点击【确认】后，进入数据库管理界面

### SQL Server 更新{#upgrade}

SQLServer更新只能是卸载旧版本，然后下载最新的安装包重新安装

### SQL Server 数据库迁移{#migration}

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


### SQL Server 手动备份{#backup}

通用的手动备份操作步骤如下：

1. 访问SQLServer企业管理器，在需要备份的数据库上点右键，选择任务->备份，弹出备份数据库窗口。 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-backup-websoft9.png)
2. 根据备份向导逐步完成备份工作

### SQL Server Express 自动备份{#autobackup}

SQL Server Express的数据库由于没有SQL Server Agent服务，所以也就不支持维护计划功能，自动备份数据库就成了一个十分麻烦的问题。

#### 引入 SQL Backup Master{#sqlbackupmaster}

经过研究，我们建议采用第三方工具 [SQL Backup Master](https://www.sqlbackupmaster.com/)  实现自动备份。SQL Backup Master 是一款免费可靠的 SQL Server 数据库备份工具，主要特性:

* 支持完整备份,差异备份,事务日志备份
* 简单强大的计划任务
* 内置邮件通知
* 支持备份到本地/网络文件夹/网络存储
* 支持备份到FTP/SFTP/FTPS服务器
* 支持备份到Dropbox，Google Drive，Box，Amazon S3，OneDrive和Azure
* 支持操作系统: Windows 10, 8, 7, Vista 和 Windows Server 2008/2012/2016
* 支持SQL Server版本 : SQL Server 2017, 2016, 2014, 2012, 2008, 2005


#### SQL Backup Master 指南

1. 从官网下载安装好 SQL Server Master，双击【运行程序】。

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
    
####  备选方案：计划任务{#backupschedule}

除了使用 SQL Backup Master 这个工具之外，也可以采用服务器系统的任务计划和备份数据库的存储过程来实现，参考：

* [How to schedule and automate backups of SQL Server databases in SQL Server Express](https://support.microsoft.com/en-us/kb/2019698)

* [创建 SQL Server Express自动备份数据库功能](http://shiyousan.com/post/635612483753095970)

* [在 Windows Server 2012中实现SQL SERVER EXPRESS自动备份数据库](http://shiyousan.com/post/635615192184858364)

## 参数

[SQL Server 技术文档](https://docs.microsoft.com/zh-cn/sql/sql-server)

#### 发行版

- Windows 服务器适用于： SQL Server Express 2005, 2008, 2012, 2014, 2016, 2017
- Linux 服务器适用于： SQL Server Express 2017 2019 2022

#### 路径{#path}

<Tabs>
<TabItem value="linuxpath" label="Linux" default>

SQL Server 安装目录： */data/apps/sqlserver*  
SQL Server 数据目录： */data/apps/sqlserver/data/mssql_data*  

</TabItem>
<TabItem value="winpath" label="Windows">

以SQL Server 2014为例，集成包中包括 SQL Server 2014 数据库引擎和 SQL Server Management Studio Express，具体包括：

* 操作系统： Windows Server系统
* 软件版本： SQL Server2014 R2 SP2 Express Edition,SQL Server Management Studio, Microsoft .Net Framework 4.6,IIS7
* 软件目录： C:\Program Files\Microsoft SQL Server
* 数据库引擎数据目录：C:\Program Files (x86)\Microsoft SQL Server\MSSQL12.MSSQLSERVER\MSSQL\DATA

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver2014/sqlserver2014-install-websoft9.png)

</TabItem>
</Tabs>

### 服务{#service}

<Tabs>
<TabItem value="linuxserver" label="Linux" default>
sudo docker start | stop | restart | stats mssql  
sudo docker start | stop | restart | stats cloudbeaver   
</TabItem>
<TabItem value="winserver" label="Windows">
##### 可视化界面管理

使用 SQL Server 身份验证登录数据库。打开**SQL Server 配置管理器**工具，重启 SQL Server 服务。  

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-config-websoft9.png)

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-restart-websoft9.png)
</TabItem>
</Tabs>

### 命令行与 API

也可以使用 cmd 工具，通过命令的方式启动或关闭数据库

*   快速启动命令：net start mssqlserver
*   关闭服务：net stop mssqlserver
*   SQL Server 管理器打开的命令是：ssms

详情参阅：[mssql-cli](https://docs.microsoft.com/en-us/sql/tools/mssql-cli)和[SQL Assessment API](https://docs.microsoft.com/en-us/sql/tools/sql-assessment-api/sql-assessment-api-overview?view=sql-server-ver15)

## 故障

#### 无法使用 SQLServer 密码登录？

为了安全考虑，本部署方案没有创建 SQLServer 的登录密码。参考：[启用密码](#enablepw)

#### SQLServer 服务启动失败？

请检查服务器名称是否正确：在【服务器名称】中通过【浏览更多...】选择正确的服务器

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

## 问答

#### 什么是 SQL Server 企业管理器？

SQL Server Management Studio (SSMS) 是用于管理任何 SQL 基础结构的集成环境。 使用 SSMS，可以访问、配置、管理和开发 SQL Server、Azure SQL 数据库和 SQL 数据仓库的所有组件。 SSMS 在一个综合实用工具中汇集了大量图形工具和丰富的脚本编辑器，为各种技能水平的开发者和数据库管理员提供对 SQL Server 的访问权限。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/ssms.png)

本部署方案默认已经安装SQLServer企业管理器


#### SQL Server Express 有自动备份功能吗？

不包含，但本部署包提供了一个免费的自动备份软件，参考本文档的 [SQLServer自动备份](#autobackup)相关章节

#### 浏览器访问 Management Studio？

SQL Server Management Studio 托管一个 Microsoft Internet Explorer 版本。 此 Web 浏览器允许您浏览 URL，并查看 MSDN Library 帮助主题，而无需离开 SQL Server Management Studio。 您可以通过指向视图菜单上的 Web 浏览器，然后单击显示浏览器来访问 Web 浏览器。 参考：https://docs.microsoft.com/en-us/sql/ssms/sql-server-management-studio-web-browser?view=sql-server-ver15

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
https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-3-websoft9.png