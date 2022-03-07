---
sidebar_position: 2
slug: /typo3/admin
tags:
  - Typo3
  - CMS
  - 站点管理
---

# 维护参考

## 系统参数

Typo3 预装包包含 Typo3 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### 网站目录

根目录： *LAMP 环境中，你的网站代码存放位置是没有限制的，因此没有根目录的说法*  
网站存放目录（建议）： */data/wwwroot*  
网站目录： */data/wwwroot/typo3*  

> 通过 *http://公网IP地址* 访问的就是示例网站 

#### Apache

Apache 虚拟主机配置文件：*/etc/httpd/conf.d/vhost.conf*  
Apache 主配置文件： */etc/httpd/conf/httpd.conf*  
Apache 日志文件： */var/log/httpd*  
Apache 模块配置文件： */etc/httpd/conf.modules.d/00-base.conf*

**vhost.conf** 默认存在一个 [VirtualHost（虚拟主机）](https://support.websoft9.com/docs/linux/zh/webs-apache.html#虚拟主机) 配置项，对应的就是 **示例网站**
```
<VirtualHost *:80>
ServerName www.mydomain.com
ServerAlias other.mydomain.com
DocumentRoot "/data/wwwroot/www.example.com"
ErrorLog "/var/log/httpd/www.mydomain.com_error_apache.log"
CustomLog "/var/log/httpd/www.mydomain.com_apache.log" common
<Directory "/data/wwwroot/www.example.com">
Options Indexes FollowSymlinks
AllowOverride All
Require all granted
</Directory>
</VirtualHost>
```

> 有多少个网站，就需要在 vhost.conf 中增加同等数量的 VirtualHost 配置项

#### PHP

PHP 配置文件： */etc/php.ini*  
PHP Modules 配置文件目录： */etc/php.d*
```
# 默认已安装的 PHP Modules
Core  date  libxml  openssl  pcre  zlib  filter  hash  Reflection  SPL  session  standard  apache2handler  
bcmath  bz2  calendar  ctype  curl  dom  mbstring  fileinfo  ftp  gd  gettext  gmp  iconv  
imap  intl  json  ldap  exif  mcrypt  mysqlnd  odbc  PDO  Phar  posix  recode  shmop  
SimpleXML  snmp  soap  sockets  sqlite3  sysvmsg  sysvsem  sysvshm  tokenizer  xml  xmlwriter  xsl  mysqli  
pdo_dblib  pdo_mysql  PDO_ODBC  pdo_sqlite  wddx  xmlreader  xmlrpc  igbinary  imagick  zip  redis  Zend OPcache  
```

#### MYSQL

MySQL 安装路径: */usr/local/mysql*  
MySQL 数据文件 */data/mysql*  
MySQL 配置文件: */etc/my.cnf*    
MySQL 可视化管理地址: *http://服务器公网IP/phpmyadmin* 用户名和密码请见 [账号密码](/快速入门.md#账号密码) 章节。

#### phpMyAdmin

phpMyAdmin 是一款可视化 MySQL 管理工具，在本项目中它基于 Docker 安装。  

phpMyAdmin directory：*/data/apps/phpmyadmin*  
phpMyAdmin docker compose file：*/data/apps/phpmyadmin/docker-compose.yml* 

#### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   
Docker daemon.json 文件：默认没有创建，请到 */etc/docker* 目录下根据需要自行创建  

#### Redis

Redis 配置文件： */etc/redis.conf*  
Redis 数据目录： */var/lib/redis*  
Redis 日志文件： */var/log/redis/redis.log*

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

本环境建议开启的端口如下：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过 HTTP 访问网站 | 必须 |
| HTTPS | 443 | 通过 HTTP 访问网站 | 可选 |
| MySQL | 3306 | 本地电脑远程连接服务器上的 MySQL | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Linux Version
lsb_release -a

# PHP Version
php -v

# List Installed PHP Modules
php -m

# Apache version on Centos
httpd -v

# Apache version on Ubuntu
apache2 -v

# List Installed Apache Modules
apachectl -M

# MySQL version
mysql -V

# Redis version
redis-server -v
```


### 服务

使用由 Websoft9 提供的 KodCloud 部署方案，可能需要用到的服务如下：

### Apache

```shell
#For CentOS&Redhat
sudo systemctl start httpd
sudo systemctl stop httpd
sudo systemctl restart httpd
sudo systemctl status httpd

#For Ubuntu&Debian
sudo systemctl start apache2
sudo systemctl stop apache2
sudo systemctl restart apache2
sudo systemctl status apache2
```

### PHP-FPM
```shell
sudo systemctl start php-fpm
sudo systemctl stop php-fpm
sudo systemctl restart php-fpm
sudo systemctl status php-fpm
```

### MySQL

```shell
sudo systemctl start mysql
sudo systemctl stop mysql
sudo systemctl restart mysql
sudo systemctl status mysql
```

### Redis

```shell
sudo systemctl start redis
sudo systemctl stop redis
sudo systemctl restart redis
sudo systemctl status redis
```

### phpMyAdmin

```shell
sudo docker start phpmyadmin
sudo docker stop phpmyadmin
sudo docker restart phpmyadmin
sudo docker stats pgadmin
```

### Docker

```shell
sudo systemctl start docker
sudo systemctl restart docker
sudo systemctl stop docker
sudo systemctl status docker
```

## 备份

### 全局自动备份

所有的云平台都提供了全局自动备份功能，基本原理是基于**磁盘快照**：快照是针对于服务器的磁盘来说的，它可以记录磁盘在指定时间点的数据，将其全部备份起来，并可以实现一键恢复。

```
- 备份范围: 将操作系统、运行环境、数据库和应用程序
- 备份效果: 非常好
- 备份频率: 按小时、天、周备份均可
- 恢复方式: 云平台一键恢复
- 技能要求：非常容易
- 自动化：设置策略后全自动备份
```

不同云平台的自动备份方案有一定的差异，详情参考 [云平台备份方案](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

### 程序手工备份

程序手工本地备份是通过**下载应用程序源码和导出数据库文件**实现最小化的备份方案。

下面以列表的方式介绍这种备份：
```
- 备份范围: 数据库和应用程序
- 备份效果: 一般
- 备份频率: 一周最低1次，备份保留30天
- 恢复方式: 重新导入
- 技能要求：非常容易
- 自动化：无
```
通用的手动备份操作步骤如下：

1. 通过 WinSCP 将网站目录（*/data/wwwroot/*）**压缩后**再完整的下载到本地
2. 通过 phpMyAdmin 导出 cells 数据库
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)
3. 将程序文件和数据库文件放到同一个文件夹，根据日期命名
4. 备份工作完成


## 恢复

## 升级

### 系统级更新

运行一条更新命令，即可完成系统级更新：

``` shell
#For Ubuntu&Debian
apt update && apt upgrade -y

#For Centos&Redhat
yum update -y
```
> 本部署包已预配置一个用于自动更新的计划任务。如果希望去掉自动更新，请删除对应的 Cron

### Typo3 程序升级

Typo3 后台提供了在线升级功能，升级非常容易：

1. 登录 Typo3后台，打开【ADMIN TOOLS】> 【Upgrade】
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-upgrade-websoft9.png)
   
2. 根据升级向导开始升级


## 故障处理

此处收集使用 Typo3 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
