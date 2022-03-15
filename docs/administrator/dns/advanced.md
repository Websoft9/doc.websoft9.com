---
sidebar_position: 2
slug: /dns/advanced
---

# 进阶

## 证书FAQ

#### 为什么设置成功，显示“与此网站建立的连接并非完全安全”？

首选明确一点即您的HTTPS设置是成功的，只是由于网站中存在包含 http访问的静态文件 或 外部链接等，导致浏览器告警您的网站并非完全安全。

#### 向云平台申请证书的注意事项

*   免费证书只能用于单个域名,例如: buy.example.com,或next.buy.example.com,
*   example.com是通配符域名方式，不能用于申请免费证书
*   申请证书的时候，请先解析好域名，有些证书会绑定域名对应的IP地址，即一旦申请后，IP地址不能更换，否则证书不可用

#### CDN/全站加速开启HTTPS

需要根据云平台参考文档设置。一般来说，此场景下有两个地方需要设置 HTTPS：

1. CDN/全站加速的控制台需设置 HTTPS
2. 服务器中的应用需设置 HTTPS

需要注意的是，两端 HTTPS 必须使用同一套证书。

#### Apache 实现 HTTP 自动跳转到 HTTPS 页面

建议在网站根目录下的.htacesss文件中增加redirect规则

```
# 全部跳转
RewriteEngine On
RewriteCond %{SERVER_PORT} 80
RewriteRule ^(.*)$ https://www.yourdomain.com/$1 [R,L]

# 指定域名跳转
RewriteEngine On
RewriteCond %{HTTP_HOST} ^yourdomain\.com [NC]
RewriteCond %{SERVER_PORT} 80
RewriteRule ^(.*)$ https://www.yourdomain.com/$1 [R,L]

# 指定某个目录跳转
RewriteEngine On
RewriteCond %{SERVER_PORT} 80
RewriteCond %{REQUEST_URI} folder
RewriteRule ^(.*)$ https://www.yourdomain.com/folder/$1 [R,L]
```

#### Nginx 实现 HTTP 自动跳转到 HTTPS 页面

建议在 Nginx 虚拟主机配置文件对应的网站配置段中增加跳转项 `if...`

```
server
{
     listen 80;
     server_name www.websoft9.com;
     index readme.html index.html index.htm;
     root  /data/nas/www.websoft9.com;
     error_log /var/log/nginx/www.websoft9.com-error.log crit;
     access_log  /var/log/nginx/www.websoft9.com-access.log;
     include conf.d/extra/*.conf;  
    
    # HTTP to HTTPS
    if ($scheme = http) {
        return 301 https://$host$request_uri;
    } 

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/www.websoft9.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/www.websoft9.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot  
}

```

#### Android 无法使用HTTPS，而IOS可以？

确保SSLCertificateChainFile已设置对应的证书文件

#### IP 地址可以申请证书吗？

不可以，且没有任何意义。

#### Docker 应用如何部署 HTTPS？

我们的方案中，不建议在容器内部设置 HTTPS，而是通过宿主机的 HTTP 服务器（Nginx/Apache等）在端口转发的模式下配置 HTTPS。

#### 中文域名如何使用HTTPS

使用中文域名先要将中文域名在[国互联网络信息中心](http://www.cnnic.cn/jczyfw/zwym/zgymzcjsy/201206/t20120612_26523.htm)转码，例如：
输入的域名串是: 久.club
经过转码后变成了: xn--3iQ.club
需要注意的是：

- 在域名解析过程中，使用中文域名 久.club 解析到服务器 IP 
- 在 Apache 或 Nginx 配置中使用 转码域名 xn--3iQ.club

在申请SSL证书时用 xn--3iQ.club 域名申请，然后进行配置即可。

## 问题

#### 什么是一级域名？二级域名？

当您成功注册了一个域名，就是拥有了一个一级域名，类似： abc.com ，
通过一级域名，可以设置出无数个二级域名，类似：www.abc.com 或 help.abc.com

> 如何设置二级域名？进入域名厂商提供的域名控制台设置。

#### 域名与服务器如何建立关联？

域名需要通过A记录的方式解析到服务器才能与服务器建立关联，域名解析到服务器IP之后，服务器会通过“域名配置文件（虚拟主机文件）”来判断多个域名与多个网站之间的映射关系

#### 服务器如何识别域名的级别？

不管是一级域名还是二级域名，对服务器来说都是不同的域名，abc.com 和 www.abc.com 对服务器来说两个独立的域名，即服务器不识别域名的级别。

#### 域名如何备案？

备案是中国大陆的一项法规，使用大陆节点服务器开办网站的用户，需要在服务器提供商处提交备案申请。

域名备案是纯粹的商务流程，需要登录到云平台的备案系统中完成备案。

#### 如何使用中文域名

使用中文域名先要将中文域名在[国互联网络信息中心](http://www.cnnic.cn/jczyfw/zwym/zgymzcjsy/201206/t20120612_26523.htm)转码，例如：
输入的域名串是: 久.club
经过转码后变成了: xn--3iQ.club
需要注意的是：

- 在域名解析过程中，使用中文域名 久.club 解析到服务器 IP 
- 在 Apache 或 Nginx 配置中使用 转码域名 xn--3iQ.club

在申请SSL证书时用 xn--3iQ.club 域名。


