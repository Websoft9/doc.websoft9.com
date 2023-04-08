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

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apitable/apitable-head-websoft9.png)

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

2. 输入邮件和密码，登录到主页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apitable/apitable-main-websoft9.png)

### 碰到问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

参阅：

## APITable 使用入门{#quickstart}

下面以 **××××** 作为一个任务，帮助用户快速入门：

## APITable 常用操作{#guide}

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数

2. 填写 APITable 邮件相关配置

3. 测试邮件发送是否可用

### 安装插件{#plugin}

### 重置管理员密码{#resetpw}

忘记管理员密码时，请参考如下方案重置密码：  


## APITable 参数{#parameter}

APITable 应用中包含 Docker, Portainer 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行 `docker ps`，查看 APITable 运行时所有的服务组件：   

```bash
CONTAINER ID   IMAGE                                      COMMAND                  CREATED          STATUS                    PORTS                                                                  NAMES
af17feebaf9f   apitable/openresty:latest                  "/usr/bin/openresty …"   10 minutes ago   Up 7 minutes              0.0.0.0:9001->80/tcp, :::9001->80/tcp                                  apitable
a818975b2753   apitable/backend-server:latest             "java -Djava.securit…"   10 minutes ago   Up 9 minutes (healthy)    8081/tcp                                                               apitable-backend-server-1
8b1a98d4e740   apitable/room-server:latest                "/start-agenthub.sh …"   10 minutes ago   Up 10 minutes             3001-3002/tcp, 3005-3007/tcp, 3333-3334/tcp                            apitable-room-server-1
93d1cbfd3d3c   apitable/web-server:latest                 "docker-entrypoint.s…"   10 minutes ago   Up 10 minutes             8080/tcp                                                               apitable-web-server-1
852a34d31086   apitable/imageproxy-server:latest          "/bin/sh -c './app/i…"   10 minutes ago   Up 10 minutes             8080/tcp                                                               apitable-imageproxy-server-1
d29ed28c9843   rabbitmq:3.11.9-management                 "docker-entrypoint.s…"   10 minutes ago   Up 10 minutes             4369/tcp, 5671-5672/tcp, 15671-15672/tcp, 15691-15692/tcp, 25672/tcp   apitable-rabbitmq-1
acfd06f75fee   redis:7.0.8                                "docker-entrypoint.s…"   10 minutes ago   Up 10 minutes             6379/tcp                                                               apitable-redis-1
0d4eca326535   minio/minio:RELEASE.2023-01-25T00-19-54Z   "/usr/bin/docker-ent…"   10 minutes ago   Up 10 minutes (healthy)   9000/tcp                                                               apitable-minio-1
c62a5751024b   mysql:8.0.32                               "docker-entrypoint.s…"   10 minutes ago   Up 10 minutes (healthy)   3306/tcp, 33060/tcp
```

### 路径{#path}

APITable 配置文件： *path/config.php*    

### 端口{#port}

无特殊端口

### 版本{#version}

控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats apitable
```

### 命令行{#cli}

### API{#api}
