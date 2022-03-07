---
sidebar_position: 1
slug: /wampserver
tags:
  - WampServer
  - PHP
  - Apache
  - Windows
---

# 快速入门

[WampServer](http://www.wampserver.com/?lang=en) 是一个 Windows 环境下的 Apache+PHP+MySQL/MariaDB 组合，由法国人维护的开源项目，拥有简单的图形和菜单安装和配置环境，支持 PHP 多版本切换。支持22种语言，其中包括简体中文和繁体中文。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-phpini-websoft9.png)


在云服务器上部署 WampServer 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 WampServer，请先到 **域名控制台** 完成一个域名解析


## 账号密码

使用WampServer，可能会用到的几组账号密码如下：

### MySQL

  **管理员用户名**：*root*   
  **密码存储路径**：*C:/credentials/password.txt*     
  **获取方式**： 远程桌面到服务器，打开此文件即可   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-pwfolder-websoft9.png)

  **注意**：若服务器上不存在 password.txt 文件，那么数据库密码是 `123456`。此时务必修改为强密码，类似于：f@N7eUUm25xAjP!$ ，这样有助于提高数据库的安全性，减少数据库密码被破解的风险。

> 需要登录MySQL，请参考 [MySQL可视化管理](#mysql-数据管理)


## WAMP 安装向导

1. 使用本地 Chrome 或 Firefox 浏览器访问网址：*http://Internet IP/9panel*, 就进入引导页面9Panel
   ![9panel](https://libs.websoft9.com/Websoft9/DocsPicture/en/wampserver/wampserver-9panelui.png)

2. 通过 9Panel 可以快速了解镜像基本情况，管理数据库，找到帮助文档，寻求人工支持

## 远程桌面到服务器

远程桌面登录到 Windows 服务器，查看 WampServer 是否正常运行（图标为绿色），点击【重新启动所有服务】测试可用性。如果桌面右下角没有 WampServer 图标，请重启服务器后再查看。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-clicks-websoft9.png)

## 登录数据库

WAMP 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，[登录MySQL](#mysql-数据管理) 管理用户和数据库

![9panel](https://libs.websoft9.com/Websoft9/DocsPicture/zh/9panel/9panel-mysql-websoft9.png)

## 安装网站

WAMP 可以用来部署多个 PHP 网站，[马上开始吧](#安装网站)


## 常用操作

### 安装网站

在 WampServer 环境上安装一个网站，也就是我们常说的增加一个虚拟主机。

宏观上看，只需两个步骤：**上传网站代码** + [**虚拟机主机配置文件（httpd-vhosts.conf）**](/维护参考.md#apache) **中增加 VirtualHost 配置段**

> VirtualHost 又称之为虚拟主机配置段，每个网站必定在 httpd-vhosts.conf 中对应唯一的 VirtualHost。

#### 准备

安装网站之前，请了解如下几个要点，做好准备工作

*  虚拟机主机配置文件：*C:\websoft9\wampserver\bin\apache\apache2.4.x\conf\extra\httpd-vhosts.conf* 
*  连接工具：使用 Windows自带的远程桌面工具 连接服务器
*  域名：若需要使用域名，请确保备案后的域名成功解析到服务器IP
*  数据库：网站安装向导过程中可能需要使用数据库，请使用 [phpMyAdmin 管理数据库](#mysql-数据管理)

有一个宏观认知之后，我们开始部署网站

#### 安装第一个网站

下面通过**替换示例网站**（WampServer 默认存在一个示例网站）的方式来教你安装你的第一个网站：

1. 使用 远程桌面工具 连接服务器

2. 删除示例网站 *C:\websoft9\wampserver\www\www.example.com* 下的所有文件（保留目录）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-exadr-websoft9.png)

3. 将本地电脑上的网站源码上传到示例目录下

4. 修改 *httpd-vhosts.conf* 中已有 VirtualHost 配置段（[修改参考](/zh/solution-deployment.md#virtualhost)），实现绑定域名、修改网站目录名称等操作。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-mddfvhost-websoft9.png)
   ::: warning
   如果不绑定域名、不修改网站目录名称，请跳过步骤4和5
   :::
5. 保存 httpd-vhosts.conf，然后 [重启所有服务](/zh/admin-services.md)

6. 本地浏览器访问：*http://域名* 或 *http://服务器公网IP* 即可访问您的网站

## 安装第二个网站

从安装第二个网站开始，需要在*httpd-vhosts.conf* 中增加对应的虚拟主机配置段，具体如下

1. 使用 远程桌面 连接服务器，在 C:\websoft9\wampserver\www 下新建一个网站目录，假设命令为“mysite2”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-addmysite2-websoft9.png)

2. 将本地网站源文件上传到：*C:\websoft9\wampserver\www\mysite2* 

3. 编辑 httpd-vhosts.conf 文件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-addmorevhostconfig-websoft9.png)

    根据是否通过域名访问，选择下面操作之一：

     * **有域名，通过 http://域名 访问网站**
     
     请将下面 VirtualHost 模板拷贝到 httpd-vhosts.conf 中，并修改其中的ServerName, DocumentRoot, ErrorLog, CusomLog, Directory等项的值

       ```
       <VirtualHost *:80>
       ServerName www.mydomain.com
       # ServerAlias other.mydomain.com
       DocumentRoot "C:\websoft9\wampserver\www\mysite2"
       ErrorLog "logs\mydomain.com_error_apache.log"
       CustomLog "logs\mydomain.com_error_apache.log" common
       <Directory "C:\websoft9\wampserver\www\mysite2">
       Options Indexes FollowSymlinks
       AllowOverride All
       Require all granted
       </Directory>
       </VirtualHost>
        ```

     * **没有域名，通过 http://IP/mysite2 访问网站**  
    
     请将下面 Alias 模板拷贝到 httpd-vhosts.conf 中，并修改其中的 /path, Directory等项的值

      ```
      Alias /sitename C:\websoft9\wampserver\www\mysite2
      <Directory "C:\websoft9\wampserver\www\mysite2">
	     Options Indexes FollowSymlinks
	     AllowOverride All
	     Require all granted
	    </Directory>
      ```
4. 保存 httpd-vhosts.conf，然后 [重启所有服务](/zh/admin-services.md)
5. 根据有无域名，本地浏览器访问：*http://域名* 或 *http://服务器公网IP/sitename*  访问你的网站。


#### 安装第 N 个网站

安装第n个网站与安装第二个网站的操作步骤一模一样

最后我们温故而知新，总结 WampServer 安装网站步骤： 

1. 上传网站代码
2. 绑定域名（非必要）
3. 新增站点配置或修改示例站点配置
4. 增加网站对应的数据库（非必要）
5. 进入安装向导

#### VirtualHost

VirtualHost 改动务必准确无误，任何错误的修改都会导致服务器上所有的网站不可访问

|  VirtualHost 项  |  作用说明  |  必要性 |
| --- | --- | --- |
|  ServerName  |  主域名   |  必须填写 |
|  ServerAlias  |   辅域名 |  可以不填或删除 |
|  DocumentRoot |  网站存放目录，同下  | 务必准确无误 |
|  Directory |  网站存放目录，同上  |  务必准确无误 |
|  ErrorLog  | 错误日志路径，系统会根据定义的路径产生相关日志文件   |  可以不填或删除 |
|  CustomLog  | 访问日志路径，系统会根据定义的路径产生相关日志文件  |  可以不填或删除 |

#### 常见问题

##### 找不到示例网站？

历史版本中历史网站路径与文档中描述有差异  
历史版本的示例网站路径为：C:\websoft9\wampstack\www

##### 修改 httpd-vhosts.conf 文件之后，Apache 服务无法启动？

一般是 VirtualHost 中虚拟主机的目录位置不正确导致

##### 新增网站不可访问，且导致其他网站都不可访问？

一般是 VirtualHost 中虚拟主机的目录位置不正确导致 Apache 无法启动

##### 打开新增的网站，显示404错误？

一般是网站目录下没有 index.php 或 index.html 等默认首页导致

##### 新增的网站，显示 500 Internal Server Error？

程序代码错误，需要查看程序的日志文件

##### 总是显示9Panel？

请删除示例中的index文件，并清空浏览器缓存

### 迁移网站

迁移网站就是将**网站数据**移动到新的位置，然后通过配置，保证移动后可正常访问。

迁移是需要谨慎对待的操作，迁移之前需要清楚的明白如下要点：

- 被移动的网站数据对象：网站源码文件和数据库数据文件  
- 目的地位置：服务器目录之间转移（本地）和转移到外部服务器（外部）

被迁移对象和目的地位置的组合，形成了多种多样的迁移场景。下面详细说明最常见的迁移场景：

#### 迁移网站源码（本地）

以将原目录 *C:\websoft9\wampserver* 下的 **www** 迁移到 *d:\www* 目录下为例，具体步骤如下：

1. 使用 **远程桌面** 连接服务器，停止 [Apache 服务](/维护参考.md#apache)
2. 将 ***www*** 文件夹整体拷贝到目标位置 *d:\www*
3. 修改 [虚拟主机配置文件](/维护参考.md#apache) 中 mysite1 这个网站对应的 VirtualHost 配置段 DocumentRoot, Directory 项的值，并保存它

   原地址：C:\websoft9\wampserver\www  
   目标地址：d:\www

4. 重启 [Apache 服务](/维护参考.md#apache-1)
5. 测试迁移后的结果，成功后可以删除原来的 *www* 文件夹

#### 迁移数据库文件（本地）

没有特殊情况，我们不建议迁移数据库文件到服务器上另外一个目录，毕竟主流的云厂商磁盘均可扩容。

1. 停止 MySQL 服务
2. 将 *C:/websoft9/wampserver/bin/mysql/data* 下所有文件拷贝到新目录，例如：D:\data
3. 修改 [数据库配置文件](/维护参考.md#mysql) 文件中数据存放的路径，范例参考：
	~~~
    datadir="C:/websoft9/wampserver/bin/mysql/data"
    log-error="C:/websoft9/wampserver/bin/mysql/data/mysqld.log"
        
    修改为：
    
    datadir="D:\data"
    log-error="D:\data\mysqld.log"
    ~~~
 4. 重启 MySQL 服务

#### 迁移到外部服务器

网站从一台服务器（原服务器）迁移到另外一台服务器（目的服务器）是一个系统工程，基本步骤如下：

1. 通过云控制台，在目的服务器上[部署](/zh/stack-deployment.md)参数一致的 WAMP 镜像。
2. 将原服务器上的网站源文件**转移到**目的服务器。
3. 通过 phpMyAdmin **导出**原服务器上的数据库，然后在目的服务器上**导入**数据库。
4. 把原服务器上的 [虚拟主机配置文件](/维护参考.mdl#apache) 配置文件内容，完整拷贝到目的服务器的 [虚拟主机配置文件](/维护参考.md#apache) 中，保存之。
5. 重启 Apache 服务。
6. 解析域名到目的服务器，等待域名解析生效。
7. 通过域名访问网站，测试可用性。
8. 正式发布。

如果一台服务器上有多个网站需要迁移，建议逐个迁移

### 域名绑定

当服务器上只有一个网站时，不做域名绑定也可以访问网站。但从安全和维护考量，**域名绑定**不可省却。

以示例网站为例，域名绑定操作步骤如下：

1. 确保域名解析已经生效  
2. 使用 **远程桌面工具** 登录云服务器
3. 修改 [Apache虚拟机主机配置文件](/维护参考.md#apache)，将其中的 **ServerName** 项的值修改为你的域名
   ```text
   <VirtualHost *:80>
   ServerName www.mydomain.com # 此处修改为你的域名
   DocumentRoot "C:\wwwroot\mysite2"
   ...
   ```
4. 保存配置文件，重启 [Apache 服务](/维护参考.md#apache-1)


### 使用 Apache 伪静态

使用 Apache 伪静态有三个步骤：

1.  打开 [Apache 主配置文件](/zh/stack-components.md#apache)，检查 Rewrite 模块是否启用（WAMP 环境默认已经开启 Rewirte）
```
 LoadModule rewrite_module modules/mod_rewrite.so #若前面有"#"号则需要将其去掉，使之支持 mod_rewrite 模块；
```
2.  保证 [Apache 虚拟主机配置文件](/zh/stack-components.md#apache)中 VirtualHost 配置段中增加 AllowOverride All
3.  给需要使用伪静态的网站的根目录中增加 `.htaccess` 文件，并在其中配置伪静态规则

### 重置 MySQL 密码

重置 MySQL 密码的原理主要分为三个部分

1. 将 MySQL 更改为临时免密模式
2. 修改密码
3. 将 MySQL 恢复为正常模式

#### 将 MySQL 更改为临时免密模式

1. 远程连接到服务器，打开 [MySQL 配置文件](/zh/stack-components.html#mysql)，在 [mysqld] 配置项中增加一行 `skip-grant-tables`，保存
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-addconfigtomysqld-websoft9.png)

2. 重启 MySQL 服务
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-managerservice-websoft9.png)

#### 修改密码 

- 进入到 MySQL 下的 bin 目录，按住键盘 `Shift`键的同时点击鼠标右键，
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-opencmdinbin-websoft9.png)

- 进入命令窗口，依次运行下列命令：
   ```
    mysql -uroot
    use mysql;
    update user set authentication_string=password("12345678") where user="root";
    flush privileges;
    exit
   ```

#### 将 MySQL 恢复为正常模式

1. 打开 [MySQL 配置文件](/zh/stack-components.html#mysql)，在 [mysqld] 配置项中删除 `skip-grant-tables` 这一行
2. 再次重启 MySQL 服务，此时密码已被重置为 `12345678`

### 修改 PHP 配置文件（php.ini）

在使用PHP网站的时候，你可能会碰到需要修改：上传文件大小、内存限制等参数。这个时候，就需要通过修改 `php.ini` 来实现

1. 远程桌面登录到服务器，打开 [`php.ini`](/维护参考.md#php) 文件 
```
# File upload limit
post_max_size = 16M
upload_max_filesize = 16M

# Max Execution Time
max_execution_time = 90

# Memory Limit
memory_limit – Minimum: 256M
```
2. 修改所需的参数，保存并重启 [Apache 服务](/维护参考.md#apache-1)


### PHP 扩展

在 WAMP 上安装和管理 PHP 扩展的通用步骤如下：

1. 下载正确的 PHP 扩展文件（[注意事项](https://www.php.net/manual/zh/install.pecl.windows.php)），上传到服务器的 [PHP 扩展目录](/维护参考.md#php)

2. 通过修改 PHP 配置文件设置，开启或关闭扩展
   ```
   extension=php_bz2.dll
   ;extension=php_com_dotnet.dll
   ```

不同的 PHP 扩展安装有一定的差异，具体以扩展提供的文档为准

### 安装 Composer

WAMP 镜像中安装 composer 的方法步骤如下：

1. 进入到 PHP 目录，按住 shift + 鼠标右键，选择“在此处打开命令行窗口”；
2. 输入 php -r "readfile('https://getcomposer.org/installer');" | php 安装 composer；
3. 在该目录下新建 composer.bat 文件，并编辑输入：```@php "%~dp0composer.phar" %*```；
4. 将 PHP 所在目录路径添加到环境变量中，添加方法参考：[Windows系统如何设置添加环境变量？](https://support.websoft9.com/docs/windows/solution-environmentvar.html)
5. 至此，composer 安装完毕。

### 修改网站根目录

将网站根目录设置到D盘或不喜欢现在根目录的位置，就需要修改网站默认根目录。  

WAMP 环境的根目录是可以被修改的，具体只需2个步骤：

1. 修改[虚拟主机配置文件](/维护参考.md#apache)，将网站对应的`<VirtualHost *:80>...</VirtualHost>` 中 DocumentRoot 和 Directory 的值修改成你网站的路径
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-mddfvhost-websoft9.png)
   
2. 保存后，重启 Apache 服务 

### 设置Apache并发连接数

1. 通过取消 http.conf 文件中 `Include conf/extra/httpd-mpm.conf`的注释，启用 MPM
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-enablempm-websoft9.png)
2. 找到 WinNT MPM 断路，修改ThreadsPerChild的值为更大，比如：15000
   ```
   # WinNT MPM
   # ThreadsPerChild: constant number of worker threads in the server process
   # MaxConnectionsPerChild: maximum number of connections a server process serves
   <IfModule mpm_winnt_module>
       ThreadsPerChild        150
       MaxConnectionsPerChild   0
   </IfModule>
   ```
**原理说明**：WinNT MPM 采用的是单一进程多线程模式，即只有唯一一个进程通过创建多线程处理请求。如果每个客户的业务涉及数十个请求，那么默认的 150 个线程就无法应对并发，因此修改成为比较大的值。

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

WAMP预装包，已安装Web服务器 OpenSSL 模块，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改 Apache 任何文件

#### 设置参考

如果你已经申请了商业证书，只需几步，即可完成HTTPS配置

1. 将申请的证书、秘钥文件上传到 *C:\wwwroot\cert* 目录

2. 打开 [bitnami-apps-vhosts.conf（虚拟主机配置配置文件）](/维护参考.md#apache) 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-addmorevhostconfig-websoft9.png)

3. 将下面的 HTTPS 配置文件模板，增加到 httpd-vhosts.conf 文件中(不能删除原有内容)

    ```
    <VirtualHost *:443>
    ServerName  www.mydomain.com
    DocumentRoot "C:\wwwroot\mysite2"
    <Directory "C:\wwwroot\mysite2">
    Options Indexes FollowSymlinks
    AllowOverride All
    Require all granted
    </Directory>
    SSLEngine on
    SSLCertificateFile  "C:\wwwroot\cert\cert.pem"
    SSLCertificateKeyFile  "C:\wwwroot\cert\key.pem"
    SSLCertificateChainFile  "C:\wwwroot\cert\chain.pem"
    </VirtualHost>
    ```

4. 修改其中的 ServerName, DocumentRoot, ErrorLog, CusomLog, Directory等项的值（[修改参考](#virtualhost)），修改完成后保存

5. 重启 Apache 服务 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-bitnami001-websoft9.png)

#### 专题指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。

> WAMP 默认已安装 SMTP 所需的组件，请勿重复安装或随意更改环境配置文件  

不建议在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

SMTP设置与具体的网站程序有关，下面以**网易邮箱**为例，提供一个通用的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 登录网站后台，找到 SMTP 设置界面
3. 填写 SMTP 参数
4. 测试发邮件

更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)


### MySQL 数据管理

Python 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP/phpmyadmin*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理

#### 浏览器打开 http://公网IP地址/9panel，无法访问（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 9Panel 是什么？

[9Panel](https://github.com/Websoft9/9panel)是 Websoft9 公司镜像的开源组件之一，支持中英文显示，部分镜像内置了9Panel. 它是集合数据库管理、文档和支持服务的引导页面，是镜像快速入门的向导工具。基于Bootstrap+vue.js开发，几乎不会占用系统资源，也不会对系统文件进行任何修改。