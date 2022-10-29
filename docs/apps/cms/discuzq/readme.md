---
sidebar_position: 1
slug: /discuzq
tags:
  - Discuz!Q
  - CMS
  - 建站系统
  - 博客系统
---

# 快速入门

[Discuz!Q](https://discuz.com/) 是开源的论坛系统，用于构建知识付费、内容变现的圈子或私域流量应用。它拥有完全开源、提供丰富接口、前后端分离、轻量化、数据独立可控、敏捷上云、快速变现七大能力。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuzq/discuzq-guim-websoft9.webp)

## 准备

部署 Websoft9 提供的 Discuz!Q 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Discuz!Q 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  Discuz!Q **[域名五步设置](./administrator/domain_step)** 过程


## Discuz!Q  初始化向导{#init}

### 详细步骤

1. 本地电脑浏览器访问网址：*http://域名/install* 或 *http://服务器公网IP/install*, 进入初始化界面

2. 设置：数据库连接（**不建议做任何更改**）和管理员账号，然后点击【安装】进入下一步
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-setting-websoft9.png)

3. 安装完成，手机扫描右侧二维码可以进入移动端页面。  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-installok-websoft9.png)

4. 本地电脑浏览器访问网址：输入*http://域名/admin* 或 *http://服务器公网IP/admin*, 进入登录页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-admin-websoft9.png)

5. 输入账号密码（[不知道账号密码？](./user/credentials)），成功登录到 Discuz!Q 后台 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-index-websoft9.png)
    
6. 其他设置：微信公众号，小程序，微信支付等
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-waychat-websoft9.png)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：


## Discuz!Q 使用入门

下面以 **使用 Discuz!Q 构建论坛系统** 作为一个任务，帮助用户快速入门：


## Discuz!Q 常用操作


## Discuz!Q 参数{#parameter}

Discuz!Q 应用中包含 Nginx, Docker, MySQL 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 Discuz!Q 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                                                  NAMES
54d7748385cf   phpmyadmin:latest            "/docker-entrypoint.…"   38 minutes ago   Up 38 minutes   0.0.0.0:9090->80/tcp, :::9090->80/tcp                  phpmyadmin
b63e355487a0   websoft9dev/discuzq:latest   "/tmp/cmd.sh"            39 minutes ago   Up 39 minutes   443/tcp, 0.0.0.0:9001->80/tcp, :::9001->80/tcp         discuzq
322344b7aad5   mysql:5.7                    "docker-entrypoint.s…"   39 minutes ago   Up 39 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   discuzq-db
```

### 路径{#path}

Discuz!Q 安装目录： */data/apps/discuzq*  
Discuz!Q 站点目录： */data/apps/discuzq/data/discuzq*  

### 网址

Discuz!Q 后台地址： *http://域名/admin*  

### 端口{#port}

无特殊端口

### 版本{#version}

```
sudo docker exec -it discuzq bash -c 'grep -rn "const VERSION =" /var/www/discuz/vendor/discuz/core/src/Foundation/Application.php | awk "{print \$5}" | tr -d ";"'
```

### 服务{#service}

```shell
sudo docker start | stop | restart | stats discuzq
sudo docker start | stop | restart | stats discuzq-db
sudo docker start | stop | restart | stats phpmyadmin
```

### 命令行{#cli}

无

### API

[官方API](https://discuz.com/api-docs/v1/)