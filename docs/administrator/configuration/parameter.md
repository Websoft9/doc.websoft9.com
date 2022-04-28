---
sidebar_position: 10
slug: /administrator/parameter
---

# 路径、端口和服务

Websoft9 将各个应用和组件的目录到一个约定的目录中，大大的简化了用户维护：  

## 目录与路径{#path}

由 Websoft9 约定了统一的**数据、日志和配置文件**存放目录：

* */data/wwwroot/appname*  存放应用本体，appname 即应用名称，例如：wordpress
* */data/apps* 存放应用所需的支持工具，例如 phpmyadmin
* */data/db* 数据库统一目录，例如 mysql
* */data/config* 配置统一目录，例如 Apache  配置
* */data/logs* 配置统一目录，例如 网站日志

运行 `whereis` 命令可以查看原始的安装路径。  

## 端口{#port}

用户可以通过 `netstat -tunlp` 查看服务器上已经用到的端口。      

下面是最常见的端口，请根据实际情况到安全组中 **开启或关闭** 它们：

### 应用访问

| 端口号 | 用途 |  必要性 |
| --- | --- | --- |
| 80 | 通过 HTTP 访问 应用 | 可选 |
| 443 | 通过 HTTPS 访问 应用 | 可选 |

### 服务器连接

| 端口号 | 用途 |  必要性 |
| --- | --- | --- |
| 21 | Linux 服务器 FTP 端口 | 可选 |
| 22 | Linux 服务器 SSH 端口 | 可选 |
| 3389 | Windows 服务器 RDP 端口 | 可选 |

### 数据库管理

参考：[可视化管理数据库](../user/dbgui)


## 服务{#service}

在应用的维护和配置中，可能涉及到服务的启动，停止，重启，状态查询等操作。  

Websoft9 应用中有基于 Systemd 和 Docker 的两种类型的服务。   

### Systemd 服务

```
sudo systemctl start | top | restart | status docker
sudo systemctl start | top | restart | status apache
sudo systemctl start | top | restart | status nginx
sudo systemctl start | top | restart | status mysql
sudo systemctl start | top | restart | status php-fpm
sudo systemctl start | top | restart | status postgresql
sudo systemctl start | top | restart | status mongod
```

### Docker 服务

我们此处约定 Docker 服务等同于每一个运行中的容器。所以，只需运行 `sudo docker ps -a` 可以查看所有 Docker 的服务。  

下面是常见的 Docker 服务

```
$ sudo docker start | stop | restart | stats container_name

# 数据库 GUI 工具
sudo docker start | stop | restart | stats phpmyadmin
sudo docker start | stop | restart | stats adminmongo
sudo docker start | stop | restart | stats pgadmin

# 数据库
sudo docker start | stop | restart | stats mysql
sudo docker start | stop | restart | stats postgresql
sudo docker start | stop | restart | stats redis
sudo docker start | stop | restart | stats sqlite
sudo docker start | stop | restart | stats memcached
```


## 版本{#version}

虽然产品页面可查看版本，但您服务器中的组件可能会不断升级，故精准的版本号请通过在服务器上运行命令查看：

##### 通用

```
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Docker version
docker -v
```

##### 数据库

```
# MongoDB version
mongo --version

# PostgreSQL version:
psql --version

# MySQL version
mysql -V

# Redis version
redis-server -v

```

##### Web 服务器

```
# Apache version on Centos
httpd -v

# Apache version on Ubuntu
apache2 -v

# List Installed Apache Modules
apachectl -M

# Nginx version
nginx -v

# List Installed Nginx Modules
nginx -V

```

##### 程序环境

```
# Java version
java -v

# PHP Version
php -v

# List Installed PHP Modules
php -m

# Node.js  Version
node -v

# PM2  Version
pm2 -V

# NPM version
npm -v

# yarn version
yarn --version
```
