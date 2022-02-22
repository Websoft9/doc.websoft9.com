---
sidebar_position: 1
slug: /couchdb
tags:
  - CouchDB
  - Cloud Native Database
---

# 快速入门

[CouchDB](https://couchdb.apache.org/) 是一个开源的面向文档的数据库管理系统，可以通过 RESTful JavaScript Object Notation (JSON) API 访问。 CouchDB 的目标具有高度可伸缩性，提供了高可用性和高可靠性，即使运行在容易出现故障的硬件上也是如此。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/couchdb/couchdb-gui-websoft9.png)

在云服务器上部署 CouchDB 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 CouchDB，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `cat /credentials/password.txt` 命令，可以查看所有相关账号和密码

下面列出可能需要用到的几组账号密码：

### CouchDB

* 管理员账号: `admin`
* 管理员密码: 存储在您的服务器中的文件中 */credentials/password.txt*  


## CouchDB 安装向导

1. 使用本地 Chrome 或 Firefox 访问网址：*http://域名/_utils* 或 *http://Internet IP/_utils*, 进入初始化页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/couchdb/couchdb-init-websoft9.png)

2. 输入账号密码，成功登录到 CouchDB 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/couchdb/couchdb-bk-websoft9.png)

3. 登录后通过：【Users】设置新密码  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/couchdb/couchdb-pw-websoft9.png)

> 需要了解更多 CouchDB 的使用，请参考官方文档：[CouchDB Documentation](https://docs.couchdb.org)
> 需要了解更多 MongoDB 的使用，请官方文档 [MongoDB Administration](https://docs.mongodb.com/manual/administration/)

## 常用操作

### 系统配置

参考官方方案：https://docs.couchdb.org/en/latest/config/index.html

### 域名绑定

当服务器上只有一个网站时，不做域名绑定也可以访问网站。但从安全和维护考量，**域名绑定**不可省却。

以示例网站为例，域名绑定操作步骤如下：

1. 确保域名解析已经生效  
2. 使用 SFTP 工具登录云服务器
3. 修改 [Nginx虚拟机主机配置文件](/zh/stack-components.md#nginx)，将其中的 **server_name** 项的值修改为你的域名
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
4. 保存配置文件，重启 [Nginx 服务](/zh/admin-services.md#nginx)

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

Metabase预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 快速参考

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

#### 详细指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### 开启远程访问

1. 修改 CouchDB 配置文件 */opt/couchdb/etc/default.ini*
   ```
      将 bindIP 修改为 0.0.0.0 或 本地电脑公网IP
      #bind_address = 127.0.0.1
      bind_address = 0.0.0.0
   ```
   > 0.0.0.0 代表任意公网IP均可访问

2. CouchDB
   ```
   systemctl restart couchdb
   ```

### 密码管理

#### 重置密码

重置密码即已经忘记密码的情况下，通过特殊手段重新设置新密码的过程。

1. 修改 CouchDB 配置文件 */opt/couchdb/etc/local.ini*，将下面的$new_password替换成新密码
   ```
   admin = $new_password
   ```
2. 重启 CouchDB 服务
   ```
   systemctl restart couchdb
   ```

### 开启用户认证

1. 修改 CouchDB 配置文件 */opt/couchdb/etc/default.ini*
   ```
  将 require_valid_user 的值设置为 false， 则每个人都必须经过身份验证。
   [chttpd]
   require_valid_user = false
   ```

2. CouchDB
   ```
   systemctl restart couchdb



## 异常处理

#### 浏览器打开IP地址，无法访问 CouchDB（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容