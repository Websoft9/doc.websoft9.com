---
sidebar_position: 100
slug: /apitable
tags:
  - Web 面板
  - 可视化
  - GUI
---

# 快速入门

[APITable](https://apitable.com/) 作为新一代数据生产力平台，是一款面向 API 的智能多维表格。它将复杂的可视化数据库、电子表格、实时在线协同、低代码开发技术四合为一，就连一行代码都不懂的普通职员都能轻松上手获得 IT 能力，从而极大降低企业数字化成本。
如果你正在寻找快捷可定制的业务系统、安全可靠的可视化数据库、高效协同的办公工具，那么 APITable 能满足你的丰富想象。 APITable 是自动化的项目管理工具。无论您是个人创业者还是大型团队的一员，APITable 都可以帮助您实现目标并提高生产力。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apitable/apitable-websoft9.png)

部署 Websoft9 提供的 APITable 之后，请参考下面的步骤快速入门。

## 准备{#prepare}

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 APITable 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问 APITable，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## APITable 初始化向导{#wizard}

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入初始化页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apitable/apitable-init-websoft9.png)

2. 注册用户并登录
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apitable/apitable-main-websoft9.png)

3. 点击左下角用户设定，选择属性标签即可设置自己想要的语言
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apitable/apitable-user-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apitable/apitable-preference-websoft9.png)

> 需要了解更多 APITable 的使用，请参考官方文档：[APITable Docs](https://help.apitable.com/docs/guide/tutorial)

### 碰到问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。


## APITable 使用入门{#quickstart}

APITable 提供详尽的使用[向导](https://help.apitable.com/docs/guide/tutorial)

## APITable 常用操作{#guide}

### 使用数学公式和函数

如同 Excle 一样，APITable  可让使用非常方便的使用[公式](https://help.apitable.com/docs/guide/tutorial-getting-started-with-formulas)来编辑数据。

### 导入数据

APITable 支持[导入导出 Excel 和 CSV 数据](https://help.apitable.com/docs/guide/manual-import-export)，方便数据迁移。

### 表单

APITable [表单](https://help.apitable.com/docs/guide/magic-form)可用于快速收集信息并同步保存和组织数据结果。

### 数据筛选排序

APITable 对于[数据过滤和排序](https://help.apitable.com/docs/guide/custom-view), 让用户可以轻松的编辑和展示数据。

### 创建数据模板

APITable 能将现有空间创建成[模板](https://help.apitable.com/docs/guide/faq-how-create-template), 让用户快速构建类似系统数据。

## APITable 参数{#parameter}

APITable 应用中包含 Docker, MySQL, Redis, RabbitMQ 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行 `docker ps`，查看 APITable 运行时所有的服务组件：   

```bash
CONTAINER ID   IMAGE                                      COMMAND                  CREATED          STATUS                    PORTS                                                                  NAMES
c1dd6d335b10   apitable/openresty:latest                  "/usr/bin/openresty …"   33 minutes ago   Up 31 minutes             0.0.0.0:9001->80/tcp, :::9001->80/tcp                                  apitable
0ee1201d2829   apitable/backend-server:latest             "java -Djava.securit…"   33 minutes ago   Up 32 minutes (healthy)   8081/tcp                                                               apitable-backendserver
76b992ee1d74   apitable/room-server:latest                "/start-agenthub.sh …"   33 minutes ago   Up 33 minutes             3001-3002/tcp, 3005-3007/tcp, 3333-3334/tcp                            apitable-roomserver
0fd5f8905d13   rabbitmq:3.11.9-management                 "docker-entrypoint.s…"   33 minutes ago   Up 33 minutes             4369/tcp, 5671-5672/tcp, 15671-15672/tcp, 15691-15692/tcp, 25672/tcp   apitable-rabbitmq
9ff890d3b6c4   apitable/web-server:latest                 "docker-entrypoint.s…"   33 minutes ago   Up 33 minutes             8080/tcp                                                               apitable-webserver
dabbd022bebe   apitable/imageproxy-server:latest          "/bin/sh -c './app/i…"   33 minutes ago   Up 33 minutes             8080/tcp                                                               apitable-imageproxyserver
133a7aff674e   minio/minio:RELEASE.2023-01-25T00-19-54Z   "/usr/bin/docker-ent…"   33 minutes ago   Up 33 minutes (healthy)   9000/tcp                                                               apitable-minio
6402cc3feae0   mysql:8.0.32                               "docker-entrypoint.s…"   33 minutes ago   Up 33 minutes (healthy)   3306/tcp, 33060/tcp                                                    apitable-db
98165163f373   redis:7.0.8                                "docker-entrypoint.s…"   33 minutes ago   Up 33 minutes             6379/tcp                                                               apitable-redis
```

### 路径{#path}

APITable 安装目录： */data/apps/apitable*  
APITable 数据目录： */data/apps/apitable/data*  

### 端口{#port}

无特殊端口

### 版本{#version}

```
sudo docker exec -it apitable-webserver sed -n '3p' package.json
```

### 服务{#service}

```shell
sudo docker start | stop | restart | stats apitable
sudo docker start | stop | restart | stats apitable-backendserver
sudo docker start | stop | restart | stats apitable-roomserver
sudo docker start | stop | restart | stats apitable-rabbitmq
sudo docker start | stop | restart | stats apitable-webserver
sudo docker start | stop | restart | stats apitable-imageproxyserver
sudo docker start | stop | restart | stats apitable-minio
sudo docker start | stop | restart | stats apitable-redis
```

### 命令行{#cli}

无

### API{#api}

APITable 对[REST API](https://developers.apitable.com/api/reference/)有良好的支持。