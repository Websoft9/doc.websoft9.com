---
title: phpMyAdmin
slug: /phpmyadmin
tags:
  - Web 面板
  - 可视化
  - GUI
---

import Meta from './_include/phpmyadmin.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 phpMyAdmin 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

### 连接 MySQL{#phpmyadminconnect}

如果部署方案中包含 phpMyAdmin 等图形化工具，使用就更加便捷方便：

1. 本地浏览器电脑浏览器访问：*`http://服务器公网IP:9090`*，进入phpMyAdmin

  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-login-websoft9.png)

2. 输入数据库用户名和密码([不知道密码？](./user/credentials))

3. 登录成功后，可以管理任意数据库

  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

### 修改 root 密码{#phpmyadminmodifypw}

1. 登录phpMyAdmin后，默认页面-常规设置，点击【修改密码】

    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/websoft9-modifymysqlpw.gif)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-modifypw-websoft9.png)

2. 修改密码-&gt;保存-&gt;退出登录，刷新浏览器后便可以使用新密码登录了

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

### 管理多个 MySQL 实例

phpMyAdmin 支持多个 MySQL 实例。

修改 phpMyAdmin 的 [phpmyadmin compose 文件](#path)的对应的环境变量（PMA_HOST 更改为 PMA_HOSTS）即可支持：

```
version: "3.7"
services:
  phpmyadmin:
      image: phpmyadmin/phpmyadmin
      container_name: "phpmyadmin"
      environment:
       - PMA_HOSTS=172.17.0.1,172.17.0.2
       - PMA_PORTS=3306
       - UPLOAD_LIMIT=20M 
...
```

### 修改导入文件大小限制

phpMyAdmin 默认可导入的文件大小有限制，可通过如下步骤修改它：

1. 使用 SFTP 连接服务器，编辑 [phpmyadmin compose 文件](#path)，在环境变量处增加一个字段 `- UPLOAD_LIMIT=20M`
  ```
  version: "3.7"
  services: 
    phpmyadmin:
        image: phpmyadmin/phpmyadmin
        container_name: "phpmyadmin"
        environment:
         - PMA_HOST=172.17.0.1
         - PMA_PORT=3306
         - UPLOAD_LIMIT=20M
  ```

2. 重新创建 phpMyAdmin 容器后生效
  ```
  cd /data/apps/phpmyadmin && docker-compose up -d
  ```

## 配置选项{#configs}
## 管理维护{#administrator}

### 重置管理员密码{#resetpw}

### 更换 URL{#url}

### HTTPS 额外设置{#https}

**[标准 HTTPS 配置](./guide/appsethttps)** 完成后，可能还需要如下步骤： 

1. 步骤1

2. 步骤2

### 备份与恢复

### 升级


## 故障

#### 更改域名导致无法访问 phpMyAdmin ？

#### 访问 phpMyAdmin 出现 502 错误？{#502}