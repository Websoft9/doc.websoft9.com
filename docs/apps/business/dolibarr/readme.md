---
sidebar_position: 1
slug: /dolibarr
tags:
  - Dolibarr
  - CRM
  - 客户成功
---

# 快速入门

[Dolibarr](https://www.dolibarr.org/) 开源的一体化、模块化的业务管理软件，它尝试通过一个  ERP/CRM， 包含企业管理中所需的全部功能：产品与服务目录、库存管理、银行账户、客户名录、订单、商业建议书、合同、发票、发票与支付、费用、运输等，即插即用。   

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/dolibarr/dolibarr-gui-websoft9.webp)

## 准备

部署 Websoft9 提供的 Dolibarr 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Dolibarr 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  Dolibarr **[域名五步设置](./administrator/domain_step)** 过程


## Dolibarr 初始化向导{#init}

### 详细步骤

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/dolibarr/dolibarr-check-websoft9.png)

2. 完成通过许可协议、安装进入环境检测步骤，点击“Start”
3. 安装进入数据库配置界面（[查看数据库账号密码](./user/credentials)），然后点击”Next Step”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/dolibarr/dolibarr-dbconf-websoft9.png)

4. 安装开始验证数据库可用性和安装过程，持续点击“Next Step”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/dolibarr/dolibarr-confss-websoft9.png)

5. 安装进入管理员账号设置界面，牢记之，点击“Next Step”
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/dolibarr/dolibarr-adminconf-websoft9.png)

6. 系统安装成功
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/dolibarr/dolibarr-installss-websoft9.png)

7. 点击“Go to Dolibarr”登录后台
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/dolibarr/dolibarr-login-websoft9.png)

8. 开始体验后台
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/dolibarr/dolibarr-backend-websoft9.png)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：


## Dolibarr 使用入门

下面以 **Dolibarr 构建企业CRM** 作为一个任务，帮助用户快速入门：


## Dolibarr 常用操作

## 参数{#parameter}

Dolibarr 应用中包含 PHP, Apache, Docker, Docker, MySQL, phpMyAdmin 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 Dolibarr 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Dolibarr 本身的参数：

### 路径{#path}

Dolibarr 路径:  */data/wwwroot/dolibarr*  

### 端口{#port}

无特殊端口

### 版本{#version}

Dolibarr  控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats dolibarr
```

### 命令行{#cli}

无

### API

[Module Web Services API REST](https://wiki.dolibarr.org/index.php?title=Module_Web_Services_API_REST_(developer))