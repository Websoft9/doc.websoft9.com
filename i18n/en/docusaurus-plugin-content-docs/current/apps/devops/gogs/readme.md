---
sidebar_position: 1
slug: /gogs
tags:
  - Gogs
  - DevOps
---

# Gogs Getting Started

[Gogs](https://github.com/gogs/gogs) 是一款极易搭建的自助 Git 仓库系统，相对于 GitLab 而言 Gogs 更加轻量级。 
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-guisart-websoft9.png)


If you have installed Websoft9 Gogs, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Gogs.
4. [Get](./user/credentials) default username and password of Gogs

## Gogs Initialization

### Steps for you

1. 使用本地电脑浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入初始化页面

2. 填写数据库连接信息（**[查看预装的数据库账号密码](./user/credentials)** ）

    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-installdb-websoft9.png)

2. 设置 Gogs 的应用基本参数   

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-installset-websoft9.png)

3. 配置完成后，系统进入登录界面 

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-installreg-websoft9.png)

4. 由于还没有账户，请先点击【还没账户？马上注册】链接，开始注册一个管理员账号

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-installreg2-websoft9.png)

5. 使用新注册的账号登录 Gogs 后台 

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/gogs/gogs-backend-websoft9.png)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Gogs QuickStart

## Gogs Setup

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Gogs

下面仅列出 Gogs 本身的参数：

### Path{#path}

Gogs installation directory: */data/apps/gogs* 

### Port

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 3000   | Gogs 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


### Version

```shell
sudo docker inspect gogs
```

### Service

```shell
sudo docker start | stop | restart | stats gogs
```

### CLI

暂无

### API

暂无

