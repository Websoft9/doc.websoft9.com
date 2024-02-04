---
sidebar_position: 1
slug: /postgresql2
tags:
  - PostgreSQL
  - Cloud Native Database
---

# 快速入门

[PostgreSQL](https://www.postgresql.org/) 社区志愿者开发的开源关系型数据库系统，它源于 UC Berkeley 大学 1977 年的 Ingres 计划。它稳定可靠，有很多前言的技术特征，并且性能卓越，在数据完整性和正确性方面赢得了良好的市场声誉。


![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/postgresql/pgadmin4-websoft9.png)

## 准备

部署 Websoft9 提供的 PostgreSQL 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:5432** 端口已经开启
3. 在服务器中查看 PostgreSQL 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  PostgreSQL，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程


## PostgreSQL 初始化向导

### 详细步骤

部署 PostgreSQL 之后，依次完成下面的步骤，验证其可用性

1. 查看服务状态：SSH 连接服务器，运行下面的命令，查看 PostgreSQL 的安装信息和运行状态
   ```
   cd /data/apps/postgresql && sudo docker compose ls
   ```
   PostgreSQL 正常运行会得到 "STATUS: running(1)" 的反馈

2. 连接 PostgreSQL：SSH 连接服务器，通过下列命令，即可使用 psql 连接数据库
    ```
    $ docker exec -it postgresql bash
    $ psql -d postgresql -U postgresql
    psql (15.0 (Debian 15.0-1.pgdg110+1))
    Type "help" for help.
    
    postgresql=#

    ```

3. 使用可视化管理工具 pgAdmin 

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## PostgreSQL 常用操作

### 设置远程访问{#remote}

本地电脑连接 PostgreSQL 时，需设置 PostgreSQL 远程访问：

1. 云控制台安全组开启 **TCP:5432** 端口
2.  修改 [postgresql.conf](#path) 文件
   ```
   #listen_addresses = 'localhost'

   修改为

   listen_addresses = '*'
   ```

3. 修改 [pg_hba.conf](#path) 文件，增加如下一行到文件末尾
   ```
   host    all             all             0.0.0.0/0            md5
   ```

4. 重启 PostgreSQL 后生效
   ```
   sudo docker restart postgresql
   ```






## 参数

PostgreSQL 应用中包含 Docker, pgAdmin 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 PostgreSQL 运行时所有的服务组件：

```bash
CONTAINER ID   IMAGE                   COMMAND                  CREATED         STATUS         PORTS                                            NAMES
7e91744ee643   dpage/pgadmin4:latest   "/entrypoint.sh"         3 seconds ago   Up 1 second    443/tcp, 0.0.0.0:9090->80/tcp, :::9090->80/tcp   pgadmin
9218c5167c4b   postgres:latest         "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp        postgresql```
```

### 路径{#path}

PostgreSQL 配置文件目录: */data/apps/postgresql*   
PostgreSQL 数据目录：*/data/apps/postgresql/data/postgres*   




### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9090   | 通过 HTTP 访问 PgAdmin	 | 可选   |
| 5432   | 远程连接PostgreSQL | 可选   |


### 版本

```shell
# PostgreSQL version
docker exec -it postgresql psql -V
```

### 服务

```shell
sudo docker start | stop | restart | stats postgresql
sudo docker start | stop | restart | stats pgadmin
```



