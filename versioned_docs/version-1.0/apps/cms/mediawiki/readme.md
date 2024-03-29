---
sidebar_position: 1
slug: /mediawiki
tags:
  - Mediawiki
  - CMS
  - 知识管理
  - 博客系统
---

# 快速入门

[MediaWiki](https://www.mediawiki.org) 是大名鼎鼎的“维基百科”网站开源的 Wiki 程序。适合用于构建百科、知识库、在线文档、个人笔记等应用。MediaWiki的最大作用在于对知识的归档，可用于构建企业/个人知识库，Wiki 系统的思想是经过越多的人的编辑，结果就越趋于正确（完美）。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mediawiki/MediaWiki_UI.png)

## 准备

部署 Websoft9 提供的 MediaWiki 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 MediaWiki 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  MediaWiki **[域名五步设置](./administrator/domain_step)** 过程


## MediaWiki 初始化向导

### 详细步骤

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 就进入引导首页
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mediawiki/mediawiki-install1-websoft9.png)

2. 点击【login in】,输入用户名和密码([不知道账号密码？](./user/credentials)) 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mediawiki/mediawiki-install2-websoft9.png)

3. 进入MediaWiki后台，体验完整功能 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mediawiki/mediawiki-install3-websoft9.png)

> 需要了解更多MediaWiki的使用，请参考官方文档：[MediaWiki FAQ](https://www.mediawiki.org/wiki/Sysadmin_hub/zh)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**重装 MediaWiki**

本地浏览器访问： *http://服务公网IP/mw-config/index.php?page=Restart&lastPage=Install* ，开始重装

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mediawiki/Mediawiki-reinstall-websoft9.png)

## MediaWiki 使用入门

下面以 **使用 MediaWiki 构建知识管理系统** 作为一个任务，帮助用户快速入门：

## MediaWiki 常用操作

### MediaWiki 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数

2. 编辑网站根目录下的 `LocalSettings.php` 配置文件

3. 找到变量 $wgSMTP，并设置它
   
   ```
    $wgSMTP = array(
    'host'     => "smtp.163.com", 
    'IDHost'   => "example.com",      // 邮箱域名，可选.如果不设置的话会设置成 $wgServer 的值.
    'port'     => 465,                 
    'auth'     => true,               
    'username' => "websoft9@163.com",     
    'password' => "#wwBJ8"       
    );
   ```

4. 找到变量 $ wgEnableEmail，设置其值为 true
   
   ```
    $ wgEnableEmail = true
   ```


5. 查找以下变量，将其值设置为发件邮箱
   
   ```
    $wgEmergencyContact = "websoft9@163.com";
    $wgPasswordSender = "websoft9@163.com";
   ```


6. 保存设置

7. 重启 [PHP-FPM 服务](./administrator/parameter#service)后生效

8. 测试是否可以发邮件

### MediaWiki 安装扩展{#plugin}

参考官方文档：[Manual:Extensions](https://www.mediawiki.org/wiki/Manual:Extensions/zh)

### MediaWiki 创建或编辑页面{#page}

参考官方文档：[Help:Starting_a_new_page](https://www.mediawiki.org/wiki/Help:Starting_a_new_page/zh)

### MediaWiki 可视化编辑器{#edit}

参考官方文档：[Help:Starting_a_new_page](https://www.mediawiki.org/wiki/Help:VisualEditor/User_guide/zh)

### MediaWiki 定制界面{#theme}

定制界面包括：修改 Logo, 设置导航栏，修改 CSS 等  

参考官方文档：[Help:FAQ:定制界面](https://www.mediawiki.org/wiki/Manual:FAQ/zh#定制界面)

### MediaWiki 允许文件上传{#upload}

Mediawiki 默认并不可以上传文件，需要启动文件上传功能  

参考官方文档：[Help:FAQ:启用文件上传](https://www.mediawiki.org/wiki/Manual:FAQ/zh#如何启用文件上传?)

### MediaWiki 语言设置{#setlang}

参考官方文档：[Help:FAQ:语言设置](https://www.mediawiki.org/wiki/Manual:FAQ/zh#我如何更改界面语言？)

### MediaWiki 设置主页{#sethomepage}

参考官方文档：[Help:FAQ:设置主页](https://www.mediawiki.org/wiki/Manual:FAQ/zh#如何指定首页?)

### MediaWiki 使用 Composer{#composer}

本预装包默认已经安装 Composer，详细使用  

参考官方文档：[Help:Composer](https://www.mediawiki.org/wiki/Composer/zh)


## 参数{#parameter}

MediaWiki 应用中包含 PHP, Nginx, Apache, Docker, MySQL 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行 `docker ps`，可以查看到 MediaWiki 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS          PORTS                                                 NAMES
88ba09aae88d   bitnami/mediawiki:latest   "/opt/bitnami/script…"   11 minutes ago   Up 11 minutes   8443/tcp, 0.0.0.0:9005->8080/tcp, :::9005->8080/tcp   mediawiki
9f651002908f   mysql:5.7                  "docker-entrypoint.s…"   11 minutes ago   Up 11 minutes   3306/tcp, 33060/tcp                                   mediawiki-db
```


### 路径{#path}

MediaWiki 安装目录： */data/apps/mediawiki*  
MediaWiki 配置文件： */data/apps/mediawiki/data/mediawiki/LocalSettings.php*    
MediaWiki 插件目录： */data/apps/mediawiki/data/mediawiki/extensions*    

### 端口{#port}

无特殊端口

### 版本{#version}

```
sudo docker exec -i mediawiki grep -rn "MediaWiki " /bitnami/mediawiki/LocalSettings.php|awk -F"MediaWiki " '{print $2}'
```

### 服务{#service}

```shell
sudo docker start | stop | restart | stats mediawiki
sudo docker start | stop | restart | stats mediawiki-db
```

### 命令行{#cli}

无

### API

[API:Main_page](https://www.mediawiki.org/wiki/API:Main_page/zh)