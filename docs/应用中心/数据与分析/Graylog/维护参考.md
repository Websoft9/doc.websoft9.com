---
sidebar_position: 2
slug: /graylog/admin
tags:
  - Graylog
  - 日志管理
  - 数据分析
---

# 维护参考

## 系统参数

Graylog 预装包包含 Graylog 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

本部署方案中的 Graylog 采用 Docker 部署，运行 `docker ps` 查看运行的容器。  

```
CONTAINER ID   IMAGE                                                      COMMAND                  CREATED         STATUS                   PORTS                                                                                                                                                                                                                           NAMES
dffc0d802a26   graylog/graylog:4.1                                        "/usr/bin/tini -- wa…"   2 minutes ago   Up 2 minutes (healthy)   0.0.0.0:1514->1514/tcp, 0.0.0.0:1514->1514/udp, :::1514->1514/tcp, :::1514->1514/udp, 0.0.0.0:12201->12201/tcp, 0.0.0.0:12201->12201/udp, :::12201->12201/tcp, :::12201->12201/udp, 0.0.0.0:9001->9000/tcp, :::9001->9000/tcp   graylog
7c0a42a383c3   mongo:4.2                                                  "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes             27017/tcp                                                                                                                                                                                                                       graylog-mongo
f4cd00fc5f58   docker.elastic.co/elasticsearch/elasticsearch-oss:7.10.2   "/tini -- /usr/local…"   2 minutes ago   Up 2 minutes             9200/tcp, 9300/tcp                                                                                                                                                                                                              graylog-elasticsearch
9497147a0263   mrvautin/adminmongo                                        "docker-entrypoint.s…"   8 minutes ago   Up 3 minutes             0.0.0.0:9091->1234/tcp, :::9091->1234/tcp                                                                                                                                                                                       adminmongo
```

#### Graylog

Graylog 安装路径: */data/wwwroot/graylog*  
Graylog 配置文件: */data/wwwroot/volumes/graylog/config/server.conf*  
Graylog 日志目录: */data/wwwroot/volumes/graylog/log*  

#### MongoDB

MongoDB 配置文件: */data/db/mongo*  
MongoDB 数据目录: */data/db/mongo/db*  

#### Elasticsearch

Elasticsearch 数据目录: */data/db/elasticsearch*  

#### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   
Docker daemon.json 文件：默认没有创建，请到 */etc/docker* 目录下根据需要自行创建   

#### Nginx

Nginx 虚拟主机配置文件: */etc/nginx/conf.d/default.conf*    
Nginx 主配置文件: */etc/nginx/nginx.conf*   
Nginx 日志文件: */var/log/nginx*  
Nginx 伪静态配置目录: */etc/nginx/conf.d/rewrite* 

#### AdminMongo

AdminMongo是一款可视化 MongoDB 管理工具，在本项目中它基于 Docker 安装。

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 80 | HTTP requests for Graylog Console| 必要 |
| TCP | 443 | HTTPS requests for Graylog Console | 可选 |
| TCP | 27017 | MongoDB | 可选 |
| TCP | 9001 | Graylog 端口 | 可选 |
| TCP | 9091 | HTTP 访问 AdminMongo | 可选 |
| TCP | 9200, 9300 | ElasticSearch 端口 | 可选 |

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

# Graylog Version
docker images |grep graylog/graylog |awk '{print $2}'

# Elasticsearch version
docker exec -it graylog-elasticsearch curl -XGET localhost:9200

# Mongo version
docker exec -it graylog-mongo mongo --version
```

### 服务

使用由Websoft9提供的 Graylog 部署方案，可能需要用到的服务如下：

#### Graylog

```shell
sudo docker start graylog
sudo docker stop graylog
sudo docker restart graylog
sudo docker status graylog
```

#### Nginx

```shell
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
```

#### MongoDB

```shell
sudo docker start graylog-mongo
sudo docker stop graylog-mongo
sudo docker restart graylog-mongo
sudo docker status graylog-mongo
```

#### Elasticsearch

```shell
sudo docker start graylog-elasticsearch
sudo docker stop graylog-elasticsearch
sudo docker restart graylog-elasticsearch
sudo docker status graylog-elasticsearch
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

1. 通过 SFTP 将 Graylog 配置文件（*/data/wwwroot/graylog*）**压缩后**再完整的下载到本地
2. 通过 AdminMongo 逐个导出数据库
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

### Graylog 升级

Graylog 基于 Docker 部署，其升级流程：拉取镜像 > 删除容器 > 重建容器

> 升级之前请确保您已经完成了服务器的镜像（快照）备份

1. 登录服务器，编辑 */data/wwwroot/graylog/.env* 文件，将版本变量的值修改为目标版本号

2. 拉取目标版本的镜像
   ```
   cd /data/wwwroot/graylog
   docker-compose pull
   ```
   > 如果显示没有镜像可拉取，则无需升级

3. 删除旧容器，重新创建 Graylog 容器
    ```
    docker-compose down
    docker-compose up -d

## 故障处理

此处收集使用 Graylog 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### Graylog服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
sudo docker logs graylog
sudo docker stats graylog
```

#### 提示 There is a node without any running inputs. This means ... ？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-nofiinput-websoft9.png)

**原因**：这只是一个当前没有 input 的提醒，并非错误。  
**方案**：新建一个本地的 input，即可消除此提醒

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-createinput-websoft9.png)


#### Index rotation strategy null not found... ?

磁盘可用空间低于 15% 的时候，会出现这个问题

## 常见问题

#### Graylog 系统架构示意图？
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-arch-websoft9.png)


#### Graylog 的集群架构示意图？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/architec_bigger_setup.png)

#### 如何访问 Graylog API?

访问的URL为：*https://Internet IP:9001/api/api-browser/global/index.html*。缺少 /global/index.html 是无法访问的

#### 如果没有域名是否可以部署 Graylog？

可以，直接端口访问即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置 AdminMongo，访问地址：*http://服务器公网IP:9091*

#### 是否可以修改 Graylog 的源码路径？

可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R graylog.graylog /data/wwwroot/graylog
# 读写执行权限
find /data/wwwroot/graylog -type d -exec chmod 750 {} \;
find /data/wwwroot/graylog -type f -exec chmod 640 {} \;
```