---
sidebar_position: 2
slug: /memcached/admin
tags:
  - Memcached 
  - Cloud Native Database
---

# 维护参考

## 系统参数

Memcached 预装包包含 Memcached 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

```
CONTAINER ID   IMAGE                                 COMMAND                  CREATED             STATUS             PORTS                                           NAMES
5f7322ff5805   memcached:latest                      "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:11211->11211/tcp, :::11211->11211/tcp   memcached
e4e671827a3e   hatamiarash7/memcached-admin:latest   "docker-php-entrypoi…"   4 minutes ago   Up 4 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp           memcached-admin
```

#### Memcached

Memcached 安装目录: */data/db/memcached*  
Memcached 配置文件：*/data/db/memcached/.env*  

#### Memcached-admin

[Memcached-admin](https://github.com/hatamiarash7/Memcached-Admin) 是一个用于管理和监控 Memcached 的可视化工具  

Memcached 安装目录: */data/apps/memadmin*  
Memcached 配置文件：*/data/apps/memadmin/.env*  

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*  
Nginx 验证访问文件：*/etc/nginx/.htpasswd/htpasswd.conf*  

> 本部署方案中 Nginx 验证访问文件存储了 Memcached-admin 的账号密码

#### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   
Docker daemon.json 文件：默认没有创建，请到 */etc/docker* 目录下根据需要自行创建   


### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：


| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| Memcached | 11211 | 远程访问 Memcached | 可选 |
| Memcached-admin | 9090 | 通过 Nginx 远程访问 Memcached 可视化工具 | 可选 |


### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Memcached version
docker inspect  memcached | grep MEMCACHED_VERSION

# Docker version
docker -v

# Nginx  Version
nginx -V
```

### 服务

使用由Websoft9提供的 Memcached 部署方案，可能需要用到的服务如下：  

#### Memcached

```shell
sudo docker start memcached
sudo docker stop memcached
sudo docker restart memcached
sudo docker stats memcached
```

#### Memcached-admin

```shell
sudo docker start memadmin
sudo docker stop memadmin
sudo docker restart memadmin
sudo docker stats memadmin
```

#### Nginx

```shell
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
```

#### Docker

```shell
sudo systemctl start docker
sudo systemctl restart docker
sudo systemctl stop docker
sudo systemctl status docker
```

#### Docker-Compose

```
#创建容器编排
sudo docker-compose up -d

#删除容器编排
sudo docker-compose up -d

#启动/停止/重启
sudo docker-compose start
sudo docker-compose stop
sudo docker-compose restart
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

1. 使用SFTP登录服务器，下载 Memcached 整个目录 */data/apps/memcached* 到本地
2. 备份完成

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

### Memcached 升级

Memcached 基于 Docker 部署，其升级流程：拉取镜像 > 删除容器 > 重建容器

> 升级之前请确保您已经完成了服务器的镜像（快照）备份

1. 登录服务器，编辑 */data/wwwroot/memcached/.env* 文件，将版本变量的值修改为目标版本号

2. 拉取目标版本的镜像
   ```
   cd /data/apps/memcached
   docker-compose pull
   ```
   > 如果显示没有镜像可拉取，则无需升级

3. 删除旧容器，重新创建 Memcached 容器
    ```
    docker-compose down -v
    docker-compose up -d
    ```


## 故障处理

此处收集使用 Memcached 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### Memcached 服务无法启动？

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误等。  
建议先通过命令进行排查  

```shell
# 查看服务
sudo docker logs memcached

# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看进程
ps aux
```

## 常见问题

#### 什么是 Memcached 客户端？

Memcached 客户端是用于与 Memcached-Server 进行通信的程序，Memcached 是通过 Telnet 来运行客户端命令的。

#### Memcached 需要密码才能登录吗？

无需设置密码验证

#### 是否有可视化的数据库管理工具？

有，内置 Memcached-admin，访问地址：*http://服务器公网IP:9090*

#### 如何修改Memcached-admin 控制台密码？

运行下面的命令即可：  
```
htpasswd -b /etc/nginx/.htpasswd admin new_password
```

#### Memcached 服务端怎么配置？

参考 [命令与配置](/zh/solution-cli.md)