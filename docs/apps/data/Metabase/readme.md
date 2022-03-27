---
sidebar_position: 1
slug: /metabase
tags:
  - Metabase
  - 大数据分析
  - BI
---

# 快速入门

[Metabase](https://www.metabase.com/) 是一个简单、开源的数据呈现方式，通过给公司成员、分析师新建Question，从而得到数据进行分析、学习。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-product-screenshot.png)

部署 Websoft9 提供的  Metabase 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 和 **TCP:9001** 端口是否开启
3. 在服务器中查看 Metabase 的 **[默认账号和密码](./setup/credentials#getpw)** 
4. 若想用域名访问 Metabase，务必先完成**[域名五步设置](./dns#domain)** 过程

## Metabase 初始化向导

1. 使用本地电脑的浏览器访问网址：*http://域名* 或 *http://Internet IP*，进入登陆页面（如果页面不是登陆页面，请按照步骤3-7操作）
![Metabase登陆界面](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-login-websoft9.png)

2. 输入邮件地址和密码[（不知道密码？）](/zh/stack-accounts.md)，登录到 Metabase 后台管理界面
![Metabase后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-dashborad-websoft9.png)

3. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 就进入了软件的引导首页
![Metabase初始化页面](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-start-websoft9.png)

4. 软件的加载速度比较慢，耐心等待1-3分钟，直至出现如下的界面。
![开始安装Metabase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-starty-websoft9.png)

5. 点击“让我们开始吧”，接下来首先设置登录账号，完成后进入下一步
6. 添加你的数据：可以选择使用的数据类型来连接一个需要分析的外部数据库，如果没有也可以点击“我之后再添加”，这样系统会默认给 Metabase 增加一个H2演示数据
![配置Metabase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-installdb-websoft9.png)

7. 安装成功后的界面，点击“带我去Metabase”登录后台
![Metabase安装成功](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-installss-websoft9.png)

8. 以H2演示数据为例，开始数据分析工作
![Metabase H2演示](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-dashborad-websoft9.png)

9. Metabase有强大的系统管理能力：后台->设置，进入系统管理界面
![Metabase Admin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-admin-websoft9.png)

10. 通过“添加一个数据库”来增加一个数据分析源
![Metabase 增加数据库](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-adddb-websoft9.png)

11. 通过点击“人员管理”标签，管理使用Metabase用户，包括增加用户、修改密码等
![Metabase 人员管理](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-users-websoft9.png)

> 需要了解更多Metabase的使用，请参考官方文档：[Metabase Documentation](https://metabase.com/docs/latest/)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## Metabase 使用入门

下面以 xxx 进行数据分析作为范例。

## 常用操作

### 配置SMTP

Metabase 配置SMTP发邮件的步骤：

1. 管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8
   ```
2. 登录 Metabase 控制台
3. 填写 SMTP 参数
![Metabase SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-smtp-websoft9.png)
4. 点击【Test Connection】，显示OK代表配置成功

## 参数

**[通用参数表](./setup/parameter)** 中可查看 Nginx, Docker, MySQL 等 Metabase 应用中包含的基础架构组件路径、版本、端口等参数。 


### 路径{#path}

Metabase 源码目录：*/data/wwwroot/metabase/data*  
Metabase 插件目录：*/data/wwwroot/metabase/plugins*  

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9001   | Metabase 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |

### 版本

```shell
# Matebase Version
curl https://api.github.com/repos/metabase/metabase/releases/latest |jq -r .tag_name
```

### 服务

本项目采用 Docker 安装，运行 `docker ps` 可以查看所有相关的容器：

```
CONTAINER ID   IMAGE                           COMMAND                  CREATED              STATUS                                 PORTS                               NAMES
453f04935734   apache/Matebase:latest          "/usr/bin/docker-ent…"   About a minute ago   Up About a minute (healthy)            0.0.0.0:8088->8088/tcp              Matebase_app
5477e7693ef3   apache/Matebase:latest          "/usr/bin/docker-ent…"   About a minute ago   Up About a minute (healthy)            8088/tcp                            Matebase_worker
d6670fa1bc11   apache/Matebase:latest          "/usr/bin/docker-ent…"   About a minute ago   Up About a minute (healthy)            8088/tcp                            Matebase_worker_beat
17689f5d6ebb   postgres:10                     "docker-entrypoint.s…"   About a minute ago   Up About a minute                      0.0.0.0:5432->5432/tcp              Matebase_db
06bf52f4b856   redis:3.2                       "docker-entrypoint.s…"   About a minute ago   Up About a minute                      127.0.0.1:6379->6379/tcp            Matebase_cache
```
可以通过命令查看和启停相关容器：

```shell
sudo docker  start | stop | restart | status metabase
sudo docker  start | stop | restart | status Matebase-mysql
```

### 命令行

Matebase 暂时未提供命令行工具


### API

[Matebase API](https://www.metabase.com/docs/latest/api-documentation.html) 采用REST API 2.0规范。


