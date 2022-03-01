---
sidebar_position: 1
slug: /rocketchat
tags:
  - Rocket.Chat
  - 团队协作
  - 团队通讯
---

# 快速入门

Rocket.Chat 是一个类似 Slack 的交流平台，可以将外部客户，团队和其他生态相关者聚集到一个平台中的交流平台。自2015年面世以来，迅速成长为出色的开源项目之一。目前，Rocket.Chat广泛应用在银行，非政府组织，初创企业和政府组织，通过自定义其外观和风格，用户可以在云上或通过在本地托管自己的服务器来设置 Rocket.Chat，用户可以安全地管理数据。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-startchat-websoft9.png)


在云服务器上部署 Rocket.Chat 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Rocket.Chat，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `cat /credentials/password.txt` 命令，可以查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Rocket.Chat

* 管理员账号: `admin`
* 管理员密码: `admin` 或 存储在您的服务器中的文件中 */credentials/password.txt*  

### MongoDB

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中（ */credentials/password.txt* ）
   ![运行cat命令](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

> 需要登录MySQL，请参考 [MongoDB 可视化管理](#mongodb-数据管理)

## Rocket.Chat 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 进入初始化页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-wizard-websoft9.png)

2. 根据向导提示，输入组织名称，用户名，密码等关键信息，完成初始配置 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-set-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-setok-websoft9.png)

3. 点击【转到您的工作区】，您就可以使用在线聊天功能   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-startchat-websoft9.png)

4. 后台进入管理-添加用户，管理员可以从后台追加用户
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-adduser-websoft9.png) 

5. 其他用户输入*http://域名* 或 *http://Internet IP*, 还可以申请注册
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-register-websoft9.png)   

> 需要了解更多 Rocket.Chat 的使用，请参考官方文档：[Rocket.Chat Documentation](https://docs.rocket.chat/guides/user-guides)

## 常用操作

### 配置

参考官方方案：https://docs.rocket.chat/installation/manual-installation

### 域名绑定

当服务器上只有一个网站时，不做域名绑定也可以访问网站。但从安全和维护考量，**域名绑定**不可省却。

以示例网站为例，域名绑定操作步骤如下：

1. 确保域名解析已经生效  
2. 使用 SFTP 工具登录云服务器
2. 修改 [Nginx虚拟机主机配置文件](/维护参考.md#nginx)，将其中的 **server_name** 项的值修改为你的域名
   ```text
   server
   {
   listen 80;
   server_name www.example.com;  # 此处修改为你的域名
   index index.html index.htm index.php;
   root  /data/wwwroot/www.example.com;
   ...
   }
   ```
3. 保存配置文件，重启 [Nginx 服务](/维护参考.md#nginx-1)

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

Rocket.Chat 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 快速参考

如果你想使用免费证书，只需在服务器中运行一条命令`certbot`就可以启动证书部署

```
sudo certbot
```

如果你已经申请了商业证书，只需三个步骤，即可完成HTTPS配置

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到 *server{ }* 中
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

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面以**网易邮箱**为例，提供设置 Rocket.Chat 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 登录 Rocket.Chat 控制台

3. 依次打开：【管理】>【设置】>【电子邮箱】>【SMTP】项，填写 SMTP 参数
   ![Rocket Chat SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketchat/rocketchat-smtp-websoft9.png)

4. 点击【向我自己发送邮件测试】

更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，HotMail等）以及无法发送邮件等故障之诊断，请参考由 Websoft9 提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)


### MongoDB 数据管理

Rocket.Chat 预装包中内置 MongoDB 及可视化数据库管理工具 `adminMongo` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组9091端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9091*，进入adminMongo
  ![登录adminMongo](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/adminmongo-connect001-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](/zh/stack-accounts.md))
4. 开始管理数据库
  ![adminMongo](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/adminmongo-connect003-websoft9.png)

> 阅读Websoft9提供的 [《MangoDB教程》](https://support.websoft9.com/docs/mongodb/zh/solution-gui.html) ，掌握更多的MongoDB实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等


## 异常处理

#### 浏览器打开IP地址，无法访问 Rocket.Chat（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### Rocket.Chat 服务启动失败？

暂无

