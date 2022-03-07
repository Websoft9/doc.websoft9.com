---
sidebar_position: 1
slug: /lnmp
tags:
  - LNMP
  - PHP
  - Nginx
  - 运行环境
---

# 快速入门

LNMP（Linux-Nginx-MySQL-PHP）是流行的Web运行环境组合，基于免费、开源软件构建。包括：Linux系统，Nginx Web服务器软件，MySQL数据库，PHP语言等四种核心组件以及其他相关辅助组件。Websoft9通过组合、优化和兼容性处理，将所有组件打包成一个高性能、易维护的PHP运行环境解决方案包，保证能够兼容运行绝大部分PHP应用程序。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/php-infra-websoft9.png)

在云服务器上部署 LNMP 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 LNMP，请先到 **域名控制台** 完成一个域名解析

## 账号密码
使用LNMP，可能会用到的几组账号密码如下：

## MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中（ */credentials/password.txt* ）    
  建议通过云控制台的命令终端，运行命令：sudo cat /credentials/password.txt，获取数据库密码   
   ![运行cat命令](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

  **注意**：若自行修改密码，务必采用类似于：f@N7eUUm25xAjP!$ 类似的加强密码，这样有助于提高数据库的安全性，减少数据库密码被破解的风险。
  
> 需要登录MySQL，请参考 [MySQL可视化管理](#mysql-数据管理)


## LNMP 安装向导


1. 使用本地 Chrome 或 Firefox 浏览器访问网址：*http:/服务器公网IP/9panel*, 就进入引导页面9Panel
   ![9panel](https://libs.websoft9.com/Websoft9/DocsPicture/zh/9panel/9panelmain-websoft9.png)

2. 通过 9Panel 可以快速了解镜像基本情况，管理数据库，找到帮助文档，寻求人工支持

## 登录数据库

LNMP 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，[登录MySQL](#mysql-数据管理) 管理用户和数据库

![9panel](https://libs.websoft9.com/Websoft9/DocsPicture/zh/9panel/9panel-mysql-websoft9.png)

## 安装网站

LNMP 可以用来部署多个 PHP 网站，[马上开始吧](#安装网站)


## 常用操作

### 安装网站

在 LNMP 环境上安装一个网站，也就是我们常说的增加一个虚拟主机。

全局上看，只需两个步骤：**上传网站代码** + [**虚拟机主机配置文件**](/zh/stack-components.md#nginx) **中增加 server{} 配置段**

> server{} 又称之为虚拟主机配置段，每个网站必定在 default.conf 中对应唯一的 server{}。

#### 准备

安装网站之前，请了解如下几个要点，做好准备工作

*  虚拟机主机配置文件：*/etc/nginx/conf.d/default.conf* 
*  连接工具：使用 WinSCP 连接服务器，它包含文件管理、运行命令两方面功能
*  域名：若需要使用域名，请确保备案后的域名成功解析到服务器IP
*  数据库：网站安装向导过程中可能需要使用数据库，请使用 [phpMyAdmin 管理数据库](/zh/admin-mysql.md)

有一个全局认知并完成准备工作之后，我们开始部署网站

#### 安装第一个网站

下面通过**替换示例网站**（LNMP 默认存在一个示例网站）的方式来教你安装你的第一个网站：

1. 使用 WinSCP 连接服务器
2. 删除示例网站 */data/wwwroot/www.example.com* 下的所有文件（保留目录）
3. 将本地电脑上的网站源码上传到示例目录下
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/winscp-uploadcodestoexample-websoft9.png)
4. 修改 *default.conf* 中已有 server{} 配置段（[修改参考](/zh/solution-deployment.md#server)），实现绑定域名、修改网站目录名称等操作。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lnmp/lnmp-editvhostconf-websoft9.png)
   ::: warning
   如果不绑定域名、不修改网站目录名称，请跳过步骤4和5
   :::
5. 保存 default.conf，然后在 WinSCP 中运行重启服务命令 或 云控制台重启服务器 ：
      ~~~
      # 重启 Nginx 服务命令
      sudo systemctl restart nginx
      ~~~
6. 本地浏览器访问：*http://域名* 或 *http://服务器公网IP* 即可访问您的网站

#### 安装第二个网站

从安装第二个网站开始，需要在 *default.conf* 中增加对应的虚拟主机配置段，具体如下

1. 使用 WinSCP 连接服务器，在 /data/wwwroot 下新建一个网站目录，假设命令为“mysite2”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-createmysite2-websoft9.png)
2. 将本地网站源文件上传到：*/data/wwwroot/mysite2* 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-uploadcodes-websoft9.png)
3. 编辑 *default.conf* 文件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-editvhostconf-websoft9.png)

    根据是否通过域名访问，选择下面操作之一：

     * **有域名，通过 http://域名 访问网站**
     
     请将下面 server 模板拷贝到 default.conf 中，并修改其中的 server_name, root, error_log, access_log等项的值
 
       ```
       server
       {
        listen 80;
        server_name mysite2.yourdomain.com;
        index index.html index.htm index.php;
        root  /data/wwwroot/mysite2;
        error_log /var/log/nginx/mysite2.yourdomain.com-error.log crit;
        access_log  /var/log/nginx/mysite2.yourdomain.com-access.log;
        include conf.d/extra/*.conf;

        ## Includes one of your Rewrite rules if you need, examples
        # include conf.d/rewrite/wordpress.conf;
        # include conf.d/rewrite/joomla.conf;
        }
        ```

     * **没有域名，通过 http://mysite1.yourdomain.com/mysite2 访问网站**  
    
     请将下面 Alias 模板插入到 default.conf 中已存在的 server{} 段中，并修改其中的 location,alias 

      ```
      location /mysite2
      {
       alias /data/wwwroot/mysite2;
       index index.php index.html;
       location ~ ^/mysite2/.+\.php$ {
        alias /data/wwwroot/mysite2;
        fastcgi_pass  unix:/dev/shm/php-fpm-default.sock;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME /data/wwwroot/$fastcgi_script_name;
        include        fastcgi_params; }
      include conf.d/extra/*.conf;
      }
      ```
      ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lnmp/lnmp-insertalias-websoft9.png)

      > 注意：Alias 模板只能插入到 server{} 配置段中
      > 
      > 如出现502错误，可以查找 fastcgi_pass  unix:/dev/shm/php-fpm-default.sock 配置中 sock 文件是否跟系统的 sock 文件一致，如不一致替换之

4. 保存 *default.conf*，然后在 WinSCP 中运行重启服务命令 或 云控制台重启服务器 ：
      ~~~
      # 重启Nginx服务命令
      sudo systemctl restart nginx
      ~~~
5. 如果配置了域名，通过：*http://域名* 访问你的网站。
6. 如果没有配置域名，通过：*http://mysite1.yourdomain.com/mysite2* 访问你的网站


#### 安装第 N 个网站

安装第n个网站与安装第二个网站的操作步骤一模一样

最后我们温故而知新，总结 LNMP 安装网站步骤： 

1. 上传网站代码
2. 绑定域名（非必要）
3. 新增站点配置或修改示例站点配置
4. 增加网站对应的数据库（非必要）
5. 进入安装向导 

#### Server

server{ } 改动务必准确无误，任何错误的修改都会导致服务器上所有的网站不可访问

|  server 项  |  作用说明  |  必要性 |
| --- | --- | --- |
|  server_name  |  域名，如果配置两个域名需以空格分开   |  必须填写 |
|  root |  网站存放目录  | 务必准确无误 |
|  error_log  | 错误日志路径，系统会根据定义的路径产生相关日志文件   |  可以不填或删除 |
|  access_log  | 访问日志路径，系统会根据定义的路径产生相关日志文件  |  可以不填或删除 |
|  ssl_certificate  | HTTPS 证书路径  |  设置 HTTPS 访问时必填 |
|  ssl_certificate_key  | HTTPS 证书秘钥路径   |  设置 HTTPS 访问时必填 |

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


### 迁移网站

迁移网站就是将**网站数据**移动到新的位置，然后通过配置，保证移动后可正常访问。

迁移是需要谨慎对待的操作，迁移之前需要清楚的明白如下要点：

- 被移动的网站数据对象：网站源码文件和数据库数据文件  
- 目的地位置：服务器目录之间转移（本地）和转移到外部服务器（外部）

被迁移对象和目的地位置的组合，形成了多种多样的迁移场景。下面详细说明最常见的迁移场景：

#### 迁移网站源码（本地）

以将原目录 */data/wwwroot* 下的 **mysite1** 迁移到 */data2/wwwroot* 目标目录下为例，具体步骤如下：

1. 使用 WinSCP 连接服务器
2. 将 ***mysite1*** 文件夹整体拷贝到目标位置 */data2/wwwroot*
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-copysite1todata2-websoft9.png)
3. 修改 *default.conf* 中 mysite1 这个网站对应的 server{ } 配置段 root 项的值
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lnmp/lnmp-modifyvhostdata2-websoft9.png)

   原地址：/data/wwwroot/mysite1  
   目标地址：/data2/wwwroot/mysite1

4. 保存 default.conf，然后在 WinSCP 中运行重启服务命令 或 云控制台重启服务器 ：
      ~~~
      # 重启Nginx服务命令
      sudo systemctl restart nginx
      ~~~ 
5. 测试迁移后的结果，成功后可以删除原来的 *mysite1* 文件夹

#### 迁移数据库文件（本地）

没有特殊情况，我们不建议迁移数据库文件到服务器上另外一个目录，毕竟主流的云厂商磁盘均可扩容。

如果要更改 [MySQL 数据库文件目录](/zh/stack-components.md#mysql)，请参考此处[ MySQL 专题文档](https://support.websoft9.com/docs/mysql/zh/solution-modifydatadir.html)

#### 将/data目录迁移到数据盘（本地）

默认情况下 /data 是在系统盘的，当需要转移到数据盘，步骤如下:

1. 开始操作之前，**请务必做好数据备份**；
2. 提前购买数据盘，然后到云控制台将数据盘关联到云服务器
3. 连接服务器，将数据盘分区格式化
4. 在云服务器根目录下创建一个临时目录 temp 
5. 将数据盘挂载（mount）到:*/temp* 目录
4. 停止云服务器上的 Nginx 和 MySQL 服务
    ~~~
    sudo systemctl stop nginx mysql
    ~~~

5. 将当前 */data* 下所有文件拷贝到服务器临时文件夹 */temp*  中
    > 数据较大的话，拷贝可能会失败，此步骤具体问题需具体对待
6. 等待数据转移完成
7. 连接服务器，将数据盘再次挂载（mount）到:*/data* 目录 
8. 运行以下命令重新启动 Nginx 和 MySQL:
   ```
   sudo systemctl start nginx mysql
   ``` 
9. 测试迁移结果

> 数据盘格式化以及挂载（mount）操作非常复杂，需要有熟练的相关技能


#### 迁移到外部服务器

网站从一台服务器（原服务器）迁移到另外一台服务器（目的服务器）是一个系统工程，基本步骤如下：

1. 通过云控制台，在目的服务器上[部署](/zh/stack-deployment.md)参数一致的 LNMP 镜像。
2. 通过 WinSCP 将原服务器上的网站源文件**下载**到本地电脑，然后再**上传**到目的服务器。
3. 通过 phpMyAdmin **导出**原服务器上的数据库，然后在目的服务器上**导入**数据库。
4. 把原服务器上的 default.conf 配置文件内容，完整拷贝到目的服务器的 default.conf 中，保存之。
5. 重启 Nginx 服务。
5. 解析域名到目的服务器，等待域名解析生效。
5. 通过域名访问网站，测试可用性。
6. 正式发布。

如果一台服务器上有多个网站需要迁移，建议逐个迁移

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

### 使用 Nginx 伪静态

使用 Nginx 伪静态有三个步骤：

1.  打开 [Apache模块配置文件](/维护参考.md#apache)，检查 Rewrite 模块是否启用（LAMP 环境默认已经开启 Rewirte）
2.  保证 [Apache 虚拟主机配置文件](/维护参考.md#apache)中 VirtualHost 配置段中增加 AllowOverride All
3.  给需要使用伪静态的网站的根目录中增加.htaccess文件，并在其中配置伪静态规则

### 重置 MySQL 密码

1. 远程连接到服务器，
2. 运行一下命令，按提示输入新密码即可
   ```
   sudo git clone https://github.com/Websoft9/linux.git; cd linux/Mysql_ResetPasswd_Script;sudo sh reset_mysql_password.sh
   ```

### 修改 php.ini

在使用PHP网站的时候，你可能会碰到需要修改：上传文件大小、内存限制等参数。这个时候，就需要通过修改 `php.ini` 来实现

1. 使用 SFTP 工具修改 */etc/php.ini* 
```
# File upload limit
post_max_size = 16M
upload_max_filesize = 16M

# Max Execution Time
max_execution_time = 90

# Memory Limit
memory_limit – Minimum: 256M
```
2. 保存并重启 [Nginx 服务](/维护参考.md#nginx-1)

### PHP版本变更

请参考 [《PHP版本管理专题》](https://support.websoft9.com/docs/linux/zh/lang-php.html#版本升级)

### PHP安装扩展

请参考 [《PHP扩展管理专题》](https://support.websoft9.com/docs/linux/zh/lang-php.html#扩展)

### 可视化Nginx配置工具

参考：https://www.digitalocean.com/community/tools/nginx

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

LNMP预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 自动部署

如果没有申请证书，只需在服务器中运行一条命令`sudo certbot`便可以启动免费证书**自动**申请和部署

```
sudo certbot
```

#### 手动部署

如果你已经申请了证书，只需三个步骤，即可完成 HTTPS 配置

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入如下的 **HTTPS 配置项** 到 server{ } 段落中
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
3. 确保ssl_certificate, ssl_certificate_key等项的值（[参考](/#安装网站)）
4. 保存 default.conf，然后在 WinSCP 中运行重启服务命令 或 云控制台重启服务器 ：
    ~~~
    # 重启Nginx服务命令
    systemctl restart nginx

#### 专题指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP


大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。

> LNMP 默认已安装 SMTP 所需的组件，请勿重复安装或随意更改环境配置文件  

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