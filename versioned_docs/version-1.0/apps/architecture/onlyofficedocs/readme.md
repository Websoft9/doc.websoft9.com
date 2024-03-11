---
sidebar_position: 1
slug: /onlyofficedocs
tags:
  - ONLYOFFICE Docs
---

# 快速入门

[ONLYOFFICE Docs](https://www.onlyoffice.com/zh/office-suite.aspx) 是一个文档中间件，为文档管理软件提供 Office 格式的文档的在线预览与编辑。支持主流格式：docx、xlsx、pptx、odt、ods、odp、doc、xls、ppt、pdf、txt、rtf、html、epub、csv。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyofficedocs-gui-websoft9.png)

部署 Websoft9 提供的 ONLYOFFICE Docs 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址**
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80,9002** 端口已经开启
3. 若想用域名访问  ONLYOFFICE Docs，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## ONLYOFFICE Docs 初始化向导

### 详细步骤

1. 本地电脑浏览器访问：*`http://服务器公网IP:9002`* 可看到 OnlyOffice Docs 正在运行的提示。  
   ![ONLYOFFICE Document Server is running](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-dkisrunning-websoft9.png)

> 如果画面的提示不是*OnlyOffice Docs is running*，则说明服务运行异常。

2. 完成域名解析后，请针对不同的 Web 服务器下，完成对应的域名绑定操作。

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## ONLYOFFICE Docs 使用入门

下面以 **×××** 作为一个任务，帮助用户快速入门：

## ONLYOFFICE Docs 常用操作

### 启用 JWT Key

JWT Key 用于第三方软件与 ONLYOFFICE Docs 的密码验证，确保 ONLYOFFICE Docs 在授权的情况下才可以被调用。

只需修改 ONLYOFFICE Docs  根目录下的 `.env` 中 JWT_ENABLED=true 即可。  

```
# [true, false]
JWT_ENABLED=false
JWT_SECRET=sBPF1mjEbQ2bzj31entX
JWT_HEADER=Authorization
JWT_IN_BODY=false
```

### 绑定域名

ONLYOFFICE Docs 绑定域名符合：**[域名五步设置](./administrator/domain_step)** 。  

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

### 增加字体{#addfonts}

我们已经验证 ONLYOFFICE Docs 官方文档 [Adding fonts to ONLYOFFICE Docs](https://helpcenter.onlyoffice.com/installation/docs-community-install-fonts-linux.aspx) 是完全可以用的。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyofficedocs-addfonts-websoft9.png)

同时，我们记录了如下的事项供您参考：

1. 需清空浏览器缓存或使用隐私模式打开新的浏览器页面，方可看到新增字体
2. Windows 系统上拷贝的 ttf 字体是可用的
3. 网上下载的 ttf 字体是可用的

### 多版本

ONLYOFFICE Docs 默认设置是支持[多版本](https://helpcenter.onlyoffice.com/onlyoffice-editors/onlyoffice-document-editor/HelpfulHints/VersionHistory.aspx)的，可以通过：【文件】>【版本历史】进行查看。  

下面是 ownCloud 下打开文档后，ONLYOFFICE Docs 多版本的查看结果：  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyofficedocs-docsversions-websoft9.png)

### HTTPS 设置

大多数情况下，调用 ONLYOFFICE Docs 的软件需要 ONLYOFFICE Docs 提供 HTTPS 服务，所以域名绑定后，需立即设置 HTTPS：

#### 通过代理配置

我们推荐使用 Proxy 代理对 ONLYOFFICE Docs 进行 HTTPS 配置：

1. 参考通用的 [HTTPS 配置指南](./administrator/domain_https)

2. 虚拟主机配置文件中增加下面的一行代码，使客户端和代理服务之间的连接所采用的传输协议

   ```
   # 以下适用于 Apache
   RequestHeader set X-Forwarded-Proto "https

   # 以下适用于 Nginx
   proxy_set_header   X-Forwarded-Proto $scheme;
   ```

#### 自签名配置

ONLYOFFICE Docs 也提供了[自签名的 HTTPS](https://helpcenter.onlyoffice.com/installation/docs-community-install-docker.aspx) 方案，经过验证完全可用：

1. ONLYOFFICE Docs 容器新增443端口，映射到宿主机

2. 进入 ONLYOFFICE Docs 容器，下载并运行创建证书的脚本
   ```
   wget -N -P /var/www/onlyoffice/Data https://websoft9.github.io/docker-library/apps/onlyofficedocs/src/createCA.sh
   bash /var/www/onlyoffice/Data/createCA.sh
   ```
3. Modify the container configuration file
   ```
   sed -i 's/"rejectUnauthorized": true/"rejectUnauthorized": false/g' /etc/onlyoffice/documentserver/default.json
   supervisorctl restart all
   ```
4. 退出 ONLYOFFICE Docs 容器，重启后生效

### 企业版 License 激活

将 License 文件放入容器内路径 **/var/www/onlyoffice/Data**, 可在对应的宿主机挂载目录去修改。

## 参数

ONLYOFFICE Docs 应用中包含 Nginx, Docker 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 ONLYOFFICE Docs 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                             COMMAND                  CREATED              STATUS              PORTS                                                                                                             NAMES
1a27919d2201   onlyoffice/documentserver:7.3     "/app/ds/run-documen…"   About a minute ago   Up About a minute   443/tcp, 0.0.0.0:9002->80/tcp, :::9002->80/tcp                                                                    onlyofficedocs
```

下面仅列出 ONLYOFFICE Docs  本身的参数：

### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9002   | ONLYOFFICE Document Server on Docker | 可选   |

### 版本

```shell
docker exec -i onlyofficedocs bash -c 'apt-cache show onlyoffice-documentserver |grep -i version |cut -d: -f2'
```

### 服务

```shell
sudo systemctl start | stop | restart | status onlyofficedocs
```

### 命令行

有待研究

### API

[ONLYOFFICE Docs API](https://api.onlyoffice.com/editors/basic)
