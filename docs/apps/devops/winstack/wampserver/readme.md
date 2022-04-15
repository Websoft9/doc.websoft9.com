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

[WampServer](http://www.wampserver.com/?lang=en) 是一个 Windows 环境下的 Apache+PHP+MySQL/MariaDB 组合，拥有简单的图形和菜单安装和配置环境，支持 PHP 多版本切换。支持22种语言，其中包括简体中文和繁体中文。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-phpini-websoft9.png)


部署 Websoft9 提供的 WampServer 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 WampServer 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  WampServer，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程


## WampServer 初始化向导

### 详细步骤

1. 使用本地 Chrome 或 Firefox 浏览器访问网址：*http://服务器公网IP/9panel*, 就进入引导页面9Panel
   ![9panel](https://libs.websoft9.com/Websoft9/DocsPicture/en/wampserver/wampserver-9panelui.png)

2. 通过 9Panel 可以快速了解镜像基本情况，管理数据库，找到帮助文档，寻求人工支持
    ![9panel](https://libs.websoft9.com/Websoft9/DocsPicture/zh/9panel/9panel-mysql-websoft9.png)

3. 远程桌面登录到 Windows 服务器，查看 WampServer 是否正常运行（图标为绿色），点击【重新启动所有服务】测试可用性。

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-clicks-websoft9.png)

   > 如果桌面右下角没有 WampServer 图标，请重启服务器后再查看。

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。


## WampServer 安装网站

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

### 安装第二个网站

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


### 安装第 N 个网站

安装第n个网站与安装第二个网站的操作步骤一模一样

最后我们温故而知新，总结 WampServer 安装网站步骤： 

1. 上传网站代码
2. 绑定域名（非必要）
3. 新增站点配置或修改示例站点配置
4. 增加网站对应的数据库（非必要）
5. 进入安装向导



## 环境配置

### Apache 配置

#### 绑定域名

修改 [Apache虚拟机主机配置文件](#apache)，将其中的 **ServerName** 项的值修改为你的域名

#### 修改网站目录

修改 [Apache虚拟机主机配置文件](#apache)，将其中的 DocumentRoot 和 Directory 的值修改成你网站的路径 项的值修改为你的域名
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-mddfvhost-websoft9.png)

#### 使用 Apache 伪静态

使用 Apache 伪静态有三个步骤：

1.  打开 [Apache 主配置文件](#apache)，检查 Rewrite 模块是否启用（Wampserver 环境默认已经开启 Rewirte）
   ```
    LoadModule rewrite_module modules/mod_rewrite.so #若前面有"#"号则需要将其去掉，使之支持 mod_rewrite 模块；
   ```
2.  保证 [Apache 虚拟主机配置文件](#apache)中 VirtualHost 配置段中增加 AllowOverride All
3.  给需要使用伪静态的网站的根目录中增加 `.htaccess` 文件，并在其中配置伪静态规则

#### 设置 Apache 并发连接数

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


### PHP 配置

#### 修改 php.ini

除了直接编辑 [php.ini](#php) 文件之外，你也可以通过 WampServer 的图形化界面修改 PHP 配置文件
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-phpini-websoft9.png)

#### PHP版本切换

WampServer 支持 PHP 版本在线切换

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-changephpversion-websoft9.png)


#### 安装 PHP 扩展


在 WampServer 上安装和管理 PHP 扩展的通用步骤如下：

1. 下载正确的 PHP 扩展文件（[注意事项](https://www.php.net/manual/zh/install.pecl.windows.php)），上传到服务器的 [PHP 扩展目录](/zh/stack-components.md#php)

2. 开启或关闭扩展

   - 通过 WampServer 可视化工具设置
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-setphpexts-websoft9.png)
   
   - 通过修改 PHP 配置文件设置
     ```
     extension=php_bz2.dll
     ;extension=php_com_dotnet.dll
     ```

不同的 PHP 扩展安装有一定的差异，具体以扩展提供的文档为准

#### 安装 Composer

WAMPServer 镜像中安装 composer 的方法步骤如下：

1. 进入到 PHP7.0.33 目录，按住 shift + 鼠标右键，选择“在此处打开命令行窗口”；
2. 输入 php -r "readfile('https://getcomposer.org/installer');" | php 安装 composer；
3. 在该目录下新建 composer.bat 文件，并编辑输入：```@php "%~dp0composer.phar" %*```；
4. 将 PHP 所在目录路径添加到环境变量中，添加方法参考：[windows系统如何设置添加环境变量？](https://jingyan.baidu.com/article/47a29f24610740c0142399ea.html)
5. 至此，composer 安装完毕。

> 因为 WAMPServer 有多个 PHP 版本，所以需要在每个 PHP 目录下都按照以上教程安装一遍，且在同一时间只能加入某一个版本的 PHP 路径到环境变量，不能同时将所有的 PHP 路径加入到环境变量中去。在切换 PHP版本时，应当同时修改环境变量。


## 参数

**[通用参数表](../administrator/parameter)** 中可查看 Nginx, Java, Docker, MySQL 等 WampServer 应用中包含的基础架构组件路径、版本、端口等参数。 

下面仅列出 WampServer 本身的参数：

### 路径{#path}

#### 网站目录

根目录： *WampServer 环境中，你的网站代码存放位置是没有限制的，因此没有根目录的说法*  
网站存放目录（建议）： *C:\websoft9\wampserver\www*  
示例网站目录： *C:\websoft9\wampserver\www\www.example.com*  

> 通过 *http://公网IP地址* 访问的就是示例网站 

#### Apache{#apache}

**Apache 虚拟主机配置文件**： *C:\websoft9\wampserver\bin\apache\apache2.4.x\conf\extra\httpd-vhosts.conf*  
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-vhost-websoft9.png)

Apache 主配置文件： *C:\websoft9\wampserver\bin\apache\apache2.4.x\conf\httpd.conf*   
Apache 日志文件： *C:\websoft9\wampserver\logs*  
Apache 模块目录： *C:\websoft9\wampserver\bin\apache\apache2.4.x\modules*  

**httpd-vhosts.conf** 默认存在一个 [VirtualHost（虚拟主机）](https://support.websoft9.com/docs/windows/zh/webs-apache.html#虚拟主机) 配置项，对应的就是 **示例网站**
```
<VirtualHost *:80>
ServerName www.mydomain.com
#ServerAlias other.mydomain.com
DocumentRoot "C:\websoft9\wampserver\www\www.example.com"
ErrorLog "logs\www.mydomain.com_error_apache.log"
CustomLog "logs\www.mydomain.com_apache.log" common
<Directory "C:\websoft9\wampserver\www\www.example.com">
   Options Indexes FollowSymlinks
   AllowOverride All
   Require all granted
</Directory>
</VirtualHost>
```

> 有多少个网站，就需要在 **httpd-vhosts.conf** 中增加同等数量的 **VirtualHost** 配置项

#### PHP{#php}

WampServer 环境支持多个 PHP 版本，每个版本都有对应的 PHP 配置文件。  

PHP 配置文件： *C:\websoft9\wampserver\bin\php\php7.x.x\php.ini*  
PHP 扩展目录： *C:\websoft9\wampserver\bin\php\php7.x.x\ext*   
PHP 扩展配置文件： *C:\websoft9\wampserver\bin\php\php7.x.x\ext\phpForApache.ini*  

PHP 扩展启用或关闭，通过修改 PHP 配置文件实现

#### MySQL

MySQL 安装路径：*C:\websoft9\wampserver\bin\mysql*  
MySQL 数据文件：*C:\websoft9\wampserver\bin\mysql\mysql5.x.x\data*  
MySQL 配置文件：*C:\websoft9\wampserver\bin\mysql\mysql5.x.x\my.ini*    
MySQL 可视化管理地址: *http://服务器公网IP/phpmyadmin*，用户名和密码请见 [账号密码](/zh/stack-accounts.md) 章节。

#### MariaDB

MariaDB 安装路径：*C:\websoft9\wampserver\bin\mariadb*  
MariaDB 数据文件：*C:\websoft9\wampserver\bin\mariadb\mariad10.x.x\data*  
MariaDB 配置文件：*C:\websoft9\wampserver\bin\mariadb\mariad10.x.x\my.ini*    
MariaDB 可视化管理地址: *http://服务器公网IP/phpmyadmin*，用户名和密码请见 [账号密码](/zh/stack-accounts.md) 章节。

#### phpMyAdmin

phpMyAdmin 安装路径: *C:\websoft9\wampserver\apps\phpmyadmin4.x.x*  
phpMyAdmin 配置文件: *C:\websoft9\wampserver\apps\phpmyadmin4.x.x\config.inc.php*   
phpMyAdmin 虚拟主机配置文件: *C:\websoft9\wampserver\alias\phpmyadmin.conf*   


### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 3306, 3307   | MySQL 和 MariaDB 端口 | 可选   |


### 版本

在服务器 *C:\websoft9\wampserver* 目录下查看安装目录名称。

### 服务

WampServe 服务随操作系统自动启动，如果手工修改配置参数后，需要重新启停服务

##### 通过 WampServer 管理服务

远程桌面到服务器，点击 WAMPServer 图标，然后点击【重新启动所有服务】，就可以同时重启 Apache, MySQL & MariaDB 服务

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-clicks-websoft9.png)

##### 通过 Windows 系统服务 管理服务

远程桌面到服务器，打开 Windows 系统的服务管理工具：【开始菜单】>【管理工具】>【服务】
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-ss-websoft9.png)

- wampapache64 代表的是 Apache 服务
- wampMysql，代表的是 MySQL 服务
- wampMariadb，代表的是 MariaDB 服务

### 命令行

无
