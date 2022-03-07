---
sidebar_position: 2
slug: /zentao/admin
tags:
  - ZenTao（禅道）
  - 项目管理
---

# 维护参考

## 系统参数

ZenTao 预装包包含 ZenTao 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### ZenTao

ZenTao 安装目录： */data/wwwroot/zentao*  
ZenTao 配置文件： */data/wwwroot/zentao/config/my.php*  

> ZenTao 配置文件中包含数据库连接信息，更改了 MySQL 数据库账号密码，此处也需要对应修改

#### PHP

PHP 配置文件： */etc/php.ini*  
PHP Modules 配置文件目录： */etc/php.d*

#### Apache

ZenTao on LAMP, the Web Server is Apache  

Apache 虚拟主机配置文件：*/etc/httpd/conf.d/vhost.conf*  
Apache 主配置文件： */etc/httpd/conf/httpd.conf*  
Apache 日志文件： */var/log/httpd*  
Apache 模块配置文件： */etc/httpd/conf.modules.d/00-base.conf*

#### Nginx

ZenTao on LEMP, the Web Server is Nginx  

Nginx 虚拟主机配置文件：*/etc/nginx/sites-available/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx/*

#### MYSQL

MySQL 安装路径: */usr/local/mysql*  
MySQL 数据文件 */data/mysql*  
MySQL 配置文件: */etc/my.cnf*    
MySQL 可视化管理地址: *http://服务器公网IP/phpmyadmin*，用户名和密码请见 [账号密码](/zh/stack-accounts.md) 章节。

#### phpMyAdmin

phpMyAdmin installation directory: */data/apps/phpmyadmin*  
phpMyAdmin configuration file: */data/apps/phpmyadmin/config.inc.php*   
phpMyAdmin vhost configuration file: */etc/httpd/conf.d/phpMyAdmin.conf* or */etc/nginx/php.conf*  

#### Redis

Redis configuration file: */etc/redis.conf*  
Redis data directory: */var/lib/redis*  
Redis logs file: */var/log/redis/redis.log*


### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

本应用建议开启的端口如下：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过 HTTP 访问 ZenTao | 必须 |
| HTTPS | 443 | 通过 HTTPS 访问 ZenTao | 可选 |
| MySQL | 3306 | 远程连接 MySQL | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

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

# Nginx version
nginx -v

# List Installed Nginx Modules
nginx -V

# MySQL version:
mysql -V

# Redis version
redis-server -v
```
### 服务

使用由Websoft9提供的 ZenTao 部署方案，可能需要用到的服务如下：

#### Apache

```shell
#For Centos&Redhat
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

#### Nginx

```shell
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
```

#### PHP-FPM
```shell
systemctl start php-fpm
systemctl stop php-fpm
systemctl restart php-fpm
systemctl status php-fpm
```

#### MySQL

```shell
sudo systemctl start mysql
sudo systemctl stop mysql
sudo systemctl restart mysql
sudo systemctl status mysql
```

#### Redis
```shell
sudo systemctl start redis
sudo systemctl stop redis
sudo systemctl restart redis
sudo systemctl status redis
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

1. 通过 WinSCP 将网站源码目录（*/data/wwwroot/zentao*）**压缩后**再完整的下载到本地
2. 通过 phpMyAdmin 导出 ZenTao 数据库
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)
3. 将程序文件、数据文件和数据库文件放到同一个文件夹，根据日期命名
4. 备份工作完成

### ZenTao 后台备份&恢复

ZenTao 后台提供了非常简单实用的在线备份功能，使用方法如下：

1. 登录 ZenTao 后台，打开：【管理】>【数据】，进入备份页面，设置备份策略。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-backupstr-websoft9.png)

2. 点击备份操作
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-backup-websoft9.png)

3. 在线实现的备份可以在线恢复（还原）

4. ZenTao 提供的回收站功能，也可以恢复手工删除的数据
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-recycle-websoft9.png)

## 恢复

## 升级

### 系统级更新

运行一条更新命令，即可完成系统级（包含rethinkdb小版本更新）更新：

``` shell
#For Ubuntu&Debian
apt update && apt upgrade -y

#For Centos&Redhat
yum update -y
```
> 本部署包已预配置一个用于自动更新的计划任务。如果希望去掉自动更新，请删除对应的 Cron


### ZenTao 升级

ZenTao 通过手工上传代码的方式进行升级。在升级之前请做好服务器的快照备份，这个是必须的步骤，因为谁都无法保证升级 100% 成功。

1. [下载](https://www.zentao.net/download.html)最新源码，解压
2. 上传并覆盖服务器上的 ZenTao 源码
3. 本地浏览器访问: *http://服务器公网IP/upgrade.php* 开始升级
4. 如果升级过程报错" Uncaught Error: Call to a member function query() on null in li..."，请给 `zentao/www` 和 `zentao/tmp` 目录递归加下777权限后再试

> 更多升级详情，请参考官方升级文档 [ZenTao 通过源代码方式升级(通用)](https://www.zentao.net/book/zentaopmshelp/67.html)


## 故障处理

此处收集使用 ZenTao 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### ZenTao 重定向错误？

重定向错误比较常见。处理办法：分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则

#### ZenTao 密码输入错误多次被锁，怎么解决？

1. 10分钟后会自动解锁。
2. 管理员登录，组织→用户 操作栏里有解锁按钮。

#### 修改了数据库密码 ZenTao 不能访问？

若已完成 ZenTao 安装向导，再通过 phpMyAdmin 修改数据库密码，ZenTao 就会连不上数据库  

需要修改 [ZenTao 配置文件](/zh/stack-components.html#zentao) 对应的数据库 password 参数即可。

#### Apache httpd 服务无法启动？

请通过分析日志文件定位原因： */var/log/httpd*

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```

## 常见问题

#### ZenTao 支持多语言吗？

支持中英文

#### ZenTao 开源版是免费的吗？

基于ZPL协议发布，源代码开放，不限商用。当然您也可以购买官方的[企业版、集团办](https://www.zentao.net/page/professional.html)等

#### 为什么要注册 ZenTao 官网账号？

[注册](https://www.zentao.net/user-register.html)官网账号，你可以将 ZenTao 系统与官网连接，在线安装插件。

#### ZenTao 提供客户端吗？

禅道手机客户端IOS版本和安卓版本， 专为禅道专业版和企业版用户提供。

#### ZenTao(LAMP)，ZenTao(LNMP)等商品括号中的 LAMP,LNMP 是什么意思？

LAMP和LNMP代表支持 ZenTao 运行所对应的基础环境，具体参考[环境说明](/zh/admin-runtime.html)

#### 是否可以使用云平台的 RDS 作为 ZenTao 的数据库？

可以，修改 [ZenTao 配置文件](/zh/stack-components.html#zentao) 即可

#### ZenTao能在 Windows 服务器上运行吗？

可以，但是我们推荐在运行 ZenTao 效率更高的 Linux 服务器上运行

#### ZenTao数据库连接配置信息在哪里？

数据库配置信息 [ZenTao 配置文件](/zh/stack-components.html#zentao)中

#### 如果没有域名是否可以部署 ZenTao？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP/phpmyadmin

#### 如何禁止phpMyAdmin访问？

连接服务器，编辑 phpMyAdmin 配置文件，将其中的 Require all granted 更改为 Require ip 192.160.1.0，然后重启 Apache 服务

#### 是否可以修改 ZenTao 的源码路径？

可以，通过修改 [虚拟主机配置文件](/zh/stack-components.md#zentao)中相关参数

#### 如何修改上传的文件权限?

```shell
#ZenTao(LAMP)
chown -R apache.apache /data/wwwroot

#ZenTao(LNMP)
chown -R nginx.nginx /data/wwwroot

find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```