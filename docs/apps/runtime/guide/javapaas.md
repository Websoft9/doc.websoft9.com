---
sidebar_position: 2
slug: /runtime/javapaas
tags:
  - Java
  - 运行环境
---

# Java PaaS

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

下面通过验证面板的几个核心功能： 

#### 登录面板

1. 使用本地电脑浏览器访问网址：*http://服务器公网IP/panel*, 进入登录界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-cockpitlogin-websoft9.png)

2. 输入您的**服务器操作系统账号密码**，登录到面板
   * 用户名：操作系统用户名，例如：root
   * 密码：操作系统用户名对应的密码 

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-cockpitmonitor-websoft9.png)

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

Nginx 代理是用于给应用配置域名和证书的管理工具：  

1. 点击面板左侧菜单【Nginx 代理】，输入账号密码后登录
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-nginxproxylogin-websoft9.png)

2. 根据提示修改密码，并牢记之
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-nginxproxy-modifypw-websoft9.png)

#### 查看 Java 范例

环境中默认启动了一个 Java 范例，它部署在 java17 容器的 8080 端口上。

本地浏览器访问网址：*http://服务器公网IP* 即可查看，也可以参考下面的 [域名配置](#dns) 给范例可以通过域名访问。  

下面列出部署 Java 范例时的相关配置，可供用户部署其他 Java 应用时参考：  

* 源码路径：*/data/apps/runtime/data/java17/jenkins*  
* Nginx 配置：*/data/apps/runtime/data/nginx_data/nginx/proxy_host/websoft9.conf*  

### 异常处理

若碰到问题，请第一时刻联系 **[技术支持](./../helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./../faq#setup)** 尝试快速解决问题：

## 常用操作

### 部署 Java 应用

本 PaaS 中部署 Java 应用只需要三个步骤：  

1. 上传 Java 程序包到对应的目录：/data/apps/runtime/data/java*
2. 向 **[应用启动配置文件](#path)** 中增加一段启动配置，并重启对应的容器 
3. 在 Nginx 代理中，为应用增加代理设置并配置域名


下面以 **在 Java17 容器下部署 [Metabase](https://www.metabase.com/docs/latest/installation-and-operation/running-the-metabase-jar-file)** 为例，详细介绍部署的具体步骤：  

1. 登录面板，打开【Navigator】菜单，将下载好的 metabase.jar 上传到相应路径

   例如：/data/apps/runtime/data/java17/matabase

2. 修改**[应用启动配置文件](#path)**，追加 Metabase 的启动命令和其他参数
   ```
   [program:metabase]
   command=java -jar metabase.jar --httpPort=8081
   autostart=true
   directory=/data/apps/metabase
   ```
    > directory 中的 **/data/apps**是固定路径，它的后面是应用的相对目录；--httpPort 用于配置域名时对应的 Forward Port 的值

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-metabase-supervisord.jpg)

3. 重启容器环境
  ```
 sudo docker restart java17
  ```

4. 在服务器中运行下面的命令，验证应用是否部署成功
  ```
 docker exec -it nginxproxymanager curl java17:8081
  ```

5. 参考 [域名配置](#dns) 章节，给此应用配置域名后方可访问

> java17 容器下默认已经部署了 Jenkins,所以 Java 环境下多应用案例也可参照上述过程。

### 配置域名{#dns}

完成域名解析后，参考如下域名配置的步骤：  

1. 登录到 Web界面后，然后打开【Nginx代理】>【Proxy Hosts】>【Add Proxy Host】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-addproxy-websoft9.png)

6. 根据自己的域名配置代理设置
    * Domain names: 填写自己的域名（如果没有域名可以填写公网IP）
    * Forward Hostname IP: 填写容器名称
    * Forward Port: 填写容器中应用对应的端口（例如：java17 容器下的 8080 端口）

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-setproxy-websoft9.png)

7. 设置成功，访问域名验证结果

### 启用多 Java 环境

本环境虽然支持 Java8-Java19 等8个环境，但默认只开启了 Java17。  

您如下想开启更多环境，其实非常容易：

1. 登录到 Web界面后，然后打开【容器】管理界面后看到正在运行的容器
2. 点击左上角的容器筛选菜单，选择【所有】，将会看到所有容器
3. 打开一个状态为 exited 的容器，点击【启动】按钮即可

### 停止已部署的 Java 应用

1. 修改**[应用启动配置文件](#path)** 中每个配置段中 **autostart** 项（ture 表示启动，fasle 表示停止）
2. 重启相关容器
  ```
 sudo docker restart java17
  ```

## 参数

### 目录路径{#path}

使用本环境时，部署应用相关的目录有严格的约定：  

* 应用源码存放目录： */data/apps/runtime/data/java* *  
* 应用启动配置文件：*/data/apps/runtime/config/java/supervisord.conf*  

> java* 是 java8, java10 等的统称，java* 容器共用应用启动配置文件。

### 组件{#component}

本 PaaS 平台包括的主要组件：

```
CONTAINER ID   IMAGE                             COMMAND                  CREATED       STATUS                     PORTS                                                                                                             NAMES
f33fbf16d9b1   phpmyadmin:latest                 "/docker-entrypoint.…"   3 hours ago   Up 3 hours                 0.0.0.0:9090->80/tcp, :::9090->80/tcp                                                                             phpmyadmin
db0afd15e660   runtime-java19                    "bash -c 'cat /opt/c…"   3 hours ago   Exited (137) 3 hours ago                                                                                                                     java19
b1a02aaddeee   mysql:5.7                         "docker-entrypoint.s…"   3 hours ago   Up 3 hours                 3306/tcp, 33060/tcp                                                                                               runtime-mysql
c2f12e170d71   runtime-java11                    "bash -c 'cat /opt/c…"   3 hours ago   Exited (137) 3 hours ago                                                                                                                     java11
5e664aef4e8d   runtime-java8                     "bash -c 'cat /opt/c…"   3 hours ago   Exited (137) 3 hours ago                                                                                                                     java8
b48e522fe1ff   runtime-java15                    "bash -c 'cat /opt/c…"   3 hours ago   Exited (137) 3 hours ago                                                                                                                     java15
e8740cb91365   runtime-java13                    "bash -c 'cat /opt/c…"   3 hours ago   Exited (137) 3 hours ago                                                                                                                     java13
455f9e6d866d   jc21/nginx-proxy-manager:latest   "/init"                  3 hours ago   Up 3 hours                 0.0.0.0:80->80/tcp, :::80->80/tcp, 0.0.0.0:443->443/tcp, :::443->443/tcp, 0.0.0.0:9001->81/tcp, :::9001->81/tcp   nginxproxymanager
e344b8a23cce   runtime-java17                    "bash -c 'cat /opt/c…"   3 hours ago   Up 3 hours                                                                                                                                   java17
5f92341a21b7   runtime-java14                    "bash -c 'cat /opt/c…"   3 hours ago   Exited (137) 3 hours ago                                                                                                                     java14
0f29bd3fe192   runtime-java18                    "bash -c 'cat /opt/c…"   3 hours ago   Exited (137) 3 hours ago                                                                                                                     java18
```

* 服务器面板：[Cockpit](../cockpit)
*  Java 环境：Java8 Java11 Java13 Java14 Java15 Java17 Java18 Java19 等8个版本
* 数据库： MySQL5.7
* 数据库管理工具：[phpMyAdmin](../mysql#phpmyadmin)
* Nginx 代理：Nginx Proxy Manager

### 端口{#port}

在云服务器中，通过 **[安全组设置](./../administrator/firewall#security)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp`查看相关端口，下面列出本应用可能要用到的端口：

| 类型 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 80/443 | Nginx, 通过 HTTP 或 HTTPS 访问应用 | 必选 |
| TCP | 3306 | MySQL/MariaDB 端口 | 可选 |

### 服务{#service}

```
systemctl start | stop | status | restart cockpit

docker start | stop | restart java17
docker start | stop | restart phpmyadmin
docker start | stop | restart runtime-mysql
docker start | stop | restart nginxproxymanager 
```

### 版本号{#version}

参考：[通用版本号查询](./../administrator/parameter#version)


