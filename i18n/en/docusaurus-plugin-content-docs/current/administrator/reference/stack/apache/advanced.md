---
slug: /apache/advanced
---

# Advanced

## 安装

安装 Apache 最简单的方式就是在线安装：

###  安装内核

```
# Installing on Fedora/CentOS/Red Hat Enterprise Linux
sudo yum install httpd
sudo systemctl enable httpd
sudo systemctl start httpd

# Installing on Ubuntu/Debian
sudo apt install apache2
sudo service apache2 start
```
> 安装Apache的时候默认会安装核心特性与多处理模块(MPM)，其他的扩展模块可以后续自行安装。  

### 安装模块{#moudle}

安装 Apache HTTP Server 内核的同时，会默认安装一些模块，通过 `apachectl -M` 命令即可查看。

```
$ apachectl -M
Loaded Modules:
 core_module (static)
 so_module (static)
 ...
```  

安装模块有yum/apt在线安装和源码编译安装两种方式，其中在线安装非常简单：

**在线安装**

例如：准备在CentOS上安装 `mod_ssl` 模块:

1. 搜索 mod_ssl 是否存在

   ```
   sudo yum search mod_ssl
   ============================= N/S matched: mod_ssl =============================
   mod_ssl.x86_64 : SSL/TLS module for the Apache HTTP Server
   ```

2. 搜索结果提示有一个 mod_ssl.x86_64 可用，接下来运行安装命令
   ```
   sudo yum install mod_ssl
   ```
3. 等待自动安装，直至安装完成

**源码安装**

如果在线搜索找不到所需的 Module, 就需要通过**源码编译安装**的方式安装新的模块。主要步骤如下：

1. 安装 apxs 这个Apache模块管理工具以及配套工具
   ```
   yum install httpd-devel
   yum groupinstall 'Development tools'
   ```
2. 下载 Apache 源码到 /opt 目录，并解压之
   ```
   cd /opt
   wget http://mirror.bit.edu.cn/apache//httpd/httpd-2.4.41.tar.gz
   tar xvf httpd-2.4.41.tar.gz
   ```
3. 以安装 mod_auth_form 模块为例，我们找到其所在的目录，然后运行编译命令
   ```
   cd /opt/httpd-2.4.41/modules/aaa
   mod_auth_form.c
   ```
4. 编译成功，会增加一个模块配置文件：/usr/lib64/httpd/modules/mod_auth_form.so

> 以上的源码编译安装方案来源于[此处](https://www.hugeserver.com/kb/install-enable-mod_evasive-apache-module-centos7/)

### 启停模块{#moudlesconf}

需要注意的是，安装过的所有模块并不会全部被启用，即安装模块与启用是有区别的，只有安装之后才能被启用，被启用的模块也可以让它停止运行。接下来，我们讲解如何启停模块。

下面先介绍通过修改模块配置文件实现模块启用的方案：  

以CentOS为例，我们打开Apache模块配置文件：*/etc/httpd/conf.modules.d/00-base.conf*

```
...
LoadModule version_module modules/mod_version.so
LoadModule vhost_alias_module modules/mod_vhost_alias.so
#LoadModule buffer_module modules/mod_buffer.so
#LoadModule watchdog_module modules/mod_watchdog.so
...
```
其中带“#”号的模块是没有启用的，如果需要启用，去掉“#”号，然后重启 Apache HTTP 服务即可。

修改Apache配置文件显得繁琐，可以安装通过`a2enmod`这个模块来管理Apache扩展模块的启停

### 更新

Apache HTTP Server在安全性方面有良好记录，并且开发人员社区高度关注安全性问题。但是，不可避免的是，某些问题（无论大小）都会在发布后在软件中发现。因此，保持对软件更新的了解至关重要。如果您直接从Apache获得HTTP Server的版本，我们强烈建议您订阅[Apache HTTP Server](http://httpd.apache.org/lists.html#http-announce)公告列表，在其中可以随时了解新版本和安全更新。


## 原理

### 配置

Apache HTTP Sever 提供了灵活的配置项，以帮助用户适用各种业务场景。

#### 配置文件

* 主配置文件：*/etc/httpd/conf/httpd.conf*
* 扩展配置文件：*/etc/httpd/conf.d/*.conf*

当Apache启动时，会加载/etc/httpd/conf.d/目录中的所有以.conf结尾的文件，做为配置文件来使用，所以管理员可以将配置推荐写在.conf中，如果将配置项写入主配置文件，系统升级时，配置项还要重新修改一遍，如果写在扩展配置项，则不存在此问题，同时也可以从繁杂的主配置文件中脱离出来。

#### 配置项

| 配置项 | 说明                                  |
| ------- | ---------------------------------------------- |
| ServerTokens OS | 系统信息,在访问出错时出现;把OS改为Minor,就不显示系统信息 |
| ServerSignature On | 把On改为Off就连普通的系统都给隐藏起来;改为Email就会显示管理员的邮箱(邮箱需要另外配置 ServerAdmin ) |
| ServerAdmin root@localhost | 管理员邮箱 |
| ServerName localhost | 服务器的主机名,一般是用虚拟机来设置,通常这个值是自动指定的，推荐显式的指定它以防止启动时出错 |
| UseCanonicalName Off | 设置为"On",Apache会使用ServerName指令的值  设置为 "Off"时,Apache会使用用户端提供的主机名和端口号。  如果有虚拟主机，必须设置为Off |
| ServerRoot "/etc/httpd" | 配置项的根目录，类似html里面的base;默认到这个路径里面找; |
| PidFile run/httpd.pid | 进程PID,位置在 /etc/httpd/run/httpd.pid,主进程决定着子进程 |
| Timeout 60 | 若60秒后没有收到或送出任何数据就切断该连接 |
| KeepAlive Off | 是否开启持久化链接,访问网站时要对网站的很多资源,如css,js,image等等创建不同的链接;事实上我们可以建立一个持久化链接来应对多个请求; |
| MaxKeepAliveRequests 100 | 一个持久化链接最多能应对多少个请求 |
| KeepAliveTimeout 15 | 15秒不链接就断开 |
| Listen 80 | 监听端口,默认是80，如果这里要更改为其他端口比如88的话,下面的ServerName localhost:88也得更改 |
| KeepAliveTimeout 15 | 15秒不链接就断开 |
| Include conf.d/*.conf | 扩展配置文件 |
| User apache | Apache子进程所有者 |
| Group apache | Apache子进程所属组 |
| DirectoryIndex index.html index.html.var | 默认主文件 |
| DocumentRoot "/var/www/html" | 网站数据根目录 |
| ErrorDocument 404 /404.html | 404可以通过PHP程序来处理(在框架中),可以通过rewrite来处理,但是最理想的模式是让Apache来处理	 |
| Directory | 定位目录 /(也就是Apache网站根目录) |
| Indexes | 如果访问的文件不存在，显示目录文件列表；要禁止的话前面加上一个 - （-indexes） |
| FollowSymLinks | 软链接 |
| AllowOverride  | 是否允许目录配置文件.htaccess有效ALL有效，None无效 |
| IfModule | 如果存在模块mod_userdir.c... |

配置注意事项：

1. Apache对文件的操作就会用系统给的一个临时账号Apache作为第三方other来运行
2. Apache的配置规则是 **后出现,先应用** 后面的出现的配置会覆盖前面的。
3. 以上配置都应该在扩展配置里面覆盖更改或增加;

### 核心模块

#### 多处理

Apache HTTP 服务器被设计为一个功能强大，并且灵活的 web 服务器， 可以在很多平台与环境中工作。不同平台和不同的环境往往需要不同的特性，或可能以不同的方式实现相同的特性最有效率。  

Apache httpd 通过模块化的设计来适应各种环境。这种设计允许网站管理员通过在编译时或运行时，选择哪些模块将会加载在服务器中，来选择服务器特性。  

Apache提供一个名称为多处理模块(MPM)，用来接受请求， 以及调度子进程处理请求。

下表列出了不同系统的默认 MPM。如果你不在编译时选择，那么它就是你将要使用的 MPM。

| 操作系统 | MPM名称                                  |
| ------- | ---------------------------------------------- |
| Netware | `mpm_netware`                                  |
| OS/2    | `mpmt_os2`                                     |
| Unix    | `prefork`，`worker` 或 `event`，取决于平台特性 |
| Windows | `mpm_winnt`                                    |

**查看 MPM**

以CentOS为例，查看当前系统的MPM模式，只需运行 `httpd -V` 命令即可查看：
```
[root@lamp7 ~]# httpd -V
Server version: Apache/2.4.6 (CentOS)
Server built:   Aug  8 2019 11:41:18
Server's Module Magic Number: 20120211:24
Server loaded:  APR 1.4.8, APR-UTIL 1.5.2
Compiled using: APR 1.4.8, APR-UTIL 1.5.2
Architecture:   64-bit
Server MPM:     prefork
  threaded:     no
    forked:     yes (variable process count)
```

另外，在Apache主配置文件：*/etc/httpd/conf/httpd.conf* 中，可以设置 prefork 的工作参数：
```
<IfModule prefork.c>
   StartServers        5
   MinSpareServers     5
   MaxSpareServers     10
   MaxClients          256
   MaxRequestsPerChild 3000
</IfModule>
```

**切换 MPM**

以CentOS为例，切换当前系统的MPM模式，编辑：*/etc/httpd/conf.modules.d/00-mpm.conf* 文件
```
LoadModule mpm_prefork_module modules/mod_mpm_prefork.so
#LoadModule mpm_worker_module modules/mod_mpm_worker.so
#LoadModule mpm_event_module modules/mod_mpm_event.so
```

通过去掉或增加“#”号的方式，选择一种MPM模式，重启Apache后生效

**比较 MPM**

![prefork](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/prefork-websoft9.png)  
图1：Prefork，每个子进程只有一个线程，在一个时间点内只能处理一个请求  

![worker](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/worker-websoft9.png)  
图2：work，多进程和多线程的混合模式  

![event](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/event-websoft9.png)  
图1：event，与worker类似，但是event解决了worker下长连接线程的阻塞问题  

三种MPM模式之间的比较请参考：
* [《Apache 工作的三种模式：Prefork、Worker、Events》](https://www.jianshu.com/p/2de515e958d6)
* [《青蛙学Linux—Apache的MPM模式和httpd-mpm.conf》](https://www.cnblogs.com/yu2006070-01/p/10303808.html)

#### 代理

Apache中的代理即 mod_proxy 模块，它用于  URL的转发，即具有代理的功能。应用此功能，可以很方便的实现同 Tomcat 等应用服务器的整合，甚至可以很方便的实现 Web 集群的功能。 

Apache 代理相关的模块包括：

```
mod_proxy
proxy_ajp_module (shared)
proxy_balancer_module (shared)
proxy_connect_module (shared)
proxy_express_module (shared)
proxy_fcgi_module (shared)
proxy_fdpass_module (shared)
proxy_ftp_module (shared)
proxy_http_module (shared)
proxy_scgi_module (shared)
proxy_wstunnel_module (shared)
```
Apache代理使用详情参考：[《Apache模块mod_proxy》](http://httpd.apache.org/docs/2.4/mod/mod_proxy.html)

#### 日志

为了有效地管理Web服务器，有必要获取有关服务器的活动和性能以及可能发生的任何问题的反馈。Apache HTTP Server提供了非常全面和灵活的日志记录功能。

Apache标准日志包括：访问日志和错误日志两种。其中与日志相关的模块包括：
```
mod_log_config
mod_log_forensic
mod_logio
mod_cgi
```

**访问日志**

Apache 访问日志在实际工作中非常有用，比较典型的例子是进行网站流量统计，查看用户访问时间、地理位置分布、页面点击率等。Apache 的访问日志具有如下4个方面的作用：

- 记录访问服务器的远程主机IP 地址，从而可以得知浏览者来自何处；
- 记录浏览者访问的Web资源，可以了解网站中的哪些部分最受欢迎；
- 记录浏览者使用的浏览器，可以根据大多数浏览者使用的浏览器对站点进行优化；
- 记录浏览者的访问时间；

**错误日志**

服务器错误日志（由ErrorLog伪指令设置名称和位置）是最重要的日志文件。Apache httpd将在此处发送诊断信息并记录其在处理请求时遇到的任何错误。当启动服务器或服务器操作出现问题时，它是第一个查看的地方，因为它通常包含发生问题的原因以及如何解决的详细信息。  

错误日志的格式由ErrorLogFormat指令定义，您可以使用该指令自定义要记录的值。如果未指定格式，则默认为格式定义。典型的日志消息如下：

```
[Fri Sep 09 10:42:29.902022 2011] [core:error] [pid 35708:tid 4328636416] [client 72.15.99.187] File does not exist: /usr/local/apache2/htdocs/favicon.ico
```

日志条目中的第一项是消息的日期和时间。接下来是产生消息的模块（在这种情况下为核心）和消息的严重性级别。紧随其后的是遇到该条件的进程的进程ID，如果合适，还包括线程ID。接下来，我们有发出请求的客户地址。最后是详细的错误消息，在这种情况下，该错误消息表示请求的文件不存在。

#### SSL/TLS 加密

Apache SSL/TLS 依赖于mod_ssl模块，这个模块基于OpenSSL，它使用安全套接字层和传输层安全协议提供了强加密。
下图是典型的使用 SSL 加密的网页认证连接流程：

![ssl认证](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/client-ssl-auth.png)

下面配置段是典型的HTTPS设置项

```
LoadModule ssl_module modules/mod_ssl.so
Listen 443
<VirtualHost *:443>
    ServerName www.example.com
    SSLEngine on
    SSLCertificateFile "/path/to/www.example.com.cert"
    SSLCertificateKeyFile "/path/to/www.example.com.key"
</VirtualHost>
```

## 问题解答{#faq}

#### 如何取消 Apache Test 页面？

使用 # 号将: */etc/httpd/conf.d/welcome.conf* 中的所有内容全部注释掉，然后重启 Apache 服务

#### mod_php 模块与 php-fpm 冲突吗？ 

Apache 默认会安装 mod_php 模块。如果采用 php-fpm 服务来解析PHP文件，mod_php 不会与之冲突。

#### 如何启用或禁用 Apache 模块？

以伪静态模块为例：

1. 打开 [Apache模块配置文件](../apache#path)，找到 *LoadModule rewrite_module modules/mod_rewrite.so*
2. 通过“#”作为注释来开启或禁用此模块

#### Apache 虚拟主机配置文件是什么？

虚拟主机配置文件是 Apache 用于管理多个网站的**配置段集合**

* 路径为：*/etc/httpd/conf.d/vhost.conf*。  
* 每个配置段的形式为： `<VirtualHost *:80> ...</VirtualHost>`，有多少个网站就有多少个配置段

