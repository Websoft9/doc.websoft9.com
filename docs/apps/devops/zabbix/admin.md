---
sidebar_position: 2
slug: /zabbix/admin
tags:
  - Zabbix 
  - DevOps
---

# 维护参考

## 系统参数

Zabbix 预装包包含 Zabbix 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

> 本自动化部署方案默认安装：Zabbix-Server, Zabbix-Agent, Zabbix-Web, Zabbix-snmptraps, Zabbix-java-gateway 等组件。

### 路径

#### Zabbix

本部署方案中的 Zabbix 采用 Docker部署以适应云原生时代。运行 `docker ps` 查看运行的容器。

```
$docker ps
CONTAINER ID   IMAGE                                              COMMAND                  CREATED       STATUS                 PORTS                                         NAMES
18540fbd8378   zabbix/zabbix-web-apache-mysql:centos-5.2-latest   "docker-entrypoint.sh"   7 hours ago   Up 7 hours (healthy)   0.0.0.0:80->8080/tcp, 0.0.0.0:443->8443/tcp   zabbix-web
ed7551e10595   zabbix/zabbix-agent:centos-5.2-latest              "/sbin/tini -- /usr/…"   7 hours ago   Up 7 hours             0.0.0.0:10050->10050/tcp                      zabbix-agent
584c72d4110c   zabbix/zabbix-server-mysql:centos-5.2-latest       "/sbin/tini -- /usr/…"   7 hours ago   Up 7 hours             0.0.0.0:10051->10051/tcp                      zabbix-server
cacb13aa8f36   zabbix/zabbix-java-gateway:centos-5.2-latest       "docker-entrypoint.s…"   7 hours ago   Up 7 hours             0.0.0.0:10052->10052/tcp                      zabbix-java-gateway
7f86df1ec563   zabbix/zabbix-snmptraps:centos-5.2-latest          "/usr/sbin/snmptrapd…"   7 hours ago   Up 7 hours             0.0.0.0:162->1162/udp                         zabbix-snmptraps
01bf45e40f13   phpmyadmin/phpmyadmin                              "/docker-entrypoint.…"   8 hours ago   Up 8 hours             0.0.0.0:9090->80/tcp                          phpmyadmin

```

Zabbix 安装目录: */data/zabbix*  
Zabbix 配置文件（环境变量）: */data/zabbix/.env.xxx*    
Docker Compose 配置文件：*/data/wwwroot/zabbix/docker-compose.yml*     
Zabbix 持久存储：*/data/wwwroot/zabbix/zbx_env  
Zabbix-Web 数据库配置：*/data/wwwroot/zabbix/.env_db_mysql*  
Zabbix-Proxy 数据库配置：*/data/wwwroot/zabbix/.env_db_mysql_proxy*   


> Zabbix 配置文件中包含数据库连接信息，更改了 MySQL 数据库账号密码，此处也需要对应修改

#### MySQL

MySQL 安装路径: */usr/local/mysql*  
MySQL 数据文件 */data/mysql*  
MySQL 配置文件: */etc/my.cnf*  

MySQL 可视化管理参考 [MySQL 管理](/zh/admin-mysql.md) 章节。

#### phpMyAdmin

phpMyAdmin 是一款可视化 MySQL 管理工具，在本项目中它基于 Docker 安装。  

phpMyAdmin directory：*/data/apps/phpmyadmin*  
phpMyAdmin docker compose file：*/data/apps/phpmyadmin/docker-compose.yml*  

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*  

#### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   
Docker daemon.json 文件：默认没有创建，请到 */etc/docker* 目录下根据需要自行创建   


### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过 HTTP 访问 Zabbix | 必须 |
| HTTP | 9006 | 通过端口访问 Zabbix  | 可选 |
| HTTPS | 443 | 通过 HTTPS 访问 Zabbix | 可选 |
| MySQL | 3306 | 远程连接 MySQL | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Docker version
docker -v

# MySQL version
mysql -v

# Zabbix version:
docker images |grep zabbix-server
```

### 服务

使用由Websoft9提供的 Zabbix 部署方案，可能需要用到的服务如下：

### Zabbix-Server

```shell
sudo docker start zabbix-server
sudo docker restart zabbix-server
sudo docker stop zabbix-server
sudo docker stats zabbix-server
```

### Zabbix-Web

```shell
sudo docker start zabbix-web
sudo docker restart zabbix-web
sudo docker stop zabbix-web
sudo docker stats zabbix-web
```

### Zabbix-Proxy

```shell
sudo docker start zabbix-proxy
sudo docker restart zabbix-proxy
sudo docker stop zabbix-proxy
sudo docker stats zabbix-proxy
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
sudo sudo systemctl start nginx
sudo sudo systemctl stop nginx
sudo sudo systemctl restart nginx
sudo sudo systemctl status nginx
```

### MySQL

```shell
sudo sudo systemctl start mysql
sudo sudo systemctl stop mysql
sudo sudo systemctl restart mysql
sudo sudo systemctl status mysql
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

1. 通过 SFTP 将网站目录（*/data/wwwroot/zabbix*）**压缩后**再完整的下载到本地
2. 使用 phpMyAdmin 导出 Zabbix 数据库
3. 将程序文件、数据文件和数据库文件放到同一个文件夹，根据日期命名
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

## 故障处理

此处收集使用 Zabbix 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 修改了数据库密码 Zabbix 不能访问？

若已完成 Zabbix 安装向导，再通过 phpMyAdmin 修改数据库密码，Zabbix 就会连不上数据库。  

1. 使用 SFTP 连接服务器，修改两个 [Zabbix 数据库配置](/zh/stack-components.md#zabbix) 文件中的密码。  

2. 重新运行容器
   ```
   cd /data/wwwroot/zabbix
   sudo docker compose up -d
   ```
#### Zabbix-server 服务无法启动？

运行 `sudo docker logs zabbix-server` 查询运行日志。  

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
sudo systemctl status mysql
sudo journalctl -u mysql
```

## 常见问题

#### Zabbix 支持多语言吗？

支持多语言（包含中文），通过[后台设置](/zh/solution-more.html#zabbix-语言包)即可

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

#### 是否可以使用云平台的 RDS 作为 Zabbix 的数据库？

可以

#### Zabbix-Server 能在 Windows 服务器上部署吗？

官方没有提供 Windows 上的安装方案

#### Zabbix数据库连接配置信息在哪里？

数据库配置信息 [Zabbix 环境变量](/zh/stack-components.html#zabbix)中

#### 如果没有域名是否可以部署 Zabbix？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

从安全角度考虑，本部署包中没有预装 phpMyAdmin

#### 是否可以修改 Zabbix 的源码路径？

不建议修改

#### 如何修改上传的文件所属用户（组）和读写权限?

```shell
#例如：用户为 apache
chown -R apache.apache /data/wwwroot

#例如：用户为 nginx
chown -R nginx.nginx /data/wwwroot

#修改读写执行权限
find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```