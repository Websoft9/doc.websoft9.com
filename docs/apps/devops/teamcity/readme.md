---
sidebar_position: 100
slug: /teamcity
tags:
  - Web 面板
  - 可视化
  - GUI
---

# 快速入门

TeamCity 介绍

部署 Websoft9 提供的 TeamCity 之后，请参考下面的步骤快速入门。

## 准备{#prepare}

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 TeamCity 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问 TeamCity，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## TeamCity 初始化向导{#wizard}

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入初始化页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teamcity/teamcity-start-websoft9.png)

2. 点击[proceed],进入[Database connection setup]页面，选择数据库类型为MySQL，并下载JDBC驱动，填写数据库连接信息
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teamcity/teamcity-setupdb-websoft9.png)

3. 完成数据库初始化需要几分钟的时间，承认license协议后，创建账号就完成初始化向导
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teamcity/teamcity-account-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teamcity/teamcity-main-websoft9.png)

### 碰到问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

**TeamCity 能打开，但总是出现 502 错误？**  

参阅：

## TeamCity 使用入门{#quickstart}

下面以 **××××** 作为一个任务，帮助用户快速入门：

## TeamCity 常用操作{#guide}

### 创建项目

创建项目的方式可以通过外部URL或者手动创建，下面我们通过已有github项目创建一个项目

1. 输入外部URL以及用户和密码信息

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teamcity/teamcity-createprj-websoft9.png)

2. 点击[proceed]，项目会提示创建成功

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teamcity/teamcity-createconfirm-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teamcity/teamcity-createsuccess-websoft9.png)

 > [更多信息请参照官方文档](https://www.jetbrains.com/help/teamcity/creating-and-editing-projects.html)
 
### 创建构建配置

创建构建配置是自动化的核心，会指定是对哪个项目，做一个具体化的具体构建过程。
这里需要说明一点，当指定外部URL构建时，构建是针对外部项目的，teamcity本地项目的代码提交不会触发构建。

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teamcity/ teamcity-createbuild-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teamcity/teamcity-createbuild2-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teamcity/teamcity-createbuild3-websoft9.png)

 > [创建详细请参照官方文档](https://www.jetbrains.com/help/teamcity/creating-and-editing-build-configurations.html)
 > 创建触发器可是构建过程自动发生，无须手动执行，[更多详细操作请参照官方文档](https://www.jetbrains.com/help/teamcity/configuring-build-triggers.html) 
 
### 重置管理员密码{#resetpw}

忘记管理员密码时，请参考如下方案重置密码：  

### 域名额外配置（修改 URL）{#dns}

**[域名五步设置](./administrator/domain_step)** 完成后，需设置 TeamCity 的 URL:  

1. 步骤1

2. 步骤2

### HTTPS 额外设置{#https}

**[标准 HTTPS 配置](./administrator/domain_https)** 完成后，可能还需要如下步骤： 

1. 步骤1

2. 步骤2

## TeamCity 参数{#parameter}

TeamCity 应用中包含 Docker, Portainer 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行 `docker ps`，查看 TeamCity 运行时所有的服务组件：   

```bash
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS          PORTS                                       NAMES
b1ab51af14f8   jetbrains/teamcity-server:latest   "/run-services.sh"       21 minutes ago   Up 21 minutes   0.0.0.0:8111->8111/tcp, :::8111->8111/tcp   teamcity
bd4d59a4adcf   mysql:8.0                          "docker-entrypoint.s…"   21 minutes ago   Up 21 minutes   3306/tcp, 33060/tcp                         teamcity-db

```

### 路径{#path}

TeamCity 安装目录： */data/apps/teamcity*   
TeamCity 数据目录： */data/apps/teamcity/data/teamcity_data*  
TeamCity 日志目录： */data/apps/teamcity/data/teamcity_logs*  

### 端口{#port}

无特殊端口

### 版本{#version}

控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats teamcity
sudo docker start | stop | restart | stats teamcity-db
```

### 命令行{#cli}

### API{#api}
