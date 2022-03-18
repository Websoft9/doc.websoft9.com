---
sidebar_position: 1
slug: /apache
tags:
  - Apache
  - Web 服务器
---


# 指南

Apache 一般代指的 Apache HTTP Server （[官方文档](http://httpd.apache.org/docs/2.4/zh-cn/)）。Apache HTTP Server 是介于应用程序和用户之间的一个中间件系统。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/apachehttp-architecture.gif)


Apache 在网站工作过程中，起着非常重要的作用。下面列出一些常见的设置场景，供用户参考


## 场景

### 域名绑定{#domain}

当服务器上只有一个网站时，不做域名绑定也可以访问网站。但从安全和维护考量，**域名绑定**不可省却。

假设用户已经上传网站到服务器，那么域名绑定操作步骤如下：

1. 确保域名解析已经生效  
2. 使用 WinSCP 等工具登录云服务器
3. 修改 [Apache虚拟机主机配置文件](#path)，将其中的 **ServerName** 项的值修改为你的域名
   ```text
   <VirtualHost *:80>
   ServerName www.mydomain.com # 此处修改为你的域名
   DocumentRoot "/data/wwwroot/mysite2"
   ...
   ```
4. 保存配置文件，重启 [Apache 服务](#service)

### 设置伪静态{#rewrite}

使用和设置 Apache 伪静态有三个步骤：

1.  打开 [Apache模块配置文件](#path)，检查 Rewrite 模块是否启用（LAMP 环境默认已经开启 Rewirte）
2.  保证 [Apache 虚拟主机配置文件](#path)中 VirtualHost 配置段中增加 AllowOverride All
3.  给需要使用伪静态的网站的根目录中增加.htaccess文件，并在其中配置伪静态规则

**范例：重定向**

1. 开启Apache的rewrite模块
1. 在网站根目录中增加.htaccess文件
```shell

<IfModule mod_rewrite.c>
RewriteEngine On
Redirect 301 "/empirecmsall-image-guide" "/xdocs/empirecms-image-guide"
Redirect 301 "/wordpress-image-guide" "/xdocs/wordpressold-image-guide"

</IfModule>

```

**范例：隐藏后缀名**

```
<IfModule mod_rewrite.c>
RewriteRule ^test$ test.php
ErrorDocument 404 /404.txt

</IfModule>

```

### 配置 Apache 使用不同端口访问网站

当服务有多个网站，但不想通过域名访问，可以配置 Apache 使用不同的端口访问不同的网站,步骤如下：

1. 确保在安全组中已放通相应端口
2. 使用 WinSCP 等工具登录云服务器
3. 修改 [Apache虚拟机主机配置文件](/zh/stack-components.md#apache)，修改虚拟主机 ** VirtualHost ** 端口号
   
   ```text
   <VirtualHost *:81>
    ServerName wordpress.example.com
    #ServerAlias example.com
    DocumentRoot "/data/wwwroot/web1"
    ErrorLog "logs/wordpress-error_log"
    CustomLog "logs/wordpress-access_log" common
    <Directory "/data/wwwroot/web1">
        Options Indexes FollowSymlinks
        AllowOverride All
        Require all granted
    </Directory>
   </VirtualHost>

   <VirtualHost *:82>
    ServerName wordpress.example.com
    #ServerAlias example.com
    DocumentRoot "/data/wwwroot/web2"
    ErrorLog "logs/wordpress-error_log"
    CustomLog "logs/wordpress-access_log" common
    <Directory "/data/wwwroot/web2">
        Options Indexes FollowSymlinks
        AllowOverride All
        Require all granted
    </Directory>
   </VirtualHost>
   
   ```

4. 保存配置文件，在 Apache 主配置文件 httpd.conf 中监听对应端口
   
   ```text
   #Listen 12.34.56.78:80
   Listen 80
   Listen 81
   Listen 82
  
   ```

5. 重启 [Apache 服务](/zh/admin-services.md#apache)



### 拒绝通过 IP 访问应用

编辑网站的 Apache 虚拟主机配置段为如下格式，其中 xxx.xxx.xxx.xxx 表示服务器 IP 地址

```
NameVirtualHost  xxx.xxx.xxx.xxx
<virtualhost  xxx.xxx.xxx.xxx:80>
ServerName   xxx.xxx.xxx.xxx
<Directory />
Order Allow,Deny
Deny from all
</Directory>
</virtualhost>
```

### 设置 Apache 并发连接数{#connections}

有大量访问的时候速度很慢，或403错误后反复刷新才能访问等问题，可能是性能造成的。  

一方面，需要提高服务器配置，另外一方面需要通过修改 Apache 并发参数以提升性能：

1. 登录服务器后运行命令`httpd -V`，查询当前Apache的NPM工作模式
   ```
   httpd -V
   AH00558: httpd: Could not reliably determine the server's fully qualified domain name
   Server version: Apache/2.4.6 (CentOS)
   Server built:   Aug  8 2019 11:41:18
   Server's Module Magic Number: 20120211:24
   Server loaded:  APR 1.4.8, APR-UTIL 1.5.2
   Compiled using: APR 1.4.8, APR-UTIL 1.5.2
   Architecture:   64-bit
   Server MPM:     prefork
     threaded:     no
       forked:     yes (variable process count)
   ```
2. 修改 */etc/httpd/conf/httpd.conf*，根据服务器配置的承载能力修改并发相关参数。比如：MaxClients 设置为2000，就可以处理2000个并发请求
   ```
   <IfModule prefork.c>
      StartServers        5
      MinSpareServers     5
      MaxSpareServers     10
      MaxClients          256
      MaxRequestsPerChild 3000
   </IfModule>
   ```

### HTTP 跳转 HTTPS{#httptohttps}

**方案一：修改.htaccess文件**

.htaccess文件提供了一种目录级别的修改配置的方式。

```
#任何情况下均强制跳转
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]


#指定域名下的自动跳转
RewriteEngine On 
RewriteCond %{HTTP_HOST} ^yourdomain\.com [NC]
RewriteCond %{SERVER_PORT} 80 
RewriteRule ^(.*)$ https://www.yourdomain.com/$1 [R,L]

#指定文件夹的自动跳转
RewriteEngine On 
RewriteCond %{SERVER_PORT} 80 
RewriteCond %{REQUEST_URI} folder 
RewriteRule ^(.*)$ https://www.yourdomain.com/folder/$1 [R,L]

```

**方案二：修改vhost文件**

要想开启自动跳转功能，请确保 Apache 的 Rewirte 模块加载，然后按照以下方案进行设置：
1. 整站跳转
    如果需要整站跳转，则在网站的配置文件（/etc/http/vhost/vhost.conf）的 \<Directory\> 标签内添加：
    
    
        RewriteEngine on
        RewriteCond %{SERVER_PORT} !^443$
        RewriteRule ^(.*)?$ https://%{SERVER_NAME}/$1 [L,R=301]
2. 只对某个目录的页面进行自动跳转，请将 **yourfolder** 改成自己的目录名 
  
        RewriteEngine on
        RewriteBase /yourfolder
        RewriteCond %{SERVER_PORT} !^443$
        #RewriteRule ^(.*)?$ https://%{SERVER_NAME}/$1 [L,R]
        RewriteRule ^.*$ https://%{SERVER_NAME}%{REQUEST_URI} [L,R=301]
3. 只将带 www 的 URL 跳转至 HTTPS，请将 **www.yourdomain.com** 改成自己想要设置跳转的域名
  
        RewriteEngine On 
        RewriteRule ^/(.*)$ www.yourdomain.com/$1 [R=301]
4. 对除了某一个页面的其他所有页面进行 HTTPS 跳转

        RewriteEngine on 
        RewriteCond %{SERVER_PORT} !^443$ 
        RewriteCond %{REQUEST_URI} !^/tz.php 
        RewriteRule (.*) https://%{SERVER_NAME}/$1 [R]
    这段配置的作用是指除了 /tz.php 页面用 http 访问，其他页面均为 https 访问，/tz.php 可改为自己实际要 http 访问的后缀。

### 设置网站默认首页{#defaultpage}

默认访问网站目录时，系统会自动根据顺序寻找列出的页面，并显示其中一个。

```
<VirtualHost *:80>
ServerName win.websoft9.com
<IfModule dir_module>
  DirectoryIndex index.hmtl defalut.html README.html readme.html about.html
</IfModule>
DocumentRoot "/data/wwwroot/default/site"
...
```

### 设置缓存，提升性能

Apache HTTP 服务器提供了一系列缓存功能，这些缓存功能旨在以各种方式提高服务器的性能。

详情参考官方文档：[缓存指南](http://httpd.apache.org/docs/2.4/caching.html)

### 安全防护

大多数情况下，Web服务器受到威胁，并不是因为HTTP Server代码中的问题。而是来自附加代码，CGI脚本或基础操作系统的问题。因此，您必须始终注意系统上所有软件的问题和更新。

**DoS攻击防护**

最有效的反DoS工具通常是防火墙或其他操作系统配置。例如，大多数防火墙可以配置为限制来自任何单个IP地址或网络的同时连接数，从而防止一系列简单的攻击。当然，这对分布式拒绝服务攻击（DDoS）没有帮助。  

但Apache HTTP Server配置设置可以帮助缓解问题：

* RequestReadTimeout
* TimeOut
* KeepAliveTimeout 
* MaxRequestWorkers 

### 关闭 Apache Test Page

使用 # 号将: /etc/httpd/conf.d/welcome.conf 中的所有内容全部注释掉，然后重启 Apache 服务

### 关闭缺省情况目录列表可查看

Apache httpd 服务器在缺省的情况下，开启了基于目录列表的访问，这是一个存在安全隐患的问题，因此可以关闭这个功能。

### 连接程序语言环境{#languages}

Apache可以作为常见的开发语言的 Web 服务器，集成数据库、应用容器，最后形成一个完整的应用运行环境，例如：Apache+PHP，Apache+Tomcat+Java等

下面我们以常见的开发语言为例，分别介绍它们是如何与Apache一起工作的。

#### PHP

Apache被广泛用于PHP环境，Apache有两种PHP处理机制：

- php-fpm：PHP内核中用来处理PHP文件的解释器和进程管理器
- mod_php：Apache的PHP处理模块

mod_php 作为Apache的模块，没有独立的进程，无需额外设置和处理，使用起来非常简单。

PHP-FPM(PHP FastCGI Process Manager)意：PHP FastCGI 进程管理器，用于管理PHP 进程池的软件，用于接受Apache HTTP Server等Web服务器的请求。PHP-FPM提供了更好的PHP进程管理方式，可以有效控制内存和进程、可以平滑重载PHP配置。  

下面是Apache+PHP-FPM共同工作的系统架构图，其中mod_proxy_fcgi用于Apache连接php-fpm

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/apache_event_php-fpm.jpg)

接下来我们将以 **php-fpm 转换成 mod_php** 为范例，介绍如何作出相应的配置：

1. 使用 SFTP 工具修改 */etc/httpd/conf.d/php.conf* （如果该目录下有php.conf的备份文件，直接复制内容到php.conf）
```
#
# The following lines prevent .user.ini files from being viewed by Web clients.
#
<Files ".user.ini">
    <IfModule mod_authz_core.c>
        Require all denied
    </IfModule>
    <IfModule !mod_authz_core.c>
        Order allow,deny
        Deny from all
        Satisfy All
    </IfModule>
</Files>

#
# Allow php to handle Multiviews
#
AddType text/html .php

#
# Add index.php to the list of files that will be served as directory
# indexes.
#
DirectoryIndex index.php

# mod_php options
<IfModule  mod_php7.c>
    #
    # Cause the PHP interpreter to handle files with a .php extension.
    #
    <FilesMatch \.(php|phar)$>
        SetHandler application/x-httpd-php
    </FilesMatch>

    #
    # Uncomment the following lines to allow PHP to pretty-print .phps
    # files as PHP source code:
    #
    #<FilesMatch \.phps$>
    #    SetHandler application/x-httpd-php-source
    #</FilesMatch>

    #
    # Apache specific PHP configuration options
    # those can be override in each configured vhost
    #
    php_value session.save_handler "files"
    php_value session.save_path    "/var/lib/php/session"
    php_value soap.wsdl_cache_dir  "/var/lib/php/wsdlcache"

    #php_value opcache.file_cache   "/var/lib/php/opcache"
</IfModule>
```

2. 停止 [PHP-FPM 服务](/zh/admin-services.md#PHP-FPM)

3. 保存并重启 [Apache 服务](/zh/admin-services.md#apache)

#### Java

Apache HTTP Server 无法直接运行Java程序，而是与Tomcat一起组合去部署Java程序。

这种组合下，Apache处理静态资源，JSP等动态程序需转发给Tomcat处理，然后返回给用户。

Apache HTTP Server 与 Tomcat 最常见的连接方式是http_proxy，即利用 Apache 自带的 mod_proxy 模块使用代理技术来连接 Tomcat。 

http_proxy 模式是基于 HTTP 协议的代理，因此它要求 Tomcat 必须提供 HTTP 服务，也就是说必须启用 Tomcat 的 HTTP Connector。一个最简单的配置如下：

```
ProxyPass /images !
ProxyPass /css !
ProxyPass /js !
ProxyPass / http://localhost:8080/
```

更多请参考：[《Apache HTTP Server 与 Tomcat 的三种连接方式介绍》](https://www.ibm.com/developerworks/cn/opensource/os-lo-apache-tomcat/)

#### Python

Apache HTTP Server 也可以用于Python环境，通过扩展模块mod_proxy_uwsgi，连接Python的uWSGI服务器或Gunicorn服务器，便可以解析Python程序。

这种组合的的基本配置方法如下：

1. 配置为uwsgi.ini
   ```
   [uwsgi]
   chdir = /home/vagrant/myweb/
   virtualenv = /home/vagrant/env/
   socket = 127.0.0.1:8080
   env = DJANGO_SETTINGS_MODULE=myweb.settings
   module =myweb.wsgi:application
   master = true
   processes = 4
   vacuum = True
   max-requests = 5000
   daemonize = /var/log/uwsgi.log
   pidfile = /var/log/uwsgi.pid
   ```
2. apache的配置文件加载mod_proxy_uwsgi.so
3. apache的配置文件反向代理到uwsgi
   ```
   ProxyPass / uwsgi://127.0.0.1:8080
   ```

#### Node.js

Apache HTTP Server 也可以用于Node.js环境，Apache HTTP Server 与 Node.js 最常见的连接方式是http_proxy，即利用 Apache 自带的 mod_proxy 模块使用代理技术来连接 Node.js。   

下面是典型的配置文件范例：

```
server {
        listen 80 default_server;
        server_name _;


        location / {
         proxy_pass http://127.0.0.1:2368;
         proxy_set_header Host $host;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

}
```



## 参数

### 路径{#path}

不同的Linux发行版，对应的安装路径有一定的差异：

**CentOS/RedHat**

Apache 安装目录：*/etc/httpd*  
Apache 虚拟主机配置文件：*/etc/httpd/conf.d/vhost.conf*  
Apache 主配置文件： */etc/httpd/conf/httpd.conf*  
Apache 日志文件： */var/log/httpd*  
Apache 模块配置文件： */etc/httpd/conf.modules.d/00-base.conf*

**Ubuntu/Debian**

Apache 安装目录：*/etc/apache2*  
Apache 虚拟主机配置文件：*/etc/apache2/sites-available/000-default.conf*  
Apache 主配置文件： */etc/apache2/apache2.conf*  
Apache 日志文件： */var/log/apache2*  
Apache 模块目录： */etc/apache2/mods-available*

### 命令行

 Apache HTTP 服务器包含的所有命令行（可执行程序）如下：

| 命令 | 说明                                  |
| ------- | ---------------------------------------------- |
| httpd |Apache 服务器|
| apachectl | Apache HTTP 服务器控制工具。|
| ab | Apache HTTP 服务器性能基准工具。|
| apxs | Apache 扩展工具。|
| configure | 配置源代码。|
| dbmmanage | 为基本认证创建和更新 DBM 格式的用户认证文件。|
| fcgistarter | 启动 FastCGI 程序。|
| htcacheclean | 清理磁盘缓存。|
| htdigest | 为摘要认证创建和更新用户认证文件。|
| htdbm | 操作 DBM 密码数据库。|
| htpasswd | 为基本认证创建和更新用户认证文件。|
| httxt2dbm | 为 RewriteMap 创建 dbm 文件。|
| logresolve | 将 Apache 日志文件中的 IP 地址解析到主机名称。|
| log_server_status | 周期性的记录服务器状态。|
| rotatelogs | 不关闭 Apache 而切换日志文件。|
| split-logfile | 将多个虚拟主机的日志文件按照主机拆分。|
| suexec | 执行外部程序前切换用户。|

### 服务启停{#service}

以 httpd 服务为例，在不同的操作系统启用如下：

```
#CentOS/Redhat/Fedora
sudo systemctl start httpd
sudo systemctl stop httpd
sudo systemctl restart httpd
sudo systemctl status httpd

# Ubutnu/Debian
sudo systemctl start apache2
sudo systemctl stop apache2
sudo systemctl restart apache2
sudo systemctl status apache2

# Docker
sudo docker start apache
sudo docker stop apache
sudo docker restart apache
sudo docker stats apache
```

### VirtualHost 模板{#virtualHost}

Apache中的虚拟主机是通过 VirtualHost 进行配置的，下表是 VirtualHost  核心参数：

|  VirtualHost 项  |  作用说明  |  必要性 |
| --- | --- | --- |
|  ServerName  |  主域名   |  必须填写 |
|  ServerAlias  |   辅域名 |  可以不填或删除 |
|  DocumentRoot |  网站存放目录，同下  | 务必准确无误 |
|  Directory |  网站存放目录，同上  |  务必准确无误 |
|  ErrorLog  | 错误日志路径，系统会根据定义的路径产生相关日志文件   |  可以不填或删除 |
|  CustomLog  | 访问日志路径，系统会根据定义的路径产生相关日志文件  |  可以不填或删除 |

下面是常见的 VirtualHost  模板，适用于各种 Apache 应用场景：

#### HTTP VirtualHost 标准模板{#wwwtemplate}

```
<VirtualHost *:80>
ServerName www.mydomain.com
ServerAlias other.mydomain.com
DocumentRoot "/data/wwwroot/zdoo"
ErrorLog "/var/log/httpd/www.mydomain.com_error_apache.log"
CustomLog "/var/log/httpd/www.mydomain.com_apache.log" common
<Directory "/data/wwwroot/zdoo">
Options Indexes FollowSymlinks
AllowOverride All
Require all granted
</Directory>
</VirtualHost>
```

#### HTTP  Alias 模板{#aliastemplate}

```
Alias /path /data/wwwroot/zdoo
<Directory "/data/wwwroot/zdoo">
Options Indexes FollowSymlinks
AllowOverride All
Require all granted
</Directory>
```

#### HTTP Proxy 模板{#proxytemplate}

下面是一个包含了 Proxy 的虚拟主机配置文件，其中应用程序运行在8069端口，通过转发配置域名访问。

```
<VirtualHost *:80>
ServerAdmin webmaster@dummy-host2.localhost
ServerName youdomain.com
ProxyRequests off
<Proxy *>
Order deny,allow
Allow from all
</Proxy>
ProxyPass / http://172.21.172.27:8069/
ProxyPassReverse / http://172.21.172.27:8069/
</VirtualHost>
```

#### HTTPS VirtualHost 模板{#httpstemplate}

```
<VirtualHost *:443>
ServerName  www.mydomain.com
DocumentRoot "/data/wwwroot/zdoo"
#ErrorLog "logs/www.mydomain.com-error_log"
#CustomLog "logs/www.mydomain.com-access_log" common
<Directory "/data/wwwroot/zdoo">
Options Indexes FollowSymlinks
AllowOverride All
Require all granted
</Directory>
SSLEngine on
SSLCertificateFile  /data/cert/www.mydomain.com.crt
SSLCertificateKeyFile  /data/cert/www.mydomain.com.key
SSLCertificateChainFile  /data/cert/root_bundle.crt
</VirtualHost>
```
