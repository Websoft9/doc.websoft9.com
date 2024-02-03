---
title: TeamCity
slug: /teamcity
tags:
  - DevOps
  - CI
  - 流水线
---

import Meta from './_include/teamcity.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 TeamCity 后，通过【我的应用】进入它的编辑窗口，在**访问**标签页中获取登录地址和账号。  

1. 进入初始化页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teamcity/teamcity-start-websoft9.png)

2. 点击 "proceed", 进入 "Database connection setup" 页面，选择数据库类型为 MySQL，并下载 JDBC 驱动，填写数据库连接信息
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teamcity/teamcity-setupdb-websoft9.png)

3. 完成数据库初始化需要几分钟的时间，承认 License 协议后，创建账号就完成初始化向导
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teamcity/teamcity-account-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teamcity/teamcity-main-websoft9.png)

### 快速了解

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

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teamcity/teamcity-createbuild-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teamcity/teamcity-createbuild2-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teamcity/teamcity-createbuild3-websoft9.png)

 > [创建详细请参照官方文档](https://www.jetbrains.com/help/teamcity/creating-and-editing-build-configurations.html)
 > 创建触发器可是构建过程自动发生，无须手动执行，[更多详细操作请参照官方文档](https://www.jetbrains.com/help/teamcity/configuring-build-triggers.html) 


## 管理维护{#administrator}

## 故障