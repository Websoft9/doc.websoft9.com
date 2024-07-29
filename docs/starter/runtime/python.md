---
title: Python
slug: /python
sidebar_position: 1.3
tags:
  - 运行环境
  - runtime
  - Python
---

## 配置选项{#configs}

- 版本号： `python3 -V`
- Python 源码目录： */usr/lib/python*  
- 命令行：`pip`, `python`
- 应用服务器：Gunicorn, [uWSGI](https://uwsgi-docs.readthedocs.io/)
- 二进制编译工具：pyinstaller, cpython
- 解释器：[CPython](./assets/python-interpreter-websoft9.png)

## 部署网站{#deploy}

参考：[Web Runtime 入门指南](../runtime)

## 环境管理{#administrator}

- 使用 uWsgi 发布 Django：`uwsgi --ini /path/django.ini`
  ![](./assets/runtime-uwsgi-websoft9.png)

## 问题与故障

#### 是否支持 Python 虚拟环境？

支持 [venv](https://docs.python.org/zh-cn/3/tutorial/venv.html)，但不建议使用
