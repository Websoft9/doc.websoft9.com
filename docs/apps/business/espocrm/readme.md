---
sidebar_position: 1
slug: /espocrm
tags:
  - EspoCRM
  - CRM
  - 客户成功
---

# 快速入门

[EspoCRM](https://www.espocrm.com/demo/) 是一个开源的轻量级CRM，采用响应式设计，界面非常美观大方，能够自动适应PC、平板和手机访问。功能非常全面，包括销售自动化、市场、销售过程、文档、产品、合同、知识库和工作流等功能。支持字段和表单布局客制化，便于定制。
![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/espocrm-gui-websoft9.jpg)


## 准备

部署 Websoft9 提供的 EspoCRM 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 EspoCRM 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  EspoCRM **[域名五步设置](./administrator/domain_step)** 过程


## EspoCRM 初始化向导{#init}

### 详细步骤


1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-lan-websoft9.png)

2. 选择语言之后（中国支持非常好），系统进入环境检测步骤
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-check-websoft9.png)

3. 然后点击“Install”，进入数据库参数设置界面（[查看数据库账号密码](./user/credentials)）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-dbconf-websoft9.png)

4. 数据库连接正确，点击“Next”进入管理员账号设置界面，填写管理员信息，牢记之，并进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-adminconf-websoft9.png)

5. 配置时区
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-timeconf-websoft9.png)

6. 系统提示安装成功
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-login-websoft9.png)
7. 进入后台，体验系统的完整功能

> 需要了解更多 EspoCRM 的使用，请参考官方文档：[EspoCRM Documentation](https://www.espocrm.com/documentation/)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：


## EspoCRM 使用入门

下面以 **EspoCRM 构建企业CRM** 作为一个任务，帮助用户快速入门：


## EspoCRM 常用操作

### 配置 SMTP{#smtp}

EspoCRM支持第三方的SMTP发送邮件模式，具体如下：

1. 在邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数
   
2. 待EspoCRM安装完成后，点击右上角菜单->admin，点击Email项
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-smtp-1-websoft9.png)

3. 根据下图的设置，完成SMTP参数的设置
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-smtp-2-websoft9.png)
	* Server 处请填写 smtp 服务器的地址 ；
	* Port 处请填写正确的端口号；
	* Auth 处勾选表示发邮件需要验证账号
	* Security 处请邮件服务器支持的连接协议；
	* UseName 处请输入自己的邮箱地址 ；
	* Password 处请输入SMTP密码或授权码（不同于邮箱密码）

4. 设置完成后，请点击“Send Test Email”测试设置是否成功

## 参数{#parameter}

EspoCRM 应用中包含 PHP, Apache, Docker, MySQL, phpMyAdmin 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。 

通过运行`docker ps`，可以查看到 EspoCRM 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 EspoCRM 本身的参数：

### 路径{#path}

EspoCRM 路径:  */data/wwwroot/espocrm*  

### 端口{#port}

无特殊端口


### 版本{#version}

控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats espocrm
```

### 命令行{#cli}

[Console Commands](https://docs.espocrm.com/administration/commands/)

### API
[EspoCRM REST API](https://docs.espocrm.com/development/api/)

