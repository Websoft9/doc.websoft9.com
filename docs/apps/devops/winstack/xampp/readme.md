---
sidebar_position: 1
slug: /xampp
tags:
  - XAMPP
  - DevOps
---

# 快速入门

XAMPP 是完全免费且易于安装的 Windows 集成环境，其中包含 MariaDB、PHP 和 Perl。XAMPP让 PHP 应用在 Windows 上安装变得非常容器。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xampp/xampp-ss-websoft9.png)



部署 Websoft9 提供的 XAMPP 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 XAMPP 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  XAMPP，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## XAMPP 初始化向导

### 详细步骤

远程桌面到服务器，点击服务器桌面的 XAMPP 图标，查看其状态。

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## XAMPP 部署网站

XAMPP环境中部署网站主要分为5个步骤：

**①**上传网站代码-&gt;**③**配置域名（根据情况而定）-&gt;**④**增加网站对应的数据库（根据程序要求而定）-&gt;**⑤**完成安装向导

XAMPP环境中只部署一个网站还是多个网站、有无域名这两种情况对应的部署操作细节略有不一样，下面分别说明：

### 部署第一个网站

如果您打算此服务器上只部署一个网站或应用，建议采用此方式：

1.  远程桌面到Windows服务器，将网站源文件拷贝到根目录
2.  如果没有可用域名，请直接通过 **http://公网IP**  的方式来访问应用
3.  如果有可用的域名，请完成 **《域名配置》** 后通过 **http://公网IP** 的方式来访问应用
4.  如果在安装向导过程中提示数据库无法自动创建，需要通过 http://ip/phpmyadmin 创建数据库

网站默认根目录为：C:\xampp\htdocs

### 部署第二个网站

1. 在 WWW 下新建一个网站目录，假设命名为“mysite2”
2. 将网站源文件上传到：*C:\xampp\htdocs\mysite2* 
3. 根据是否有域名，选择一种操作：
	* **有可用域名**，请将下面 **VirtualHost** 模板拷贝到 httpd-vhosts.conf 中，将ServerName , ServerAlias , DocumentRoot , ErrorLog,CusomLog , Directory 等参数相关值更换成你的实际内容。

    ```
    NameVirtualHost *:80

    <VirtualHost *:80>
    DocumentRoot "C:/xampp/htdocs/"
    ServerName localhost
    </VirtualHost>

    <VirtualHost *:80>
       ServerAdmin help@websoft9.com
        DocumentRoot "C:/xampp/htdocs/mysite2"
        ServerName www.mydomain.com
       ErrorLog "logs/www.mydomain.com-error.log"
        CustomLog "logs/www.mydomain.com-access.log" common

       <Directory "C:/xampp/htdocs/mysite2" >
        Options Indexes FollowSymLinks
      AllowOverride all
        Order allow,deny
         Allow from all
       </Directory>
    </VirtualHost>
    ```
	 * **无可用域名**，请将下面 **Alias** 模板拷贝到 httpd-vhosts.conf 中，将Alias，Directory等参数相关之更换成你的实际内容。
      ```
      Alias /mysite2 C:/xampp/htdocs\mysite2
      <Directory "C:/xampp/htdocs\mysite2">
	  Options Indexes FollowSymlinks
	  AllowOverride All
	  Require all granted
	  </Directory>
      ```
4. 保存 httpd-vhosts.conf，然后重启Apache服务。

5. 本地浏览器访问：http://域名 或 http://服务器公网IP/mysite2  就可以访问本次安装的网站

> 最后我们温故而知新，总结了WAMP部署网站步骤： 1.上传网站代码-&gt;2.绑定域名（非必要）3.新增站点配置或修改示例站点配置-&gt;4.增加网站对应的数据库（非必要）-&gt;5.进入安装向导


## 环境配置

### PHP 配置

通过修改C:\xampp\php\php.ini即可修改php配置：

*   何修改系统最大响应时间？将max_execution_time设置成你需要的值
*   如何修改上传文件大小限制？将post_max_size = 64M,upload_max_filesize = 64M设置成你需要的值


### Apache 配置

### 域名绑定

**XAMPP**环境下，请远程桌面到服务器，打开C:\xampp\apache\conf\extra\httpd-vhosts.conf文件，将其中的ServerName,ServerAlias的值替换成你的域名信息，重启Apache服务后生效。


#### 设置伪静态

Apache开启为静态的步骤如下：

1. 在 C:\xampp\apache\conf\httpd.conf 文件中查找以下语句 LoadModule rewrite_module modules/mod_rewrite.so，若前面有 # 号则需要将其去掉，使之支持 mod_rewrite 模块；
2. 再查找 AllowOverride 语句，若其后为 None 则将其更改为 ALL 使apache支持 .htaccess 文件,若已经是 ALL 则不需要变动；  
4. 重启 Apache，这样就可以在你的 PHP 项目根目录下建立 .htaccess 文件开启伪静态了。

> 一般情况下，如果您的网站是基于第三方开源网站（如：wordpress等）建立的，则网站目录下都会自带 .htaccess 文件，不需要另外自己设置。

#### 修改网站根目录

XAMPP 环境的根目录是可以被修改的，具体只需2个步骤：

1.  修改配置文件：C:\xampp\apache\conf\extra\httpd-vhosts.conf，将 DocumentRoot 和 Directory 的值修改成你网站的路径

2.   保存后，重启Apache服务


## 参数

**[通用参数表](../administrator/parameter)** 中可查看 Apache, MySQL 等 XAMPP 应用中包含的基础架构组件路径、版本、端口等参数。 

下面仅列出 XAMPP 本身的参数：

### 路径{#path}

| **项** | **路径或说明** |
| :--- | :--- |
| 默认根目录 | C:\xampp\htdocs |
| PHP配置文件 | C:\xampp\php\php.ini |
| Apache虚拟主机文件--根目录对应的文件 | C:\xampp\apache\conf\extra\httpd-vhosts.conf |
| 日志文件 | 请通过XAMPP面板查看 |
| Java安装目录 | C:\Program Files (x86)\Java |
| Tomcat安装目录 | C:\xampp\tomcat Java |
| Tomcat日志文件 | 请通过XAMPP面板查看 |
| Tomcat Manager App | 请通过http://ip/9panel的运维工具进入（登录账号:tomcat/tomcat） |
| Tomcat面板 | 管理地址:http://ip:8080/manager/html（登录账号:tomcat/tomcat） |
| MySQL数据目录 | C:\xampp\mysql |
| MySQL配置文件 | C:\xampp\mysql\my.ini |
| MySQL管理地址 | [http://服务器公网IP/phpmyadmin](http://服务器公网IP/phpmyadmin) |
| 9Panel访问地址 | [http://服务器公网IP/9panel](http://服务器公网IP/9panel) |

### 版本

界面中查看

### 服务

*服务随操作系统自动启动，如果手工修改配置参数后，需要重新启停服务。**

*   **方法一**：远程桌面点击XAMPP图标，然后点击需要启动或停止的服务 
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xampp/xampp-ss-websoft9.png)

*   **方法二**：打开xampp安装的文件夹，点击对应的服务启停exe/bat文件 
    MySQL start: \xampp\xampp_start.exe 
     MySQL stop: \xampp\xampp_stop.exe 
     Apache start: \xampp\apache_start.bat 
     Apache stop: \xampp\apache_stop.bat 
     MySQL start: \xampp\mysql_start.bat 
     MySQL stop: \xampp\mysql_stop.bat 
     Mercury Mailserver start: \xampp\mercury_start.bat 
     Mercury Mailserver stop: \xampp\mercury_stop.bat 
     FileZilla Server start: \xampp\filezilla_start.bat 
     FileZilla Server stop: \xampp\filezilla_stop.bat

### 命令行

无

### API

无