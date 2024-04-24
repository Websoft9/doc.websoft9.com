---
sidebar_position: 1
slug: /nopcommerce
tags:
  - nopCommerce
  - eCommerce
  - Customer Experience
---

# nopCommerce Getting Started

[nopCommerce](https://nopcommerce.com/zh) 基于 .NET 技术的 100% 开源的企业级电子商务系统，它集成了 1,500+ 插件，主题，语言包。它满足中小企业以及大型企业的电商场景，支持多供应商和多商店功能（B2B和B2C）。

![](https://netmarket.oss.aliyuncs.com/product/f8b1e93e-fba8-4fe3-b349-2a393ac01aa8.png)  

If you have installed Websoft9 nopCommerce, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. **[Get](./user/credentials)** default username and password of nopCommerce
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for nopCommerce

## nopCommerce Initialization

### Steps for you

1. 本地浏览器访问：*http://域名* 或 *http://服务器公网IP* 进入安装向导
    
2. 选择语言，设置管理员账号信息， 填写数据库信息（默认账号密码是：sa/websoft9!）  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/nopcommerce/nopcommerce-install-websoft9.png)

3. 点击安装， 进入安装进程![](http://libs.websoft9.com/Websoft9/DocsPicture/en/nopcommerce/nopcommerce-intalling-websoft9.png)

4. 安装成功后，您会看到如下界面  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/nopcommerce/nopcommerce-front-websoft9.png)

5. 访问[后台地址](#path)，开始管理 NopCommerce
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/nopcommerce/nopcommerce-backend-websoft9.png)

> More useful Jenkins guide, please refer to [Jenkins Documentation](https://www.jenkins.io/zh/doc/)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## nopCommerce QuickStart

下面以 **使用 NopCommerce 构建在线商城** 作为一个任务，帮助用户快速入门：

## nopCommerce Setup

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

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage nopCommerce

通过运行`docker ps`，可以查看到 NopCommerce 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

### Path{#path}
  

  
### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 80   | 通过 HTTP 访问 NopCommerce | 必要   |
| 443   | 通过 HTTPS 访问 NopCommerce | 可选   |
  
### URL{#url}

NopCommerce 后台地址： *http://URL/Admin*
  
### Version{#version}



### Service{#service}



### CLI{#cli}



### API

