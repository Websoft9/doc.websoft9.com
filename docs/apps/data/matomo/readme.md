---
sidebar_position: 100
slug: /matomo
tags:
  - matomo
  - analytics
  - 统计分析
---

# 快速入门

Matomo 介绍

Matomo 是一个强大的开源网络分析平台，拥有100% 的数据所有权，并确保业务符合GDPR和CCPA。尤其对于商业软件来说，Matomo 增强的搜索引擎优化以及转换优化能力，让您在数字营销领域能力大大增强。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/matomo/matomo-show-websoft9.png)

部署 Websoft9 提供的 Matomo 之后，请参考下面的步骤快速入门。

## 准备{#prepare}

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Matomo 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问 Matomo，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## Matomo 初始化向导{#wizard}

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入初始化页面
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/matomo/matomo-init1-websoft9.png)

2. 点击【Next】，直到Superuser页面设置用户名，密码和登陆邮件账号并牢记
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/matomo/matomo-init2-websoft9.png)
  
3. 点击【Next】，设置站点名称，时区，URL
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/matomo/matomo-init3-websoft9.png)
  
4. 完成初始化向导，进入登陆页面
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/matomo/matomo-login-websoft9.png)
  
5. 输入向导设置的用户名和密码，开始体验后台
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/matomo/matomo-main-websoft9.png)
  
### 碰到问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## Matomo 使用入门{#quickstart}

下面以 **××××** 作为一个任务，帮助用户快速入门：

## Matomo 常用操作{#guide}



## 参数{#parameter}

Matomo 应用中包含 Docker, Portainer 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行 `docker ps`，查看 Matomo 运行时所有的服务组件：   

```bash
CONTAINER ID   IMAGE               COMMAND                  CREATED       STATUS       PORTS                                   NAMES
55278a64ce01   phpmyadmin:latest   "/docker-entrypoint.…"   3 hours ago   Up 3 hours   0.0.0.0:9090->80/tcp, :::9090->80/tcp   phpmyadmin
c17ad9f95f74   matomo:latest       "/entrypoint.sh apac…"   3 hours ago   Up 3 hours   0.0.0.0:9001->80/tcp, :::9001->80/tcp   matomo
ead45db0cdab   mysql:5.7           "docker-entrypoint.s…"   3 hours ago   Up 3 hours   3306/tcp, 33060/tcp                     matomo-db
```

### 路径{#path}

Matomo 数据目录： */data/apps/matomo*  
Matomo 数据目录： */data/apps/matom/data/matomo* 

### 端口{#port}

除 80, 443 等常见端口需开启之外，以下端口可能会用到：  

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9090   | 数据库可视化工具phpmyadmin | 可选   |

### 版本{#version}

```
docker exec -it matomo cat /var/www/html/core/Version.php|grep "const VERSION ="|cut -d"=" -f2
```

### 服务{#service}

```shell
sudo docker start | stop | restart | stats matomo
sudo docker start | stop | restart | stats matomo-db
sudo docker start | stop | restart | stats phpmyadmin
```

### 命令行{#cli}

暂无

### API{#api}

[Matomo API Documentation](https://matomo.org/guide/apis/)
