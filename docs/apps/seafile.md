---
title: Seafile
slug: /seafile
tags:
  - 文档管理
  - Office
  - 档案
---

import Meta from './_include/seafile.md';

<Meta name="meta" />

## 企业版

Websoft9 是 Seafile 的企业版合作伙伴，通过 Websoft9 购买企业版，可以获得更多优惠

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Seafile 后，通过【我的应用】进入它的编辑窗口，在**访问**标签页中获取登录地址和账号。  

1. 本地浏览器访问, 进入Seafile 登录页面
   ![Seafile登录页面](http://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-login-websoft9.png)

2. 输入用户名和密码，登录到Seafile后台管理界面
   ![Seafile后台界面](http://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-bk-websoft9.png)

3. 设置（检查） Seafile 的真实主机地址（**必选项，否则无法使用文件上传功能**）

   - SERVICE_URL：*http://服务器公网IP*
   - FILE_SERVER_ROOT：*http://服务器公网IP/seafhttp*

   ![Seafile后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-seturl-websoft9.png)

4. 开始使用 Seafile 全面友好的功能吧

5. [导入](#importlicense)授权文件 (仅 Seafile 企业版需要)


### 快速了解

- [《Seafile 用户手册》](https://cloud.seafile.com/published/seafile-user-manual/home.md) 
- [《Seafile 服务器手册》](https://cloud.seafile.com/published/seafile-manual-cn/home.md)
- 手机端支持（√）
- 多语言（√）
- 文档进行预览和编辑（需第三方中间件）

### 集成 ONLYOFFICE Docs{#onlyoffice}

Seafile 开源版支持集成 OnlyOffice Docs 作为 Office 格式的文档预览与编辑，且本部署方案已配置好 OnlyOffice Docs，开机即用。

但是，为了便于用户维护，下面我们把配置的详细步骤列出，以供需要时参考：  

1. 首先，确保 [OnlyOffice Docs](../onlyofficedocs) 可访问
2. 然后，SFTP 连接服务器，编辑 Seafile 配置文件/data/apps/seafile/data/seafile_data/seafile/conf/seahub_settings.py
3. 插入下面的模板（或对已经存在的模板进行修改）
   ```
   # Enable Only Office
   ENABLE_ONLYOFFICE = True
   VERIFY_ONLYOFFICE_CERTIFICATE = False
   ONLYOFFICE_APIJS_URL = 'http://example.seafile.com:9002/web-apps/apps/api/documents/api.js'
   ONLYOFFICE_FILE_EXTENSION = ('doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'odt', 'fodt', 'odp', 'fodp', 'ods', 'fods')
   ONLYOFFICE_EDIT_FILE_EXTENSION = ('docx', 'pptx', 'xlsx')
   ```
   > ONLYOFFICE_APIJS_URL 字段中的 **example.seafile.com** 地址请更改为你的服务器公网IP地址或域名。如果 OnlyOffice 已启用 https，URL地址改成 https 开头

4. 重启 Seafile 容器服务
   ```
   sudo docker restart seafile
   ```

5. 测试预览或编辑文档功能
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-onlyofficepr-websoft9.png)

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
cp seafile-license.txt /data/apps/seafile/data/seafile_data
docker restart seafile
```

### 使用客户端{#client}

1. 到[官网](https://www.seafile.com/download/)下载客户端

2. 获取客户端登录 SERVICE_URL ：登录到 Seafile 后台，点击右上方个人头像，进入【系统设置】获取 SERVICE_URL

   ![Seafile](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-client-web-websoft9.jpg)

3. 在手机上打开 Seafile 客户端，输入上面获取的 SERVICE_URL 和[账号](./user/credentials)，点击登录

   ![Seafile](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-client-login-websoft9.jpg)

4. 客户端主界面

   ![Seafile](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-client-main-websoft9.jpg)

## 管理维护{#administrator}

### 配置 SMTP{#smtp}

1. 编辑 Seafile 配置文件 seahub_settings.py，插入邮箱配置段
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

2. 重启 Seafile 容器服务

### 修改邮件通知签名

在[邮件模板](https://manual-cn-origin.seafile.com/config/customize_email_notifications)文件中 "Seafile 团队" 实际上对应后台的【site_name】字段。所以，如果想将邮件通知中默认签名 "Seafile 团队" 修改成自己的签名，方案如下：

登录到 Seafile 修改网站名称即可：
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-sitename-email-websoft9.png)

### 修改 URL{#url}

首次使用、设置HTTPS 或 修改域名后，登录 Seafile 后台，修改主机地址。必须修改，否则文件无法正常上传、下载。

  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-seturl-websoft9.png)  


#### 找回密码

若不记得 Seafile 管理员密码，除了邮件找回之外。可以通过修改数据库的方式：

1. 使用可视化管理工具，编辑 *EmailUser* 表中的管理员用户，将下面的值更新到其 password 值中
   ```
   PBKDF2SHA256$10000$7289a20ae4fc2329415b0645fa3d106019cc61952ae1bc2f9eeef7b30dc47d88$5418ac28f06bd84f2bb701a10dbea6b0bd30676c8042e1f73b9ce12aac302a8d
   ```
2. 密码就被重置为 `123456`

## 故障

#### Seafile 无法上传文件？

设置 Seafile 的主机地址（**必选项，否则无法使用文件上传功能**）

   - SERVICE_URL：*http://服务器公网IP*
   - FILE_SERVER_ROOT：*http://服务器公网IP/seafhttp*

   ![Seafile后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-seturl-websoft9.png)
   
   
#### 完成文档服务器配置，Seafile 仍然无法编辑和预览文件？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-canotaccess-websoft9.png)  

问题原因：SERVICE_URL 与实际不符  
解决方案：需登录控制台的系统设置，修改 SERVICE_URL 为实际值

#### 完成 ONLYOFFICE Docs 配置，Seafile 编辑和预览显示错误 “文档安全令牌未正确形成”？

问题原因：ONLYOFFICE docs 安全设置过高   
解决方案：需修改 ONLYOFFICE docs 编排文件中的环境变量 JWT_ENABLED，设置为 false  

```
  onlyoffice-document-server:
    container_name: onlyoffice-docs
    image: onlyoffice/documentserver:6.0.2
    stdin_open: true
    tty: true
    restart: always
    environment:
     - JWT_ENABLED=flase
```