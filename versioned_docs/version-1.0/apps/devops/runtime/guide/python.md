---
sidebar_position: 4
slug: /runtime/python
tags:
  - Python
  - Django
  - 运行环境
---

# Python 应用

## 安装 Python 应用

### 检查 Python

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

### 安装步骤说明

在 Python Runtime 环境上安装不同的网站有一定的差异，但总体上是遵循如下几个步骤的：

1. 创建一个独立的隔离环境
2. 准备好网站的源码（通过命令行拉取或上传代码）
3. 修改配置信息（端口、数据库、IP地址等）
4. 启动网站

> 务必牢记以上几个步骤，不要一开始就落入技术陷阱中

### 开始安装应用{#installdjango}

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

## Django 

下面我们采用先易后难的方式，讲解用户可能需要的 Django 几种应用场景。

### 上传 Django 应用

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

### 创建 Django 应用

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

### 安装 Django 框架

如果用户向自行安装一个新的 Django 框架，请参考上一个章节 [《开始安装应用》](#installdjango)

## 维护 Python 环境

参考本文的相关专题：[《Python 指南》](../python) 和 [《Python 进阶》](../python/advanced) 
