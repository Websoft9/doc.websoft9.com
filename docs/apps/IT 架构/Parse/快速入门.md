---
sidebar_position: 1
slug: /parse
tags:
  - Parse Server
  - Serverless
---

# 快速入门

[Parse Server ](https://parseplatform.org/) 是一个用Node.js编写的 Serverless 后台程序。它抽象了后端开发常用功能，并以服务端的方式对外提供API供第三方应用程序使用。针对不同环境、不同语言，官方同时提供了客户端SDK以简化您的开发工作。

Parse Server 提供的基础功能包括:

- 用户的登录注册
- 用户身份的认证
- 数据存储 && 灵活查询
- 文件存储
- 实时查询
- 消息推送
- 缓存服务
- 与云平台很好的对接
- 自定义业务逻辑与Hook机制

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/parseserver/dashboard.png)

在云服务器上部署 Parse Server 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 在 **域名控制台** 完成两个域名解析，分别对应 Parse Server 和 Parse Dashboard 两个核心模块  
例如：*parseserver.yourdomain.com* 和 *parsedashboard.yourdomain.com* 

## 账号密码

使用Parse Server，可能会用到的几组账号密码如下：

### Parse Server 

管理员用户名：admin  
管理员密码：admin

> 建议自行修改 Parse Dashboard 的账号密码（[参考](/zh/solution-more.md#修改-parse-dashboard-账号密码)）

### MongoDB

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中：*/credentials/password.txt*。建议通过云控制台直接连接服务器，进入命令终端，运行`cat /credentials/password.txt` 命令获取数据库密码：
   ![运行cat命令](https://libs.websoft9.com/Websoft9/DocsPicture/en/common/catdbpasswordmongdo-websoft9.png)

> 需要登录Mongodb，请参考 [Mongodb可视化管理](#mongodb-数据管理)


## Parse 安装向导

### 绑定域名

由于本项目不可以通过IP访问，因此绑定域名操作是能否正常运行本项目的关键。  

请参考 [绑定域名](#域名绑定) 完成绑定操作。


1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名*  就进入 Parse Dashboard 登录页面
![Parse Dashboard 登录](https://libs.websoft9.com/Websoft9/DocsPicture/en/parseserver/ParseServer-loginpage-websoft9.png)

2. 输入账号和密码（[查看](/zh/stack-accounts.md)），登录后的界面如下
![Parse Dashboard 后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/en/parseserver/parse-backend-websoft9.png)

3. 修改 Parse Dashboard 的密码（[参考](/zh/solution-more.md#修改-parse-dashboard-账号密码)）

> 需要了解更多 Parse 的使用，请参考官方文档：[Parse Server Documentation](https://docs.parseplatform.org/)


## 常用操作

### 域名绑定

请在域名绑定之前，先完成**域名解析**工作，并确认解析成功。  

Parse Server 域名绑定操作步骤：

1. 使用 SSH 连接云服务器，运行如下一条命令：
   ``` shell
   wget https://raw.githubusercontent.com/Websoft9/ansible-Parse-Server/master/script/parse-set-domain.sh && chmod +x parse-set-domain.sh &&./parse-set-domain.sh
   ```
2. 根据提示输入两个不同的域名，回车
   ```   
   Input Parse Server Domain: parseserver.websoft9.com
   Input Parse Dashboard Domain: parsedashboard.websoft9.com
   ```
3. 如果域名格式没有问题，会得到成功提示"Configure Done!"
4. 绑定完成

### 域名修改

修改域名不同于绑定域名，请严格参考下面的步骤：

1. 使用 SFTP 工具连接云服务器
2. 修改 */etc/nginx/conf.d/default.conf* 文件中两个域名信息
3. 修改 */etc/parse-server/parse-dashboard.json* 文件中的域名信息
4. 重启服务后生效
   ```
   sudo systemctl restart parse-dashboard
   sudo systemctl restart parse-server
   sudo systemctl restart nginx
   ```

### 修改 Parse Dashboard 账号密码

Parse Dashboard的账号密码存在它的配置文件中，修改步骤如下： 

1. 通过 SSH 工具连接到云服务器
2. 编辑 * /etc/parse-server/parse-server.json*，修改其中的 **users** 项
   ```
    "users": [
    {
      "user":"admin",
      "pass":"admin"
    } ]
   ```
3. 重启 Parse Dashboard 服务后生效
   ```
   systemctl restart parse-dashboard
   ```

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

Parse Server 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 简易步骤

如果你想使用免费证书，只需在服务器中运行一条命令`certbot`就可以启动证书部署

如果你已经申请了商业证书，只需三个步骤，即可完成HTTPS配置

> Parse Server 和 Parse Dashboard 域名不同，需要分别配置

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到所属的 *server{ }* 中
 ``` text
   #-----HTTPS template start------------
   listen 443 ssl; 
   ssl_certificate /data/cert/xxx.crt;
   ssl_certificate_key /data/cert/xxx.key;
   ssl_session_timeout 5m;
   ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
   ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
   ssl_prefer_server_ciphers on;
   #-----HTTPS template end------------
   ```
3. 重启Nginx服务

#### 专题指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿尝试在服务器上安装sendmail等发邮件方案，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，导致不稳定、不易维护、诊断故障困难。

下面以**网易邮箱**为例，提供设置 Parse Server  发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. Parse Server 暂无 SMTP 功能

更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### MongoDB 数据管理

Parse Server 预装包中内置 MongoDB 及可视化数据库管理工具 `adminMongo` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组9091和47017端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9091*，进入adminMongo
  ![adminMongo界面](https://libs.websoft9.com/Websoft9/DocsPicture/en/mongodb/adminmongo/adminmogo-sconnect-websoft9.png)
3. 参考下面的范例，新建一个【Connection】。其中的IP地址是服务器公网IP，数据库账号[此处获取](/zh/stack-accounts.md)
   ```
   # 连接到config数据库
   mongodb://root:1cTFecwTEs@40.114.115.58

   # 连接到admin数据库
   mongodb://root:1cTFecwTEs@40.114.115.58/admin

   # 连接到parse数据库
   mongodb://parse:AxXFcV5zSz@40.114.115.58/parse
   ```
4. 连接成功，开始管理 Parse库
  ![adminMongo parse](https://libs.websoft9.com/Websoft9/DocsPicture/en/mongodb/adminmongo/adminmogo-parse-websoft9.png)

5. 数据库操作完成后，务必参考下图**删除 Connection**
  ![adminMongo](https://libs.websoft9.com/Websoft9/DocsPicture/en/mongodb/adminmongo/adminmogo-delconnect-websoft9.png)

> 阅读Websoft9提供的 [《MongoDB教程》](https://support.websoft9.com/docs/mongodb/zh/admin-adminmongo.html) ，掌握更多的 MongoDB 实用技能：连接字符串范例、修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等 


## 异常处理

#### 浏览器打开IP地址，出现 "error":"unauthorized" ？

本项目不支持IP访问，需要 **[绑定域名](/zh/solution-more.md#域名绑定)** 方可使用

#### 本部署包采用的哪个数据库来存储 Parse Server 数据？

MongoDB