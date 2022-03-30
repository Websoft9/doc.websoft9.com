---
sidebar_position: 1
slug: /onlyoffice
tags:
  - ONLYOFFICE Workspace
  - 企业管理
  - CRM
---

# 快速入门

[ONLYOFFICE](https://onlyoffice.com) 是一款集成了文档、电子邮件、事件、任务和客户关系管理工具的开源在线办公套件。其文档管理功能实现了文档的在线编辑、在线预览和协同管理，可用于替代Office365或Google docs。另外，它还提供了CRM、项目管理等功能，非常合适作为企业内部的全员协作Office系统。  

ONLYOFFICE 包括三大套件：Community Server, Document Server and Mail Server，各司其职。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-websoft9-001.png)


部署 Websoft9 提供的 ONLYOFFICE 之后，需完成如下的准备工作：

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 ONLYOFFICE 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  ONLYOFFICE **[域名五步设置](./dns#domain)** 过程


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

**ONLYOFFICE 默认支持文档编辑与预览吗**

默认已经配置好，无需任何设置即可使用

**ONLYOFFICE 运行慢**

ONLYOFFICE 对内存要求比较高，建议最少 8G 内存

**本应用是否可以对外提供文档编辑与预览服务**

可以，*http://服务器公网IP:9002* 即服务地址


## ONLYOFFICE 使用入门

下面以 **ONLYOFFICE 构建企业ERP** 作为一个任务，帮助用户快速入门：



## ONLYOFFICE 常用操作

### Document Server

本章适合使用了 Websoft9 提供的 ONLYOFFICE Document Server 部署方案（区别于 ONLYOFFICE）。

#### 组件

包含：Nginx, ONLYOFFICE Document Server on Docker, Docker等三个组件。  

Nginx 用于接受用户访问请求，然后转发给 ONLYOFFICE Document Server on Docker。  

组件的详细信息参考 [*参数*](#path) 章节。

#### 访问

本地浏览器访问：*http://服务器公网IP:9002* 可看到 OnlyOffice Document Server 正在运行的提示。  
![ONLYOFFICE Document Server is running](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-dkisrunning-websoft9.png)

> 如果画面的提示不是*OnlyOffice Document Server is running*，则说明服务运行异常。

### ONLYOFFICE 文件预览与编辑

由 Websoft9 提供的 ONLYOFFICE 部署方案默认包含 ONLYOFFICE Document Server，并已完成设置，无需任何设置即可在线编辑和预览文档。

下面展现文档预览与编辑的设置原理，仅供后续个性化修改参考：

* 登录到 ONLYOFFICE ，依次打开：【设置】>【集成】>【文件服务】，你可以看到预配置：
  ![ONLYOFFICE 文件服务](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-preview-websoft9.png)

* 本地浏览器访问：*http://服务器公网IP:9002*，会看到 OnlyOffice Document Server 正在运行的提示 
   ![ONLYOFFICE document is running ](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-dkisrunning-websoft9.png)

> 请勿修改默认的文档配置，除非你打算采用其他文档服务替换它

### ONLYOFFICE 设置语言

登录 ONLYOFFICE，在后台 【设置】>【通用】>【自定义】中设置语言

![ONLYOFFICE 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-lanuageset-websoft9.png)


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

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数
   
2. 登录 ONLYOFFICE 控制台，依次打开：【设置】>【集成】>【SMTP设置】

3. 准确填写 SMTP 参数
   ![ONLYOFFICE SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-smtp-1-websoft9.png)

   > 【主机登录】与【发件人电邮地址】必须保持一致，否则无法发送邮件。

4. 点击【发送邮件测试】

### 配置域名{#dns}

参考： **[域名五步设置](./dns#domain)** 

### 配置 HTTPS{#https}

参考： **[HTTPS 配置](./dns#https)**


## 参数{#parameter}

**[通用参数表](./setup/parameter)** 中可查看 Nginx, Apache, Docker, MySQL 等 ONLYOFFICE 应用中包含的基础架构组件路径、版本、端口等参数。 

通过运行`docker ps`，可以查看到 ONLYOFFICE 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 ONLYOFFICE 本身的参数：

### 路径{#path}

ONLYOFFICE Community Server存储目录： */data/wwwroot/communityserver*  
ONLYOFFICE docker-compose 文件路径： */data/wwwroot/onlyoffice/docker-compose.yml*  
ONLYOFFICE 日志目录： */data/wwwroot/onlyoffice/communityserver/logs*

ONLYOFFICE Document Server存储目录： */data/apps/onlyofficedocumentserver*  
ONLYOFFICE Docs docker-compose 文件路径： */data/apps/onlyofficedocumentserver/docker-compose.yml*  
ONLYOFFICE 日志目录： */data/apps/onlyofficedocumentserver/logs*

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 8080   | ONLYOFFICE 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |
| 9002   | ONLYOFFICE Document Server on Docker  | 可选   |


### 版本{#version}

```shell
sudo cat /data/logs/install_version.txt
```

### 服务{#service}

```shell
sudo docker start | stop | restart onlyofficecommunityserver
sudo docker start | stop | restart onlyofficedocumentserver
```

### 命令行{#cli}

### API

### 参考{#ref}

