---
sidebar_position: 5
slug: /setup/parameter
---

# 参数速查

Websoft9 将各个应用和组件的目录到一个约定的目录中，大大的简化了用户维护：  

## 目录与路径{#path}

由 Websoft9 提供的应用，规划了统一的**数据、日志和配置文件**存放目录：

* */data/wwwroot/appname*  存放应用本体，appname 即应用名称，例如：wordpress
* */data/apps* 存放应用所需的支持工具，例如 phpmyadmin
* */data/db* 数据库统一目录，例如 mysql
* */data/config* 配置统一目录，例如 Apache  配置
* */data/logs* 配置统一目录，例如 网站日志

## 端口{#port}

下面是大部分应用都需要用到的端口，请根据实际情况到安全组中 **开启或关闭** 它们：

| 端口号 | 用途 |  必要性 |
| --- | --- | --- |
| 80 | 通过 HTTP 访问 Jenkins | 可选 |
| 443 | 通过 HTTPS 访问 Jenkins | 可选 |
| 22 | Linux 服务器 SSH 端口 | 可选 |
| 3389 | Windows 服务器 RDP 端口 | 可选 |
| 9090/9091 | 数据库可视化界面端口 | 可选 |

## 服务{#service}

Linux 系统中，服务主要是通过 `systemcl` 命令进行管理（启动，停止，重启，状态）。

比较常见的服务包括：  

```
sudo systemctl start | top | restart | status docker
sudo systemctl start | top | restart | status apache
sudo systemctl start | top | restart | status nginx
sudo systemctl start | top | restart | status mysql
```

## 版本{#version}

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# MongoDB version
mongo --version

# MySQL version
mysql -V

# Redis version
redis-server -v


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


# Docker version
docker -v

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