---
sidebar_position: 1
slug: /xwiki
tags:
  - XWiki
  - 知识管理
---

# 快速入门

[XWiki](https://www.xwiki.org/xwiki/bin/view/Main/WebHome) 是一个 100% 开源的企业级 Wiki 系统，超过 600 个扩展：应用程序、宏、皮肤、插件、主题等。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-gui-websoft9.png)

## 准备

部署 Websoft9 提供的 XWiki 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 XWiki 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  XWiki **[域名五步设置](./administrator/domain_step)** 过程


## XWiki 初始化向导

### 详细步骤

1. 本地浏览器访问：http://域名 或 http://公网IP 进入安装向导

2. Xwiki 开始初始化，耐心等待  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-initializing-websoft9.png)

3. 正式进入【安装向导】，点击【Continue】进入下一步
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-wizard-websoft9.png)

4. 设置管理员用户信息，牢记账号密码
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-set-admin.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-admin-install-websoft9.png)

5. 安装可选的预制模板之一（标准版和演示版），**此步骤不能跳过,否则无法使用**
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-flavor1-websoft9.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-flavor2-websoft9.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-flavor3-websoft9.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-flavor4-websoft9.png)

10. 预制模板安装完成后，点击【Continue】完成最后步骤
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-complete-websoft9.png)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**访问出现 502 错误？**  

主要原因是 XWiki 还未启动造成，需等待 1-2分钟再试。

## XWiki 使用入门

下面以 **使用 XWiki 构建知识管理系统** 作为一个任务，帮助用户快速入门：


## XWiki 常用操作

## 参数{#parameter}

XWiki 应用中包含 Java, Nginx, Solr, Tomcat, Docker, MySQL 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。

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


### 服务{#service}

```shell
```

### 命令行{#cli}

### API