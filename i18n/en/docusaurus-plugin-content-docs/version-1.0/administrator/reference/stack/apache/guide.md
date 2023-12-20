---
sidebar_position: 1
slug: /apache
tags:
  - HTTP
  - Web Server
  - proxy
---


# Guide

Apache is the short name of [Apache HTTP Server](https://httpd.apache.org/) 

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/apachehttp-architecture.gif)


## Tutorial

### Domain binding{#domain}

The precondition for binding a domain is that application can accessed by domain name, then complete below:  

1. Connect your Server by SFTP tool

2. Modify [Apache vhost configuration file](#path), change the **ServerName**'s value to your domain name
   ```text
   <VirtualHost *:80>
   ServerName www.mydomain.com # Set your domain name
   DocumentRoot "/data/wwwroot/mysite2"
   ...
   ```
3. Restart [Apache service](#service)
   ```
   sudo systemctl restart apache
   ```

### Set Rewrite{#rewrite}

There are three steps to using and set Apache Rewrite:  

1. Open the [Apache module configuration file](#path), make sure **Rewrite module** is enabled
2. Check your [Apache vhost configuration file](#path) that VirtualHost section have **AllowOverride All** item
3. Add .htaccess file to your application root directory and configure rewrite rules in the file  

**Example: 301**    

```shell

<IfModule mod_rewrite.c>
RewriteEngine On
Redirect 301 "/empirecmsall-image-guide" "/xdocs/empirecms-image-guide"
Redirect 301 "/wordpress-image-guide" "/xdocs/wordpressold-image-guide"

</IfModule>

```

**Example: Hide suffix**

```
<IfModule mod_rewrite.c>
RewriteRule ^test$ test.php
ErrorDocument 404 /404.txt

</IfModule>

```

### Use special port for Apache

1. Add VirtualHost section at [Apache vhost configuration file](#path)
   
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

2. Add below section at **httpd.conf** file
   
   ```text
   #Listen 12.34.56.78:80
   Listen 80
   Listen 81
   Listen 82
  
   ```

3. Restart [Apache service](#service)



### Forbidden special IP access{#denyip}

Edit VirtualHost section at [Apache vhost configuration file](#path), xxx.xxx.xxx.xxx is IP address  

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

### Set Apache MaxRequests{#connections}

1. Run the command `httpd -V` to check NPM work mode of Apache
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
2. Modify */etc/httpd/conf/httpd.conf* and set the below items
   ```
   <IfModule prefork.c>
      StartServers        5
      MinSpareServers     5
      MaxSpareServers     10
      MaxClients          256
      MaxRequestsPerChild 3000
   </IfModule>
   ```

### Set the default page{#defaultpage}

```
<VirtualHost *:80>
ServerName win.websoft9.com
<IfModule dir_module>
  DirectoryIndex index.hmtl defalut.html README.html readme.html about.html
</IfModule>
DocumentRoot "/data/wwwroot/default/site"
...
```

### Set the Cache for Apache

Refer to: [Cache guide](http://httpd.apache.org/docs/2.4/caching.html)

## Troubleshoot{#troubleshoot}

#### Apache error: You don't have permission to access/on this server?

Solution:  

1.  Check the permission of application root directory
2.  Check the Apache vhost file that have **AllowOverride All   Require all granted** items

####  *No spaces...* warning restart Apache?

When this message appears, restarting the service was successful also.  

Solution:  

```
echo "fs.inotify.max_user_watches=262144" >> /etc/sysctl.conf 

sysctl -p
```

####  [so:warn] [pid 14645] AH01574: module ssl_module is already loaded when running `httpd -t` command?

Reason: mod_ssl reload   
Solution: Check the below files and found **mod_ssl** item, just retain one  

  * /etc/httpd/conf.modules.d/00-base.conf
  * /etc/httpd/conf.modules.d/00-ssl.conf 

## Parameters

### Path{#path}

Different Linux distributions have different installation paths:  

**CentOS/RedHat**

Apache main directory:  */etc/httpd*  
Apache vhost configuration file: */etc/httpd/conf.d/vhost.conf*    
Apache main configuration file: */etc/httpd/conf/httpd.conf*   
Apache logs file: */var/log/httpd*  
Apache module configuration file: */etc/httpd/conf.modules.d/00-base.conf*   

**Ubuntu/Debian**

Apache main directory:  */etc/apache2*  
Apache vhost configuration file: */etc/apache2/sites-available/000-default.conf*  
Apache main configuration file: */etc/apache2/apache2.conf*  
Apache logs file: */var/log/apache2*  
Apache module directory: */etc/apache2/mods-available*

### CLI

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

### Service{#service}

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

### VirtualHost Template{#virtualhost}

All items in the VirtualHost must be correct, any error may cause Apache can't start and application not accessible

|  VirtualHost Item  |  Use  |  Necessity |
| --- | --- | --- |
|  ServerName  |  Primary domain   |  Required |
|  ServerAlias  |   Sencond |  Optional |
|  DocumentRoot |  The real website storage directory   | Required and must be correct |
|  Directory |  The real website storage directory   |  Required and must be correct |
|  ErrorLog  | error logs directory   |  Suggestion  |
|  CustomLog  | visit logs directory  |  Suggestion |

The following are common VirtualHost templates for various Apache use cases:

#### HTTP VirtualHost{#wwwtemplate}

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

#### HTTPS VirtualHost{#httpstemplate}

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

#### HTTP  Alias{#aliastemplate}

```
Alias /path /data/wwwroot/zdoo
<Directory "/data/wwwroot/zdoo">
Options Indexes FollowSymlinks
AllowOverride All
Require all granted
</Directory>
```

#### HTTP Proxy{#proxytemplate}

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