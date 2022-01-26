# 配置 SSL/HTTPS

配置HTTPS访问的前置条件：

* 开启服务器安全组的443端口
* 网站通过HTTP可正常访问
* Web服务器已经安装SSL模块（Websoft9提供的所有镜像默认已经安装）

具体以上条件后，便可以登录服务器配置HTTPS。此处提供两种方案，请根据实际情况选择：

## 方案一：自动免费证书配置

Websoft9的镜像默认安装了 [Let's Encrypt](https://letsencrypt.org/) 免费的证书部署软件，只需一条命令就可以启动证书部署.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/certbot-ui-websoft9.png)

自动部署证书会根据已有的HTTP配置而定，故请确保网站的配置文件中ServerName和ServerAlias中配置有正确的解析后的域名

1. 连接服务器，运行命令 
   ```
   sudo certbot
   ```
2. 根据提示输入对应的内容（下图为范例）

   ![1542853767834](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/certbot-websoft9.png)

   > 第4步可以多选,输入的数字以逗号/空格为分隔

4.  以上步骤操作完成后,certbot将会自动配置好证书,浏览器访问域名检查是否配置成功。生成的网站证书存放目录：`/etc/letsencrypt/live/`

## 方案二：自行上传证书配置

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
