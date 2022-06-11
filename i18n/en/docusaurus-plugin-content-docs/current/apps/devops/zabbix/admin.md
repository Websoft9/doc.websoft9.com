---
sidebar_position: 3
slug: /zabbix/admin
tags:
  - Zabbix 
  - DevOps
---

# Zabbix Maintenance

This chapter is special guide for Zabbix maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Replace database

This deployment solution is used the MySQL installed in local, if you want to use other database, refer to:

1. Export database  **zabbix, zabbix-proxy** by phpMyAmin

2. Use **SFTP** to connect Zabbix instance and edit the database configuration file

   * /data/wwwroot/zabbix/.env_db_mysql_proxy
   * /data/wwwroot/zabbix/.env_db_mysql

3. Recreate container 
   ```
   cd /data/wwwroot/zabbix
   sudo docker compose up -d
   ```

5. Import database  


### Zabbix Upgrade

You can upgrade Zabbix by Docker very easy

> Please backup all Zabbix data and database before upgrade

1. Use **SSH** to connect Zabbix instance and pull the latest image
   ```
   docker image pull zabbix/zabbix-server-mysql:centos-5.2-latest 
   docker image pull zabbix/zabbix-proxy-mysql:centos-5.2-latest
   docker image pull zabbix/zabbix-web-apache-mysql:centos-5.2-latest
   docker image pull zabbix/zabbix-java-gateway:centos-5.2-latest
   docker image pull zabbix/zabbix-snmptraps:centos-5.2-latest
   ```
2. Run the docker compose file to recreate container
    ```
    cd /data/wwwroot/zabbix
    docker-compose up -d
    ```
3. Login to Zabbix console to check upgrade

More upgrade detail, refer to: [INSTALLATION FROM CONTAINERS](https://www.zabbix.com/documentation/5.0/manual/installation/containers)

## Troubleshoot{#troubleshoot}

In addition to the Zabbix issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### 修改了数据库密码 Zabbix 不能访问？

若已完成 Zabbix 安装向导，再通过 phpMyAdmin 修改数据库密码，Zabbix 就会连不上数据库。  

1. 使用 SFTP 连接服务器，修改两个 [Zabbix 数据库配置](../zabbix#path) 文件中的密码。  

2. 重新运行容器
   ```
   cd /data/wwwroot/zabbix
   sudo docker compose up -d
   ```

## FAQ{#faq}

#### Zabbix 能监控哪些对象？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-structure-websoft9.png)

#### Does Zabbix support multi-language?

Yes,refer to [Zabbix language](../zabbix#i18)

#### How does this deployment plan install Zabbix?

Docker

#### Will Docker installation lose data?

Zabbix have mount to volume, and database MySQL is based on non-container deployment

#### What components included in this Zabbix deployment solution? 

Zabbix-Server, Zabbix-Web, Zabbix-Proxy, Zabbix-Agent, Zabbix-java-gateway   

Zabbix-Web 是可视化的 Web 控制台，与 Zabbix-Server 是分离的。

#### Zabbix-Proxy是用来干什么的？

Proxy 适合于 Zabbix 分布式部署架构中从 Zabbix-Agent 采集数据，用于减轻 Zabbix-Server 的压力。

#### What's Zabbix-Sender?

Zabbix sender is a command line utility that may be used to send performance data to Zabbix server for processing.

#### What's Zabbix-Git?

Zabbix get is a command line utility which can be used to communicate with Zabbix agent and retrieve required information from the agent.


#### Can I use the RDS of Cloud Provider for Zabbix?

Yes

#### Zabbix-Server 能在 Windows 上部署吗？

官方没有提供 Windows 上的安装方案

#### #### Where is the database connection configuration of Zabbix?

Database configuration information in *LocalSettings.php* in the [Zabbix Path](../zabbix#path)中