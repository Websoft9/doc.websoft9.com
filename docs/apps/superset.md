---
title: Superset
slug: /superset
tags:
  - Superset
  - 大数据分析
  - BI
---

import Meta from './_include/superset.md';

<Meta name="meta" />

## 入门指南{#guide}

### 登录后台{#wizard}

Websoft9 控制台安装 Superset 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

1. 通过浏览器访问，进入登录页面 

2. 输入账号密码，成功登录到 Superset 后台  
   ![](./assets/superset-console-websoft9.png)


### 分析数据

1. 登录 Superset 后，打开 **Datasets** 页面，新建一个数据库连接

2. 连接成功后，系统会导入数据库表

3. 开始对表进行分析

## 配置选项{#configs}

- 多语言（✅）：支持后台切换
- CLI：`superset [OPTIONS] COMMAND [ARGS]...`
- [配置文件](https://github.com/apache/superset/blob/master/superset/config.py)：*./src/docker/pythonpath_dev/superset_config.py*
- SMTP（✅）：配置文件中增加如下的 SMTP 配置段，重启应用后生效

   ```
   # smtp server configuration
   EMAIL_NOTIFICATIONS = True  # all the emails are sent using dryrun
   SMTP_HOST = 'smtp.163.com'
   SMTP_STARTTLS = True
   SMTP_SSL = True
   SMTP_USER = 'websoft9@163.com'
   SMTP_PORT = 465
   SMTP_PASSWORD = '#wwBJ8'
   SMTP_MAIL_FROM = 'websoft9@163.com'
   ```

## 管理维护{#administrator}

- 更换 Logo：替换容器文件 */app/superset/static/assets/images/superset-logo-horiz.png*
- 找回密码：Superset 数据库中运行下面的 SQL 语句后，用户 `admin` 的密码就被设置为 `admin123`
   ```
   update ab_user set password='pbkdf2:sha256:150000$w8vfDHis$b9c8fa353137417946766ed87cf20510da7e1e3a7b79eef37426330abef552bf' where username='admin';
   ```
- 安装数据库驱动：Superset 需在容器中安装[数据库的驱动](https://superset.apache.org/docs/databases/installing-database-drivers)方可连接对应的数据库
   ```
   # 范例：安装 MySQL 驱动
   pip install mysqlclient

   # 范例：安装 PostgreSQL 驱动
   pip install psycopg2

   # 范例：通过 pip 镜像仓库安装 PostgreSQL 驱动，解决网络慢的问题
   pip install psycopg2 -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```


## 故障

#### Superset 容器安装驱动报错？

**现象描述**：ERROR: Could not install packages due to an OSError: [Errno 13]
Check the permissions.

**原因分析**：权限不足

**解决方案**：以 `root` 身份进入容器命令模式，再安装驱动
