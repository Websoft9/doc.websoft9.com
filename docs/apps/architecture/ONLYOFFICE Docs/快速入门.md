---
sidebar_position: 1
slug: /onlyofficedocs
tags:
  - ONLYOFFICE Docs
---

# 快速入门

[ONLYOFFICE Docs ](https://www.onlyoffice.com/zh/office-suite.aspx) 是一个文档中间件，为文档管理软件提供 Office 格式的文档的在线预览与编辑。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启

## ONLYOFFICE Docs 初始化向导

本章适合使用了 Websoft9 提供的 ONLYOFFICE ONLYOFFICE Docs 部署方案（区别于 ONLYOFFICE）。

#### 访问

本地浏览器访问：*http://服务器公网IP:9002* 可看到 OnlyOffice Document Server 正在运行的提示。  
![ONLYOFFICE Document Server is running](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-dkisrunning-websoft9.png)

> 如果画面的提示不是*OnlyOffice Document Server is running*，则说明服务运行异常。

#### 域名绑定

完成域名解析后，请针对不同的 Web 服务器下，完成对应的域名绑定操作：

##### Nginx

1. 编辑 **Nginx 虚拟主机配置文件**，增加如下域名绑定代码，保存
    ```
    server {
        listen 80;
        server_name onlyoffice.yourdomain.com;
        location / {
            proxy_pass  http://127.0.0.1:9002;
            proxy_redirect     off;
            proxy_set_header   Host             $host;
            proxy_set_header   X-Real-IP        $remote_addr;
            proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
            #proxy_set_header   X-Forwarded-Proto $scheme;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection upgrade;
            proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
            proxy_max_temp_file_size 0;
            proxy_connect_timeout      90;
            proxy_send_timeout         90;
            proxy_read_timeout         90;
            proxy_buffer_size          4k;
            proxy_buffers              4 32k;
            proxy_busy_buffers_size    64k;
            proxy_temp_file_write_size 64k;
    }
    error_log /var/log/nginx/onlyoffice.yourdomain.com-error.log error;
    access_log  /var/log/nginx/onlyoffice.yourdomain.com-access.log;
    }
    ```
2. 重启 Nginx 服务后生效
   ```
   sudo systemctl restart nginx
   ```

##### Apache

当用户使用 nextCloud 等网盘解决方案时，ONLYOFFICE Document Server 已经被包含到部署方案中。  

如果想更安全、更方便的使用 ONLYOFFICE Document Server，需要参考下面的方案配置域名

1. 编辑 **Apache 虚拟主机配置文件**，增加如下域名绑定代码，保存
    ```
    <VirtualHost *:80>
    ProxyPreserveHost On
    ProxyAddHeaders Off
    ServerName onlyoffice.yourdomain.com
    ProxyPass / http://127.0.0.1:9002/
    ProxyPassReverse / http://127.0.0.1:9002/
    </VirtualHost>
    ```
2. 重启 Apache 服务后生效
   ```
   sudo systemctl restart apache
   ```

#### HTTPS 设置

完成域名绑定之后，开始设置 HTTPS：

1. 运行 `sudo certbot` 即可自助设置 [HTTPS](/zh/solution-https.md)

2. 虚拟主机配置文件中增加下面的一行代码，使客户端和代理服务之间的连接所采用的传输协议
   ```
   # 以下适用于 Apache
   RequestHeader set X-Forwarded-Proto "https

   # 以下适用于 Nginx
   proxy_set_header   X-Forwarded-Proto $scheme;
   ```

3. 重启服务后生效

#### 集成

ONLYOFFICE Document Server 支持被 ownCloud, Nextcloud, Seafile 等网盘软件的文档预览与集成。

* [ownCloud 集成 ONLYOFFICE Document Server](http://support.websoft9.com/docs/owncloud/zh/solution-more.html#owncloud-文件预览与编辑)
* [Nextcloud 集成 ONLYOFFICE Document Server](http://support.websoft9.com/docs/nextcloud/zh/solution-more.html#nextcloud-文件预览与编辑)
* [Seafile 集成 ONLYOFFICE Document Server](https://support.websoft9.com/docs/seafile/zh/solution-office.html)
