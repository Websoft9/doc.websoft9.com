---
sidebar_position: 2
slug: /superset/admin
tags:
  - Superset
  - 大数据分析
  - BI
---

# 维护参考

## 系统参数

Superset 预装包包含 Superset 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

本项目除 Nginx 之外，所有组件均基于 Docker 安装，运行 `docker ps` 命令查看所有组件：

```
CONTAINER ID   IMAGE                           COMMAND                  CREATED              STATUS                                 PORTS                               NAMES
453f04935734   apache/superset:latest          "/usr/bin/docker-ent…"   About a minute ago   Up About a minute (healthy)            0.0.0.0:8088->8088/tcp              superset_app
5477e7693ef3   apache/superset:latest          "/usr/bin/docker-ent…"   About a minute ago   Up About a minute (healthy)            8088/tcp                            superset_worker
d6670fa1bc11   apache/superset:latest          "/usr/bin/docker-ent…"   About a minute ago   Up About a minute (healthy)            8088/tcp                            superset_worker_beat
17689f5d6ebb   postgres:10                     "docker-entrypoint.s…"   About a minute ago   Up About a minute                      0.0.0.0:5432->5432/tcp              superset_db
06bf52f4b856   redis:3.2                       "docker-entrypoint.s…"   About a minute ago   Up About a minute                      127.0.0.1:6379->6379/tcp            superset_cache
```

#### Superset

Superset 源码目录：*/data/wwwroot/superset*  
Superset 数据目录：*/data/wwwroot/superset_home*  
Superset 配置目录：*/data/wwwroot/superset/docker*  
Superset 配置文件： */data/wwwroot/superset/docker/pythonpath_dev/superset_config.py*  

> 配置目录包括数据库连接信息、[Superset 配置文件](https://github.com/apache/superset/blob/master/superset/config.py)等

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*

#### PostgreSQL

PostgreSQL 主目录：*/data/wwwroot/superset/postgresql*  

> 包含所有 PostgreSQL 数据文件和配置文件

#### pgAdmin

pgAdmin 主目录：*/data/apps/pgadmin*  

#### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   
Docker 存储卷：*/var/lib/docker/volumes*  

#### Docker Compose

本环境使用 Docker Compose 作为容器编排（调度）工具，用于管理多个容器的启动和服务连接。

Docker Compose 命令位置：*/usr/local/bin/docker-compose*  
Docker Compose 配置目录 */data/wwwroot/superset* 

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 80 | 通过 HTTP 访问 Superset | 必选 |
| TCP | 443 | 通过 HTTPS 访问 Superset | 可选 |
| TCP | 5432 | 通过 TCP 访问 PostgreSQL数据库 | 可选 |
| TCP | 9090 | PostgreSQL 可视化管理工具 pgAdmin | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Nginx  Version
nginx -V

# Docker Version
docker -v

# Superset Version
docker exec -it superset_app /bin/bash -c 'cat /app/superset-frontend/package.json |grep version'

# PostgreSQL version
docker exec -it superset_db /bin/bash -c 'psql -V'
```

### 服务

使用由Websoft9提供的 Superset 部署方案，可能需要用到的服务如下：

> 先通过 `sudo docker ps` 命令查看容器名称

### Docker-compose

```
sudo docker-compose stop
sudo docker-compose restart
```

### Superset

```shell
sudo docker start superset_app
sudo docker stop superset_app
sudo docker restart superset_app
sudo docker stats superset_app
```

### PostgreSQL

```shell
sudo docker start superset_db
sudo docker stop superset_db
sudo docker restart superset_db
sudo docker stats superset_db
```

### Redis

```shell
sudo docker start superset_cache
sudo docker stop superset_cache
sudo docker restart superset_cache
sudo docker stats superset_cache
```

### pgAdmin

```shell
sudo docker start pgadmin
sudo docker stop pgadmin
sudo docker restart pgadmin
```

## 备份

### 全局自动备份

所有的云平台都提供了全局自动备份功能，基本原理是基于**磁盘快照**：快照是针对于服务器的磁盘来说的，它可以记录磁盘在指定时间点的数据，将其全部备份起来，并可以实现一键恢复。

```
- 备份范围: 将操作系统、运行环境、数据库和应用程序
- 备份效果: 非常好
- 备份频率: 按小时、天、周备份均可
- 恢复方式: 云平台一键恢复
- 技能要求：非常容易
- 自动化：设置策略后全自动备份
```

不同云平台的自动备份方案有一定的差异，详情参考 [云平台备份方案](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

### 程序手工备份

程序手工本地备份是通过**下载应用程序源码和导出数据库文件**实现最小化的备份方案。

下面以列表的方式介绍这种备份：
```
- 备份范围: 数据库和应用程序
- 备份效果: 一般
- 备份频率: 一周最低1次，备份保留30天
- 恢复方式: 重新导入
- 技能要求：非常容易
- 自动化：无
```
通用的手动备份操作步骤如下：

1. 通过 SFTP 将持久化数据卷目录（*/data/wwwroot/superset*）**压缩后**再完整的下载到本地

2. 导出[ PostgreSQL 数据库](/快速入门.md#postgresql-数据管理)

3. 将程序文件和数据库文件放到同一个文件夹，根据日期命名

4. 备份工作完成

## 恢复

## 升级

### 系统级更新

运行一条更新命令，即可完成系统级（包含rethinkdb小版本更新）更新：

``` shell
#For Ubuntu&Debian
apt update && apt upgrade -y

#For Centos&Redhat
yum update -y
```
> 本部署包已预配置一个用于自动更新的计划任务。如果希望去掉自动更新，请删除对应的 Cron

### Superset 升级

Superset 采用 Docker 部署，其升级流程：拉取镜像 > 删除容器 > 重建容器

> 升级之前请完成服务器的快照备份，以防不测。

1. 使用 SSH 登录服务，进入到 Superset 目录后， 停止当前的 Superset 容器
   ```
   cd /data/wwwroot/superset
   docker-compose down
   ```

2. 备份并更新docker启动需要的文件
   ```
   mv  /data/wwwroot/superset/docker /data/wwwroot/superset/docker_bark
   mkdir superset-latest
   cd superset-latest
   git clone https://github.com/Websoft9/docker-superset.git
   cp -R docker-superset/docker /data/wwwroot/superset
   ```

3. 将老版本更新成您指定的版本（注意：不能将版本指定为"latest"）

   ```
   cd /data/wwwroot/superset
   sed -i "s/APP_VERSION=old_version/APP_VERSION=new_version/g" /data/wwwroot/superset/.env
   ```
   
4. 重新创建 Superset 容器
   ```
   docker-compose up -d
   ```

## 故障处理

此处收集使用 Superset 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

通过 `sudo docker logs superset_app` 查看 Superset 容器错误日志

#### Superset 运行报错？

先通过如下的命令，重新运行容器

```
cat /data/wwwroot/superset
docker-compose down
docker-compose up -d
```

如果仍然报错，请检查数据库连接、持久化存储挂载是否准确无误。

#### Superset 容器中安装数据库驱动报错？

错误信息：ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: '/home/superset'
Check the permissions.  

问题原因：权限不足  

解决方案：以 root 用户进入容器 `docker exec -it --user root superset_app bash`，然后再安装驱动  

#### Superset 密码正确，但仍然登录失败？

问题描述：用户名和密码完全正确，但 Superset 仍然登录失败，错误信息 Invalid login, Please try again  
问题原因：暂时未知  
解决方案：重启所有 Superset 容器 `cd /data/wwwroot/superset && docker-compose restart`  

## 常见问题

#### Superset 支持多语言吗？

支持（包含中文)，但测试版不支持多语言

#### 如何查看所有容器？

```
sudo docker ps
```

#### 是否可以通过命令行修改 Superset 后台密码？

不支持，需登录控制台修改

#### 如果没有域名是否可以部署 Superset？

可以，访问 `http://服务器公网IP` 或 `http://服务器公网IP:8088` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置pgAdmin，访问地址：*http://服务器公网IP:9090*

#### 如何以 root 身份进入容器运行命令？

```
docker exec -it --user root superset_app bash
```

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R superset.superset /data/wwwroot/superset
# 读写执行权限
find /data/wwwroot/superset -type d -exec chmod 750 {} \;
find /data/wwwroot/superset -type f -exec chmod 640 {} \;
```

#### 是否支持 google authentication 或 OKTA based authentication (OIDC)?

SuperSet 默认只提供了邮件登录，更多登录方式使用需参考其框架文档：[Flask-AppBuilder](https://flask-appbuilder.readthedocs.io/en/latest/security.html#supported-authentication-types)
