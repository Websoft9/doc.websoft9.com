---
sidebar_position: 1
slug: /canvas
tags:
  - Canvas
  - 在线学习管理
---

# 快速入门

[Canvas](https://www.instructure.com/canvas/) 是一个基于云端的开源在线学习系统（LMS），使学校能够构建数字学习环境，以应对远程教学趋势。Canvas简化了教学，提高了学习效率，并消除了支持和发展传统学习技术的麻烦。它具有开放，直观的特点，通过所有数字工具和内容，简化老师的教学，让学生获得更简单的互联网学习体验。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/canvas/canvas-gui-websoft9.png)

## 准备

部署 Websoft9 提供的 Canvas 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Canvas 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  Canvas **[域名五步设置](./administrator/domain_step)** 过程


## Canvas 初始化向导

### 详细步骤

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入登录页面
   ![canvas 登录](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](./user/credentials)），成功登录到 Canvas 后台  
   ![canvas 后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-console001-websoft9.png)

3. 依次打开：【管理员】>【设置】>【账户设置】设置语言  
   ![canvas 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-setlanguage-websoft9.png)

4. 依次打开：【账户】>【设置】>【编辑设置】修改默认邮件账户和密码
   ![canvas 修改账号](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-setaccount001-websoft9.png)
   ![canvas 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-setaccount002-websoft9.png)

5. 开放注册：【管理员】>【身份验证设置】>【提供者】开放教师和学生注册 
   ![canvas 开放注册](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-register-websoft9.png)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**Canvas 访问速度很慢？**

Canvas 对服务器的配置要求极高，最低配置为2核8G

## Canvas 使用入门

下面以 **使用 Canvas 构建学习管理系统** 作为一个任务，帮助用户快速入门：


## Canvas 常用操作

### 重置 Canvas 至初始状态

如果你忘记了 Canvas  管理员密码，又无法通过邮件找回密码，重置至 Canvas 初始状态。

使用 SSH 连接服务器，重置环境变量后开始初始化：

```
  export RAILS_ENV=production
  export CANVAS_LMS_ADMIN_EMAIL=help@websoft9.com
  export CANVAS_LMS_ADMIN_PASSWORD=websoft9
  export CANVAS_LMS_ACCOUNT_NAME=admin
  export CANVAS_LMS_STATS_COLLECTION=opt_in
  cd /data/wwwroot/canvas; bundle exec rake db:initial_setup
```

> 为防止初始化删除历史数据，建议先做备份

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数

2. 使用 SSH 登录服务器，修改[邮件配置文件](#path)文件后保存
   ```
   production:
   address: smtp.163.com
   port: 465
   user_name: websoft9@163.com
   password: #wwBJ8
   authentication: plain        # plain, login, or cram_md5
   domain: smtp.163.com
   outgoing_address: websoft9@163.com
   default_name: Instructure Canvas
   ```
   > 以上配置如果不能收到邮件，请尝试将 authentication 改为 login**

3. 给 Canvas [配置域名](./administrator/domain_step)，并确保可以访问

   > 配置域名很重要，否则即使收到邮件，里面的链接也无法打开。

4. 给 Canvas [配置 HTTPS 访问](./administrator/domain_https)（可选），否则打开邮件中的链接时会有安全提示

4. 重启 Apache 服务后生效
   ```
   sudo systemctl restart apache
   ```

> 很多用户反馈，Canvas部署在中国大陆之外（比如香港）区域，方可成功发出邮件。原因未知。


### Canvas 更换域名

如果 Canvas 需要更换域名，除[ Canvas 配置文件](#path)之外，还需修改 Canvas 根目录下 `.htaccess` 中域名有关的值。  


### Canvas 安装插件{#plugin}

通过BigBlueButton为例，步骤如下：

1. 登陆 Canvas 站点

2. 通过URL：*http://域名/plugins* 或 *http://服务器公网IP/plugins*, 进入插件选择页面
   ![canvas 插件](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-plugin01-websoft9.png)

3. 选择您要安装的插件，点击安装

4. 在插件安装页面，去掉勾选【禁用此插件】，输入相关引导信息，点击【申请】
   ![canvas 插件设置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-plugin02-websoft9.png)
   ![canvas 插件设置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-plugin03-websoft9.png)

5. 安装插件前后，页面已经发生变化（课程中追加了BigBlueButton对应的会议功能）
   ![canvas 插件安装前后对比](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-plugin04-websoft9.png)
   ![canvas 插件安装前后对比](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-plugin05-websoft9.png)

## 参数{#parameter}

Canvas 应用中包含 Ruby, Node.js, Apache, Passenger, Docker, Redis, PostgreSQL, PgAdmin 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 Canvas 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Canvas 本身的参数：

### 路径{#path}

Canvas 安装目录： */data/wwwroot/canvas*  
Canvas 日志目录： */data/wwwroot/canvas/log*  
Canvas 配置目录： */data/wwwroot/canvas/config*  
Canvas 域名配置文件：*/data/wwwroot/canvas/config/domain.yml*  
Canvas 域名配置文件：*/data/wwwroot/canvas/config/outgoing_mail.yml*  

### 端口{#port}

无特殊端口

### 版本{#version}

控制台查看

### 服务{#service}

```shell
# 通过 Apache 服务启停来管理 Canvas
sudo systemctl start | stop | restart | status apache

# Canvas Job
sudo systemctl start | stop | restart | status canvas-init
```

### 命令行{#cli}

Canvas 提供一序列脚本工具，脚本目录： `/data/wwwroot/canvas/script`  

Passenger 应用服务器提供了命令行工具 `passenger`  

### API

[Canvas API Documentation](https://community.canvaslms.com/t5/Academic-Benchmarks-Basics/API-Documentation-Overview/ta-p/474357)