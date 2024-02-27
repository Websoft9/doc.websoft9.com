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

### 初始化{#wizard}

Websoft9 控制台安装 Superset 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 通过浏览器访问，进入登录页面 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-login-websoft9.png)

2. 输入账号密码，成功登录到 Superset 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-console-websoft9.png)

3. 修改密码：【Superset Admin】>【Profiles】>【Reset my Password】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-resetpw-websoft9.png)

4. 修改语言：通过右上角国旗图标设置你所需的语言
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-setlanguagech-websoft9.png)


### 从 MySQL 中分析数据

下面以连接 Superset 从 MySQL 数据源中获取数据进行分析作为范例：

1. 登录后，依次打开：【Data】>【Databases】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-database-websoft9.png)

2. 点击右上角【数据库】，输入要连接的数据地址、端口、库名以及驱动（[参考](https://docs.sqlalchemy.org/en/13/core/engines.html)）  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-connect-websoft9.png)

3. 点击【确认】，追加的数据库显示在列表中
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-connect-websoft9.png)

4. 依次打开菜单栏：【Data】>【Datesets】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-dataset-websoft9.png)

5. 点击追加 Datasets，依次选择库、SCHEMA、Table，点击追加
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-selecttable-websoft9.png)

6. 新追加的表已经显示在 Datasets 一览了
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-datalist-websoft9.png)

### 安装数据库驱动{#installdriver}

Superset 支持数十种数据库，但 Superset 默认并没有安装[数据库的驱动](https://superset.apache.org/docs/databases/installing-database-drivers)（连接程序）。

因此，需要用户进入到容器后手动安装，具体如下： 

```
# 范例：安装 MySQL 驱动
pip install mysqlclient

# 范例：安装 PostgreSQL 驱动
pip install psycopg2

# 范例：通过 pip 镜像仓库安装 PostgreSQL 驱动，解决网络慢的问题
pip install psycopg2 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 配置选项

- CLI：Usage: superset [OPTIONS] COMMAND [ARGS]...
- [API](https://superset.apache.org/docs/api) 
- [Flask-AppBuilder](https://flask-appbuilder.readthedocs.io/en/latest/security.html#supported-authentication-types)
- 配置文件：/src/docker/pythonpath_dev/superset_config.py，配置项参考：[config.py](https://github.com/apache/superset/blob/master/superset/config.py)

## 管理维护{#administrator}

### 更换 Logo

SuperSet 不支持从界面上更换 Logo，所以只能从源码角度进行 Logo 替换：

1. 上传 Logo 到服务器，命名为：superset-logo-horiz.png

2. 通过 docker cp 命令拷贝到容器。范例参考如下：

   ```
   docker cp /path/superset-logo-horiz.png superset-containername:/app/superset/static/assets/images/superset-logo-horiz.png
   ```

   > /path 是服务器上 Logo 所在的文件夹路径；superset-containername 为 SuperSet 容器名称

3. 刷新 Superset 后台页面，查看更换效果

### 配置 SMTP

Superset 配置 SMTP 发邮件的步骤：

1. 修改 *Superset 配置文件*，增加如下的 SMTP 配置段，设置好自己的参数。

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

2. 重启 Superset 容器后生效
   ```
   sudo docker restart superset-app
   ```

### 修改密码

登录 Superset 后台，修改密码：【Settings】>【User】>【Info】

![Superset 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-resetpw-websoft9.png)

### 找回密码

如果用户忘记了密码，需要连接 SuperSet 数据库，并运行重置密码的 SQL 命令。  

运行如下的 SQL 语句后，用户 admin 的密码就被设置为`admin123`

   ```
   update ab_user set password='pbkdf2:sha256:150000$w8vfDHis$b9c8fa353137417946766ed87cf20510da7e1e3a7b79eef37426330abef552bf' where username='admin';
   ```

## 故障

#### Superset 容器中安装数据库驱动报错？

**现象描述**：ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: '/home/superset'
Check the permissions.

**原因分析**：权限不足

**解决方案**：在 Websoft9 控制台中的**容器**管理界面，执行容器命令（默认会以 roo 用户连接），然后再安装驱动

#### Superset 密码正确，但仍然登录失败？{#loginfail}

**现象描述**：用户名和密码完全正确，但 Superset 仍然登录失败，错误信息 Invalid login, Please try again

**原因分析**：暂时未知

**解决方案**：重启所有 Superset 容器