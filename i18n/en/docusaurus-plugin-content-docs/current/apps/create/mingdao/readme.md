---
sidebar_position: 1
slug: /mingdao
tags:
  - 明道云
  - APaaS
  - 无代码平台
---

# 快速入门

[明道云](https://www.mingdao.com/) 是一个无代码开发平台（aPaas, No-Code, Low-Code），它可以让企业的业务部门在**不需要编程序**的情况下，自行创作出完全符合实际需求的软件系统。它的主要价值是：大大降低软件生产成本的同时，进一步提高软件交付的成功率。

![](https://alifile.mingdaocloud.com/wwwhome/dist/pack/static/src-common-mdfeature-img-2x-yy02.jpg)

Websoft9 提供的是明道云私有部署的**免费版**。它相对于**标准版**和**专业版**等收费版本来说，其有如下限制：  

- 用户数不超过 30 个
- 单个工作表最大行数 10 万行

## 准备

部署 Websoft9 提供的 明道云 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的  **TCP:38881** 和 **TCP:8880**  端口已经开启
3. 在服务器中查看 明道云 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  明道云 **[域名五步设置](./administrator/domain_step)** 过程


## 明道云初始化向导{#init}

### 详细步骤

明道云安装向导包含三个过程：初始化、安装数据、设置管理员：

1. 使用本地电脑的浏览器访问网址：*http://服务器公网IP:38881* 进入初始化页面

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-initial1-websoft9.png)

   > 上图中访问地址的默认端口 8880 可自行设置为其他端口号

2. 设置访问地址后，进入【下一步】，开始初始化（过程持续约 3~5 分钟）

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-initial2-websoft9.png)

3. 初始化完成后，开始**安装数据** （此过程中会引导至明道云官网申请密钥）

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-install1-websoft9.png)
   

4. 完成**注册系统管理员**信息（务必牢记账号密码）

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-set-admin-websoft9.png)

5. 访问第1步设置的访问地址（例如：**http://服务器公网IP:8880**），登陆明道云后台

    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-login-websoft9.png)
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-main-app-websoft9.png)
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-main-lib-websoft9.png)


> 需要了解更多 明道云 的使用，请参考：[明道云官方文档](https://help.mingdao.com/)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：


**浏览器打开IP地址，无法访问 明道云（白屏没有结果）**

您的服务器对应的安全组 38881 端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容


**访问地址的端口号可以不用 **8880** 吗**

可以，但需要在云控制台安全组中，检查 **Inbound（入）规则** 下您所使用的端口确保开启


**服务器重启后，服务器IP地址变化，导致工作流等一些服务无法使用**

参考：[工作流无法使用](./mingdao/admin#workflow)

**服务器重启后，程序打不开**

参考：[程序打不开](./mingdao/admin#restart)


## 明道云使用入门

明道云官方提供了非常不错的：[教程和视频](https://help.mingdao.com/)

## 明道云定制服务

Websoft9 作为明道的合作伙伴，具备基于明道云的软件快速构建能力。我们可以为客户提供如下的服务：

* 基于实际业务，快速建立基础数据模型
* 提炼管理流程，将业务融合到软件操作中
* 将明道云与其他系统的连接集成，打破企业数据孤岛

![](https://alifile.mingdaocloud.com/wwwhome/dist/pack/static/src-common-partnerIntroduction-img-jj2.png)

欢迎广大的客户朋友和行业合作[联系我们](./helpdesk#contact)。

## 明道云常用操作


### 基础设置

请参考官方提供的：[《私有版维护文档》](https://docs.pd.mingdao.com/)，包括：短信设置、对象存储设置、网络访问、环境变量、服务管理等

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数
   
2. 登录明道云，打开右上角用户图标下的【系统配置】，点击【邮件服务设置】开始配置
   ![明道云 SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-smtp-websoft9.png)

3. 完成设置

### 重置密码

常用的 明道云 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码

1. 登录 明道云 后台，依次打开：【系统设置】>【用户管理】，找到所需修改密码的账号对象

2. 开始修改密码

#### 找回密码

方案有待完善

## 参数{#parameter}

明道云 应用中包含 Nginx, Docker 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行`docker ps`，可以查看到 明道云 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                                                                   COMMAND                  CREATED       STATUS       PORTS                       NAMES
1100b00c55ec   registry.cn-hangzhou.aliyuncs.com/mdpublic/mingdaoyun-community:2.4.1   "/Housekeeper/main -…"   2 hours ago   Up 2 hours   0.0.0.0:8880->8880/tcp      script_app_1
d6fa950fb107   registry.cn-hangzhou.aliyuncs.com/mdpublic/mingdaoyun-doc:1.2.0         "/bin/sh -c /app/ds/…"   2 hours ago   Up 2 hours   80/tcp, 443/tcp, 8000/tcp   script_doc_1
```


下面仅列出 明道云 本身的参数：

### 路径{#path}

明道云目录： */data/wwwroot/mingdao*  
明道云安装管理器目录： */data/wwwroot/mingdao/installer*  
明道云持久化目录： */data/wwwroot/mingdao/volume*  
明道云容器配置文件： */data/wwwroot/mingdao/script/docker-compose.yaml*  

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 38881   | HTTP 访问 明道云初始化页面 | 可选   |
| 8880   | HTTP 访问 明道云后台（初始化完成后)  | 可选   |


### 版本{#version}

控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats  mingdao
```

### 命令行{#cli}

[常用命令](https://docs.pd.mingdao.com/deployment/docker-compose/command.html)

### API

[平台API介绍](https://help.mingdao.com/API1.html)
