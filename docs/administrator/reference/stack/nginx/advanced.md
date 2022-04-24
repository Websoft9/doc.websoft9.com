---
slug: /nginx/advanced
---

# 进阶

## 安装

### 安装内核

安装 Nginx 有在线包安装和源码编译安装两种方式。其中在线安装通常称之为 yum/apt 安装，而源码安装即需要下载源码然后进行编译后方可使用。

相比源码编译安装来说，在线安装非常简单，下面是在线安装的范例：

```
# Fedora/CentOS/RedHat
sudo yum install nginx
sudo systemctl enable nginx
sudo systemctl start nginx

# Ubuntu/Debian
sudo apt install nginx
sudo service nginx start
```
### 安装模块

### 查看模块

通过 `nginx -V` 命令可以查看已经安装的所有 Nginx 模块。  

```bash
~# nginx -V
nginx version: nginx/1.12.2
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC)
built with OpenSSL 1.0.2k-fips  26 Jan 2017
TLS SNI support enabled
configure arguments: 
--prefix=/usr/share/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib64/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --http-client-body-temp-path=/var/lib/nginx/tmp/client_body --http-proxy-temp-path=/var/lib/nginx/tmp/proxy --http-fastcgi-temp-path=/var/lib/nginx/tmp/fastcgi --http-uwsgi-temp-path=/var/lib/nginx/tmp/uwsgi --http-scgi-temp-path=/var/lib/nginx/tmp/scgi --pid-path=/run/nginx.pid --lock-path=/run/lock/subsys/nginx --user=nginx --group=nginx --with-file-aio --with-ipv6 --with-http_auth_request_module --with-http_ssl_module --with-http_v2_module --with-http_realip_module --with-http_addition_module --with-http_xslt_module=dynamic --with-http_image_filter_module=dynamic --with-http_geoip_module=dynamic --with-http_sub_module --with-http_dav_module --with-http_flv_module --with-http_mp4_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_random_index_module --with-http_secure_link_module --with-http_degradation_module --with-http_slice_module --with-http_stub_status_module --with-http_perl_module=dynamic --with-mail=dynamic --with-mail_ssl_module --with-pcre --with-pcre-jit --with-stream=dynamic --with-stream_ssl_module --with-google_perftools_module --with-debug --with-cc-opt='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic' --with-ld-opt='-Wl,-z,relro -specs=/usr/lib/rpm/redhat/redhat-hardened-ld -Wl,-E'
```



## 配置

### 配置文件

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


### 配置项

Nginx中的 VirtualHost 虚拟主机是通过server{ } 进行配置的。

server{ } 改动务必准确无误，任何错误的修改都会导致服务器上所有的网站不可访问

|  server 项  |  作用说明  |  必要性 |
| --- | --- | --- |
|  server_name  |  域名，如果配置两个域名需以空格分开   |  必须填写 |
|  root |  网站存放目录  | 务必准确无误 |
|  error_log  | 错误日志路径，系统会根据定义的路径产生相关日志文件   |  可以不填或删除 |
|  access_log  | 访问日志路径，系统会根据定义的路径产生相关日志文件  |  可以不填或删除 |
|  ssl_certificate  | HTTPS 证书路径  |  设置 HTTPS 访问时必填 |
|  ssl_certificate_key  | HTTPS 证书秘钥路径   |  设置 HTTPS 访问时必填 |

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


### Proxy 代理

```
- proxy_set_header  Host  $host;  作用web服务器上有多个站点时，用该参数header来区分反向代理哪个域名。比如下边的代码举例。
- proxy_set_header X-Forwarded-For  $remote_addr; 作用是后端服务器上的程序获取访客真实IP，从该header头获取。部分程序需要该功能。
```

Nginx 本身并不支持现在流行的 JSP、ASP、PHP、PERL 等动态页面，但是它可以通过反向代理将请求发送到后端的服务器，例如 Tomcat、Apache、IIS 等来完成动态页面的请求处理。

前面的配置示例中，我们首先定义了由 Nginx 直接处理的一些静态文件请求后，其他所有的请求通过 proxy_pass 指令传送给后端的服务器（在上述例子中是 Tomcat）。最简单的 `proxy_pass` 用法如下：

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


### upstream 负载均衡 

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
来源于[第三方博客](https://www.jianshu.com/p/10ecc107b5ee)

### 缓存

Nginx使用proxy_cache模块处理缓存。

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


### 日志

Nginx日志对于统计、系统服务排错很有用。Nginx日志主要分为两种：access_log(访问日志)和error_log(错误日志)。通过访问日志我们可以得到用户的IP地址、浏览器的信息，请求的处理时间等信息。错误日志记录了访问出错的信息，可以帮助我们定位错误的原因。本文将详细描述一下如何配置Nginx日志。

以下内容来源于：https://blog.csdn.net/biubiuli/article/details/79481882

#### 访问日志

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

#### 错误日志

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


## 常见问题

#### Nginx 公司有哪些企业级产品？

Nginx公司还有企业级的商业产品：  

* NGINX Plus  
* NGINX Controller  
* NGINX Unit  
* NGINX Amplify  
* NGINX WAF  


#### Nginx 有哪些延伸项目？

基于Nginx的著名开源项目包括：

* Tengine：由淘宝网发起的Web服务器项目。它在Nginx的基础上，针对大访问量网站的需求，添加了很多高级功能和特性。
* OpenResty：一个基于 Nginx 与 Lua 的高性能 Web 平台，其内部集成了大量精良的 Lua 库、第三方模块以及大多数的依赖项。用于方便地搭建能够处理超高并发、扩展性极高的动态 Web 应用、Web 服务和动态网关。

#### Nginx 进程模型？

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

#### 什么是 Nginx IO多路复用？

一般情况下并发处理机制有三种：多进程、多线程，与异步机制。Nginx对于并发的处理同时采用了三种机制。Nginx的进程分为两类：master进程与worker进程。每个master进程可以生成多个worker进程，所以其是多进程的。每个worker进程可以同时处理多个用户请求，每个用户请求会由一个线程来处理，所以其是多线程的  

对于操作系统而言，IO多路复用就是要完成操作系统IO的请求。对于IO文件的请求，当一个IO流要进行文件处理的时候，要获取一组文件的描述符，当文件描述符还没有就绪时，那么它就在等待，直到描述符一旦就绪，马上上报系统通知的机制，告诉应用程序我准备就绪，你可以来操作了。这就是IO多路复用的方式。  

worker进程采用的就是epoll多路复用机制来对后端服务器进行处理的。当后端服务器返回结果后，后端服务器就会回调epoll多路复用器，由多路复用器对相应的worker进程进行通知。此时，worker进程就会挂起当前正在处理的事务，拿IO返回结果去响应客户端请求。响应完毕后，会再继续执行挂起的事务。这个过程就是“异步非阻塞”的。

#### NginxStatus 参数是什么意思？

NginxStatus 显示的内容意思如下：

* active connections – 当前 Nginx 正处理的活动连接数。
* server accepts handled requests -- 总共处理了 14553819 个连接 , 成功创建 14553819 次握手 ( 证明中间没有失败的 ), 总共处理了 19239266 个请求 ( 平均每次握手处理了 1.3 个数据请求 )。
* reading -- nginx 读取到客户端的 Header 信息数。
* writing -- nginx 返回给客户端的 Header 信息数。
* waiting -- 开启 keep-alive 的情况下，这个值等于 active - (reading + writing)，意思就是 Nginx 已经处理完正在等候下一次请求指令的驻留连接。

#### 如何为HTML, CSS, JS 开启 Gzip？

默认情况下 Nginx 并没有开启 Gzip，需将如下代码添加到虚拟主机配置文件中

```
gzip on;
gzip_types application/xml application/json text/css text/javascript application/javascript;
gzip_vary on;
gzip_comp_level 6;
gzip_min_length 500;
```

#### 如何修改上传的 Nginx 文件权限?

```
# 拥有者
chown -R nginx.nginx /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```

#### 如何启用或禁用 Nginx 模块？

不支持模块启用或关闭

## 故障速查

#### 网站显示重定向错误？

打开Nginx虚拟主机配置文件，检查网站对应的 server{} 配置段内容，分析其中的重定向规则，找到其中的死循环。

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

#### 413 Request Entity Too Large

这是由于上传文件大小超过了Nginx默认设置，因此需要修改 Nginx 这个限制：

1. 使用 WinSCP 远程连接服务器
2. 编辑 [Nginx 虚拟机主机配置文件](../nginx#path)
3. 插入一行 `client_max_body_size 0;` 解除上传文件限制的配置项
   ```
   server {
    listen 80;
    server_name _;
    client_max_body_size 0; #解除上传文件限制
    ...
   ```
4. 保存并[重启 Nginx 服务](../nginx#service)
