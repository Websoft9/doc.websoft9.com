---
sidebar_position: 1
slug: /mattermost
tags:
  - Mattermost
  - 团队协作
  - 团队通讯
---

# 快速入门

[Mattermost](https://mattermost.com/) 是一个 Slack 的开源替代品，用于跨团队和工具的安全通信、协作和工作编排。它为团队带来跨 PC 和移动设备的消息、文件分享、应用程序集成以及归档和搜索功能。

![](https://ucarecdn.com/8cd90d9d-8902-4845-a15b-f4664e5fcfb3/-/format/auto/-/quality/lighter/-/max_icc_size/10/-/resize/1288x/)

## 准备

部署 Websoft9 提供的 Mattermost 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Mattermost 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  Mattermost **[域名五步设置](./administrator/domain_step)** 过程

## Mattermost 初始化向导{#init}

### 详细步骤

1. 本地电脑的 Chrome 或 Firefox 浏览器访问网址：`http://域名` 或 `http://服务器公网IP`, 进入引导页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-install-websoft9.png)

2. 设置后台管理员账号和密码，开始创建账号
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-createdaccount-websoft9.png)

3. 开始创建团队 或 登录到系统控制台

4. 打开：【Settings】>【Display】设置你所需的语言
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-display-websoft9.png)

5. 退出并重新登录，所选语言生效

> 需要了解更多 Mattermost 的使用，请参考官方文档：[Matterbase Administrator’s Guide](https://docs.mattermost.com/guides/administrator.html)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：



## Mattermost 使用入门

下面以 **Mattermost 构建协作系统** 作为一个任务，帮助用户快速入门：


## Mattermost 常用操作

### 增加团队用户数

系统控制台 【SITE CONFIGURATION】>【Users and Teams】> 【Max Users Per Team】值来设置团队人数：
![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-maxusers-websoft9.png)

### 域名额外配置（修改 URL）{#dns}

**[域名五步设置](./administrator/domain_step)** 完成后，需设置 Mattermost 的 URL:

登录Mattermost控制台，打开：【ENVIRONMENT】>【Web Server】，修改 【Site URL】值  
![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-urlset-websoft9.png)

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数

2. 登录 Mattermost控制台，打开【ENVIROMENT】>【SMTP】
   ![设置smtp](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-smtp-websoft9.png)

3. 填写 SMTP 参数

4. 点击【Test Connection】

### 安装插件

例如，jitmi被用户大量使用。

### 语言设置{#setlang}

支持多语言（包含中文），可以登录控制台，通过【SITE CONFIGURATION】>【Localization】设置语言 

## Mattermost 参数{#parameter}

Mattermost 应用中包含 Nginx, Docker, MySQL 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 Mattermost 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Mattermost 本身的参数：

### 路径{#path}

Mattermost 安装目录： */opt/mattermost/*  
Mattermost 配置文件： */opt/mattermost/config/config.json*  
Mattermost 数据目录： */opt/mattermost/data*  
Mattermost 日志目录： */opt/mattermost/logs*

> config.json 包含数据库连接信息

### 端口{#port}

无特殊端口

### 版本{#version}

```shell
# mattermost version
cd /opt/mattermost/bin
./mattermost version
```

### 服务{#service}

```shell
sudo docker start | stop | restart | stats mattermost
```

### 命令行{#cli}

Mattermost 提供了 `mattermost` 和 `mmctl` 两种命令，[mattermost](https://docs.mattermost.com/administration/command-line-tools.html)是服务器端命令，[mmctl](https://docs.mattermost.com/administration/mmctl-cli-tool.html)基于API的客户端命令
 
```
/opt/mattermost/bin/mattermost -h
/opt/mattermost/bin/mmctl -h
```

如果运行 /opt/mattermost/bin/mmctl version 查询出的版本稍微低一点

### API

[Mattermost API Reference](https://api.mattermost.com/)