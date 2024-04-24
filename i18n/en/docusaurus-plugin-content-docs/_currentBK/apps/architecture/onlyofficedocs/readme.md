---
sidebar_position: 1
slug: /onlyofficedocs
tags:
  - ONLYOFFICE Docs
  - IT Architecture
  - Broker
---

# ONLYOFFICE Docs Getting Started

[ONLYOFFICE Docs ](https://www.onlyoffice.com/office-suite.aspx) 是一个文档中间件，为文档管理软件提供 Office 格式的文档的在线预览与编辑。支持主流格式：docx, xlsx, pptx, odt, ods, odp, doc, xls, ppt, pdf, txt, rtf, html, epub, csv.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyofficedocs-gui-websoft9.png)
  
If you have installed Websoft9 ONLYOFFICE Docs, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80,9002** is allowed
3. **[Get](./user/credentials)** default username and password of ONLYOFFICE Docs
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for ONLYOFFICE Docs

## ONLYOFFICE Docs Initialization

### Steps for you

1. Use local browser to access *http://Cloud Server Internet IP* and *http://Cloud Server Internet IP:9002* and see the notice that ONLYOFFICE Document Server is running.
![ONLYOFFICE Document Server is running](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-dkisrunning-websoft9.png)

> 如果画面的提示不是*OnlyOffice Docs is running*，则说明服务运行异常。

2. 完成域名解析后，请针对不同的 Web 服务器下，完成对应的域名绑定操作。

>  More guide about ONLYOFFICE, please refer to [ONLYOFFICE Documentation](https://helpcenter.onlyoffice.com/server/docker/opensource/index.aspx).

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## ONLYOFFICE Docs QuickStart

## ONLYOFFICE Docs Setup

### Domain Binding

Refer to：**[Five steps for Domain](./administrator/domain_step)** 。  

但是 Apache 或 Nginx **虚拟主机配置文件**请采用下面的模板：

**Nginx**
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

**Apache**

    ```
    <VirtualHost *:80>
    ProxyPreserveHost On
    ProxyAddHeaders Off
    ServerName onlyoffice.yourdomain.com
    ProxyPass / http://127.0.0.1:9002/
    ProxyPassReverse / http://127.0.0.1:9002/
    </VirtualHost>
    ```

### SSL/HTTPS
  
大多数情况下，调用 ONLYOFFICE Docs 的软件需要 ONLYOFFICE Docs 提供 HTTPS 服务，所以域名绑定后，需立即设置 HTTPS：

1. Refer to [Set HTTPS for App](./administrator/domain_https)

2. 虚拟主机配置文件中增加下面的一行代码，使客户端和代理服务之间的连接所采用的传输协议
   ```
   # 以下适用于 Apache
   RequestHeader set X-Forwarded-Proto "https

   # 以下适用于 Nginx
   proxy_set_header   X-Forwarded-Proto $scheme;
   ```
  
## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage ONLYOFFICE Docs

通过运行`docker ps`，可以查看到 ONLYOFFICE Docs 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 9002   | ONLYOFFICE Document Server on Docker | Optional   |


### Version{#version}

```shell
docker image inspect onlyoffice/communityserver  | grep onlyoffice.community.version | sed -n 1p
```

### Service{#service}

```shell
sudo systemctl start | stop | restart | status onlyofficedocs
```

### CLI{#cli}

Coming soon...  

### API

[ONLYOFFICE Docs API](https://api.onlyoffice.com/editors/basic)