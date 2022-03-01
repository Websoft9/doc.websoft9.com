---
sidebar_position: 2
slug: /magento/admin
tags:
  - Magento
  - 电子商务
---

# 维护参考

## 系统参数

Magento 预装包包含 Magento 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### Magento

Magento 安装目录： */data/wwwroot/magento*  
Magento 配置文件： */data/wwwroot/magento/app/etc/env.php*  

> Magento 配置文件中包含数据库连接信息，更改了 MySQL 数据库账号密码，此处也需要对应修改

#### PHP

PHP 配置文件： */etc/php.ini*  
PHP Modules 配置文件目录： */etc/php.d*

#### Apache

Magento on LAMP, the Web Server is Apache  

Apache 虚拟主机配置文件：*/etc/httpd/conf.d/vhost.conf*  
Apache 主配置文件： */etc/httpd/conf/httpd.conf*  
Apache 日志文件： */var/log/httpd*  
Apache 模块配置文件： */etc/httpd/conf.modules.d/00-base.conf*

#### Nginx

Magento on LEMP, the Web Server is Nginx  

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*  
Nginx 验证访问文件：*/etc/nginx/.htpasswd/htpasswd.conf*  

#### MySQL

MySQL 安装路径: */usr/local/mysql*  
MySQL 数据文件 */data/mysql*  
MySQL 配置文件: */etc/my.cnf*  

MySQL 可视化管理参考 [MySQL 管理](/zh/admin-mysql.md) 章节。

#### Varnish

Varnish 安装目录： */data/varnish*  
Varnish 日志目录： */data/logs/varnish*  

#### RabbitMQ

RabbitMQ 安装目录： */data/rabbitmq*  
RabbitMQ 日志目录： */data/logs/rabbitmq*  

#### Elasticsearch

Elasticsearch 安装目录： */data/elasticsearch*  
Elasticsearch 日志目录： */data/logs/elasticsearch*  

#### phpMyAdmin

phpMyAdmin 是一款可视化 MySQL 管理工具，在本项目中它基于 Docker 安装。  

phpMyAdmin directory：*/data/apps/phpmyadmin*  
phpMyAdmin docker compose file：*/data/apps/phpmyadmin/docker-compose.yml* 

#### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image* 
 
#### Redis

Redis configuration file: */etc/redis.conf*  
Redis data directory: */var/lib/redis*  
Redis logs file: */var/log/redis/redis.log*

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过 HTTP 访问 Magento | 必须 |
| HTTPS | 443 | 通过 HTTPS 访问 Magento | 可选 |
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

使用由Websoft9提供的 Magento 部署方案，可能需要用到的服务如下：

#### Apache

```shell
sudo systemctl start apache
sudo systemctl stop apache
sudo systemctl restart apache
sudo systemctl status apache
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

#### Docker-compose服务

```
#创建容器编排
sudo docker-compose up

#创建容器编排并重建有变化的容器
sudo docker-compose up -d

#启动/重启
sudo docker-compose start
sudo docker-compose stop
sudo docker-compose restart
```

#### Varnish

```shell
sudo systemctl start varnish
sudo systemctl stop varnish
sudo systemctl restart varnish
sudo systemctl status varnish
```

#### RabbitMQ

```shell
sudo systemctl start rabbitmq-server
sudo systemctl stop rabbitmq-server
sudo systemctl restart rabbitmq-server
sudo systemctl status rabbitmq-server
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

1. 通过 WinSCP 将网站目录（*/data/wwwroot/magento*）**压缩后**再完整的下载到本地
2. 通过 phpMyAdmin 导出 Magento 数据库
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)
3. 将程序文件、数据文件和数据库文件放到同一个文件夹，根据日期命名
4. 备份工作完成

### Magento 在线备份

本节提供Magento在线备份方案，请提前在云控制台做好必备的快照备份。

1. 登录到 Magento 后台，依次打开：【System】>【System->Backup】，进入Magento的备份设置页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-backup-websoft9.png)
2. 设置备份
3. 建议将备份加入到计划任务中
   - 登录 Magento 后台，依次打开：【Stores】>【Configuration】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-bkscheduleset-websoft9.png)
   - 找到：【System】>【Backup Settings】，设置计划任务
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-bkschedulesets-websoft9.png)

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


### Magento升级

Magento 可以通过两种方式升级：后台升级界面和 Composer 升级命令。  

下面介绍后台升级界面升级步骤：

1. 以管理身份登录 Magento，依次打开：【System】>【Web Setup Wizard】>【System Upgrade】 
   ![Magento upgrade](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-sysupgradestart-websoft9.png)
2. 如果没有[连接 Marketplace](/zh/stack-installation.html#连接-magento-marketplace)，系统会要求你输入 Access key
   ![Magento connect Marketplace](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-sysupgradestartkey-websoft9.png)
3. 点击升级按钮，开始在线升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-sysupgradestarting-websoft9.png)
4. 升级过程时间较长且报错，请查看[故障原因](/zh/else-troubleshooting.html#magento-在线升级或在线安装插件报错？)

更多更新操作请参考官方文档：[Magento Upgrade](https://devdocs.magento.com/guides/v2.3/comp-mgr/bk-compman-upgrade-guide.html)


## 故障处理

此处收集使用 Magento 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### Magento 在线升级或在线安装插件报错？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-upgrade-dependency.png)

如果升级过程若报错，最可能的原因是内存不足，一方面需要保证服务器内存不低于 4G，另一方面需要修改 Magento 根目录下的 `.htaccess` 文件。

其中的 `php_value memory_limit` 不低于 2048M

```
    php_value memory_limit 2048M
    php_value max_execution_time 18000
```

#### Magento 站点通过IP访问的情况下， 服务器IP发生变更导致无法访问？

通过SSH连接云服务器，运行下面的CLI命令即可恢复
```shell
    /data/wwwroot/magento/bin/magento setup:store-config:set --base-url=http://服务器公网IP # 修改成您的当前服务器IP
```
 > 通过域名访问的情况，请参照[域名绑定](solution-more.md/#域名绑定)

#### 修改了数据库密码 Magento 不能访问？

若已完成 Magento 安装向导，再通过 phpMyAdmin 修改数据库密码，此候 Magento 就会连不上数据库

需要修改配置文件（/data/wwwroot/magento/app/etc/env.php）对应的数据库 password 参数即可。

#### Magento 出现“One or more indexers are invalid....”如何解决？
##### 方法1
1.  在管理员页面的左边控制栏点击“SYSTEM”,在弹出的选项中选择Index Management；
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-cron001.png)
2.  点击图中所示的选项框，选择下拉菜单中的Update by Schedule，然后点击序号4所示的选项框选择Select All，最后单击5所示的Submit即可。
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-cron002.png)

##### 方法2
1. 使用命令行工具 (SSH or Terminal)进入magento安装根目录：cd /data/wwwroot/magento/bin
2. 重新编制索引：php magento indexer:reindex

#### Apache httpd 服务无法启动？

请通过分析日志文件定位原因： */var/log/httpd*

#### 登陆时需要邮件验证，无法收到邮件怎么办？

关闭密码邮件双重认证，通过密码即可登陆
```shell
# Close Magento_TwoFactorAuth
sudo php /data/wwwroot/magento/bin/magento module:disable Magento_TwoFactorAuth
```


#### 网站重定向错误？

分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则

#### Magento 后台重定向太多，无法访问（ERR_TOO_MANY_REDIRECTS magento admin）

在网站配置域名或做了 https 配置后，网站可能出现后台重定向太多无法访问，在确定不是 '.htaccess' 配置文件的问题下，请检查如下几个 url ，将其改成你的域名，同时修改2个选项为 true。
这些信息保存在 Magento 的配置数据表 core_config_data 中，可以通过修改数据表来修改，也可以通过下列 cli 方式处理。

```shell
cd /data/wwwroot/magento
php bin/magento setup:store-config:set --use-secure=1 --use-secure-admin=1 --base-url-secure="https://www.yourdomain.com/"
php bin/magento cache:flush  #将基础URL更改为https并刷新缓存
```

#### Magento 无法加载CSS/js资源，页面排版混乱

在网站配置域名或做了 https 配置后，网站可能出现，能访问但页面排版混乱，图片不显示（不能访问请先[配置域名](http://support.websoft9.com/docs/magento/zh/solution-more.html#%E5%9F%9F%E5%90%8D%E7%BB%91%E5%AE%9A)）。

造成这样的原因，在确定不是配置文件的问题下，可以通过【重新发布】来处理。虽然不会删除数据，但请操作前做好数据备份。步骤如下:

1. 开启维护模式
2. 删除静态文件和一系列缓存文件
3. 更新数据库以及代码编译
4. deploy生成静态文件到pub/static里
5. 更新索引，关闭维护模式，以及清空刷新magento缓存


```shell
cd /data/wwwroot/magento
php bin/magento maintenance:enable
php rm -rf var/di/* && rm -rf var/generation/* && rm -rf var/cache/* && rm -rf var/page_cache/* && rm -rf var/view_preprocessed/* && rm -rf pub/static/* && rm -rf generated/* 
php bin/magento setup:upgrade 
php bin/magento setup:di:compile
php bin/magento setup:static-content:deploy -f
php bin/magento indexer:reindex
php bin/magento cache:clean && bin/magento cache:flush
php bin/magento maintenance:disable 
```


#### We can't find products matching the selection，添加类别和商品但不能正常显示

Magento 除了系统给出的商品属性，还允许用户通过后台“STORES”->"Attributes"->"Product"添加额外的商品属性。添加的额外属性的属性值设置不正确就会影响前台的商品展示，出现如图错误。通过以下步骤可以排查此问题：

![magento](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-products-matching-the-selection-websoft9.png)


1. 查看日志/data/wwwroot/magento/var/log/exception.log，看是否是添加的属性引发的异常，本例中查看到“eanl3”属性有异常

![magento](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-log-websoft9.png)

2. 进入后台“STORES”->"Attributes"->"Product"，查看相关属性设置.

![magento](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-product-attribute-websoft9.png)

3. 在属性列表中点击“ean13”，进入设置界面

![magento](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-product-attribute1-websoft9.png)

4. 属性设置

![magento](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-product-attribute2-websoft9.png)

5. 清空浏览器缓存，重新打开网站


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

#### Magento 支持多语言吗？

支持多语言（包含中文），需要上传语言包才能设置语言

#### Magento 为什么运行这么慢？

Magento 是一个复杂的企业级电商系统，对计算资源要求较高

#### 忘记了Magento后台登陆地址怎么办？

进入linux系统，通过命令一下命令查看
```shell
# Show Magento(URL)
/data/wwwroot/magento/bin/magento info:adminuri

# Update Magento(URL)
sudo /data/wwwroot/magento/bin/magento setup:config:set --backend-frontname=[yourAdminUrl] -n
```

#### 为什么要连接 Magento Marketplace？

只有连接Magento Marketplace，才可以使用其资源。连接教程[参考](/zh/solution-more.html#连接-magento-marketplace)

#### Magento(LAMP)，Magento(LNMP)等商品括号中的 LAMP,LNMP 是什么意思？

LAMP和LNMP代表支持Magento运行所对应的基础环境，具体参考[环境说明](/zh/admin-runtime.html)

#### 是否可以使用云平台的 RDS 作为 Magento 的数据库？

可以，修改 Magento 根目录下的配置文件 `config.php` 即可

#### Magento能在Windows服务器上运行吗？

可以，但是我们推荐在运行 Magento 效率更高的 Linux 服务器上运行

#### Magento数据库连接配置信息在哪里？

数据库配置信息在Magento安装目录下的 *LocalSettings.php* 中，[查阅安装目录路径](/zh/stack-components.md#magento)

#### 如果没有域名是否可以部署 Magento？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP/phpmyadmin

#### 如何禁止phpMyAdmin访问？

连接服务器，编辑 phpMyAdmin 配置文件，将其中的 Require all granted 更改为 Require ip 192.160.1.0，然后重启 Apache 服务

#### 是否可以修改 Magento 的源码路径？

可以，通过修改 [虚拟主机配置文件](/zh/stack-components.md#magento)中相关参数

#### 如何修改上传的文件权限?

```shell
#Magento(LAMP)
chown -R apache.apache /data/wwwroot

#Magento(LEMP)
chown -R nginx.nginx /data/wwwroot

find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```
