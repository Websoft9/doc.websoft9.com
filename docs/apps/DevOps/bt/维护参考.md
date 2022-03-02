---
sidebar_position: 2
slug: /bt/admin
tags:
  - BT
  - 宝塔面板
  - 运行环境
---


# 维护参考

## 系统参数

BT 预装包包含 BT 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### Linux 版

*   安装目录：*/www/server*
*   网站目录：*/www/wwwroot/default*
*   Apache目录：*/www/server/httpd*
*   Nginx目录：*/www/server/nginx*
*   MySQL目录：*/www/server/mysql*
*   PHP目录：*/www/server/php*
*   Redis目录：*/www/server/redis*
*   Memcached目录：/usr/local/memcached*
*   日志目录：*/www/wwwlogs*

访问方式：Web面板

#### Windows 版

*   安装目录：*C:\BtSoft\ServerAdmin*
*   网站目录：*C:\wwwroot*
*   MySQL 目录：*C:\BtSoft\mysql*
*   Apache 日志文件：*C:\BtSoft\apache\logs*

访问方式：Web面板 或 服务器客户端

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过 HTTP 访问你的网站 | 必须 |
| HTTPS | 443 | 通过 HTTPS 访问你的网站 | 可选 |
| BT| 8888 | 访问 宝塔 Linux 版的管理界面 | 必须 |
| MySQL | 3306 | 远程连接 MySQL | 可选 |

### 版本号

组件版本号可以宝塔控制台查看。

### 服务

使用由Websoft9提供的 BT 部署方案，可能需要用到的服务如下：

#### BT 启停

通过控制台，启动和关闭 BT 面板  

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btlinux/bt-disablebt-websoft9.png)

或运行命令

```shell
sudo service bt start
sudo service bt stop
sudo service bt restart

## 删除（慎用）
service bt stop && chkconfig --del bt && rm -f /etc/init.d/bt && rm -rf /www/server/panel
```


#### Apache

```shell
##For Ubuntu&Debian
sudo systemctl start apache2
sudo systemctl stop apache2
sudo systemctl restart apache2
sudo systemctl status apache2

##For Centos&Redhat
sudo systemctl start httpd
sudo systemctl stop httpd
sudo systemctl restart httpd
sudo systemctl status httpd
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

#### MySQL&MariaDB

```shell
sudo systemctl start mysql
sudo systemctl stop mysql
sudo systemctl restart mysql
sudo systemctl status mysql
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

1. 通过 WinSCP 将网站目录**压缩后**再完整的下载到本地
2. 导出 BT 数据库
3. 将程序文件、数据文件和数据库文件放到同一个文件夹，根据日期命名
4. 备份工作完成

###  BT自动备份

宝塔提供的计划任务功能，可以实现自动网站的自动备份

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btwin/bt-taskbackup-websoft9.png)

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

### Window 系统

Windows服务器的更新与本地电脑类似，手动找到更新管理程序，设置自动下载自动更新即可。

### 宝塔升级

#### 宝塔内核升级

宝塔提供了一键在线升级功能，只要根据系统提示，点击升级按钮即可完成升级

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/btlinux/bt-update001-websoft9.png)

#### 环境组件升级

宝塔在使用中一般会安装大量的软件或组件，包括：php，mysql，phpmyadmin等，

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btwin/bt-win-intallhj-websoft9.png)

升级请参考官方教程《[宝塔-软件管理](https://www.kancloud.cn/chudong/bt2017/424281)》

## 故障处理

此处收集使用 BT 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 导入SQL出现乱码？

问：用宝塔里边的上传导入SQL，导入的SQL都是乱码！如果使用PHPMyAdmin就不会

答：不同的数据库客户端工具默认的编码格式可能有差异，宝塔里也可以使用phpmyadmin工具。

#### 网站数量过多，服务经常自动重启

问：一台服务器网站数量100个，发现服务经常自动重启

答：一台服务器上管理网站的数量请勿超过20个，否则初始资源不充裕的情况下会导致内存和CPU消耗殆尽，从而服务自动重启。理论上，一个网站最少需要0.5G的内存容量，如果有20个网站话，最低是16G内存。

#### Apache or Nginx 服务无法启动？

最常见的原因是配置文件语法错误，具体请通过分析日志文件定位原因

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```

#### 宝塔的登录地址不对？

待研究

## 常见问题


#### BT 支持多语言吗？

支持中英文语言，但需要在部署之前选定语言，即安装中文版或英文版

#### BT Windows 面板支持哪些操作系统？

支持 Windows Server 2008/2012/2016/2019 64位

#### 宝塔的账号绑定是必须的吗？

不是。您可以直接访问： *http://服务器公网IP:8888/soft* 绕开绑定。

#### 宝塔 Linux 版 VS 宝塔 Window 版？

下面按照操作系统的不同，将宝塔的功能清单做一个对比说明，供您参考：

|  功能  |  Linux  |  Windows  |
| --- | --- | --- |
| 应用服务   |  Apache, Nginx, Tomcat, OpenLiteSpeed  | Apache, Nginx, IIS   |
|  程序语言  |   PHP5.2-php8.0, Java, Node |   PHP5.2-php8.0, Node |
|   FTP |  Pure-Ftpd  |  FileZilla Server |
|   数据库 |  MySQL, MongoDB  |  MySQL, SQLServer Express, MongoDB  |
|  数据库工具  | phpMyAdmin   |  phpMyAdmin  |
|  缓存  |  Redis, Memcached  |  Redis, Memcached   |
| 外部存储接口    |  七牛云，阿里云，又拍云，FTP存储空间  | 阿里云，又拍云，FTP存储空间   |
|  插件 |   宝塔运维，宝塔安全登录，云解析，PHP守护，宝塔跑分，宝塔一键迁移等 |  宝塔运维，宝塔安全登录，宝塔-主服务，宝塔一键部署源码，宝塔一键迁移等   |
|  其他  |  Linux工具箱, Docker  | ImageMagick，Windows设置工具   |

> 建议选更稳定可靠的 宝塔 Linux 版

#### 宝塔能帮我做什么？是必须的吗？

**从业务场景的角度看**，宝塔适合多网站、多用户管理，即您的服务器上管理多个网站，每个网站属于不同的用户/客户，这种情况下，宝塔非常管用。

**从技术的角度上看**，如果您有如下的技术需求，宝塔是可以帮助您的：

* 需要服务器支持PHP多版本，甚至Java，.NET共存（虽然不建议这样做）
* 不擅长通过修改配置文件去实现多网站、https等设置
* 不擅长设置多个FTP
* 希望可以监控服务器运行状态（CPU、内存、流量监控图表等）
* 希望通过可视化解决管理防火墙和端口更改
* 希望通过可视化界面计划任务设置
* 希望常见的服务器软件可以在线安装

总之，如果在技术配置上有可视化需求的您，您会觉得宝塔是很贴心的工具。

但需要注意的是，对运行服务器来说，环境越简单、所安装的软件越少、网站数量越少，服务运行就更加稳定可靠。万事万物都不完美，宝塔良好的用户体验和全面覆盖性，也是有代价的。

> 总结：宝塔是很好用的，但是宝塔不是必须的

#### 宝塔可以管理多少网站？

宝塔官方并没有关于网站数量上限的说明。但从实际运维经验来看，建议一台使用宝塔的云服务器上最好不要超过20个网站。


#### 如果没有域名是否可以部署 BT？

可以

#### 是否有可视化的数据库管理工具？

宝塔安装 LAMP 或 LNMP 的时候默认安装 phpMyAdmin

#### 宝塔 Windows 面板的桌面客户端有什么作用？

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btwin/bt-wintools-websoft9.png)

主要用于配置域名、安装授权、重置密码、启停宝塔服务等。


#### 是否可以修改 BT 的源码路径？

不可以

#### 如何修改上传的文件所属用户（组）和读写权限?

通过宝塔后台的文件管理修改权限  
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btlinux/bt-quanxian-websoft9.png)


#### 用 phpMyAdmin 还是 BT 后台管理数据库？

虽然宝塔有数据库管理功能，但实际上数据库管理是一件复杂而严谨的事情，与 MySQL 最匹配的可视化管理工具是 phpMyAdmin，建议使用 phpMyAdmin 完成如下操作：

*   数据导入与导出
*   修改数据库密码
*   增加用户
*   修改字符集
*   SQL语言的运用

#### 为什么 BT 防火墙设置没有生效？

宝塔的【安全】>【防火墙】设置中，有灵活的服务器操作系统的端口设置功能。但不建议通过此处设置端口，为什么呢？  

当我们在云服务器上使用宝塔的时候，云服务器厂商的安全组中已经有了端口设置，且云厂商安全组的设置优先级大于宝塔防火墙对应的设置。

例如：在宝塔中开放了80端口，而安全组中80端口是关闭，最终结果80端口仍然是关闭的。即宝塔中设置与否，不起决定作用，所以还是不设置为好。

#### BT 面板奔溃了怎么办？

宝塔面板会奔溃吗？任何软件都会出问题
宝塔奔溃的几率大吗？不大，但需要预防

宝塔是面板，面板工具都是调用操作系统层面的东西。对应宝塔奔溃之后的处理，需要掌握如下知识点：

*   宝塔的基础环境安装在哪里？是否可用？
*   数据库是否可用？
*   网站文件在哪里？
*   是否能够实现快速备份

掌握以上几点，也许能够力挽狂澜

#### 可以使用BT网站搬家功能吗？

请勿轻易使用任何形式的一站搬家这样的功能
