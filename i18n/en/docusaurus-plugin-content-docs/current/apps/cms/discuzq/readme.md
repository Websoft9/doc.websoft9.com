---
sidebar_position: 1
slug: /discuzq
tags:
  - Discuz!Q
  - CMS
  - 建站系统
  - Blog
---

# Discuz!Q Getting Started

[Discuz!Q](https://discuz.com/) 是开源的论坛系统，用于构建知识付费、内容变现的圈子或私域流量应用。它拥有完全开源、提供丰富接口、前后端分离、轻量化、数据独立可控、敏捷上云、快速变现七大能力。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuzq/discuzq-guim-websoft9.webp)  

If you have installed Websoft9 Discuz!Q, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. **[Get](./user/credentials)** default username and password of Discuz!Q
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Discuz!Q.
 

## Discuz!Q Initialization

### Steps for you

1. 本地电脑浏览器访问网址：*http://域名/install* 或 *http://服务器公网IP/install*, 进入初始化界面

2. 设置：数据库连接（**不建议做任何更改**）和管理员账号，然后点击【安装】进入下一步
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-setting-websoft9.png)

3. 安装完成，手机扫描右侧二维码可以进入移动端页面。  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-installok-websoft9.png)

4. 本地电脑浏览器访问网址：输入*http://域名/admin* 或 *http://服务器公网IP/admin*, 进入登录页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-admin-websoft9.png)

5. 输入账号密码（[不知道账号密码？](./user/credentials)），成功登录到 Discuz!Q 后台 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-index-websoft9.png)
    
6. 其他设置：微信公众号，小程序，微信支付等
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuzq-waychat-websoft9.png)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Discuz!Q QuickStart

下面以 **使用 Discuz!Q 构建论坛系统** 作为一个任务，帮助用户快速入门：

## Discuz!Q Setup


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Discuz!Q

通过运行`docker ps`，可以查看到 Discuz!Q 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

### Path{#path}

Discuz!Q installation directory： */data/wwwroot/discuzq*  
Discuz!Q 配置文件： */data/wwwroot/discuzq/volumes/config/config.php*  

### URL

Discuz!Q 后台地址： *http://URL/admin*

### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 9001   | Discuz!Q 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


### Version{#version}

控制台查看

### Service{#service}

```shell
sudo docker start | stop | restart | stats discuzq
```

### CLI



### API

[官方API](https://discuz.com/api-docs/v1/)