---
sidebar_position: 1
slug: /codeserver
tags:
  - code-server
  - 在线编辑器
---

# 快速入门

[code-server](https://github.com/cdr/code-server) 是一个由第三方公司开发的浏览器版本的 VS Code，可以直接通过浏览器进行开发，由于后端运行在服务器中，其运行效率高的同时又非常便捷。

![code-server 界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-consolegui-websoft9.png)


在云服务器上部署 code-server 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 code-server，请先到 **域名控制台** 完成一个域名解析


## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

## code-server

* 管理员账号: `无`
* 管理员密码: 存储在您的服务器中的文件中 */credentials/password.txt*

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

### MongoDB

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  


## code-server 安装向导

1. 使用本地 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入登录页面
   ![code-server 登录界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-login-websoft9.png)

2. 输入密码（[不知道账号密码？](/zh/stack-accounts.md#codeserver)），成功登录到 code-server 后台  
   ![code-server 后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-consolegui-websoft9.png)

3. 在 code-server 界面上打开 workspace 文件夹  
   ![code-server 打开项目目录](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-openfolder-websoft9.png)
   > 默认存放代码的根目录为：*/data/wwwroot/codeserver/volumes/config/workspace*  

4. 打开 Terminal，查看系统环境（默认已安装 Node, Yarn等）
   ![code-server 打开Terminal](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-terminal-websoft9.png)

5. 参考[配置环境](/zh/solution-runtime.md)章节，安装更多开发所需的组件。

## code-server 入门向导

下面以 Python 开发为范例，介绍如何使用 code-server：

1. 登录 code-server，在当前 WorkSpace 下克隆一个代码仓库
   ```
   git clone https://github.com/Websoft9/ansible-wordpress.git
   ```
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-gitclone-websoft9.png)

2. 在项目文件夹中新建一个文件，命名为：myfile.py，并拷贝下面的 Python 程序实例代码。
   ```
   #!/usr/bin/env python2
   #!/usr/bin/env python3
   #coding: utf-8

   import os, io, sys

   print("hello world")
   ```
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-createfile-websoft9.png)

3. 在【窗口的终端栏】中执行 `python myfile.py` 命令，运行 Python 程序
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-runpython-websoft9.png)

4. 查看正确的输出结果

> 需要了解更多 code-server 的使用，请参考官方文档：[code-server Documentation](https://hub.docker.com/r/linuxserver/code-server)

## 常用操作

### 配置环境

code-server 容器默认已经运行 Node, Yarn, Git等工具，可以很方便的配合 code-server 进行 Node 相关程序的开发。  

#### 安装组件

若默认环境不符合需求，可以直接通过 **code-server 控制台**安装组件，下面以 JAVA 为例进行说明：

1. 登录 code-server 控制台，在【Terminal】窗口中运行 `sudo su` 切换为 root 用户
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-sudosu-websoft9.png)
   > 密码为 code-server 控制台登录密码

2. 更新 apt 仓库
   ```
   apt update
   ```

3. 安装并验证 Java
   ```
   #1 安装JRE
   apt-get install openjdk-8-jre

   #2 验证版本
   java -version
   ```

#### 备份环境

由于 code-server 基于容器运行，如果你打算将容器安装后的环境长期的备份下来，需要参考如下方式创建自定义容器镜像：

1. 登录服务器
2. 运行创建命令命令（基于 codeserver 容器创建一个名称为 codeserver-java 的镜像）
   ```
   #1 创建镜像
   sudo docker commit -m "add java" -a "your name" codeserver codeserver-java:latest

   #2 查看镜像
   sudo docker image ls
   ```

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

code-server 域名绑定操作步骤：

1. 确保域名解析已经生效  
2. 使用 SFTP 工具登录云服务器
3. 修改 [Nginx虚拟机主机配置文件](/维护参考.md#nginx)，将其中的 **server_name** 项的值修改为你的域名
   ```text
   server
   {
   listen 80;
   server_name codeserver.yourdomain.com;  # 此处修改为你的域名
   ...
   }
   ```
4. 保存配置文件，重启 [Nginx 服务](/维护参考.md#nginx-1)

### 重置密码

code-server 无法通过控制台直接修改密码，必须通过重置容器的方式修改密码：

1. 修改 code-server 的 [.env 文件](zh/stack-components.md#code-server)中 **APP_PASSWORD** 的值
   ```
   APP_VERSION=latest
   APP_PORT=9001
   APP_PASSWORD=123456
   ```
2. 重置 code-server 容器后生效
   ```
   sudo docker-compose -f /data/wwwroot/codeserver/docker-compose.yml up -d
   ```

> 重置密码会重新创建容器，即用户额外安装的组件会丢失

### 修改端口

方案与重置密码类似，唯一不同的是需要修改的是 **APP_PORT** 变量的值。

### 多开发者

当前部署方案默认只有一个 code-server，由于它并不支持多用户，所以不合适多开发协同工作的场景。  

那么如何才能支持多开发者协作使用 code-server 呢？从宏观上设计，需多开发者使用，每一名开发者分配如下资源即可实现此需求：

1. 单独分配一个宿主机的端口
2. 单独分配一个 code-server 目录
3. 单独运行一个 code-server 容器

下面是一个范例：

1. 运行下面的命令，将现有的 code-server 整个目录复制一份，命名为：/data/wwwroot/user1
   ```
   # 复制
   cd /data/wwwroot
   cp -r codeserver user1

   # 删除持久数据
   rm -rf user1/volumes
   ```

2. 修改 */data/wwwroot/user1/.env* 文件中的 APP_PORT、APP_PASSWORD、APP_CONTAINER_NAME，然后保存
   ```
   APP_PORT=9001
   APP_PASSWORD=123456
   APP_CONTAINER_NAME=codeserver
   ```
   > APP_PORT和APP_CONTAINER_NAME 必须与当前已经存在的 code-server 容器不同名称，否则无法创建


3. 启动新的 code-server 项目
   ```
   cd /data/wwwroot/user1
   sudo docker-compose  up -d
   ```

由于多用户协同开发有诸多个性化需求，无法在以上方案中一一列出，欢迎提出更多需求。

### DevOps

本部署方案默认已经安装 Docker，用户可以基于 Docker 安装 更多的 DevOps 原生应用，包括：

* Jenkins
* Gitlab


### SSL/HTTPS

必须完成[域名绑定](/zh/solution-more.md)且可通过 HTTP 访问 code-server ，才可以设置 HTTPS。

code-server 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。因此，除了虚拟主机配置文件之外，HTTPS 设置则不需要修改 Nginx 其他文件。

#### 自动部署

如果没有申请证书，只需在服务器中运行一条命令`sudo certbot`便可以启动免费证书**自动**申请和部署

```
sudo certbot
```

#### 手动部署

如果你已经申请了证书，只需三个步骤，即可完成 HTTPS 配置

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到 *server{ }* 中
 ``` text
   #-----HTTPS template start------------
   listen 443 ssl; 
   ssl_certificate /data/cert/xxx.crt;
   ssl_certificate_key /data/cert/xxx.key;
   ssl_trusted_certificate /data/cert/chain.pem;
   ssl_session_timeout 5m;
   ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
   ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
   ssl_prefer_server_ciphers on;
   #-----HTTPS template end------------
   ```
3. 重启[Nginx服务](/维护参考.md#nginx)

#### 专题指南

若参考上面的**快速指南**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

《HTTPS 专题专题》方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### MongoDB 数据管理

code-server 预装包中内置 MongoDB 及可视化数据库管理工具 `adminMongo` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组9091端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9091*，进入adminMongo
  ![登录adminMongo](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/adminmongo-connect001-websoft9.png)

3. 输入数据库用户名和密码([不知道密码？](#账号密码))

4. 开始管理数据库
  ![adminMongo](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/adminmongo-connect003-websoft9.png)

> 阅读Websoft9提供的 [《MangoDB教程》](https://support.websoft9.com/docs/mongodb/zh/solution-gui.html) ，掌握更多的MongoDB实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

### MySQL 数据管理

code-server 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组9090端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等


## 异常处理

#### 浏览器打开IP地址，无法访问 code-server（白屏没有结果）？

您的服务器对应的安全组 80 端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署方案中 code-server 是如何安装的？

本部署方案中的 code-server 基于 Docker 安装，实现开发环境与宿主机隔离。

#### code-server 创建文件出现文件权限不足的问题？

如果上传的文件存在一些文件权限需要修正。运行如下命令即可解决文件权限问题：

```
chown -R docker.docker /data/wwwroot/codeserver/volumes/config/workspace
```