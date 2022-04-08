---
sidebar_position: 1
slug: /sakai
tags:
  - Sakai
  - LMS
  - 在线学习系统
---

# 快速入门

[Sakai](https://github.com/sakaiproject/sakai) ，中文名“赛课”，它是一个 100% 开源的在线学习系统。它被广泛用于学习、教学、研究和协作。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/sakai/sakai-gui-websoft9.png)

## 准备

部署 Websoft9 提供的 Sakai 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Sakai 的 **[默认账号和密码](./setup/credentials)**  
4. 若想用域名访问  Sakai **[域名五步设置](./dns#domain)** 过程


## Sakai 初始化向导

### 详细步骤

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://公网ip/portal/*  

2. 输入账号和密码（[查看](./setup/credentials)），登录


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

## Sakai 使用入门

下面以 **使用 Sakai 构建学习管理系统** 作为一个任务，帮助用户快速入门：


## Sakai 常用操作


## 参数{#parameter}

Sakai 应用中包含 Java, Nginx, Tomcat, Docker, MySQL 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。 

通过运行`docker ps`，可以查看到 Sakai 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Sakai 本身的参数：

### 路径{#path}

Sakai 安装目录：*/usr/local/tomcat/webapps*  
Sakai 配置目录: */usr/local/tomcat/sakai/sakai.properties*  

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 8080   | Sakai 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


### 版本{#version}

```shell
sudo cat /data/logs/install_version.txt
```

### 服务{#service}

```shell
```

### 命令行{#cli}

### API