---
sidebar_position: 2
slug: /owncloud/admin
tags:
  - ownCloud
  - 网盘
  - 知识管理
  - 团队协作
---

# 维护参考

## 系统参数

ownCloud 预装包包含 ownCloud 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### ownCloud

ownCloud 安装目录： */data/wwwroot/owncloud*  
ownCloud 配置文件： */data/wwwroot/owncloud/config/config.php*  

> ownCloud 配置文件中包含数据库连接信息，更改了 MySQL 数据库账号密码，此处也需要对应修改

#### PHP

PHP 配置文件： */etc/php.ini*  
PHP Modules 配置文件目录： */etc/php.d*

#### Apache

ownCloud on LAMP, the Web Server is Apache  

Apache 虚拟主机配置文件：*/etc/httpd/conf.d/vhost.conf*  
Apache 主配置文件： */etc/httpd/conf/httpd.conf*  
Apache 日志文件： */var/log/httpd*  
Apache 模块配置文件： */etc/httpd/conf.modules.d/00-base.conf*

#### Nginx

ownCloud on LEMP, the Web Server is Nginx  

Nginx 虚拟主机配置文件：*/etc/nginx/sites-available/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx/*

#### MYSQL

MySQL 安装路径: */usr/local/mysql*  
MySQL 数据文件 */data/mysql*  
MySQL 配置文件: */etc/my.cnf*    

MySQL 可视化管理参考：[MySQL管理](/zh/admin-mysql.md) 章节。

#### Docker

基于 Docker 安装了如下辅助工具：

#### OnlyOffice Document Server

OnlyOffice Document Server directory：*/data/apps/onlyofficedocumentserver*  
phpMyAdmin docker compose file：*/data/apps/onlyofficedocumentserver/docker-compose.yml*  

####  phpMyAdmin

phpMyAdmin directory：*/data/apps/phpmyadmin*  
phpMyAdmin docker compose file：*/data/apps/phpmyadmin/docker-compose.yml*  


#### Redis

Redis configuration file: */etc/redis.conf*  
Redis data directory: */var/lib/redis*  
Redis logs file: */var/log/redis/redis.log*


### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

本应用建议开启的端口如下：

| 类型 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 80 | 通过 HTTP 访问 ownCloud | 必须 |
| TCP | 443 | 通过 HTTPS 访问 ownCloud | 可选 |
| TCP | 3306 | 远程连接 MySQL | 可选 |
| TCP | 9002 | OnlyOffice Document Server on Docker | 可选 |
| TCP | 9090 | phpMyAdmin on Docker | 可选 |

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

# Dokcer:
docker --version
```


### 服务

使用由Websoft9提供的 ownCloud 部署方案，可能需要用到的服务如下：

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

#### Docker
```shell
sudo systemctl start docker
sudo systemctl stop docker
sudo systemctl restart docker
sudo systemctl status docker
```

#### phpMyAdmin on Docker
```shell
sudo docker inspect phpmyadmin
sudo docker start phpmyadmin
sudo docker restart phpmyadmin
sudo docker stop phpmyadmin
sudo docker rm phpmyadmin
```

#### ONLYOFFICE Document Server on Docker
```shell
sudo docker inspect onlyofficedocumentserver
sudo docker start onlyofficedocumentserver
sudo docker restart onlyofficedocumentserver
sudo docker stop onlyofficedocumentserver
sudo docker rm onlyofficedocumentserver
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

1. 通过 WinSCP 将网站源码目录（*/data/wwwroot/owncloud*）**压缩后**再完整的下载到本地
1. 通过 WinSCP 将网站数据目录（*/data/wwwroot/owncloud/data*）**压缩后**再完整的下载到本地
2. 通过 phpMyAdmin 导出 ownCloud 数据库
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)
3. 将程序文件、数据文件和数据库文件放到同一个文件夹，根据日期命名
4. 备份工作完成

### ownCloud 后台备份

ownCloud 后台提供在线备份功能

1. 登录 ownCloud 后台，安装 **[OwnBackup](https://en.websoft9.com/xdocs/owncloud-image-guide/#using-apps)** 插件
2. 打开：【Admin】>【OwnBackup】，开始备份
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-ownbackup-websoft9.png)
3. 此插件也可以用于恢复
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-restore-websoft9.png)

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


### ownCloud 升级

ownCloud提供了非常人性化的升级入口，根据系统的更新提示既可以完成主版本、插件的更新。

> 在升级之前请做好服务器的快照备份，这个是必须的步骤，因为谁都无法保证升级100%成功。

#### 插件升级

升级步骤参加如下：

1. 登录 OwnCloud 之后查看右上角是否有更新通知，若有，请点击其中的更新条目
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-updatenotify-websoft9.png)

2. 点击更新条目后 或 访问：*http://域名/index.php/apps/market/#/updates*  进入更新界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-updatelist-websoft9.png)

3. 点击【更新】按钮，系统进入【UPDATING】，耐心等待更新
4. 所有更新完成后，更新清单会显示“所有应用都是最新的”

> 如果升级过程出现问题，例如：无法下载升级包/没有读写权限，请确保网络是通的/OwnCloud目录具有读写权限


#### 主程序升级

主程序升级与插件升级略有差异，具体参考如下：

1. 当有可用升级的程序时，系统提示“ownCloud is available. Get more information ...”
2. 依次打开：Admin->设置->常规，找到更新管理器，若有更新请点击“打开更新管理器”按钮
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-openupdater-websoft9.png)
3. 进入 Updater（更新管理器）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-updater-websoft9.png)
4. 点击【Create a checkpoint】，创建一个核心文件备份
5. 点击【Start】按钮，系统进入自动化升级过程，下载和升级过程比较长，请耐心等待
6. 升级成功提示

> 由于升级过程会下载最新版本，ownCloud的下载服务器在国外，若下载不成功，需要不定期尝试

## 故障处理

此处收集使用 ownCloud 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### ownCloud 重定向错误？

多语言下，重定向错误比较常见。例如：打开您的ownCloud商店中文版会出现重定向

处理办法：
1. 分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则
2. 进入后台先删除中文，然后再重新导入中文。重新导入的时候，ownCloud会自动生成伪静态规则，覆盖您网站根目录的 `.htaccess` 文件

####  域名配置后，会出现“页面布局混乱或图片无法显示”？

如果先通过 IP 安装，再绑定域名，就会出现这个问题，请分别打开 ownCloud 的[配置文件](/zh/stack-components.html#owncloud)，将其中的IP地址改成域名。

#### 安装插件，显示403权限不足，错误"you dont have permession to access /admin/index.php"

修改文件：/etc/httpd/conf.d/mod\_evasive.conf 中  DOSPageCount 2 改为 DOSPageCount 12

#### 修改了数据库密码 ownCloud 不能访问？

若已完成 ownCloud 安装向导，再通过 phpMyAdmin 修改数据库密码，ownCloud 就会连不上数据库  

需要修改 [ownCloud 配置文件](/zh/stack-components.html#owncloud) 对应的数据库 password 参数即可。

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

#### 您正在访问来自不信任域名的服务器？

错误：您正在访问来自不信任域名的服务器，请联系你的系统管理员。如果你是系统管理员，配置 config/config.php 文件中参数 "trusted_domain" 设置。  
原因：您的 ownCloud 服务器IP地址发生变化，而配置文件还是旧的IP地址。  
方案：编辑 ownCloud 根目录下的 *config/config.php* 配置文件，修改其中的IP地址信息：  

```
  'trusted_domains' => 
  array (
    0 => '8.210.158.103',
  ),
```

## 常见问题

#### ownCloud 支持多语言吗？

支持多语言（包含中文）

#### ownCloud 是否提供客户端？

有。包括：ownCloud Desktop Client, ownCloud Android App, ownCloud iOS App

#### ownCloud 自身能够预览和编辑 Office 文档吗？

不可以，需要连接第三方的文档编辑和服务才可以，参考：[文件预览与编辑设置](/zh/solution-more.html#owncloud-文件预览与编辑)

#### ownCloud 支持集成外部存储吗？

支持多种主流外部存储服务

#### 为什么在云厂商购买的云存储空间和ownCloud 显示不一致 ？

需要进入用户管理，设置该用户的配额为*无限*
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-setting-websoft9.png)

#### ownCloud(LAMP)，ownCloud(LNMP)等商品括号中的 LAMP,LNMP 是什么意思？

LAMP和LNMP代表支持 ownCloud 运行所对应的基础环境，具体参考[环境说明](/zh/admin-runtime.html)

#### 是否可以使用云平台的 RDS 作为 ownCloud 的数据库？

可以，修改 [ownCloud 配置文件](/zh/stack-components.html#owncloud) 即可

#### ownCloud能在Windows服务器上运行吗？

可以，但是我们推荐在运行 ownCloud 效率更高的 Linux 服务器上运行

#### ownCloud数据库连接配置信息在哪里？

数据库配置信息 [ownCloud 配置文件](/zh/stack-components.html#owncloud)中

#### 如果没有域名是否可以部署 ownCloud？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP/phpmyadmin

#### 如何禁止phpMyAdmin访问？

连接服务器，编辑 phpMyAdmin 配置文件，将其中的 Require all granted 更改为 Require ip 192.160.1.0，然后重启 Apache 服务

#### 是否可以修改 ownCloud 的源码路径？

可以，通过修改 [虚拟主机配置文件](/zh/stack-components.md#owncloud)中相关参数

#### 如何修改上传的文件权限?

```shell
#ownCloud(LAMP)
chown -R apache.apache /data/wwwroot

#ownCloud(LEMP)
chown -R nginx.nginx /data/wwwroot

find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```

