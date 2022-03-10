---
sidebar_position: 1
slug: /php
---

# 指南

## 场景

### PHP版本升级

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

### PHP 版本降级

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

### 引入包

包则是直接引入通过 require/include 方式加载

### php.ini 修改

对 PHP 来说，配置主要通过修改`php.ini`文件来实现。

当我们在运行PHP应用的时候，常常会碰到类似提示 **“超过最大的文件大小”**, **“运行超时”**, **“超过内存限制”**等，这个时候就需要php.ini来进行最大值的调整。

以CentOS上的PHP为例，php.ini路径为：/etc/php.ini

```shell
# 修改文件大小限制，注意数字后面需要带上单位M
post_max_size = 16M
upload_max_filesize = 16M

# 修改超时时间限制
max_execution_time = 90

# 修改内存限制
memory_limit – Minimum: 256M
```

### PHP-FPM 使用{#fpm}

PHP-FPM 用于管理 PHP 进程池，接受 Apache/Nginx 等 Web 服务器的请求。PHP-FPM 提供了更好的 PHP 进程管理方式，可以有效控制内存和进程、可以平滑重载 PHP 配置。

## 参数

### 路径{#path}

配置文件：*/etc/php.ini*  

### 命令行

主要有 php 和 composer 两个命令行

### 服务

```
#Linux
sudo systemctl start php
sudo systemctl stop php
sudo systemctl restart php
sudo systemctl status php

# Docker
sudo docker start php
sudo docker stop php
sudo docker restart php
sudo docker stats php
```