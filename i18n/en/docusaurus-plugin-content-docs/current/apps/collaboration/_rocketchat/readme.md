---
sidebar_position: 1
slug: /rocketchat
tags:
  - Rocket.Chat
  - 团队协作
  - 团队通讯
---

# Rocket.Chat Getting Started

[Rocket.Chat](https://rocket.chat) is the most widely deployed open source message broker. Rocket.Chat is more than your average company, is the leading open source team chat community. When you choose Rocket.Chat, you become part of a global community comprised of a core team, hundreds of open source developers, testers and writers, and millions of users..

As an open-source platform, Rocket.Chat provides the architecture for uniting all communications in a single place, regardless of the user’s device or the diverse messaging services they are using. By leveraging the collective brainpower of their user base through open source, Rocket.Chat is the only platform capable of rapidly evolving alongside its users’ needs.


If you have installed Websoft9 Jenkins, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:3000** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Rocket.Chat
4. [Get](./user/credentials) default username and password of Rocket.Chat


## Rocket.Chat Initialization{#init}

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://DNS* or *http://Internet IP*, you will enter installation wizard of Rocket.Chat
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/rocketchat/rocketchat-wizard-websoft9.png)

2. According to the wizard prompts, enter the organization name, user name, password and other key information to complete the initial configuration  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/rocketchat/rocketchat-set-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/rocketchat/rocketchat-setok-websoft9.png)

3. Click [go to your workspace] and you can use the online Rocket.chat
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/rocketchat/rocketchat-startchat-websoft9.png)

4. Adminstrator access Rocket.Chat-add users, can add users from the background
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/rocketchat/rocketchat-adduser-websoft9.png) 

5. Visit the URL*http://域名* 或 *http://Internet IP*, you can also apply for registration
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/rocketchat/rocketchat-register-websoft9.png) 
   
> More useful Rocket.Chat guide, please refer to [Rocket.Chat Documentation](https://docs.rocket.chat/guides/user-guides)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  


## Rocket.Chat QuickStart

下面以 **Rocket.Chat 构建协作系统** 作为一个任务，帮助用户快速入门：


## Rocket.Chat Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Log in Rocket.Chat Console

3. Open【Administrator】>【Settings】>【Email】>【SMTP】, set it
   ![Rocket Chat SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/rocketchat/rocketchat-smtp-websoft9.png)

4. Click the **Send a test mail to my user**

### Reset Password

Run the command `rocketchatctl change_password admin newpassword`

## Reference sheet{#parameter}

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Rocket.Chat


通过运行`docker ps`，可以查看到 Rocket.Chat 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Rocket.Chat 本身的参数：

### Path{#path}

Rocket.Chat installation directory： */data/wwwroot/rocketchat*  
Rocket.Chat 日志目录： */data/logs/nginx*  

### Port{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 3000   | 通过 HTTP 访问 Rocket.Chat | 可选   |


### Version{#version}

```shell
curl  localhost/api/info
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats rocketchat
```

### CLI{#cli}

[RocketChatCTL](https://docs.rocket.chat/quick-start/installing-and-updating/rapid-deployment-methods/rocketchatctl)

### API

[Rocket.Chat API](https://developer.rocket.chat/reference/api)

