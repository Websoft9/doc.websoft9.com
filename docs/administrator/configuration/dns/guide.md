---
sidebar_position: 1
slug: /dns
---

# 指南

## 场景

### 域名五步设置{#domain}

#### 域名注册{#domainreg}

通过域名服务商注册（购买）一个自己喜欢且符合网站特征的域名。

#### 域名实名制认证{#domainauth}

域名注册完成之后，还需要提供个人或公司法人证件进行域名所有者的实名制认证。  

#### 域名备案{#domainbei}

备案是中国大陆的一项法规，域名用于中国大陆地区的服务器访问必须备案。也就是说向政府监管部门提供：**网站存放的详细信息**

备案是纯粹的**商务流程活动**，没有任何技术门槛，建议用户自行完成：

* 购买服务器满足云平台的免费备案要求，就可以由云平台供备案服务。
* 备案过程请通过云平台的**备案系统**全程操作
* 云平台提供 7*24 域名备案咨询服务

#### 域名解析{#domainresolve}

我们知道，网站如果通过 IP 地址访问，这样不便于记忆和识别。域名解析的作用是通过一段**容易识别的文字段**来指向服务器的**IP地址**。类似：abc.com 指向 80.123.9.11 

下面是是一个域名解析的范例：通过域名的控制台，将域名（或子域名）指向 IP：  
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/domain-websoft9.png)


#### 域名绑定{#domainbind}

上面的域名解析避免了直接使用 IP 地址，但域名配置还差最后一步。  

我们设想一个很常见的情况：有多个域名解析到同一个服务器时，服务器是如何区分并提供不同域名所需资源的？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/apache/apache-vhostui-websoft9.png)

其实这个问题就是**域名绑定**要做的工作。通过修改服务器中的 Web  服务器的 **虚拟主机配置文件**，即可实现域名绑定。  

具体参考对应的指南：  

* [Apache 域名绑定](./apache#domain)
* [Nginx  域名绑定](./nginx#domain)
* [Caddy 域名绑定](./caddy#domain)
* [Traefik 域名绑定](./traefik#domain)
* [IIS 域名绑定](./iis#domain)

### HTTPS 基本设置{#https}

#### 前置条件

配置HTTPS访问的前置条件：

* 开启服务器安全组的443端口
* 网站通过HTTP可正常访问
* Web服务器已经安装SSL模块（Websoft9提供的所有镜像默认已经安装）

具体以上条件后，便可以登录服务器配置HTTPS。此处提供两种方案，请根据实际情况选择：

#### 方案一：自动免费证书配置

Websoft9的镜像默认安装了 [Let's Encrypt](https://letsencrypt.org/) 免费的证书部署软件，只需一条命令就可以启动证书部署.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/certbot-ui-websoft9.png)

自动部署证书程序会读取已有 HTTP 配置，故请确保配置文件中 ServerName 和 ServerAlias 中配置域名绑定

1. 连接服务器，运行自动部署证书命令 
   ```
   sudo certbot
   ```
2. 根据提示输入或选择正确的项，直至提示成功

3. 测试 HTTPS 是否生效

#### 方案二：自行上传证书配置

下面详细说明上传证书的配置方案：

1. 将可用的证书上传到服务器证书目录：/data/cert（没有cert目录可以自己新建）

2. 打开**虚拟主机配置文件**，插入 HTTP 配置段
   * 以 Nginx 为例，虚拟主机配置文件为 */etc/nginx/conf.d/default.conf*，插入下面的**HTTPS template** 到对应的*server{  }*段落中
        ``` text
        #-----HTTPS template start------------
        listen 443 ssl; 
        ssl_certificate /data/cert/xxx.crt;
        ssl_certificate_key /data/cert/xxx.key;
        ssl_trusted_certificate /data/cert/chain.pem;
        ssl_session_timeout 5m;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
        ssl_prefer_server_ciphers on;
        #-----HTTPS template end------------
        ```
    * 以 Apache 为例，虚拟主机配置文件为 */etc/nginx/conf.d/default.conf*，插入下面的**HTTPS template** 到文件中

        ```
        #-----HTTPS template start------------
        <VirtualHost *:443>
        ServerName  www.mydomain.com
        DocumentRoot "/data/wwwroot/default"
        #ErrorLog "logs/www.mydomain.com-error_log"
        #CustomLog "logs/www.mydomain.com-access_log" common
        <Directory "/data/wwwroot/default">
        Options Indexes FollowSymlinks
        AllowOverride All
        Require all granted
        </Directory>
        SSLEngine on
        SSLCertificateFile  /data/cert/www.mydomain.com.crt
        SSLCertificateKeyFile  /data/cert/www.mydomain.com.key
        SSLCertificateChainFile  /data/cert/www.mydomain.com_chain.crt
        </VirtualHost>
        #-----HTTPS template end------------
        ```

4.  修改配置文件中相关项，并保存。
     
     * ServerName: 首选域名  
     * ServerAlias: 可选域名  
     * DocumentRoot: 应用目录，例如：*/data/wwwroot/wordpress*
     * Directory：应用目录，同上  
     * SSLCertificateFile：证书路径 
     * SSLCertificateKeyFile：证书私钥路径
     * SSLCertificateChainFile：证书链文件 

     > 证书文件的后缀一般是 `.crt` 或者 `.pem`；私钥的后缀一般是：`.key`。错误的路径会导致服务无法启动。

5.  重启服务
    ```
    systemctl restart nginx
    systemctl restart httpd
    ```
---

###  HTTPS 特殊方案

#### CDN 或全站加速开启 HTTPS

需要根据云平台参考文档设置。一般来说，此场景下有两个地方需要设置 HTTPS：

1. CDN/全站加速的控制台需设置 HTTPS
2. 服务器中的应用需设置 HTTPS

需要注意的是，两端 HTTPS 必须使用同一套证书。

#### HTTP 自动跳转 HTTPS（Apache）

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

#### HTTP 自动跳转 HTTPS（Nginx）

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
#### 中文域名配置 HTTPS

中文域名很特殊，它仅在中国被使用。HTTPS 是不支持中文域名的，但如何设置证书呢？

1. 在[中国互联网络信息中心](http://www.cnnic.cn/jczyfw/zwym/zgymzcjsy/201206/t20120612_26523.htm)转码。例如：`网久软件.com` 转码为 `xn--3iQsQ211JuqN.com`
2. 域名解析：将中文域名解析直接解析到服务器 IP 地址
3. 域名绑定：在虚拟主机配置文件中绑定 `xn--3iQsQ211JuqN.com`  
4. 使用`certbot` 命令自动配置HTTPS 或 使用`xn--3iQsQ211JuqN.com`申请证书后在配置HTTPS

### 向云平台申请证书

*   免费证书只能用于单个域名，例如: buy.example.com 或 next.buy.example.com,
*   example.com 是通配符域名方式，不能用于申请免费证书
*   申请证书的时候，请先解析好域名，有些证书会绑定域名对应的 IP 地址，即一旦申请后，IP 地址不能更换，否则证书不可用


## 参数

### 路径{#path}

虚拟主机配置文件：[Apache](./apache#path), [Nginx](./nginx#path) , [Caddy](./caddy#path)    
Certbot 证书目录：*/etc/letsencrypt/live*

### 端口{#port}

HTTPS 访问端口： 443  
HTTP 访问端口： 80  

### 服务{#service}

配置域名，需重启 Web 服务器  


