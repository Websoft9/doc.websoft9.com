---
sidebar_position: 2
slug: /vtiger/admin
tags:
  - VtigerCRM
  - CRM
  - 客户成功
---

# 维护参考

## 系统参数

VtigerCRM 预装包包含 VtigerCRM（LAMP） 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### 网站目录

根目录： *LAMP 环境中，你的网站代码存放位置是没有限制的，因此没有根目录的说法*  
网站存放目录（建议）： */data/wwwroot*  
网站目录： */data/wwwroot/VtigerCRM*  

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
MySQL 可视化管理地址: *http://服务器公网IP/phpmyadmin* 用户名和密码请见 [账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html) 章节。

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

使用由 Websoft9 提供的 LAMP 部署方案，可能需要用到的服务如下：

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
2. 通过 phpMyAdmin 导出 VtigerCRM 数据库
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)
3. 将程序文件和数据库文件放到同一个文件夹，根据日期命名
4. 备份工作完成


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


### VtigerCRM 如何升级

当镜像版本不是官方发布的最新版本的时候，有些用户朋友就有升级需求（虽然升级不是必要的）。VtigerCRM自身提供了升级功能，具体操作如下：

1. 到 VtigerCRM 官网[下载升级包](https://www.vtiger.com/open-source-crm/download-open-source/)（注意：是升级包，不是最新的软件包）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-dlupgradepack-websoft9.png)
   
   > 如果下载不到匹配的升级包，升级就无法进行。
  
2. 将下载包解压后，通过 SFTP 上传到 VtigerCRM 根目录（*data/wwwroot/defualt/vtigercrm*）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-unzippatch-websoft9.png)

3. 运行一条修改文件权限的命令：
    ~~~
    chown -R apache.apache /data/wwwroot
    ~~~
4.  浏览器访问：http://域名或IP地址/migrate 开始升级流程

> 升级之前请备份好网站代码和数据库，这是常识哦

以上方案是Websoft9对[VtigerCRM官方升级文档](http://community.vtiger.com/help/vtigercrm/administrators/migration.html)的解读，建议同时阅读官方提供的升级文档


## 故障处理

此处收集使用 VtigerCRM 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 更换服务器IP，VtigerCRM 无法访问？错误信息：*Invalid compiled template for 'modules/Install/Header.tpl'*

问题原因：VtigerCRM 启动后会生成一个记录服务器IP地址的缓存文件  
解决方案：使用下面的命令删除缓存文件

```
- rm -rf /data/wwwroot/vtigercrm/test/templates_c/v7
- rm -rf /data/wwwroot/vtigercrm/cache/*
```

#### 网站显示重定向错误？

检查网站根目录下的 *.htaccess* 文件，分析其中的重定向规则，找到其中的死循环。

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看 MySQL 状态
sudo systemctl status mysql
sudo journalctl -u mysql
```

#### 数据库日志文件太大，导致磁盘空间不足？

默认安装，mysql会自动开启binlog，binlog是一个二进制格式的文件，用于记录用户对数据库**更新的****SQL语句****信息**，例如更改数据库表和更改内容的SQL语句都会记录到binlog里。

binlog主要用于出现没有备份的情况下，恢复数据库。但binlog会占用较大空间，长期不清理会让剩余磁盘空间为0，从而影响数据库或服务器无法启动

如果对自己的备份有信心，不需要binlog功能，参考如下步骤关闭之：

1. 编辑 [MySQL 配置文件](/zh/stack-components.md#mysql)，注释掉 binlog 日志
  ~~~
  #log-bin=mysql-bin  
  ~~~
2. 重启mysql
  ~~~
  systemctl restart mysqld
  ~~~

#### 重启 Apache 服务显示 *No spaces...*

出现此信息的时候，重启服务是成功的。

解决方案:

```
echo "fs.inotify.max_user_watches=262144" >> /etc/sysctl.conf 

sysctl -p
```

#### 运行命令 `httpd -t` 报错 [so:warn] [pid 14645] AH01574: module ssl_module is already loaded

问题原因：mod_ssl 重复加载  
解决方案：检查下面两个文件，找到 mod_ssl 字段，注释其中一个

  * /etc/httpd/conf.modules.d/00-base.conf
  * /etc/httpd/conf.modules.d/00-ssl.conf 


## 常见问题

#### 默认字符集是什么？
UTF-8

#### Apache工作模式有event,prefork,worker等，LAMP 默认是哪个？
prefork

#### Apache 虚拟主机配置文件是什么？

虚拟主机配置文件是 Apache 用于管理多个网站的**配置段集合**，路径为：*/etc/httpd/conf.d/vhost.conf*。  
每个配置段的形式为： `<VirtualHost *:80> ...</VirtualHost>`，有多少个网站就有多少个配置段

#### 如何修改示例网站根目录？

示例网站路径信息 */data/wwwroot/www.example.com* 存放在 [Apache 虚拟主机配置文件](/zh/stack-components.md#apache)中

#### LAMP 环境是否支持部署多个网站？

支持。每增加一个网站，只需在[Apache 虚拟主机配置文件](/zh/stack-components.md#apache)中增加对应的  VirtualHost 即可。

#### 如果没有域名是否可以部署 LAMP？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：*http://服务器公网IP:9090*

#### 如何禁止外界访问phpMyAdmin？

```
sudo docker stop phpmyadmin
```

#### 网站源码路径如何修改？

通过修改 [Apache 虚拟主机配置文件](/zh/stack-components.md#apache) 中相关路径参数

#### 如何删除9Panel?

删除 */data/apps/9panel* 下的所有数据即可，但需要保留文件夹

#### 通过 SFTP 上传网站源码后是否需要修改拥有者权限？

不需要，LAMP 会自动修正

#### 如何重置 php.ini 文件？

[下载 php.ini 模板](https://github.com/Websoft9/ansible-lamp/blob/master/roles/php/templates/php.ini) 后覆盖你服务器上的 */ect/php.ini*

#### 如何取消 Apache Test 页面？

使用 # 号将: */etc/httpd/conf.d/welcome.conf* 中的所有内容全部注释掉，然后重启 Apache 服务

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R apache.apache /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```
#### 如何拒绝用户通过IP访问服务器？

编辑你的php主文件*httpd.conf*，增加下面的一段代码，保存然后重启服务即可

```
   <VirtualHost *:80>
       ServerName 47.105.50.140
   <Location />
       Order Allow,Deny
       Deny from all
   </Location>
   </VirtualHost>
   
    <VirtualHost *:443>
   ServerName 47.105.50.140
   SSLEngine on
   SSLCertificateFile /etc/pki/tls/certs/localhost.crt
   SSLCertificateKeyFile /etc/pki/tls/private/localhost.key
   <Location />
   Order Allow,Deny
   Deny from all
   </Location>
   </VirtualHost>

```
#### 如果设置 HTTP 跳转到 HTTPS？

建议在网站根目录下的.htacesss文件中增加redirect规则，参考如下：
```
RewriteEngine on
RewriteBase /
RewriteCond %{SERVER_PORT} !^443$
RewriteRule ^.*$ https://%{SERVER_NAME}%{REQUEST_URI} [L,R]
```

从 non-www 到 www 配置：

```
RewriteEngine on
RewriteCond %{HTTP_HOST} ^example.com [NC]
RewriteRule ^(.*)$ http://www.example.com/$1 [L,R=301,NC]
```
从 www 到 non-www：
```
RewriteEngine on
RewriteCond %{HTTP_HOST} ^www.example.com [NC]
RewriteRule ^(.*)$ http://example.com/$1 [L,R=301,NC]

```

#### LAMP 是否安装了mod_php模块，Apache服务器怎么解析PHP文件？ 
LAMP 默认安装了mod_php模块，并且已经已经启用。Apache服务器通过php-fpm服务来解析PHP文件，如果想用mod_php解析PHP文件，请参照 [PHP文件解析方式变更](/zh/solution-more.md#PHP文件解析方式变更)

#### LAMP 默认安装了哪些 Apache模块？ 

运行命令 `apachectl -M` 查看

#### LAMP 默认安装了哪些 PHP 模块？

运行命令 `php -m` 查看

#### 如何启用或禁用 Apache 模块？

以伪静态模块为例。打开 [Apache模块配置文件](/zh/stack-components.md#apache)，找到 *LoadModule rewrite_module modules/mod_rewrite.so*，通过“#”作为注释来开启或禁用此模块

#### 如何禁用IP访问网站，防止恶意解析？

参考 [Apache 相关配置文档](https://support.websoft9.com/docs/linux/zh/webs-apache.html#禁用ip访问-防止恶意解析)

#### 没有域名是否可以通过 http://公网IP/mysite1 这样的方式访问网站？

可以。具体配置方法参考 [安装网站](/zh/solution-deployment.md#安装第二个网站)