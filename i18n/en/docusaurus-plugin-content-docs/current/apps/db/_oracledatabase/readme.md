---
sidebar_position: 1
slug: /oracledatabase
tags:
  - Oracle Database
  - Cloude Native Database
---

# Oracle Database Getting Started

[Oracle Database](https://oracle-server.apache.org/) is the most widely deployed open source message broker. With more than 35,000 production deployments of Oracle Database world-wide at small startups and large enterprises, Oracle Database is the most popular open source message broker.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-gui-websoft9.png)

If you have installed Websoft9 Oracle Database, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:1521** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Oracle Database
4. [Get](./user/credentials) default username and password of Oracle Database

## Oracle Database Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://DNS:15672* or *http://Internet IP:15672*, you will enter installation wizard of Oracle Database
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-login-websoft9.png)

2. Log in to Oracle Database web console([Don't have password?](./user/credentials))  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-bk-websoft9.png)

3. Set you new password from: 【Users】>【Admin】>【Permissions】>【Update this user】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-pw-websoft9.png)

> More useful Oracle Database guide, please refer to [Oracle Database Documentation](https://www.oracle.com/documentation.html)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Oracle Database  QuickStart

## Oracle Database Setup

### Set remote connection {#remote}

镜像默认已经设置好了远程连接，只需开启安全组 `TCP:1521` 端口即可启用远程访问

### GUI

Oracle Database支持第三方可视化数据库管理工具，例如 Navicat,Maestro,Oracle 企业管理器等。下面以使用最为广泛的 Navicat 为例来说明如何管理本镜像的数据库：

1.  [下载](http://www.navicat.com.cn/download/navicat-for-oracle)并安装Navicat For Oracle
2.  新建一个Oracle连接，填写好连接参数（用户名为：system，密码为：123456；端口1521不能更改，另外请确保云服务器控制台上的安全组打开了TCP:1521），点击“连接测试”，成功标明参数没有问题。
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle_database/oracle11gex-conn-websoft9.png)
3.  点击确认后，进入数据库管理界面
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle_database/oracle11gex-ui-websoft9.png)

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Oracle Database


通过运行 `docker ps`，可以查看到 Oracle Database 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

下面仅列出 Oracle Database 本身的参数：

### Path{#path}

Oracle Database 配置文件路径：*/u01/app/oracle/product/11.2.0/db1/network/admin/listener.ora*  

### Port

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 1521   | 远程连接Oracle Database | 可选   |


### Version

```shell
select * from v$version;
```

### Service

```shell
sudo systemctl start | stop | restart | status oracle

# 查看监听
lsnrctl status
```

### CLI

### API

### 版权与约束

Oracle Database XE 对安装主机的规模和 CPU 数量不作限制（每台计算机一个数据库），但 XE 将最多存储 11GB 的用户数据，最多使用 1GB 内存，使用主机上的一个 CPU。版权说明：在使用软件之前，建议阅读[ Oracle Database 快捷版 11*g* 第 2 版的 OTN 许可协议](http://www.oracle.com/technetwork/licenses/database-11g-express-license-459621.html)



