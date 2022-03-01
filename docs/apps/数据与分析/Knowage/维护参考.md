---
sidebar_position: 2
slug: /knowage/admin
tags:
  - Knowage
  - 大数据分析
  - BI
---

# 维护参考

## 系统参数

Knowage 预装包包含 Knowage 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

本项目采用 Docker 安装，运行 `docker ps` 可以查看所有相关的容器：

```
CONTAINER ID   IMAGE                                              COMMAND                  CREATED        STATUS                 PORTS                               NAMES
3b30d327e903   mariadb:10.3                                       "docker-entrypoint.s…"   2 hours ago    Up 2 hours             0.0.0.0:3307->3306/tcp              knowage-mariadb-server
a28572948615   knowagelabs/knowage-server-docker:8.0.0-SNAPSHOT   "./entrypoint.sh ./a…"   2 hours ago    Up 2 hours (healthy)   0.0.0.0:8080->8080/tcp              knowage-server
90d49e9971bf   mariadb:10.3                                       "docker-entrypoint.s…"   2 hours ago    Up 2 hours             3306/tcp                            knowage-mariadb-cache
fa5d3ce16865   knowagelabs/knowage-python-docker:8.0.0-SNAPSHOT   "./entrypoint.sh gun…"   2 hours ago    Up 2 hours (healthy)   5000/tcp                            knowage-python
7fbfe56727d5   knowagelabs/knowage-r-docker:8.0.0-SNAPSHOT        "./entrypoint.sh r k…"   2 hours ago    Up 2 hours (healthy)   5001/tcp                            knowage-r
```

#### Knowage server

Knowage-Server 资源目录：*/data/wwwroot/knowage/resources*  

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*

#### MariaDB

MariaDB 数据目录：*/data/db/mariadb*  
MariaDB 可视化管理地址: *http://服务器公网IP:9090*，用户名和密码请见 [账号密码](/zh/stack-accounts.md) 章节。  

#### phpMyAdmin on Docker

本部署方案中的 phpMyAdmin 采用 Docker 部署。

#### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 80 | 通过 HTTP 访问 Knowage 控制台 | 可选 |
| TCP | 9001 | 通过 HTTP 访问 Knowage 控制台 | 可选 |
| TCP | 9090 | 通过 HTTP 访问 phpMyAdmin 控制台 | 可选 |
| TCP | 3306 | MariaDB 服务端口 | 可选 |

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

# MariaDB version

docker inspect knowage-mariadb-server | grep "MARIADB_VERSION"

# Knowage Version
docker images |grep knowagelabs |awk '{print $2}' |head -1 |cut -d- -f1
```


### 服务


使用由Websoft9提供的 Knowage 部署方案，可能需要用到的服务如下：

#### Knowage Server on Docker

```shell
sudo docker inspect knowage-server
sudo docker start knowage-server
sudo docker restart knowage-server
sudo docker stop knowage-server
sudo docker rm knowage-server

# 进入容器运行命令
sudo docker exec -it knowage-server /bin/bash
```

#### MariaDB Server on Docker
```shell
sudo docker inspect knowage-mariadb-server
sudo docker start knowage-mariadb-server
sudo docker restart knowage-mariadb-server
sudo docker stop knowage-mariadb-server
sudo docker rm knowage-mariadb-server

# 进入容器运行命令
sudo docker exec -it knowage-mariadb-server /bin/bash
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

1. 通过 SFTP 将网站目录（*/data/wwwroot/knowage*）**压缩后**再完整的下载到本地
2. 通过 phpMyAdmin 导出数据库
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

### Knowage 升级

本部署基于 Docker 安装，故遵循 Docker 标准的升级流程，具体方案如下：

> 升级 Knowage 之前，请务必做好服务器的快照备份。

1. 使用 SSH 登录到服务器，进入到 docker-compose 文件所在的目录后拉取最新的 Docker 镜像
   ```
   cd /data/knowage/knowage-server
   docker-compose pull
   ```
2. 停止当前的运行容器
   ```
   docker-compose down -v
   ```
3. 重新创建新的容器
   ```
   docker-compose up -d
   ```

## 故障处理

此处收集使用 Knowage 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看 Knowage-Server 错误日志？

运行命令 `docker logs knowage-server` 即可查看错误日志

#### Knowage服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看日志
docker logs knowage-server
```
## 常见问题

#### Knowage 支持多语言吗？

支持，但不包含中文

#### 采用哪种方式安装 Knowage？

本项目采用官方的 Docker 镜像安装，同时预设了持久化存储

#### Knowage 与 SpagoBI 有什么关系？

Knowage 是 SpagoBI 更名后的产品

#### 如果没有域名是否可以部署 Knowage？

可以，直接通过：*http://服务器公网IP:8080/knowage* 或 *http://服务器公网IP* 访问即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：*http://服务器公网IP:9090*

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R knowage.knowage /data/wwwroot/knowage
# 读写执行权限
find /data/wwwroot/knowage -type d -exec chmod 750 {} \;
find /data/wwwroot/knowage -type f -exec chmod 640 {} \;
```

