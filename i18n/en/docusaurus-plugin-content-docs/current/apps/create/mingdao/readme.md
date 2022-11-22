---
sidebar_position: 1
slug: /mingdao
tags:
  - Mingdao
  - APaaS
  - No-code Development Platform
---

# Mingdao  Getting Started

[Mingdao ](https://www.mingdao.com/en/about) is leader of APaaS, No Code Platform, it provide rapid development Tool and middle-ground application solution for enterprise customer.

![](https://alifile.mingdaocloud.com/wwwhome/dist/pack/static/src-common-mdfeature-img-2x-yy02.jpg)

> Access [Mingdao official docs](https://docs.pd.mingdao.com/) to get more reference when you use this deployment solution

Websoft9 提供的是明道云私有部署的**免费版**。它相对于**标准版**和**专业版**等收费版本来说，其有如下限制：  

- 用户数不超过 30 个
- 单个工作表最大行数 10 万行

If you have installed Websoft9 Mingdao , the following steps is for your quick start


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:38881,8880** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Mingdao 
4. [Get](./user/credentials) default username and password of Mingdao 

## Mingdao  Initialization

### Steps for you

1. Use local browser to access the URL *http://DNS:38881* or *http://Server's Internet IP:38881* to access installation wizard

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mingdao/mingdao-initial1-websoft9.png)

   > You can set any other port which you want to use

2. Then, go to 【Next】 step, start the initialization (need 3-5 minutes)

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mingdao/mingdao-initial2-websoft9.png)

3. When complete the initialization, then start to **Data installation**

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mingdao/mingdao-install1-websoft9.png)
   
   > You should register from official website to get the credential 

4. At last, **Register the administrator** account

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mingdao/mingdao-set-admin-websoft9.png)

5. Access the Mingdao's URL (e.g **http://Server's IP:8880**) to login the backend
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mingdao/mingdao-login-websoft9.png)
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mingdao/mingdao-main-app-websoft9.png)
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mingdao/mingdao-main-lib-websoft9.png)


> More guide about MingDao, please refer to [MingDao Documentation](https://docs.pd.mingdao.com/).

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**Can't visit the start page of MingDao?**

Your TCP:38881 of Security Group Rules is not allowed, so there is no response from Chrome or Firefox.

**Can the port number of the access address not need **8880**?**

Yes, but you should enable your port at **[Inbound of Security Group Rule](https://support.websoft9.com/docs/faq/tech-instance.html)** of Cloud console


**服务器重启后，服务器IP地址变化，导致工作流等一些服务无法使用**

参考：[工作流无法使用](./mingdao/admin#workflow)

**服务器重启后，程序打不开**

参考：[程序打不开](./mingdao/admin#restart)


## Mingdao QuickStart

明道云官方提供了非常不错的：[教程和视频](https://help.mingdao.com/)

## 明道云定制服务

Websoft9 作为明道的合作伙伴，具备基于明道云的软件快速构建能力。我们可以为客户提供如下的服务：

* 基于实际业务，快速建立基础数据模型
* 提炼管理流程，将业务融合到软件操作中
* 将明道云与其他系统的连接集成，打破企业数据孤岛

![](https://alifile.mingdaocloud.com/wwwhome/dist/pack/static/src-common-partnerIntroduction-img-jj2.png)

欢迎广大的客户朋友和行业合作[联系我们](./helpdesk#contact)。

## Mingdao Setup

### Configuration 

Refer to [official docs](https://docs.pd.mingdao.com)

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Log in MingDao Console and go to 【Email settings】 at 【System settings】
   ![Mingdao SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/mingdao/mingdao-smtp-websoft9.png)

3. SMTP completed  

### Reset Password

There are two main measures to reset password.

### Changing password

Take the steps below:

1. Log in the MingDao backend, open 【System Setting】 to find the user account, of which you want to change password;

2. Start to change the password.

### Forgot Password

Try to retrieve your password through e-mail when forgot it.

Follow the steps below:

Coming soon...

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Mingdao 


通过运行`docker ps`，可以查看到 明道云 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                                                                   COMMAND                  CREATED       STATUS       PORTS                       NAMES
1100b00c55ec   registry.cn-hangzhou.aliyuncs.com/mdpublic/mingdaoyun-community:2.4.1   "/Housekeeper/main -…"   2 hours ago   Up 2 hours   0.0.0.0:8880->8880/tcp      script_app_1
d6fa950fb107   registry.cn-hangzhou.aliyuncs.com/mdpublic/mingdaoyun-doc:1.2.0         "/bin/sh -c /app/ds/…"   2 hours ago   Up 2 hours   80/tcp, 443/tcp, 8000/tcp   script_doc_1
```


下面仅列出 明道云 本身的参数：

### Path{#path}

明道云目录： */data/apps/mingdao*  
明道云安装管理器目录： */data/apps/mingdao/installer*  
明道云持久化目录： */data/apps/mingdao/volume*  
明道云容器配置文件： */data/apps/mingdao/script/docker-compose.yaml*  

### Port{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 38881   | HTTP 访问 明道云初始化页面 | 可选   |
| 8880   | HTTP 访问 明道云后台（初始化完成后)  | 可选   |


### Version{#version}

控制台查看

### Service{#service}

```shell
sudo docker start | stop | restart | stats  mingdao
```

### CLI{#cli}

[常用命令](https://docs.pd.mingdao.com/deployment/docker-compose/command.html)

### API

[平台API介绍](https://help.mingdao.com/API1.html)
