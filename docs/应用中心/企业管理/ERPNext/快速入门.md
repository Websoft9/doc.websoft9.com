---
sidebar_position: 1
slug: /erpnext
tags:
  - ERPNext
  - 企业管理
  - ERP
---

# 快速入门

[ERPNext](https://erpnext.com/)  是一个 100% 开源的 ERP，基于 Python 和 Node 开发，它功能全面，包含会计、人力资源、制造、网站、电商、CRM、资产管理、客服工作台等全面的功能。非常合适作为 SAP 的替代品，全球已经有超过 5,000 家企业客户使用。
![](http://libs.websoft9.com/Websoft9/DocsPicture/en/erpnext/erpnext-adminui-websoft9.png)


在云服务器上部署 ERPNext 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 ERPNext，请先到 **域名控制台** 完成一个域名解析


## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### ERPNext

* 管理员账号: `Administrator`
* 管理员密码: 存储在您的服务器中的文件中 */credentials/password.txt*  

### MariaDB

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

## ERPNext 安装向导

1. 使用本地电脑 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入初始化页面
   ![erpnext安装登录](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](/zh/stack-accounts.md#erpnext)），选择语言， 进入下一步 
   ![erpnext安装](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-language-websoft9.png)

3. 根据安装向导依次完成后续步骤

4. 安装完成之后，ERPNext 会弹出如下界面
   ![erpnext后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-cpsetup-websoft9.png)

   可能会出现安装错误提示，此时需要反复安装：
   ![erpnext 向导安装报错](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-wizarderror-websoft9.png)

5. ERPNext 顶部菜单中提供了搜索框，用于快速检索并进入 ERPNext 所有的功能
   ![erpnext 快速检索](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-sbar-websoft9.png)

6. 通过检索功能，进入【用户】设置，可以管理当前系统下所有账号
   ![erpnext 用户管理](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-users-websoft9.png)


> 需要了解更多 ERPNext 的使用，请参考官方文档：[ERPNext Documentation](https://docs.erpnext.com)

## 常用操作

### 域名绑定

当服务器上只有一个网站时，不做域名绑定也可以访问网站。但从安全和维护考量，**域名绑定**不可省却。

以示例网站为例，域名绑定操作步骤如下：

1. 确保域名解析已经生效  
2. 使用 SFTP 工具登录云服务器
2. 修改 [Nginx虚拟机主机配置文件](/zh/stack-components.md#nginx)，将其中的 **server_name** 项的值修改为你的域名
   ```text
   server
   {
   listen 80;
   server_name name;  # modify it to your domain
   root /data/wwwroot/frappe-bench/sites;
   ...
   }
   ```
3. 保存配置文件，重启 [Nginx 服务](/zh/admin-services.md#nginx)
4. 修改 ERPNext 环境变量，绑定域名:
   进入 ERPNext 目录 /data/wwwroot/erpnext
   修改 .env 文件域名配置项
   ```
   ...
   APP_SITE_URL=your domain
   APP_SITE_NAME=`your domain`
   ...
   ```
6. 重启 ERPNext 
   ```
   docker-compose up -d 
   ```

### SSL/HTTPS

必须完成[域名绑定](/zh/solution-more.md)且可通过 HTTP 访问 ERPNext ，才可以设置 HTTPS。

ERPNext 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。因此，除了虚拟主机配置文件之外，HTTPS 设置则不需要修改 Nginx 其他文件。

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
3. 重启[Nginx服务](/zh/admin-services.md#nginx)

#### 专题指南

若参考上面的**快速指南**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

《HTTPS 专题专题》方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面以**QQ邮箱**为例，提供设置 ERPNext 发邮件的步骤：

1. 在QQ邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.qq.com
   SMTP port: 465 or 587 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9smpt
   SMTP password: #fdfwwBJ8f #这个密码不是邮箱密码，是需要通过QQ邮箱SMTP设置去获取的授权码
   ```
2. 登录 ERPNext控制台，在【设置】>【电子邮件域名】填写SMTP参数
![ERPNext SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/erpnext/erpnext-smtp-websoft9.png)

3. 点击【保存】后，系统后进行一个 SMTP 初步验证，验证通过才能保存成功

更多邮箱设置（阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### 重置密码

常用的 ERPNext 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码


1. 登录 ERPNext后台，依次打开：【设置】>【个人设置】，找到修改密码项
  ![ERPNext 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-modifypw-websoft9.png)

2. 直接设置新密码，保存后生效

#### 找回密码

如果用户忘记了 ERPNext 密码，可以通过如下的命令直接设置一个新密码：

```
sudo -H -u erpnext bash -c "cd /data/wwwroot/frappe-bench && export GIT_PYTHON_REFRESH=quiet && /usr/local/bin/bench set-admin-password newpassword"
```

#### 使用RDS

如果用户不喜欢使用服务器上安装的 MariaDB，而希望迁移到云数据库中（RDS），大致流程：

1. 备份已有数据库，并导入到 RDS 中（适合于 ERPNext 已经完成安装）

2. 修改 [ERPNext 容器配置文件:/data/wwwroot/erpnext/.env](/zh/stack-components.md#erpnext) 中的数据库相关信息
   ```
   DB_MRAIADB_USER=root
   DB_MARIADB_PASSWORD=123456
   DB_MARIADB_HOST=mariadb
   DB_MARIADB_PORT=3306
   DB_MARIADB_VERSION=10.6
   ```

   > DB_MARIADB_HOST 设置为外部数据库地址

3. 重新运行容器
   ```
   cd /data/wwwroot/erpnext
   docker-compose up -d
   ```

4. 测试更改数据库后的连接可用性

### MariaDB 数据库操作

ERPNext 预装包中内置 MariaDB 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组9090端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/) ，掌握更多的MariaDB实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等


## 异常处理

#### 浏览器打开IP地址，无法访问 ERPNext（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### ERPNext 安装向导最后一步出现错误提示？
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-wizarderror-websoft9.png)
原因：未知  
方案：重复安装几次直至成功  

#### ERPNext 服务启动失败？

请确认hostname是否包含字符串 "."，例如 erpnext12.14.0对于ERPNext来说是一个不合规的hostname

你可以使用下列命令来修改hostname：

```
hostnamectl set-hostname erpnext
```