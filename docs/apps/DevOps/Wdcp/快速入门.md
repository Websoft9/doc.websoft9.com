---
sidebar_position: 1
slug: /wdcp
tags:
  - WDCP
  - DevOps
---

# 快速入门

[WDCP](https://www.wdlinux.cn/wdcp/) 是国内知名的 Linux 面板和主机管理系统，自带LAMP（LNMP），支持PHP多版本自由切换，功能全面，包括管理文件、查看日志、配置应用服务器、备份数据库、配置域名等，被广泛用于多网站管理与维护。

![](https://oss.aliyuncs.com/netmarket/product/bce9a597-71dd-4692-8166-236b8bb08c8b.png)

## 演示

WDCP 官网提供了试用环境，您可以直接试用

* 演示地址：https://www.wdlinux.cn/wdcp/demo.html

> 免责说明：此处仅提供 WDCP 官方的演示，不保证与 Websoft9 部署包功能完全一致，若演示过程中若需要填写个人资料、获取Cookie等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此可能存在的商业纠纷与我司无关。


在云服务器上部署 WDCP 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问网站，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

使用 WDCP，可能会用到的几组账号密码如下：

### WDCP 

管理员用户名：admin  
管理员密码：websoft9

### MySQL账号和密码：

MySQL 的 root 账户默认密码已优化为强随机密码，查看方式：

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  
>[danger] 默认的 “wdlinux.cn” 请务必修改为强密码，类似于：f@N7eUUm25xAjP!$ ，这样有助于提高数据库的安全性，减少数据库密码被破解的风险。
> 需要登录MySQL，请参考 [MySQL可视化管理](#MySQL-数据管理)


## WDCP 入门向导

使用浏览器访问 http://服务器公网IP:8080 ，即可进入WDCP面板。为了能够正常使用WDCP，请务必在服务器安全组中开启如下端口：

* 8080端口：WDCP访问入口
* 21端口：FTP入口
* 443端口：https入口
* 80端口：http入口

### 启用PHP版本

WDCP支持PHP多版本，默认情况下，面板没有启动任何版本的PHP，需要手工启动其中之一或多个，具体如下：

* 登录WDCP->网站管理->PHP版本管理，选一个版本点击“启动”按钮即可
 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wdcp/wdcp-enablephp-websoft9.png)
* 如果要设置开机启动，请点击自启动设置

### 修改WDCP默认密码

建议第一次登录WDCP后立即修改默认密码，具体如下：

* 登录WDCP->admin（右上角）->修改密码 
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wdcp/wdcp-adminpw-websoft9.png)
* 修改密码后，请立即重新登录，以验证修改密码操作是成功的

### 修改数据库root密码

建议第一次登录WDCP后立即修改数据库root密码

* 登录WDCP->MySQL管理->修改密码
* 修改密码后，请立即通过phpMyAdmin登录，以验证修改密码操作是成功的


## 常用操作

### WDCP安装网站

在WDCP中新增一个网站的步骤包括：

1. 域名解析成功（WDCP中安装网站必须对应的域名，无域名或没有备案是不可以安装网站的）
2. WDCP面板中完成增加站点信息、站点FTP、站点数据库以及其他
3. 上传网站代码，并设置好权限和用户组
4. 通过访问域名进入网站的安装向导，完成网站安装

下面以WordPress为例，演示网站的安装方法（假设已经完成了域名解析）：

### # 第一步：WDCP面板中完成增加站点信息

1. 网站管理-创建站点，填写已经解析好了域名（即访问域名显示本镜像的引导页面），然后选择php7.0版本 
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wdcp/wdcp-create001-websoft9.png)
2. 建议开启FTP账号，用户名和密码自行设置
3. 创建数据库名、用户名和密码（Wordpress安装的时候不能自行生成数据库，因此在此处先创建） 
 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wdcp/wdcp-create002-websoft9.png)
4. 绑定域名：如果还需绑定额外域名，请在此项中填写
5. 其他项一般无需填写
6. 点击“提交”，完成站点信息创建

####  第二步：上传网站代码，并设置好权限和用户组

1. 如果第一步成功，打开你的域名，系统会有代码上传和FTP使用提示
2. 以WinSCP为例，FTP参数填写如下 
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wdcp/wdcp-create003-websoft9.png)
3. 本此常见的的网站为FTP根目录下的public_html，即将WordPress代码上传到这个目录下（先删除默认的index.html） 
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wdcp/wdcp-create004-websoft9.png)

####  第三步：通过访问域名进入网站的安装向导，完成网站安装

1. 如果第二步没有问题，系统会进入WordPress安装界面
2. 数据库参数填写请使用WDCP面板中创建网站时所设置的 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wdcp/wdcp-create005-websoft9.png)

### 域名绑定

在WDCP中，新增网站首先就要填写域名。如果是修改网站，先删除旧域名，然后再增加域名

### SSL/HTTPS

### SMTP

应用中发送邮件是一个很常见的功能。经过大量用户实践反馈，只推荐一种发邮件的方式，即安装邮件插调用第三方邮件系统的STMP相关账号来进行邮件发送。

SMTP发送邮件有三个步骤：

1. 申请一个可用的[SMTP服务](http://service.mail.qq.com/cgi-bin/help?id=28)（例如：stmp.qq.com，端口号465，账号...）
2. 打开应用软件中的SMTP配置界面（类似WordPress默认没有SMTP配置项，则需要额外安装一个SMTP插件）
3. 测试SMTP

> 请忘掉在本机上安装sendmail等邮件服务器的方案，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，导致不稳定、不容易维护、不好诊断问题。

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

## 异常处理

#### 浏览器打开IP地址，无法访问 WDCP（白屏没有结果）？

使用浏览器访问 http://服务器公网IP:8080 ，进入WDCP面板。

您的服务器对应的安全组8080端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

