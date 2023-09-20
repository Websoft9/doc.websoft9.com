---
sidebar_position: 100
slug: /akeneo
tags:
  - Akeneo
---

# 快速入门

[Akeneo](https://www.akeneo.com/) 是一个开源的产品体验管理 (PXM) 和产品信息管理 (PIM) 软件产品。可帮助商家和品牌在所有销售渠道中提供引人入胜的客户体验、提高产品数据质量并简化产品目录管理。使用 Akeneo 作为产品基础设施管理，能够转变业务模式，消减产品浓缩成本。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/akeneo/akeneo-main-websoft9.png)

部署 Websoft9 提供的 Akeneo 之后，请参考下面的步骤快速入门。

## 准备{#prepare}

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Akeneo 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问 Akeneo，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## Akeneo 初始化向导{#wizard}

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入初始化页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/akeneo/akeneo-login-websoft9.png)

2. 输入用户名和密码([不知道密码?](./user/credentials)) ，登陆 Akeneo 开始产品管理 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/akeneo/akeneo-product-websoft9.png)

### 碰到问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## Akeneo 使用入门{#quickstart}

下面以 **Akeneo 数据导入导出** 作为一个任务，帮助用户快速入门：

详细请参照[Akeneo 数据导入导出](https://docs.akeneo.com/6.0/import_and_export_data/index.html)

## Akeneo 常用操作{#guide}

### 连接 App Store {#Appstore}  
Akeneo 通过 App Store 通过扩展应用。连接到 App Store 需要2个步骤：  
1. 给用户授权管理App Store。依次点击：System - Users - Roles - Administrator - Permissions - System - Manager apps / Open apps  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/akeneo/akeneo-appmanager-websoft9.png)
2. 配置 AKENEO_PIM_URL ：修改 /data/apps/akeneo/data/akeneo/.env.local 文件，将 AKENEO_PIM_URL 值修改成服务器 IP 或域名，比如 AKENEO_PIM_URL=http://100.100.100.100 


## 参数{#parameter}

Akeneo 应用中包含 Docker, Portainer 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行 `docker ps`，查看 Akeneo 运行时所有的服务组件：   

```bash
CONTAINER ID   IMAGE                                                      COMMAND                  CREATED         STATUS         PORTS                                                  NAMES
7d46c77c8bc7   phpmyadmin:latest                                          "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes   0.0.0.0:9090->80/tcp, :::9090->80/tcp                  phpmyadmin
db9a7668dad3   websoft9dev/akeneo:latest                                  "/entrypoint.sh /usr…"   7 minutes ago   Up 6 minutes   0.0.0.0:9001->80/tcp, :::9001->80/tcp                  akeneo
6ecce79ee4c1   mysql:8.0                                                  "docker-entrypoint.s…"   7 minutes ago   Up 6 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   akeneo-mysql
8ea176b3bf04   docker.elastic.co/elasticsearch/elasticsearch-oss:7.10.1   "/tini -- /usr/local…"   7 minutes ago   Up 6 minutes   0.0.0.0:9200->9200/tcp, :::9200->9200/tcp, 9300/tcp    akeneo-elasticsearch
```

### 路径{#path}

Akeneo 安装目录： */data/apps/akeneo*  
Akeneo 配置文件： */data/apps/akeneo/000-default.conf*  
Akeneo 站点目录： */data/apps/akeneo/data/akeneo*    

### 端口{#port}

除 80, 443 等常见端口需开启之外，以下端口可能会用到：  

暂无特殊端口

### 版本{#version}

```
docker exec -i akeneo  grep "pim-community-dev/tree" /var/www/html/composer.lock |awk -F"/v" '{print $2}'
```

### 服务{#service}

```shell
sudo docker start | stop | restart | stats akeneo
sudo docker start | stop | restart | stats akeneo-elasticsearch
sudo docker start | stop | restart | stats akeneo-mysql
```

### 命令行{#cli}

暂无

### API{#api}

Akeneo 采用 [REST API](https://api.akeneo.com/documentation/introduction.html) 规范。 

