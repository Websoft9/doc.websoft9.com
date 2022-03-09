---
sidebar_position: 1
slug: /sqlserver
tags:
  - SQL Server
  - Cloude Native Database
---

# 快速入门

[SQL Server Express](https://www.sqlserver.com) 是 Microsoft 官方的免费版 SQLServer 数据库。具有易于部署以及可以快速设计原型的特点，您可以无偿获取并可以随应用程序免费再分发。如果需要更多的高级数据库功能，可将SQL Server Express 无缝升级到更复杂的 SQL Server 版本。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/microsoft-sql-server-express.png)

## 适用性

SQL Server Express 2005, 2008, 2012, 2014, 2016, 2017

## 版权与限制

本文档中所涉及的 SQLServer 均为 Express 版本，可以免费使用或分发。详情参考官方：[许可条款](https://www.microsoft.com/zh-cn/download/details.aspx?id=29693)

产品 License 清单： 

* [license_Expr_2005.rtf](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/license/license_Expr_2005.rtf)
* [license_Expr_2008R2.rtf](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/license/license_Expr_2008R2.rtf)
* [license_Expr_2008.rtf](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/license/license_Expr_2008.rtf)
* [license_Expr_2012.rtf](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/license/license_Expr_2012.rtf)

Express版本与企业版相比，功能更少（例：[SQLServer 2016 各个版本功能对比](https://docs.microsoft.com/zh-cn/sql/sql-server/editions-and-components-of-sql-server-2016?view=sql-server-ver15#Cross-BoxScaleLimits)）。另外，它针对服务器有如下的限制：不超过1个处理器，不超过10G数据存储


在云服务器上部署 SQLServer 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:1433** 端口是否开启
3. 若想用域名访问 SQLServer，请先到 **域名控制台** 完成一个域名解析

## 账号密码

使用SQLServer，可能会用到的几组账号密码如下：

### SQLServer

管理员账号: `sa`  
管理员密码: 默认没有启用密码登录方式，参考下面的步骤设置密码  

1. 打开桌面上的 **SQLServer企业管理器**工具，以【Windows】身份登录数据库
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-winlogin-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-winlogin-pw1-websoft9.png)

2. 依次展开【安全性】、【登录名】，找到默认登录名【sa】，右键【属性】，在弹出的窗口中点击【状态】，将登录选项选择【已启用】，也可以在【常规】选项卡里设置你的登录密码，点击确认保存.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-winlogin-pw2-websoft9.png)


## SQLServer 安装向导

1. 使用本地电脑的 **远程桌面**工具，登录到服务器
2. 打开桌面上的 **SQLServer企业管理器**工具，在【服务器名称】中通过【浏览更多...】选择服务器，并以【Windows身份】登录数据库
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-getsqlserver-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-getsqlserver2-websoft9.png)
   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-winlogin-websoft9.png)
   
3. 开启 SQL Server 账号登录模式，用于远程访问（服务器需开通1433端口）
   - 在服务器的安全性中开启SQL Server 服务器身份验证模式：右键单击服务器，通过【属性】-【安全性】，选择服务器身份验证模式
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-winlogin-pw1-websoft9.png)
   
   - 启用 sa 账户，并设置密码：依次展开【安全性】、【登录名】，找到默认登录名【sa】，右键【属性】，在弹出的窗口中点击【状态】，将登录选项选择【已启用】，也可以在【常规】选项卡里设置你的登录密码，点击确认保存.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-winlogin-pw2-websoft9.png)
 
4. 重启 SQL Server 服务，使配置生效，使用 SQL Server 身份验证登录数据库。打开**SQL Server 配置管理器**工具，重启 SQL Server 服务。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-config-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-restart-websoft9.png)

> 需要了解更多 SQLServer 的使用，请参考官方文档：[SQL Server 技术文档](https://docs.microsoft.com/zh-cn/sql/sql-server)


## 常用操作

### SQLServer 远程访问

除了远程桌面登录到服务器访问SQLServer之外，也可以通过本地访问SQLServer。  

但需要完成如下两个步骤：

#### 服务器端：开启远程连接

本镜像默认完成了SQLServer远程访问的配置，但为了能够顺利访问，SQLServer所在的服务器还需完成如下两个设置：

1. 检查SQLServer数据库服务器中是否允许远程链接  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-enableremote001-websoft9.jpg)
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-enableremote002-websoft9.png)

2. 为SQLServer服务器（MSSQLServer）配置相应协议。  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-enableremote003-websoft9.png)
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-enableremote004-websoft9.png)
   
3. 在Windows服务器防火墙设置中开启远程访问：【控制面板】>【系统和安全】>【Windows防火墙】>【允许程序或功能通过Windows防火墙】  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver2014/sqlserver-firewall001-websoft9.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver2014/sqlserver-firewall002-websoft9.png)

4. 在云控制台中，开启服务器安全组的**1433端口**  

#### 客户端：工具设置

设置完成上面的服务器之后，下面以Navicat为例来说明如何在本地电脑访问并管理SQLServer

1. [下载](http://www.navicat.com.cn/download)并安装Navicat

2. 在Windows服务器防火墙设置中开启远程访问（请见上一章）

3. 在Navicat->新建一个SQLServer连接，填写好连接参数（[不知道账号密码](/zh/stack-account.md)）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver2008express/sqlserver2008-navicat-websoft9.png)

   > 端口1433不能更改，另外请确保云服务器控制台上的安全组打开了TCP:1433）

4.  点击【连接测试】，成功表明参数没有问题。

5.  点击【确认】后，进入数据库管理界面

### SQL Server 企业管理器

SQL Server Management Studio (SSMS) 是用于管理任何 SQL 基础结构的集成环境。 使用 SSMS，可以访问、配置、管理和开发 SQL Server、Azure SQL 数据库和 SQL 数据仓库的所有组件。 SSMS 在一个综合实用工具中汇集了大量图形工具和丰富的脚本编辑器，为各种技能水平的开发者和数据库管理员提供对 SQL Server 的访问权限。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/ssms.png)

本部署方案默认已经安装SQLServer企业管理器

### SQLServer 迁移

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

### 使用Reporting Services

待续...

#### 异常处理

#### 本部署方案数据库默认密码是多少？

为了安全考虑，本部署方案没有创建SQLServer的登录密码。请参考安装向导，手动开启【SQL Server账号登录】

#### SQLServer 服务启动失败？

请检查服务器名称是否正确：在【服务器名称】中通过【浏览更多...】选择正确的服务器

#### SQLServer 远程登录失败（服务器需开通1433端口）

1. 打开**SQLServer企业管理器**工具，在服务器【连接】属性中，勾选【允许远程连接到本服务器】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-remote1-websoft9.png)
   
2. 打开**SQL Server 配置管理器**工具，在网络配置中，启用【TCP/IP】协议
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-remote2-websoft9.png)
   
3. 打开**SQL Server 配置管理器**工具，重启 SQL Server 服务。
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver/sqlserver-restart-websoft9.png)
