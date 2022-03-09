---
sidebar_position: 2
slug: /wordpress/admin
tags:
  - WordPress
  - CMS
  - 建站系统
  - 博客系统
---

# 维护参考

## 系统参数

WordPress 预装包包含 WordPress 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

Websoft9 提供了多种 WordPress部署包，有着不同的操作系统以及 Web 服务器组合，请根据你具体使用的部署包查看对应的路径

#### WordPress路径

##### Wordpress(LAMP or LNMP)

WordPress 安装目录： */data/wwwroot/wordpress*  
WordPress 配置文件： */data/wwwroot/wordpress/wp-config.php*   
虚拟机主机配置文件： */etc/httpd/conf.d/vhost.conf* 或 */etc/nginx/conf.d/default.conf*  

##### Wordpress(IIS)

WordPress 安装目录： *C:\inetpub\wwwroot\wordpress*  
WordPress 配置文件： *C:\inetpub\wwwroot\wordpress\wp-config.php*   
虚拟机主机配置文件： *C:\websoft9\wampserver\bin\apache\apache2.4.23\conf\extra\httpd-vhosts.conf*

##### Wordpress(WAMP)

WordPress 安装目录： *C:\websoft9\wampserver\www*  
WordPress 配置文件： *C:\websoft9\wampserver\www\wp-config.php* 
虚拟机主机配置文件： *C:\websoft9\wampserver\bin\apache\apache2.4.23\conf\extra\httpd-vhosts.conf*

> WordPress 配置文件中包含数据库连接信息，更改了 MySQL 数据库账号密码，此处也需要对应修改

#### 环境路径 

支撑 WordPress 运行的环境组件包括：PHP, MySQL, Apache or Nginx等，请根据不同的部署包分别查看

| 部署包名称 | 说明| 参考项 |
| --- | --- | --- |
| Wordpress(LAMP) | Web服务器为 Apache，系统为 Linux |[PHP](https://support.websoft9.com/docs/lamp/zh/stack-components.html#php), [Apache](https://support.websoft9.com/docs/lamp/zh/stack-components.html#apache), [MySQL](https://support.websoft9.com/docs/lamp/zh/stack-components.html#mysql) |
| Wordpress(LNMP)| Web服务器为 Nginx，系统为 Linux |[PHP](https://support.websoft9.com/docs/lnmp/zh/stack-components.html#php), [Nginx](https://support.websoft9.com/docs/lnmp/zh/stack-components.html#nginx), [MySQL](https://support.websoft9.com/docs/lnmp/zh/stack-components.html#mysql) |
| Wordpress(IIS)| Web服务器为 IIS，系统为 Linux |[PHP](https://support.websoft9.com/docs/windows/zh/stack-components.html#php), [IIS](https://support.websoft9.com/docs/windows/zh/stack-components.html#iis), [MySQL](https://support.websoft9.com/docs/windows/zh/stack-components.html#mysql) |
| Wordpress(WAMP)| Web服务器为 WAMPServer，系统为 Linux |[PHP](https://support.websoft9.com/docs/wampserver/zh/stack-components.html#apache), [Apache](https://support.websoft9.com/docs/wampserver/zh/stack-components.html#apache), [MySQL](https://support.websoft9.com/docs/wampserver/zh/stack-components.html#mysql) |


### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

本应用建议开启的端口如下：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过 HTTP 访问 WordPress | 必须 |
| HTTPS | 443 | 通过 HTTPS 访问 Wordpress | 可选 |
| MySQL | 3306 | 远程连接 MySQL | 可选 |

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

# List Installed nginx Modules
Nginx -V

# MySQL version
mysql -V

# Redis version
redis-server -v
```

### 服务


使用由 Websoft9 提供的 WordPress 部署方案，可能需要用到的服务如下：

#### Linux系统

##### Apache

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

##### Nginx

```shell
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
```

##### PHP-FPM
```shell
systemctl start php-fpm
systemctl stop php-fpm
systemctl restart php-fpm
systemctl status php-fpm
```

##### MySQL

```shell
sudo systemctl start mysql
sudo systemctl stop mysql
sudo systemctl restart mysql
sudo systemctl status mysql
```

##### Redis

```shell
systemctl start redis
systemctl stop redis
systemctl restart redis
systemctl status redis
```

#### Windows系统

Windows下的镜像采用图形化界面实现服务的启动、停止和重启操作

##### --IIS

进入IIS，点击主机名称，右侧的操作就会显示重启启动，停止等操作

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-restart-websoft9.png)

##### --WAMPServer

远程桌面点击WAMPServer图标，然后点击“重新启动所有服务”
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-clicks-websoft9.png)

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

1. 通过 WinSCP 将网站目录（例如：*/data/wwwroot/wordpress*）**压缩后**再完整的下载到本地
2. 通过 phpMyAdmin 导出 WordPress 数据库
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)
3. 将程序文件和数据库文件放到同一个文件夹，根据日期命名
4. 备份工作完成

### WordPress 备份插件

WordPress插件库中有数量众多的备份插件，我们推荐使用：[UpdraftPlus WordPress Backup Plugin ](https://wordpress.org/plugins/updraftplus/)

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-updraftplus-websoft9.png)

这个插件特点和好处包括：

* 可以预设备份时间点，实现自动备份
* 可以备份网站文件和数据库
* 可以实现一键恢复


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



### WordPress升级

#### 须知

WordPress 升级包括：WordPress 内核升级、插件升级和主题升级。这三者都可以通过 WordPress 后台进行在线升级，下图是升级提醒：  
![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-upgrade-websoft9.png)

由于这三者分别属于不同的开发者，升级后可能会导致不兼容的现象。具体表现有：

- 网站打不开，显示500程序错误
- 网站结构变得混乱
- 主题部分功能不可用

以上不兼容现象是正常的，最好的解决办法是让 主题和插件的版本 适应 WordPress 内核版本。

#### 内核升级

##### 一键升级

WordPress 内核升级非常简单，当进入后台之后系统会提示需要升级，点击升级即可（ 特别注意：Wordpress应用程序升级之前务必进行完整备份，以保证备份出现差错之后能够复原。）

 ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-wordpresscoreupdate-websoft9.png)

##### 手动升级

有的时候，由于网络原因，在线一键升级不可用，那么就需要手工升级

1. [下载](https://github.com/WordPress/WordPress/tags)最新的 WordPress 版本，并解压
2. 登录云服务器，进入 [WordPress 的根目录](/zh/stack-components.html#wordpress路径)
3. 删除此目录下的 `wp-admin` 和 `wp-includes` 文件夹
4. 上传本地解压后的 WordPress代码，有同名文件提醒的时候选择覆盖上传
5. 重新访问WordPress，可能会出现下图所示的数据库升级步骤
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-update-db-websoft9.jpg)
6. 点击【升级WordPress数据库】即可

#### 插件升级

插件一般采用在线升级的方式，并逐一升级  

 ![WordPress 插件升级](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-pluginupdate-websoft9.png)

#### 主题升级

主题升级建议采用的方式：

1. 使用 WinSCP 登录服务，删除原有主题（或对其改名）
2. 通过 【WordPress 后台】>【外观】>【主题】>【添加】>【上传主题】的方式，完成主题安装
   ![Wordpress 上传主题](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-addthemes-websoft9.png)


## 故障处理

此处收集使用 WordPress 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

####  WordPress 出现病毒导致乱码？

由于被广泛使用，导致安全漏洞被无限放大，其中WordPress网站被[植入第三方代码](././administrator/security/emergency#insertcode)是最常见的安全故障。 

#### WordPress 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```

#### WordPress运行中，频繁出现数据库连接错误？
诊断原因：可能性最大的原因是内存不足导致数据库运行异常
解决方案：增加内存+启用CDN

> CDN可以在给网站加速的同时，大大降低服务器内存的开销

#### WordPress上传图片出错？

WordPress上传文件出错，有几种可能性：  
1. 图片大小超过服务器限定的要求  
解决方案：请参考本章环境管理-&gt;PHP配置中的修改上传文件大小  
2. 图片实际的格式与后缀不一致。  
解决方案：例如一个 WordPress9.jpg的图片的真实格式是Wordpress9.jpeg，上传的时候会报错，如果把后缀改为jpeg，上传正常。实际上，真实格式与后缀不一致的时候，在Windows系统的文件中也不会有预览效果
3. 权限问题（IIS中比较常见）

#### WordPress出现解决正在执行例行维护请一分钟后回来

出现这个提示的原因是在网站Wordpress安装目录下生成了.maintenance文件

* 如果存在将其删除即可,恢复正常. 
* 如果不存在,那么新建一个.maintenance，内容为空白，刷新，恢复正常后再删除它

#### WordPress不能发送邮件的原因

WordPress默认是通过mail\(\)函数发送邮件，必须要求服务器本身配置好了邮件功能。实际中，将服务器改造成邮件服务器，是一件非常复杂的工作，且难以维护。因此，建议安装一个SMTP插件来解决发送邮件问题：WP-Mail-SMTP

#### WordPress 5.0 换回老版”Classic Editor”经典编辑器
Wordpress5.0之后的版本，编辑器与之前有了明显的区别。这里不探讨编辑器孰优孰劣，我们发现编辑器升级之后，用户的主题无法适应新的编辑器，导致做不到可视化编辑。如果您希望主题可以可视化编辑，您必须启用经典编辑器。启用的方法非常简单，安装“Classic Editor”这个插件即可

#### WordPress 后台升级网络不通，官网也打不开？
WordPress是国外的网站，后台升级地址也是国外的，如果网站打不开，后台升级同样就无法进行。如果您迫切需要升级，请参考我们的[WordPress手工升级文档](/zh/solution-upgrade.md#手动升级)

#### WordPress 管理员失去权限，无法正常登录后台？
WordPress的后台管理是分权限的，而最高权限是超级管理员。当wordpress管理员因失去权限无法正常进入后台，可以通过进入PhpMyAdmin数据库管理工具，来进行权限恢复：
* 登录数据库管理工具phpMyAdmin:  http:// 服务器ip/phpMyAdmin/
* 找到跟用户相关的数据表：wp_users和wp_usermeta;
* 先进入wp_users,查看自己的管理员用户名，超级管理员用户id一般都是1，不是就修改；
* 再进入wp_usermeta表，找到wp_user_level，wp_capabilities字段。如果对应账号wp_user_level的值不是10 ，请修改为10（超级管理员一半都是10，最高权   限）；查看wp_capabilities值，如果里面不是 “administrator”，可以直接改成：a:1:{s:13:"administrator";b:1;} ；
* 重新登录。

#### Wordpress导入一个演示数据显示 You don't have permission to access /wp-admin/admin.php on this server?
待研究

## 常见问题

#### WordPress支持多语言吗？

支持多语言（包含中文），后台可以设置语言

#### WordPress能建企业网站吗？

可以，全球34%的网站都是基于 WordPress 构建

#### WordPress(LAMP)，WordPress(LNMP)等商品括号中的 LAMP,LNMP 是什么意思？

LAMP和LNMP代表支持WordPress运行所对应的基础环境，具体参考[环境说明](/zh/admin-runtime.html)

#### 是否可以使用云平台的 RDS 作为 WordPress 的数据库？

可以，修改 WordPress 根目录下的配置文件 `wp-config.php` 即可

#### WordPress能在Windows服务器上运行吗？

可以，但是我们推荐在运行 WordPress 效率更高的 Linux 服务器上运行

#### WordPress数据库连接配置信息在哪里？

数据库配置信息在WordPress安装目录下的 *wp-config.php* 中，[查阅安装目录路径](/zh/stack-components.md#wordpress)

#### 如果没有域名是否可以部署 WordPress？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`（Linux） 或 服务器桌面（Windows）

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP/phpmyadmin

#### 如何禁止phpMyAdmin访问？

连接服务器，编辑 phpMyAdmin 配置文件，将其中的 Require all granted 更改为 Require ip 192.160.1.0，然后重启 Apache 服务

#### 是否可以修改WordPress的源码路径？

可以，通过修改 [虚拟主机配置文件](/zh/stack-components.md#wordpress路径)中相关参数

#### WordPress 登录后台如何使用 SSL？

在 wp-config.php 文件中的特定位置，添加如下两行代码

```
### 添加代码开始 ###
define('FORCE_SSL_ADMIN', true);
define('FORCE_SSL_LOGIN', true);
### 添加代码结束 ###

if ( !defined(‘ABSPATH’) )
        define(‘ABSPATH’, dirname(__FILE__) . ‘/’)
```


#### 如何修改上传的文件权限?

```shell
#WordPress(LAMP)
chown -R apache.apache /data/wwwroot

#WordPress(LNMP)
chown -R nginx.nginx /data/wwwroot

find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```