---
title: Python
slug: /python
tags:
  - 运行环境
  - runtime
  - Python
---

import Meta from '../apps/_include/python.md';

<Meta name="meta" />

## 配置选项{#configs}

- 版本号： `python3 -V`
- Python 源码目录： */usr/lib/python*  
- 命令行：`pip`, `python`
- 应用服务器：Gunicorn, [uWSGI](https://uwsgi-docs.readthedocs.io/)
- 二进制编译工具：pyinstaller, cpython
- 解释器：[CPython](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/python-interpreter-websoft9.png)

## 部署网站

### 部署 FastAPI {#guide}

下面通过 [ Web 框架 FastAPI](https://github.com/tiangolo/fastapi) 为例，描述应用安装过程：

1. Websoft9 控制台安装 Python 运行环境

2. Websoft9 控制台，我的应用管理的 **编排** 标签页，开始对应用进行编排

3. 修改 **.src/cmd.sh**，注释掉的安装脚本生效
   ```
    pip install fastapi uvicorn[standard]
    cat << 'EOF' > main.py
    from typing import Union

    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    EOF
    uvicorn main:app --host 0.0.0.0 --port 8080
   ```

4. Websoft9 控制台 **重建应用** 后生效，方可访问此 Web 应用 

### 部署 Django

下面再以 Django 为例，提供完整的在容器内部运行命令的部署方法：

1. Websoft9 控制台安装 Python 运行环境

2. 通过 Websoft9 控制台进入 Python 容器的命令模式，再分别运行如下命令：
   ```
   #1 安装 django CMS 命令行工具（用于创建和管理 django CMS 项目）
   pip install django

   #2 基于命令行创建一个项目（创建时会拉取所有依赖的源码）
   django-admin startproject mysite1

   #3 允许所有来自的外部的访问
   sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = ['*']/" mysite1/mysite1/settings.py

   #4 初始化 Django 项目
   cd mysite1
   python manage.py migrate

   #5 在后台运行 Django，并输出日志到 output.log 文件
   nohup python manage.py runserver 0.0.0.0:8080 > output.log 2>&1 &
   ```
   > 如果容器重启了，需进入容器后再次运行 #5

3. 此时，即可访问此 Web 应用

### 使用 uWsgi 发布网站

上述的部署 Django 也可以通过 [uWSGI](https://uwsgi-docs.readthedocs.io/) 发布网站（替代 Django 内置的 web 服务器）。
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/django-behind-uwsgi-nginx.png)

下面是一个 uWsgi 应用在 Django 上的示例：

1. 进入 Python 容器，pip install uwsgi

2. 在 Django 目录中新增一个 uWsgi 配置文件，命名为：django.ini 
   ```
   [uwsgi]
   master        = true
   protocol      = uwsgi
   http          = 0.0.0.0:8001
   wsgi-file     = /path/wsgi.py
   chdir         = /path
   buffer-size   = 8192
   enable-threads= true
   close-on-exec = true
   uid           = nginx
   gid           = nginx
   ```

3. uWsgi 命令启动应用
   ```
   uwsgi --ini /path/django.ini
   ```

## 管理维护{#administrator}

### pip 包管理器

Python 环境中使用 pip 命令完成各种不同类型的包管理操作：

    ```
    #查看pip版本
    pip --version

    #查看包信息
    pip show Django

    #列出所有已安装的包
    pip list

    #查看可升级的包
    pip list -o

    #安装Python包，以Django为例
    pip install Django              # 安装
    pip install Django -U           # 安装并更新至最新版本
    pip install Django==2.1.7       # 指定版本
    pip install 'Django>=2.1.7'     # 最小版本

    #升级Python模块
    pip install --upgrade django==2.1.7

    #pip自身的升级
    python -m pip install --upgrade pip  
    python3 -m pip install --upgrade pip
    ```


## 问题与故障

#### 是否支持 Python 虚拟环境？

Python 默认包含虚拟环境模块 [venv](https://docs.python.org/zh-cn/3/tutorial/venv.html)，但不建议通过虚拟环境部署多个应用。

#### Python 程序跨平台逻辑？

Python 程序由解释器（Interpreter）即 Python 的运行内核处理，它具有编译器和虚拟机两方面的功能。

* 编译器：词法分析，语法解释，将 Python 代码编译成字节码（一种类似汇编的代码）
* 虚拟机：模仿可执行文件的入栈出栈调用顺序执行 Python 程序

正因为有了解释器的存在，使得 Python 程序无需编译成机器码，就可以实现跨平台运行。

