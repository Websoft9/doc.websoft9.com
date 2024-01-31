---
sidebar_position: 1
slug: /suitecrm
tags:
  - SuiteCRM
  - 企业管理
  - CRM
---

# 快速入门

[SuiteCRM](https://suitecrm.com/) 是一个屡获殊荣的企业级的、强大的、可定制的，免费的CRM系统。包括市场、销售过程管理、协作管理、工作流、门户等功能模块。所有功能全部开源，完全具备商业CRM软件媲美的功能和架构。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-ui.png)

## 准备

部署 Websoft9 提供的 SuiteCRM 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 SuiteCRM 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  SuiteCRM **[域名五步设置](./administrator/domain_step)** 过程

## SuiteCRM 初始化向导{#init}

### 详细步骤

1. 本地浏览器访问：*http://域名* 或 *http://服务器公网IP* ，进入登陆页面
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-init1-websoft9.png)

2. 根据向导提示，选择【Next】初始化设置
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-init2-websoft9.png)

3. 初始化设置完成，开始体验后台
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-init3-websoft9.png)

> 需要了解更多SuiteCRM 的使用，请参考官方文档：[EspoCRM Documentation](https://suitecrm.com/wiki/index.php/Main_Page)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：


## SuiteCRM 使用入门

下面以 **SuiteCRM 构建企业CRM** 作为一个任务，帮助用户快速入门：

## SuiteCRM 常用操作

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数
   
2. 打开SuiteCRM->Administartor->Admin->Email->Email Setting，打开邮件发送设置项（Outgoing Mail Configuration）

3. 设置无误后，请点击“Send Test Email”进行测试以验证

另外，SuiteCRM安装过程（第三步）也可以设置SMTP，参考下图：

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-smtp-websoft9.png)

### 安装中文包

SuiteCRM默认安装只有英文，需要中文或其他语言，需要下载语言包，然后通过后台进行安装，以中文为例，具体如下：

1.  下载[中文语言包](https://crowdin.com/project/suitecrmtranslations/zh-CN) – 存到本地电脑上
2.  以Admin身份进入SuiteCRM，进入 “admin-Admin Tools-Module loader”
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-lmodule-websoft9.png)
3.  Upload file->Install it->Commit
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-linstall-websoft9.png)
4.  Go to “Admin” enter “Repair” and apply “Quick repair and rebuild” for languages
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-repair-websoft9.png)
5.  退出 SuiteCRM
6.  先选择所需的语言，再登录
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-logincn-websoft9.png)


## SuiteCRM 参数{#parameter}

SuiteCRM 应用中包含 PHP, Nginx, Apache, Docker, MySQL等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 SuiteCRM 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                         COMMAND                  CREATED          STATUS                 PORTS                                                                               NAMES
f705c84dd8d1   bitnami/suitecrm:latest       "/opt/bitnami/script…"   27 seconds ago   Up 26 seconds          8443/tcp, 0.0.0.0:9002->8080/tcp, :::9002->8080/tcp                                 suitecrm
5d2d02d4c02e   mariadb:10.6                  "docker-entrypoint.s…"   29 seconds ago   Up 26 seconds          0.0.0.0:3306->3306/tcp, :::3306->3306/tcp                                           suitecrm-db

```

### 路径{#path}

SuiteCRM 安装目录:  */data/apps/suitecrm*  
SuiteCRM 站点目录: */data/apps/suitecrm/data/suitecrm*

### 端口{#port}

无特殊端口

### 版本{#version}

```
docker exec -i suitecrm cat /bitnami/suitecrm/VERSION
```

### 服务{#service}

```shell
sudo docker start | stop | restart | stats suitecrm
sudo docker start | stop | restart | stats suitecrm-db
```

### 命令行{#cli}

无

### API

[API Versions](https://docs.suitecrm.com/developer/api/)

