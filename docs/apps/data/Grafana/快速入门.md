---
sidebar_position: 1
slug: /grafana
tags:
  - Grafana
  - 大数据分析
  - BI
---

# 快速入门

[Grafana](https://github.com/grafana/grafana) 是一个开源的度量分析与可视化套件。经常被用作基础设施的时间序列数据和应用程序分析的可视化，它在其他领域也被广泛的使用包括工业传感器、家庭自动化、天气和过程控制等。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-dashboardui.png)

在云服务器上部署 Grafana 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Grafana，请先到 **域名控制台** 完成一个域名解析

## 账号密码

使用Grafana，可能会用到的几组账号密码如下：

### Grafana

Administrator username：`admin`  
Administrator password： `admin` 或 存储在您的服务器中的文件中 */credentials/password.txt*  

运行 `cat /credentials/password.txt` 命令，可以查看其中内容  

## Grafana 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 就进入登录页面
![Grafana 登录](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-login-websoft9.png)

2. 输入默认的用户名和密码（[查看](/zh/stack-accounts.md#grafana)），系统会提示修改密码
![Grafana 强提示修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-forcechangepw-websoft9.png)

3. 登录到 Grafana 控制台页面  
![Grafana 控制台](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-dashboard-websoft9.png)

4. 通过【Configuration】>【Plugins】添加插件  
![Grafana 添加插件](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-plugins-websoft9.png)

5. 通过【Configuration】>【Data Sources】添加数据源（分析对象）  
![Grafana 添加数据源](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-datasource-websoft9.png)

6. 通过【Configuration】>【Users】增加用户    
![Grafana 添加用户](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-users-websoft9.png)

> 需要了解更多 Grafana 的使用，请参考官方文档：[Grafana Documentation](https://grafana.com/docs)


## 常用操作

### CLI

直接运行 `grafana-cli` 即可

### 域名绑定

绑定域名的前置条件是：Grafana已经可以通过解析后的域名访问。  

虽然如此，从服务器安全和后续维护考量，**域名绑定**步骤不可省却  

Grafana 域名绑定操作步骤：

1. 登录云服务器
2. 修改 [Nginx虚拟机主机配置文件](/维护参考.md#nginx)，将其中的 **server_name** 项的值 *_* 修改为你的域名
   ```text
   server {
      listen 80;
      server_name _; # 改为自定义域名
   ...
   ```
3. 保存配置文件，重启[Nginx服务](/维护参考.md#nginx-1)


### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

Grafana预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 简易步骤

如果你想使用免费证书，只需在服务器中运行一条命令`certbot`就可以启动证书部署

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

请勿尝试在服务器上安装sendmail等发邮件方案，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，导致不稳定、不易维护、诊断故障困难。

下面以**网易邮箱**为例，提供设置 Grafana 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
3. 编辑 [Grafana 配置文件](/zh/stack-components.md#grafana) 中的 SMTP选项，填写自己的 SMTP 项
   ```
   #################################### SMTP / Emailing #####################
   [smtp]
   enabled = false
   host = localhost:25
   user =
   # If the password contains # or ; you have to wrap it with triple quotes. Ex """#password;"""
   password =
   cert_file =
   key_file =
   skip_verify = false
   from_address = admin@grafana.localhost
   from_name = Grafana
   ehlo_identity =

   [emails]
   welcome_email_on_sign_up = false
   templates_pattern = emails/*.html
   ```
4. 重启服务
   ```
   sudo systemctl restart grafana-server
   ```
5. 登录 Grafana控制台，打开：【Alerting】>【Alert Rules】，新建一个【Email】通知渠道
   ![Grafana SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-sendmails-websoft9.png)
6. 点击【Send Test】

更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### MySQL 数据管理

Grafana 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组9090端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等



## 异常处理

#### 浏览器打开IP地址，无法访问 Grafana（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 Grafana 数据？

SQlite



