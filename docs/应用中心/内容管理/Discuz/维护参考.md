---
sidebar_position: 2
slug: /discuz/admin
tags:
  - Discuz
  - CMS
  - 建站系统
  - 博客系统
---

# 维护参考

## 系统参数

Discuz 预装包包含 Discuz 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

目前我们提供了两种 Discuz 部署包，下面分别列出其参数

### Discuz (LAMP) 路径

Discuz (LAMP) 即以 LAMP 为基础环境的 Discuz 部署包，其路径参数如下：

#### Discuz

Discuz 安装目录： */data/wwwroot/discuz*  
Discuz 配置文件： */data/wwwroot/discuz/upload/config/config_global_default.php*  

> Discuz 配置文件中包含数据库连接信息，更改了 MySQL 数据库账号密码，此处也需要对应修改

#### PHP

PHP 配置文件： */etc/php.ini*  
PHP Modules 配置文件目录： */etc/php.d*

#### Apache

Discuz on LAMP, the Web Server is Apache  

Apache 虚拟主机配置文件：*/etc/httpd/conf.d/vhost.conf*  
Apache 主配置文件： */etc/httpd/conf/httpd.conf*  
Apache 日志文件： */var/log/httpd*  
Apache 模块配置文件： */etc/httpd/conf.modules.d/00-base.conf*

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

### Discuz (WAMP) 路径

Discuz (WAMP) 即以 WAMPServer 为基础环境的 Discuz 部署包，其路径参数如下：

#### Discuz

Discuz 安装目录： *C:\websoft9\wampserver\www*  
Discuz 配置文件： *C:\websoft9\wampserver\www\wp-config.php* 
虚拟机主机配置文件： *C:\websoft9\wampserver\bin\apache\apache2.4.23\conf\extra\httpd-vhosts.conf*

#### WAMPServer

WAMPServer 是支持 Discuz (WAMP) 的 PHP 运行环境，包括：Apache, PHP, MySQL/MariaDB 等组件，具体参考： [《WAMPServer 管理员手册》](https://support.websoft9.com/docs/wampserver/zh/stack-components.html)


### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

本应用建议开启的端口如下：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过 HTTP 访问 Discuz | 必须 |
| HTTPS | 443 | 通过 HTTPS 访问 Discuz | 可选 |
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

# List Installed Nginx Modules
nginx -V

# MySQL version:
mysql -V

# Redis version
redis-server -v
```
### 服务

使用由 Websoft9 提供的 Discuz 部署方案，可能需要用到的服务如下：

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

1. 通过 WinSCP 将网站源码目录（*/data/wwwroot/discuz*）**压缩后**再完整的下载到本地
2. 通过 phpMyAdmin 导出 Discuz 数据库
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)
3. 将程序文件、数据文件和数据库文件放到同一个文件夹，根据日期命名
4. 备份工作完成

### Discuz 后台备份&恢复

Discuz 后台提供了非常简单实用的在线备份功能，使用方法如下：

1. 登录 Discuz 后台，打开：【后台】>【站长】>【数据库】，进入备份页面，设置备份策略。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-backup-websoft9.png)

2. 点击备份操作

3. 在线实现的备份可以在线恢复（还原）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-restore-websoft9.png)

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

### DiscuzQ 升级

官方提供可视化界面和命令行两种升级工具，详情参考官方文档：[DiscuzQ 升级](https://discuz.com/docs/%E5%B8%B8%E8%A7%84%E9%83%A8%E7%BD%B2%E5%8D%87%E7%BA%A7.html#%E4%BD%BF%E7%94%A8-dl-php-%E8%87%AA%E5%8A%A8%E5%8D%87%E7%BA%A7%E6%96%B9%E5%BC%8F-%E6%8E%A8%E8%8D%90)

下面介绍可视化升级的主要步骤：  

1. 使用 SFTP 工具连接服务器，删除 `/data/wwwroot/discuz/public/dl.php.lock` 文件

2. 本地浏览器访问： *http://服务器公网IP/dl.php* 进入升级界面
   ![可视化界面升级方式](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-installgui-websoft9.png)

3. 根据升级向导完成升级

### Discuz 升级

Discuz 需要手工上传升级包方可升级，也就是说升级对普通用户来说有点难。  

Discuz官方提供了一个简易的升级方案，[查看详情](https://gitee.com/Discuz/DiscuzX/wikis/%E5%8D%87%E7%BA%A7%E6%96%B9%E6%B3%95?sort_id=9978)

## 故障处理

此处收集使用 Discuz 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### Discuz后台系统首页的文件校验显示大量文件被修改，这是系统风险或网站漏洞吗？

websoft9为了优化用户体验，初始设定了随机密码；同时为了用户安全，修改了网站的访问权限，这样造成安装文件被修改的假象。
例如，discuzX3.4显示318文件被修改，60个文件丢失，这个是正常的，请勿担心。请参照下图
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-risk-websoft9.png)

#### Discuz 重定向错误？

重定向错误比较常见。处理办法：分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则

#### Discuz 密码输入错误多次被锁，怎么解决？

1. 10分钟后会自动解锁。
2. 管理员登录，组织→用户 操作栏里有解锁按钮。

#### 修改了数据库密码 Discuz 不能访问？

若已完成 Discuz 安装，后通过 phpMyAdmin 修改数据库密码，Discuz 就会连不上数据库。解决办法[参考](/zh/solution-more.html#discuz-修改数据库配置)

#### Discuz 出现“对不起，您的网站已被设置禁止下载此应用”问题

该问题出现的原因：由于 Discuz 官方设置了一个应用中心开发平台[Discuz!扩展中心防骗云平台](http://www.kuozhan.net/blacklist-index.html)专门针对所谓的盗版网站进行屏蔽网站授权，导致众多无辜站长用户无法更新和下载应用中心插件、模板，并且出现”对不起，您的网站已被设置禁止下载此应用“的提示。  

解决方法：

 1. 登录到phpmyadmin，找到pre_common_setting这个表（默认表前缀pre_，请以你自己的为准。）
 2. 在找到的表里删除掉siteuniqueid这个数据（pre_common_setting表中的第10页位置。）
 3. 再重新进入网站后台——应用——获取更多应用，再次下载更新试下吧！

#### Discuz 手机版访问报错“接口错误 err05 微社区域名已更换”

错误原因：Discuz官方提供的接口地址由http://wsq.discuz.qq.com/ 换成了现在 http://wsq.discuz.com/
解决方法：

  1. 登录服务器，找到Discuz根目录下的 */data/wwwroot/discuz/upload/source/class/helper/helper_form.php* 文件
  2. 将 'http://wsq.discuz.qq.com/', 25  改为 'http://wsq.discuz.com/', 22
  3. 清除 data/cache/qrcode 下的所有缓存文件

#### Discuz GBK版本乱码?

Websoft9提供的 Discuz 部署包默认都是UTF-8，一般情况下也可以支持 GBK 版本的Discuz。即当您用Discuz(GBK) 替换 Discuz00(UTF-8) 源码的时候，安装或使用若出现乱码，请参考如下解决办法：

1. 使用SFTP工具（例如“WinSCP”）连接服务器，修改 ect/php.ini 文件，保存
    ```
    默认
    default_charset = "UTF-8"

    修改为
    default_charset = "GBK"
    ```
2. 重启服务或重启服务器后生效
    ```
    systemctl restart httpd
    ```


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

#### [DiscuzQ](https://discuz.com/) 与 Discuz 有什么关系和区别？

从品牌上讲，DiscuzQ 是全新架构的 Discuz。但从代码角度看，它们完全不一样。Discuz! Q 的前后端完全分离，后端基于 Laravel，前端基于 Vue.js 和 uni-app，易于二次开发和扩展。

#### Discuz 支持多语言吗？

官方没有提供多语言方案

#### Discuz 是免费的吗？

Discuz 官方说得很模糊，我们也拿不准是不是免费的

#### Dicuz 最新源码在哪了下载？

参考官方：[码云Git地址](https://gitee.com/ComsenzDiscuz/DiscuzX)

#### Discuz 提供客户端吗？

Discuz 官方没有提供，但应用中心有服务商提供了相关的扩展

#### Discuz(LAMP)，Discuz(WAMP)等商品括号中的 LAMP,WAMP 是什么意思？

LAMP和WAMP代表支持 Discuz 运行所对应的基础环境，具体参考[环境说明](/zh/admin-runtime.md)

#### 是否可以使用云平台的 RDS 作为 Discuz 的数据库？

可以，修改 [Discuz 配置文件](/zh/stack-components.html#discuz) 即可

#### Discuz能在 Windows 服务器上运行吗？

可以，但是我们推荐在运行 Discuz 效率更高的 Linux 服务器上运行

#### Discuz数据库连接配置信息在哪里？

数据库配置信息 [Discuz 配置文件](/zh/stack-components.html#discuz)中

#### 如果没有域名是否可以部署 Discuz？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP/phpmyadmin

#### 如何禁止phpMyAdmin访问？

连接服务器，编辑 phpMyAdmin 配置文件，将其中的 Require all granted 更改为 Require ip 192.160.1.0，然后重启 Apache 服务

#### 是否可以修改 Discuz 的源码路径？

可以，通过修改 [虚拟主机配置文件](/zh/stack-components.md#discuz)中相关参数

#### 如何修改上传的文件权限?

```shell
#Discuz(LAMP)
chown -R apache.apache /data/wwwroot

find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```