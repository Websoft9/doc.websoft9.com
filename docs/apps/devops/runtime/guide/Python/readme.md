---
sidebar_position: 1
slug: /runtime/python
tags:
  - Python
  - 运行环境
---

# 快速入门

**Python Runtime** 是一个产品化的全栈运行环境，包含：[Python](https://www.python.org/), Django, Nginx, MySQL, Docker 以及其他组件，它让用户专注于应用程序的发布，以可靠、稳定、可控的方式部署各种不同类型的 Python 应用程序，在提示效率的同时减少生产环境中人为出错的风险。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/python-infra-websoft9.png)


在云服务器上部署 Python 预装包之后，请参考下面的步骤快速入门。  

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Python 应用，请先到 **域名控制台** 完成一个域名解析


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



## Python 安装向导

1. 使用 SSH 工具登录服务器，输入命令`python3`，便进入交互式解释器界面，即具备 Python3 环境
   ```
   Python 3.6.8 (default, Apr  2 2020, 13:34:55)
   [GCC 4.8.5 20150623 (Red Hat 4.8.5-39)] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>>
   ```

   > 部分系统中内置 Python2，输入命令 `python` 会进入 Python2 的交互式计界面

2. 使用本地浏览器访问网址：*http://域名* 或 *http://服务器公网IP*，可以看到 Django 界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/django-installss-websoft9.png)

2. 使用本地浏览器访问网址：*http:/服务器公网IP/9panel*, 就进入引导页面 9Panel
   ![9panel](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/python-9panel-websoft9.png)

3. 通过 9Panel 可以快速了解环境的基本情况，并管理数据库，找到帮助文档，寻求人工支持

> 需要了解更多 Python 的使用，请参考官方文档：[Python Documentation](https://docs.python.org/zh-cn/3/)


## 登录数据库

Python Runtime 内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，[登录MySQL](#mysql-数据管理) 管理用户和数据库

![9panel](https://libs.websoft9.com/Websoft9/DocsPicture/zh/9panel/9panel-mysql-websoft9.png)

## 安装网站

Python Runtime 可以用来部署多个 Python 网站，[马上开始吧](#安装网站)

## 常用操作

### 安装网站

在 Python Runtime 环境上安装不同的网站有一定的差异，但总体上是遵循如下几个步骤的：

1. 创建一个独立的隔离环境
2. 准备好网站的源码（通过命令行拉取或上传代码）
3. 修改配置信息（端口、数据库、IP地址等）
4. 启动网站

> 务必牢记以上几个步骤，不要一开始就落入技术陷阱中

#### 部署

下面通过安装一个开源 Python 框架 [Django](https://www.djangoproject.com/) 作为范例，帮助用户理解安装的方法。   

1. 首先，为 Django 创建一个全新的 Python 隔离环境
   ```
   #1 创建隔离环境
   mkdir /data/wwwroot/mydjango
   python3 -m venv --system-site-packages "/data/wwwroot/mydjango"

   #2 进入到隔离环境状态下
   cd /data/wwwroot/mydjango && source bin/activate

   #3 升级隔离环境下的 pip 版本
   pip install --upgrade pip
   ```

   > 进入到隔离环境下后，所有的 Python 命令只在隔离环境中有效

2. 安装 **django CMS** 命令工具，并创建项目拉取源码
   ```
   #1 安装 django CMS 命令行工具（用于创建和管理 django CMS 项目）
   pip install django

   #2 基于命令行创建一个项目（创建时会拉取所有依赖的源码）
   django-admin startproject mysite1
   ```

   > 如果再次运行 django-admin startproject mysite2，即再创建一个项目，以此类推...

3. 修改网站的配置文件 *mysite1/mysite1/settings.py* 中 **ALLOWED_HOSTS** 值为如下
   ```
   ALLOWED_HOSTS = ['*']
   ```
   > 也可以修改 DATABASES 参数，指定数据库

4. 指定端口下启动网站（下面设置为绑定任意IP地址）
   ```
   cd mysite1
   python manage.py migrate
   python manage.py runserver 0.0.0.0:8001
   ```

5. 本地浏览器访问：*http://服务器公网IP:8001* 便可以访问 Django 界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/django-installss-websoft9.png)

#### 架构优化

上面的安装可知，虽然可以通过 runserver 访问 Django，但 runserver 只是 Django 框架中用于测试的 Web 服务器，根本无法满足生产应用。

而真正的生产应用如下图所示的架构：  

![Python 生产环境架构](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/python-webhttpstructure001-websoft9.jpg)

![Python 生产环境架构](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/python-webhttpstructure002-websoft9.jpg)

![Python 生产环境架构](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/python-webhttpstructure003-websoft9.jpg)

即在网站程序之前，增加 uWsgi 作为 Python 应用程序 Web 服务器，在 uWsgi 增加 Nginx 作为用户端的请求处理，以满足性能和安全要求。  

下面我们分别介绍如何配置这两个组件：  

##### 配置 uWsgi

1. 隔离环境中安装 uWsgi
   ```
   cd /data/wwwroot/mydjango && source bin/activate
   pip install uwsgi
   ```
   > uWsgi 不能安装到全局环境中，否则无法管理隔离环境中的 Django 框架

2. 在 */data/wwwroot/mydjango* 目录中新增一个 uWsgi 配置文件，命名为：django.ini 
   ```
   [uwsgi]
   master        = true
   protocol      = uwsgi
   http          = 0.0.0.0:8001
   wsgi-file     = mysite1/mysite1/wsgi.py
   chdir         = /data/wwwroot/mydjango
   buffer-size   = 8192
   enable-threads= true
   close-on-exec = true
   uid           = nginx
   gid           = nginx
   ```

3. 通过隔离环境中的 uWsgi 命令启动应用
   ```
   /data/wwwroot/mydjango/bin/uwsgi --ini /data/wwwroot/mydjango/django.ini
   ```

4. 本地浏览器访问：*http://服务器公网IP:8001* 便可以访问 Django 界面


> 架构逻辑：**客户-uWsgi-Django**。同时，配置过程中把握好 django.ini 中的路径不要出错。

##### 配置 Nginx

Nginx 用作前端 Web 服务器，有着高性能

1. 为网站配置 HTTP 服务：在 [Nginx 虚拟主机配置文件](/zh/stack-components.md#nginx) 中增加如下的配置段

   * **配置方式一**

   ```
    server {
        listen 80;
        server_name yoursite1.yourdomain.com;
        location / {
            proxy_pass  http://127.0.0.1:8001;
            proxy_redirect     off;
            proxy_set_header   Host             $host;
            proxy_set_header   X-Real-IP        $remote_addr;
            proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Proto $scheme;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection upgrade;
            proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
            proxy_max_temp_file_size 0;
            proxy_connect_timeout      90;
            proxy_send_timeout         90;
            proxy_read_timeout         90;
            proxy_buffer_size          4k;
            proxy_buffers              4 32k;
            proxy_busy_buffers_size    64k;
            proxy_temp_file_write_size 64k;
    }
    error_log /var/log/nginx/yourdomain.com-error.log error;
    access_log  /var/log/nginx/yourdomain.com-access.log;

    include extra/*.conf;
    
    #------------- SSL Start --------------

    #------------- SSL End  ---------------
    }
   ```  

   重点需要注意修改如下几个参数：server_name, proxy_pass


   * **配置方式二**（未验证）

   > 采用 Nginx 中的 uwsgi 模块，可以做到真正意义上的动静分离，性能更好
   
   ```
   server {
      listen 80;
      server_name yoursite1.yourdomain.com;

      location / {
         include uwsgi_params;
         uwsgi_read_timeout 3600;
         uwsgi_pass 127.0.0.1:8001;
         }

      location  ~/static/ {
         expires 30d;
         autoindex on; 
         add_header Cache-Control private;
         root /data/wwwroot/mydjango/mysite1; 
         }

      error_log /var/log/nginx/yourdomain.com-error.log error;
      access_log  /var/log/nginx/yourdomain.com-access.log;

      include extra/*.conf;
      
      #------------- SSL Start --------------

      #------------- SSL End  ---------------
      }
   ```

2. 重启 Nginx 服务后，查看新安装的网站


#### 常见问题

###### 是否可以在不同版本的 Python 安装网站？

可以，创建隔离环境的时候指定具体版本，例如：

```
python3.8 -m venv --system-site-packages "/data/wwwroot/yoursite1"
```

###### 为什么需要创建隔离环境？

避免不同的应用对同一个 Python 软件包有不同的版本冲突，隔离环境完美解决此问题

###### 一个 django CMS 隔离环境可以创建多个 django CMS 项目吗？

可以

### Django

Python Runtime 中默认已经安装并启用了一个 [Django](https://github.com/django/django) 项目，其安装路径参考[此处](/zh/stack-components.md#django)。

> 以下内容仅适用于 Linux 系统，如果你使用的是 Windows 系统，请参考[历史文档](django-windows-old.md)

下面我们采用先易后难的方式，讲解用户可能需要的 Django 几种应用场景。

#### 上传 Django 应用

基于环境中默认的 Django 框架，用户可以通过**上传自己的代码**的方式来部署应用。

1. 使用 SFTP 远程连接到 Django 所在的服务器

2. 进入 */data/wwwroot/django* 目录，创建文件夹 **myproject**

3. 上传代码到 **myproject** 中

4. 根据用户应用的手册完成后续配置，可能的用的到的操作如下：
   ```
   cd /data/wwwroot/django && source bin/activate
   cd myproject
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver 0.0.0.0:9099
   ```

#### 创建 Django 应用

基于环境中默认的 Django 框架，用户通过**命令行**创建应用。下面详细说明：

1. 远程连接到 Django 所在的服务器

2. 进入到已安装的 Django 中创建新的应用，命令为 **myproject**
   ```
   cd /data/wwwroot/django
   source bin/activate
   django-admin startproject myproject
   ```

3. 修改 myproject 的配置文件 *myproject/myproject/settings.py* 中 **ALLOWED_HOSTS** 值为如下
   ```
   ALLOWED_HOSTS = ['*']
   ```
   > 也可以修改 DATABASES 参数，指定数据库

4. 指定端口下启动网站（下面设置为绑定任意IP地址）
   ```
   cd myproject
   python manage.py migrate
   python manage.py runserver 0.0.0.0:9099
   ```

5. 本地浏览器访问：*http://服务器公网IP:9099* 便可以看到 Django 界面

> 以上步骤可见，一个 Django 框架（隔离环境）下可以创建多个应用项目。

#### 安装 Django 框架

如果用户向自行安装一个新的 Django 框架，请参考上一个章节 [《安装网站》](#安装网站)

### Django on Window

1. 上传Django项目程序

2. (可选)创建虚拟环境

    在**项目根目录**下通过CMD运行命令: 

      python2如下:

      `virtualenv env`  创建一个py2的虚拟环境

     python3如下:

    ` python3 -m venv env`  创建一个py3的虚拟环境

3. 安装项目模块

   在**项目根目录**下通过CMD运行命令:

   - 如果有虚拟环境,先激活虚拟环境(如果没有创建虚拟环境跳过此步骤)

   ​             `.\env\Script\activate.bat`

   - 运行命令 `pip install requirements.txt `  安装项目所需要的模块

     ​

   > 如果项目目录下没有requirements.txt  文件  开发者请先在开发环境使用命令  pip freeze >requirements.txt  创建好文件, 非开发者请要求程序提供方提供 requirements.txt 文件



4.  根据Django不同版本创建或修改wsgi.py文件(存放目录一般在与项目目录下同名的文件夹下(同setting.py存放目录一致)), 内容如下,根据情况修改

   ```
   import os
   import sys

   sys.path.append('C:\django_prject')   #Django项目存放目录
   from django.core.wsgi import get_wsgi_application

   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_prject.settings")  # django_prject 为项目名称和项目文件夹名一致

   application = get_wsgi_application()
   ```

   ​

5. 编辑  `C:\websoft9\djangostack-1.11.10-0\apache2\conf\bitnami\bitnami-apps-vhosts.conf` 将一下内容复制进去,按照实际情况进行修改

   ```
   <VirtualHost *:80>
   ServerName www.mydomin.com    # 域名
   ErrorLog "logs/www.mydomin.com-error.log"  # 错误日志 
   CustomLog "logs/www.mydomin.com-access.log" common  # 访问日志

   Alias /static "C:\django_prject\static"   # Django静态资源访问路径和存放目录
   <Directory "C:\django_prject\static">     # 同上保持一致
       Require all granted
   </Directory>

   WSGIScriptAlias / "C:\django_prject\django_prject\wsgi.py"  # 项目wsgi.py的路径, '/' 指访问根目录
   # WSGIPythonHome /path/to/venv   # Virtualenv创建的虚拟环境路径

   <Directory "C:\django_prject\django_prject"> # Django wsgi.py 存放目录
   	<Files wsgi.py>
   		Require all granted
   	</Files>
   </Directory>

   </VirtualHost>
   ```

6. 在桌面上提供的  `manager-windows`   中的 Manage Servers 重启apache

7. 浏览器中打开测试是否正常

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

Python 域名绑定操作步骤：

1. 确保域名解析已经生效  
2. 使用 SFTP 工具登录云服务器
3. 修改 [Nginx虚拟机主机配置文件](/维护参考.md#nginx)，将其中的 **server_name** 项的值修改为你的域名
   ```text
   server
   {
   listen 80;
   server_name python.yourdomain.com;  # 此处修改为你的域名
   ...
   }
   ```
4. 保存配置文件，重启 [Nginx 服务](/维护参考.md#nginx-1)

### Nginx 连接 uWsgi

如果 uWsgi 安装在虚拟隔离环境下，Nginx 如何连接呢？

Coming soon...

### SSL/HTTPS

必须完成[域名绑定](/zh/solution-more.md)且可通过 HTTP 访问 Python ，才可以设置 HTTPS。

Python 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。因此，除了虚拟主机配置文件之外，HTTPS 设置则不需要修改 Nginx 其他文件。

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
3. 重启[Nginx服务](/维护参考.md#nginx)

#### 专题指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

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

#### 浏览器打开IP地址，无法访问 Django（白屏没有结果）？

您的服务器对应的安全组 80 端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署方案中的 Django 是如何安装的？

采用隔离环境安装

#### 9Panel 是什么？

[9Panel](https://github.com/Websoft9/9panel)是 Websoft9 公司镜像的开源组件之一，支持中英文显示，部分镜像内置了9Panel. 它是集合数据库管理、文档和支持服务的引导页面，是镜像快速入门的向导工具。基于Bootstrap+vue.js开发，几乎不会占用系统资源，也不会对系统文件进行任何修改。