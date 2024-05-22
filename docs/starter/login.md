---
sidebar_position: 0.1
slug: /login-console
---

# 登录 Websoft9 控制台

安装 Websoft9 服务器后，接下来的事情便是登录 Websoft9 控制台

## 准备

在使用应用之前，需要做好如下准备工作：

- 服务器的安全组入方向开放端口

   - 必要端口：80, 443, 22, 9000
   - 可选端口：9001-9999

- 获取服务器的 [账号密码](./credentials)（Websoft9 与服务器共享账号）
- 解析一个[域名](./guide/appsetdomain)到服务器（建议）

## 登录

登录 Websoft9 不需要额外的特别设置，只需要从**本地浏览器**访问服务器对应的端口即可：  

1. 本地浏览器访问： `http://服务器公网IP:9000`，即 Websoft9 登录界面
   ![Websoft9 登录界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-loginpage.png)

2. 输入服务器的[账号与密码](./credentials)，登录成功后进入控制台概述页面

   - 用户名：服务器的管理员账号，建议首次使用 `root`
   - 密码：服务器的管理员密码

   ![](./assets/websoft9-console-index.png)

3. 点击 "应用商店"，查看可安装的所有应用模板
   ![](./assets/websoft9-appstore.png)

4. 点击 "我的应用"，查看已安装的应用列表
   ![](./assets/websoft9-myapps.png)

## 相关主题

- 绑定域名
- 管理应用
- 数据库
- 设置应用的访问