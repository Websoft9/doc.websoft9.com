---
sidebar_position: 1
slug: /ruby
tags:
  - Ruby
  - 运行环境
---

# 快速入门

[Ruby](https://www.ruby-lang.org/)是一门开源的动态编程语言，注重简洁和效率。Ruby 的句法优雅，读起来自然，写起来舒适。它由日本人发明，混合了多门语言（Perl、Smalltalk、Eiffel、Ada 和 Lisp），创造出了一种兼具函数式编程和命令式编程特色的新语言。

![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/ruby/ruby-stackframe-websoft9.png)


在云服务器上部署 Ruby Runtime 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Ruby Runtime，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

## MySQL/MariaDB

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  
  
> 需要登录MySQL，请参考 [MySQL可视化管理](#mysql-数据管理)

## MongoDB

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

> 需要登录 MongoDB，请参考 [MongoDB可视化管理](#mongodb-数据管理)


## Ruby 安装向导

1. 使用本地浏览器访问网址：*http:/服务器公网IP*，进入 Rails 演示项目页面
   ![Ruby Rails](https://libs.websoft9.com/Websoft9/DocsPicture/zh/ruby/ruby-railsgui-websoft9.png)

2. 使用本地浏览器访问网址：*http:/服务器公网IP/9panel*, 就进入引导页面9Panel
   ![9panel](https://libs.websoft9.com/Websoft9/DocsPicture/zh/ruby/ruby-9panel-websoft9.png)

3. 通过 9Panel 可以快速了解环境的基本情况，并管理数据库，找到帮助文档，寻求人工支持

## 登录数据库

Ruby Runtime 内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，[登录MySQL](#mysql-数据管理) 管理用户和数据库

![9panel](https://libs.websoft9.com/Websoft9/DocsPicture/zh/9panel/9panel-mysql-websoft9.png)

## 安装网站

Ruby Runtime 可以用来部署多个 Ruby 网站，[马上开始吧](#安装网站)

## 常用操作

### 安装网站

在 Ruby Runtime 环境上安装一个网站，一般是基于已有的 Rails 环境配置。  

主要步骤包括：

```
# 安装应用包
gem install yourapp

# 基于 rails 创建应用脚手架
rail new yourapp

# 安装依赖包
cd yourapp
bundle install

# 自动配置
bin/rake ..

# 运行
rails s -b 0.0.0.0
```

#### 常见问题

##### 是否可以基于现有的 rails 框架直接添加应用？

待研究

##### 不同版本的 ruby 是否都可以安装 rails？

待研究

##### 每个应用是否都有隔离环境？

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

Ruby 域名绑定操作步骤：

1. 确保域名解析已经生效  
2. 使用 SFTP 工具登录云服务器
3. 修改 [Nginx虚拟机主机配置文件](/维护参考.md#nginx)，将其中的 **server_name** 项的值修改为你的域名
   ```text
   server
   {
   listen 80;
   server_name ruby.yourdomain.com;  # 此处修改为你的域名
   ...
   }
   ```
4. 保存配置文件，重启 [Nginx 服务](/维护参考.md#nginx-1)

### SSL/HTTPS

必须完成[域名绑定](/zh/solution-more.md)且可通过 HTTP 访问 Python ，才可以设置 HTTPS。

Ruby 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。因此，除了虚拟主机配置文件之外，HTTPS 设置则不需要修改 Nginx 其他文件。

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


### 隔离环境

有两种隔离环境的解决方案：

* RVM Gemset
* Bundler

经过实验验证，bundle 可以很方便的将项目所需的软件包安装到项目目录中。  

### gem 源

rubygems.org 存放在 Amazon S3 上，有时由于网络问题导致无法安装

```
# 查询当前源，假设为：https://rubygems.org/
gem sources -l

# 删除当前源
gem sources --remove https://rubygems.org/

# 安装替换源
gem sources -a https://gems.ruby-china.com/

# 查询替换后的结果
gem sources -l

# bundle 源更换  
bundle config mirror.https://rubygems.org https://gems.ruby-china.com/
```

> gemfile 中也可以指定源，这样就无需全局设置


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