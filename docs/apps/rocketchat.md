---
title: Rocket.Chat
slug: /rocketchat
tags:
  - Rocket.Chat
  - 团队协作
  - 团队通讯
---

import Meta from './_include/rocketchat.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Rocket.Chat 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 使用本地电脑浏览器访问, 进入初始化页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-wizard-websoft9.png)

2. 根据向导提示，输入组织名称，用户名，密码等关键信息，完成初始配置 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-set-websoft9.png)

3. 点击【转到您的工作区】，您就可以使用在线聊天功能   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-startchat-websoft9.png)

4. 后台进入管理-添加用户，管理员可以从后台追加用户（亦或用户自行注册）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-adduser-websoft9.png) 

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-register-websoft9.png)   

## 管理维护{#administrator}

### 配置 SMTP{#smtp}

1. 登录 Rocket.Chat 控制台，依次打开：【管理】>【设置】>【电子邮箱】>【SMTP】项，填写 SMTP 参数
   ![Rocket Chat SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-smtp-websoft9.png)

2. 点击【向我自己发送邮件测试】

### 重置管理员密码{#resetpw}

exec 到容器，运行命令 `rocketchatctl change_password  admin newpassword` 即可

### CLI 和 API

- [RocketChatCTL](https://docs.rocket.chat/quick-start/installing-and-updating/rapid-deployment-methods/rocketchatctl)
- [Rocket.Chat API](https://developer.rocket.chat/reference/api)

### 升级

参考： [官方文档](https://docs.rocket.chat/quick-start/upgrading-rocket.chat)

## 故障