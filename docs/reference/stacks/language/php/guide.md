---
sidebar_position: 1
slug: /php
---

# 指南

## 场景

### PHP-FPM 使用{#fpm}

PHP-FPM 用于管理 PHP 进程池，接受 Apache/Nginx 等 Web 服务器的请求。PHP-FPM 提供了更好的 PHP 进程管理方式，可以有效控制内存和进程、可以平滑重载 PHP 配置。

### Composer 使用{#compose}

### Web 框架{#framework}

#### Symfony{#symfony}
#### Laravel{#laravel}
#### CodeIgniter{#codeigniter}
#### ThinkPHP{#thinkphp}
#### Yii 2{#yii}

### PHP 版本变更（Linux）{#changeversion}

#### PHP 版本升级{#upgrade}

在实际使用过程中，会遇到升级 PHP 大版本的情形，如：从 PHP5.5->PHP5.6 或 PHP5.6->PHP7.0等。对于我们提供的LAMP环境来说，升级方法非常简单。

以PHP5.5->PHP5.6为例，具体如下：

1. 连接到Linux服务器后，依次执行如下命令：
```
//首先，禁用当前 PHP55 源
yum-config-manager --disable remi-php55   

//然后，启用需升级 PHP56 源
yum-config-manager --enable remi-php56     

//最后，升级更新
yum update -y
```


2. 为了确保升级成功，请检查升级后的 PHP 版本
```
php -v
```

> 以上方案也适用于 PHP7.0->PHP7.2

#### PHP 版本降级{#downgrade}

以PHP7.0降级到PHP5.6为例，具体步骤如下：

```
//禁用当前7.0版本的下载源
yum-config-manager --disable remi-php70

//然后，启用需降级的版本 PHP56 源
yum-config-manager --enable remi-php56     

# 卸载PHP7.0
yum remove php-* -y

# 安装主要的PHP模块
yum -y install php-pecl-imagick php php-mysql php-common php-gd php-mbstring php-mcrypt php-devel php-xml php-pdo php-bcmath php-pear php-opcache php-ldap php-odbc php-xmlrpc php-json php-mysqlnd php-pdo php-pdo_dblib php-recode php-snmp php-soap php-pecl-zip php-curl php-imap

# 安装其他包
pear install Mail
pear install net_smtp
```

### PHP 版本变更（Windows）{#versionwin}

Windows系统下的IIS环境，安装了多版本的PHP，可以直接修改php配置文件，也可以通过图形化界面操作：

选择需要管理PHP版本的网站，然后打开PHP Manager，点击“Change PHP Version”，重启IIS后生效

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-changephpver-websoft9.png)

> 注意：PHP版本影响范围为一个网站或网站中的应用程序，没有整个IIS全局PHP版本设置，这样大大的方便了多版本的应用访问。


### 修改 php 配置{#config}

在使用PHP网站的时候，你可能会碰到需要修改：上传文件大小、内存限制等参数。这个时候，就需要修改 PHP 的配置文件。  

有两种修改 PHP 配置的方案：

#### 修改 php.ini{#ini}

修改 php.ini 文件对全局生效。  

1. 使用 SFTP 工具修改 */etc/php.ini* 
    ```shell
    # 修改文件大小限制，注意数字后面需要带上单位M
    post_max_size = 16M
    upload_max_filesize = 16M

    # 修改超时时间限制
    max_execution_time = 90

    # 修改内存限制
    memory_limit – Minimum: 256M
    ```
2. 保存并重启 [PHP 服务](#service)

#### 修改 .htaccess{#htaccess}

修改 .htaccess 文件对网站生效。  

1. 使用 SFTP 工具修改**网站根目录**下的 .htaccess 文件（没有此文件可以自行创建），增加所需的配置项
   ```
   # File upload limit
   php_value  post_max_size = 16M
   php_value  upload_max_filesize = 16M

   # Max Execution Time
   php_value  max_execution_time = 90

   # Memory Limit
   php_value  memory_limit – Minimum: 256M
   ```
   > 同 php.ini 一样的参数

2. 保存并重启 [PHP 服务](#service)

#### 将 php-fpm 切换到 mod_php

LAMP 默认使用 php-fpm 服务来解析PHP文件，如果想用 mod_php 解析 PHP 文件，请参照下面步骤：

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

2. 停止 [PHP-FPM 服务](#service)


## 故障排除{#troubleshoot}

#### PHP 不支持 SMTP？

PHP 与 SMTP 相关的问题

1.  需要了解你所使用的STMP功能是否调用了PHP软件包（或扩展类）

   	* php官方提供的mail()类，这个类不支持SMTP验证
    * php扩展包-[PHPMailer](https://github.com/PHPMailer/PHPMailer)，这个类功能比较全面

2.  php_openss 版本过低或者没有安装，php_openssl 的 CA 证书缺失或异常


## 参数

### 路径{#path}

PHP on Linux 配置文件：*/etc/php.ini* 
PHP on Windows 配置文件：*C:\websoft9\php-\*\php.ini*

### 命令行{#cmd}

主要有 php 和 composer 两个命令行

### 服务{#service}

针对不同的 PHP 环境有不同的服务启停模式：

```
# PHP-FPM On Linux
sudo systemctl start php
sudo systemctl stop php
sudo systemctl restart php
sudo systemctl status php

# PHP On Docker
sudo docker start php
sudo docker stop php
sudo docker restart php
sudo docker stats php
```