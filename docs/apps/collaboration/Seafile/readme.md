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


在云服务器上部署 Seafile 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 和 **TCP:9002** 端口是否开启
3. 若想用域名访问 Seafile，请先到 **域名控制台** 完成一个域名解析

> 9002 是用于文档预览和编辑的 OnlyOffice Document Server 服务所需的端口。

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Seafile

管理员用户名：`me@example.com`  
管理员密码： 存储在您的服务器指定文件中：*/credentials/password.txt*

### MariaDB/MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中（ */credentials/password.txt* ）

> 需要登录MySQL，请参考 [MySQL可视化管理](#mysql-数据管理)


## Seafile 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://公网IP*, 进入Seafile登录页面
   ![Seafile登录页面](http://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-login-websoft9.png)

2. 输入用户名和密码[（查看）](/zh/stack-accounts.md)，登录到Seafile后台管理界面
   ![Seafile后台界面](http://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-bk-websoft9.png)

3. 设置（检查） Seafile 的真实主机地址（**必选项，否则无法使用文件上传功能**）

   - SERVICE_URL：*http://服务器公网IP*
   - FILE_SERVER_ROOT：*http://服务器公网IP/seafhttp*

   ![Seafile后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-seturl-websoft9.png)


4. 开始使用 Seafile 全面友好的功能吧

> 需要了解更多Seafile的使用，请参考：[《Seafile 用户手册》](https://cloud.seafile.com/published/seafile-user-manual/home.md) 和 [《Seafile 服务器手册》](https://cloud.seafile.com/published/seafile-manual-cn/home.md)

5. 安装授权文件(仅支持seafile企业版)

   如果您已经向 Seafile 软件商购买了专业版的授权文件seafile-license.txt，您只需要将该授权文件拷贝至 Seafile 数据持久化目录中的/data/wwwroot/seafile/seafile-data/seafile/目录下，然后重启docker容器，即可完成授权文件的安装。
   
```bash
cp seafile-license.txt /data/wwwroot/seafile/seafile-data/seafile/
docker restart seafile
```
## Seafile 入门向导

Seafile 是一款开源的企业云盘，作为企业云盘，主要用于网络存储和管理文件，以及文件共享和协同办公。在使用 Seafile 时，有如下常规操作：

- 用户和分组管理，用于用户管理，和成员分组统一管理
- 文件和文件库管理，用于文件的管理和分类，并通过查看文件的历史信息了解文件的版本变更
- 共享与写作，用于将文件或文件库共享给个人或群组，实现协同办公

下面我们通过创建资料库、创建文件、编辑文件、设置权限、用户共享等操作，来熟悉 Seafile 的使用。

### 添加文件

下面我们介绍如何添加和编辑文件：

1. 登录到 Seafile 后，添加资料库，然后添加文件

   ![Seafile添加资料库](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-addlib-websoft9.png)

   ![Seafile添加文件](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-addfile-websoft9.png)

2. 在线编辑文件（通过内置的 OnlyOffice Document Server 服务实现）

   ![Seafile编辑文件](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-editfile1-websoft9.png)

### 用户管理

下面我们介绍如何创建用户和群组：

1. 打开右上角用户图标，进入【系统管理】，分别添加【用户】和【群组】

   ![Seafile进入系统管理](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-system-websoft9.png)

   ![Seafile添加用户](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-adduser-websoft9.png)

   ![Seafile添加群组](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-addgroup-websoft9.png)

2. 设置所创建的用户所归属群组

   ![Seafile用户分组](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-addusertogroup-websoft9.png)

### 文件共享

下面我们介绍如何给另外一个用户共享自己的文件：

1. 进入【我的资料库】，将资料库共享给指定用户，

   ![Seafile文件共享](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-sharefile1-websoft9.png)


2. 设定权限为【可写】或【只读】

   ![Seafile文件共享](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-sharefile-websoft9.png)

   > 在选择用户时，需输入用户名，系统自动查找匹配

### 读写共享文件

下面我们演示用户如何读写其他人共享过来的文件：

1. 切换user1用户登录，使用邮箱地址【user1@websoft9】作为登录名
   ![Seafile登录页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-login1-websoft9.png)

2. 查看共享文件，进入 OnlyOffice 进行编辑，保存文档
   ![Seafile查看共享文件](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-viewsharefile-websoft9.png)
   ![Seafile编辑共享文件](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-editfile-websoft9.png)

3. 切换到管理员账号 `me@example.com`，查看共享文件的版本变更信息
   ![查看共享文件版本信息](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-viewfileinfo1-websoft9.png)
   ![查看共享文件版本信息](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-viewfileinfo-websoft9.png)


## 常用操作

### 域名绑定

绑定域名的前置条件是：完成域名解析，且 Seafile 可以通过域名访问

虽然如此，从服务器安全和后续维护考量，**域名绑定**步骤不可省却  

Seafile 域名绑定操作步骤：

1. 使用 SFTP 登录云服务器，修改 [Docker-compose 配置文件](/维护参考.md#docker-compose)，将其中的 **SEAFILE_SERVER_HOSTNAME** 项的值为你的域名
   ```text
    - SEAFILE_SERVER_HOSTNAME=seafile.example.com  # Specifies your host name.
   ```
2. 保存配置文件，重启 Seafile 服务
   ```
   sudo cd /data && docker-compose up -d
   ```

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

Seafile预装包已内置 SSL 模块方案，需要根据自己的域名进行设置方可使用

#### 前置条件

1. 在云控制台开启 **TCP:443** 端口
2. 完成域名解析，确保 Seafile 可以通过域名访问
3. 登录 Seafile 后台，修改主机地址
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-seturl-websoft9.png)

#### 基本设置

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

以上方案是对 Seafile 官方文档：[向Let's encrypt申请SSL证书](https://manual-cn-origin.seafile.com/deploy/deploy_with_docker#xiang-lets-encrypt-shen-qing-ssl-zheng-shu)的实践解读，验证可用

##### 常见问题

##### 设置HTTPS之后，Seafile 容器无法启动？

先运行 `sudo docker logs seafile` 查看日志文件，然后根据日志逐步排查错误

##### 没有域名是否可以设置 Seafile HTTPS？

不可以，即如果 SEAFILE_SERVER_HOSTNAME 处设置为IP地址，会导致 Seafile 无法启动

##### 是否支持自己上传证书？

支持，具体参考[官方文档](https://manual-cn-origin.seafile.com/deploy/deploy_with_docker#xiang-lets-encrypt-shen-qing-ssl-zheng-shu)

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿尝试在服务器上安装sendmail等发邮件方案，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，导致不稳定、不易维护、诊断故障困难。

下面以**网易邮箱**为例，提供设置 Seafile 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数

2. 使用 SFTP 连接服务器，编辑 Seafile 配置文件 [seahub_settings.py](/zh/stack-components.md#seafile)，插入邮箱配置段
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

> 更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)


#### 如何将邮件通知签名 "Seafile 团队" 修改成自己的签名？

Seafile 采用[邮件模板](https://manual-cn-origin.seafile.com/config/customize_email_notifications)进行邮件内容规范化，【Seafile 团队】在邮件模板文件中对应的是【site_name】字段，即网站名称。因此，只需登录到 Seafile 修改网站名称即可。  
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-sitename-email-websoft9.png)

### Seafile 文档预览与编辑

Seafile 开源版支持集成 OnlyOffice Document Server 作为 Office 格式的文档预览与编辑，且本部署方案默认安装 OnlyOffice Document Server，无需设置即可使用

#### 前置条件

1. 在云控制台安全组中，检查 **TCP:9002** 端口是否开启
2. 使用本地电脑浏览器测试文档服务是否可用：*http://服务器公网IP:9002*，会看到 OnlyOffice Document Server 正在运行的提示 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-dkisrunning-websoft9.png)
   
   > 如果 OnlyOffice Document Server 设置好了 HTTPS 访问，请使用 9003 端口

#### 配置

1. 使用 SFTP 连接服务器，编辑 Seafile 配置文件/opt/seafile-data/seafile/conf/seahub_settings.py
2. 插入下面的模板（或对已经存在的模板进行修改）
   ```
   # Enable Only Office
   ENABLE_ONLYOFFICE = True
   VERIFY_ONLYOFFICE_CERTIFICATE = False
   ONLYOFFICE_APIJS_URL = 'http://example.seafile.com:9002/web-apps/apps/api/documents/api.js'
   ONLYOFFICE_FILE_EXTENSION = ('doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'odt', 'fodt', 'odp', 'fodp', 'ods', 'fods')
   ONLYOFFICE_EDIT_FILE_EXTENSION = ('docx', 'pptx', 'xlsx')
   ```
   > ONLYOFFICE_APIJS_URL 字段中的 **example.seafile.com** 地址请更改为你的服务器公网IP地址或域名。如果 OnlyOffice 已启用 https，URL地址改成 https 开头

3. 重启 Seafile 容器服务
   ```
   sudo docker restart seafile
   ```

4. 打开 Seafile 控制台，试一试预览或编辑文档
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-onlyofficepr-websoft9.png)

### MySql 数据管理

Nextcloud 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](/zh/stack-accounts.md))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

### Docker-compose 配置文件

使用 SFTP 登录云服务器，修改 [Docker-compose 配置文件](/维护参考.md#docker-compose)，可以完成常见的维护工作：
> 修改 Docker-compose 配置文件后，运行命令 `sudo cd /data && docker-compose up -d` 后生效

### 管理员密码

实际工作中，我们可能会 **修改** 或 **找回** Seafile 管理员密码

#### 修改Seafile管理员密码？

1. 以管理员账号登录后台
2. 依次打开：【设置】>【更新】，编辑需要修改密码的账号
3. 修改密码后提交，退出后新密码生效 
   ![Seafile 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-modifypw-websoft9.png)

#### 找回 Seafile 管理员密码？

若不记得 Seafile 管理员密码，可以通过如下两个方式找回

##### 方案一：通过邮件找回密码

Seafile可以通过发送邮件找回密码，但前提条件是您的 Seafile 已经配置好SMTP
![Seafile 找回密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-forgetpw-websoft9.png)

##### 方案二：修改数据库中的密码字段

如果不能发邮件，请登录数据库管理面板 phpMyAdmin 进行修改

1. 登录 phpMyAdmin，并找到你的网站数据库下的 *EmailUser* 表,编辑管理员用户（下图以用户名 `me.example.com`为例）
   ![Wordpress 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-userspw-websoft9.png)
   
2. 截图的地方数据库密码(加密后的密文)，用`PBKDF2SHA256$10000$7289a20ae4fc2329415b0645fa3d106019cc61952ae1bc2f9eeef7b30dc47d88$5418ac28f06bd84f2bb701a10dbea6b0bd30676c8042e1f73b9ce12aac302a8d`替换之
3. 点击【执行】
4. 新的密码为`123456`


## 异常处理

#### 浏览器打开IP地址，无法访问 Seafile（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 Seafile 数据？

MariaDB/MySQL on Docker

#### 为什么使用 Docker 安装 Seafile？

是官方推荐的安装方式

#### 默认是否支持文档预览与编辑？

支持

