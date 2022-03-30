---
sidebar_position: 1
slug: /alfresco
tags:
  - Alfresco
  - 企业管理
  - ERP
---

# 快速入门

[Alfresco Community Edition](https://www.alfresco.com/ecm-software/alfresco-community-editions) 是开源的企业内容管理系统，它面向大中型客户，作为一个灵活、可扩展的 ECM 平台，Alfresco Content Services 支持一系列用例，包括内容服务、信息治理、上下文搜索和洞察力，与领先业务应用程序 SAP, IBM Lotus, Microsoft Office, SharePoint 和 Google Docs 等轻松集成。

![Alfresco 系统架构](https://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-arcgui-websoft9.png)


部署 Websoft9 提供的 Alfresco 之后，需完成如下的准备工作：

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Alfresco 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  Alfresco **[域名五步设置](./dns#domain)** 过程


## Alfresco 初始化向导{#init}

### 详细步骤

1. 使用本地电脑的浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入登陆界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](./setup/credentials#getpw)），成功登录到 Alfresco 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-consolegui-websoft9.png)

3. Alfresco会自动根据浏览器语言来选择程序语言

> 需要了解更多 Alfresco 的使用，请参考官方文档：[Alfresco Documentation](https://docs.alfresco.com/content-services/community/using/content/) 和 [Alfresco Videos](https://docs.alfresco.com/content-services/latest/tutorial/video/)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**Alfresco 服务启动失败**

Alfresco 开机启动最少需要 10 分钟，请耐心等待


## Alfresco 使用入门

下面以 **Alfresco 传递数据** 作为一个任务，帮助用户快速入门：

- 后台仪表盘
  ![Alfresco台仪表盘](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-adminui-websoft9.png)

- 我的文档
  ![Alfresco我的文档](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-mydocs-websoft9.png)

- 共享文档
  ![Alfresco共享文档](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-sharedocs-websoft9.png)

- 增加多用户
  ![Alfresco增加多用户](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-addusers-websoft9.png)

- 增加组（部门）
  ![Alfresco增加组（部门）](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-addgroup-websoft9.png)

- 工作流（审批）
  ![Alfresco工作流（审批）](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-workflow-websoft9.png)

## Alfresco 常用操作

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数
   
2. 登录 Alfresco 控制台，设置 SMTP 参数（暂未找到具体方案）

### 配置域名{#dns}

参考： **[域名五步设置](./dns#domain)** 

### 配置 HTTPS{#https}

参考： **[HTTPS 配置](./dns#https)**

### 重置密码

常用的 Alfresco 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码

1. 登录 Alfresco 后台，右上角依次打开：【Administrator】>【我的个人档案】
  ![Alfresco 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-modifypw-websoft9.png)

2. 点击【更改密码】，开始修改密码

#### 找回密码

如果用户忘记了密码，需要通过修改数据库中的密码信息来重置密码：

1. 使用 **SSH** 连接到 Alfresco 所在的服务器

2. 进入到 alfresco 数据库的 PSQL 交互式状态
   ```
   docker exec -it alfresco-postgres psql -U alfresco -d alfresco
   ```

3. 运行如下的修改密码命令（新的密码为 **admin**）
   ```
   UPDATE alf_node_properties SET string_value='209c6174da490caeb422f3fa5a7ae634' WHERE node_id=4 and qname_id=10
   ```

4. 退出容器交互式模式，回到服务器命令行中重启所有容器后生效
   ```
   cd /data/wwwroot/alfresco
   docker-compose restart
   ```

## 参数{#parameter}

**[通用参数表](./setup/parameter)** 中可查看 Nginx, Apache, Docker, MySQL 等 Alfresco 应用中包含的基础架构组件路径、版本、端口等参数。 

通过运行`docker ps`，可以查看到 Alfresco 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Alfresco 本身的参数：

### 路径{#path}

Alfresco 安装目录： */data/wwwroot/alfresco*  
Alfresco 容器存储目录： */data/wwwroot/alfresco/volumes/alfresco*  
Alfresco 日志目录： */data/wwwroot/alfresco/volumes/alfresco/share/logs*  

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 8080   | Alfresco 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |



### 版本{#version}

```shell
sudo cat /data/logs/install_version.txt
```

### 服务{#service}

```shell
sudo docker-compose start | stop | restart alfresco-server
```

### 命令行{#cli}

### API

### 参考{#ref}

