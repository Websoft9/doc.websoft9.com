---
sidebar_position: 1
slug: /python
---

# 指南

Python技术体系博大精深，我们不会在此处展开长篇大论。本章我们重点梳理我们在工作中可能涉及与Python相关的技术，以帮助更好的改善我们的产品，更好的帮助客户建立一个对Python的全局认识。

## 场景

### Nginx 连接 uWsgi{#nginxtouwsgi}


## 参数

### 路径{#path}

#### Python

除了 Python3 之外，预装包中还安装了 Virtualenv, pip 等常用的 Python 工具。

Python 应用目录： */data/wwwroot*  
Python 框架目录： */data/apps*  
Python 源码目录： */usr/lib/python*  
Python 日志目录： */data/logs/python*  

> 操作系统一般默认自带 Python2，部分操作系统默认也安装了 Python3

#### Django

**For Linux**

Django 安装目录： */data/wwwroot/django*  
Django systemctl 名称： *django.service*  

**For Windows**

采用 [Bitnami Django](https://bitnami.com/stack/django) 安装包制作而成。  

Django 安装目录： *C:\websoft9\django*  
Django 安装目录： *C:\websoft9\django\apache2\htdocs*  

### 版本号{#checkversion}

下面的命令用于查看 Python 相关的版本号

```shell
# Python version
python3 -V
python -V

# Django version
/data/wwwroot/django/bin/pip show django
``````

### 服务{#service}

Django 服务的管理方式如下：

**On Linux**

```shell
systemctl start django
systemctl stop django
systemctl restart django
systemctl status django
```

**On Windows**

服务随操作系统自动启动，如果手工修改配置参数后，需要重新启停服务，有两种方法。

* 方法一：在“开始”-> “管理工具”->“服务”中重启django***服务。

* 方法二：在C:\websoft9\django*中找到“manager-windows”。

双击打开“manager-windows”，可以进行服务启停、参数配置。

### 命令行{#cmd}

主要包括 pip, django-admin, python 等命令