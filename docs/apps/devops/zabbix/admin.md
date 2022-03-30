---
sidebar_position: 3
slug: /zabbix/admin
tags:
  - Zabbix 
  - DevOps
---

# 维护指南

## 场景

### 更换数据库

默认部署方案中，采用的是本地安装的 MySQL 数据库。如果您打算更换数据库，请参考如下步骤：

1. 导出 zabbix, zabbix-proxy 数据库

2. 使用 SFTP 连接到服务器，编辑与数据库连接相关的两个文件

   * /data/wwwroot/zabbix/.env_db_mysql_proxy
   * /data/wwwroot/zabbix/.env_db_mysql

3. 分别修改两个文件中的数据库连接信息，保存

4. 重新运行容器后生效
   ```
   cd /data/wwwroot/zabbix
   sudo docker compose up -d
   ```

5. 导入备份数据到新的数据库中


### Zabbix 升级

Zabbix 升级原理非常简单：先拉取最新版本的 Zabbix 镜像，然后重新运行容器。

> Zabbix 升级之前请完成服务器的快照备份，以防不测。

1. 使用 SSH 登录 Zabbix 服务器后，拉取最新版本镜像
   ```
   docker image pull zabbix/zabbix-server-mysql:centos-5.2-latest 
   docker image pull zabbix/zabbix-proxy-mysql:centos-5.2-latest
   docker image pull zabbix/zabbix-web-apache-mysql:centos-5.2-latest
   docker image pull zabbix/zabbix-java-gateway:centos-5.2-latest
   docker image pull zabbix/zabbix-snmptraps:centos-5.2-latest
   ```
2. 重新运行 docker-compose 编排文件，启用新的容器
    ```
    cd /data/wwwroot/zabbix
    docker-compose up -d
    ```
3. 登录 Zabbix 后台查看升级后的版本

与升级有关的详细配置方案，请参考官方文档：[INSTALLATION FROM CONTAINERS](https://www.zabbix.com/documentation/5.0/manual/installation/containers)

## 故障速查

除以下列出的 Zabbix 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

#### 修改了数据库密码 Zabbix 不能访问？

若已完成 Zabbix 安装向导，再通过 phpMyAdmin 修改数据库密码，Zabbix 就会连不上数据库。  

1. 使用 SFTP 连接服务器，修改两个 [Zabbix 数据库配置](../zabbix#path) 文件中的密码。  

2. 重新运行容器
   ```
   cd /data/wwwroot/zabbix
   sudo docker compose up -d
   ```

## 问题解答

#### Zabbix 能监控哪些对象？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-structure-websoft9.png)

#### Zabbix 支持多语言吗？

支持多语言（包含中文），通过后台设置即可

#### 本部署方案是如何安装 Zabbix 的？

采用 Docker 安装，以适用云原生时代

#### Docker 安装是否会丢失数据？

Zabbix 代码和运行文件已经采用持久存储，数据库 MySQL 是基于非容器部署

#### Zabbix 中有哪些组件？

包含：Zabbix-Server，Zabbix-Web，Zabbix-Proxy，Zabbix-Agent，Zabbix-java-gateway等组件。  

Zabbix-Web 是可视化的 Web 控制台，与 Zabbix-Server 是分离的。

#### Zabbix-Proxy是用来干什么的？

Proxy 适合于 Zabbix 分布式部署架构中从 Zabbix-Agent 采集数据，用于减轻 Zabbix-Server 的压力。

#### Zabbix-Sender是什么？

Zabbix sender 是一个命令行应用程序，可用于将性能数据发送到 Zabbix server 进行处理。

#### Zabbix-Git是什么？

Zabbix get 是一个可以用于与 Zabbix agent 进行通信的命令行，并从 Zabbix agent 那里获取信息。

#### 是否可以使用 RDS 作为 Zabbix 的数据库？

可以

#### Zabbix-Server 能在 Windows 上部署吗？

官方没有提供 Windows 上的安装方案

#### Zabbix数据库连接配置信息在哪里？

数据库配置信息 [Zabbix 环境变量](../zabbix#path)中