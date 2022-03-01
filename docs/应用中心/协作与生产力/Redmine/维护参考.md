---
sidebar_position: 2
slug: /redmine/admin
tags:
  - Redmine
  - 项目管理
---

# 维护参考

## 系统参数

Redmine 预装包包含 Redmine 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

本部署方案中的 Redmine 采用 Docker 部署，运行 `docker ps` 查看运行的容器。

```
CONTAINER ID   IMAGE                           COMMAND                  CREATED              STATUS                PORTS                               NAMES
4ff55aec7671   redmine                         "/docker-entrypoint.…"   11 seconds ago       Up 10 seconds         0.0.0.0:9010->3000/tcp              redmine
3067c535663b   mysql:5.7                       "docker-entrypoint.s…"   About a minute ago   Up 58 seconds         33060/tcp, 0.0.0.0:3309->3306/tcp   redmine-mysql
```

#### Redmine

Redmine 安装目录：*/data/wwwroot/redmine*  
Redmine 容器配置文件：*/data/wwwroot/redmine/docker-compose.yml*  
Redmine 系统配置文件：*/data/wwwroot/redmineconfig/configuration.yml*  

> configuration.yml 用于对 Redmine 进行个性配置，例如：设置 SMTP

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*

#### MySQL

本项目中 phpMyAdmin 是采用 Docker 方式来安装  

MySQL 配置文件目录: */data/db/mysql/mysql_config/conf.d*  
MySQL 数据目录：*/data/db/mysql/mysql_data*   
  
MySQL 可视化管理地址: *http://服务器公网IP:9090*

#### phpMyAdmin

本项目中 phpMyAdmin 是采用 Docker 方式来安装的 

#### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   
Docker daemon.json 文件：默认没有创建，请到 */etc/docker* 目录下根据需要自行创建   

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过 HTTP 访问 Redmine | 必须 |
| HTTPS | 443 | 通过 HTTP 访问 Redmine | 可选 |
| phpMyAdmin | 9090 | 通过 HTTP 访问 phpMyAdmin | 可选 |
| MySQL | 3306 | 本地电脑远程连接服务器上的 MySQL | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Nginx version
nginx -v

# List Installed Nginx Modules
nginx -V

# MySQL version
docker inspect redmine-mysql | grep "MYSQL_VERSION"

# Redmine Version
docker inspect redmine:latest |grep REDMINE_VERSION |head -1 |cut -d= -f2

# Docker Version
docker -v
```

### 服务

使用由Websoft9提供的Redmine部署方案，可能需要用到的服务如下：

### Redmine

```shell
sudo docker start redmine
sudo docker restart redmine
sudo docker stop redmine
sudo docker stats redmine
```

### MySQL

```shell
sudo docker start redmine-mysql
sudo docker restart redmine-mysql
sudo docker stop redmine-mysql
sudo docker stats redmine-mysql
```

### phpMyAdmin

```shell
sudo docker start phpmyadmin
sudo docker restart phpmyadmin
sudo docker stop phpmyadmin
sudo docker stats phpmyadmin
```

### Nginx

```shell
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
```

### Docker

```shell
sudo systemctl start docker
sudo systemctl restart docker
sudo systemctl stop docker
sudo systemctl status docker
```

### Docker-compose 服务

```
#创建容器编排
sudo docker-compose up

#创建容器编排并重建有变化的容器
sudo docker-compose up -d

#启动/重启
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

1. 通过 WinSCP 将网站目录（*/data/wwwroot/redmine*）**压缩后**再完整的下载到本地

2. 通过 phpMyAdmin 逐个导出数据库
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)

3. 将所有文件放到同一个文件夹，根据日期命名

4. 备份工作完成

更多备份相关方案，参考官方文档：[《RedmineBackupRestore》](https://redmine.org/projects/redmine/wiki/RedmineBackupRestore)

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


### Redmine升级

Redmine 采用 Docker 部署，其升级流程：拉取镜像 > 删除容器 > 重建容器

> Redmine 升级之前请完成服务器的快照备份，以防不测。

1. 使用 SSH 登录服务，进入到 redmine 目录后，拉取最新版本镜像
   ```
   cd /data/wwwroot/redmine
   docker-compose pull
   ```
   > 系统会自动拉取最新版镜像，如果没有镜像可拉取，则无需更新

2. 停止并删除当前的 Redmine 容器

   ```
   docker-compose down -v
   ```

3. 重新创建 Redmine 容器
   ```
   docker-compose up -d
   ```

## 故障处理

此处收集使用 Redmine 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### Redmine 无法启动？

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看日志
docker logs redmine
```

#### 新建工程，名称为中文的时候，系统报错？

数据库字符编码导致，需修改数据库字符编码为 utf8

## 常见问题

#### Redmine 支持多语言？

支持英文、中文等多种语言

#### Redmine 支持哪些SCM？

SVN, CVS, Git, Mercurial and Bazaar

#### Redmine有企业版吗？

官方没有提供企业版

#### Redmine 支持哪些数据库？

支持 MySQL, PostgreSQL, SQlite, SQL Server 等多种数据库，本部署方案采用 MySQL 作为数据库。

#### 是否有可视化的数据库管理工具？

已经安装 PHPMyAdmin 作为数据库管理工具

#### 如何禁止 phpMyAdmin 访问？

在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:9090** 端口是否开启，开启代表可以访问，反之则不可访问

#### 是否可以修改Redmine的源码路径？

不建议修改
