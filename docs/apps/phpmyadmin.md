---
title: phpMyAdmin
slug: /phpmyadmin
tags:
  - 数据库
  - 可视化管理
  - Web
  - MySQL
  - MariaDB
---

import Meta from './_include/phpmyadmin.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 phpMyAdmin 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

### 连接 MySQL{#phpmyadminconnect}

如果部署方案中包含 phpMyAdmin 等图形化工具，使用就更加便捷方便：

1. 本地浏览器电脑浏览器访问后，进入phpMyAdmin
   ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-login-websoft9.png)

2. 输入 MySQL 的连接信息
   - 服务器：MySQL 主机名（Websoft9 控制台安装的 MySQL 的容器名）
   - 账号：root

3. 登录成功后，可以管理任意数据库
   ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

### 修改 root 密码{#phpmyadminmodifypw}

1. 登录 phpMyAdmin 后，默认页面-常规设置，点击【修改密码】
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-modifypw-websoft9.png)

2. 修改密码并保存，然后退出刷新浏览器后生效

### 新增数据库{#phpmyadmindb}

1. 登录phpMyAdmin后，点击左侧菜单栏的“新建”，进入如下的数据库创建界面 

    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

2. 填写数据库名-&gt;点击创建按钮，一个新的数据库变建立成功

3. 默认情况下，root拥有新建的数据库的全部权限

### 新增数据库用户{#phpmyadminuser}

> 数据库用户与数据库是分离的，是“多对多”的关系。可以通过关联使得某个用户具有某个数据库的权限

1. 登录phpMyAdmin后，点击左侧菜单栏中新打算对其新增用户的数据库（例如：mywebsoft9）

2. 点击顶部菜单栏的“权限”，找到“新增用户账户”，如下新增用户界面 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adduser-websoft9.png)

3. 根据上图填写用户名、主机地址和密码，然后关联对应的数据库和勾选权限设置

4. 点击“执行”，就完成新增用户和数据库关联了

说明：也可以登录phpMyAdmin的默认页面后，点击顶部菜单上“账户”，对用户和权限进行管理

### 数据库导入和导出{#phpmyadminexportimport}

> 导出即备份数据库，导入即恢复数据库。这个两个操作对 phpMyAdmin 来说比较简单，具体如下：

1. 登录phpMyAdmin后，选择您需要操作的数据库后，点击顶部菜单栏的“导出” 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)

2. 选择导出方式（默认为“快速”）和格式（默认为“SQL”），点击“执行”按钮

3. 数据库备份文件（.sql后缀）生成后，保存到本地完成导出工具

4. 恢复数据库，对应的是“导入”操作，具体参考下图 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-import-websoft9.png)

5. 导入文件特别要注意字符集兼容性

### MySQL 远程访问{#phpmyadminremote}

在phpMyAdmin中开启远程只需要将root账号的访问方式改成“任意方式访问”，具体如下：

1. 打开账户->找到主机名为127.0.0.1的root用户，点击“修改权限”
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/mysql-openremote001-websoft9.png)
2. 在“登录信息”选项卡中，将“主机名”下拉菜单选项更改为“任意主机”，点击执行
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/mysql-openremote002-websoft9.png)
3. 以上两步就完成了开启远程连接的工作

### 修改导入文件大小限制

phpMyAdmin 默认可导入的文件大小有限制，可通过修改编排文件的 .env 中的 `UPLOAD_LIMIT=20M` 字段。  

## 配置选项{#configs}

- 多语言（✅）
- 配置文件：/etc/phpmyadmin/config.user.inc.php

## 管理维护{#administrator}

## 故障