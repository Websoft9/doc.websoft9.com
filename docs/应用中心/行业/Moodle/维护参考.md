---
sidebar_position: 2
slug: /moodle/admin
tags:
  - Moodle
  - 在线学习管理
---

# 维护参考

## 系统参数

Moodle 预装包包含 Moodle 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

### Moodle

Moodle 安装目录： */data/wwwroot/moodle*  
Moodle 配置文件： */data/wwwroot/moodle/config.php*  

> Moodle 配置文件中包含数据库连接信息，更改了 MySQL 数据库账号密码，此处也需要对应修改

#### PHP

PHP 配置文件： */etc/php.ini*  
PHP Modules 配置文件目录： */etc/php.d*

#### Apache

Moodle on LAMP, the Web Server is Apache  

Apache 虚拟主机配置文件：*/etc/httpd/conf.d/vhost.conf*  
Apache 主配置文件： */etc/httpd/conf/httpd.conf*  
Apache 日志文件： */var/log/httpd*  
Apache 模块配置文件： */etc/httpd/conf.modules.d/00-base.conf*

#### Nginx

Moodle on LEMP, the Web Server is Nginx  

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
| HTTP | 80 | 通过 HTTP 访问 Moodle | 必须 |
| HTTPS | 443 | 通过 HTTPS 访问 Moodle | 可选 |
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

使用由Websoft9提供的Moodle部署方案，可能需要用到的服务如下：

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
sudo systemctl star redis
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

1. 通过 WinSCP 将网站目录（*/data/wwwroot/moodle*）**压缩后**再完整的下载到本地
2. 通过 WinSCP 将数据目录（*/data/wwwroot/moodledata*）**压缩后**再完整的下载到本地
3. 通过 phpMyAdmin 导出 Moodle 数据库
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)
4. 将程序文件、数据文件和数据库文件放到同一个文件夹，根据日期命名
5. 备份工作完成

### Moodle 课程备份

课程是 Moodle 最重要的资源，Moodle 后台提供了自动备份课程的功能

1. 以管理员身份登录 Moodle 后台
2. 依次打开：【网站管理】>【课程】>【备份】，开始进行备份设置
  ![Moodle 课程备份](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-coursebk-websoft9.png)
3. 详细设置请自行研究
4. 依次打开：【网站管理】>【报表】>【备份】，查看备份执行情况
  ![Moodle 查看备份](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-coursebkrp-websoft9.png)


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


### Moodle升级

Moodle 官方提供了多种升级方式（[Moodle Upgrading](https://docs.moodle.org/37/en/Upgrading)），包括上传代码升级和命令升级等方式。  

下面我们以命令行升级方式为例，介绍升级的大致方案：

1. 提前做好代码和数据库备份

2. 使用 SSH 远程登录到 Moodle 服务器，运行如下的命令开始升级：
   ```
   cd /data/wwwroot/moodle/admin/cli
   php upgrade.php
   ```
3. 等待升级完成


## 故障处理

此处收集使用 Moodle 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
systemctl status mysql
```

#### 修复数据库错误

出现数据库需要修复的提示，请参考下面的命令修复对应的数据库表  

```
#mysqlcheck -u moodleuser -p --auto-repair moodle
Enter password:
moodle.adodb_logsql                      OK
moodle.mdl_assignment                    OK
moodle.mdl_assignment_submissions        OK
...
moodle.mdl_log
error    : Table './moodle/mdl_log' is marked as crashed and should be repaired
...
moodle.mdl_sessions2
error    : Table './moodle/mdl_sessions2' is marked as crashed and should be repaired

Repairing tables
moodle_18_latest.mdl_log                           OK
moodle_18_latest.mdl_sessions2                     OK
```

## 常见问题

#### Moodle 支持多语言吗？

支持多语言（包含中文），后台可以设置语言

#### Moodle 支持在线安装插件吗？

支持，类似 Wordpress 在线安装插件，不过 Moodle 需要提前到官方注册一个账号

#### Moodle 能上传多媒体文件吗？

可以

#### Moodle(LAMP)，Moodle(LNMP)等商品括号中的 LAMP,LNMP 是什么意思？

LAMP和LNMP代表支持Moodle运行所对应的基础环境，具体参考[环境说明](/zh/admin-runtime.html)

#### 是否可以使用云平台的 RDS 作为 Moodle 的数据库？

可以，修改 Moodle 根目录下的配置文件 `config.php` 即可

#### Moodle能在Windows服务器上运行吗？

可以，但是我们推荐在运行 Moodle 效率更高的 Linux 服务器上运行

#### Moodle数据库连接配置信息在哪里？

数据库配置信息在Moodle安装目录下的 *config.php* 中，[查阅安装目录路径](/zh/stack-components.md#moodle)

#### 如果没有域名是否可以部署 Moodle？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP/phpmyadmin

#### 如何禁止phpMyAdmin访问？

连接服务器，编辑 phpMyAdmin 配置文件，将其中的 Require all granted 更改为 Require ip 192.160.1.0，然后重启 Apache 服务

#### 是否可以修改Moodle的源码路径？

可以，通过修改 [虚拟主机配置文件](/zh/stack-components.md#moodle)中相关参数

#### 如何修改上传的文件权限?

```shell
#Moodle(LAMP)
chown -R apache.apache /data/wwwroot

#Moodle(LEMP)
chown -R nginx.nginx /data/wwwroot

find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```
