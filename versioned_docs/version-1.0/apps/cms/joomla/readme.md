---
sidebar_position: 1
slug: /joomla
tags:
  - Joomla
  - CMS
---

# 快速入门

[Joomla](https://joomla.org) 是一个 100% 开源的老牌建站系统（CMS），它占据全球 6% 的 CMS 市场。它拥有良好的社区，提供超过 6,500 个经过验证的扩展和高质量模板。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-gui-websoft9.jpg)

## 准备

部署 Websoft9 提供的 Joomla 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Joomla 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  Joomla **[域名五步设置](./administrator/domain_step)** 过程


## Joomla 初始化向导

### 详细步骤

1. 使用浏览器访问网址：*http://域名/administrator* 或 *http://服务器公网IP/administrator*, 就进入登陆页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-install1-websoft9.png)

2. 输入用户名和密码（[不知道账号密码？](./user/credentials)），成功登陆后您可以开始使用Joomla
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-install2-websoft9.png)

3. 使用浏览器访问网址：*http://域名* 或 *http://服务器公网IP*，可以体验前端页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-install3-websoft9.png)

> 需要了解更多 Joomla 的使用，请参考官方文档：[Joomla Docs](https://docs.joomla.org/Main_Page/zh-cn)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**Joomla 不是最新版本**

完成 Joomla 初始化安装后，登录后台可以一键在线更新至最新版本

## Joomla 使用入门

下面以 **使用 Joomla 构建内容管理系统** 作为一个任务，帮助用户快速入门：


## Joomla 常用操作

### Joomla 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数

2. 登录 Joomla 后，打开：【系统管理】>【全局设置】>【服务器设置】，服务器邮件类型选择：SMTP
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-opensmtp-websoft9.png)

3. 填写准确的 SMTP 设置项信息
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-smtpsettings-websoft9.png)

    * 发送模式选择“SMTP”，加密方式选择“SSL/TLS”;
    * 输入发送方邮箱地址；
    * 认证方式选择“登录”，并勾选“需要认证”选项；
    * 输入SMTP服务器地址和SMTP服务器的端口号；
    * 输入和发件人邮箱一致的邮箱地址；
    * 输入该邮箱地址的SMTP服务的授权码或密码；
    * 存储凭据；

4. 设置完成后，点击【发送测试邮件】，测试可用性
     
### Joomla 多语言{#setlang}

Joomla 支持多语言，下面是安装并设置多语言的主要步骤：

1. 登录 Joomla，在后台 【扩展管理】>【语言管理】中安装语言
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkinstalllan-websoft9.png)

2. 然后设置前后台的默认语言
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkenablelang-websoft9.png)

### Joomla 扩展{#plugin}

Joomla 后台集成了 [Joomla! Extensions Directory™](https://extensions.joomla.org/) 大量的扩展，下面介绍如何安装它们

1. 登录 Joomla
2. 打开【扩展管理】>【安装扩展】，建议选择【从扩展目录安装】的方式在线寻找扩展
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkinstallext-websoft9.png)
3. 安装你所需的扩展

### Joomla 安装模板{#template}

Joomla 的模板安装，主要通过上传模板安装包的方式实现：

1. 准备好你的模板安装包（一般是 .zip 文件）

2. 登录 Joomla 后台

3. 打开 【扩展管理】>【安装扩展】，选择【上传安装包文件】的方式上传你的模板，开始安装
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkuploadext-websoft9.png)

4. 安装后，打开【扩展管理】>【模板管理】>【风格管理】，找到已经安装的模板，启用它
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkenabletemplate-websoft9.png)

> 有些模板提供商，提供的模板压缩包中包含 Joomla 内核文件，这种情况下 **安装模板=安装Joomla**

### Joomla Cache

Joomla 后台提供了缓存管理功能，参考下图：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-cache-websoft9.png)

### Joomla 重置密码{#setpwd}

如果忘记了管理员密码，可以参考 [此处](https://docs.joomla.org/How_do_you_recover_or_reset_your_admin_password%3F/zh-cn) 重置密码


## Joomla 参数{#parameter}

Joomla 应用中包含 Nginx, Docker, MySQL, phpmyadmin 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行`docker ps`，可以查看到 Joomla 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE               COMMAND                  CREATED             STATUS             PORTS                                                 NAMES
d25075df271f   phpmyadmin:latest   "/docker-entrypoint.…"   About an hour ago   Up About an hour   0.0.0.0:9090->80/tcp, :::9090->80/tcp                 phpmyadmin
5c64467e167f   bitnami/joomla:4    "/opt/bitnami/script…"   About an hour ago   Up About an hour   8443/tcp, 0.0.0.0:9001->8080/tcp, :::9001->8080/tcp   joomla
9a027cdd4220   mariadb:10.6        "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp             joomla-db
```

### 路径{#path}

Joomla 安装目录： */data/apps/joomla*  
Joomla 站点目录： */data/apps/joomla/data/joomla*  
Joomla 配置文件: */data/apps/joomla/data/joomla/configuration.php*   


### 端口{#port}

无特殊端口


### 版本{#version}

```shell
sudo docker exec -i joomla cat /bitnami/joomla/language/en-GB/install.xml |grep "<version>"
```

### 服务{#service}

```shell
sudo docker start | stop | restart | stats joomla
sudo docker start | stop | restart | stats joomla-db
sudo docker start | stop | restart | stats phpmyadmin
```

### 命令行{#cli}

无

### API

[Joomla! API Documentation](https://api.joomla.org/)
