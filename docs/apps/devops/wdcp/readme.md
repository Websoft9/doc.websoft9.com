---
sidebar_position: 1
slug: /wdcp
tags:
  - WDCP
  - DevOps
---

# 快速入门

[WDCP](https://www.wdlinux.cn/wdcp/demo.html) 是一个老牌的 Linux 面板和主机管理系统，自带LAMP（LNMP），支持 PHP 多版本自由切换，功能全面，包括管理文件、查看日志、配置应用服务器、备份数据库、配置域名等，被广泛用于多网站管理与维护。

![](https://oss.aliyuncs.com/netmarket/product/bce9a597-71dd-4692-8166-236b8bb08c8b.png)

部署 Websoft9 提供的 Jenkins 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80, 8080, 21** 端口已经开启
3. 在服务器中查看 WDCP 的 **[默认账号和密码](./setup/credentials)**  
4. 若想用域名访问  WDCP，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程


管理员用户名：admin  
管理员密码：websoft9

## WDCP 初始化向导

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入登录页面

2. 输入默认账号密码（**[查看](./setup/credentials)** ），登录成功后，到 admin（右上角）->修改密码 
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wdcp/wdcp-adminpw-websoft9.png)
* 修改密码后，请立即重新登录，以验证修改密码操作是成功的

3. 网站管理->PHP版本管理，选一个版本点击“启动”按钮
 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wdcp/wdcp-enablephp-websoft9.png)

4. MySQL管理->修改密码 

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## WDCP 使用入门

下面以 **WDCP 安装网站** 作为一个任务，帮助用户快速入门：

在WDCP中新增一个网站的步骤包括：

1. 域名解析成功（WDCP中安装网站必须对应的域名，无域名或没有备案是不可以安装网站的）
2. WDCP面板中完成增加站点信息、站点FTP、站点数据库以及其他
3. 上传网站代码，并设置好权限和用户组
4. 通过访问域名进入网站的安装向导，完成网站安装

下面以WordPress为例，演示网站的安装方法（假设已经完成了域名解析）：

##### 第一步：WDCP面板中完成增加站点信息

1. 网站管理-创建站点，填写已经解析好了域名（即访问域名显示本镜像的引导页面），然后选择php7.0版本 
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wdcp/wdcp-create001-websoft9.png)
2. 建议开启FTP账号，用户名和密码自行设置
3. 创建数据库名、用户名和密码（Wordpress安装的时候不能自行生成数据库，因此在此处先创建） 
 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wdcp/wdcp-create002-websoft9.png)
4. 绑定域名：如果还需绑定额外域名，请在此项中填写
5. 其他项一般无需填写
6. 点击“提交”，完成站点信息创建

#####  第二步：上传网站代码，并设置好权限和用户组

1. 如果第一步成功，打开你的域名，系统会有代码上传和FTP使用提示
2. 以WinSCP为例，FTP参数填写如下 
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wdcp/wdcp-create003-websoft9.png)
3. 本此常见的的网站为FTP根目录下的public_html，即将WordPress代码上传到这个目录下（先删除默认的index.html） 
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wdcp/wdcp-create004-websoft9.png)

#####  第三步：通过访问域名进入网站的安装向导，完成网站安装

1. 如果第二步没有问题，系统会进入WordPress安装界面
2. 数据库参数填写请使用WDCP面板中创建网站时所设置的 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wdcp/wdcp-create005-websoft9.png)

## 常用操作

### 升级PHP版本

在已有安装WDCP默认面板的前提下，PHP 版本默认为 5.2.x 或5.3.x ，如果想要升级版本到 5.6，可远程连接到服务器执行以下命令（其他版本修改 php_up56.sh 为对应的 版本号即可）：

    wget https://soft.itbulu.com/wdcp/php_up56.sh
    sh php_up56.sh

### 升级 MySQL 版本

在升级之前，**请务必做好数据备份以避免数据丢失**，如果有网站环境，最好先停掉MYSQL数据库服务，然后再执行升级。
   

    wget https://soft.itbulu.com/wdcp/mysql_up55.sh
    sh mysql_up55.sh
执行过程中，会出现类似这样的错误：

    ERROR! MySQL server PID file could not be found!
    Starting MySQL. ERROR! The server quit without updating PID file (/www/wdlinux/mysql-5.5.36/data/MyCloudServer.pid).

这个问题需要通过修改配置文件解决：

    vi /www/wdlinux/init.d/mysqld

找到下面两行：

    basedir=
    datadir=

然后替换成：

    basedir=/www/wdlinux/mysql-5.5.27
    datadir=/www/wdlinux/mysql-5.5.27/var
    
或者替换成：

    basedir=/www/wdlinux/mysql
    datadir=/www/wdlinux/mysql/var

## 参数

WDCP 应用中包含 Docker, PHP, MySQL 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。  

下面仅列出 WDCP 本身的参数：

### 路径{#path}

* 网站根目录：*/www/web*
* 备份目录：*/www/backup* 
* 日志目录：*/www/weblogs*
* 运行环境:*PHP5.4~7.1,Apache2.4,Nginx 1.8*
* PHP配置文件:*/www/wdlinux/etc/php.ini*
* nginx证书文件：*/www/wdlinux/nginx/conf/cert*
* apache证书文件：*/www/wdlinux/apache/conf/cert* 

### 端口

无特殊端口

### 版本

控制台查看

### 服务

无

### 命令行

无

### API

无


