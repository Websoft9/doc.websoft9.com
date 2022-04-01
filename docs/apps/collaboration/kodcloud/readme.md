---
sidebar_position: 1
slug: /kodcloud
tags:
  - KodCloud
  - 网盘
  - 知识管理
  - 团队协作
---

# 快速入门

[KodCloud](https://kodcloud.com)-可道云 是一款基于Web的在线文件管理和代码编辑器系统，界面风格和操作体验类似Windows，及其好用。合适构建私有企业网盘、云资源管理、多媒体管理、网站管理等场景。 

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodexplorer/kodcloud-gui-websoft9.png)

部署 Websoft9 提供的 KodCloud 之后，需完成如下的准备工作：

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 KodCloud 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  KodCloud **[域名五步设置](./dns#domain)** 过程


## KodCloud 初始化向导{#init}

### 详细步骤

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）

2. 在下面的界面设置 admin 管理员用户的密码
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodexplorer/kodexplorer-setadminpw-websoft9.png)

3.  设置管理员密码后，系统转到登录界面
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodexplorer/kodexplorer-login-websoft9.png)

4.  登录成功，系统进入后台，如果有新版本，系统会提示是否自动更新。点击“自动更新”，系统会自动完成更换后要求重新登录
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodexplorer/kodexplorer-updateauto-websoft9.png)

5.  登录成功，进入后台，开始体验后台  
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodexplorer/kodexplorer-backend-websoft9.png)

6. 进入后台，体验系统的完整功能

> 需要了解更多 KodCloud 的使用，请参考官方文档：[KodCloud Help](https://kodcloud.com/help/)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**本部署包采用的哪个数据库来存储 KodCloud 数据**

KodCloud 无需数据库支持

## KodCloud 使用入门

下面以 **KodCloud 构建企业网盘系统** 作为一个任务，帮助用户快速入门：


## KodCloud 常用操作

### 配置 SMTP{#smtp}

### 配置域名{#dns}

参考： **[域名五步设置](./dns#domain)** 

### 配置 HTTPS{#https}

参考： **[HTTPS 配置](./dns#https)**

## 参数{#parameter}

**[通用参数表](./setup/parameter)** 中可查看 Nginx, Apache, Docker, MySQL 等 KodCloud 应用中包含的基础架构组件路径、版本、端口等参数。 

通过运行`docker ps`，可以查看到 KodCloud 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 KodCloud 本身的参数：

### 路径{#path}

KodCloud 安装目录： */data/wwwroot/kodcloud*  

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 80   | 通过 HTTP 访问 KodCloud | 可选   |


### 版本{#version}

```shell
sudo cat /data/logs/install_version.txt
```

### 服务{#service}

```shell


```

### 命令行{#cli}

### API

[官方API](http://doc.kodcloud.com/#/start)

### 参考{#ref}

