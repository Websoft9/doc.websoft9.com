---
sidebar_position: 1
slug: /php
---

# Guide

## Tutorial

### Change PHP Version on Linux{#changeversion}

#### PHP upgrade{#upgrade}

If you use Websoft9 LAMP/LNMP runtime, upgrade PHP by these steps:  

e.g: PHP5.6 to PHP7.0

1. Connect your Server and run these commands
    ```
    # disable the old PHP repo
    yum-config-manager --disable remi-php56  

    # enable the target PHP repo
    yum-config-manager --enable remi-php70     

    # Upgrade it
    yum update -y
    ```


2. Check the PHP version after upgrading
    ```
    php -v
    ```

#### PHP downgrade{#downgrade}

e.g: PHP7.0 to PHP5.6

```
# disable the old PHP repo
yum-config-manager --disable remi-php70

# enable the target PHP repo
yum-config-manager --enable remi-php56     

# uninstall all PHP installed packages
yum remove php-* -y

# Install target PHP and modules
yum -y install php-pecl-imagick php php-mysql php-common php-gd php-mbstring php-mcrypt php-devel php-xml php-pdo php-bcmath php-pear php-opcache php-ldap php-odbc php-xmlrpc php-json php-mysqlnd php-pdo php-pdo_dblib php-recode php-snmp php-soap php-pecl-zip php-curl php-imap

# Install other useful PHP packages by pear
pear install Mail
pear install net_smtp
```

### Change PHP Version on Windows{#versionwin}

Open the PHP Manager at IIS, change PHP version is very easy:  

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-changephpver-websoft9.png)


### Configure PHP{#config}

You can choose one of the options below to configure PHP:  

* **php.ini**: global scope
* **.htaccess**: site scope


### Web Framework{#framework}

#### Symfony{#symfony}
#### Laravel{#laravel}
#### CodeIgniter{#codeigniter}
#### ThinkPHP{#thinkphp}
#### Yii 2{#yii}

## Troubleshoot{#troubleshoot}

## Parameters

### Path{#path}

PHP configuration file: */etc/php.ini*   
PHP configuration file on Windows：*C:\websoft9\php-\*\php.ini*   
PHP Modules configurations directory: */etc/php.d*   

### CLI{#cmd}

* php
* composer
* pear

### Service{#service}

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