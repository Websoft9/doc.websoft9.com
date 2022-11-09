---
sidebar_position: 1
slug: /scratch
tags:
  - Scratch
  - 少儿编程
---

# 快速入门

[Scratch](https://scratch.mit.edu/) 是一款由麻省理工学院设计开发的少儿编程工具。使用 Scratch，你可以编写属于你的互动程序，像是故事、游戏、动画，然后将你的创意分享给全世界。Scratch 3.0是一个部署在服务器上的 Web 版本，有浏览器就可以使用 Scratch。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/scratch/scratch-gui-websoft9.png)

## 准备

部署 Websoft9 提供的 Scratch 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Scratch 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  Scratch **[域名五步设置](./administrator/domain_step)** 过程


## Scratch 初始化向导{#init}

### 详细步骤

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 就进入了Scratch
![Scratch初始化页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/scratch/scratch-gui-websoft9.png)

2. Scratch首次加载数据超过 20 M，如果您的网络带宽不足的话，加载会很慢，耐心等待

> 需要了解更多Scratch的使用，请参考官方文档：[Scratch Documentation](https://en.scratch-wiki.info)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**[Scratch打开很慢？](./scratch/admin#slowy)**

## Scratch 使用入门

下面以 **Scratch 构建少儿编程系统** 作为一个任务，帮助用户快速入门：



## Scratch 常用操作

## 参数{#parameter}

Scratch 应用中包含 Nginx, Docker 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 Scratch 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                                   NAMES
537d4d38eef3   websoft9dev/scratch:latest   "nginx -g 'daemon of…"   58 seconds ago   Up 57 seconds   0.0.0.0:9001->80/tcp, :::9001->80/tcp   scratch
```

### 路径{#path}

Scratch 安装目录： */data/apps/scratch*  
Scratch 静态页面目录： */usr/share/nginx/html（容器内）*  

### 端口{#port}

无特殊端口

### 版本{#version}

控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart scratch
```

### 命令行{#cli}

无

### API

[Scratch API](https://en.scratch-wiki.info/wiki/Scratch_API)

