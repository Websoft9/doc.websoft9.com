---
sidebar_position: 1
slug: /knowage
tags:
  - Knowage
  - Data Analysis
  - BI
---

# Knowage Getting Started

[Knowage](https://www.knowage-suite.com) is the full capabilities open source suite for modern business analytics over traditional sources and big data systems. Its features, such as data federation, mash-up, data/text mining and advanced data visualization, give comprehensive support to rich and multi-source data analysis. The suite is composed of several modules, each one conceived for a specific analytical domain. They can be used individually as complete solution for a certain task, or combined with one another to ensure full coverage of user’ requirements.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-gui-websoft9.png)

If you have installed Websoft9 Knowage, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Knowage
4. [Get](./user/credentials) default username and password of Knowage

## Knowage Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://DNS* or *http://Server's Internet IP*, you will enter login page of Knowage
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-login-websoft9.png)

   > You can visit Knowage by the URL: *http://Internet IP:8080/knowage* also

2. Log in to Knowage web console([Don't have password?](./user/credentials)), go to dashboard of Knowage 

3. Go to  Profile Management->Users Management to change the password of Administrator
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-changepw-websoft9.png)

4. Go 【Server Settings】>【Configuration Management】 to configure Knowage
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-confmanagement-websoft9.png)

> More useful Knowage guide, please refer to [Knowage Documentation](https://knowage-suite.readthedocs.io/)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**无法进入登录页面？**

因为 Knowage 应用比较消耗资源，4G 内存的服务器虽然也能运行，初始化过程比较慢，请耐心等待几分钟后再试。

## Knowage QuickStart

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

## Knowage Setup

### 连接数据源{#datasource}

Take connecting to MySQL as an example, log in to Knowage, enter the main panel, and select > [Data source]:

   ![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-datasource-websoft9.png)

### 数据建模{#datamodel}

根据业务场景从数据源中选取数据，建模：

   ![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-model-websoft9.png)

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Knowage


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

### Path{#path}

Knowage-server 资源目录： */data/wwwroot/knowage/resources*

### Port{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 8080   | Knowage 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |

### Version

```shell
# Knowage Version
docker images |grep knowagelabs |awk '{print $2}' |head -1 |cut -d- -f1
```

### Sevice

```shell
sudo docker  start | stop | restart | status knowage-server
sudo docker  start | stop | restart | status knowage-python
sudo docker  start | stop | restart | status knowage-r
sudo docker  start | stop | restart | status knowage-mariadb-server
sudo docker  start | stop | restart | status knowage-mariadb-cache
```

### CLI

Knowage 暂未提供命令行工具

### API

[Knowage API](https://knowage.docs.apiary.io) 采用 REST API 2.0 规范。Knowage REST API 旨在管理 Knowage 分析文档和数据集的生命周期。
