---
sidebar_position: 1
slug: /gogs
tags:
  - Gogs
  - DevOps
---

# 快速入门

[Gogs](https://github.com/gogs/gogs) 是一款极易搭建的自助 Git 仓库系统，相对于 GitLab 而言 Gogs 更加轻量级。 
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-guisart-websoft9.png)



部署 Websoft9 提供的 Gogs 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Gogs 的 **[默认管理员账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  Gogs，务必先完成 **[域名五步设置](./dns#domain)** 过程

## Gogs 安装向导

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入初始化页面

2. 填写数据库连接信息（**[查看预装的数据库账号密码](./setup/credentials#getpw)** ）

    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-installdb-websoft9.png)

2. 设置 Gogs 的应用基本参数   

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-installset-websoft9.png)

3. 配置完成后，系统进入登录界面 

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-installreg-websoft9.png)

4. 由于还没有账户，请先点击【还没账户？马上注册】链接，开始注册一个管理员账号

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-installreg2-websoft9.png)

5. 使用新注册的账号登录 Gogs 后台 

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-backend-websoft9.png)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。


## 常用操作

## 参数

**[通用参数表](../setup/parameter)** 中可查看 Nginx, Docker, MySQL 等 Gogs 应用中包含的基础架构组件路径、版本、端口等参数。 

下面仅列出 Gogs 本身的参数：

### 路径{#path}

Gogs 安装目录: */data/apps/gogs* 

### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 3000   | Jenkins 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


### 版本

```shell
sudo docker inspect gogs
```

### 服务

```shell
sudo docker start | stop | restart | stats gogs
```

### 命令行

暂无

### API

暂无

