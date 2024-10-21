---
sidebar_position: 1
slug: /discuz
tags:
  - Discuz
  - CMS
  - 建站系统
  - Blog
---

# Discuz Getting Started

[Discuz](https://www.discuz.net)  is the best Forum & Community software in China, 200 million users in the world

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-gui-websoft9.png)  

If you have installed Websoft9 Discuz, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. **[Get](./user/credentials)** default username and password of Discuz
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Discuz.


## Discuz Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *https://domain* or *https://Internet IP*, start to install  

2. Click "我同意",accept the liecense to the next step
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds01.png)

3. Requirement check,then Click "下一步"
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds02.png)

4. Select "全新安装 Discuz!X(含 UCenter Server)" and Click "下一步"
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds03.png)

5. Then configure the database connection information([Don't know password?](./user/credentials))
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds04.png)

6. Complete the installation, you can access the Discuz now
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds05.png)

7. In the index page of Discuz, you can see the log in area
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds06.png)

8. Discuz provides a very powerful function of installing templates and plug-ins online. you log in to the background of Discuz and connect your application center account, you can purchase (free or charged) plugin templates online through the background and install them online.

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more. 

#### Discuz! Database Error

If you database configuration is incorrect,you can receive the message "Discuz! Database Error"

1. Using phpMyAdmin to check you database account
2. Connect in Cloud Server, delete the file: */data/wwwroot/discuz/data/install.lock*
3. Visit URL *https://Internet IP or Domain/install* to start re-installation

## Discuz QuickStart

下面以 **使用 Discuz 构建论坛系统** 作为一个任务，帮助用户快速入门：

## Discuz Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Log in Discuz Console, open 【Manage Discuz】>【Configure System】, set you SMTP
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-smtp-1-websoft9.png)

   - 选择第二项
	- 根据你的 SMTP 邮箱选择 SMTP服务器域名，前面的”ssl://“一定不能省略
	- 端口栏输入 SMTP 服务器提供的端口号，一般为 465 ，具体的可根据自己的邮箱地址到官网查看
	- 发件人邮件地址输入你自己的邮箱（**需要与SMTP身份验证用户名所填的邮箱地址一致**）
	- 输入提供 SMTP 服务的邮箱地址
	- 输入 SMTP 服务验证码（和邮箱登陆密码不一样）

3. 在 Discuz 后台，打开【全局】>【站点信息】，设置全局管理员邮箱，尽量和 SMTP 发件人邮箱保持一致
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-smtp-2-websoft9.png)
    
4. 测试，如出现如图所示的对话框则证明 SMTP 设置正确，另外，如果出现该对话框却在收件箱内没有邮件，请到垃圾邮件列表查看
	![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-smtp-3-websoft9.png)

### Discuz Change domain

Refer to [discuz! X3 更改域名全程记录](https://www.discuz.net/thread-3528253-1-1.html)

### Discuz 模板/主题/应用中心使用

Discuz 有非常强大生态，大量在线安装模板、插件，您通过登录到 Discuz 后台，并连接您的【应用中心】账号，你就可以通过后台在线购买（免费或收费）插件模板，并在线安装就可以使用了。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-appcenter-websoft9.png)

> 声明：Websoft9 不擅长 Discuz 具体功能的使用，更无法提供此类问题指出。请自行参阅 [Discuz 官方论坛](http://www.discuz.net/forum.php) 完成你要做的吧

### Discuz modify database connection{#modifydbconn}

In your Discuz installation directory, there are three database-related [configuration files](#path)

Once you have modified the database information used to initialize the installation, you will need to modify the above three files to apply the new database configuration.

### Discuz recover administrator password

1. Use SFTP to login Server, edit the *uc_server/data/config.inc.php* file in the root directory of Discuz  

2. Replace two items below with 
   ```
   define('UC_FOUNDERPW','047099adb883dc19616dae0ef2adc5b6');
   define('UC_FOUNDERSALT','311254');
   ```  

3. [Restart Service](./administrator/parameter#service)  

4. Then, your Ucenter administrator password is: `123456789`  

5. Visit URL *http://Internet IP/uc_server*, us `123456789` as your password to login Ucenter
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-ucpwlogin-websoft9.png)  

6. Modify adminitrator password from 【用户管理】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-ucentermodifyadmin-websoft9.png)

### Discuz change Logo

Refer to Discuz forum [如何替换程序默认Logo](http://www.discuz.net/thread-3185527-1-1.html)  

### Discuz 设置伪静态

Discuz论坛安装完成后，想使连接里面显示文章名，应怎么开启它的伪静态功能？

1. 网站安装完成后，登录进入后台，在全局>SEO优化设置>将要设置的页面勾选上，然后提交； 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-rewrite001-websoft9.png)

2. 重新回到上图页面，点击【查看当前的 Rewrite 规则】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-rewrite002-websoft9.png)

3. 页面会列出多种规则，请选择【Apache Web Server(虚拟主机用户)】模板（内容如下）
   ```
   # 将 RewriteEngine 模式打开
   RewriteEngine On

   # 修改以下语句中的 /discuz 为您的论坛目录地址，如果程序放在根目录中，请将 /discuz 修改为 /  对于websoft9提供的镜像，如果服务器内只有一个dicuz网站，则改成如下即可
   RewriteBase / 

   # Rewrite 系统规则请勿修改
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^topic-(.+)\.html$ portal.php?mod=topic&topic=$1&%1
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^article-([0-9]+)-([0-9]+)\.html$ portal.php?mod=view&aid=$1&page=$2&%1
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^forum-(\w+)-([0-9]+)\.html$ forum.php?mod=forumdisplay&fid=$1&page=$2&%1
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^thread-([0-9]+)-([0-9]+)-([0-9]+)\.html$ forum.php?mod=viewthread&tid=$1&extra=page\%3D$3&page=$2&%1
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^group-([0-9]+)-([0-9]+)\.html$ forum.php?mod=group&fid=$1&page=$2&%1
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^space-(username|uid)-(.+)\.html$ home.php?mod=space&$1=$2&%1
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^blog-([0-9]+)-([0-9]+)\.html$ home.php?mod=space&uid=$1&do=blog&id=$2&%1
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^(fid|tid)-([0-9]+)\.html$ archiver/index.php?action=$1&value=$2&%1
   RewriteCond %{QUERY_STRING} ^(.*)$
   RewriteRule ^([a-z]+[a-z0-9_]*)-([a-z0-9_\-]+)\.html$ plugin.php?id=$1:$2&%1
   ```

4. 在 Discuz 的根目录下，新建一个`.htaccess` 文件，将上面的模板内容拷贝进去，保存
   如果是Windows服务器，请选择【另存为】，文件类型选择【所有文件】，否则无法命名
  
5. [重启服务](./administrator/parameter#service) 后生效
  
### Discuz 修改上传附件大小

如果 [PHP](./php) 上传参数已经足够大，但 Discuz 用户上传大小无法满足需求，请通过如下的方式进行修改：

1.进入后台，选择【用户】选项，在【管理者】中选择相应用户组，进入基本设置

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-modifyfilesize001-websoft9.png)

2.选择【论坛相关】，选中【附件相关】

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-modifyfilesize002-websoft9.png)

3.进入附件相关，在【论坛最大附件尺寸】中设置附加最大尺寸

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-modifyfilesize003-websoft9.png)

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Discuz

Run `docker ps` command, view all Containers when Discuz is running:

```bash
CONTAINER ID   IMAGE                     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
39280f60a6be   phpmyadmin:latest         "/docker-entrypoint.…"   29 minutes ago   Up 29 minutes   0.0.0.0:9090->80/tcp, :::9090->80/tcp   phpmyadmin
7d838f86d7c8   websoft9dev/discuz:v1.0   "bash -c 'cat /my_cm…"   29 minutes ago   Up 29 minutes   0.0.0.0:9001->80/tcp, :::9001->80/tcp   discuz
916b76113150   mysql:5.7                 "docker-entrypoint.s…"   29 minutes ago   Up 29 minutes   3306/tcp, 33060/tcp                     discuz-db
```

### Path{#path}

Discuz installation directory: */data/apps/discuz*  
Discuz website directory： */data/apps/discuz/data/discuz*  
Discuz configuration file: */data/apps/discuz/data/discuz/config/config_global_default.php*  

### Port{#port}

No special port

### Version{#version}

```
sudo docker exec -it discuz cat /usr/src/discuz/upload/source/discuz_version.php |grep "'DISCUZ_VERSION'," |awk -F"," '{print $2}'|awk -F"'" '{print $2}'
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats discuz
sudo docker start | stop | restart | stats discuz-db
sudo docker start | stop | restart | stats phpmyadmin
```

### CLI{#cli}



### API
