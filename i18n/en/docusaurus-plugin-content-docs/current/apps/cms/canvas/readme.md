---
sidebar_position: 1
slug: /canvas
tags:
  - Canvas
  - elearning
---

# Canvas Getting Started

[Canvas](https://canvas-server.apache.org/) is the World's Fastest-Growing Learning Management Platform. Canvas streamlines all the digital tools and content that teachers and students love, for a simpler and more connected learning experience.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/canvas/canvas-gui-websoft9.png)  

If you have installed Websoft9 Canvas, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. [Get](./user/credentials) default username and password of Canvas
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Canvas.

## Canvas Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://DNS* or *http://Internet IP*, you can see login page
   ![canvas login page](https://libs.websoft9.com/Websoft9/DocsPicture/en/canvas/canvas-login-websoft9.png)

2. Log in to Canvas console([Don't have password?](./user/credentials))  
   ![canvas console](https://libs.websoft9.com/Websoft9/DocsPicture/en/canvas/canvas-console001-websoft9.png)

3. Open:【Admin】>【Settings】>【Account Settings】to set your language
   ![canvas set language](https://libs.websoft9.com/Websoft9/DocsPicture/en/canvas/canvas-setlanguage-websoft9.png)

4. Open:【Account】>【Settings】>【Edit Settings】 to modify the default email and password
   ![canvas edit setting](https://libs.websoft9.com/Websoft9/DocsPicture/en/canvas/canvas-setaccount001-websoft9.png)
   ![canvas modify password](https://libs.websoft9.com/Websoft9/DocsPicture/en/canvas/canvas-setaccount002-websoft9.png)

5. 开放注册：【管理员】>【身份验证设置】>【提供者】开放教师和学生注册 
   ![canvas 开放注册](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-register-websoft9.png)

> More useful Canvas guide, please refer to [Canvas Guides](https://community.canvaslms.com/community/answers/guides)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more. 

#### Canvas very slowly?

Canvas need very high configuration of Server, minimal: 2 vCPU and 8G memory

## Canvas QuickStart

下面以 **使用 Canvas 构建学习管理系统** 作为一个任务，帮助用户快速入门：

## Canvas Setup

### 重置 Canvas 至初始状态

**Init Canvas**

You may init Canvas if you can't recover your administrator password by email

Use SSH to connect Server, run the follow sample commands, you can recover your account and password to: `help@websoft9.com/websoft9`

```
export RAILS_ENV=production
export CANVAS_LMS_ADMIN_EMAIL=help@websoft9.com
export CANVAS_LMS_ADMIN_PASSWORD=websoft9
export CANVAS_LMS_ACCOUNT_NAME=admin
export CANVAS_LMS_STATS_COLLECTION=opt_in
cd /data/wwwroot/canvas; bundle exec rake db:initial_setup
```

> Init Canvas will delete all your history data in your database

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console  

2. Use SFTP or SSH to modify the email configuration file on your Server: */data/wwwroot/canvas/config/outgoing_mail.yml*
   ```
   production:
   address: smtp.sendgrid.net
   port: 465
   user_name: websoft9smpt
   password: #fdfwwBJ8f    
   authentication: plain        # plain, login, or cram_md5
   domain: smtp.sendgrid.net
   outgoing_address: sendgrid.net
   default_name: Instructure Canvas
   ```
   >  If you can't receive email, try to modify the item `authentication: plain` to `authentication: login` 

3. Complete the Canvas [Domain name configuration](./administrator/domain_step) and make sure it's successful

   > Domain is very important, if you don't configure Domain for Canvas, the links can't be opened in the email send to user. If you don't configure SSL for canvas, there may have security reminder when you click the links

4. Restart Apache service
   ```
   systemctl restart apache
   ```
   
### DNS Additional Configure（Modify URL）{#dns}

如果 Canvas 需要更换域名，除[ Canvas 配置文件](#path)之外，还需修改 Canvas 根目录下 `.htaccess` 中域名有关的值。  

### Install plugin{#installplugin}

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


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Canvas

通过运行`docker ps`，可以查看到 Canvas 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

### Path{#path}

Canvas installation directory: */data/wwwroot/canvas*  
Canvas logs directory: */data/wwwroot/canvas/log*  
Canvas configuration directory:  */data/wwwroot/canvas/config*  
Canvas 域名配置文件：*/data/wwwroot/canvas/config/domain.yml*  
Canvas 域名配置文件：*/data/wwwroot/canvas/config/outgoing_mail.yml*  

### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 80 | HTTP  to visit Canvas | Optional |
| 443 | HTTPS to visit Canvas  | Optional |
| 9090 | PostgreSQL web GUI tool | Optional |
| 5432 | PostgreSQL server | Optional |

### Version{#version}

控制台查看

### Service{#service}

```shell
# Canvas
sudo systemctl start | stop | restart | status apache

# Canvas Job
sudo systemctl start | stop | restart | status canvas-init
```

### CLI{#cli}

Canvas provide some useful scripts in the directory: `/data/wwwroot/canvas/script`  

Passenger cli: `passenger`    

### API

[Canvas API Documentation](https://community.canvaslms.com/t5/Academic-Benchmarks-Basics/API-Documentation-Overview/ta-p/474357)