---
sidebar_position: 2
slug: /lnmp/admin
tags:
  - LNMP
  - PHP
  - Nginx
  - 运行环境
---


# 维护参考

## 系统参数

LNMP 预装包包含 LNMP 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### 网站目录

根目录： *LNMP 环境中，你的网站代码存放位置是没有限制的，因此没有根目录的说法*  
网站存放目录（建议）： */data/wwwroot*  
示例网站目录： */data/wwwroot/www.example.com*  

> 通过 *http://公网IP地址* 访问的就是示例网站 

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*

**default.conf** 默认存在一个 [server（虚拟主机）](https://support.websoft9.com/docs/linux/zh/webs-nginx.html#虚拟主机) 配置项，对应的就是 **示例网站**
```
server
{
listen 80;
server_name www.example.com  example.com;
index index.html index.htm index.php;
root  /data/wwwroot/www.example.com;
error_log /var/log/nginx/example.com-error.log crit;
access_log  /var/log/nginx/example.com-access.log;

include conf.d/extra/*.conf;

## Includes one of your Rewrite rules if you need, examples
 # include conf.d/rewrite/wordpress.conf;
 # include conf.d/rewrite/joomla.conf;
}
```

> 有多少个网站，就需要在 default.conf 中增加同等数量的 server 配置项

#### PHP

PHP 配置文件： */etc/php.ini*  
PHP Modules 配置文件目录： */etc/php.d*
```
# 默认已安装的 PHP Modules
Core  date  libxml  openssl  pcre  zlib  filter  hash  Reflection  SPL  session  standard    
bcmath  bz2  calendar  ctype  curl  dom  mbstring  fileinfo  ftp  gd  gettext  gmp  iconv  
imap  intl  json  ldap  exif  mcrypt  mysqlnd  odbc  PDO  Phar  posix  recode  shmop  
SimpleXML  snmp  soap  sockets  sqlite3  sysvmsg  sysvsem  sysvshm  tokenizer  xml  xmlwriter  xsl  mysqli  
pdo_dblib  pdo_mysql  PDO_ODBC  pdo_sqlite  wddx  xmlreader  xmlrpc  igbinary  imagick  zip  redis  Zend OPcache  
```

#### MYSQL

MySQL 安装路径: */usr/local/mysql*  
MySQL 数据文件 */data/mysql*  
MySQL 配置文件: */etc/my.cnf*    
MySQL 可视化管理地址: *http://服务器公网IP/phpmyadmin*，用户名和密码请见 [账号密码](/zh/stack-accounts.md) 章节。

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
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# PHP Version
php -v

# List Installed PHP Modules
php -m

# Nginx version
nginx -v

# List Installed Nginx Modules
nginx -V

# MySQL version
mysql -V

# Redis version
redis-server -v
```

### 服务

使用由 Websoft9 提供的 LNMP 部署方案，可能需要用到的服务如下：

#### Nginx

```shell
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
```

#### PHP-FPM
```shell
sudo systemctl start php-fpm
sudo systemctl stop php-fpm
sudo systemctl restart php-fpm
sudo systemctl status php-fpm
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

#### Tomcat
```shell
sudo systemctl start tomcat
sudo systemctl stop tomcat
sudo systemctl restart tomcat
sudo systemctl status nginx
```

#### phpMyAdmin

```shell
sudo docker start phpmyadmin
sudo docker stop phpmyadmin
sudo docker restart phpmyadmin
sudo docker stats pgadmin
```

#### Docker

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
2. 通过 phpMyAdmin 逐个导出数据库
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

### phpMyAdmin 升级

参考：[《phpMyAdmin 升级》](http://support.websoft9.com/docs/mysql/zh/solution-upgrade.html#mysql-更新升级)

### 网站升级

具体网站具体方案，此处不探讨

#### 常见问题

##### 是否支持 MySQL 大版本升级，例如：MySQL5.6-> MySQL5.7？
不支持，仅支持小版本升级。例如：5.6.x to 5.6.y 或 5.7.x to 5.7.y

##### 是否支持 PHP 大版本升级，例如：PHP7.0-> PHP7.2？
支持

##### 是否支持 PHP 大版本降级，例如：PHP7.2-> PHP7.0？
不支持

##### 升级之前需要做什么准备工作？
做好快照备份

## 故障处理

故障处理主要通过日志进行分析，处理故障基本等同于解读日志文件。

> 一部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 网站显示重定向错误？

打开Nginx虚拟主机配置文件，检查网站对应的 *server{}* 配置段内容，分析其中的重定向规则，找到其中的死循环。

#### 数据库服务无法启动？

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
  systemctl restart mysql
  ~~~

#### phpMyAdmin 出现 Error during session...错误？

Error during session start; please check your PHP and/or webserver log file and configure your PHP installation properly. Also ensure that cookies are enabled in your browser. session_start(): open(SESSION_FILE, O_RDWR) failed: Permission denied (13)

**问题原因**：系统更新后，PHP 的 session.save_path 路径目录的权限设置不正确。  
**解决方案**：打开WinSCP，运行如下命令即可
~~~
chown -R root:nginx /var/lib/php/session
echo 'chown nginx. -R /var/lib/php' >> /etc/cron.daily/0yum-daily.cron
~~~

#### 重启 Nginx 服务显示 *No spaces...*

出现此信息的时候，重启服务是成功的。

#### 502 错误？

Nginx应用服务器出现502错误的原因很多，但是基本都是资源不够造成的。 包括：内存不足，CPU超标，硬盘满了，另外可能也有程序导致php-fpm停止运行。对应的的解决办法：

*   内存和CPU超标，通过重启一下php-fpm 和nginx mysql 三个服务可以临时解决，如果是1核1g的配置且经常出现502错误的话，建议升级
*   硬盘满了的话，会导致MySQL停止服务，需要进行硬盘扩容
*   php-fpm服务停止或者报错也会出现502，需要重启php-fpm

#### 413 Request Entity Too Large

这是由于上传文件大小超过了Nginx默认设置，因此需要修改 Nginx 这个限制：

1. 使用 WinSCP 远程连接服务器
2. 编辑 [Nginx 虚拟机主机配置文件](/zh/stack-components.md#nginx)
3. 插入一行 `client_max_body_size 0;` 解除上传文件限制的配置项
   ```
   server {
    listen 80;
    server_name _;
    client_max_body_size 0; #解除上传文件限制
    ...
   ```
4. 保存并[重启 Nginx 服务](/zh/admin-services.md#nginx)

## 常见问题

#### LEMP 与 LNMP 有何不同？

LEMP 就是 LNMP，是不同的用户采用的不同名称而已

#### 默认字符集是什么？
UTF-8

#### Nginx 虚拟主机配置文件是什么？

虚拟主机配置文件是 Nginx 用于管理多个网站的**配置段集合**，路径为：*/etc/nginx/conf.d/default.conf*。  
每个配置段的形式为： `server{ }`，有多少个网站就有多少个配置段

#### LNMP 环境中默认有伪静态模板吗？

已经内置了部分常用网站的伪静态规则文件，进入目录可以查看
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/lnmp-multi/lnmp-rewrite-1-websoft9.png)

#### 如何修改示例网站根目录？

示例网站路径信息 */data/wwwroot/www.example.com* 存放在 [Nginx 虚拟主机配置文件](/zh/stack-components.md#nginx)中

#### LNMP 环境是否支持部署多个网站？

支持。每增加一个网站，只需在[Nginx 虚拟主机配置文件](/zh/stack-components.md#nginx)中增加对应的 **server{ }** 即可。

#### 如果没有域名是否可以部署 LNMP？

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

通过修改 [Nginx 虚拟主机配置文件](/zh/stack-components.md#nginx) 中相关路径参数

#### 如何删除9Panel?

删除 */data/apps/9panel* 下的所有数据即可，但需要保留文件夹

#### 通过 SFTP 上传网站源码后是否需要修改拥有者权限？

不需要，LNMP 会自动修正

#### 如何重置 php.ini 文件？

[下载 php.ini 模板](https://github.com/Websoft9/ansible-lamp/blob/master/roles/php/templates/php.ini) 后覆盖你服务器上的 */ect/php.ini*

#### Enabling Gzip Compression for HTML, CSS, and JavaScript Files

By default, compression is disabled in NGINX but depending on your installation or Linux distribution, some settings might be enabled in the default nginx.conf file. Here we enable gzip compression in the NGINX configuration file:

```
gzip on;
gzip_types application/xml application/json text/css text/javascript application/javascript;
gzip_vary on;
gzip_comp_level 6;
gzip_min_length 500;
```

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R nginx.nginx /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```

#### 如果设置 HTTP 跳转到 HTTPS？

只需在网站对应的 server{} 配置段中增加规则即可：
```
 if ($scheme != "https") 
    {
    return 301 https://$host$request_uri;
    }
```
#### LNMP 默认安装了哪些 Nginx模块？ 

运行命令 `nginx -V` 查看

#### LNMP 默认安装了哪些 PHP 模块？

运行命令 `php -m` 查看

#### 如何启用或禁用 Nginx 模块？

不支持模块启用或关闭

#### 如何禁用IP访问网站，防止恶意解析？

参考 [Nginx 相关配置文档](https://support.websoft9.com/docs/linux/zh/webs-nginx.html#禁用ip访问-防止恶意解析)

#### 没有域名是否可以通过 http://公网IP/mysite1 这样的方式访问网站？

可以。具体配置方法参考 [安装网站](/zh/solution-deployment.md#安装第二个网站)

