---
sidebar_position: 1
slug: /knowage
tags:
  - Knowage
  - 大数据分析
  - BI
---

# 快速入门

[Knowage](https://www.knowage-suite.com) 源自SpagoBI，是使用Java语言写的开放源码的商业智能分析工具,是一套适合现代商业分析的开源工具套装。Knowage提供了高级的自助服务功能，为最终用户提供了自主权，可以构建自己的分析、探索和组织自己的数据空间。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-gui-websoft9.png)

在云服务器上部署 Knowage 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 和 **TCP:8080** 端口是否开启
3. 在服务器中查看 Knowage 的 **[默认账号和密码](./setup/credentials#getpw)** 
4. 若想用域名访问 Knowage，务必先完成**[域名五步设置](./dns#domain)** 过程

## Knowage 初始化向导

### 详细步骤

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 进入登录界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-login-websoft9.png)

   > 也可以通过 http://公网IP:8080/knowage 访问本应用

2. 输入账号密码（[不知道账号密码？](#账号密码)），成功登录到 Knowage 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-backend-websoft9.png)

3. 打开【Profile Management】>【Users Management】 修改密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-changepw-websoft9.png)

4. 打开【Server Settings】>【Configuration Management】 配置 Knowage
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-confmanagement-websoft9.png)

> 需要了解更多 Knowage 的使用，请参考官方文档：[Knowage Documentation](https://knowage-suite.readthedocs.io/)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

## Knowage 使用入门

下面我们以一个完整的示例（**可视化呈现订单中不同国家的订单总额**），介绍如何使用 Knowage 快速分析数据。

基本步骤分为 4 步：连接数据源，数据建模，配置数据集，数据可视化呈现。
前2步为IT人员的数据准备，后2步为业务人员的自助分析。

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-websoft9.png)

1. 连接数据源：连接 MySQL 数据库服务器；

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-datasource-websoft9.png)

2. 数据建模：根据业务场景从数据源中选取数据，建模；

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-model-websoft9.png)

3. 配置数据集：业务人员从模型中二次筛选数据，分析和呈现；

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-dataset1-websoft9.png)

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-dataset2-websoft9.png)

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-dataset3-websoft9.png)

4. 数据呈现，设置可视化呈现方式（CHART）。根据场景也可以将数据以其他的可视化业务报表（仪表盘）呈现，供决策、分析使用。

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis-websoft9.png)

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis1-websoft9.png)

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis2-websoft9.png)

选择数据集
![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis3-websoft9.png)

配置数据项
![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis4-websoft9.png)

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis5-websoft9.png)

## Knowage 常用操作

## 参数

**[通用参数表](./setup/parameter)** 中可查看 Nginx, Docker, MariaDB 等 Knowage 应用中包含的基础架构组件路径、版本、端口等参数。 


### 路径{#path}

本项目采用 Docker 安装，运行 `docker ps` 可以查看所有相关的容器：

```
CONTAINER ID   IMAGE                                              COMMAND                  CREATED        STATUS                 PORTS                               NAMES
3b30d327e903   mariadb:10.3                                       "docker-entrypoint.s…"   2 hours ago    Up 2 hours             0.0.0.0:3307->3306/tcp              knowage-mariadb-server
a28572948615   knowagelabs/knowage-server-docker:8.0.0-SNAPSHOT   "./entrypoint.sh ./a…"   2 hours ago    Up 2 hours (healthy)   0.0.0.0:8080->8080/tcp              knowage-server
90d49e9971bf   mariadb:10.3                                       "docker-entrypoint.s…"   2 hours ago    Up 2 hours             3306/tcp                            knowage-mariadb-cache
fa5d3ce16865   knowagelabs/knowage-python-docker:8.0.0-SNAPSHOT   "./entrypoint.sh gun…"   2 hours ago    Up 2 hours (healthy)   5000/tcp                            knowage-python
7fbfe56727d5   knowagelabs/knowage-r-docker:8.0.0-SNAPSHOT        "./entrypoint.sh r k…"   2 hours ago    Up 2 hours (healthy)   5001/tcp                            knowage-r
```

### Knowage server

Knowage-Server 资源目录：*/data/wwwroot/knowage/resources*  


### 端口{#port}

Knowage server的默认端口是8080

### 版本

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Nginx  Version
nginx -V

# Docker Version
docker -v

# MariaDB version

docker inspect knowage-mariadb-server | grep "MARIADB_VERSION"

# Knowage Version
docker images |grep knowagelabs |awk '{print $2}' |head -1 |cut -d- -f1
```

### 服务

GitLab 提供的（[gitlab-ctl ](https://docs.gitlab.com/omnibus/maintenance/README.html#get-service-status)）可以很方便的管理各个组件的服务：

```shell
sudo gitlab-ctl start | stop | restart | status reconfigure nginx
sudo gitlab-ctl start | stop | restart | status reconfigure unicorn
sudo gitlab-ctl start | stop | restart | status reconfigure sidekiq
sudo gitlab-ctl start | stop | restart | status reconfigure postgresql
sudo gitlab-ctl start | stop | restart | status reconfigure redis
```

GitLab 自身的启动/停止，是通过 Systemd 服务来管理的：

```shell
systemctl start | stop | restart | status gitlab-runsvdir.service
```

### 命令行

GitLab 提供了命令行工具 `gitlab-ctl` 用于全面管理和配置 GitLab

```
$ gitlab-ctl -h

I don't know that command.
omnibus-ctl: command (subcommand)
check-config
  Check if there are any configuration in gitlab.rb that is removed in specified version
deploy-page
  Put up the deploy page
diff-config
  Compare the user configuration with package available configuration
get-redis-master
  Get connection details to Redis master
prometheus-upgrade
  Upgrade the Prometheus data to the latest supported version
remove-accounts
  Delete *all* users and groups used by this package
reset-grafana
  Reset Grafana instance to its initial state by removing the data directory
set-grafana-password
  Reset admin password for Grafana
upgrade
  Run migrations after a package upgrade
upgrade-check
  Check if the upgrade is acceptable
General Commands:
  cleanse
    Delete *all* gitlab data, and start from scratch.
  help
    Print this help message.
  reconfigure
    Reconfigure the application.
  show-config
    Show the configuration that would be generated by reconfigure.
  uninstall
    Kill all processes and uninstall the process supervisor (data will be preserved).
Service Management Commands:
  graceful-kill
    Attempt a graceful stop, then SIGKILL the entire process group.
  hup
    Send the services a HUP.
  int
    Send the services an INT.
  kill
    Send the services a KILL.
  once
    Start the services if they are down. Do not restart them if they stop.
  restart
    Stop the services if they are running, then start them again.
  service-list
    List all the services (enabled services appear with a *.)
  start
    Start services if they are down, and restart them if they stop.
  status
    Show the status of all the services.
  stop
    Stop the services, and do not restart them.
  tail
    Watch the service logs of all enabled services.
  term
    Send the services a TERM.
  usr1
    Send the services a USR1.
  usr2
    Send the services a USR2.
Gitlab Geo Commands:
  geo
    Interact with Geo
  geo-replication-pause
    Replication Process
  geo-replication-resume
    Replication Process
  promote-db
    Promote secondary PostgreSQL database
  promote-to-primary-node
    Promote to primary node
  promotion-preflight-checks
    Run preflight checks for promotion to primary node
  replicate-geo-database
    Replicate Geo database
  set-geo-primary-node
    Make this node the Geo primary
Pgbouncer Commands:
  pgb-console
    Connect to the pgbouncer console
  pgb-kill
    Send the "resume" command to pgbouncer
  pgb-notify
    Notify pgbouncer of an update to its database
  pgb-resume
    Send the "resume" command to pgbouncer
  pgb-suspend
    Send the "suspend" command to pgbouncer
Database Commands:
  get-postgresql-primary
    Get connection details to the PostgreSQL primary
  patroni
    Interact with Patroni
  pg-password-md5
    Generate MD5 Hash of user password in PostgreSQL format
  pg-upgrade
    Upgrade the PostgreSQL DB to the latest supported version
  revert-pg-upgrade
    Run this to revert to the previous version of the database
  set-replication-password
    Set database replication password
  write-pgpass
    Write a pgpass file for the specified user
Consul Commands:
  consul
    Interact with the gitlab-consul cluster
Container Registry Commands:
  registry-garbage-collect
    Run Container Registry garbage collection.
Let's Encrypt Commands:
  renew-le-certs
    Renew the existing Let's Encrypt certificates
Gitaly Commands:
  praefect
    Interact with Gitaly cluster
Backup Commands:
  backup-etc
    Backup GitLab configuration [options]
```

### API

GitLab 提供[多种 API](https://docs.gitlab.com/ee/api/) 方式，包括：REST API, SCIM API, GraphQL API

```
curl "https://gitlab.example.com/api/v4/projects"
```




