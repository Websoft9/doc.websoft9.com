---
sidebar_position: 1
slug: /seafile
tags:
  - Seafile
  - 网盘
  - 知识管理
  - 团队协作
---

# 快速入门

[Seafile](https://www.seafile.com/home/) 是一款开源的企业云盘，注重可靠性和性能。支持 Windows, Mac, Linux, iOS, Android 平台。支持文件同步或者直接挂载到本地访问。私有云盘产品 Seafile 起源于创始人清华实验室时期，历经6年的打磨，已发展成为一个国际化的开源项目，在 GitHub 上的项目有超过4500人关注，在国内开源社区开源中国上面也赢得了很多赞誉。

![Seafile界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-gui-websoft9.png)

## 准备

部署 Websoft9 提供的 Seafile 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 和 **TCP:9002**  端口已经开启
3. 在服务器中查看 Seafile 的 **[默认账号和密码](./setup/credentials)**  
4. 若想用域名访问  Seafile **[域名五步设置](./administrator/domain_step)** 过程


## Seafile 初始化向导{#init}

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入Seafile 登录页面
   ![Seafile登录页面](http://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-login-websoft9.png)

2. 输入用户名和密码[（查看）](./setup/credentials)，登录到Seafile后台管理界面
   ![Seafile后台界面](http://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-bk-websoft9.png)

3. 设置（检查） Seafile 的真实主机地址（**必选项，否则无法使用文件上传功能**）

   - SERVICE_URL：*http://服务器公网IP*
   - FILE_SERVER_ROOT：*http://服务器公网IP/seafhttp*

   ![Seafile后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-seturl-websoft9.png)

4. 开始使用 Seafile 全面友好的功能吧

5. [导入](#importlicense)授权文件 (仅 Seafile 企业版需要)

> 需要了解更多Seafile的使用，请参考：[《Seafile 用户手册》](https://cloud.seafile.com/published/seafile-user-manual/home.md) 和 [《Seafile 服务器手册》](https://cloud.seafile.com/published/seafile-manual-cn/home.md)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**Seafile 是否支持在线文档编辑与预览？**

镜像预装了 OnlyOffice Docs，可以通过配置实现在线文档编辑与预览，[参考](./seafile/solution#onlyoffice)


## Seafile 使用入门


下面以 **Seafile 构建企业网盘系统** 作为一个任务，帮助用户快速入门：

## Seafile 常用操作

### 添加文件

下面我们介绍 Seafile 如何添加和编辑文件：

1. 登录到 Seafile 后，添加资料库，然后添加文件

   ![Seafile添加资料库](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-addlib-websoft9.png)

   ![Seafile添加文件](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-addfile-websoft9.png)

2. 在线编辑文件（通过内置的 OnlyOffice Docs 服务实现）

   ![Seafile编辑文件](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-editfile1-websoft9.png)

### 用户管理

下面我们介绍 Seafile 如何创建用户和群组：

1. 打开右上角用户图标，进入【系统管理】，分别添加【用户】和【群组】

   ![Seafile进入系统管理](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-system-websoft9.png)

   ![Seafile添加用户](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-adduser-websoft9.png)

   ![Seafile添加群组](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-addgroup-websoft9.png)

2. 设置所创建的用户所归属群组

   ![Seafile用户分组](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-addusertogroup-websoft9.png)

### 文件共享

下面我们介绍 Seafile 如何给另外一个用户共享自己的文件：

1. 进入【我的资料库】，将资料库共享给指定用户，

   ![Seafile文件共享](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-sharefile1-websoft9.png)


2. 设定权限为【可写】或【只读】

   ![Seafile文件共享](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-sharefile-websoft9.png)

   > 在选择用户时，需输入用户名，系统自动查找匹配

### 读写共享文件

下面我们演示 Seafile 用户如何读写其他人共享过来的文件：

1. 切换user1用户登录，使用邮箱地址【user1@websoft9】作为登录名
   ![Seafile登录页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-login1-websoft9.png)

2. 查看共享文件，进入 OnlyOffice 进行编辑，保存文档
   ![Seafile查看共享文件](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-viewsharefile-websoft9.png)
   ![Seafile编辑共享文件](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-editfile-websoft9.png)

3. 切换到管理员账号 `me@example.com`，查看共享文件的版本变更信息
   ![查看共享文件版本信息](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-viewfileinfo1-websoft9.png)
   ![查看共享文件版本信息](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-viewfileinfo-websoft9.png)


### 导入企业版 License{#importlicense}

如果您已经向 Seafile 软件商购买了专业版，官方会向您提供授权文件 seafile-license.txt。

通过下面的命令，拷贝授权至 Seafile，即可完成授权文件的安装:

```bash
cp seafile-license.txt /data/wwwroot/seafile/seafile-data/seafile/
docker restart seafile
```

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数
   
2. 使用 SFTP 连接服务器，编辑 Seafile 配置文件 [seahub_settings.py](#path)，插入邮箱配置段
   ```
   EMAIL_USE_SSL = True
   EMAIL_HOST = 'smtp.163.com'
   EMAIL_HOST_USER = 'websoft9@163.com'
   EMAIL_HOST_PASSWORD = 'Auth_Code'  //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   EMAIL_PORT = '465'
   DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
   SERVER_EMAIL = EMAIL_HOST_USER
   ```
   参考官方文档：[发送邮件提醒](https://manual-cn-origin.seafile.com/config/sending_email)

3. 重启 Seafile 容器服务
   ```
   sudo docker restart seafile
   ```

### 修改邮件通知签名

在[邮件模板](https://manual-cn-origin.seafile.com/config/customize_email_notifications)文件中 "Seafile 团队" 实际上对应后台的【site_name】字段。所以，如果想将邮件通知中默认签名 "Seafile 团队" 修改成自己的签名，方案如下：

登录到 Seafile 修改网站名称即可：
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-sitename-email-websoft9.png)

### Seafile 文档预览与编辑

参考：[Seafile 连接 ONLYOFFICE docs](./seafile/solution#onlyoffice)


### 域名额外配置（修改 URL）{#dns}

**[域名五步设置](./administrator/domain_step)** 完成后，需设置 Seafile 的 URL:

1. 使用 SFTP 登录云服务器，修改 [Docker-compose 配置文件](#path)，将其中的 **SEAFILE_SERVER_HOSTNAME** 项的值为你的域名
   
   ```text
    - SEAFILE_SERVER_HOSTNAME=seafile.example.com  # Specifies your host name.
   ```
2. 保存配置文件，重启 [Seafile 服务](#service)

### 配置 HTTPS{#https}

下面是对 Seafile 官方文档：[向Let's encrypt申请SSL证书](https://manual-cn-origin.seafile.com/deploy/deploy_with_docker#xiang-lets-encrypt-shen-qing-ssl-zheng-shu) 的实践解读，验证可用：

**前置条件**

1. 在云控制台开启 **TCP:443** 端口
2. 完成域名解析，确保 Seafile 可以通过域名访问
3. 登录 Seafile 后台，修改主机地址
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-seturl-websoft9.png)

**基本设置**

Seafile 默认支持 [Let's Encrypt](https://letsencrypt.org/) 免费证书自动部署方案，只需如下几步设置：

1. 使用 SFTP 连接服务器，编辑 [docker-compose 配置文件](/维护参考.md#docker-compose)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-editconfig-websoft9.png)

2. 修改（检查）配置文件并保存，确保三个核心参数符合如下要求
   ```
   - "443:443" 启用
   - SEAFILE_SERVER_LETSENCRYPT 设置为 true
   - SEAFILE_SERVER_HOSTNAME 修改为你自己的域名
   ```
3. 运行 compose 重建命令
   ```
   sudo cd /data && docker-compose up -d
   ```
4. HTTPS 设置成功


### 管理员密码

实际工作中，我们可能会 **修改** 或 **找回** Seafile 管理员密码

#### 修改密码

1. 以管理员账号登录后台
2. 依次打开：【设置】>【更新】，编辑需要修改密码的账号
3. 修改密码后提交，退出后新密码生效 
   ![Seafile 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-modifypw-websoft9.png)

#### 找回密码

若不记得 Seafile 管理员密码，可以通过如下两个方式找回

方案一：通过邮件找回密码

Seafile可以通过发送邮件找回密码，但前提条件是您的 Seafile 已经配置好SMTP
![Seafile 找回密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-forgetpw-websoft9.png)

方案二：修改数据库中的密码字段

如果不能发邮件，请登录数据库管理面板 phpMyAdmin 进行修改

1. 登录 phpMyAdmin，并找到你的网站数据库下的 *EmailUser* 表,编辑管理员用户（下图以用户名 `me.example.com`为例）
   ![Wordpress 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-userspw-websoft9.png)
   
2. 截图的地方数据库密码(加密后的密文)，用`PBKDF2SHA256$10000$7289a20ae4fc2329415b0645fa3d106019cc61952ae1bc2f9eeef7b30dc47d88$5418ac28f06bd84f2bb701a10dbea6b0bd30676c8042e1f73b9ce12aac302a8d`替换之
3. 点击【执行】
4. 新的密码为`123456`

## 参数{#parameter}

Seafile 应用中包含 Nginx, Docker, MySQL, phpMyAdmin, ONLYOFFICE docs, ElasticSearch 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 Seafile 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE                              COMMAND                  CREATED             STATUS              PORTS                                         NAMES
958e4cbc8dbe        seafileltd/seafile-mc:latest       "/sbin/my_init -- /s…"   14 hours ago        Up 9 minutes        0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp      seafile
80c266262079        phpmyadmin/phpmyadmin:latest       "/docker-entrypoint.…"   14 hours ago        Up 9 minutes        0.0.0.0:9090->80/tcp                          phpmyadmin
cea7ee7b8f2a        memcached:1.5.6                    "memcached -m 256"       14 hours ago        Up 9 minutes        11211/tcp                                     seafile-memcached
43881d791ed6        seafileltd/elasticsearch:5.6.16    "/docker-entrypoint.…"   14 hours ago        Up 9 minutes        3306/tcp                                      seafile-elasticsearch
a4498231bb29        onlyoffice/documentserver:latest   "/bin/sh -c /app/ds/…"   39 hours ago        Up 9 minutes        0.0.0.0:9002->80/tcp, 0.0.0.0:9003->443/tcp   onlyoffice-documentserver
```


下面仅列出 Seafile 本身的参数：

### 路径{#path}

Seafile 存储目录： */data/wwwroot/seafile/seafile-data*  
Seafile 日志目录： */data/wwwroot/seafile/seafile-data/logs*

seafile-memcached 存储目录： */data/wwwroot/seafile/seafile-data*  
seafile-memcached 日志目录： */data/wwwroot/seafile/seafile-data/logs*

seafile-elasticsearch 存储目录： */data/wwwroot/seafile/seafile-elasticsearch*  
seafile-elasticsearch 日志目录： */data/wwwroot/seafile/seafile-data/logs*

> Seafile 配置文件包括 seahub_settings.py, seafile.conf等

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9002 | 通过 http访问 OnlyOffice Docs on Docker | 可选 |

### 版本{#version}

Seafile 控制台查看  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-aboutversion-websoft9.png)

### 服务{#service}

```shell
sudo docker start | stop | restart seafile
```

### 命令行{#cli}

[Seafile client for a Cli server](https://help.seafile.com/syncing_client/linux-cli/)

### API

[Web AP](https://manual.seafile.com/develop/web_api_v2.1/)

