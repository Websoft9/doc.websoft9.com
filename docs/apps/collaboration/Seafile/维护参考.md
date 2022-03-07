---
sidebar_position: 2
slug: /seafile/admin
tags:
  - Seafile
  - 网盘
  - 知识管理
  - 团队协作
---

# 维护参考

## 系统参数

Seafile 预装包包含 Seafile 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

本项目基于Docker安装，针对容器提供了持久化存储设置，保证数据不会随着容器的生命周期而丢失。通过运行`docker ps`，可以查看到 Seafile 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE                              COMMAND                  CREATED             STATUS              PORTS                                         NAMES
958e4cbc8dbe        seafileltd/seafile-mc:latest       "/sbin/my_init -- /s…"   14 hours ago        Up 9 minutes        0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp      seafile
80c266262079        phpmyadmin/phpmyadmin:latest       "/docker-entrypoint.…"   14 hours ago        Up 9 minutes        0.0.0.0:9090->80/tcp                          phpmyadmin
cea7ee7b8f2a        memcached:1.5.6                    "memcached -m 256"       14 hours ago        Up 9 minutes        11211/tcp                                     seafile-memcached
43881d791ed6        seafileltd/elasticsearch:5.6.16    "/docker-entrypoint.…"   14 hours ago        Up 9 minutes        3306/tcp                                      seafile-elasticsearch
a4498231bb29        onlyoffice/documentserver:latest   "/bin/sh -c /app/ds/…"   39 hours ago        Up 9 minutes        0.0.0.0:9002->80/tcp, 0.0.0.0:9003->443/tcp   onlyoffice-documentserver
```

### 路径

下面主要列出Docker有关的参数：

#### Seafile

本项目中的 Seafile 是由：seafile、seafile-memcached和seafile-elasticsearch(企业版专有)组成，它们均基于 Docker 安装，并完成了集成。 

##### Seafile

Seafile 存储目录： */data/wwwroot/seafile/seafile-data*  
Seafile docker-compose 文件路径： */data/wwwroot/seafile/docker-compose.yml*  
Seafile 日志目录： */data/wwwroot/seafile/seafile-data/logs*

seafile-memcached 存储目录： */data/wwwroot/seafile/seafile-data*  
seafile-memcached docker-compose 文件路径： */data/wwwroot/seafile/docker-compose.yml*  
seafile-memcached 日志目录： */data/wwwroot/seafile/seafile-data/logs*

seafile-elasticsearch 存储目录： */data/wwwroot/seafile/seafile-elasticsearch*  
seafile-elasticsearch docker-compose 文件路径： */data/wwwroot/seafile/docker-compose.yml*  
seafile-elasticsearch 日志目录： */data/wwwroot/seafile/seafile-data/logs*

> Seafile配置文件包括 seahub_settings.py, seafile.conf等

#### ONLYOFFICE Document Server

ONLYOFFICE Document Server存储目录： */data/apps/onlyofficedocumentserver*  
ONLYOFFICE docker-compose 文件路径： */data/apps/onlyofficedocumentserver/docker-compose.yml*  
ONLYOFFICE 日志目录： */data/apps/onlyofficedocumentserver/logs*

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

下面是您在使用本镜像过程中，需要用到的端口号，请通过 [云控制台安全组](https://support.websoft9.com/docs/faq/zh/tech-instance.html)进行设置

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过 http 访问 Seafile | 必须 |
| HTTPS | 443 | 通过 https 访问 Seafile | 可选 |
| HTTP | 9090 | 通过 http 访问 phpMyAdmin | 可选 |
| HTTP | 9002 | 通过 http 访问 OnlyOffice Document Server | 可选 |
| HTTPS | 9003 | 通过 https访问 OnlyOffice Document Server | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Python Version
python --version

# Docker Version
docker -v

# Docker image lists(includes version)
sudo docker images

# Docker Compose Version
docker-compose --version
```

### 服务

使用由Websoft9提供的Seafile部署方案，可能需要用到的服务如下：

> start 启动一个被停止的容器；restart 重启容器；stop 停止正在运行的容器

#### Seafile

```shell
#Seafile-主程序
sudo docker start seafile
sudo docker restart seafile
sudo docker stop seafile

#Seafile-memcached
sudo docker start seafile-memcached
sudo docker restart seafile-memcached
sudo docker stop seafile-memcached

#Seafile-MySQL
sudo docker start seafile-mysql
sudo docker restart seafile-mysql
sudo docker stop seafile-mysql
```

#### phpMyAdmin

```shell
sudo docker restart phpmyadmin
sudo docker stop phpmyadmin
sudo docker start phpmyadmin
sudo docker stats phpmyadmin
```

#### OnlyOffice DocumentServer

```shell
sudo docker restart onlyoffice-documentserver
sudo docker stop onlyoffice-documentserver
sudo docker start onlyoffice-documentserver
sudo docker stats onlyoffice-documentserver
```

#### Docker Compose

```shell
#创建容器
sudo docker-compose up
#创建容器并重建有变化的容器
sudo docker-compose up -d
```

#### Docker

```shell
sudo systemctl start docker
sudo systemctl restart docker
sudo systemctl stop docker
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

1. 通过 SFTP 将持久卷目录（*/data*）**压缩后**再完整的下载到本地
2. 使用 phpMyAdmin 导出 MySQL 数据库
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

### Seafile 升级

Seafile 升级大致流程：先拉取最新版本的 Seafile 镜像，然后重新运行容器。

> Seafile 升级之前请完成服务器的快照备份，以防不测。

1. 使用 SSH 登录 Seafile 服务器后，停止容器

   ```
   cd /data/wwwroot/seafile 
   docker-compose down -v
   ```

2. 拉取最新版本镜像
   ```
   docker image pull seafileltd/seafile-mc:latest
   ```

3. 重新运行 docker-compose 编排文件，启用新的容器
    ```
    docker-compose up -d
    ```
    
4. 登录 Seafile 后台查看升级后的版本
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-aboutversion-websoft9.png)

更多参考官方升级文档：[升级 Seafile 服务](https://cloud.seafile.com/published/seafile-manual-cn/docker/%E7%94%A8Docker%E9%83%A8%E7%BD%B2Seafile.md#user-content-%E5%8D%87%E7%BA%A7%20Seafile%20%E6%9C%8D%E5%8A%A1)


## 故障处理

此处收集使用 Seafile 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### Seafile 无法上传文件？

设置 Seafile 的主机地址（**必选项，否则无法使用文件上传功能**）

   - SERVICE_URL：*http://服务器公网IP*
   - FILE_SERVER_ROOT：*http://服务器公网IP/seafhttp*

   ![Seafile后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-seturl-websoft9.png)
   
   
#### 完成文档服务器配置，Seafile 仍然无法编辑和预览文件？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-canotaccess-websoft9.png)  

问题原因：SERVICE_URL 与实际不符  
解决方案：需登录控制台的系统设置，修改 SERVICE_URL 为实际值

#### 完成 ONLYOFFICE Docs 配置，Seafile 编辑和预览显示错误 “文档安全令牌未正确形成”？

问题原因：ONLYOFFICE docs 安全设置过高   
解决方案：需修改 ONLYOFFICE docs 编排文件中的环境变量 JWT_ENABLED，设置为 false  

```
  onlyoffice-document-server:
    container_name: onlyoffice-docs
    image: onlyoffice/documentserver:6.0.2
    stdin_open: true
    tty: true
    restart: always
    environment:
     - JWT_ENABLED=flase
```

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```

#### Seafile 无法打开？

查看启动日志，分析错误原因

```
docker logs seafile
```

## 常见问题

#### Seafile 支持多语言吗？

支持多种语言（中文，英文等）

#### 为什么要推荐使用企业版Seafile？

企业版用户拥有很多社区版没有的功能，如下：
![Seafile企业版社区版功能对比](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-compare-websoft9.png)

#### 为什么采用 Docker 方式部署 Seafile？

官方推荐

#### Seafile 是如何与MySQL 连接的？

容器内部连接，即容器编排

#### Seafile 默认能否对文档进行预览和编辑？

支持，如果不能预览，请参考[Office设置](/zh/solution-office.md)

#### 如果没有域名是否可以部署 Seafile？

可以，访问`http://服务器公网IP` 即可

#### 如何管理 MySQL/MariaDB 数据库？

参考本文档的 [MySQL 章节](/zh/admin-mysql.md)

#### 是否有可视化的数据库管理工具？

有，提供可视化的数据库管理工具 phpMyAdmin

#### 是否可以修改Seafile的数据路径？

可以，但需要对历史数据进行迁移

#### 部署和安装有什么区别？

部署是将一序列软件按照不同顺序，先后安装并配置到服务器的过程，是一个复杂的系统工程。  
安装是将单一的软件拷贝到服务器之后，启动安装向导完成初始化配置的过程。  
安装相对于部署来说更简单一些。 

#### 云平台是什么意思？

云平台指提供云计算服务的平台厂家，例如：Azure,AWS,阿里云,华为云,腾讯云等

#### 实例，云服务器，虚拟机，ECS，EC2，CVM，VM有什么区别？

没有区别，只是不同厂家所采用的专业术语，实际上都是云服务器