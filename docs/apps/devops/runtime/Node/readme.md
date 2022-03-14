---
sidebar_position: 1
slug: /runtime/nodejs
tags:
  - Node.js
  - Node
  - 运行环境
---

# 快速入门

[Node.js](https://nodejs.org/) 是一个Javascript运行环境(runtime)。 实际上它是对Google V8引擎进行了封装。V8引 擎执行Javascript的速度非常快，性能非常好。Node.js对一些特殊用例进行了优化，提供了替代的API，使得V8在非浏览器环境下运行得更好。Node.js是一个基于Chrome JavaScript运行时建立的平台， 用于方便地搭建响应速度快、易于扩展的网络应用。Node.js 使用事件驱动， 非阻塞I/O 模型而得以轻量和高效，非常适合在分布式设备上运行数据密集型的实时应用。  


![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nodejs/nodejs-stackgui-websoft9.png)

在云服务器上部署 Node.js 运行环境 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Node.js 运行环境，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

## MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  
  
> 需要登录MySQL，请参考 [MySQL可视化管理](#mysql-数据管理)

## MongoDB

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

> 需要登录 MongoDB，请参考 [MongoDB可视化管理](#mongodb-数据管理)


## Ruby 安装向导


1. 使用本地 Chrome 或 Firefox 浏览器访问网址：*http://Internet IP*, 显示Express的欢迎页面
1. 使用本地 Chrome 或 Firefox 浏览器访问网址：*http://Internet IP/9panel*, 就进入引导页面
   ![9panel](https://libs.websoft9.com/Websoft9/DocsPicture/zh/9panel/9panelmain-websoft9.png)

3. 通过 9Panel 可以快速了解镜像基本情况，管理数据库，找到帮助文档，寻求人工支持

## 登录数据库

Node.js 运行环境 预装包中内置 MongoDB, MySQL 及可视化数据库管理工具 

* [登录 MySQL](#mysql-数据管理) 管理用户和数据库
* [登录 MongoDB](#mongodb-数据管理) 管理用户和数据库

![9panel](https://libs.websoft9.com/Websoft9/DocsPicture/zh/9panel/9panel-mysql-websoft9.png)

## 常用操作

### 安装网站

在 Node.js 环境上安装一个网站（应用），也就是我们常说的增加一个虚拟主机。

全局上看，只需三个步骤：**上传网站代码** + **运行NPM命令** + [**虚拟机主机配置文件**](/zh/stack-components.md#nginx) **中增加 server{} 配置段**

> server{} 又称之为虚拟主机配置段，每个网站必定在 default.conf 中对应唯一的 server{}。

#### 准备

安装网站之前，请了解如下几个要点，做好准备工作

*  虚拟机主机配置文件：*/etc/nginx/conf.d/default.conf* 
*  连接工具：使用 WinSCP 连接服务器，它包含文件管理、运行命令两方面功能
*  域名：若需要使用域名，请确保备案后的域名成功解析到服务器IP
*  数据库：网站安装向导过程中可能需要使用 [MongoDB]((#mongodb-数据管理) 和 [MySQL]((#mysql-数据管理) 数据库

有一个全局认知并完成准备工作之后，我们开始部署网站

#### 删除示例

本部署方案默认已经安装并启动了[Express框架](https://www.expressjs.com.cn/)，我们先删除它：

1. 运行 `npm list` 查询正在运行的Node.js程序
   ```
   ┌────┬────────────────────┬──────────┬──────┬───────────┬──────────┬──────────┐
   │ id │ name               │ mode     │ ↺    │ status    │ cpu      │ memory   │
   ├────┼────────────────────┼──────────┼──────┼───────────┼──────────┼──────────┤
   │ 0  │ www                │ fork     │ 0    │ online    │ 0.1%     │ 48.7mb   │
   ```
2. 运行 `pm2 delete 0` 删除程序
3. 运行 `pm2 save`
4. 删除项目文件夹 `rm -rf /data/wwwroot/express.example.com`
5. 删除初始化
   ```
   //delete the PM2 init script
   pm2 unstartup systemd

   //delete the have been saved PM2 file of process
   rm -rf /root/.pm2
   ```


#### 安装Express

下面我们还原Express的安装过程：

1. 创建目录
   ```
   mkdir myapp
   cd myapp
   ```
2. 创建Express应用骨架
   ···
   npx express-generator
   ···
3. 安装依赖包
   ```
   npm install
   ```
4. 启动应用程序，通过：*http://服务器公网IP:3000* 访问应用
   ```
   DEBUG=myapp:* npm start
   ```

> 你也可以使用pm2管理应用程序


#### 常见问题

##### 访问刚安装的网站，页面显示 “没有权限...” ？

运行一条修改文件权限的命令
~~~
chown -R nginx.nginx /data/wwwroot
~~~

##### 修改 default.conf 文件之后，Nginx 服务无法启动？

一般是 server{ } 中虚拟主机的目录位置不正确导致

##### 新增网站不可访问，且导致其他网站都不可访问？

一般是 server{ } 中虚拟主机的目录位置不正确导致 Nginx 无法启动

##### 打开新增的网站，显示404错误？

一般是网站目录下没有 index.php 或 index.html 等默认首页导致

##### 新增的网站，显示 500 Internal Server Error？

程序代码错误，需要查看程序的日志文件

### 使用 NPM

NPM 是随同 Node.js 一起安装的包管理工具，能解决NodeJS代码部署上的很多问题，常见的使用场景有以下几种：

* 允许用户从NPM服务器下载别人编写的第三方包到本地使用。
* 允许用户从NPM服务器下载并安装别人编写的命令行程序到本地使用。
* 允许用户将自己编写的包或命令行程序上传到NPM服务器供别人使用。

由于新版的nodejs已经集成了npm，所以之前npm也一并安装好了。同样可以通过输入 "npm -v" 查询版本

运行下面的命令，升级 NPM
```
sudo npm install npm -g
```

### 使用 PM2

PM2是一个用于管理Node.js的进程管理工具。本部署方案默认已经安装了PM2，如果你的服务器没有安装PM2，请参加下面的命令全局安装它：
```
npm install -g pm2
```

进入到项目的根目录，例如：`cd /data/wwwroot/project`， 开始使用pm2管理你的Node.js应用

```
# 启动进程/应用  
pm2 start bin/www 或 pm2 start app.js

# 重命名进程/应用  
pm2 start app.js --name wb123

# 添加进程/应用 
watch  pm2 start bin/www --watch

# 结束进程/应用  
pm2 stop www

# 结束所有进程/应用  
pm2 stop all

# 删除进程/应用  
pm2 delete www

# 删除所有进程/应用  
pm2 delete all

# 列出所有进程/应用  
pm2 list

# 查看某个进程/应用具体情况  
pm2 describe www

# 查看进程/应用的资源消耗情况  
pm2 monit

# 查看pm2的日志  
pm2 logs

# 若要查看某个进程/应用的日志,使用  
pm2 logs www

# 重新启动进程/应用  
pm2 restart www

# 重新启动所有进程/应用  
pm2 restart all
```

### 使用 NVM

[NVM](https://github.com/creationix/nvm), Node 版本管理 - 管理多个活动 node.js 版本的简单 bash 脚本

#### 为什么使用 NVM

由于 npm 和 node.js 产品由不同的实体管理，因此更新和维护可能会变得复杂。 此外，Node.js 安装过程会将 npm 安装在仅具有本地权限的目录中。 当您尝试全局运行包时，这可能会导致权限错误。

为了解决这两个问题，许多开发人员选择使用_node version manager_或_nvm_来安装npm。 版本管理器将避免权限错误，并解决更新 Node.js 和 npm 的复杂性。<br />此外，开发人员可以使用 nvm 在多个版本的 npm 上测试他们的应用程序。 nvm 使您能够轻松切换 npm 以及节点版本。 这样可以更轻松地确保您的应用程序适用于大多数用户，即使他们使用的是其他版本的 npm。 如果您决定安装版本管理器，请使用您选择的版本管理器的说明来了解如何切换版本，并了解如何与最新版本的 npm 保持同步。 

#### 安装和更新 NVM 脚本

**安装**或**更新** nvm，您可以使用 [安装脚本](https://github.com/creationix/nvm/blob/v0.34.0/install.sh) 使用 cURL：

```shell
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash
```

or Wget:

```shell
wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash
```

`~/.nvm``~/.bash_profile``~/.zshrc``~/.profile``~/.bashrc`

#### 使用 NVM

要下载、编译和安装最新版本的  Node，请执行以下操作：

```shell
nvm install node # "node" is an alias for the latest version
```
要安装特定版本的  Node:

```shell
nvm install 6.14.4 # or 10.10.0, 8.9.1, etc
```

安装的第一个版本成为默认版本。 新的 shell 将以弄得的默认版本开始（例如，`nvm alias default`）。

您可以使用 ls-remote 列出可用版本：
```shell
nvm ls-remote
```

然后在任何新的 shell 中使用已安装的版本：
```shell
nvm use node
```

或者直接运行：
```shell
nvm run node --version
```

或者，使用所需版本的 Node 在子 shell 中运行：

您还可以获取可执行文件的安装路径：
```shell
nvm which 5.0
```

### Node.js 应用示例（集）

#### Ghost

Ghost(ghost.org)是由WordPress前员工创建，系统基于Node.JS开发的开源内容管理系统（CMS），界面简洁、现代、美观，代码优雅。继承了WordPress的一些特征，如短代码、固定链接、在线主题修改等，去掉了WordPress复杂的部分，显得更为简洁，官方的Marketplace可以提供大量免费或付费的精美主题。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ghost/ghostui.jpg)

##### 获取Ghost镜像
镜像需要与服务器配套使用，获取Websoft9的镜像有两种方式： 
* 方式一：若没有可用的云服务器，登录主流云厂商的云市场，找到由Websoft9提供的“Ghost博客系统”相关免费镜像，点击“购买”（同时会配套购买云服务器，若只打算试用请选择“**按量**”方式购买，实现按小时使用，接近免费） 
* 方式二：若有可用的云服务器，登录到云厂商的控制面板，找到可用的云服务器，通过关机-&gt;更换系统盘（重装镜像）,在更换过程中选取云市场镜像，获取本镜像

##### 验证Ghost

待镜像购买或更换完成后，镜像会自动安装到配套的云服务器上，当云服务实例处于“运行中”后，通过浏览器访问网址 http://服务器公网IP/， 正常会出现Ghost前台界面： ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ghost/ghost-bootpage-websoft9.png)

如果浏览器访问以上网址没有任何反应，请检查您的安全组设置，确保80端口是开放的。

##### Ghost官方支持资源

* 文档：[https://docs.ghost.org/docs](https://docs.ghost.org/docs)
* FAQ：[https://ghost.org/pricing/#faq](https://ghost.org/pricing/#faq)

### 域名绑定

当服务器上只有一个网站时，不做域名绑定也可以访问网站。但从安全和维护考量，**域名绑定**不可省却。

以示例网站为例，域名绑定操作步骤如下：

1. 确保域名解析已经生效  
2. 使用 SFTP 工具登录云服务器
3. 修改 [Nginx虚拟机主机配置文件](/维护参考.md#nginx)，将其中的 **server_name** 项的值修改为你的域名
   ```text
   server
   {
   listen 80;
   server_name www.example.com;  # 此处修改为你的域名
   ...
   }
   ```
4. 保存配置文件，重启 [Nginx 服务](/维护参考.md#nginx-1)

### 使用 Nginx 伪静态

Node.js 环境默认已经安装 伪静态模块，通过下面两个方式配置网站的伪静态规格：

1.  在服务器目录 */etc/nginx/conf.d/rewrite* 下新建你网站的伪静态规则文件（例如：wordpress.conf）
2.  在网站的[虚拟主机配置段](/维护参考.md#nginx) **server{ }** 中将伪静态规则文件 include 进来
   ```text
   server
   {
   listen 80;
   server_name mysite2.yourdomain.com;  # 此处修改为你的域名
   index index.html index.htm index.php;
   root  /data/wwwroot/mysite2;
   ...

   ## Includes one of your Rewrite rules if you need, examples
   include conf.d/rewrite/wordpress.conf;  # 引入你的伪静态规则
   }
   ```
3. 保存配置文件，重启 [Nginx 服务](/维护参考.md#nginx-1)


### 重置 MySQL 密码

1. 远程连接到服务器，
2. 运行一下命令，按提示输入新密码即可
   ```
   sudo git clone https://github.com/Websoft9/ansible-linux.git; cd ansile-linux/Mysql_ResetPasswd_Script;sudo sh reset_mysql_password.sh
   ```

### SSL/HTTPS

必须完成[域名绑定](#域名绑定)且可通过 HTTP 访问 Python ，才可以设置 HTTPS。

Node.js预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

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
3. 重启[Nginx服务](/维护参考.md#nginx-1)

#### 专题指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。

> Node.js runtime 默认已安装 SMTP 所需的组件，请勿重复安装或随意更改环境配置文件  

不建议在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

SMTP设置与具体的网站程序有关，下面以**网易邮箱**为例，提供一个通用的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 登录网站后台，找到 SMTP 设置界面
3. 填写 SMTP 参数
4. 测试发邮件

更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### MongoDB 数据管理

Python 预装包中内置 MongoDB 及可视化数据库管理工具 `adminMongo` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组9091端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9091*，进入adminMongo
  ![登录adminMongo](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/adminmongo-connect001-websoft9.png)
  
3. 输入数据库用户名和密码([不知道密码？](#账号密码)))

4. 开始管理数据库
  ![adminMongo](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/adminmongo-connect003-websoft9.png)

> 阅读Websoft9提供的 [《MangoDB教程》](https://support.websoft9.com/docs/mongodb/zh/solution-gui.html) ，掌握更多的MongoDB实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等


### MySQL 数据管理

Python 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP/phpmyadmin*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理

#### 浏览器打开 http://公网IP地址/9panel，无法访问（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 9Panel 是什么？

[9Panel](https://github.com/Websoft9/9panel)是 Websoft9 公司镜像的开源组件之一，支持中英文显示，部分镜像内置了9Panel. 它是集合数据库管理、文档和支持服务的引导页面，是镜像快速入门的向导工具。基于Bootstrap+vue.js开发，几乎不会占用系统资源，也不会对系统文件进行任何修改。