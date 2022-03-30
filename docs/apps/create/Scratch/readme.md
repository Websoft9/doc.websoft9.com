---
sidebar_position: 1
slug: /scratch
tags:
  - Scratch
  - 少儿编程
---

# 快速入门

[Scratch](https://scratch.mit.edu/) 是一款由麻省理工学院(MIT) 设计开发的一款面向少年的简易编程工具，scratch已经是少儿编程行业的基础软件。使用 Scratch，你可以编写属于你的互动媒体，像是故事、游戏、动画，然后你可以将你的创意分享给全世界。Scratch3.0是一个部署在服务器上的Web版本，有浏览器就可以使用Scratch。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/scratch/scratch-gui-websoft9.png)


部署 Websoft9 提供的 Scratch 之后，需完成如下的准备工作：

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Scratch 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  Scratch **[域名五步设置](./dns#domain)** 过程


## Scratch 初始化向导{#init}

### 详细步骤

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 就进入了Scratch
![Scratch初始化页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/scratch/scratch-gui-websoft9.png)

2. Scratch首次加载数据超过20M，如果您的网络带宽不足的话，加载会很慢，耐心等待

> 需要了解更多Scratch的使用，请参考官方文档：[Scratch Documentation](https://en.scratch-wiki.info)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**Scratch打开很慢**

Scratch首次加载数据超过20M。例如：您使用的是2M带宽，那么理想情况下的加载时间为：20000k/(128k/s×2)=78s。显然，如果带宽不足，速度会非常慢。

## Scratch 使用入门

下面以 **Scratch 构建少儿编程系统** 作为一个任务，帮助用户快速入门：



## Scratch 常用操作

### 配置域名{#dns}

参考： **[域名五步设置](./dns#domain)** 

### 配置 HTTPS{#https}

参考： **[HTTPS 配置](./dns#https)**


## 参数{#parameter}

**[通用参数表](./setup/parameter)** 中可查看 Nginx, Apache, Docker, MySQL 等 Scratch 应用中包含的基础架构组件路径、版本、端口等参数。 

通过运行`docker ps`，可以查看到 Scratch 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Scratch 本身的参数：

### 路径{#path}

Scratch 项目目录： */data/wwwroot/scratch*  
Scratch 静态页面目录： */data/wwwroot/scratch/build*  

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 80   | 通过HTTP访问 Scratch | 可选   |
| 443   | 通过HTTPS访问 Scratch  | 可选   |


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

