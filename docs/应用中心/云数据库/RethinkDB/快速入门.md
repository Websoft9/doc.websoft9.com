---
sidebar_position: 1
slug: /rethinkdb
tags:
  - RethinkDB
  - Cloud Native Database
---

# 快速入门

[RethinkDB](https://rethinkdb.com) 是一个曾经与 MongoDB 齐名的开源文档（JASON）数据库，目前完全由开源社区驱动。它支持多种数据类型，提供可视化的控制台，很方便部署和构建集群。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-gui-websoft9.png)

在云服务器上部署 RethinkDB 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 RethinkDB **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### RethinkDB 控制台

* 管理员账号: `admin`
* 管理员密码: 存储在您的服务器中的文件中 */credentials/password.txt* 

> 本部署方案通过 [Nginx 验证访问](/zh/stack-components.md#nginx)控制 RethinkDB 控制台的访问

### RethinkDB

* 管理员账号: `admin`
* 管理员密码: 存储在您的服务器中的文件中 */credentials/password.txt* 


## RethinkDB 安装向导

1. 使用本地电脑的浏览器访问网址：*http://域名* 或 *http://服务器公网IP*，准备登陆 RethinkDB 控制台

2. 输入用户名和密码

3. 成功登录到 RethinkDB 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-gui-websoft9.png)

## RethinkDB 入门向导

下面通过 RethinkDB 控制台，演示如何增加 Database 和 Table：

1. 依次打开：【Tables】>【Add Database】，增加一个数据库
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-adddb-websoft9.png)

2. 打开数据库，点击【Add Table】增加表
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-addtable-websoft9.png)

> 需要了解更多 RethinkDB 的使用，请参考官方文档：[RethinkDB Documentation](https://rethinkdb.com/docs)

## 常用操作

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
    server_name example.yourdomain.com; # 此处修改为真实域名
    location / {
        proxy_pass  http://127.0.0.1:8080; 
   ...
   }
   ```
4. 保存配置文件，重启 [Nginx 服务](/zh/admin-services.md#nginx)

### 控制台密码

本部署方案通过 Nginx 验证访问控制 RethinkDB 的访问，通过如下两个步骤修改密码：

1. 编辑 Nginx 验证访问控制文件： */etc/nginx/.htpasswd/htpasswd.conf* 中的密码
2. 重启 Nginx 服务后生效
   ```
   sudo systemctl restart nginx
   ```

### 远程访问

RethinkDB 远程访问的开关存储在：*/etc/rethinkdb/instances.d/instance.conf* 文件中。  

只需执行下面命令，然后重启服务，即可开启远程访问。

```
sudo sed -n "s/^#bind=/bind=0.0.0.0/g" /etc/rethinkdb/instances.d/instance.conf
```

### 用户管理

下面以 Python 客户端新增一个用户并设置其初始密码作为范例进行说明

1. 以 `admin` 用户身份连接数据库
   ```
   from rethinkdb import r

   # 无密码连接
   r.connect('localhost', 28015).repl()

   # 有密码连接
   r.connect('localhost', 28015, password='123456').repl()
   ```

2. 新增用户名和密码
   ```
   r.db('rethinkdb').table('users').insert({id: 'bob', password: 'secret'})
   ```

### 重置密码

常用的 RethinkDB 重置密码相关的操作主要有修改密码和清空密码（将密码设置为空）两种方式。  

1. 登录 RethinkDB Web 界面，在【Data explorer】下输入所需的命令

   ```
   # 修改密码命令
   r.db('rethinkdb').table('users').get('admin').update({password: 'newpassword'})

   # 清空密码命令
   r.db('rethinkdb').table('users').get('admin').update({password: false})
   ```
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-editpassword-websoft9.png)

2. 点击【run】后生效

## SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

RethinkDB 预装包，已安装 Web 服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改 Nginx 任何文件

### 快速参考

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
   ssl_trusted_certificate /data/cert/chain.pem;
   ssl_session_timeout 5m;
   ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
   ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
   ssl_prefer_server_ciphers on;
   #-----HTTPS template end------------
   ```
3. 重启[ Nginx 服务](/zh/admin-services.md#nginx)

### 详细指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

《HTTPS 专题专题》方案包括：HTTPS前置条件、HTTPS 配置段模板及故障诊断等具体方案。

## 可视化工具

RethinkDB 可视化控制台是它的重要组成部分，是其重要的产品特征。  

1. 使用本地电脑的浏览器访问网址：*http://服务器公网IP*，准备登陆 RethinkDB 控制台

2. 输入用户名和密码（[不知道账号密码？](/zh/stack-accounts.md#rethinkdb)）

3. 成功登录到 RethinkDB 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-ok-websoft9.png)

4. 依次打开：【Tables】>【Add Database】，增加一个数据库
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-adddb-websoft9.png)

5. 打开数据库，点击【Add Table】增加表
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-addtable-websoft9.png)

## 异常处理

#### 浏览器打开IP地址，无法访问 RethinkDB（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### RethinkDB 控制台运行在哪个端口？

8080 端口，本部署方案通过 Nginx 转发到了 80 端口。