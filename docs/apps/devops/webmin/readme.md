---
sidebar_position: 1
slug: /webmin
tags:
  - Webmin
  - 虚拟桌面
  - Web 可视化 Linux 管理员工具
---

# 快速入门

[Webmin](https://www.webmin.com) 是基于 Web 的 Linux/Unix 可视工具，它可以管理 Apache, MySQL等基础环境软件，也可以管理 DNS, FTP, 用户, 防火墙等系统级配置。它的操作有一定的复杂性，适合于系统管理员使用。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-dashboard-websoft9.png)


部署 Websoft9 提供的 Webmin 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启  
3. 若想用域名访问  Webmin，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程
4. 准备好服务器 root 密码（Webmin 直接使用服务器账号登录）


## Webmin 初始化向导

### 详细步骤

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://服务器公网IP*, 进入登录页面

   ![Webmin 登录页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-login-websoft9.png)

2. 输入账号密码，成功登录到 Webmin 后台  

   ![Webmin 登录](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-dashboard-websoft9.png)

3. 设置语言：依次打开菜单【Webmin】>【Change Language and Theme】重设所需的语言

   ![Webmin 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-changelangs-websoft9.png)

4. 系统管理：通过【系统】菜单可以进行系统管理，如修改密码及用户及群组、软件包管理等

   ![Webmin 系统管理](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-system-websoft9.png)

5. 服务器管理：通过【服务器】菜单可以进行服务器管理，如 Apache web服务、SSH服务等

   ![Webmin 服务器管理](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-server-websoft9.png)

5. 文件管理：通过【Tools】>【File Manage】菜单可以进行目录、文件管理，如新建文件夹、上传文件、修改文件的权限等

   ![Webmin 文件管理](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-file-websoft9.png)

6. 点击菜单下方的【>_】图标，进入 SSH 命令行模式（ESC 键取消）

   ![Webmin SSH 模式](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-sshcli-websoft9.png)

7. 完成其他所需的配置

> 需要了解更多 Webmin 的使用，请参考官方文档：[Webmin Documentation](http://doxfer.webmin.com/Webmin/Main_Page)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**服务器使用的是秘钥对，如何登录 Webmin？**   

由于 Webmin 不支持密钥对登录，因此需要用户自行设置 root 密码：
```
sudo su -
passwd 'your password'
```

## Webmin 使用入门

下面以 **通过 Webmin 安装一个 WordPress 网站作**为一个任务，帮助用户快速入门：  

> 需提前将域名解析至服务器

1. 安装 PHP，MySQL 环境 （[参考](./ansible#installrole)）
2. 本地下载 WordPress 源码上传至服务器 */data/wwwroot* 目录，然后在线解压（[参考](#file)）
3. 修改解压后的文件夹拥有者为 www（[参考](#file)）
4. 打开[数据库管理](#db)界面，增加一个名称为 wordpress 的数据库
5. 通过修改 WordPress 的配置文件中数据库相关项目 */data/wwwroot/wordpress/wp-config.php*  
6. 为 WordPress 网站创建一个虚拟主机（[参考](#apachevhost)）
7. 本地浏览器访问：http://域名，测试 WordPress

## 常用操作

### 安装组件

Webmin 应用中除预装 Apache, Docker 之外，没有安装其他组件。 

可通过 Websoft9 提供的 [自动化组件项目](./ansible#installrole) 来安装所需的各种组件：PHP, JDK, Ruby, MySQL 等


### 配置 Apache 虚拟主机{#apachevhost}

Webmin 中可以直接通过可视化的方式配置多个 Apache 虚拟主机，具体如下：  

1. 登录 Webmin 之后，打开：【服务器】>【Apache服务器】

2. 单机【Create virtual host】创建新的虚拟主机，填写配置项，然后点击【创建】

   * 服务端口：80
   * 根文件（目录）: */data/wwwroot/yoursite* 
   * 服务器名称（域名）：*domain.example.com*
   * 选择的配置文件：*/etc/httpd/conf.d/domain.example.com.conf*

   ![Webmin Apache](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-apache-vhost-websoft9.png)

3. 在 Webmin 的终端中可以查看新创建的虚拟主机配置文件

   ![Webmin Apache](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-apache-vhost-conf-websoft9.png)

### 文件管理{#file}

通过【Tools】 > 【File Manage】菜单可以进行文件管理，如文件的上传、下载等

**上传文件**  

选择本地文件夹，点击【file】下拉菜单，选择“上传到当前目录”，完成文件上传

   ![Webmin File](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-ftp-websoft9.png)

**修改文件拥有者**

1. 选中目录，鼠标右键【属性】>【更改所有权】，开始授权

   ![Webmin 修改文件权限](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb04.png)

2. 分别将用户和组都设置为 apache 勾选 Recursive，点击“Change”

   ![Webmin 修改文件权限](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb05.png)

**解压**  

1. 选中软件压缩包，鼠标右键中选择【提取】,文件开始解压

   ![Webmin 解压](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb02.png)

2. 文件解压后，多了1个目录

   ![Webmin 解压](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb03.png)


### 用户管理

通过【系统】 > 【用户与群组】菜单可以进行用户及角色（分组）管理，如新增用户和编辑用户

选择“创建新用户”或点击用户列表中的用户可以实现用户添加和编辑操作。

   ![Webmin File](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-user-websoft9.png)

### 数据库管理{#db}

Webmin 提供了可视化的 MySQL 数据库管理界面，可以很方面的创建和管理数据库：  

1.  打开菜单【服务器】 > 【MySQL数据库服务器】，点击【创建新的数据库】

   ![Webmin MySQL数据库服务器](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb06.png)

2.  设置你的数据库名称，点击【新建】即可

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb07.png)

### 域名绑定

完成 **[域名五步设置](./administrator/domain_step)** 过程中的前四个步骤后，参考下面的步骤完成域名绑定：

1. 登录 Webmin 控制台，打开：【Apache 服务器】>【编辑配置文件】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-confapache001-websoft9.png)

2. 修改 [Apache虚拟机主机配置文件](#path)，将其中的 **ServerName** 项的值修改为你的域名
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-confapache002-websoft9.png)

3. 保存配置文件，重启 [Apache 服务](#service)


### 修改密码

Webmin 默认使用的是服务器 root 账号，修改服务器密码即修改 Webmin 密码。  

故，用 `passwd` 系统命令即可


## 参数

Webmin 应用中包含 Apache, Docker 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。 

下面仅列出 Webmin 本身的参数：

### 路径{#path}

##### Webmin

Webmin 安装目录： */data/apps/webmin*  
Webmin 日志文件： */data/apps/webmin/webmin.log*  
Webmin 模块目录： */data/apps/webmin/modules*  

##### Apache

Apache 虚拟主机配置文件：*/etc/httpd/conf.d/vhost.conf*  
Apache 主配置文件： */etc/httpd/conf/httpd.conf*  
Apache 日志文件： */var/log/httpd*  
Apache 模块配置文件： */etc/httpd/conf.modules.d/00-base.conf*


### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 10000   | Webmin 原始端口，已通过 Apache 转发到 80 端口 | 可选   |

### 版本

```shell
cat /data/apps/webmin/
```

### 服务

```shell
sudo systemctl start | stop | restart | status webmin
```

### 命令行

Webmin 没有提供命令行程序

### API

参考:[Webmin API](https://doxfer.webmin.com/Webmin/The_Webmin_API)

