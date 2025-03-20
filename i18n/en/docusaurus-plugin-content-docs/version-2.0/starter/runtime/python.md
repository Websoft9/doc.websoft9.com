---
slug: /python
sidebar_position: 1.3
tags:
  - container
  - runtime
  - Python
---

# For Python App

## Configuration options{#configs}

- Get Python version: `python3 -V`
- Python source directory: */usr/lib/python*  
- CLI: `pip`, `python`
- Application server: Gunicorn, [uWSGI](https://uwsgi-docs.readthedocs.io/)
- Compile tools: pyinstaller, cpython

## Deploy a Python application{#deploy}

Refer to: [App Runtime tutorials](./runtime)

## Manage runtime{#administrator}

- Use uWsgi for Django: `uwsgi --ini /path/django.ini`

## Troubleshoot

### Do I need to use venv?

No, [venv](https://docs.python.org/zh-cn/3/tutorial/venv.html) is only need if you want to deploy multiply applications at one Python container
