---
sidebar_position: 2
slug: /elk/admin
tags:
  - ELK Stack
  - 日志管理
  - 数据分析
---

# 维护参考

## 系统参数

ELK 预装包包含 ELK 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

本部署方案中的 ELK 采用 Docker 部署，运行 `docker ps` 查看运行的容器。
```
CONTAINER ID   IMAGE                  COMMAND                  CREATED         STATUS         PORTS                                                                                                                                                                        NAMES
4c27ee6b8e98   logstash:7.13.4        "/usr/local/bin/dock…"   4 minutes ago   Up 4 minutes   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp, 0.0.0.0:5044->5044/tcp, :::5044->5044/tcp, 0.0.0.0:9600->9600/tcp, 0.0.0.0:5000->5000/udp, :::9600->9600/tcp, :::5000->5000/udp   elk-logstash
babdf8193e8d   kibana:7.13.4          "/bin/tini -- /usr/l…"   4 minutes ago   Up 4 minutes   0.0.0.0:9001->5601/tcp, :::9001->5601/tcp                                                                                                                                    elk-kibana
de14eb80b9f9   elasticsearch:7.13.4   "/bin/tini -- /usr/l…"   4 minutes ago   Up 4 minutes   0.0.0.0:9200->9200/tcp, :::9200->9200/tcp, 0.0.0.0:9300->9300/tcp, :::9300->9300/tcp                                                                                         elk-elasticsearch
```

#### ELK

ELK Stack 包含：Elasticsearch, Kibana, Logstash 等组件

ELK 安装目录： */data/wwwroot/elk*  
ELK 配置目录： */data/wwwroot/elk/src*  
ELK 配置容器配置文件： */data/wwwroot/elk/.env*  

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

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 类型 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| Kibana | 9001 | 通过 HTTP 访问 Kibana 控制台 | 可选 |
| Elasticsearch | 9200 | Elasticsearch HTTP | 可选 |
| Elasticsearch | 9300 | Elasticsearch TCP | 可选 |
| Logstash | 9600 | Logstash API | 可选 |
| Logstash | 5000 | Logstash TCP | 可选 |
| Logstash | 5044 | Logstash TCP | 可选 |

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

# ELK version
docker exec -it elk-elasticsearch bin/elasticsearch --version
```

### 服务

使用由Websoft9提供的 ELK 部署方案，可能需要用到的服务如下：

#### ELK

```shell
sudo systemctl start elk-elasticsearch | elk-logstash | elk-kibana
sudo systemctl stop elk-elasticsearch | elk-logstash | elk-kibana
sudo systemctl restart elk-elasticsearch | elk-logstash | elk-kibana
sudo systemctl status elk-elasticsearch | elk-logstash | elk-kibana
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

1. 通过 SFTP 将网站目录（*/data/wwwroot/elk*）**压缩后**再完整的下载到本地
2. 将程序文件和数据库文件放到同一个文件夹，根据日期命名
3. 备份工作完成

### ELK 快照

ELK 内置快照备份功能（阅读[官方文档](https://www.elastic.co/guide/en/elasticsearch/reference/7.13/snapshot-restore.html)）

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-backupsp-websoft9.png)


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

### ELK 升级

ELK 基于 Docker 部署，其升级流程：拉取镜像 > 删除容器 > 重建容器

> 升级之前请确保您已经完成了服务器的镜像（快照）备份

1. 登录服务器，编辑 */data/wwwroot/elk/.env* 文件，将版本变量的值修改为目标版本号

2. 拉取目标版本的镜像
   ```
   cd /data/wwwroot/elk
   docker-compose pull
   ```
   > 如果显示没有镜像可拉取，则无需升级

3. 删除旧容器，重新创建 ELK 容器
    ```
    docker-compose down
    docker-compose up -d
    ```

## 故障处理

此处收集使用 ELK 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### ELK 服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
docker logs elk-elasticsearch | elk-logstash | elk-kibana
```

#### Logstash 无法输出到 Elasticsearch？

检查 Logstash 的 pipeline 配置文件中 Elasticsearch 账号密码是否正确

## 常见问题

#### ELK 是否支持多语言？

支持，只需在 Kibana 配置文件中增加 `i18n.locale: "zh-CN"` 即可

#### 本项目中 ELK 采用何种安装方式？

采用[官方提供 Docker 安装](https://github.com/elastic/dockerfiles)方式

#### ELK 采用哪种开源许可？

[ELASTIC-LICENSE](https://github.com/elastic/elasticsearch/blob/master/licenses/ELASTIC-LICENSE-2.0.txt)

#### Elasticsearch 全部免费吗？

Elasticsearch 由之前的开源版+商业扩展包 xpack 组成。其中 xpack 基本功能免费，需要使用全部功能可以向官方申请 30 天的免费试用期，试用期结束后回归到基本功能或订阅。  

#### 如果没有域名是否可以部署 ELK？

可以，访问`http://服务器公网IP` 即可

#### 是否可以修改ELK的源码路径？

可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R nginx.nginx /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```