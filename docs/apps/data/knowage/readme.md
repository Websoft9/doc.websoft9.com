---
sidebar_position: 1
slug: /knowage
tags:
  - Knowage
  - 大数据分析
  - BI
---

# 快速入门

[Knowage](https://www.knowage-suite.com) 源自 SpagoBI，是使用 Java 语言写的开放源码的商业智能分析工具,是一套适合现代商业分析的开源工具套装。Knowage 提供了高级的自助服务功能，为最终用户提供了自主权，可以构建自己的分析、探索和组织自己的数据空间。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-gui-websoft9.png)

部署 Websoft9 提供的 Knowage 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网 IP 地址**
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80**  端口是否开启
3. 在服务器中查看 Knowage 的 **[默认账号和密码](./user/credentials)**
4. 若想用域名访问 Knowage，务必先完成**[域名五步设置](./administrator/domain_step)** 过程

## Knowage 初始化向导

### 详细步骤

1. 使用本地电脑的浏览器访问网址： *http://域名/knowage* 或  *http://服务器公网IP/knowage*, 进入登录界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](./user/credentials)），成功登录到 Knowage 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-backend-websoft9.png)

3. 打开【Profile Management】>【Users Management】 修改密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-changepw-websoft9.png)

4. 打开【Server Settings】>【Configuration Management】 配置 Knowage
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-confmanagement-websoft9.png)

> 需要了解更多 Knowage 的使用，请参考官方文档：[Knowage Documentation](https://knowage-suite.readthedocs.io/)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或 **[FAQ](./faq#setup)** 尝试快速解决问题。

**无法进入登录页面？**

因为 Knowage 应用比较消耗资源，4G 内存的服务器虽然也能运行，初始化过程比较慢，请耐心等待几分钟后再试。

## Knowage 使用入门

下面我们以一个完整的示例（**可视化呈现订单中不同国家的订单总额**），介绍如何使用 Knowage 快速分析数据。
基本步骤分为 4 步：连接数据源，数据建模，配置数据，数据可视化呈现。前 2 步为 IT 人员准备数据，后 2 步为业务人员的自助分析。

1. 操作步骤展示

   ![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-websoft9.png)

2. [连接数据源](#datasource)

3. [数据建模](#datamodel)

4. 配置数据集：业务人员从模型中二次筛选数据，分析和呈现；

   ![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-dataset1-websoft9.png)

   ![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-dataset2-websoft9.png)

   ![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-dataset3-websoft9.png)

5. 数据呈现，设置可视化呈现方式（CHART）。根据场景也可以将数据以其他的可视化业务报表（仪表盘）呈现，供决策分析使用。

   ![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis-websoft9.png)

   ![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis1-websoft9.png)

   ![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis2-websoft9.png)

6. 选择数据集
   ![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis3-websoft9.png)

7. 配置数据项
   ![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis4-websoft9.png)
   ![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis5-websoft9.png)

## Knowage 常用操作

### 连接数据源{#datasource}

以连接 MySQL 为例，登录 Knowage，进入主面板，选择>【Data source】：

   ![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-datasource-websoft9.png)

### 数据建模{#datamodel}

根据业务场景从数据源中选取数据，建模：

   ![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-model-websoft9.png)

## Knowage 参数

Knowage 应用中包含 Nginx, Docker, MariaDB 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 Knowage 运行时所有的 Container：

```
CONTAINER ID   IMAGE                                              COMMAND                  CREATED        STATUS                 PORTS                               NAMES
3b30d327e903   mariadb:10.3                                       "docker-entrypoint.s…"   2 hours ago    Up 2 hours             0.0.0.0:3307->3306/tcp              knowage-mariadb-server
a28572948615   knowagelabs/knowage-server-docker:8.0.0-SNAPSHOT   "./entrypoint.sh ./a…"   2 hours ago    Up 2 hours (healthy)   0.0.0.0:8080->8080/tcp              knowage-server
90d49e9971bf   mariadb:10.3                                       "docker-entrypoint.s…"   2 hours ago    Up 2 hours             3306/tcp                            knowage-mariadb-cache
fa5d3ce16865   knowagelabs/knowage-python-docker:8.0.0-SNAPSHOT   "./entrypoint.sh gun…"   2 hours ago    Up 2 hours (healthy)   5000/tcp                            knowage-python
7fbfe56727d5   knowagelabs/knowage-r-docker:8.0.0-SNAPSHOT        "./entrypoint.sh r k…"   2 hours ago    Up 2 hours (healthy)   5001/tcp                            knowage-r
```

下面仅列出 Knowage 本身的参数：

### 路径{#path}

Knowage 安装目录： */data/apps/knowage*  
Knowage 资源目录： */data/apps/knowage/data/resources*  

### 端口{#port}

无特殊端口

### 版本

```shell
# Knowage Version
docker images |grep knowagelabs |awk '{print $2}' |head -1 |cut -d- -f1
```

### 服务

```shell
sudo docker  start | stop | restart | status knowage-server
sudo docker  start | stop | restart | status knowage-python
sudo docker  start | stop | restart | status knowage-r
sudo docker  start | stop | restart | status knowage-mariadb-server
sudo docker  start | stop | restart | status knowage-mariadb-cache
```

### 命令行

Knowage 暂未提供命令行工具

### API

[Knowage API](https://knowage.docs.apiary.io) 采用 REST API 2.0 规范。Knowage REST API 旨在管理 Knowage 分析文档和数据集的生命周期。
