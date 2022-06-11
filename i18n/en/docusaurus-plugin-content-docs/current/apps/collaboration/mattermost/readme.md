---
sidebar_position: 1
slug: /mattermost
tags:
  - Mattermost
  - 团队协作
  - 团队通讯
---

# Mattermost Getting Started

[Mattermost](https://mattermost.com/) is an open source, self-hosted Slack-alternative. As an alternative to proprietary SaaS messaging, Mattermost brings all your team communication into one place, making it searchable and accessible anywhere.

![](https://ucarecdn.com/8cd90d9d-8902-4845-a15b-f4664e5fcfb3/-/format/auto/-/quality/lighter/-/max_icc_size/10/-/resize/1288x/)

If you have installed Websoft9 Mattermost, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Mattermost
4. [Get](./user/credentials) default username and password of Mattermost


## Mattermost Initialization{#init}

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://domain name* or *http://Internet IP*, you will enter the register interface of Mattermost
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-install-websoft9.png)
2. Set the username and password, start to create administrator account of Mattermost
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-createdaccount-websoft9.png)
3. Create a new team or Go to system console
4. Open **Settings** > **Display** to set your language
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-display-websoft9.png)
5. Quit and reload Mattermost, you can see your language is in effect

> More useful Mattermost guide, please refer to [Matterbase Administrator’s Guide](https://docs.mattermost.com/guides/administrator.html)


### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  


## Mattermost QuickStart


## Mattermost Setup

### 增加团队用户数

系统控制台 【SITE CONFIGURATION】>【Users and Teams】> 【Max Users Per Team】值来设置团队人数：
![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-maxusers-websoft9.png)

### Domain Binding（Modify URL）{#dns}

**[Domain name five-step setting](./administrator/domain_step)** After completion, you need to set the URL of Mattermost:

Log in Mattermost console, open: **ENVIRONMENT** > **Web Server**, modify **Site URL** value
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-urlset-websoft9.png)


### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Log in Mattermost Console, open **ENVIROMENT** > **SMTP**
   ![Set smtp](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-smtpsendgrid-websoft9.png)

3. Enter the SMTP settings
   
4. Click the **Test Connection**, you can get the feedback *"no errors were..."* if SMTP is useful

### 安装插件

例如，jitmi被用户大量使用。

### 语言设置{#setlang}

支持多语言（包含中文），可以登录控制台，通过【SITE CONFIGURATION】>【Localization】设置语言 

## Reference sheet{#parameter}

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Mattermost


通过运行`docker ps`，可以查看到 Mattermost 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Mattermost 本身的参数：

### Path{#path}

Mattermost installation directory： */opt/mattermost/*  
Mattermost 配置文件： */opt/mattermost/config/config.json*  
Mattermost 数据目录： */opt/mattermost/data*  
Mattermost 日志目录： */opt/mattermost/logs*

> config.json 包含数据库连接信息

### Port{#port}

无特殊端口

### Version{#version}

```shell
# mattermost version
cd /opt/mattermost/bin
./mattermost version
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats mattermost
```

### CLI{#cli}

Mattermost 提供了 `mattermost` 和 `mmctl` 两种命令，[mattermost](https://docs.mattermost.com/administration/command-line-tools.html)是服务器端命令，[mmctl](https://docs.mattermost.com/administration/mmctl-cli-tool.html)基于API的客户端命令
 
```
/opt/mattermost/bin/mattermost -h
/opt/mattermost/bin/mmctl -h
```

如果运行 /opt/mattermost/bin/mmctl version 查询出的版本稍微低一点

### API

[Mattermost API Reference](https://api.mattermost.com/)