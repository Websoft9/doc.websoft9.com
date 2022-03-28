---
sidebar_position: 1
slug: /xwiki
tags:
  - XWiki
  - 知识管理
---

# 快速入门

[XWiki](https://www.xwiki.org/xwiki/bin/view/Main/WebHome)是一个使用Java编写的开源Wiki引擎，XWiki自称其为“第二代wiki”。它支持一些受欢迎的特性如：
- 内容管理（浏览／编辑／预览／保存）
- 支持附件
- 版本控制
- 全文本搜索
- 权限管理
- 使用Hibernate进行数据存储
- RSS输出与显示外部的RSS feeds
- 多语言支持
- 提供XML/RPC的API
- WYSIWYG HTML编辑器
- Groovy脚本支持等等


部署 Websoft9 提供的 XWiki 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 XWiki 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  XWiki **[域名五步设置](./dns#domain)** 过程


## XWiki 初始化向导

### 详细步骤

1. 本地浏览器访问：http://域名 或 http://公网IP 进入安装向导（镜像刚部署上去会出先 502的错误,是因为xwiki还未启动造成,等待几分钟即可）

2. xwiki初始化
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-initializing-websoft9.png)

3. 安装向导,点击 "Continue" 进入下一步
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-wizard-websoft9.png)

4. 设置管理员用户信息,填写信息后点击 " Register and login"
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-set-admin.png)

5. 确认注册安装xwiki,点击 "Continue" 进入下一步
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-admin-install-websoft9.png)

6. (**注意:此步骤不能跳过,否则无法使用**) 安装插件模块, 如果显示空白 ,等待十几秒,选择"XWiki Standard Flavor" 后点击 "Install this flavor" 进行安装
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-flavor1-websoft9.png)

7. 确认安装Flavor,点击 "Install" 进行安装
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-flavor2-websoft9.png)

8. 安装flavor
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-flavor3-websoft9.png)

9. flavor安装完成,点击 "Continue" 进入下一步
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-flavor4-websoft9.png)

10. xwiki 安装完成 ,点击 "Continue" 完成最后步骤
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-complete-websoft9.png)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

## XWiki 使用入门

下面以 **使用 XWiki 构建知识管理系统** 作为一个任务，帮助用户快速入门：


## XWiki 常用操作

### 配置 SMTP{#smtp}

### 配置域名{#dns}

参考： **[域名五步设置](./dns#domain)** 

### 配置 HTTPS{#https}

参考： **[HTTPS 配置](./dns#https)**

## 参数{#parameter}

**[通用参数表](../setup/parameter)** 中可查看 Nginx, Apache, Docker, MySQL 等 XWiki 应用中包含的基础架构组件路径、版本、端口等参数。 

通过运行`docker ps`，可以查看到 XWiki 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 XWiki 本身的参数：

### 路径{#path}

xwiki 配置文件目录: */etc/xwiki/*
xwiki 程序目录: */usr/lib/xwiki*
xwiki 相关插件/组件目录: */var/lib/xwiki*
xwiki 数据库配置文件: */etc/xwiki/hibernate.cfg.xml*

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 8080   | XWiki 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


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
