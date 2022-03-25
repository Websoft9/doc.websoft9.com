---
sidebar_position: 2
slug: /joomla/admin
tags:
  - Joomla
  - CMS
  - 建站系统
---

# 维护参考

## 系统参数

Joomla 预装包包含 Joomla 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### Joomla

Joomla 安装目录： */data/wwwroot/joomla*  
Joomla 配置文件： */data/wwwroot/joomla/configuration.php*  

> Joomla 配置文件中包含数据库连接信息，更改了 MySQL 数据库账号密码，此处也需要对应修改

#### PHP

PHP 配置文件： */etc/php.ini*  
PHP Modules 配置文件目录： */etc/php.d*

#### Apache

Joomla on LAMP, the Web Server is Apache  

Apache 虚拟主机配置文件：*/etc/httpd/conf.d/vhost.conf*  
Apache 主配置文件： */etc/httpd/conf/httpd.conf*  
Apache 日志文件： */var/log/httpd*  
Apache 模块配置文件： */etc/httpd/conf.modules.d/00-base.conf*

#### Nginx

Joomla on LEMP, the Web Server is Nginx  

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
| HTTP | 80 | 通过 HTTP 访问 Joomla | 必须 |
| HTTPS | 443 | 通过 HTTPS 访问 Joomla | 可选 |
| MySQL | 3306 | 远程连接 MySQL | 可选 |
| HTTP | 9090 | phpMyAdmin 访问端口 |	可选

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

使用由Websoft9提供的 Joomla 部署方案，可能需要用到的服务如下：

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

1. 通过 WinSCP 将网站源码目录（*/data/wwwroot/joomla*）**压缩后**再完整的下载到本地
2. 通过 phpMyAdmin 导出 Joomla 数据库
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)
3. 将程序文件、数据文件和数据库文件放到同一个文件夹，根据日期命名
4. 备份工作完成

### Joomla 后台备份

通过安装 Joomla 扩展，可以实现后台在线备份：

1. 下载 [Akeeda](https://www.akeebabackup.com/download.html)

2. 登录 Joomla 后台，通过上传压缩文件的方式安装 **Akeeda** 

3. 打开：【Dashboard】>【System】>【Control Panel】，找到【Backup is up-to-date】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-backup-websoft9.png)

4. 开始设置备份策略

5. 通过 Akeeda 实现的备份可以在线恢复
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-restore-websoft9.png)


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


### Joomla 升级

Joomla 提供了非常人性化的在线升级方案，根据系统的更新提示完成升级

> 在升级之前请做好服务器的快照备份，这个是必须的步骤，因为谁都无法保证升级 100% 成功。

1. 登录 Joomla 后台，如果有升级需求系统会显示升级提示
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkupgradets-websoft9.png)  

2. 根据提示进入升级中心，确认是否具备升级条件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-update003-websoft9.png)

3. 升级中，请耐心等待
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-update004-websoft9.PNG)

4. 升级成功
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-update005-websoft9.PNG)

5. 扩展也可以在线升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkextupgrade-websoft9.png)


> 更多升级详情，请参考官方升级文档 [Joomla Upgrading](https://docs.joomla.org/Portal:Upgrading_Versions/zh-cn)


## 故障处理

此处收集使用 Joomla 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### Joomla 重定向错误？

多语言下，重定向错误比较常见。例如：打开您的 Joomla 中文版会出现重定向错误

处理办法：分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则

#### 修改了数据库密码 Joomla 不能访问？

若已完成 Joomla 安装向导，再通过 phpMyAdmin 修改数据库密码，Joomla 就会连不上数据库  

需要修改 [Joomla 配置文件](/zh/stack-components.html#joomla) 对应的数据库 password 参数即可。

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

#### Joomla 支持多语言吗？

支持多语言（包含中文），建议在初始化安装的时候安装多语言

#### Joomla(LAMP)，Joomla(LNMP)等商品括号中的 LAMP,LNMP 是什么意思？

LAMP和LNMP代表支持 Joomla 运行所对应的基础环境，具体参考[环境说明](/zh/admin-runtime.html)

#### 是否可以使用云平台的 RDS 作为 Joomla 的数据库？

可以，修改 [Joomla 配置文件](/zh/stack-components.html#joomla) 即可

#### Joomla能在 Windows 服务器上运行吗？

可以，但是我们推荐在运行 Joomla 效率更高的 Linux 服务器上运行

#### Joomla数据库连接配置信息在哪里？

数据库配置信息 [Joomla 配置文件](/zh/stack-components.html#joomla)中

#### 如果没有域名是否可以部署 Joomla？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP:9090

#### 如何禁止phpMyAdmin访问？

连接服务器，编辑 phpMyAdmin 配置文件，将其中的 Require all granted 更改为 Require ip 192.160.1.0，然后重启 Apache 服务

#### 是否可以修改 Joomla 的源码路径？

可以，通过修改 [虚拟主机配置文件](/zh/stack-components.md#joomla)中相关参数

#### 如何修改上传的文件权限?

```shell
#Joomla(LAMP)
chown -R apache.apache /data/wwwroot

#Joomla(LNMP)
chown -R nginx.nginx /data/wwwroot

find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```

#### 在组件中如何加载其他扩展的语言文件?

开发一个Joomla投稿组件的时候，需要调用joomla文章组件的语言文件，因为界面很多字符串都来自系统的文章组件，本来打算直接将系统的文章组件的语言文件直接复制一份的，但感觉那样做不优雅，因此，查了一下源码，发现是Joomla是可以在任何时间，任何地方调用任何组件的语言文件的。

直接上代码了，并不难理解

~~~
`$lang` `= JFactory::getLanguage();`

`$extension` `= ``'com_content'``;`

`$base_dir` `= JPATH_ADMINISTRATOR;`

`$language_tag` `= ``'zh-CN'``;`

`$reload` `= true;`

`$lang``->load(``$extension``, ``$base_dir``, ``$language_tag``, ``$reload``);`
~~~

上面的代码没有什么好解释的。需要什么扩展就将extension变量赋值即可。
