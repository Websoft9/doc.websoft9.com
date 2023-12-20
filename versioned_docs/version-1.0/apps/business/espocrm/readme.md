---
sidebar_position: 1
slug: /espocrm
tags:
  - EspoCRM
  - CRM
  - 客户成功
---

# 快速入门

[EspoCRM](https://www.espocrm.com/demo/) 是一个开源的轻量级CRM，采用响应式设计，界面非常美观大方，能够自动适应PC、平板和手机访问。功能非常全面，包括销售自动化、市场、销售过程、文档、产品、合同、知识库和工作流等功能。支持字段和表单布局客制化，便于定制。
![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/espocrm-gui-websoft9.jpg)


## 准备

部署 Websoft9 提供的 EspoCRM 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 EspoCRM 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  EspoCRM **[域名五步设置](./administrator/domain_step)** 过程


## EspoCRM 初始化向导{#init}

### 详细步骤


1. 本地浏览器访问：*http://域名* 或 *http://公网IP* , 进入登录页面，输入[账号密码](./user/credentials)登录

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-login-websoft9.png)

2. 进入后台，体验系统的完整功能

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-main-websoft9.png)

> 需要了解更多 EspoCRM 的使用，请参考官方文档：[EspoCRM Documentation](https://www.espocrm.com/documentation/)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：


## EspoCRM 使用入门

下面以 **EspoCRM 构建企业CRM** 作为一个任务，帮助用户快速入门：


## EspoCRM 常用操作

### 配置 SMTP{#smtp}

EspoCRM支持第三方的SMTP发送邮件模式，具体如下：

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数
   
2. 待EspoCRM安装完成后，点击右上角菜单->admin，点击【电子邮件账户】进行个人邮箱的添加或编辑
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-smtp-1-websoft9.png)

3. 根据下图的设置，进行收发邮件的设置，分别设置 IMAP/SMTP 参数

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-smtp-2-websoft9.png)

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-smtp-3-websoft9.png)

4. 设置完成后，请点击“Send Test Email”测试设置是否成功

## EspoCRM 参数{#parameter}

EspoCRM 应用中包含 PHP, Apache, Docker, MySQL, phpMyAdmin 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行`docker ps`，可以查看到 EspoCRM 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE               COMMAND                  CREATED          STATUS          PORTS                                               NAMES
b7518429ca6d   phpmyadmin:latest   "/docker-entrypoint.…"   29 minutes ago   Up 29 minutes   0.0.0.0:9090->80/tcp, :::9090->80/tcp               phpmyadmin
764219b50614   espocrm/espocrm     "docker-daemon.sh"       30 minutes ago   Up 29 minutes   80/tcp                                              espocrm-daemon
e16a2e7fef6d   mysql:8             "docker-entrypoint.s…"   30 minutes ago   Up 30 minutes   3306/tcp, 33060/tcp                                 espocrm-db
e768059102e7   espocrm/espocrm     "docker-entrypoint.s…"   30 minutes ago   Up 30 minutes   0.0.0.0:9001->80/tcp, :::9001->80/tcp               espocrm
f7a3374937b2   espocrm/espocrm     "docker-websocket.sh"    30 minutes ago   Up 29 minutes   80/tcp, 0.0.0.0:9002->8080/tcp, :::9002->8080/tcp   espocrm-websocket
```

### 路径{#path}

EspoCRM 安装目录:  */data/apps/espocrm*  
EspoCRM 站点目录:  */data/apps/espocrm/data/espocrm*  

### 端口{#port}

无特殊端口

### 版本{#version}

```
sudo docker exec -i espocrm cat /var/www/html/data/config.php|grep "'version' =>" |cut -d">" -f2
```

### 服务{#service}

```shell
sudo docker start | stop | restart | stats espocrm
sudo docker start | stop | restart | stats espocrm-db
sudo docker start | stop | restart | stats espocrm-daemon
sudo docker start | stop | restart | stats espocrm-websocket
sudo docker start | stop | restart | stats phpmyadmin
```

### 命令行{#cli}

[Console Commands](https://docs.espocrm.com/administration/commands/)

### API
[EspoCRM REST API](https://docs.espocrm.com/development/api/)

