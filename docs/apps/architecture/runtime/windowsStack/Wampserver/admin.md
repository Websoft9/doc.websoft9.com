---
sidebar_position: 2
slug: /wampserver/admin
tags:
  - WampServer
  - PHP
  - Apache
  - Windows
---


# 维护参考

## 系统参数

WampServer 预装包包含 WampServer 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### 网站目录

根目录： *WampServer 环境中，你的网站代码存放位置是没有限制的，因此没有根目录的说法*  
网站存放目录（建议）： *C:\websoft9\wampserver\www*  
示例网站目录： *C:\websoft9\wampserver\www\www.example.com*  

> 通过 *http://公网IP地址* 访问的就是示例网站 

#### Apache

**Apache 虚拟主机配置文件**： *C:\websoft9\wampserver\bin\apache\apache2.4.x\conf\extra\httpd-vhosts.conf*  
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-vhost-websoft9.png)

Apache 主配置文件： *C:\websoft9\wampserver\bin\apache\apache2.4.x\conf\httpd.conf*   
Apache 日志文件： *C:\websoft9\wampserver\logs*  
Apache 模块目录： *C:\websoft9\wampserver\bin\apache\apache2.4.x\modules*  

**httpd-vhosts.conf** 默认存在一个 [VirtualHost（虚拟主机）](https://support.websoft9.com/docs/windows/zh/webs-apache.html#虚拟主机) 配置项，对应的就是 **示例网站**
```
<VirtualHost *:80>
ServerName www.mydomain.com
#ServerAlias other.mydomain.com
DocumentRoot "C:\websoft9\wampserver\www\www.example.com"
ErrorLog "logs\www.mydomain.com_error_apache.log"
CustomLog "logs\www.mydomain.com_apache.log" common
<Directory "C:\websoft9\wampserver\www\www.example.com">
   Options Indexes FollowSymlinks
   AllowOverride All
   Require all granted
</Directory>
</VirtualHost>
```

> 有多少个网站，就需要在 **httpd-vhosts.conf** 中增加同等数量的 **VirtualHost** 配置项

#### PHP

WampServer 环境支持多个 PHP 版本，每个版本都有对应的 PHP 配置文件。  

PHP 配置文件： *C:\websoft9\wampserver\bin\php\php7.x.x\php.ini*  
PHP 扩展目录： *C:\websoft9\wampserver\bin\php\php7.x.x\ext*   
PHP 扩展配置文件： *C:\websoft9\wampserver\bin\php\php7.x.x\ext\phpForApache.ini*  

PHP 扩展启用或关闭，通过修改 PHP 配置文件实现

#### MySQL

MySQL 安装路径：*C:\websoft9\wampserver\bin\mysql*  
MySQL 数据文件：*C:\websoft9\wampserver\bin\mysql\mysql5.x.x\data*  
MySQL 配置文件：*C:\websoft9\wampserver\bin\mysql\mysql5.x.x\my.ini*    
MySQL 可视化管理地址: *http://服务器公网IP/phpmyadmin*，用户名和密码请见 [账号密码](/zh/stack-accounts.md) 章节。

#### MariaDB

MariaDB 安装路径：*C:\websoft9\wampserver\bin\mariadb*  
MariaDB 数据文件：*C:\websoft9\wampserver\bin\mariadb\mariad10.x.x\data*  
MariaDB 配置文件：*C:\websoft9\wampserver\bin\mariadb\mariad10.x.x\my.ini*    
MariaDB 可视化管理地址: *http://服务器公网IP/phpmyadmin*，用户名和密码请见 [账号密码](/zh/stack-accounts.md) 章节。

#### phpMyAdmin

phpMyAdmin 安装路径: *C:\websoft9\wampserver\apps\phpmyadmin4.x.x*  
phpMyAdmin 配置文件: *C:\websoft9\wampserver\apps\phpmyadmin4.x.x\config.inc.php*   
phpMyAdmin 虚拟主机配置文件: *C:\websoft9\wampserver\alias\phpmyadmin.conf*   

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

本环境建议开启的端口如下：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过 HTTP 访问网站 | 必须 |
| HTTPS | 443 | 通过 HTTP 访问网站 | 可选 |
| MySQL | 3306 | 本地电脑远程连接服务器上的 MySQL | 可选 |
| MariaDB | 3307 | 本地电脑远程连接服务器上的 MySQL | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看，更精准的版本号请通过下面的方式获取：

- 在服务器 *C:\websoft9\wampserver* 目录下查看安装目录名称。
- 或通过：*http://服务器公网IP/9panel/tz.php* 查看组件的版本
- 
### 服务

使用由Websoft9提供的WAMP部署方案，可能需要用到的服务如下：

> 服务随操作系统自动启动，如果手工修改配置参数后，需要重新启停服务

#### 通过 WampServer 管理服务

远程桌面到服务器，点击 WAMPServer 图标，然后点击【重新启动所有服务】，就可以同时重启 Apache, MySQL & MariaDB 服务

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-clicks-websoft9.png)

#### 通过 Windows 系统服务 管理服务

远程桌面到服务器，打开 Windows 系统的服务管理工具：【开始菜单】>【管理工具】>【服务】
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-ss-websoft9.png)

- wampapache64 代表的是 Apache 服务
- wampMysql，代表的是 MySQL 服务
- wampMariadb，代表的是 MariaDB 服务

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


1. 通过 远程桌面工具 将网站目录（*C:\websoft9\wampserver\www*）**压缩后**再完整的下载到本地
2. 通过 phpMyAdmin 逐个导出数据库
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)
3. 将程序文件和数据库文件放到同一个文件夹，根据日期命名
4. 备份工作完成



## 恢复


## 升级

WAMP 完整的更新升级包括：操作系统更新、PHP 更新、Apache 更新、MySQL 更新

### Windows 更新

Windows服务器的更新与本地电脑类似，手动找到更新管理程序，设置自动下载自动更新即可。

### PHP 更新

以从 PHP7.0.29 升级到 PHP7.0.31 为例：

1. 左击右下角任务栏的 WAMP 图标，停止所有服务

2. 到 [PHP 官网](https://windows.php.net/download/)下载最新版本的 PHP7.0 
   > 注意：下载的文件为压缩包文件，且必须选择 **Thread Safe** 版本。
   	![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/wampserver-phpupdate-1-websoft9.png)

3. 备份原来的 C:\websoft9\wampstack\php 文件夹，再将该文件夹下所有文件删除，将新版 PHP 文件解压到这个文件夹里

4. 将新版 php 文件夹下的 php.ini-production 文件重命名为 php.ini

5. 重新服务


### Apache 更新

待续...

### MySQL 更新

待续...

### 常见问题

#### 是否支持 MySQL 大版本升级，例如：MySQL5.6-> MySQL5.7？
不支持，仅支持小版本升级。例如：5.6.x to 5.6.y 或 5.7.x to 5.7.y

#### 是否支持 PHP 大版本升级，例如：PHP7.0-> PHP7.2？
官方没有提供升级文档

#### 是否支持 PHP 大版本降级，例如：PHP7.2-> PHP7.0？
不支持

#### 升级之前需要做什么准备工作？

做好快照备份

## 故障处理

此处收集使用 WampServer 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 网站重定向错误？

网站重定向错误比较常见。  

处理办法：分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则

#### 新增站点报错：You don't have permission to access/on this server

解决办法：

1.  检查网站目录的权限
2.  配置虚拟主机配置文件是否有 "AllowOverride All   Require all granted" 相关内容

#### 如何解决 http-proxy 漏洞？
升级 PHP 的小版本即可解决 ttp-proxy 漏洞

#### Apache httpd 服务无法启动？

请通过分析日志文件定位原因

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```

#### 数据库日志文件太大，导致磁盘空间不足？

默认安装，mysql会自动开启binlog，binlog是一个二进制格式的文件，用于记录用户对数据库**更新的****SQL语句****信息**，例如更改数据库表和更改内容的SQL语句都会记录到binlog里。

binlog主要用于出现没有备份的情况下，恢复数据库。但binlog会占用较大空间，长期不清理会让剩余磁盘空间为0，从而影响数据库或服务器无法启动

如果对自己的备份有信心，不需要binlog功能，参考如下步骤关闭之：

1. 编辑 [MySQL 配置文件](/zh/stack-components.md#mysql)，注释掉 binlog 日志
  ~~~
  #log-bin=mysql-bin  
  ~~~
2. 重启 MySQL 服务

#### 如何根据 Windows 系统日志查看故障原因？

按照下列图中所示，进入到 Windows 系统的**事件查看器**，选择 Windows 日志下的应用程序，然后在右侧的事件列表查看出现错误的应用程序，单击即可在下方弹出详细的错误信息，最后就可以根据错误原因来纠正错误。

![event](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-eventerror-websoft9-1.png)
![event](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-eventerror-websoft9-2.png)

#### 如何解决端口冲突？

默认下，Apache默认端口为80，MySQL默认端口为3306；可以通过cmd控制台输入指令：netstat -ano，查看服务器端口的使用情况。  

如果发送端口冲突故障，具体解决方法如下：

1. 找到 Apache 的配置文件（包括 httpd.conf 和站点配置文件），将端口 80 改为其他端口，如：81，然后重启 Apache。
**注意：更改端口后，需要将安全组的对应端口开放出来，否则服务正常启动，但外网依然无法访问网站。**
2. 找到 MySQL 的配置文件 my.ini ，将其中的 port = 3306 改为其他端口，然后重启MySQL服务。
3. 通过 netstat -ano 命令查看是哪个程序或服务占用了 80 或 3306 端口，可根据 PID 到任务管理器或服务列表将其关闭，再重新启动 Apache 和 MySQL。

## 常见问题

#### 默认字符集是什么？

UTF-8

#### WAMP使用的是哪个MPM模块？
[Apache MPM winnt](http://httpd.apache.org/docs/current/mod/mpm_winnt.html)

#### Apache 虚拟主机配置文件是什么？

虚拟主机配置文件是 Apache 用于管理多个网站的**配置段集合**，路径为：*C:\websoft9\wampstack\apache2\conf\bitnami\bitnami-apps-vhosts.conf*。  
每个配置段的形式为： `<VirtualHost *:80> ...</VirtualHost>`，有多少个网站就有多少个配置段

#### 如何修改示例网站根目录？

示例网站路径信息 *C:\wwwroot* 存放在 [Apache 虚拟主机配置文件](/zh/stack-components.md#apache)中

#### WAMP 环境是否支持部署多个网站？

支持。每增加一个网站，只需在[Apache 虚拟主机配置文件](/zh/stack-components.md#apache)中增加对应的  VirtualHost 即可。

#### 如何设置 phpMyAdmin 只允许在127.0.0.1访问？

镜像默认开启了 phpMyAdmin 远程访问，若想关闭之，请修改：*C:\websoft9\wampstack\apps\phpmyadmin\conf\httpd-vhosts.conf* 

找到如下 `<ifDefine APACHE24>...</ifDefine>` 配置项 

```
  <ifDefine APACHE24>
		#Require local
		Require all granted
	</ifDefine>
  
  修改成

  <ifDefine APACHE24>
		Require local
		#Require all granted
	</ifDefine>
```

#### 如何禁止外界访问phpMyAdmin？

连接服务器，编辑 [phpMyAdmin 配置文件](/zh/stack-components.md#phpmyadmin)，将其中的 `Require all granted` 更改为 `Require ip 192.160.1.0`，然后重启 Apache 服务

修改后[重启 WAMP 所有服务](/zh/admin-services.md)后生效

#### 如果没有域名是否可以部署 WAMP？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：*http://服务器公网IP/phpmyadmin*

#### 网站源码路径如何修改？

通过修改 [Apache 虚拟主机配置文件](/zh/stack-components.md#apache) 中相关路径参数

#### 如何删除9Panel?

删除 */data/apps/9panel* 下的所有数据即可，但需要保留文件夹

#### 通过 SFTP 上传网站源码后是否需要修改拥有者权限？

不需要，WAMP 会自动修正

#### 如果设置 HTTP 跳转到 HTTPS？

建议在网站根目录下的.htacesss文件中增加redirect规则，参考如下：
```
RewriteEngine on
RewriteBase /
RewriteCond %{SERVER_PORT} !^443$
RewriteRule ^.*$ https://%{SERVER_NAME}%{REQUEST_URI} [L,R]
```
#### WAMP 默认安装了哪些 Apache模块？ 

可以通过 WAMP 可视化界面查看

#### WAMP 默认安装了哪些 PHP 模块？

可以通过 WAMP 可视化界面查看

#### 如何启用或禁用 Apache 模块？

可以通过 WAMP 可视化界面设置

#### 如何禁用IP访问网站，防止恶意解析？

参考 [Apache 相关配置文档](https://support.websoft9.com/docs/windows/zh/webs-apache.html#禁用ip访问-防止恶意解析)

#### 没有域名是否可以通过 http://公网IP/mysite1 这样的方式访问网站？

可以。具体配置方法参考 [安装网站](/zh/solution-deployment.md#安装第二个网站)

