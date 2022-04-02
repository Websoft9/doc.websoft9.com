---
sidebar_position: 1
slug: /ghost
tags:
  - Ghost
  - CMS
  - 建站系统
  - 博客系统
---

# 快速入门

[Ghost](https://ghost.org) 是一款功能强大的知识内容变现软件，供新媒体创作者围绕其内容发布、分享和发展业务。它配备了现代工具来构建网站、发布内容、发送时事通讯并向会员提供付费订阅。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/ghost/ghost-dsgui-websoft9.png)

## 准备

部署 Websoft9 提供的 Ghost 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Ghost 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  Ghost **[域名五步设置](./dns#domain)** 过程


## Ghost 初始化向导

### 详细步骤

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入前台界面
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-bootpage-websoft9.png)

2. 访问网址：*http://域名/ghost* 或 *http://服务器公网IP/ghost*, 进入后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-register001-websoft9.png)

3. 开始创建管理员账号，以邮箱地址为用户名，密码不要设置过于简单  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-register002-websoft9.png)

> 需要了解更多 Ghost 的使用，参考官方：[Tutorials](https://ghost.org/tutorials/) 和 [FAQ](https://ghost.org/faq/)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

## Ghost 使用入门

下面以 **使用 Ghost 构建博客** 作为一个任务，帮助用户快速入门：


## Ghost 常用操作

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数

2. 修改 Ghost 配置文件 mail 相关配置段。特别注意的是 "from" 与 "user" 必须一致，否则邮件无法发送。
   ```
      "mail": {
         "transport": "SMTP",
         "from": "45745412@qq.com",
         "options": {
            "service": "QQ",
            "auth": {
               "user": "45745412@qq.com",
               "pass": "#wwBJ8"
            }
         }
   },
   ```

   也支持详细的 SMTP 设置方案（此时不要 "service": "QQ" 这个配置段）

   ```
      "mail": {
         "transport": "SMTP",
         "from": "norelpy@smtp.websoft9.com",
         "options": {
            "host": "smtp.websoft9.com",
            "port": 465,
            "secureConnection": true,
            "auth": {
               "user": "norelpy@smtp.websoft9.com",
               "pass": "yourpassword****"
            }
         }
   },
   ```

3. 重启 Ghost 容器
   ```
   cd /data/wwwroot/ghost && docker-compose up -d && docker restart ghost
   ```

4. 登录 Ghost 后台，打开：【Manage】>【Staff】，通过【Invite People】 测试邮箱可用性

### 域名额外配置（修改 URL） {#dns}

**[域名五步设置](./dns#domain)** 完成后，需设置 Ghost 的 URL:  

1. 修改 [Ghost 配置文件](#path)中的 URL 域名地址（同上）
   ```
   {
   "url": "http://ghost.yourdomain.com",
   "server": {
      "port": 2368,
      "host": "0.0.0.0"
   },
   ```

2. 重启服务后生效
   ```
   sudo systemctl restart nginx
   cd /data/wwwroot/ghost && sudo docker-compose up -d && sudo docker restart ghost
   ```


### 功能设置

#### 菜单

Ghost 可以很方便的定义菜单栏：

1. 登录 Ghost，点击左侧菜单栏的【SETTING】>【Design】
  ![Ghost 代码插入](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-setmenus-websoft9.png)

2. 设置所需的网址，点击【Save】保存后即可生效。

#### 主题

Ghost 的主题是网站页面的主要个性化入口。系统默认提供了一个主题，同时也支持用户自己上传主题，实现界面个性化

1. 登录 Ghost，点击左侧菜单栏的【SETTING】>【Design】，下拉到主题设置区域

2. 先点击【Theme Marketplace】找到一款自己喜欢的主题，并下载主题的压缩文件（一般以.zip结尾）
  ![Ghost 设置主题](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-setthemes-websoft9.png)

3. 再点击【Upload a theme】上传主题文件，并【Active】它后生效

上传的主题会保存到服务器：*/data/wwwroot/ghost/content/themes* 目录下，用户可以修改其中的文件，实现主题在代码层面的个性化定制与开发。

#### 多语言

Ghost 的后台不支持中文，但是前台支持中文（需主题中有中文）。

1. 使用 SSH 或 SFTP 工具登录服务，进入到你的主题下 locales 目录

2. 正常情况下，你会看到很多 json 文件，这些就是主题的翻译文件

3. 查看 zh-hans.json 文件，你会看到中文简体的翻译，即此文件代表简体中文

4. 登录到 Ghost 后台，点击左侧菜单栏的【General】，展开【Publication Language】，设置其值为：zh-hans
  ![Ghost 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-setzhhans-websoft9.png)

5. 保存后即刻生效

#### 代码嵌入

代码嵌入可以帮助你的 Ghost 网站插入第三方 JavaScript 代码，例如：百度统计、Google Analysis 等。这些代码一旦插入之后，就会针对每一个页面生效。

1. 登录 Ghost，点击左侧菜单栏的【SETTING】>【Code Injection】
  ![Ghost 代码插入](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-codeinjection-websoft9.png)

2. 将所需的代码拷贝到此处后，点击【Save】保存后即可生效。

#### 订阅

Ghost 支持网站向客户以订阅的方式售卖文章，是知识付费创业者的生产力工具。

1. 登录 Ghost，点击左侧菜单栏的【SETTING】>【Labs 】

2. 分别对 Enable members, Connect to Stripe, Subscription pricing 等项进行设置
  ![Ghost 代码插入](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-setsubs-websoft9.png)


## 参数{#parameter}

Ghost 应用中包含 Apache, Docker, MySQL 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。  

通过运行`docker ps`，可以查看到 Ghost 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Ghost 本身的参数：

### 路径{#path}

Ghost 安装目录： */data/wwwroot/ghost/content*  
Ghost 配置文件： */data/wwwroot/ghost/config.production.json*  
Ghost 容器编排文件： */data/wwwroot/ghost/docker-compose.yml*  


### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 8080   | Ghost 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


### 版本{#version}

控制塔查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats ghost
```

### 命令行{#cli}

[Ghost CLI](https://ghost.org/docs/ghost-cli/)

### API

[Content API](https://ghost.org/docs/content-api/)
