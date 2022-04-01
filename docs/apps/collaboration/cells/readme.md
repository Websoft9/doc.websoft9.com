---
sidebar_position: 1
slug: /cells
tags:
  - Cells
  - 网盘
  - 知识管理
  - 团队协作
---

# 快速入门

Cells 是 [Pydio](pydio.com) 旗下一个功能强大在线文件管理系统（ECM），采用PHP+MySQL开发，用于构建自托管的企业网盘和云存储系统，支持多用户的文档协作、分享、设备同步。功能全面，包括：文档管理、用户管理、权限管理，甚至还有能够恢复删除的文件等功能，开源版支持的设备APP非常全面，包括：IOS、Android、Windows、OSX、Linux五个客户端同步APP。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-login-websoft9.png)

部署 Websoft9 提供的 Cells 之后，需完成如下的准备工作：

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Cells 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  Cells **[域名五步设置](./dns#domain)** 过程


## Cells 初始化向导{#init}

### 详细步骤

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   
2. 选择语言，点击"Start Wizard"
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-install001-websoft9.png)

3. 设置管理员账号，进入下一步
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-install002-websoft9.png)

4. 选择Mysql数据库，填写数据库信息（[查看数据库账号密码](./setup/credentials#getpw)），点击“test db connection”进入下一步
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-install003-websoft9.png)

5. 进入高级设置，设置默认语言为“简体中文”，点击“Install Pydio”，开始安装
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-install004-websoft9.png)

6. 安装完成后，登录后台
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-login-websoft9.png)

7. 后台界面
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-bk-websoft9.png)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**Cells 是否提供移动端**

提供了移动端，[下载地址](https://pydio.com/en/download)

**Cells 默认是否可以编辑 Office 文档**

不可以，需要自行配置文档预览服务器

## Cells 使用入门

下面以 **Cells 构建文档管理系统** 作为一个任务，帮助用户快速入门：


## Cells 常用操作

### 配置域名{#dns}

参考： **[域名五步设置](./dns#domain)** 

### 配置 HTTPS{#https}

参考： **[HTTPS 配置](./dns#https)**

## 参数{#parameter}

**[通用参数表](./setup/parameter)** 中可查看 Nginx, Apache, Docker, MySQL 等 Cells 应用中包含的基础架构组件路径、版本、端口等参数。 

通过运行`docker ps`，可以查看到 Cells 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Cells 本身的参数：

### 路径{#path}

Cells 安装目录： */data/wwwroot/cells*  

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 80  | 通过 HTTP 访问 Cells | 可选   |


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

