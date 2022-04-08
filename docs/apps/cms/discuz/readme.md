---
sidebar_position: 1
slug: /discuz
tags:
  - Discuz
  - CMS
  - 建站系统
  - 博客系统 
---

# 快速入门

Discuz 是老牌的论坛社区系统（也称之为 DiscuzX），诞生于2001年6月，后被腾讯公司收购。Discuz 生态经久不衰，基于它可以搭建社区论坛、知识付费网站、视频直播点播站、企业网站、同城社区、小程序、APP、图片素材站，游戏交流站，电商购物站、小说阅读、博客、拼车系统、房产信息、求职招聘、婚恋交友等等绝大多数类型的网站

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds06.png)

## 准备

部署 Websoft9 提供的 Discuz 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Discuz 的 **[默认账号和密码](./setup/credentials)**  
4. 若想用域名访问  Discuz **[域名五步设置](./dns#domain)** 过程


## Discuz 初始化向导{#init}

### 详细步骤

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 就进入引导首页

2.  首先点击【我同意】，确认用户许可协议
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds01.png)

3.  通过环境检测后，点击【下一步】。  
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds02.png)

4.  选择需要安装的程序组，建议选择【全新安装】，然后点击【下一步】。  
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds03.png)

5.  配置数据库连接信息：请直接点击【下一步】完成连接。（**请不做任何修改**）   
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds04.png)

6.  安装完成后的界面如下  
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds05.png)

7.  进入论坛后，可以通过右上角登录对论坛进行管理。
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds06.png)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**安装的时候显示Discuz! Database Error**

如果数据库名称、数据库账号与数据库密码填写与实际不符合，安装就会失败，显示“Discuz! Database Error”错误，具体解决办法：

1. 使用 phpMyAdmin 连接数据库，验证填写的数据库账号是否与实际匹配
2. 删除 Discuz 目录下的 *data/install.lock* 文件
3. 本地浏览器访问： *http://服务器公网IP/discuz/install* 或 *http://域名/install* 重装


## Discuz 使用入门

下面以 **使用 Discuz 构建论坛系统** 作为一个任务，帮助用户快速入门：


## Discuz 常用操作

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数

2. 进入 Discuz 后台，打开：【站长】>【邮件设置】，仔细填写 SMTP 参数项   
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
     
### Discuz 更换域名

Discuz 更换域名非常繁琐，参考论坛上的热心帖子：[discuz! X3 更改域名全程记录](https://www.discuz.net/thread-3528253-1-1.html)

### Discuz 模板/主题/应用中心使用

Discuz 有非常强大生态，大量在线安装模板、插件，您通过登录到 Discuz 后台，并连接您的【应用中心】账号，你就可以通过后台在线购买（免费或收费）插件模板，并在线安装就可以使用了。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-appcenter-websoft9.png)

> 声明：Websoft9 不擅长 Discuz 具体功能的使用，更无法提供此类问题指出。请自行参阅 [Discuz 官方论坛](http://www.discuz.net/forum.php) 完成你要做的吧

### Discuz 修改数据库配置

在你的 Discuz 安装目录下，有三个与数据库相关的[配置文件](#path)

一旦数据库连接信息变化，你需要配套修改以上三个文件以适用新的数据库配置。

### Discuz 重置管理员密码

Discuz 密码忘记了，怎么找回？ 如下方案经过实践可用：

1. 适用 SFTP 工具连接服务器，编辑 Discuz 根目录下的 *uc_server/data/config.inc.php* 文件
2. 用下面两行代码替换 `config.inc.php` 中已有的同名段
   ```
   define('UC_FOUNDERPW','047099adb883dc19616dae0ef2adc5b6');
   define('UC_FOUNDERSALT','311254');
   ```
3. [重启服务](./setup/parameter#service)
4. 此时 Ucenter 创始人的密码就变为: `123456789`
5. 访问 *http://服务器公网IP/uc_server*，以`123456789`作为密码登录 Ucenter
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-ucpwlogin-websoft9.png)
6. 通过【用户管理】中修改管理员密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-ucentermodifyadmin-websoft9.png)

### Discuz 更换默认 Logo

参考论坛上的热心帖子：[如何替换程序默认Logo](http://www.discuz.net/thread-3185527-1-1.html) 

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
  
5. [重启服务](./setup/parameter#service) 后生效
  
### Discuz 修改上传附件大小

如果 [PHP](./php#ini) 上传参数已经足够大，但 Discuz 用户上传大小无法满足需求，请通过如下的方式进行修改：

1.进入后台，选择【用户】选项，在【管理者】中选择相应用户组，进入基本设置

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-modifyfilesize001-websoft9.png)

2.选择【论坛相关】，选中【附件相关】

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-modifyfilesize002-websoft9.png)

3.进入附件相关，在【论坛最大附件尺寸】中设置附加最大尺寸

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-modifyfilesize003-websoft9.png)


## 参数{#parameter}

**[通用参数表](./setup/parameter)** 中可查看 PHP, Nginx, Apache, Docker, MySQL 等 Discuz 应用中包含的基础架构组件路径、版本、端口等参数。 

通过运行`docker ps`，可以查看到 Discuz 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Discuz 本身的参数：

### 路径{#path}

Discuz 安装目录： */data/wwwroot/discuz*  
Discuz 配置文件： */data/wwwroot/discuz/upload/config/config_global_default.php*  
Discuz 数据库相关配置文件：  
- config/config_global.php
- config/config_ucenter.php
- uc_server/data/config.inc.php

### 端口{#port}

无特殊端口


### 版本{#version}

控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats discuz
```

### 命令行{#cli}

无

### API

无