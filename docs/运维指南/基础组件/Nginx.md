# Nginx

[Nginx](http://nginx.org/)("engine x")是一款是由俄罗斯的程序设计师Igor Sysoev所开发高性能的Web和反向代理服务器，具有优异的静态资源处理能力，同时也是一个 IMAP/POP3/SMTP 代理服务器。在高连接并发的情况下，Nginx是Apache服务器不错的替代品。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nginx/nginx-architecture-websoft9.png)

本章所提及的Nginx，具体是指NGINX Open Source（即Nginx开源Web服务器）。实际上：

Nginx公司还有企业级的商业产品：  

* NGINX Plus  
* NGINX Controller  
* NGINX Unit  
* NGINX Amplify  
* NGINX WAF  

同时基于Nginx的著名开源项目包括：

* Tengine：由淘宝网发起的Web服务器项目。它在Nginx的基础上，针对大访问量网站的需求，添加了很多高级功能和特性。
* OpenResty：一个基于 Nginx 与 Lua 的高性能 Web 平台，其内部集成了大量精良的 Lua 库、第三方模块以及大多数的依赖项。用于方便地搭建能够处理超高并发、扩展性极高的动态 Web 应用、Web 服务和动态网关。

## 安装

安装Nginx有在线包安装和源码编译安装两种方式。其中在线安装通常称之为 yum/apt 安装，而源码安装即需要下载源码然后进行编译后方可使用。

相比源码编译安装来说，在线安装非常简单，下面是在线安装的范例：

```
# Fedora/CentOS/Red Hat
sudo yum install nginx
sudo systemctl enable nginx
sudo systemctl start nginx

# Ubuntu/Debian
sudo apt install nginx
sudo service nginx start
```

## 命令和服务

### 命令

安装完成之后，系统生成一个可以运行的Nginx命令，它提供几个可选参数：

```
-c <path_to_config>：使用指定的配置文件而不是 conf 目录下的 nginx.conf 。

-t：测试配置文件是否正确，在运行时需要重新加载配置的时候，此命令非常重要，用来检测所修改的配置文件是否有语法错误。

-v：显示 nginx 版本号。

-V：显示 nginx 的版本号以及编译环境信息以及编译时的参数。
```

### 服务

在不同的操作系统下，Nginx对应的服务启停如下：

```
#CentOS or Redhat
systemctl start httpd
systemctl stop httpd
systemctl restart httpd
systemctl status httpd

# Ubutnu
systemctl start apache2
systemctl stop apache2
systemctl restart apache2
systemctl status apache2
```

## 模块

Nginx 采用模块化设计机制，各个模块协作共同完成处理任务。主要模块分类：

* 核心模块：核心模块是指Nginx服务器正常运行时必不可少的模块，它们提供了Nginx最基本最核心的服务，如进程管理、权限控制、错误日志记录等
* 标准HTTP模块：编译Nginx后包含的模块，其支持Nginx服务器的标准HTTP功能。
* 可选HTTP模块：主要用于扩展标准的HTTP功能，使其能够处理一些特殊的HTTP请求。在编译Nginx时，如果不指定这些模块，默认是不会安装的。
* 邮件模块：主要用于支持Ningx的邮件服务。
* 第三方模块：由第三方机构或者个人开发的模块，用于实现某种特殊功能。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nginx/nginx-modules-websoft9.png)

安装模块之前，先查看当前已安装的所有模块，然后再决定是否安装，最后将已安装模块启用或停止。

更多模块机制参考博客：[Nginx 模块及运行机制](https://www.cnblogs.com/zy09/p/10273399.html)

### 查看

通过 `nginx -V` 命令可以查看已经安装的所有Nginx模块。  

```bash
~# nginx -V
nginx version: nginx/1.12.2
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC)
built with OpenSSL 1.0.2k-fips  26 Jan 2017
TLS SNI support enabled
configure arguments: 
--prefix=/usr/share/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib64/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --http-client-body-temp-path=/var/lib/nginx/tmp/client_body --http-proxy-temp-path=/var/lib/nginx/tmp/proxy --http-fastcgi-temp-path=/var/lib/nginx/tmp/fastcgi --http-uwsgi-temp-path=/var/lib/nginx/tmp/uwsgi --http-scgi-temp-path=/var/lib/nginx/tmp/scgi --pid-path=/run/nginx.pid --lock-path=/run/lock/subsys/nginx --user=nginx --group=nginx --with-file-aio --with-ipv6 --with-http_auth_request_module --with-http_ssl_module --with-http_v2_module --with-http_realip_module --with-http_addition_module --with-http_xslt_module=dynamic --with-http_image_filter_module=dynamic --with-http_geoip_module=dynamic --with-http_sub_module --with-http_dav_module --with-http_flv_module --with-http_mp4_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_random_index_module --with-http_secure_link_module --with-http_degradation_module --with-http_slice_module --with-http_stub_status_module --with-http_perl_module=dynamic --with-mail=dynamic --with-mail_ssl_module --with-pcre --with-pcre-jit --with-stream=dynamic --with-stream_ssl_module --with-google_perftools_module --with-debug --with-cc-opt='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic' --with-ld-opt='-Wl,-z,relro -specs=/usr/lib/rpm/redhat/redhat-hardened-ld -Wl,-E'
```

### 安装

### 启停


## 路径

不同的Linux发行版，对应的安装路径有一定的差异：

### CentOS

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*

### Ubuntu

Nginx 虚拟主机配置文件：*/etc/nginx/sites-available/default*  
Nginx 主配置文件：*/etc/nginx/nginx.conf*  
Nginx 日志文件：*/var/log/nginx/*


## 性能管理

以下内容参考：[《nginx性能优化 汇总篇》](https://www.cnblogs.com/yyxianren/p/12106362.html) 和[《使用 Nginx 提升网站访问速度》](https://www.ibm.com/developerworks/cn/web/wa-lo-nginx/index.html)


### 进程模型

NGINX有一个主进程（master process）（执行特权操作，如读取配置、绑定端口）和一系列工作进程（worker process）和辅助进程（helper process）。
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nginx/nginx-processes-websoft9.png)

Nginx运行工作进程个数一般设置CPU的核心或者核心数x2。下面是一台2核CPU服务器的Nginx相关进程查看，有1个主进程，2个子进程，还有一个辅助进程。

```
[root@nginx]# ps -ef --forest | grep nginx
root       747     1  0 11:48 ?        00:00:00 nginx: master process /usr/sbin/nginx
nginx      752   747  0 11:48 ?        00:00:00  \_ nginx: worker process
nginx      753   747  0 11:48 ?        00:00:00  \_ nginx: worker process
root      1756  1708  0 17:04 pts/0    00:00:00          \_ grep --color=auto nginx
```
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nginx/nginx-processmaster-websoft9.jpg)


通过信号对 Nginx 进行控制

### IO多路复用

一般情况下并发处理机制有三种：多进程、多线程，与异步机制。Nginx对于并发的处理同时采用了三种机制。Nginx的进程分为两类：master进程与worker进程。每个master进程可以生成多个worker进程，所以其是多进程的。每个worker进程可以同时处理多个用户请求，每个用户请求会由一个线程来处理，所以其是多线程的  

对于操作系统而言，IO多路复用就是要完成操作系统IO的请求。对于IO文件的请求，当一个IO流要进行文件处理的时候，要获取一组文件的描述符，当文件描述符还没有就绪时，那么它就在等待，直到描述符一旦就绪，马上上报系统通知的机制，告诉应用程序我准备就绪，你可以来操作了。这就是IO多路复用的方式。  

worker进程采用的就是epoll多路复用机制来对后端服务器进行处理的。当后端服务器返回结果后，后端服务器就会回调epoll多路复用器，由多路复用器对相应的worker进程进行通知。此时，worker进程就会挂起当前正在处理的事务，拿IO返回结果去响应客户端请求。响应完毕后，会再继续执行挂起的事务。这个过程就是“异步非阻塞”的。

### 最大打开文件数

这个指令是指当一个Nginx进程打开的最多文件描述符数目，理论值应该是最多打开文件数（ulimit -n）与nginx进程数相除，但是nginx分配请求并不是那么均匀，所以最好与ulimit -n的值保持一致。

注：文件资源限制的配置可以在/etc/security/limits.conf设置，针对root/user等各个用户或者*代表所有用户来设置。
```
*   soft nofile   65535
*   hard nofile   65535
```

### 压缩

使用gzip压缩功能，可能为我们节约带宽，加快传输速度，有更好的体验，也为我们节约成本，所以说这是一个重点。Nginx启用压缩功能需要你来ngx_http_gzip_module模块，apache使用的是mod_deflate。

一般我们需要压缩的内容有：文本，js，html，css，对于图片，视频，flash什么的不压缩。
```
gzip on;
gzip_min_length 2k;
gzip_buffers   4 32k;
gzip_http_version 1.1;
gzip_comp_level 6;
gzip_typestext/plain text/css text/javascriptapplication/json application/javascript application/x-javascriptapplication/xml;
gzip_vary on;
gzip_proxied any;
gzip on;
```

## 配置

先来看一个实际的配置文件：

```
user  nobody;# 工作进程的属主
worker_processes  4;# 工作进程数，一般与 CPU 核数等同
 
#error_log  logs/error.log; 
#error_log  logs/error.log  notice; 
#error_log  logs/error.log  info; 
 
#pid        logs/nginx.pid; 
 
events { 
   use epoll;#Linux 下性能最好的 event 模式
   worker_connections  2048;# 每个工作进程允许最大的同时连接数
} 
 
http { 
   include       mime.types; 
   default_type  application/octet-stream; 
 
   #log_format  main  '$remote_addr - $remote_user [$time_local] $request ' 
   #                  '"$status" $body_bytes_sent "$http_referer" ' 
   #                  '"$http_user_agent" "$http_x_forwarded_for"'; 
 
   #access_log  off; 
   access_log  logs/access.log;# 日志文件名
 
   sendfile        on; 
   #tcp_nopush     on; 
   tcp_nodelay     on; 
 
   keepalive_timeout  65; 
 
   include      gzip.conf; 
    
   # 集群中的所有后台服务器的配置信息
   upstream tomcats { 
    server 192.168.0.11:8080 weight=10; 
    server 192.168.0.11:8081 weight=10; 
    server 192.168.0.12:8080 weight=10; 
    server 192.168.0.12:8081 weight=10; 
    server 192.168.0.13:8080 weight=10; 
    server 192.168.0.13:8081 weight=10; 
   } 
 
   server { 
       listen       80;#HTTP 的端口
       server_name  localhost; 
 
       charset utf-8; 
 
       #access_log  logs/host.access.log  main; 
 
    location ~ ^/NginxStatus/ { 
       stub_status on; #Nginx 状态监控配置
       access_log off; 
    } 
 
    location ~ ^/(WEB-INF)/ { 
       deny all; 
    } 
    
 
    location ~ \.(htm|html|asp|php|gif|jpg|jpeg|png|bmp|ico|rar|css|js|
    zip|java|jar|txt|flv|swf|mid|doc|ppt|xls|pdf|txt|mp3|wma)$ { 
            root /opt/webapp; 
       expires 24h; 
       } 
 
       location / { 
       proxy_pass http://tomcats;# 反向代理
       include proxy.conf; 
       } 
 
       error_page 404 /html/404.html; 
 
       # redirect server error pages to the static page /50x.html 
       # 
    error_page 502 503 /html/502.html; 
       error_page 500 504 /50x.html; 
       location = /50x.html { 
           root   html; 
       } 
   } 
}
```

### Nginx 监控

上面是一个实际网站的配置实例，其中灰色文字为配置说明。上述配置中，首先我们定义了一个 location ~ ^/NginxStatus/，这样通过 http://localhost/NginxStatus/ 就可以监控到 Nginx 的运行信息，显示的内容如下：

```
Active connections: 70 
server accepts handled requests
 14553819 14553819 19239266 
Reading: 0 Writing: 3 Waiting: 67
```

NginxStatus 显示的内容意思如下：

* active connections – 当前 Nginx 正处理的活动连接数。
* server accepts handled requests -- 总共处理了 14553819 个连接 , 成功创建 14553819 次握手 ( 证明中间没有失败的 ), 总共处理了 19239266 个请求 ( 平均每次握手处理了 1.3 个数据请求 )。
* reading -- nginx 读取到客户端的 Header 信息数。
* writing -- nginx 返回给客户端的 Header 信息数。
* waiting -- 开启 keep-alive 的情况下，这个值等于 active - (reading + writing)，意思就是 Nginx 已经处理完正在等候下一次请求指令的驻留连接。

### 静态文件处理

通过正则表达式，我们可让 Nginx 识别出各种静态文件，例如 images 路径下的所有请求可以写为：

```
location ~ ^/images/ {
root /opt/webapp/images;
}
```

而下面的配置则定义了几种文件类型的请求处理方式。

```
location ~ \.(htm|html|gif|jpg|jpeg|png|bmp|ico|css|js|txt)$ {
root /opt/webapp;
expires 24h;
}
```

对于例如图片、静态 HTML 文件、js 脚本文件和 css 样式文件等，我们希望 Nginx 直接处理并返回给浏览器，这样可以大大的加快网页浏览时的速度。因此对于这类文件我们需要通过 root 指令来指定文件的存放路径，同时因为这类文件并不常修改，通过 `expires` 指令来控制其在浏览器的缓存，以减少不必要的请求。 `expires` 指令可以控制 HTTP 应答中的“ Expires ”和“ Cache-Control ”的头标（起到控制页面缓存的作用）。您可以使用例如以下的格式来书写 Expires：

```
expires 1 January, 1970, 00:00:01 GMT;
expires 60s;
expires 30m;
expires 24h;
expires 1d;
expires max;
expires off;
```

### 动态页面请求处理

Nginx 本身并不支持现在流行的 JSP、ASP、PHP、PERL 等动态页面，但是它可以通过反向代理将请求发送到后端的服务器，例如 Tomcat、Apache、IIS 等来完成动态页面的请求处理。前面的配置示例中，我们首先定义了由 Nginx 直接处理的一些静态文件请求后，其他所有的请求通过 proxy_pass 指令传送给后端的服务器（在上述例子中是 Tomcat）。最简单的 `proxy_pass` 用法如下：

```
location / {
proxy_pass    http://localhost:8080;
proxy_set_header X-Real-IP $remote_addr;
}
```

这里我们没有使用到集群，而是将请求直接送到运行在 8080 端口的 Tomcat 服务上来完成类似 JSP 和 Servlet 的请求处理。

当页面的访问量非常大的时候，往往需要多个应用服务器来共同承担动态页面的执行操作，这时我们就需要使用集群的架构。 Nginx 通过 `upstream` 指令来定义一个服务器的集群，最前面那个完整的例子中我们定义了一个名为 tomcats 的集群，这个集群中包括了三台服务器共 6 个 Tomcat 服务。而 proxy_pass 指令的写法变成了：

```
location / {
proxy_pass    http://tomcats;
proxy_set_header X-Real-IP $remote_addr;}
```

在 Nginx 的集群配置中，Nginx 使用最简单的平均分配规则给集群中的每个节点分配请求。一旦某个节点失效时，或者重新起效时，Nginx 都会非常及时的处理状态的变化，以保证不会影响到用户的访问。

## 伪静态

### 基本设置

使用伪静态有三个步骤：

1. 确保已经安装Rewrite模块。
2. 在服务器目录 */etc/nginx/conf.d/rewrite* 下新建你网站的伪静态规则文件（例如：wordpress.conf）
3. 在网站的[虚拟主机配置段](/zh/stack-components.md#nginx) **server{ }** 中将伪静态规则文件 include 进来
   ```text
   server
   {
   listen 80;
   server_name mysite2.yourdomain.com;  # 此处修改为你的域名
   index index.html index.htm index.php;
   root  /data/wwwroot/mysite2;
   ...

   ## Includes one of your Rewrite rules if you need, examples
   include conf.d/rewrite/wordpress.conf;  # 引入你的伪静态规则
   }
   ```

### 场景

伪静态的常见场景包括：重定向、隐藏页面后缀名、.htaccess文件使用

## VirtualHost配置

Nginx中的虚拟主机是通过server{ } 进行配置的。

server{ } 改动务必准确无误，任何错误的修改都会导致服务器上所有的网站不可访问

|  server 项  |  作用说明  |  必要性 |
| --- | --- | --- |
|  server_name  |  域名，如果配置两个域名需以空格分开   |  必须填写 |
|  root |  网站存放目录  | 务必准确无误 |
|  error_log  | 错误日志路径，系统会根据定义的路径产生相关日志文件   |  可以不填或删除 |
|  access_log  | 访问日志路径，系统会根据定义的路径产生相关日志文件  |  可以不填或删除 |
|  ssl_certificate  | HTTPS 证书路径  |  设置 HTTPS 访问时必填 |
|  ssl_certificate_key  | HTTPS 证书秘钥路径   |  设置 HTTPS 访问时必填 |

### HTTP VirtualHost template

```
server
       {
        listen 80;
        server_name mysite2.yourdomain.com;
        index index.html index.htm index.php;
        root  /data/wwwroot/mysite2;
        error_log /var/log/nginx/mysite2.yourdomain.com-error.log crit;
        access_log  /var/log/nginx/mysite2.yourdomain.com-access.log;
        include conf.d/extra/*.conf;

        ## Includes one of your Rewrite rules if you need, examples
        # include conf.d/rewrite/wordpress.conf;
        # include conf.d/rewrite/joomla.conf;
        }
```

### Alias template

请将下面 Alias 模板插入到 default.conf 中已存在的 server{} 段中，并修改其中的 location,alias 

      ```
      location /mysite2
      {
       alias /data/wwwroot/mysite2;
       index index.php index.html;
       location ~ ^/mysite2/.+\.php$ {
        alias /data/wwwroot/mysite2;
        fastcgi_pass  unix:/dev/shm/php-fpm-default.sock;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME /data/wwwroot/$fastcgi_script_name;
        include        fastcgi_params; }
      include conf.d/extra/*.conf;
      }
      ```
      ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lnmp/lnmp-insertalias-websoft9.png)

      注意：Alias 模板只能插入到 server{} 配置段中

### HTTPS VirtualHost template

HTTPS 配置项 到对应的 HTTP server{ } 段落中

```
#-----HTTPS template start------------
listen 443 ssl; 
ssl_certificate /data/cert/xxx.crt;
ssl_certificate_key /data/cert/xxx.key;
ssl_session_timeout 5m;
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
ssl_prefer_server_ciphers on;
#-----HTTPS template end------------
```

### 特殊场景

虚拟主机配置的更多特殊场景包括：默认首页名称顺序、禁用IP访问,防止恶意解析等


## 代理

Proxy_pass反向代理，用的是nginx的Proxy模块。

```
第一种：
location /proxy/ {
    proxy_pass http://127.0.0.1/;
}
代理到URL：http://127.0.0.1/test.html


第二种：
location /proxy/ {
    proxy_pass http://127.0.0.1;  #少/
}
代理到URL：http://127.0.0.1/proxy/test.html


第三种：
location /proxy/ {
    proxy_pass http://127.0.0.1/aaa/;
}
代理到URL：http://127.0.0.1/aaa/test.html


第四种（相对于第三种，最后少一个 / ）
location /proxy/ {
    proxy_pass http://127.0.0.1/aaa;
}
代理到URL：http://127.0.0.1/aaatest.html
```

```
- proxy_set_header  Host  $host;  作用web服务器上有多个站点时，用该参数header来区分反向代理哪个域名。比如下边的代码举例。
- proxy_set_header X-Forwarded-For  $remote_addr; 作用是后端服务器上的程序获取访客真实IP，从该header头获取。部分程序需要该功能。
```

## 负载均衡

本节来源于：https://www.jianshu.com/p/10ecc107b5ee

Proxy_pass配合upstream实现负载均衡。

Nginx负载均衡的几种模式：

* 轮询：每个请求按时间顺序逐一分配到不同的后端服务器，如果后端服务器down掉，就不在分配；
* 权重轮询：根据后端服务器性能不通配置轮询的权重比，权重越高访问的比重越高；
* IP_Hash：根据请求的ip地址hash结果进行分配，第一次分配到A服务器，后面再请求默认还是分配到A服务器；可以解决Session失效重新登录问题；
* Fair：按后端服务器的响应时间来分配请求，响应时间短的优先分配；
* Url_hash：按访问url的hash结果来分配请求，使每个url定向到同一个后端服务器，后端服务器为缓存时比较有效；


```
http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
 
    upstream core_tomcat {
      server 192.168.1.253:80      weight=5  max_fails=3 fail_timeout=30;
      server 192.168.1.252:80      weight=1  max_fails=3 fail_timeout=30;
      server 192.168.1.251:80      backup;
    }

    server {
        listen       80;
        server_name  www.jd.com;
        location /web {
            proxy_pass http://core_tomcat;
            proxy_set_header  Host  $host;
        }
    }
 }
```

## 日志

Nginx日志对于统计、系统服务排错很有用。Nginx日志主要分为两种：access_log(访问日志)和error_log(错误日志)。通过访问日志我们可以得到用户的IP地址、浏览器的信息，请求的处理时间等信息。错误日志记录了访问出错的信息，可以帮助我们定位错误的原因。本文将详细描述一下如何配置Nginx日志。

以下内容来源于：https://blog.csdn.net/biubiuli/article/details/79481882

### 访问日志

访问日志主要记录客户端的请求。客户端向Nginx服务器发起的每一次请求都记录在这里。客户端IP，浏览器信息，referer，请求处理时间，请求URL等都可以在访问日志中得到。当然具体要记录哪些信息，你可以通过log_format指令定义。  

```
access_log path [format [buffer=size] [gzip[=level]] [flush=time] [if=condition]]; # 设置访问日志
access_log off; # 关闭访问日志

```
1. path 指定日志的存放位置。
2. format 指定日志的格式。默认使用预定义的combined。
3. buffer 用来指定日志写入时的缓存大小。默认是64k。
4. gzip 日志写入前先进行压缩。压缩率可以指定，从1到9数值越大压缩比越高，同时压缩的速度也越慢。默认是1。
5. flush 设置缓存的有效时间。如果超过flush指定的时间，缓存中的内容将被清空。
6. if 条件判断。如果指定的条件计算为0或空字符串，那么该请求不会写入日志。

可以应用access_log指令的作用域分别有http，server，location，limit_except。也就是说，在这几个作用域外使用该指令，Nginx会报错。

### 错误日志

错误日志的形式如下：
```
10.1.1.1 - - [22/Aug/2014:16:48:14 +0800] "POST /ajax/MbpRequest.do HTTP/1.1" 200 367 "-" "Dalvik/1.6.0 (Linux; U; Android 4.1.1; ARMM7K Build/JRO03H)" "119.189.56.175" 127.0.0.1:8090 0.022 0.022 
10.1.1.1 - - [22/Aug/2014:16:48:19 +0800] "POST /ajax/MbpRequest.do HTTP/1.1" 200 616 "-" "Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-I9103 Build/IMM76D)" "36.250.89.22" 127.0.0.1:8090 0.036 0.036 
```

1. 客户端（用户）IP地址。如：上例中的 10.1.1.1 (内网负载均衡地址)
2. 访问时间。如：上例中的 [22/Aug/2014:16:48:19 +0800]
3. 访问端口。如：上例中的 127.0.0.1:8080
4. 响应时间。如：上例中的 0.022
5. 请求时间。如：上例中的 0.022
6. 用户地理位置代码（国家代码）。
7. 请求的url地址（目标url地址）的host。如：上例中的 /....
8. 请求方式（GET或者POST等）。如：上例中的 GET
9. 请求url地址（去除host部分）。如：上例中的 /html/test.html
10. 请求状态（状态码，200表示成功，404表示页面不存在，301表示永久重定向等，具体状态码可以在网上找相关文章，不再赘述）。如：上例中的 "200"
11. 请求页面大小，默认为B（byte）。如：上例中的 2426
12. 来源页面，即从哪个页面转到本页，专业名称叫做“referer”。如：上例中的 "http://a.com"
13. 用户浏览器语言。如：上例中的 "es-ES,es;q=0.8"
14. 用户浏览器其他信息，浏览器版本、浏览器类型等。如：上例中的  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11"

nginx access日志的格式不是一成不变的，是可以自定义的。在nginx的nginx.conf配置文件找到：log_format 这里就是日志的格式

## 缓存

Nginx使用proxy_cache模块处理缓存。

## 安全

### 更新

### DoS攻击

### SSL/TLS 加密

## 运行环境

Apache可以作为常见的开发语言的 Web 服务器，集成数据库、应用容器，最后形成一个完整的应用运行环境，例如：Apache+PHP，Apache+Tomcat+Java等

下面我们以常见的开发语言为例，分别介绍它们是如何与Apache一起工作的。

### PHP

Apache被广泛用于PHP环境，Apache有两种PHP处理机制：

- php-fpm：PHP内核中用来处理PHP文件的解释器和进程管理器
- mod_php：Apache的PHP处理模块

mod_php 作为Apache的模块，没有独立的进程，无需额外设置和处理，使用起来非常简单。

PHP-FPM(PHP FastCGI Process Manager)意：PHP FastCGI 进程管理器，用于管理PHP 进程池的软件，用于接受Nginx等Web服务器的请求。PHP-FPM提供了更好的PHP进程管理方式，可以有效控制内存和进程、可以平滑重载PHP配置。  

下面是Apache+PHP-FPM共同工作的系统架构图，其中mod_proxy_fcgi用于Apache连接php-fpm

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/apache_event_php-fpm.jpg)

### Java

Nginx 无法直接运行Java程序，而是与Tomcat一起组合去部署Java程序。

这种组合下，Nginx处理静态资源，JSP等动态程序需转发给Tomcat处理，然后返回给用户。Nginx 使用 proxy_pass 模块来连接 Tomcat。 

proxy_pass 模块是基于 HTTP 协议的代理，因此它要求 Tomcat 必须提供 HTTP 服务，也就是说必须启用 Tomcat 的 HTTP Connector。常见的配置如下：

```
server
{
    listen 80;
    server_name www.xxx.com;
    
    location ~* "\.(jpg|png|jepg|js|css|xml|bmp|swf|gif|html)$"
    {
        root /data/wwwroot/aminglinux/;
        access_log off;
        expire 7d;
    }
    
    location /
    {
        proxy_pass http://127.0.0.1:8080/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP      $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

### Python

Nginx 也可以用于Python环境，通过扩展模块mod_proxy_uwsgi，连接Python的uWSGI服务器或Gunicorn服务器，便可以解析Python程序。

这种组合的的基本配置方法如下：

1. 配置为uwsgi.ini
   ```
   [uwsgi]
   chdir = /home/vagrant/myweb/
   virtualenv = /home/vagrant/env/
   socket = 127.0.0.1:8080
   env = DJANGO_SETTINGS_MODULE=myweb.settings
   module =myweb.wsgi:application
   master = true
   processes = 4
   vacuum = True
   max-requests = 5000
   daemonize = /var/log/uwsgi.log
   pidfile = /var/log/uwsgi.pid
   ```
2. apache的配置文件加载mod_proxy_uwsgi.so
3. apache的配置文件反向代理到uwsgi
   ```
   ProxyPass / uwsgi://127.0.0.1:8080
   ```

### Node.js

Nginx 也可以用于Node.js环境，Nginx 与 Node.js 最常见的连接方式是http_proxy，即利用 Apache 自带的 mod_proxy 模块使用代理技术来连接 Node.js。   

下面是典型的配置文件范例：

```
server {
        listen 80 default_server;
        server_name _;


        location / {
         proxy_pass http://127.0.0.1:2368;
         proxy_set_header Host $host;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

}
```

### Ruby