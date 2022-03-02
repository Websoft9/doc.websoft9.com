---
sidebar_position: 2
slug: /cloudbeaver/admin
tags:
  - CloudBeaver
  - 虚拟桌面
  - 数据库可视化管理工具
---

# 维护参考

## 系统参数

CloudBeaver 预装包包含 CloudBeaver 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

本部署方案中的 CloudBeaver 采用 Docker 部署，运行 `docker ps` 查看运行的容器。
```
CONTAINER ID   IMAGE                        COMMAND             CREATED       STATUS       PORTS                                       NAMES
34baab38d75f   dbeaver/cloudbeaver:latest   "./run-server.sh"   3 hours ago   Up 3 hours   0.0.0.0:8080->8978/tcp, :::8080->8978/tcp   cloudbeaver
```

#### CloudBeaver

CloudBeaver 安装目录： */data/apps/cloudbeaver*  
CloudBeaver 存储目录： */data/apps/cloudbeaver/volumes*  
CloudBeaver 配置文件： */data/apps/cloudbeaver/volumes/GlobalConfiguration/.dbeaver/data-sources.json*  

> data-sources.json 存放数据库连接信息

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*  
Nginx 验证访问文件：*/etc/nginx/.htpasswd/htpasswd.conf*  

#### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   
Docker daemon.json 文件：默认没有创建，请到 */etc/docker* 目录下根据需要自行创建   

#### Redis

Redis 配置文件： */etc/redis.conf*  
Redis 数据目录： */var/lib/redis*  
Redis 日志文件： */var/log/redis/redis.log*

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 80 | 通过 HTTP 访问 CloudBeaver 控制台 | 必选 |
| TCP | 443 | 通过 HTTPS 访问 CloudBeaver 控制台 | 可选 |
| TCP | 9093 | 通过 HTTP 访问 CloudBeaver 控制台 | 可选 |

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

# CloudBeaver version

```

### 服务

使用由Websoft9提供的 CloudBeaver 部署方案，可能需要用到的服务如下：

#### CloudBeaver

```shell
sudo docker start cloudbeaver
sudo docker stop cloudbeaver
sudo docker restart cloudbeaver
sudo docker stats cloudbeaver
```

#### Docker

```shell
sudo systemctl start docker
sudo systemctl restart docker
sudo systemctl stop docker
sudo systemctl status docker
```

#### Docker-compose 服务

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

1. 通过 SFTP 将网站目录（*/data/apps/cloudbeaver/*）**压缩后**再完整的下载到本地

2. 备份工作完成


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

### CloudBeaver 升级

CloudBeaver 基于 Docker 部署，其升级流程：拉取镜像 > 删除容器 > 重建容器

> 升级之前请确保您已经完成了服务器的镜像（快照）备份

1. 登录服务器，编辑 */data/apps/cloudbeaver/.env* 文件，将版本变量的值修改为目标版本号

2. 拉取目标版本的镜像
   ```
   cd /data/apps/cloudbeaver
   docker-compose pull
   ```
   > 如果显示没有镜像可拉取，则无需升级

3. 删除旧容器，重新创建 CloudBeaver 容器
    ```
    docker-compose down -v
    docker-compose up -d
    ```


## 故障处理

此处收集使用 CloudBeaver 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### CloudBeaver 容器无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
sudo docker logs cloudbeaver
sudo docker stats cloudbeaver
```

## 常见问题

#### CloudBeaver 是否支持多语言？

支持（包含中文）后台直接切换语言，但目前中文语言包不完整

#### CloudBeaver 支持哪些数据库？

默认支持 

#### 本项目中 CloudBeaver 采用何种安装方式？

Docker

#### CloudBeaver 采用何种驱动连接数据库？

JDBC 驱动


#### 是否可以通过命令行修改CloudBeaver后台密码？

不可以，只支持控制台修改

#### CloudBeaver 是否支持创建数据库？

暂未发现此功能

#### 如果没有域名是否可以部署 CloudBeaver？

可以，访问`http://服务器公网IP` 即可

#### 如何更改 CloudBeaver 的默认访问方式？

修改 [Nginx虚拟机主机文件](/zh/stack-components.md#nginx)，将其中的 **server_name** 项 `listen 80` 修改成类似 `listen 8090` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：*http://服务器公网IP:9090*

#### 如何禁止外界访问phpMyAdmin？

连接服务器，编辑 [phpMyAdmin 配置文件](/zh/stack-components.md#phpmyadmin)，将其中的 `Require all granted` 更改为 `Require ip 192.160.1.0`，然后重启 Apache 服务

#### 是否可以修改CloudBeaver的源码路径？

不可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R nginx.nginx /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```

