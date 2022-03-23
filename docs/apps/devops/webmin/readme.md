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
3. 若想用域名访问  Webmin，务必先完成 **[域名五步设置](./dns#domain)** 过程
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

### 准备环境

WordPress 基于PHP 和 MySQL 技术栈，web 服务器使用Apache 。本部署方案中默认已经安装 Apache，还缺少 PHP 和 MySQL。  

PHP 和 MySQL 的安装是比较麻烦的，所幸，我们可以使用 Websoft9 提供的自动化脚本完成安装

> 可能会因网络原因，git clone 从 github 站下载时会有异常，可以多尝试几次

1. 运行下面的命令，安装 PHP，本次安装的 WordPress 是 5.8 ，需要 PHP7.4 支持，因此版本选择 7.4 
   ```
   git clone https://github.com/Websoft9/role_php.git
   ansible-playbook role_php/tests/test.yml
   ```

2. 运行下面的命令，安装 MySQL，其中版本选择 5.7
   ```
   git clone https://github.com/Websoft9/role_mysql.git
   ansible-playbook role_mysql/tests/test.yml
   ```
   > 请记住 MySQL 安装时设置的登录密码。如没有设置，默认密码为：123456 ，请及时修改为更为复杂的强密码。

3. 登录到 Webmin 后台，点击左侧菜单下方的【刷新模块】按钮，在【服务器】菜单下可以看到【MySQL数据库服务器】


### 上传源码

先下载 WordPress 到本地，然后上传、解压、修改文件权限。

1. 通过菜单打开【Tools】>【File Manager】 选择进入/data/wwwroot 目录，点击“File”下拉菜单，选择“Upload to current directory”完成wordpress压缩包上传：

   ![Webmin 上传](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb01.png)


### 配置虚拟主机

配置虚拟主机，需提前将域名解析到服务器。解析成功后，参考下面配置完成虚拟主机设置：

1. 打开菜单【服务器】 > 【Apache服务器】，点击“Create virtual host”。

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb08.png)

2. 点击右上角按钮，使域名设置生效：

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb09.png)

3. 本地浏览器访问：http://域名，测试 WordPress

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb10.png)

### 配置数据库

为 WordPress 连接数据库。
通过FTP工具（这里是用 WinSCP）连接到服务器，找到 WordPress 的配置文件 /data/wwwroot/wordpress/wp-config.php，修改数据库连接信息（** 密码是上面安装MySQL时设置的密码 **），并保存。

   ![Webmin 连接数据库](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb071.png)


## 常用操作

### 安装组件

Webmin 应用中除预装 Apache, Docker 之外，没有安装其他组件。  


### 配置 Apache 虚拟主机

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

### 文件管理

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

### 数据库管理

Webmin 提供了可视化的 MySQL 数据库管理界面，可以很方面的创建和管理数据库：  

1.  打开菜单【服务器】 > 【MySQL数据库服务器】，点击【创建新的数据库】

   ![Webmin MySQL数据库服务器](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb06.png)

2.  设置你的数据库名称，点击【新建】即可

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb07.png)

### 域名绑定

完成 **[域名五步设置](./dns#domain)** 过程中的前四个步骤后，参考下面的步骤完成域名绑定：

1. 登录 Webmin 控制台，打开：【Apache 服务器】>【编辑配置文件】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-confapache001-websoft9.png)

2. 修改 [Apache虚拟机主机配置文件](#path)，将其中的 **ServerName** 项的值修改为你的域名
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-confapache002-websoft9.png)

3. 保存配置文件，重启 [Apache 服务](#service)


### 修改密码

Webmin 默认使用的是服务器 root 账号，修改服务器密码即修改 Webmin 密码。  

故，用 `passwd` 系统命令即可


## 参数

**[通用参数表](../setup/parameter)** 中可查看 Apache, Docker 等 Webmin 应用中包含的基础架构组件路径、版本、端口等参数。 

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

### API