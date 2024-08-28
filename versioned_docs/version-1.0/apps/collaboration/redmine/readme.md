---
sidebar_position: 1
slug: /redmine
tags:
  - Redmine
  - 项目管理
---

# 快速入门

[Redmine](https://www.redmine.org/) 是一个开源的项目管理软件，功能包括：项目管理、Wiki、新闻台等功能，集成版本管理系统 GIT、SVN、CVS 等工具。通过 Web 形式把成员、任务、文档、讨论以及各种形式的资源组织在一起，推动项目的进度。

![Redmine界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-gui-websoft9.jpg)

## 准备

部署 Websoft9 提供的 Redmine 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Redmine 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  Redmine **[域名五步设置](./administrator/domain_step)** 过程


## Redmine 初始化向导{#init}

### 详细步骤

1. 使用本地 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入Redmine主页。

2. 点击【登录】，进入系统（[不知道账号密码？](./user/credentials)）
   ![Redmine 密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-login-websoft9.png)

3. 进入 Redmine 控制台，系统提示修改密码 
   ![Redmine 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-resetpwf-websoft9.png)

4. 打开：【项目】，新建一个项目
   ![Redmine 新建项目](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-createproject-websoft9.png)

5. 通过：【管理】>【配置】>【显示】，设置 Redmine 项目区语言
   ![Redmine 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-language-websoft9.png)

6. 通过：【管理】>【配置】>【用户】，设置 Redmine 用户语言（区别于项目区语言）
   ![Redmine SSH key](https://libs.websoft9.com/Websoft9/DocsPicture/en/redmine/redmine-userlanguage-websoft9.png)
   
7. 激活新注册用户：通过【管理】>【用户】，在【状态】选项中选择 已注册用户，然后激活用户，该用户才能登陆。

> 需要了解更多 Redmine 的使用和配置，请参考官方文档：[Redmine guide](https://www.redmine.org/projects/redmine/wiki/Guide)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**Redmine能打开，但总是出现502错误**

Redmine 所需内存最低为2G，若服务器配置较低或并发访问超过服务器计算能力，会出现502错误

## Redmine 使用入门

下面以 **Redmine 管理项目** 作为一个任务，帮助用户快速入门：

1. 登录 Redmine，依次打开：【项目】>【创建项目】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-createproject001-websoft9.png)

2. 填写上面标题和英文缩写，保存
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-createproject002-websoft9.png)

3. 打开项目页面，开始工作
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-createproject003-websoft9.png)

4. [安装插件](#插件管理)，增加更多所需的功能

## Redmine 常用操作

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数

2. 通过 SFTP 连接服务器，修改 `configuration.yml` 文件，找到 “production:”, 在 production 下面添加并完善你的 SMTP 参数:  
   ```
   production:
   delivery_method: :smtp
   smtp_settings:
      address: smtp.exmail.qq.com
      port: 465
      ssl: true
      enable_starttls_auto: true
      domain: websoft9.com
      authentication: :login
      user_name: help@websoft9.com
      password: ********

   ```
    > 注意缩进/空格,按照规定格式配置，否则Redmine报错

3. 重启 Redmine 服务后生效
   ```
   sudo docker restart redmine
   ```

4. 配置系统主机：【管理】-【配置】-【一般】-【主机名称】

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-sethost-websoft9.png)

5. 配置系统邮件发件人地址：【管理】-【配置】-【邮件通知】-【邮件发件人地址】,保存，点击最下方“发送测试邮件”进行测试
   
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-smtp-websoft9.png)

Redmine 官方提供了数十种不同 SMTP 配置方法，请参考官方文档： [Email Configuration](https://www.redmine.org/projects/redmine/wiki/EmailConfiguration)

### 插件管理

通过 Redmine 提供的[插件中心](https://www.redmine.org/plugins)可以扩展它的功能：

**安装插件**

下面以一个具体的插件为例说明如何安装插件：  

1. 进入[Ajax Redmine Issue Dynamic Edit](https://www.redmine.org/plugins/redmine_issue_dynamic_edit) 插件页面，获取其下载地址

2. 使用 SFTP 登录服务，分别运行如下命令
   ```
   # 进入 Redmine 目录
   cd /data/wwwroot/redmine
   wget https://www.redmine.org/attachments/download/25386/redmine_issue_dynamic_edit.zip
   unzip redmine_issue_dynamic_edit.zip 
   docker cp redmine_issue_dynamic_edit redmine:/usr/src/redmine/plugins
   ```

3. 重启 Redmine 容器服务
   ```
   sudo docker restart redmine
   ```
   
4. 登陆 Redmine 控制台查看插件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-installplugindy-websoft9.png)

**卸载插件**

1. 使用 SFTP 删除 /data/wwwroot/redmine/plugins 对应的插件
2. 重启 Redmine 容器生效
   ```
   sudo docker restart redmine
   ```

### LDAP

参考官方文档：https://www.redmine.org/projects/redmine/wiki/RedmineLDAP



## Redmine 参数{#parameter}

Redmine 应用中包含 Nginx, Docker, MySQL, phpMyAdmin 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。  

通过运行`docker ps`，可以查看到 Redmine 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE               COMMAND                  CREATED          STATUS          PORTS                                                  NAMES
635cd1609242   phpmyadmin:latest   "/docker-entrypoint.…"   21 minutes ago   Up 21 minutes   0.0.0.0:9090->80/tcp, :::9090->80/tcp                  phpmyadmin
bcd0b75f04d7   redmine:4.2         "bash -c 'cat /my_cm…"   21 minutes ago   Up 21 minutes   0.0.0.0:9001->3000/tcp, :::9001->3000/tcp              redmine
b171c341fa90   mysql:5.7           "docker-entrypoint.s…"   21 minutes ago   Up 21 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   redmine-db
```

### 路径{#path}

Redmine 安装目录：*/data/apps/redmine*  
Redmine 站点目录：*/data/apps/redmine/data/redmine*  
Redmine 配置目录：*/data/apps/redmine/data/redmine/config*  
Redmine 配置文件：*/data/apps/redmine/data/redmine/config/configuration.yml*  

> configuration.yml 是容器首次启动时基于 configuration.yml.example 而创建的

### 端口{#port}

无特殊端口

### 版本{#version}

```shell
docker inspect redmine:latest |grep REDMINE_VERSION |head -1 |cut -d= -f2
```

### 服务{#service}

```shell
sudo docker start | stop | restart redmine
sudo docker start | stop | restart redmine-db
sudo docker start | stop | restart phpmyadmin
```

### 命令行{#cli}

[Redmine-CLI](https://pypi.org/project/Redmine-CLI/)

### API

[Redmine API](https://www.redmine.org/projects/redmine/wiki/Rest_api)
