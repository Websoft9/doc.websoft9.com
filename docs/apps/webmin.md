---
title: Webmin
slug: /webmin
tags:
  - Webmin
  - 虚拟桌面
  - Web 可视化 Linux 管理员工具
---

import Meta from './_include/webmin.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Webmin 后，通过【我的应用】进入它的编辑窗口，在**访问**标签页中获取登录地址和账号。  

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问后，进入登录页面

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

> Webmin 监控的不是云服务器本身，对应的容器内系统主要用作学习使用。其他请参考官方文档：[Webmin Documentation](http://doxfer.webmin.com/Webmin/Main_Page)

### 快速了解

- [Webmin API](https://doxfer.webmin.com/Webmin/The_Webmin_API)

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


## 管理维护{#administrator}

#### 禁用 Webmin 继承系统账号

默认的【Unix验证】 更改为 【设置为】，同时设置新密码和用户

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-usermode-websoft9.png)

### 修改密码

Webmin 默认使用的是服务器 root 账号，修改服务器密码即修改 Webmin 密码。  

故，用 `passwd` 系统命令即可

### 升级

Webmin 提供了可视化的在线升级功能，升级非常方便

![升级](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-upgrade-websoft9.png)


## 故障