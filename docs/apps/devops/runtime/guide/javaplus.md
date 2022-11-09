---
sidebar_position: 2
slug: /runtime/javaplus
tags:
  - Java
  - 运行环境
---

# Java 原生应用

Java 原生应用环境是 Websoft9 最新推出的云原生 PaaS 平台，它完全基于 Docker 架构和容器镜像，支持多个 Java 版本的扩展和自定义。与非云原生的环境相比，它的具备更好的扩展能力，升级更简单。

另外，Java 原生应用环境提供了可视化的 Web 面板 -- 以 [Cockpit](https://cockpit-project.org/) 面板为核心，集成了数据库管理工具、Nginx 代理设置、文件管理器、Web 终端等，用户可以在面板可以很方便的完成应用的部署。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/java/runtime-console-java-websoft9.jpg)

## 初始化向导

在云服务器上部署相关预装包之后，请参考下面的步骤快速入门。

### 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80 和 443** 端口是否开启
3. 若想用域名访问，请先到 **域名控制台** 完成一个域名解析  

### Web 面板使用

下面通过验证面板的几个核心功能的可用性：

#### 登录面板

1. 使用本地电脑浏览器访问网址：*http://服务器公网IP/panel*, 进入登录界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus1-websoft9.png)

2. 输入您的**服务器操作系统账号密码**，登录到面板
   * 用户名：操作系统用户名，例如：root
   * 密码：操作系统用户名对应的密码 

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus2-websoft9.png)

#### 获取账号密码

此步骤可以获取 MySQL、Nginx 代理的账号密码：  

1. 点击面板左侧菜单【初始账号】
2. 查看账号或隐藏账号
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-getpw-websoft9.png)

#### phpMyAdmin

1. 点击面板左侧菜单【phpMyAdmin】
3. 输入 MySQL 数据库账号密码登录
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-phpmyadminlogin-websoft9.png)

#### Nginx 代理

1. 点击面板左侧菜单【Nginx 代理】
3. 输入账号密码后登录，根据提示修改密码，并牢记之
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-nginxproxylogin-websoft9.png)

#### 查看 Java 范例

环境中默认启动了一个 Java 范例，以证明环境可用，同时也可供用户部署新的 Java 应用作为参考。
本地浏览器访问网址：*http://服务器公网IP*, 查看Java范例Jenkins
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus6-websoft9.png)

> Java应用Jenkins 通过`java -jar jenkins`启动

## 常用操作

### 配置域名

前提：准备好IP对应的域名

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://服务器公网IP/panel*, 进入登录界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus1-websoft9.png)

2. 输入操作系统账号密码后登录到后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus2-websoft9.png)

3. 进入登录界面后选择【Nginx代理】菜单
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus5-websoft9.png)

4. 登陆Nginx Proxy Manager，密码通过【初始账号】查看，初次登陆会提示修改邮件和密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus7-websoft9.png)

5. 点击【Proxy Hosts】-> 【Add Proxy Host】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus8-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus9-websoft9.png)

6. 根据自己的域名配置代理设置
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus10-websoft9.png)

7. 浏览器输入域名访问Java应用
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus11-websoft9.png)

### 如何启动自己的Java应用

通过上传新的Java应用metabase，我们来了解创建自己java应用的过程：

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://服务器公网IP/panel*, 进入登录界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus1-websoft9.png)

2. 输入操作系统账号密码后登录到后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus2-websoft9.png)

3. 进入登录界面后选择【Navigator】菜单，将下载好的metabase.jar上传到相应路径
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus12-websoft9.png)

4. 修改配置文件，追加metabase的启动命令和其他参数
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus13-websoft9.png)

5. 登陆Nginx Proxy Manager，点击【Proxy Hosts】，编辑host以及你的metabase的端口
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus14-websoft9.png)

6. 修改容器启动配置文件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus15-websoft9.png)

7. 重新启动运行环境

  ```
  cd /data/apps/runtime && docker compose up -d
  ```

8. 点击Nginx Proxy Manager对应配置的host，metabase应用启动成功
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus16-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus17-websoft9.png)

## 参数

### 网站目录

环境中，你的网站代码存放位置是实际是没有限制的，但为了方便维护，我们给出如下约定：

* 网站存放目录： */data/wwwroot*  
* 示例网站目录： */data/wwwroot/example*  

> 通过 *http://公网IP地址* 访问的就是示例网站 

### 组件路径{#path}

#### Web 服务器{#webserverpath}

* [Apache](./apache#path) 虚拟主机配置文件： */data/config/apache*
* [Nginx](./nginx#path) 虚拟主机配置文件：*/data/config/nginx*
* [Caddy](./caddy#path) 虚拟主机配置文件: */data/config/caddy*

### 端口{#port}

在云服务器中，通过 **[安全组设置](./administrator/firewall#security)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp`查看相关端口，下面列出本应用可能要用到的端口：

| 类型 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 80/443 | Nginx, 通过 HTTP 访问 Express 框架 | 可选 |
| TCP | 9090 | 通过 HTTP 访问 phpMyAdmin | 可选 |
| TCP | 9091 | 通过 HTTP 访问 adminMongo | 可选 |
| TCP | 27017 |MongoDB 端口 | 可选 |
| TCP | 6379 | Redis 端口 | 可选 |
| TCP | 3306 | MySQL/MariaDB 端口 | 可选 |

### 服务{#service}

```
systemctl start | stop | status | restart apache
systemctl start | stop | status | restart nginx
systemctl start | stop | status | restart tomcat
systemctl start | stop | status | restart caddy

systemctl start | stop | status | restart docker
systemctl start | stop | status | restart pm2

systemctl start | stop | status | restart mysql
systemctl start | stop | status | restart mariadb
systemctl start | stop | status | restart mongod
systemctl start | stop | status | restart redis

systemctl start | stop | status | restart rails
systemctl start | stop | status | restart django


docker start | stop | restart phpmyadmin
docker start | stop | restart adminmongo
docker start | stop | restart redis
```

### 版本号{#version}

参考：[通用版本号查询](./administrator/parameter#version)

### 矩阵架构{#matrix}

【Web Server】+【应用程序 Server】+【数据库】+【数据库管理工具】+【应用程序语言环境】组合成为 Web 程序环境。

例如：LAMP = Apache + MySQL + PHP；PHP&JAVA 双能环境=Nginx+Java+PHP+MySQL



下面是矩阵关系表：  


| 类别              | 名称              | 备注 |
| ----------------- | ----------------- | ------------------------------ |
|  Web Server | Apache            |                                |
|                   | Nginx             |                                |
|                   | Caddy             |                                |
| 应用程序 Server   | Tomcat            | 适用于 Java 的应用程序服务器   |
|                   | php-fpm           | 适用于 PHP 的应用程序服务器    |
|                   | uWsgi             | 适用于 Python 的应用程序服务器 |
|                   | Phusion Passenger | 适用于 Ruby 的应用程序服务器   |
| 数据库及管理工具 | MySQL/MariaDB     | Web 可视化管理工具：phpMyadmin |
|                   | MongoDB           | Web 可视化管理工具：adminMongo |
|                   | Redis             |                                |
|                   | SQLite            |                                |
| 应用程序语言环境      | PHP               | 扩展框架： |
|                   | Java              | 扩展框架： |
|                   | Node.js           | 扩展框架：Express, React, Vue, AngularJS,Gatsby.js |
|                   | Python            | 扩展框架：Django |
|                   | Ruby              | 扩展框架：Rails |
|                   | Go                | 扩展框架： |
| 维护工具          | 9Panel            | Websoft9 自行研发的入门向导工具 |

