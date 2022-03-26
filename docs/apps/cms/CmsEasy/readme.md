---
sidebar_position: 1
slug: /cmseasy
tags:
  - CmsEasy
  - CMS
  - 建站系统
---

# 快速入门

[CmsEasy](cmseasy.cn)是一个源自中国本土的100%开源免费的CMS，基于PHP+MySQL开发，采用模块化架构，拥有全新的设计体验与传播方式，后台功能让你的创作去繁化简， 响应式UI设计，全面支持PC和移动端访问。功能非常全面，文章、产品、表单、支付等网站所需功能一应具全。


部署 Websoft9 提供的 CmsEasy 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 CmsEasy 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  CmsEasy **[域名五步设置](./dns#domain)** 过程


## CmsEasy 初始化向导

### 详细步骤

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cmseasy/cmseasy-startinstall-websoft9.png)

2. 完成通过许可协议、环境检测之后，进入配置数据库界面（[查看数据库账号密码](./setup/credentials#getpw)）
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cmseasy/cmseasy-installsetpw-websoft9.png)

3. 设置管理员账号，牢记之，点击“安装” 
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cmseasy/cmseasy-setadmin-websoft9.png)

4. 系统安装成功，系统提示 
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cmseasy/cmseasy-installss-websoft9.png)

5. 进入后台登录,开始体验后台 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cmseasy/cmseasy-backend-websoft9.png)

说明：CmsEasy的后台地址是：*http://域名/admin*

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

## CmsEasy 使用入门

下面以 **使用 CmsEasy 构建内容管理系统** 作为一个任务，帮助用户快速入门：


## CmsEasy 常用操作

### 配置 SMTP{#smtp}

### 配置域名{#dns}

参考： **[域名五步设置](./dns#domain)** 

### 配置 HTTPS{#https}

参考： **[HTTPS 配置](./dns#https)**

## 参数{#parameter}

**[通用参数表](../setup/parameter)** 中可查看 Nginx, Apache, Docker, MySQL 等 CmsEasy 应用中包含的基础架构组件路径、版本、端口等参数。 

通过运行`docker ps`，可以查看到 CmsEasy 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 CmsEasy 本身的参数：

### 路径{#path}

CmsEasy 安装目录： */data/wwwroot/cmseasy*  

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 8080   | CmsEasy 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


### 版本{#version}

```shell
sudo cat /data/logs/install_version.txt
```

### 服务{#service}

```shell
```

### 命令行{#cli}

### API

### 参考{#ref}

 [《PHP运行环境》](./runtime/php) 
