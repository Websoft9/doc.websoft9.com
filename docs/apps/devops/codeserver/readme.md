---
sidebar_position: 1
slug: /codeserver
tags:
  - code-server
  - 在线编辑器
---

# 快速入门

[code-server](https://github.com/cdr/code-server) 是社区创作的 Web 版 VS Code，后端运行在服务器中，开发者基于浏览器运行 IDE。

![code-server 界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-consolegui-websoft9.png)


部署 Websoft9 提供的 code-server 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 code-server 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  code-server，务必先完成 **[域名五步设置](./dns#domain)** 过程

## code-server 初始化向导

### 详细步骤

1. 使用本地 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入登录页面
   ![code-server 登录界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-login-websoft9.png)

2. 输入密码（[不知道账号密码？](/zh/stack-accounts.md#codeserver)），成功登录到 code-server 后台  
   ![code-server 后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-consolegui-websoft9.png)

3. 在 code-server 界面上打开 workspace 文件夹  
   ![code-server 打开项目目录](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-openfolder-websoft9.png)
   > 默认存放代码的根目录为：*/data/wwwroot/codeserver/volumes/config/workspace*  

4. 打开 Terminal，查看系统环境（默认已安装 Node, Yarn等）
   ![code-server 打开Terminal](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-terminal-websoft9.png)

5. 参考[配置环境](/zh/solution-runtime.md)章节，安装更多开发所需的组件。

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## code-server 使用入门

下面以 Python 开发为范例，介绍如何使用 code-server：

1. 登录 code-server，在当前 WorkSpace 下克隆一个代码仓库
   ```
   git clone https://github.com/Websoft9/ansible-wordpress.git
   ```
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-gitclone-websoft9.png)

2. 在项目文件夹中新建一个文件，命名为：myfile.py，并拷贝下面的 Python 程序实例代码。
   ```
   #!/usr/bin/env python2
   #!/usr/bin/env python3
   #coding: utf-8

   import os, io, sys

   print("hello world")
   ```
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-createfile-websoft9.png)

3. 在【窗口的终端栏】中执行 `python myfile.py` 命令，运行 Python 程序
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-runpython-websoft9.png)

4. 查看正确的输出结果

> 需要了解更多 code-server 的使用，请参考官方文档：[code-server Documentation](https://hub.docker.com/r/linuxserver/code-server)

## 常用操作

### 安装组件

若默认环境不符合需求，可以直接通过 **code-server 控制台**安装组件，下面以 JAVA 为例进行说明：

1. 登录 code-server 控制台，在【Terminal】窗口中运行 `sudo su` 切换为 root 用户
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-sudosu-websoft9.png)
   > 密码为 code-server 控制台登录密码

2. 更新 apt 仓库
   ```
   apt update
   ```

3. 安装并验证 Java
   ```
   #1 安装JRE
   apt-get install openjdk-8-jre

   #2 验证版本
   java -version
   ```

### 备份环境

由于 code-server 基于容器运行，如果你打算将容器安装后的环境长期的备份下来，需要参考如下方式创建自定义容器镜像：

1. 登录服务器
2. 运行创建命令命令（基于 codeserver 容器创建一个名称为 codeserver-java 的镜像）
   ```
   #1 创建镜像
   sudo docker commit -m "add java" -a "your name" codeserver codeserver-java:latest

   #2 查看镜像
   sudo docker image ls
   ```

### 多开发者

当前部署方案默认只有一个 code-server，由于它并不支持多用户，所以不合适多开发协同工作的场景。  

那么如何才能支持多开发者协作使用 code-server 呢？从宏观上设计，需多开发者使用，每一名开发者分配如下资源即可实现此需求：

1. 单独分配一个宿主机的端口
2. 单独分配一个 code-server 目录
3. 单独运行一个 code-server 容器

下面是一个范例：

1. 运行下面的命令，将现有的 code-server 整个目录复制一份，命名为：/data/wwwroot/user1
   ```
   # 复制
   cd /data/wwwroot
   cp -r codeserver user1

   # 删除持久数据
   rm -rf user1/volumes
   ```

2. 修改 */data/wwwroot/user1/.env* 文件中的 APP_PORT、APP_PASSWORD、APP_CONTAINER_NAME，然后保存
   ```
   APP_PORT=9001
   APP_PASSWORD=123456
   APP_CONTAINER_NAME=codeserver
   ```
   > APP_PORT和APP_CONTAINER_NAME 必须与当前已经存在的 code-server 容器不同名称，否则无法创建


3. 启动新的 code-server 项目
   ```
   cd /data/wwwroot/user1
   sudo docker-compose  up -d
   ```

由于多用户协同开发有诸多个性化需求，无法在以上方案中一一列出，欢迎提出更多需求。

## 参数

**[通用参数表](../setup/parameter)** 中可查看 Nginx, MySQL, MongoDB, phpMyAdmin, adminMongo, Docker 等 code-server 应用中包含的基础架构组件路径、版本、端口等参数。 

通过运行`docker ps`，可以查看到 code-server 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

下面仅列出 code-server 本身的参数：

### 路径{#path}

code-server 日志目录： */data/wwwroot/codeserver/volumes/config/data/logs*  
code-server 工作目录： */data/wwwroot/codeserver/volumes/config/workspace*  
code-server Extension 目录： */data/wwwroot/codeserver/volumes/config/extensions*  


### 端口

无特殊端口


### 版本

```shell
docker inspect -f '{{ index .Config.Labels "build_version" }}' codeserver
```

### 服务

```shell
sudo docker start | stop | restart | stats codeserver
```

### 命令行

```
code-server -h
```

### API

无

