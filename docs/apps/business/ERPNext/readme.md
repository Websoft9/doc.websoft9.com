---
sidebar_position: 1
slug: /erpnext
tags:
  - ERPNext
  - 企业管理
  - ERP
---

# 快速入门

[ERPNext](https://erpnext.com/)  是一个 100% 开源的 ERP，基于 Python 和 Node 开发，它功能全面，包含会计、人力资源、制造、网站、电商、CRM、资产管理、客服工作台等全面的功能。非常合适作为 SAP 的替代品，全球已经有超过 5,000 家企业客户使用。

![](http://libs.websoft9.com/Websoft9/DocsPicture/en/erpnext/erpnext-adminui-websoft9.png)


部署 Websoft9 提供的 ERPNext 之后，需完成如下的准备工作：

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 ERPNext 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  ERPNext **[域名五步设置](./dns#domain)** 过程


## ERPNext 初始化向导{#init}

### 详细步骤

1. 使用本地电脑 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入初始化页面
   ![erpnext安装登录](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](./setup/credentials#getpw)），选择语言， 进入下一步 
   ![erpnext安装](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-language-websoft9.png)

3. 根据安装向导依次完成后续步骤

4. 安装完成之后，ERPNext 会弹出如下界面
   ![erpnext后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-cpsetup-websoft9.png)

   可能会出现安装错误提示，此时需要反复安装：
   ![erpnext 向导安装报错](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-wizarderror-websoft9.png)

5. ERPNext 顶部菜单中提供了搜索框，用于快速检索并进入 ERPNext 所有的功能
   ![erpnext 快速检索](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-sbar-websoft9.png)

6. 通过检索功能，进入【用户】设置，可以管理当前系统下所有账号
   ![erpnext 用户管理](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-users-websoft9.png)


> 需要了解更多 ERPNext 的使用，请参考官方文档：[ERPNext Documentation](https://docs.erpnext.com)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**ERPNext 服务启动失败**

请确认hostname是否包含字符串 "."，例如 erpnext12.14.0对于ERPNext来说是一个不合规的hostname

你可以使用下列命令来修改hostname：

```
hostnamectl set-hostname erpnext
```


## ERPNext 使用入门

下面以 **ERPNext 构建企业ERP** 作为一个任务，帮助用户快速入门：



## ERPNext 常用操作

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数
   
2. 登录 ERPNext控制台，在【设置】>【电子邮件域名】填写SMTP参数
![ERPNext SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/erpnext/erpnext-smtp-websoft9.png)

3. 点击【保存】后，系统后进行一个 SMTP 初步验证，验证通过才能保存成功

### 配置域名{#dns}

参考： **[域名五步设置](./dns#domain)** 

1. 确保域名解析已经生效  
2. 修改 ERPNext 环境变量，绑定域名:
   进入 ERPNext 目录 /data/wwwroot/erpnext
   修改 .env 文件域名配置项
   ```
   ...
   APP_SITE_URL=your domain
   APP_SITE_NAME=`your domain`
   ...
   ```
3. 重启 ERPNext 
   ```
   docker-compose up -d 
   ```

### 配置 HTTPS{#https}

参考： **[HTTPS 配置](./dns#https)**

### 重置密码

常用的 ERPNext 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码


1. 登录 ERPNext后台，依次打开：【设置】>【个人设置】，找到修改密码项
  ![ERPNext 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-modifypw-websoft9.png)

2. 直接设置新密码，保存后生效

#### 找回密码

如果用户忘记了 ERPNext 密码，可以通过如下的命令直接设置一个新密码：

```
sudo -H -u erpnext bash -c "cd /data/wwwroot/frappe-bench && export GIT_PYTHON_REFRESH=quiet && /usr/local/bin/bench set-admin-password newpassword"
```

### 使用RDS

如果用户不喜欢使用服务器上安装的 MariaDB，而希望迁移到云数据库中（RDS），大致流程：

1. 备份已有数据库，并导入到 RDS 中（适合于 ERPNext 已经完成安装）

2. 修改 [ERPNext 容器配置文件:/data/wwwroot/erpnext/.env](#path) 中的数据库相关信息
   ```
   DB_MRAIADB_USER=root
   DB_MARIADB_PASSWORD=123456
   DB_MARIADB_HOST=mariadb
   DB_MARIADB_PORT=3306
   DB_MARIADB_VERSION=10.6
   ```

   > DB_MARIADB_HOST 设置为外部数据库地址

3. 重新运行容器
   ```
   cd /data/wwwroot/erpnext
   docker-compose up -d
   ```

4. 测试更改数据库后的连接可用性


## 参数{#parameter}

**[通用参数表](./setup/parameter)** 中可查看 Nginx, Apache, Docker, MySQL 等 ERPNext 应用中包含的基础架构组件路径、版本、端口等参数。 

通过运行`docker ps`，可以查看到 ERPNext 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 ERPNext 本身的参数：

### 路径{#path}

ERPNext 路径:  */data/wwwroot/erpnext*  
ERPNext 数据库配置文件: */data/wwwroot/erpnext/.env*  
ERPNext 日志路径:  */data/wwwroot/erpnext/volumes/erpnext-logs-vol*  
ERPNext 应用路径 : */data/wwwroot/frappe-bench/volumes/erpnext-site-vol*  
ERPNext 附件路径:  */data/wwwroot/frappe-bench/volumes/erpnext-assets-vol*   

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 8080   | ERPNext 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


### 版本{#version}

```shell
sudo cat /data/logs/install_version.txt
```

### 服务{#service}

```shell
```

### 命令行{#cli}

### API

参考： [ERPNext API](https://frappeframework.com/docs/user/en/api)

### 参考{#ref}

