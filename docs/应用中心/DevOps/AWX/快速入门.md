---
sidebar_position: 1
slug: /awx
tags:
  - AWX
  - DevOps
---

# 快速入门

[AWX](https://github.com/ansible/awx) 是Ansible Tower的开源版，Ansible Tower是一个可视化界面的服务器自动部署和运维管理平台。AWX提供基于Web的用户界面，REST API和构建在Ansible之上的任务引擎。
![AWX界面](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awxui-websoft9.png)

在云服务器上部署 AWX 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 AWX，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### AWX

管理员用户名：`admin`  
管理员密码： 存储在您的服务器指定文件中：*/credentials/password.txt*

### PostgreSQL

本部署方案中，PostgreSQL 采用 Docker 部署：

* 管理员账号：*`postgres`*
* 管理员密码：存储在您的服务器指定文件中：*/credentials/password.txt*

## AWX 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://公网IP*, 进入 AWX 登录页面
   ![AWX登录页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-login-websoft9.png)

3. 输入用户名和密码[（不知道密码？）](/zh/stack-accounts.md)，登录到 AWX 后台管理界面
   ![AWX后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-gui-websoft9.png)

4. 此时，AWX 安装部署已经验证通过

> 需要了解更多AWX的使用，请参考：[Ansible Tower Documentation](https://docs.ansible.com/ansible-tower/).

## AWX 入门向导

现在开始针对于**如何使用 AWX 可视化运行 Ansible 项目**进行完整的实战操作说明：

### 概念

在实战之前，必须先了解几个概念：

![AWX后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-consoleui-websoft9.png)

* **清单（Inventories）**：对应 Ansible 的 Inventory，即主机组和主机IP清单列表。

* **凭证（Credentials）**：受控主机的用户名、密码（秘钥）以及提权控制

* **项目（Projects）**：一个完整可运行的 Ansible 项目

* **模板（Templates）**：将清单、项目和凭证关联起来的任务模板，一次创建，多次使用，可修改

* **作业（Jobs）**：模板每一次运行视为一次作业

### 准备

在使用 AWX 运行一个 Ansible 项目之前，请确保符合如下条件：

* 准备一个可用的 Ansible 项目，例如：[Grafana](https://github.com/Websoft9/ansible-grafana)
* 准备一台新创建的云服务器，此服务器被 AWX 安装 Ansible 项目。建议先运行下面的脚本，在服务中安装主流的仓库，以及 Git,pip 等工具
  ```
  wget -N https://cdn.statically.io/gh/Websoft9/ansible-linux/main/scripts/install.sh; bash install.sh
  ```

### 步骤

下面我们开始列出具体的步骤：

1. 登录 AWX，创建【清单】，然后在清单中增加【主机】

   ![创建清单](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-inventories001-websoft9.png)

   ![创建主机](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-inventories002-websoft9.png)

   ![创建主机](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-inventories003-websoft9.png)

2. 创建【凭证】，下面是创建一个 root 账号以及管理密码所对应的范例（凭证类型选择【机器】）
   ![创建凭证](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-credentials-websoft9.png)

3. 创建【项目】，下面以我们提供的开源项目 [HelloWorld](https://github.com/ansible/tower-example) 作为范例

   ![创建项目](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-project-websoft9.png)

4. 创建【模板】，分别将前面创建的【凭证】、【清单】、【项目】关联起来，便完成了模板的配置
   ![创建模板](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-templates-websoft9.png)

   > 也可以直接设置**额外变量**覆盖交互式

6. 启动Template，进入 Job 页面，开始安装所需的应用程序
   ![成功运行项目](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-templaterunning-websoft9.png)

## 常用操作

### 域名绑定

绑定域名的前置条件是：AWX已经可以通过解析后的域名访问。  

虽然如此，从服务器安全和后续维护考量，**域名绑定**步骤不可省却  

AWX 域名绑定操作步骤：

1. 使用 SFTP 登录云服务器
2. 修改 [Nginx 配置文件](/zh/stack-components.md#nginx)，将其中的 **server_name** 项的值 *localhost* 修改为你的域名
   ```text
   ...
      server_name    localhost; # 改为自定义域名
   ...
   ```
3. 保存配置文件，重启[ Nginx 服务](/zh/admin-services.md#nginx)
   ```
   sudo docker pause awx_web
   ```
4. 登录AWX，依次打开：【Settings】>【System】，修改下图的 URL 地址
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awx-seturl-websoft9.png)

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

AWX 预装 SSL 设置，但需要开启并上传证书。  

#### 前置条件

1. 云控制台已经开启安全组443端口
2. 完成域名解析
3. 申请了可用的CA证书

#### 配置方案

AWX 采用的是 Docker 部署，同时也设置 Nginx 作为转发，所以有两种 HTTPS 设置方案。

#### Nginx 中配置（推荐）

#### 自动部署

如果没有申请证书，只需在服务器中运行一条命令`sudo certbot`便可以启动免费证书**自动**申请和部署

```
sudo certbot
```

#### 手动部署

如果你已经申请了证书，只需三个步骤，即可完成 HTTPS 配置

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到 *server{ }* 中
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
3. 重启[Nginx服务](/zh/admin-services.md#nginx)

#### 容器中配置

通过向 AWX 容器持久化存储目录增加证书的方式来配置 HTTPS，具体如下：

1. 修改（检查） /data/.awx/docker-compose.yml 文件，确保有如下两项 "- 443:443" 和 "- /data/cert:/etc/ssl/certs"：       
    ```
    ports:
    - "80:8052"
    - "443:443"
    hostname: awxweb
    user: root
    restart: unless-stopped
    volumes:
    - /data/cert:/etc/ssl/certs
    ```
2. 上传证书到 /data/cert 目录

3. 打开虚拟主机配置文件：*/data/.awx/nginx.conf* ，插入如下的 **HTTPS 配置项** 到 server{ } 段落中，保存
   ``` text
   #-----HTTPS template start------------
   listen 443 ssl; 
   ssl_certificate /etc/ssl/certs/xxx.crt;
   ssl_certificate_key /etc/ssl/certs/xxx.key;
   ssl_trusted_certificate /etc/ssl/certs/chain.pem;
   ssl_session_timeout 5m;
   ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
   ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
   ssl_prefer_server_ciphers on;
   #-----HTTPS template end------------
   ```
   > 以上的配置文件中的路径必须是 awx-web 容器虚拟机的路径：/etc/ssl/certs

4. 运行如下命令，重置容器
   ```
   cd /data/.awx
   sudo docker-compose up -d
   docker restart awx_web
   ```

### 配置 SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿尝试在服务器上安装sendmail等发邮件方案，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，导致不稳定、不易维护、诊断故障困难。

下面以**网易邮箱**为例，提供设置 AWX 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 登录 AWX控制台，打开：【ADMINISTRATION】>【NOTIFICATIONS】
3. 新建一个 Notification 模板，选择【电子邮件】，填写相关 SMTP 参数
   ![AWX SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-smtp-websoft9.png)

> 更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### 负载均衡

通过负载均衡处理多台 AWX 并行工作，对于大型企业来说这是一种很常见的部署方案。

AWX是基于Docker部署，处理web的容器名称为：awx_web

### 使用外部PostgreSQL

默认安装下，使用的是Docker版本的PostgreSQL数据库，并设置了持久化存储。  

如果你想将数据库更换为外部PostgreSQL数据库（自建或云数据库），请参考如下步骤：

1. 备份好已有的AWX数据
2. 进入到AWX的配置文件夹
   ```
   cd /data/.awx
   ```
2. 删除目前AWX项目的所有容器
   ```
   cd /data/.awx
   docker-compose -f docker-compose.yml down -v
   ```
3. 修改 *docker-compose.yml* 文件，去掉两处 *depends_on:* 项中的 *- postgres*，并删除 *postgres: ...* 整段，最后文件的内容如下： 
   ```
   version: '2'
   services:

     web:
       image: ansible/awx_web:11.2.0
       container_name: awx_web
       depends_on:
         - redis
         - memcached
       ports:
         - "80:8052"
       hostname: awxweb
       user: root
       restart: unless-stopped
       volumes:
         - supervisor-socket:/var/run/supervisor
         - rsyslog-socket:/var/run/awx-rsyslog/
         - rsyslog-config:/var/lib/awx/rsyslog/
         - "/data/.awx/SECRET_KEY:/etc/tower/SECRET_KEY"
         - "/data/.awx/environment.sh:/etc/tower/conf.d/environment.sh"
         - "/data/.awx/credentials.py:/etc/tower/conf.d/credentials.py"
         - "/data/.awx/nginx.conf:/etc/nginx/nginx.conf:ro"
         - "/data/.awx/redis_socket:/var/run/redis/:rw"
         - "/data/.awx/memcached_socket:/var/run/memcached/:rw"
       environment:
         http_proxy: 
         https_proxy: 
         no_proxy: 

     task:
       image: ansible/awx_task:11.2.0
       container_name: awx_task
       depends_on:
         - redis
         - memcached
         - web
       hostname: awx
       user: root
       restart: unless-stopped
       volumes:
         - supervisor-socket:/var/run/supervisor
         - rsyslog-socket:/var/run/awx-rsyslog/
         - rsyslog-config:/var/lib/awx/rsyslog/
         - "/data/.awx/SECRET_KEY:/etc/tower/SECRET_KEY"
         - "/data/.awx/environment.sh:/etc/tower/conf.d/environment.sh"
         - "/data/.awx/credentials.py:/etc/tower/conf.d/credentials.py"
         - "/data/.awx/redis_socket:/var/run/redis/:rw"
         - "/data/.awx/memcached_socket:/var/run/memcached/:rw"
       environment:
         http_proxy: 
         https_proxy: 
         no_proxy: 
         SUPERVISOR_WEB_CONFIG_PATH: '/supervisor.conf'

     redis:
       image: redis
       container_name: awx_redis
       restart: unless-stopped
       environment:
         http_proxy: 
         https_proxy: 
         no_proxy: 
       command: ["/usr/local/etc/redis/redis.conf"]
       volumes:
         - "/data/.awx/redis.conf:/usr/local/etc/redis/redis.conf:ro"
         - "/data/.awx/redis_socket:/var/run/redis/:rw"
         - "/data/.awx/memcached_socket:/var/run/memcached/:rw"

     memcached:
       image: "memcached:alpine"
       container_name: awx_memcached
       command: ["-s", "/var/run/memcached/memcached.sock", "-a", "0666"]
       restart: unless-stopped
       environment:
         http_proxy: 
         https_proxy: 
         no_proxy: 
       volumes:
         - "/data/.awx/memcached_socket:/var/run/memcached/:rw"

   volumes:
     supervisor-socket:
     rsyslog-socket:
     rsyslog-config:

   ```
4. 修改 */data/.awx/credentials.py* 文件中数据库账号信息，确保为外部PostgreSQL的连接信息
   ```
      DATABASES = {
       'default': {
           'ATOMIC_REQUESTS': True,
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': "awx",
           'USER': "awx",
           'PASSWORD': "yourpassword",
           'HOST': "pgm-j6cr72qyfadij3980o.pg.rds.websoft9.com",
           'PORT': "1433",
       }
   }

   BROADCAST_WEBSOCKET_SECRET = "al9mLS4tWTlmX1owN1FyOElJWDY="
   ```
5. 修改 */data/.awx/environment.sh* 文件中数据库账号信息，确保为外部PostgreSQL的连接信息
   ```
   DATABASE_USER=awx
   DATABASE_NAME=awx
   DATABASE_HOST=pgm-j6cr72qyfadij3980o.pg.rds.websoft9.com
   DATABASE_PORT=1433
   DATABASE_PASSWORD=yourpassword
   AWX_ADMIN_USER=admin
   AWX_ADMIN_PASSWORD=password

   ```
6. 重新创建容器
   ```
   docker-compose -f docker-compose.yml up -d
   ```

### 额外变量

AWX 支持从项目之外注入所需的变量，它是通过**额外变量**机制实现，一方面可以增加变量的多样性，另外可以绕过 Ansible 项目中的交互式。  

有两种额外变量的方式：

* **方式一**：在【模板】编辑页面直接增加额外变量
  ![Ansible-Tower 额外变量](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-extravars-websoft9.png)

* **方式二**：在【模板】编辑页面增加一个【问卷调查】项
  ![Ansible-Tower 问卷调查](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-varspromptset-websoft9.png)

详情参考官方文档 [Create a Survey](https://docs.ansible.com/ansible-tower/latest/html/userguide/job_templates.html#ug-surveys)

## 异常处理

#### 浏览器打开IP地址，无法访问 AWX（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 AWX 数据？

PostgreSQL Docker

#### AWX 是否支持 Ansible Galaxy？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-setgalax-websoft9.png)

支持，参考官方文档 [Ansible Galaxy Support](https://docs.ansible.com/ansible-tower/latest/html/userguide/projects.html#ug-galaxy)