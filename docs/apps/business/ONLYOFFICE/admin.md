---
sidebar_position: 2
slug: /onlyoffice/admin
tags:
  - ONLYOFFICE
  - 企业管理
  - ERP
  - Document on line
---

# 维护参考

## 系统参数

ONLYOFFICE 预装包包含 ONLYOFFICE 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### ONLYOFFICE

本项目中的 ONLYOFFICE 是由：ONLYOFFICE Community Server 和 ONLYOFFICE Document Server 组成，它们均基于 Docker 安装，并完成了集成。

##### ONLYOFFICE Community Server

ONLYOFFICE Community Server存储目录： */data/wwwroot/communityserver*  
ONLYOFFICE docker-compose 文件路径： */data/wwwroot/onlyoffice/docker-compose.yml*  
ONLYOFFICE 日志目录： */data/wwwroot/onlyoffice/communityserver/logs*

##### ONLYOFFICE Document Server

ONLYOFFICE Document Server存储目录： */data/apps/onlyofficedocumentserver*  
ONLYOFFICE docker-compose 文件路径： */data/apps/onlyofficedocumentserver/docker-compose.yml*  
ONLYOFFICE 日志目录： */data/apps/onlyofficedocumentserver/logs*

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*

#### MySQL

MySQL 安装路径: */usr/local/mysql*  
MySQL 数据文件 */data/mysql*  
MySQL 配置文件: */etc/my.cnf*  

MySQL 可视化管理参考 [MySQL 管理](/zh/admin-mysql.md) 章节。

####  phpMyAdmin

phpMyAdmin 是一款可视化 MySQL 管理工具，在本项目中它基于 Docker 安装。  

phpMyAdmin directory：*/data/apps/phpmyadmin*  
phpMyAdmin docker compose file：*/data/apps/phpmyadmin/docker-compose.yml*  

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 类型 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 80 | 通过 HTTP 访问 ONLYOFFICE | 必须 |
| TCP | 443 | 通过 HTTPS 访问 ONLYOFFICE | 可选 |
| TCP | 3306 | 远程连接 MySQL | 可选 |
| TCP | 9003 | 通过端口访问 ONLYOFFICE | 可选 |
| TCP | 9002 | ONLYOFFICE Document Server on Docker | 可选 |
| TCP | 9090 | phpMyAdmin on Docker | 可选 |

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

# ONLYOFFICE version
onlyofficectl status | grep ONLYOFFICE*

# Dokcer version
docker --version

# MySQL version
mysql -V

# ONLYOFFICE Community Server version
docker image inspect onlyoffice/communityserver  | grep onlyoffice.community.version | sed -n 1p
```
### 服务

使用由Websoft9提供的 ONLYOFFICE 部署方案，可能需要用到的服务如下：

#### ONLYOFFICE Community Server on Docker

```shell
sudo docker inspect onlyofficecommunityserver
sudo docker start onlyofficecommunityserver
sudo docker restart onlyofficecommunityserver
sudo docker stop onlyofficecommunityserver
sudo docker rm onlyofficecommunityserver

# 进入容器运行命令
sudo docker exec -it onlyofficecommunityserver /bin/bash
```


#### ONLYOFFICE Document Server on Docker

```shell
sudo docker inspect onlyofficedocumentserver
sudo docker start onlyofficedocumentserver
sudo docker restart onlyofficedocumentserver
sudo docker stop onlyofficedocumentserver
sudo docker rm onlyofficedocumentserver

# 进入容器运行命令
sudo docker exec -it onlyofficedocumentserver /bin/bash
```

#### MySQL Server on Docker
```shell
sudo docker inspect onlyoffice-mysql-server
sudo docker start onlyoffice-mysql-server
sudo docker restart onlyoffice-mysql-server
sudo docker stop onlyoffice-mysql-server
sudo docker rm onlyoffice-mysql-server

# 进入容器运行命令
sudo docker exec -it onlyoffice-mysql-server /bin/bash
```

#### phpMyAdmin on Docker
```shell
sudo docker inspect phpmyadmin
sudo docker start phpmyadmin
sudo docker restart phpmyadmin
sudo docker stop phpmyadmin
sudo docker rm phpmyadmin
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
sudo systemctl stop docker
sudo systemctl restart docker
sudo systemctl status docker
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

1. 通过 SFTP 将网站目录（*/data/wwwroot/onlyoffice*）**压缩后**再完整的下载到本地

2. 通过 phpMyAdmin导出 ONLYOFFICE 数据库
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)

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

### ONLYOFFICE升级

ONLYOFFICE 采用 [Docker 部署](https://github.com/ONLYOFFICE/Docker-CommunityServer#upgrading-onlyoffice-community-server)，其升级流程：拉取镜像 > 删除容器 > 重建容器

> 升级之前请完成服务器的快照备份，以防不测。

1. 使用 SSH 登录服务，进入到 ONLYOFFICE 目录后，拉取最新版本镜像
   ```
   cd /data/wwwroot/onlyoffice
   sudo docker-compose pull
   ```
   > 系统会自动拉取最新版镜像，如果没有镜像可拉取，则无需更新

2. 停止并删除当前的 ONLYOFFICE 容器

   ```
   sudo docker-compose down -v
   ```

3. 重新创建 ONLYOFFICE 容器
    ```
   docker-compose up -d
   ```

## 故障处理

此处收集使用 ONLYOFFICE 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### ONLYOFFICE 服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看容器服务
sudo docker inspect onlyofficecommunityserver
sudo docker logs onlyofficecommunityserver
```

#### 修改 MySQl 数据库密码之后 ONLYOFFICE 无法启动？

修改密码之后需要需改 ONLYOFFICE docker-compose 文件中对应的数据库密码： */data/wwwroot/onlyoffice/docker-compose.yml*，然后运行如下命令：

```
cd /data/wwwroot/onlyoffice
docker-compose down -v
docker-compose up -d
```

#### ONLYOFFICE 显示502错误？

首先通过命令 `sudo docker logs onlyofficecommunityserver`，查看是否有错误日志。  

一般是由文件权限不足或数据连接问题导致。

#### 重新安装了数据库导致 ONLYOFFICE 无法运行？

ONLYOFFICE 对数据库的配置有严格的要求，保证符合如下要求：

```
echo "[mysqld]
sql_mode = 'NO_ENGINE_SUBSTITUTION'
max_connections = 1000
max_allowed_packet = 1048576000
group_concat_max_len = 2048
log-error = /var/log/mysql/error.log" > /app/onlyoffice/mysql/conf.d/onlyoffice.cnf
```

## 常见问题

#### ONLYOFFICE 是否支持中文？

支持，可以在线切换多种语言

#### Community Edition vs Enterprise Edition？

参考官方说明 [Compare Community Edition and Enterprise Edition](https://github.com/ONLYOFFICE/CommunityServer#compare-community-edition-and-enterprise-edition)

#### 能否介绍 ONLYOFFICE 各种版本的关系？

OnlyOffice的产品家族比较复杂，根据官方的介绍，可以分为：

* ENTERPRISE EDITION：企业版
* COMMUNITY EDITION：开源版
* INTEGRATION EDITION：比如集成了 ownCloud 的版本
* DEVELOPER EDITION：开发者版本

其中每一个版本都是由：Community Server, Document Server, Mail Server 组成。  

COMMUNITY EDITION 是一个完全免费的版本。DEVELOPER EDITION 是适用于开发者的[收费版本](https://www.onlyoffice.com/zh/developer-edition-prices.aspx)。

#### ONLYOFFICE 开源版并发连接数有限制吗？

并发连接数不超过20个（Up to 20 Simultaneous connections）

#### ONLYOFFICE Document Server 同时连接数是如何规定的？

ONLYOFFICE Document Server 同时连接数是指用户在编辑模式下打开文档的数量。  
例如，对于具有200个同时连接的许可证，一个用户可以打开200个文档，200个用户每个可以打开一个，50个用户每个可以打开4个文档等。  
以何种方式并不重要，但文档服务器只会根据您购买的许可证处理编辑请求的数量。  
超过此数量的连接以预览模式打开文档。  

#### 数据库密码可以修改吗？

可以，但是修改后需要同步修改 ONLYOFFICE docker-compose 文件，然后通过 docker-compose 重新运行容器。

#### 如果没有域名是否可以部署 ONLYOFFICE？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：*http://服务器公网IP:9090*

#### 如何禁止外界访问phpMyAdmin？

服务器安全组中关闭 9090 端口即可

#### 是否可以修改ONLYOFFICE的源码路径？

不可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R onlyoffice.onlyoffice /data/wwwroot/onlyoffice
# 读写执行权限
find /data/wwwroot/onlyoffice -type d -exec chmod 750 {} \;
find /data/wwwroot/onlyoffice -type f -exec chmod 640 {} \;
```
