---
sidebar_position: 1
slug: /onlyoffice
tags:
  - ONLYOFFICE Workspace
  - 企业管理
  - CRM
---

# 快速入门

[ONLYOFFICE Workspace](https://onlyoffice.com) 是一款集成了 Office 在线文档、电子邮件、事件、任务和客户关系管理工具的开源软件，适用于高效的团队管理和协作能力。 它可以当做 Office 365 或 Google Docs 的替代品，也可以当做一个内部企业门户应用（OA）。

> 为了便于表达，以下用 ONLYOFFICE 代指 ONLYOFFICE Workspace  


![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-websoft9-001.png)

## 准备

部署 Websoft9 提供的 ONLYOFFICE Workspace 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80，9002** 端口已经开启
3. 在服务器中查看 ONLYOFFICE Workspace 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  ONLYOFFICE Workspace **[域名五步设置](./administrator/domain_step)** 过程


## ONLYOFFICE 初始化向导{#init}

### 详细步骤

1. 使用本地 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入初始化页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-installwait-websoft9.png)

2. 耐心等待 ONLYOFFICE 初始化过程（可能会持续2-5分钟），直至出现如下界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-install-websoft9.png)

3. 设置自己的密码和邮箱（作为登录的用户名），勾选条款后点击【Continue】开始安装
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-bk-websoft9.png)

4. 登录到 ONLYOFFICE 后台，开始使用。  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-websoft9-001.png)

   * **文档管理**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-websoft9-002.png)

   * **项目管理**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-websoft9-003.png)

   * **客户关系管理（CRM）**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-websoft9-004.png)

   * **文档在线编辑（默认可用，无需任何设置）**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-websoft9-005.png)

   * **社区博客**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-function-club-websoft9.png)

   * **邮件管理门户**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-function-email-websoft9.png)

   * **第三方APP集成**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-function-apps-websoft9.png)

> 需要了解更多 ONLYOFFICE 的使用，请参考官方文档：[ONLYOFFICE Documentation](https://helpcenter.onlyoffice.com/server/docker/opensource/index.aspx)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**ONLYOFFICE 运行慢？**

ONLYOFFICE 对内存要求比较高，建议最少 8G 内存

## ONLYOFFICE 使用入门

下面以 **ONLYOFFICE 构建集成邮件服务器** 作为一个任务，帮助用户快速入门：



## ONLYOFFICE 常用操作

### 文件预览与编辑

本方案中默认包含文档中间件 [ONLYOFFICE Docs](./onlyofficedocs)，并已完成设置，无需任何设置即可在线编辑和预览文档。

下面是 ONLYOFFICE 配置文件预览与编辑的设置界面，仅供后续个性化修改参考：

* 登录到 ONLYOFFICE ，依次打开：【设置】>【集成】>【文件服务】，你可以看到预配置：
  ![ONLYOFFICE 文件服务](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-preview-websoft9.png)

* 本地浏览器访问：*http://服务器公网IP:9002*，会看到 OnlyOffice Docs 正在运行的提示 
   ![ONLYOFFICE document is running ](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-dkisrunning-websoft9.png)

> 请勿修改默认的文档配置，除非你打算采用其他文档服务替换它

### 设置语言

登录 ONLYOFFICE，在后台 【设置】>【通用】>【自定义】中设置语言

![ONLYOFFICE 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-lanuageset-websoft9.png)

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数
   
2. 登录 ONLYOFFICE 控制台，依次打开：【设置】>【集成】>【SMTP设置】

3. 准确填写 SMTP 参数
   ![ONLYOFFICE SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-smtp-1-websoft9.png)

   > 【主机登录】与【发件人电邮地址】必须保持一致，否则无法发送邮件。

4. 点击【发送邮件测试】


### 重置密码

常用的 ONLYOFFICE 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码

1. 登录 ONLYOFFICE 后台，依次打开：【Administrator】>【个人资料】，先完成**电子邮件验证**
  ![ONLYOFFICE 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-modifypw001-websoft9.png)

2. 重新回到个人资料页面，点击【Administrator】下的到下角，就会看到修改密码入口
  ![ONLYOFFICE 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-modifypw002-websoft9.png)

#### 找回密码

如果用户忘记了密码，建议通过邮件的方式找回密码：

1. 完成 [SMTP 设置](#smtp)

2. 打开 ONLYOFFICE 登录页面，点击【Forgot】开始通过邮件找回密码
  ![ONLYOFFICE 找回密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-forgetpw-websoft9.png)


## ONLYOFFICE 参数{#parameter}

ONLYOFFICE Workspace 应用中包含 Nginx, Docker, MySQL, phpMyAdmin, [ONLYOFFICE Docs](./onlyofficedocs) 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 ONLYOFFICE 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                               COMMAND                  CREATED          STATUS          PORTS                                                                                                                                                                                          NAMES
9e404a923dbb   onlyoffice/controlpanel:3.0.3.410   "/var/www/onlyoffice…"   17 seconds ago   Up 14 seconds   80/tcp, 443/tcp                                                                                                                                                                                onlyoffice-control
e9180dd570a4   onlyoffice/communityserver:latest   "/app/run-community-…"   20 seconds ago   Up 15 seconds   3306/tcp, 5280/tcp, 9865-9866/tcp, 9871/tcp, 9882/tcp, 9888/tcp, 0.0.0.0:5222->5222/tcp, :::5222->5222/tcp, 0.0.0.0:9003->80/tcp, :::9003->80/tcp, 0.0.0.0:49153->443/tcp, :::49153->443/tcp   onlyoffice
2a191ade9b10   onlyoffice/documentserver:7.0       "/app/ds/run-documen…"   25 seconds ago   Up 16 seconds   443/tcp, 0.0.0.0:9002->80/tcp, :::9002->80/tcp                                                                                                                                                 onlyoffice-docs
c90ae46964ba   mysql:5.7                           "docker-entrypoint.s…"   25 seconds ago   Up 16 seconds   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp                                                                                                                                           onlyoffice-db
```


下面仅列出 ONLYOFFICE 本身的参数：

### 路径{#path}

ONLYOFFICE Workspace 安装目录： */data/apps/onlyoffice*  
ONLYOFFICE Workspace 存储目录： */data/apps/onlyoffice/data/community_data*  
ONLYOFFICE Workspace 日志目录： */data/apps/onlyoffice/data/community_log*  
ONLYOFFICE Workspace 文档目录： */data/apps/onlyoffice/data/document_data* 



### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9002   | ONLYOFFICE docs  | 可选   |


### 版本{#version}

```shell
# ONLYOFFICE Community Server version
docker image inspect onlyoffice/communityserver  | grep onlyoffice.community.version | sed -n 1p
```

### 服务{#service}

```shell
sudo docker start | stop | restart onlyoffice
sudo docker start | stop | restart onlyoffice-db
sudo docker start | stop | restart onlyoffice-control
sudo docker start | stop | restart onlyoffice-docs
```

### 命令行{#cli}

无

### API

[ONLYOFFICE API](https://api.onlyoffice.com/)

