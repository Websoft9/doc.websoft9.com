---
sidebar_position: 1
slug: /alfresco
tags:
  - Alfresco
  - 企业管理
  - ERP
---

# 快速入门

[Alfresco Community Edition](https://www.alfresco.com/ecm-software/alfresco-community-editions) 是开源的企业内容管理系统，它面向大中型客户，作为一个灵活、可扩展的 ECM 平台，Alfresco Content Services 支持一系列用例，包括内容服务、信息治理、上下文搜索和洞察力，与领先业务应用程序 SAP, IBM Lotus, Microsoft Office, SharePoint 和 Google Docs 等轻松集成。

![Alfresco 系统架构](https://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-arcgui-websoft9.png)

## 准备

部署 Websoft9 提供的 Alfresco 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Alfresco 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  Alfresco **[域名五步设置](./administrator/domain_step)** 过程


## Alfresco 初始化向导{#init}

### 详细步骤

1. 使用本地浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 点击 [Alfresco Repository]->[Alfresco Share]
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](./user/credentials)），成功登录到 Alfresco 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-consolegui-websoft9.png)

3. Alfresco会自动根据浏览器语言来选择程序语言

> 需要了解更多 Alfresco 的使用，请参考官方文档：[Alfresco Documentation](https://docs.alfresco.com/content-services/community/using/content/) 和 [Alfresco Videos](https://docs.alfresco.com/content-services/latest/tutorial/video/)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**访问 Alfresco 出现 502 错误？**

Alfresco 开机启动最少需要 10 分钟，请耐心等待


## Alfresco 使用入门

下面以 **Alfresco 传递数据** 作为一个任务，帮助用户快速入门：

- 后台仪表盘
  ![Alfresco台仪表盘](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-adminui-websoft9.png)

- 我的文档
  ![Alfresco我的文档](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-mydocs-websoft9.png)

- 共享文档
  ![Alfresco共享文档](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-sharedocs-websoft9.png)

- 增加多用户
  ![Alfresco增加多用户](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-addusers-websoft9.png)

- 增加组（部门）
  ![Alfresco增加组（部门）](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-addgroup-websoft9.png)

- 工作流（审批）
  ![Alfresco工作流（审批）](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-workflow-websoft9.png)

## Alfresco 常用操作

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数
   
2. 登录 Alfresco 控制台，设置 SMTP 参数（暂未找到具体方案）

### 重置密码

常用的 Alfresco 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码

1. 登录 Alfresco 后台，右上角依次打开：【Administrator】>【我的个人档案】
  ![Alfresco 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-modifypw-websoft9.png)

2. 点击【更改密码】，开始修改密码

#### 找回密码

如果用户忘记了密码，需要通过修改数据库中的密码信息来重置密码：

1. 使用 **SSH** 连接到 Alfresco 所在的服务器

2. 进入到 alfresco 数据库的 PSQL 交互式状态
   ```
   docker exec -it alfresco-postgres psql -U alfresco -d alfresco
   ```

3. 运行如下的修改密码命令（新的密码为 **admin**）
   ```
   UPDATE alf_node_properties SET string_value='209c6174da490caeb422f3fa5a7ae634' WHERE node_id=4 and qname_id=10
   ```

4. 退出容器交互式模式，回到服务器命令行中重启所有容器后生效
   ```
   cd /data/wwwroot/alfresco
   docker-compose restart
   ```

## 参数{#parameter}

Alfresco 应用中包含 Nginx, Docker, PostgreSQL, pgAdmin 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 Alfresco 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                                                  COMMAND                  CREATED             STATUS             PORTS                                                                                                                                                                                NAMES
3d2afa8a1cc7   alfresco/alfresco-acs-nginx:3.1.1                      "/entrypoint.sh"         About an hour ago   Up About an hour   80/tcp, 0.0.0.0:8080->8080/tcp, :::8080->8080/tcp                                                                                                                                    alfresco-proxy
b42251c78a71   alfresco/alfresco-search-services:2.0.1                "/bin/sh -c '$DIST_D…"   About an hour ago   Up About an hour   10001/tcp, 0.0.0.0:8083->8983/tcp, :::8083->8983/tcp                                                                                                                                 alfresco-solr6
a381a9646f4b   alfresco/alfresco-transform-core-aio:2.3.10            "/bin/sh -c 'java $J…"   About an hour ago   Up About an hour   0.0.0.0:8090->8090/tcp, :::8090->8090/tcp                                                                                                                                            alfresco-transform
af14e4d3cd86   alfresco/alfresco-content-repository-community:7.0.0   "catalina.sh run -se…"   About an hour ago   Up About an hour   8000/tcp, 8080/tcp, 10001/tcp                                                                                                                                                        alfresco-content
50059f56edff   postgres:13.1                                          "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp                                                                                                                                            alfresco-postgres
692e2acf019d   alfresco/alfresco-activemq:5.16.1                      "/bin/sh -c '${ACTIV…"   About an hour ago   Up About an hour   0.0.0.0:5672->5672/tcp, :::5672->5672/tcp, 0.0.0.0:8161->8161/tcp, :::8161->8161/tcp, 0.0.0.0:61613->61613/tcp, :::61613->61613/tcp, 0.0.0.0:61616->61616/tcp, :::61616->61616/tcp   alfresco-activemq
ca3a6baf750e   alfresco/alfresco-share:7.0.0                          "/usr/local/tomcat/s…"   About an hour ago   Up About an hour   8000/tcp, 8080/tcp                                                                                                                                                                   alfresco-share
4a0c8d7e6c2e   dpage/pgadmin4                                         "/entrypoint.sh"         About an hour ago   Up About an hour   443/tcp, 0.0.0.0:9090->80/tcp, :::9090->80/tcp                                                                                                                                       pgadmin
```


### 路径{#path}

Alfresco 安装目录： */data/apps/alfresco*  
Alfresco 容器存储目录： */data/apps/alfresco/data/alfresco*  

### 端口{#port}

无特殊端口


### 版本{#version}

```shell
docker images |grep alfresco-share |awk '{print $2}'
```

### 服务{#service}

```shell
sudo docker-compose start | stop | restart alfresco
```

### 命令行{#cli}

暂未发现

### API

[ReST API Guide](https://docs.alfresco.com/content-services/latest/develop/rest-api-guide/)

