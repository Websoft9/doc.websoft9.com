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
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 AWX 的 **[默认管理员账号和密码](./user/credentials)**  
4. 若想用域名访问  AWX，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## AWX 初始化向导

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名* 或 *http://公网IP*, 进入 AWX 登录页面
   ![AWX登录页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-login-websoft9.png)

3. 输入用户名和密码[（不知道密码？）](./user/credentials)，登录到 AWX 后台管理界面
   ![AWX后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-gui-websoft9.png)

4. 此时，AWX 安装部署已经验证通过

> 需要了解更多 AWX 的使用，请参考：[Ansible Tower Documentation](https://docs.ansible.com/ansible-tower/).

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。


## AWX 使用入门

下面以 **使用 AWX 可视化运行 Ansible 项目** 作为一个任务，帮助用户快速入门：

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

### 修改 URL

 **[域名五步设置](./administrator/domain_step)** 完成后，需登录 AWX，依次打开：【Settings】>【System】， 修改默认的 URL

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awx-seturl-websoft9.png)

### 容器中配置 SSL/HTTPS

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

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数

2. 登录 AWX控制台，打开：【ADMINISTRATION】>【NOTIFICATIONS】

3. 新建一个 Notification 模板，选择【电子邮件】，填写相关 SMTP 参数
   ![AWX SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-smtp-websoft9.png)


### 增加额外变量

AWX 支持从项目之外注入所需的变量，它是通过**额外变量**机制实现，一方面可以增加变量的多样性，另外可以绕过 Ansible 项目中的交互式。  

有两种额外变量的方式：

* **方式一**：在【模板】编辑页面直接增加额外变量
  ![Ansible-Tower 额外变量](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-extravars-websoft9.png)

* **方式二**：在【模板】编辑页面增加一个【问卷调查】项
  ![Ansible-Tower 问卷调查](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-varspromptset-websoft9.png)

详情参考官方文档 [Create a Survey](https://docs.ansible.com/ansible-tower/latest/html/userguide/job_templates.html#ug-surveys)

## 参数

AWX 应用中包含 Nginx, Docker, PostgreSQL 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行`docker ps`，可以查看到 AWX 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
e240ed8209cd        awx_task:1.0.0.8    "/tini -- /bin/sh ..."   2 minutes ago       Up About a minute   8052/tcp                             awx_task
1cfd02601690        awx_web:1.0.0.8     "/tini -- /bin/sh ..."   2 minutes ago       Up About a minute   0.0.0.0:443->8052/tcp                 awx_web
55a552142bcd        memcached:alpine    "docker-entrypoint..."   2 minutes ago       Up 2 minutes        11211/tcp                            memcached
84011c072aad        rabbitmq:3          "docker-entrypoint..."   2 minutes ago       Up 2 minutes        4369/tcp, 5671-5672/tcp, 25672/tcp   rabbitmq
97e196120ab3        postgres:9.6        "docker-entrypoint..."   2 minutes ago       Up 2 minutes        5432/tcp                             postgres
```


下面仅列出 AWX 本身的参数：

### 路径{#path}

AWX 配置文件目录 */data/.awx*  
awx_postgres 挂载的目录：*/var/lib/postgresql/data*  
awx_postgres 数据持久存储：*/data/pgdocker*
awx_rabbitmq 挂载的目录：*/var/lib/rabbitmq*  
awx_web 挂载的目录：*/var/lib/nginx*   
awx_task 挂载的目录：*/var/lib/nginx* 

### 端口

无特殊端口

### 版本

```shell
sudo docker inspect awx_web
```

### 服务

```shell
#AWX-主程序
sudo docker start | stop | restart | pause | stats awx_task

#AWX-Web界面
sudo docker start | stop | restart | pause | stats awx_web

sudo docker start | stop | restart | pause | stats awx_rabbitmq
sudo docker start | stop | restart | pause | stats awx_postgres
sudo docker start | stop | restart | pause | stats awx_memcached
```

### 命令行

先运行  `pip install ansible-tower-cli` 安装 [AWX CLI ](https://docs.ansible.com/ansible-tower/latest/html/towercli/usage.html#installation)，然后配置使用

```
tower-cli config host http://<new-awx-host.example.com>
tower-cli config username <user>
tower-cli config password <pass>
tower-cli send assets.json
tower-cli user list 
```
更多参考：[ AWX CLI on AWX Github](https://github.com/ansible/awx/tree/devel/awxkit/awxkit/cli/docs)


### API

[Ansible Tower API Guide](https://docs.ansible.com/ansible-tower/latest/html/towerapi/index.html)