---
sidebar_position: 1
slug: /nopcommerce
tags:
  - nopCommerce
  - 电商平台
  - 客户体验
---

# 快速入门

[nopCommerce](https://nopcommerce.com/zh) 基于 .NET 技术的 100% 开源的企业级电子商务系统，它集成了 1,500+ 插件，主题，语言包。它满足中小企业以及大型企业的电商场景，支持多供应商和多商店功能（B2B和B2C）。

![](https://netmarket.oss.aliyuncs.com/product/f8b1e93e-fba8-4fe3-b349-2a393ac01aa8.png)

## 准备

部署 Websoft9 提供的 NopCommerce 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 NopCommerce 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  NopCommerce **[域名五步设置](./administrator/domain_step)** 过程


## NopCommerce 初始化向导

### 详细步骤

1. 本地浏览器访问：*http://域名* 或 *http://服务器公网IP* 进入安装向导
    
2. 选择语言，设置管理员账号信息， 填写数据库信息（默认账号密码是：sa/websoft9!）  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/nopcommerce/nopcommerce-install-websoft9.png)

3. 点击安装， 进入安装进程![](http://libs.websoft9.com/Websoft9/DocsPicture/en/nopcommerce/nopcommerce-intalling-websoft9.png)

4. 安装成功后，您会看到如下界面  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/nopcommerce/nopcommerce-front-websoft9.png)

5. 访问[后台地址](#path)，开始管理 NopCommerce
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/nopcommerce/nopcommerce-backend-websoft9.png)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## NopCommerce 使用入门

下面以 **使用 NopCommerce 构建在线商城** 作为一个任务，帮助用户快速入门：


## NopCommerce 常用操作

### SQLServer 数据管理

开启SQLServer的远程访问

本镜像默认完成了SQLServer远程访问的配置，但需要立即使用远程连接，还需要完成如下两个步骤：

1.  在Windows服务器防火墙设置中开启远程访问。控制面板-&gt;系统和安全-&gt;Windows防火墙-&gt;打开或关闭Windows防火墙 

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver2014/sqlserver-firewall001-websoft9.png) ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver2014/sqlserver-firewall002-websoft9.png)

2.  在云控制台中，开启服务器安全组的1433端口，即可远程访问。

### 域名绑定

参考 ：[配置域名](./iis#binddomain)

### SSL/HTTPS

参考 ：[配置HTTPS](./iis#https)

### 设置伪静态

参考 ：[设置伪静态](./iis#rewrite)

## 参数{#parameter}

**[通用参数表](./administrator/parameter)** 中可查看 Nginx, Apache, Docker, MySQL 等 NopCommerce 应用中包含的基础架构组件路径、版本、端口等参数。 

通过运行`docker ps`，可以查看到 NopCommerce 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 NopCommerce 本身的参数：

### 路径{#path}


### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 80   | 通过 HTTP 访问 NopCommerce | 必要   |
| 443   | 通过 HTTPS 访问 NopCommerce | 可选   |

### 网址

NopCommerce 后台地址： *http://URL/Admin*  

### 版本{#version}

```shell

```

### 服务{#service}

**服务随操作系统自动启动，如果手工修改配置参数后，需要重新启停服务。**

### 命令行{#cli}

### API
