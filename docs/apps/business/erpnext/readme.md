---
sidebar_position: 1
slug: /erpnext
tags:
  - ERPNext
  - 企业管理
  - ERP
---

# 快速入门

[ERPNext](https://erpnext.com/)  是一个 100% 开源的 ERP，基于 Python 和 Node 开发。它功能全面，包含会计、人力资源、制造、网站、电商、CRM、资产管理、客服工作台等全面的功能。它是 SAP 的开源替代品，全球已经有超过 5,000 家企业客户使用。

![](http://libs.websoft9.com/Websoft9/DocsPicture/en/erpnext/erpnext-adminui-websoft9.png)

## 准备

部署 Websoft9 提供的 ERPNext 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 ERPNext 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  ERPNext **[域名五步设置](./dns#domain)** 过程


## ERPNext 初始化向导{#init}

### 详细步骤

1. 使用本地电脑 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入初始化页面
   ![erpnext安装登录](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](./setup/credentials#getpw)），选择语言， 进入下一步 
   ![erpnext安装](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-language-websoft9.png)

3. 根据安装向导依次完成后续步骤

4. 安装完成之后，ERPNext 会弹出如下界面
   ![erpnext后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-cpsetup-websoft9.png)

   可能会出现安装错误提示，此时需要反复安装：
   ![erpnext 向导安装报错](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-wizarderror-websoft9.png)

5. ERPNext 顶部菜单中提供了搜索框，用于快速检索并进入 ERPNext 所有的功能
   ![erpnext 快速检索](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-sbar-websoft9.png)

6. 通过检索功能，进入【用户】设置，可以管理当前系统下所有账号
   ![erpnext 用户管理](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-users-websoft9.png)


> 需要了解更多 ERPNext 的使用，请参考官方文档：[ERPNext Documentation](https://docs.erpnext.com)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**ERPNext 服务启动失败？**

请确认hostname是否包含字符串 "."，例如 erpnext12.14.0 对于 ERPNext 来说是一个不合规的 hostname

你可以使用下列命令来修改hostname：

```
hostnamectl set-hostname erpnext
```


## ERPNext 使用入门

下面以 **ERPNext 构建企业ERP** 作为一个任务，帮助用户快速入门：



## ERPNext 常用操作

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数
   
2. 登录 ERPNext控制台，在【设置】>【电子邮件域名】填写SMTP参数
![ERPNext SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/erpnext/erpnext-smtp-websoft9.png)

3. 点击【保存】后，系统后进行一个 SMTP 初步验证，验证通过才能保存成功

### 域名额外配置（修改 URL） {#dns}

**[域名五步设置](./dns#domain)** 完成后，需设置 ERPNext 的 SITE_URL：

1. 连接服务器，修改 ERPNext 容器环境变量文件：*/data/wwwroot/erpnext/.env*  
   
   ```
   ...
   APP_SITE_URL=your domain
   APP_SITE_NAME=`your domain`
   ...
   ```


3. 重启 ERPNext 
   ```
   docker-compose up -d 
   ```

### 重置密码

常用的 ERPNext 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码

1. 登录 ERPNext后台，依次打开：【设置】>【个人设置】，找到修改密码项
  ![ERPNext 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-modifypw-websoft9.png)

2. 直接设置新密码，保存后生效

#### 找回密码

如果用户忘记了 ERPNext 密码，可以通过如下的命令直接设置一个新密码：

```
sudo -H -u erpnext bash -c "cd /data/wwwroot/frappe-bench && export GIT_PYTHON_REFRESH=quiet && /usr/local/bin/bench set-admin-password newpassword"
```

## 参数{#parameter}

ERPNext 应用中包含 Nginx, Redis, MariaDB, Docker 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。  

通过运行`docker ps`，可以查看到 ERPNext 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                        COMMAND                  CREATED             STATUS             PORTS                                       NAMES
949746dc0e88   frappe/frappe-socketio:v13   "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-socketio
030c4324b810   frappe/erpnext-worker:v13    "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-schedule
5816692bb579   frappe/erpnext-worker:v13    "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-worker-long
09b2e2242549   frappe/erpnext-worker:v13    "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-worker-short
2252928c2230   frappe/erpnext-worker:v13    "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-worker-default
4108b4ca06d5   redis:latest                 "docker-entrypoint.s…"   About an hour ago   Up About an hour   6379/tcp                                    erpnext-redis-cache
bbe639069a28   redis:latest                 "docker-entrypoint.s…"   About an hour ago   Up About an hour   6379/tcp                                    erpnext-redis-queue
29f4870961b4   mariadb:10.3                 "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp   erpnext-mariadb
9aecda1e6f3e   redis:latest                 "docker-entrypoint.s…"   About an hour ago   Up About an hour   6379/tcp                                    erpnext-redis-socketio
a404ca45d127   frappe/erpnext-nginx:v13     "/docker-entrypoint.…"   About an hour ago   Up About an hour   0.0.0.0:8000->80/tcp, :::8000->80/tcp       erpnext-nginx
39d908b3132e   frappe/erpnext-worker:v13    "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-worker
```

> erpnext-worker-default 为项目主容器

下面仅列出 ERPNext 本身的参数：

### 路径{#path}

ERPNext 路径:  */data/wwwroot/erpnext*  
ERPNext 数据库配置文件: */data/wwwroot/erpnext/.env*  
ERPNext 日志路径:  */data/wwwroot/erpnext/volumes/erpnext-logs-vol*  
ERPNext 应用路径 : */data/wwwroot/frappe-bench/volumes/erpnext-site-vol*  
ERPNext 附件路径:  */data/wwwroot/frappe-bench/volumes/erpnext-assets-vol*     
ERPNext 备份位置：*/var/lib/docker/volumes/docker-erpnext_sites-vol/_data/IP/private/backups*  

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 8080   | ERPNext 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


### 版本{#version}

控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats erpnext-worker-default
```

### 命令行{#cli}

[CLI to manage Multi-tenant deployments for Frappe apps](https://github.com/frappe/bench)

### API

参考： [ERPNext API](https://frappeframework.com/docs/user/en/api)

