---
sidebar_position: 2
slug: /alfresco/admin
tags:
  - Alfresco
  - 企业管理
  - ERP
---

# 维护参考

## 系统参数

Alfresco 预装包包含 Alfresco 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

本部署方案中的 Alfresco 采用 Docker 部署，运行 `docker ps` 查看运行的容器。
```
CONTAINER ID   IMAGE                                                  COMMAND                  CREATED             STATUS             PORTS                                                                                                                                                                                NAMES
3d2afa8a1cc7   alfresco/alfresco-acs-nginx:3.1.1                      "/entrypoint.sh"         About an hour ago   Up About an hour   80/tcp, 0.0.0.0:8080->8080/tcp, :::8080->8080/tcp                                                                                                                                    alfresco-proxy
b42251c78a71   alfresco/alfresco-search-services:2.0.1                "/bin/sh -c '$DIST_D…"   About an hour ago   Up About an hour   10001/tcp, 0.0.0.0:8083->8983/tcp, :::8083->8983/tcp                                                                                                                                 alfresco-solr6
a381a9646f4b   alfresco/alfresco-transform-core-aio:2.3.10            "/bin/sh -c 'java $J…"   About an hour ago   Up About an hour   0.0.0.0:8090->8090/tcp, :::8090->8090/tcp                                                                                                                                            alfresco-transform
af14e4d3cd86   alfresco/alfresco-content-repository-community:7.0.0   "catalina.sh run -se…"   About an hour ago   Up About an hour   8000/tcp, 8080/tcp, 10001/tcp                                                                                                                                                        alfresco-content
50059f56edff   postgres:13.1                                          "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp                                                                                                                                            alfresco-postgres
692e2acf019d   alfresco/alfresco-activemq:5.16.1                      "/bin/sh -c '${ACTIV…"   About an hour ago   Up About an hour   0.0.0.0:5672->5672/tcp, :::5672->5672/tcp, 0.0.0.0:8161->8161/tcp, :::8161->8161/tcp, 0.0.0.0:61613->61613/tcp, :::61613->61613/tcp, 0.0.0.0:61616->61616/tcp, :::61616->61616/tcp   alfresco-activemq
ca3a6baf750e   alfresco/alfresco-share:7.0.0                          "/usr/local/tomcat/s…"   About an hour ago   Up About an hour   8000/tcp, 8080/tcp                                                                                                                                                                   alfresco-share
4a0c8d7e6c2e   dpage/pgadmin4                                         "/entrypoint.sh"         About an hour ago   Up About an hour   443/tcp, 0.0.0.0:9090->80/tcp, :::9090->80/tcp                                                                                                                                       pgadmin
```

#### Alfresco

Alfresco 安装目录： */data/wwwroot/alfresco*  
Alfresco 容器存储目录： */data/wwwroot/alfresco/volumes/alfresco*  
Alfresco 日志目录： */data/wwwroot/alfresco/volumes/alfresco/share/logs*  

> 上传的文档存放在...

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*  
Nginx 验证访问文件：*/etc/nginx/.htpasswd/htpasswd.conf*  

#### PostgreSQL

PostgreSQL 数据目录：*/data/db/postgresql/data*  
PostgreSQL 日志目录: */data/db/postgresql/log*  

#### pgAdmin

pgAdmin 是官方出品的可视化 PostgreSQL 管理工具，采用 Docker 安装

pgAdmin 存储目录: */data/apps/pgadmin*  
pgAdmin 配置文件: */data/apps/pgadmin/.env*  

#### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   
Docker daemon.json 文件：默认没有创建，请到 */etc/docker* 目录下根据需要自行创建   

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 80 | 通过 HTTP 访问 Alfresco Share  | 必要 |
| TCP | 443 | 通过 HTTPS 访问 Alfresco Share | 可选 |
| TCP | 8080 | 通过 HTTP 访问 Alfresco 入口 | 可选 |
| TCP | 5432 | PostgreSQL 远程访问 | 可选 |
| TCP | 9090 | 通过 HTTP 访问 pgAdmin | 可选 |

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

# PostgreSQL version
docker images |grep postgres |awk '{print $2}'

# Alfresco version
docker images |grep alfresco-share |awk '{print $2}'
```

### 服务

使用由Websoft9提供的 Alfresco 部署方案，可能需要用到的服务如下：

#### Alfresco

Alfresco 使用 7 个容器，因此直接使用 Docker-compose 管理所有容器的服务器

```shell

cd /data/wwwroot/alfresco

sudo docker-compose start alfresco-server
sudo docker-compose stop alfresco-server
sudo docker-compose restart alfresco-server
```

#### PostgreSQL

```shell
sudo docker start alfresco-postgres
sudo docker restart alfresco-postgres
sudo docker stop alfresco-postgres
sudo docker stats alfresco-postgres
```


#### pgAdmin

```shell
sudo docker start pgadmin
sudo docker stop pgadmin
sudo docker restart pgadmin
sudo docker stats pgadmin
```

#### Docker

```shell
sudo systemctl start docker
sudo systemctl restart docker
sudo systemctl stop docker
sudo systemctl status docker
```

#### Docker-compose

```
#创建容器编排
sudo docker-compose up -d

#启动/停止/重启
sudo docker-compose start
sudo docker-compose stop
sudo docker-compose restart
```

#### Nginx

```shell
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
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

1. 通过 SFTP 将网站目录（*/data/wwwroot/alfresco*）**压缩后**再完整的下载到本地

2. 通过 [pgAdmin](/zh/admin-postgresql.md) 导出数据库

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

### Alfresco 升级

Alfresco 基于 Docker 部署，其升级流程：拉取镜像 > 删除容器 > 重建容器

> 升级之前请确保您已经完成了服务器的镜像（快照）备份

1. 登录服务器，编辑 */data/wwwroot/alfresco/.env* 文件，将版本变量的值修改为目标版本号

2. 拉取目标版本的镜像
   ```
   cd /data/wwwroot/alfresco
   docker-compose pull
   ```
   > 如果显示没有镜像可拉取，则无需升级

3. 删除旧容器，重新创建 Alfresco 容器
    ```
    docker-compose down -v
    docker-compose up -d
    ```


## 故障处理


此处收集使用 Alfresco 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### Alfresco 服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
docker ps
```

## 常见问题

#### 中文 Markdown 格式预览乱码？

暂无方案

#### Alfresco 是否支持多语言？

支持（包含中文），后台可以自行切换

#### Alfresco Content Services Enterprise 与 Alfresco Community Edition 有什么不同？

Alfresco Community Edition 是 Alfresco Content Services Enterprise 的开源版本，参考[对比](https://www.alfresco.com/alfresco-content-services-enterprise-vs-alfresco-community-edition)

#### Alfresco 支持哪些文件格式？

参考[Alfresco支持所有文件格式](https://www.alfresco.com.cn/alfresco-formats)

#### 本项目中 Alfresco 采用何种安装方式？

Docker

#### 如果没有域名是否可以部署 Alfresco？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置 pgAdmin，访问地址：*http://服务器公网IP:9090*

#### 是否可以修改Alfresco的源码路径？

不可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R apache.apache /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```
