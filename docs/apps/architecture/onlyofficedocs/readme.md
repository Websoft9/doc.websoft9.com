---
sidebar_position: 1
slug: /onlyofficedocs
tags:
  - ONLYOFFICE Docs
---

# 快速入门

[ONLYOFFICE Docs ](https://www.onlyoffice.com/zh/office-suite.aspx) 是一个文档中间件，为文档管理软件提供 Office 格式的文档的在线预览与编辑。支持主流格式：docx、xlsx、pptx、odt、ods、odp、doc、xls、ppt、pdf、txt、rtf、html、epub、csv。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyofficedocs-gui-websoft9.png)

部署 Websoft9 提供的 ONLYOFFICE Docs 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80,9002** 端口已经开启 
3. 若想用域名访问  ONLYOFFICE Docs，务必先完成 **[域名五步设置](./dns#domain)** 过程


## ONLYOFFICE Docs 初始化向导

### 详细步骤

1. 本地电脑浏览器访问：*http://服务器公网IP:9002* 可看到 OnlyOffice Document Server 正在运行的提示。  
   ![ONLYOFFICE Document Server is running](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-dkisrunning-websoft9.png)

> 如果画面的提示不是*OnlyOffice Document Server is running*，则说明服务运行异常。

2. 完成域名解析后，请针对不同的 Web 服务器下，完成对应的域名绑定操作。


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## ONLYOFFICE Docs 使用入门

下面以 **×××** 作为一个任务，帮助用户快速入门：

## ONLYOFFICE Docs 常用操作

### 绑定域名

ONLYOFFICE Docs 绑定域名符合：**[域名五步设置](./dns#domain)** 。  

但是 Apache 或 Nginx **虚拟主机配置文件**请采用下面的模板：

##### Nginx
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

##### Apache

    ```
    <VirtualHost *:80>
    ProxyPreserveHost On
    ProxyAddHeaders Off
    ServerName onlyoffice.yourdomain.com
    ProxyPass / http://127.0.0.1:9002/
    ProxyPassReverse / http://127.0.0.1:9002/
    </VirtualHost>
    ```
### HTTPS 设置

大多数情况下，调用 ONLYOFFICE Docs 的软件需要 ONLYOFFICE Docs 提供 HTTPS 服务，所以域名绑定后，需立即设置 HTTPS：

1. 参考通用的 [HTTPS 配置指南](./dns#https)

2. 虚拟主机配置文件中增加下面的一行代码，使客户端和代理服务之间的连接所采用的传输协议
   ```
   # 以下适用于 Apache
   RequestHeader set X-Forwarded-Proto "https

   # 以下适用于 Nginx
   proxy_set_header   X-Forwarded-Proto $scheme;
   ```

## 参数

**[通用参数表](../setup/parameter)** 中可查看 Nginx,  Docker 等 ONLYOFFICE Docs  应用中包含的基础架构组件路径、版本、端口等参数。 

通过运行`docker ps`，可以查看到 ONLYOFFICE Docs 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

下面仅列出 ONLYOFFICE Docs  本身的参数：

### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9002   | ONLYOFFICE Document Server on Docker | 可选   |

### 版本

```shell
docker image inspect onlyoffice/communityserver  | grep onlyoffice.community.version | sed -n 1p
```

### 服务

```shell
sudo systemctl start | stop | restart | status onlyofficedocs
```

### 命令行

有待研究

### API

[ONLYOFFICE Docs API](https://api.onlyoffice.com/editors/basic)

