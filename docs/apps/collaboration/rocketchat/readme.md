---
sidebar_position: 1
slug: /rocketchat
tags:
  - Rocket.Chat
  - 团队协作
  - 团队通讯
---

# 快速入门

[Rocket.Chat](https://rocket.chat/) 是一个类似 Slack 的交流平台，可以将外部客户，团队和其他生态相关者聚集到自定义的交流平台中。自2015年面世以来，迅速成长为出色的开源项目之一。目前，Rocket.Chat广泛应用在银行，非政府组织，初创企业和政府组织。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-gui-websoft9.png)

## 准备

部署 Websoft9 提供的 Rocket.Chat 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:3000** 端口已经开启
3. 在服务器中查看 Rocket.Chat 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  Rocket.Chat **[域名五步设置](./administrator/domain_step)** 过程


## Rocket.Chat 初始化向导{#init}

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名:3000* 或 *http://服务器公网IP:3000*, 进入初始化页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-wizard-websoft9.png)

2. 根据向导提示，输入组织名称，用户名，密码等关键信息，完成初始配置 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-set-websoft9.png)

3. 点击【转到您的工作区】，您就可以使用在线聊天功能   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-startchat-websoft9.png)

4. 后台进入管理-添加用户，管理员可以从后台追加用户（亦或用户自行注册）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-adduser-websoft9.png) 

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-register-websoft9.png)   

> 需要了解更多 Rocket.Chat 的使用，请参考官方文档：[Rocket.Chat Documentation](https://docs.rocket.chat/guides/user-guides)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：


## Rocket.Chat 使用入门

下面以 **Rocket.Chat 构建协作系统** 作为一个任务，帮助用户快速入门：


## Rocket.Chat 常用操作

### 配置 SMTP{#smtp}

1. 邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数

2. 登录 Rocket.Chat 控制台

3. 依次打开：【管理】>【设置】>【电子邮箱】>【SMTP】项，填写 SMTP 参数
   ![Rocket Chat SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-smtp-websoft9.png)

4. 点击【向我自己发送邮件测试】

### 重置密码

运行命令 `rocketchatctl change_password  admin newpassword` 即可

## 参数{#parameter}

Rocket.Chat 应用中包含 Nginx, Docker, MongoDB 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 Rocket.Chat 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Rocket.Chat 本身的参数：

### 路径{#path}

Rocket.Chat 安装目录： */data/wwwroot/rocketchat*  
Rocket.Chat 日志目录： */data/logs/nginx*  

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 3000   | 通过 HTTP 访问 Rocket.Chat | 可选   |


### 版本{#version}

```shell
curl  localhost/api/info
```

### 服务{#service}

```shell
sudo docker start | stop | restart | stats rocketchat
```

### 命令行{#cli}

[RocketChatCTL](https://docs.rocket.chat/quick-start/installing-and-updating/rapid-deployment-methods/rocketchatctl)

### API

[Rocket.Chat API](https://developer.rocket.chat/reference/api)

