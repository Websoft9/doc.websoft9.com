---
sidebar_position: 2
slug: /erpnext/admin
tags:
  - ERPNext
  - 企业管理
  - ERP
---

# 维护参考

## 系统参数

ERPNext 预装包包含 ERPNext 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

本部署方案中的 ERPNext 采用 Docker 部署，运行 `docker ps` 查看运行的容器。

```
CONTAINER ID   IMAGE                        COMMAND                  CREATED             STATUS             PORTS                                       NAMES
949746dc0e88   frappe/frappe-socketio:v13   "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-socketio
030c4324b810   frappe/erpnext-worker:v13    "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-schedule
5816692bb579   frappe/erpnext-worker:v13    "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-worker-long
09b2e2242549   frappe/erpnext-worker:v13    "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-worker-short
2252928c2230   frappe/erpnext-worker:v13    "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-worker-default
4108b4ca06d5   redis:latest                 "docker-entrypoint.s…"   About an hour ago   Up About an hour   6379/tcp                                    erpnext-redis-cache
bbe639069a28   redis:latest                 "docker-entrypoint.s…"   About an hour ago   Up About an hour   6379/tcp                                    erpnext-redis-queue
29f4870961b4   mariadb:10.3                 "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp   erpnext-mariadb
9aecda1e6f3e   redis:latest                 "docker-entrypoint.s…"   About an hour ago   Up About an hour   6379/tcp                                    erpnext-redis-socketio
a404ca45d127   frappe/erpnext-nginx:v13     "/docker-entrypoint.…"   About an hour ago   Up About an hour   0.0.0.0:8000->80/tcp, :::8000->80/tcp       erpnext-nginx
39d908b3132e   frappe/erpnext-worker:v13    "docker-entrypoint.s…"   About an hour ago   Up About an hour                                               erpnext-worker
```

> erpnext-worker-default 为项目主容器

#### ERPNext

ERPNext 路径:  */data/wwwroot/erpnext*  
ERPNext 数据库配置文件: */data/wwwroot/erpnext/.env*  
ERPNext 日志路径:  */data/wwwroot/erpnext/volumes/erpnext-logs-vol*  
ERPNext 应用路径 : */data/wwwroot/frappe-bench/volumes/erpnext-site-vol*  
ERPNext 附件路径:  */data/wwwroot/frappe-bench/volumes/erpnext-assets-vol*   

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*

#### MariaDB

MariaDB 数据目录 */data/db/mariadb/data*  
MariaDB 日志目录: */data/db/mariadb/log*  
MariaDB 配置文件：*/data/db/mariadb/config/conf.d*  

MySQL 可视化管理参考 [MySQL 管理](/zh/admin-mysql.md) 章节。

####  phpMyAdmin

phpMyAdmin 是一款可视化 MySQL 管理工具，在本项目中它基于 Docker 安装。  

phpMyAdmin directory：*/data/apps/phpmyadmin*  
phpMyAdmin docker compose file：*/data/apps/phpmyadmin/docker-compose.yml* 

#### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   
Docker daemon.json 文件：默认没有创建，请到 */etc/docker* 目录下根据需要自行创建   

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过 HTTP 访问 ERPNext | Required |
| HTTP | 443 | 通过 HTTPS 访问 ERPNext| Optional |
| HTTP | 8000 | 通过端口直接访问 ERPNext| Optional |
| TCP | 9090 | 数据库可视化工具 phpMyAdmin | Optional |
| TCP | 3306 | 远程访问 MariaDB 数据库 | Optional |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Docker Version
docker -v

# Nginx version
nginx -v
```

### 服务

使用由Websoft9提供的 ERPNext 部署方案，可能需要用到的服务如下：

#### ERPNext

```shell
sudo docker start erpnext-worker
sudo docker stop erpnext-worker
sudo docker restart erpnext-worker
sudo docker status erpnext-worker

```

```shell
sudo docker start erpnext-worker-short
sudo docker stop erpnext-worker-short
sudo docker restart erpnext-worker-short
sudo docker status erpnext-worker-short

```

```shell
sudo docker start erpnext-worker-long
sudo docker stop erpnext-worker-long
sudo docker restart erpnext-worker-long
sudo docker status erpnext-worker-long

```

```shell
sudo docker start erpnext-nginx
sudo docker stop erpnext-nginx
sudo docker restart erpnext-nginx
sudo docker status erpnext-nginx

```

#### Nginx

```shell
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
```

#### MariaDB

```shell
sudo docker start erpnext-mariadb
sudo docker stop erpnext-mariadb
sudo docker restart erpnext-mariadb
sudo docker status erpnext-mariadb

```

#### Redis

```shell
sudo docker start erpnext-redis-queue
sudo docker stop erpnext-redis-queue
sudo docker restart erpnext-redis-queue
sudo docker status erpnext-redis-queue

```

```shell
sudo docker start erpnext-redis-cache
sudo docker stop erpnext-redis-cache
sudo docker restart erpnext-redis-cache
sudo docker status erpnext-redis-cache

```

```shell
sudo docker start erpnext-redis-schedule
sudo docker stop erpnext-redis-schedule
sudo docker restart erpnext-redis-schedule
sudo docker status erpnext-redis-schedule

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

1. 通过 WinSCP 将网站目录（*/data/wwwroot/frappe-bench*）**压缩后**再完整的下载到本地

2. 通过 **mysqldump** 备份 erpnext 数据库
   ```
   mysqldump -uroot -p erpnext>erpnext.sql
   ```
   > ERPNext 超过 1000 个表且部分表中字段过多，使用 phpMyAdmin 导出数据库可能会丢失数据

3. 将程序文件和数据库文件放到同一个文件夹，根据日期命名

4. 备份工作完成


### ERPNext 备份

ERPNext 提供了自动备份（计划任务）和[手动输入命令](https://frappeframework.com/docs/user/en/bench/reference/backup)的两种备份方式。


1. 登录 ERPNext 后，依次打开：【Settings】>【System Settings】
   ![ERPNext backup](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-autobk-websoft9.png)

2. 进入 ERPNext 主容器
   ```
   docker exec -it erpnext-worker-default  bash
   ```
3. 在容器中运行备份命令
   ```
   # 查询项目文件夹名称（IP 或 域名）
   ls

   # 备份
   bench --site 121.41.86.118 backup
   ```

4. 在宿主机的 Docker VOLUME 中获取备份文件。备份位置：*/var/lib/docker/volumes/docker-erpnext_sites-vol/_data/IP/private/backups*

   > 后台 Download Backups 处下载失败，原因有待研究。故，直接从上面的路径下载即可


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

### ERPNext 更新

ERPNext 基于 Docker 部署，其升级流程：拉取镜像 > 删除容器 > 重建容器

> 升级之前请确保您已经完成了服务器的镜像（快照）备份

1. 登录服务器，删除旧容器
   ```
   docker-compose down -v
   ```
2. 编辑 */data/wwwroot/erpnext/.env* 文件，将版本变量的值修改为目标版本号

2. 拉取目标版本的镜像
   ```
   cd /data/wwwroot/erpnext
   docker-compose pull
   ```
   > 如果显示没有镜像可拉取，则无需升级

3. 重新创建 ERPNext 容器
    ```
    docker-compose up -d
    ```

## 故障处理

此处收集使用 ERPNext 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

ERPNext 报错后，有如下几个可以分析日志的入口：

1. ERPNext 程序运行日志：*/data/logs/erpnext*
2. 进程管理日志，运行 `systemctl status erpnext -l` 查看
3. Nginx日志：*/data/logs/nginx*

检索关键词 **Failed** 或者 **error** 查看错误

#### ERPNext服务无法启动？

1. 运行`docker status erpnext`，便可以查看启动状态和错误

2. 打开日志文件：*/data/logs/erpnext*，检索 **failed** 关键词，分析错误原因


#### 在Chrome下修改密码后报错？

这个并不是服务器端的问题，只要更新浏览器即可。

#### 运行Bench时报错 "You should not run this command as root" when run bench?

Bench只能通过frapper运行,必须先切换到此用户

```shell
su - frapper
```

#### ERPNext 安装向导最后一步出现错误提示？
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-wizarderror-websoft9.png)

原因：未知   
方案：重复安装几次直至成功   

## 常见问题

#### 本项目中 ERPNext 采用何种安装方式？

采用 Docker 安装，查看我们提供的 [Docker-Compose for ERPNext](https://github.com/Websoft9/docker-erpnext) 开源项目

#### ERPNext 支持非 Docker 安装方式吗？

支持，具体的安装大致流程如下：

1. 使用Bench命令初始化一个Frappe框架
2. 安装ERPNext app
3. 创建一个名称同样为 ERPNext 的site
4. 将site与app 连接起来

#### Frappe，bench，ERPNext 有什么关系和区别？

ERPNext 是基于 [Frappe](https://github.com/frappe/frappe) 框架开发的免费 ERP 。而 Frappe 是一个用于快速开发JS和Python集成化应用的框架。[Bench](https://github.com/frappe/bench) 是Frappe框架体系中的 CLI 工具，用于创建和管理基于 Frappe 的应用程序。

#### ERPNext 安装的时候需要创建 site 是什么原理？

Frappe 框架主要由两个部分组成：app 和 site，app 是后端Python代码，site 是用于处理 HTTP 请求的前端部分。

#### ERPNext 支持外部数据库吗？

支持，只需在[数据库配置文件](/zh/stack-components.md#erpnext) 中添加 db_host 为外部数据库地址即可。更多数据库连接参数参考官方文档[Standard Config](https://frappeframework.com/docs/user/en/basics/site_config#mandatory-settings)

#### ERPNext 支持哪些数据库？

MariaDB 和 PostgreSQL

#### 数据库用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有可视化数据库管理工具 phpMyAdmin,访问地址：*http://服务器公网IP:9090*

#### 是否可以修改 ERPNext 的源码路径？

不建议

#### 是否有ERPNext的API文档？

有，包括Python，Javascript，Jinja API等，参考官方文档[ERPNext API](https://frappeframework.com/docs/user/en/api)

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R erpnext.erpnext /data/wwwroot/erpnext
# 读写执行权限
find /data/wwwroot/erpnext -type d -exec chmod 750 {} \;
find /data/wwwroot/erpnext -type f -exec chmod 640 {} \;
```