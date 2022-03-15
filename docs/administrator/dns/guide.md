---
sidebar_position: 1
slug: /dns
---

# 指南

## 场景

### 域名解析与绑定

域名的目的是通过一段容易识别的文字段来指向服务器上的网站。如果没有域名，网站就只能通过IP地址访问，这样不便于记忆和识别。
给网站配上域名访问有两个步骤：

1. 域名解析：域名解析需要通过域名控制台操作
2. 域名绑定：域名绑定需要连接到云服务器，修改云服务器上**虚拟主机配置文件**中的域名项：

虚拟主机配置文件在哪里呢？ 要根据所使用的 HTTP 服务器而定，一般说来：

* Apache 的虚拟主机配置文件地址：*/etc/httpd/conf.d/vhost.conf*
* Nginx 的虚拟主机配置文件地址：*/etc/nginx/conf.d/default.conf*

## 域名配置步骤

为了使网站可以通过域名访问，配置域名分为两个步骤：

*   **域名解析**：在域名的控制台上做一个将域名（或子域名）指向IP的操作(下图示例)
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/domain-websoft9.png)

*   **域名绑定**：域名绑定指一台服务器在多网站部署的时候，通过**虚拟主机配置文件**，将每个域名绑定到其对应的网站目录，从而达到每个网站都可以通过域名访问且相会不会干扰的效果。

下面是一个虚拟配置文件范例（LAMP环境）：

   ~~~ 
<VirtualHost *:80>
ServerName www.mydomain.com
ServerAlias other.mydomain.com
DocumentRoot "/data/wwwroot/default/mysite2"
ErrorLog "/var/log/httpd/www.mydomain.com_error_apache.log"
CustomLog "/var/log/httpd/www.mydomain.com_apache.log" common
<Directory "/data/wwwroot/default/mysite1">
Options Indexes FollowSymlinks
AllowOverride All
Require all granted
</Directory>
</VirtualHost>
   ~~~

通过修改配置文件中域名相关的值（ServerName,ServerAlias等）实现绑定域名

> 配置文件主要包括域名与网站的对应的关系，即某个域名应该对应访问哪个目录。如果服务器上有多个网站，就必须对应多个配置文件。

### HTTPS

配置HTTPS访问的前置条件：

* 开启服务器安全组的443端口
* 网站通过HTTP可正常访问
* Web服务器已经安装SSL模块（Websoft9提供的所有镜像默认已经安装）

具体以上条件后，便可以登录服务器配置HTTPS。此处提供两种方案，请根据实际情况选择：

#### 方案一：自动免费证书配置

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

## 参数


