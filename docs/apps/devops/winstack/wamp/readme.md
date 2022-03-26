---
sidebar_position: 1
slug: /wamp
tags:
  - WAMP
  - PHP
  - Apache
  - Windows
---

# 快速入门

WAMP 集成 PHP 环境，由 Bitnami  维护。它除 Apache,MySQL,PHP 之外，还包含 Zend,Symfony 等6大开发框架，ImageMagick,SQLite 等16个辅助组件，能够兼容运行绝大部分 PHP 应用。

> 本文档兼容 WAPP，它与 WAMP 类似，区别仅在于采用的是PostrgreSQL数据库。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-gui-websoft9.png)


部署 Websoft9 提供的 WAMP 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 WAMP 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  WAMP，务必先完成 **[域名五步设置](./dns#domain)** 过程


## WAMP 初始化向导

### 详细步骤

1. 使用电脑浏览器访问网址：*http://Internet IP/9panel*, 就进入引导页面9Panel

   ![9panel](https://libs.websoft9.com/Websoft9/DocsPicture/en/wampserver/wampserver-9panelui.png)

2. 通过 9Panel 可以快速了解镜像基本情况，管理数据库，找到帮助文档，寻求人工支持

    ![9panel](https://libs.websoft9.com/Websoft9/DocsPicture/zh/9panel/9panel-mysql-websoft9.png)

3. 远程桌面登录到 Windows 服务器，查看 WAMP 是否正常运行（图标为绿色），点击【Restart】按钮测试可用性。如果桌面右下角没有 WAMP 图标，请重启服务器后再查看。

  ![](https://oss.aliyuncs.com/photogallery/photo/1904996544835414/4614/0e08a244-a067-42fa-86a7-5af16328d5c0.png)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题
## WAMP 安装网站

在 WAMP 环境上安装一个网站，也就是我们常说的增加一个虚拟主机。

宏观上看，只需两个步骤：**上传网站代码** + [**虚拟机主机配置文件**](/维护参考.md#apache) **中增加 VirtualHost 配置段**

> VirtualHost 又称之为虚拟主机配置段，每个网站必定在 **虚拟机主机配置文件** 中对应唯一配置段。

### 准备

安装网站之前，请了解如下几个要点，做好准备工作

*  虚拟机主机配置文件：**C:\websoft9\wampstack\apache2\conf\bitnami\bitnami-apps-vhosts.conf* 
*  连接工具：使用 Windows自带的远程桌面工具 连接服务器
*  域名：若需要使用域名，请确保备案后的域名成功解析到服务器IP
*  数据库：网站安装向导过程中可能需要使用数据库，请使用 [phpMyAdmin 管理数据库](#mysql-数据管理)

有一个宏观认知之后，我们开始部署网站

### 安装第一个网站

下面通过**替换示例网站**（WAMP 默认存在一个示例网站）的方式来教你安装你的第一个网站：

1. 使用 远程桌面工具 连接服务器

2. 删除示例网站 *C:\websoft9\wamp\www\www.example.com* 下的所有文件（保留目录）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-exadr-websoft9.png)

3. 将本地电脑上的网站源码上传到示例目录下

4. 修改 [**虚拟机主机配置文件**](/维护参考.md#apache) 中已有 VirtualHost 配置段（[修改参考](/zh/solution-deployment.md#virtualhost)），实现绑定域名、修改网站目录名称等操作。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-mddfvhost-websoft9.png)
   ::: warning
   如果不绑定域名、不修改网站目录名称，请跳过步骤4和5
   :::
5. 保存 **虚拟机主机配置文件**，然后 [重启所有服务](/维护参考.md#apache-1)

6. 本地浏览器访问：*http://域名* 或 *http://服务器公网IP* 即可访问您的网站

### 安装第二个网站

从安装第二个网站开始，需要在 [**虚拟机主机配置文件**](/zh/stack-components.md#apache) 中增加对应的虚拟主机配置段，具体如下

1. 使用 远程桌面 连接服务器，在 C:\wwwroot 下新建一个网站目录，假设命令为“mysite2”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-addmysite2-websoft9.png)

2. 将本地网站源文件上传到：*C:\wwwroot\mysite2* 

3. 编辑 [**虚拟机主机配置文件**](/维护参考.md#apache) 文件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-addmorevhostconfig-websoft9.png)

    根据是否通过域名访问，选择下面操作之一：

     * **有域名，通过 http://域名 访问网站**
     
     请将下面 VirtualHost 模板拷贝到 httpd-vhosts.conf 中，并修改其中的ServerName, DocumentRoot, ErrorLog, CusomLog, Directory等项的值

       ```
       <VirtualHost *:80>
       ServerName www.mydomain.com
       # ServerAlias other.mydomain.com
       DocumentRoot "C:\wwwroot\mysite2"
       ErrorLog "logs\mydomain.com_error_apache.log"
       CustomLog "logs\mydomain.com_error_apache.log" common
       <Directory "C:\wwwroot\mysite2">
       Options Indexes FollowSymlinks
       AllowOverride All
       Require all granted
       </Directory>
       </VirtualHost>
        ```

     * **没有域名，通过 http://IP/mysite2 访问网站**  
    
     请将下面 Alias 模板拷贝到 httpd-vhosts.conf 中，并修改其中的 /path, Directory等项的值

      ```
      Alias /sitename C:\wwwroot\mysite2
      <Directory "C:\wwwroot\mysite2">
	     Options Indexes FollowSymlinks
	     AllowOverride All
	     Require all granted
	    </Directory>
      ```
4. 保存 [**虚拟机主机配置文件**](/维护参考.md#apache)，然后 [重启Apache服务](/维护参考.md#apache-1)
5. 根据有无域名，本地浏览器访问：*http://域名* 或 *http://服务器公网IP/sitename*  访问你的网站。


### 安装第 N 个网站

安装第n个网站与安装第二个网站的操作步骤一模一样

最后我们温故而知新，总结 WAMP 安装网站步骤： 

1. 上传网站代码
2. 绑定域名（非必要）
3. 新增站点配置或修改示例站点配置
4. 增加网站对应的数据库（非必要）
5. 进入安装向导

## 环境配置


### Apache 配置

Apache 配置主要通过修改 [虚拟主机配置文件](#path) 中的 [VirtualHost 指令](./apache#virtualHost)去实现各种需求。  

#### 绑定域名

修改 [Apache虚拟机主机配置文件](#apache)，将其中的 **ServerName** 项的值修改为你的域名

#### 修改网站目录

修改 [Apache虚拟机主机配置文件](#apache)，将其中的 DocumentRoot 和 Directory 的值修改成你网站的路径 项的值修改为你的域名
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-mddfvhost-websoft9.png)


#### 使用 Apache 伪静态

使用 Apache 伪静态有三个步骤：

1.  打开 [Apache 主配置文件](#apache)，检查 Rewrite 模块是否启用（WAMP 环境默认已经开启 Rewirte）
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

直接编辑 [php.ini](#php) 文件即可

#### 安装 PHP 扩展

在 WAMP 上安装和管理 PHP 扩展的通用步骤如下：

1. 下载正确的 PHP 扩展文件（[注意事项](https://www.php.net/manual/zh/install.pecl.windows.php)），上传到服务器的 [PHP 扩展目录](/维护参考.md#php)

2. 通过修改 PHP 配置文件设置，开启或关闭扩展
   ```
   extension=php_bz2.dll
   ;extension=php_com_dotnet.dll
   ```

不同的 PHP 扩展安装有一定的差异，具体以扩展提供的文档为准

#### 安装 Composer

WAMP 镜像中安装 composer 的方法步骤如下：

1. 进入到 PHP 目录，按住 shift + 鼠标右键，选择“在此处打开命令行窗口”；
2. 输入 php -r "readfile('https://getcomposer.org/installer');" | php 安装 composer；
3. 在该目录下新建 composer.bat 文件，并编辑输入：```@php "%~dp0composer.phar" %*```；
4. 将 PHP 所在目录路径添加到环境变量中，添加方法参考：[Windows系统如何设置添加环境变量？](https://support.websoft9.com/docs/windows/solution-environmentvar.html)
5. 至此，composer 安装完毕。

## 参数

**[通用参数表](./setup/parameter)** 中可查看 Apache, Docker, MySQL 等 WAMP 应用中包含的基础架构组件路径、版本、端口等参数。 

下面仅列出 WAMP 本身的参数：

### 路径{#path}

#### 网站目录

根目录： *WAMP 环境中，你的网站代码存放位置是没有限制的，因此没有根目录的说法*  
网站存放目录（建议）： * C:\wwwroot*  
示例网站目录： * C:\wwwroot\www.example.com*  

> 通过 *http://公网IP地址* 访问的就是示例网站 

#### Apache{#apache}

**Apache 虚拟主机配置文件**： *C:\websoft9\wampstack\apache2\conf\bitnami\bitnami-apps-vhosts.conf*  
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-openvhostconf-websoft9.png)

Apache 主配置文件： *C:\websoft9\wampstack\apache2\conf\httpd.conf*   
Apache 日志文件： *C:\websoft9\wampstack\apache2\logs*  
Apache 模块目录： *C:\websoft9\wampstack\apache2\modules*  

#### PHP{#php}

PHP 配置文件： *C:\websoft9\wampstack\php\php.ini*  
PHP 扩展目录： *C:\websoft9\wampstack\php\ext*   

PHP 扩展启用或关闭，通过修改 PHP 配置文件实现

#### MySQL{#mysql}

MySQL 安装路径：*C:\websoft9\wampstack\mysql\*    
MySQL 数据文件：*C:\websoft9\wampstack\mysql\data\mysql*    
MySQL 配置文件：*C:\websoft9\wampstack\mysql\my.ini*      
MySQL 可视化管理地址: *http://服务器公网IP/phpmyadmin*    

#### phpMyAdmin

phpMyAdmin 安装路径: *C:\websoft9\wampstack\apps\phpmyadmin*  
phpMyAdmin 配置文件: *C:\websoft9\wampstack\apps\phpmyadmin\htdocs\config.inc.php*   
phpMyAdmin 虚拟主机配置文件: *C:\websoft9\wampstack\apps\phpmyadmin\conf\httpd-vhosts.conf*   

### 端口

**[通用参数表](./setup/parameter)** 中可查看

### 版本

在服务器 *C:\websoft9\wampstack\README.txt* 文件中查看。

### 服务

Wamp 服务随操作系统自动启动，如果手工修改配置参数后，需要重新启停服务

##### 通过 WAMP 管理服务

远程桌面到服务器，点击 WAMP 图标，选择 Apache 或 MySQL，然后点击【Restart】，就可以重启服务

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-bitnami001-websoft9.png)

##### 通过 Windows 系统服务 管理服务

远程桌面到服务器，打开 Windows 系统的服务管理工具：【开始菜单】>【管理工具】>【服务】
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wamp-managerservice-websoft9.png)

- wampstackApache 代表的是 Apache 服务
- wampstackMySQL，代表的是 MySQL 服务

### 命令行

无
