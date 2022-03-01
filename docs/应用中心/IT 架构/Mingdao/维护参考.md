---
sidebar_position: 2
slug: /mingdao/admin
tags:
  - 明道云
  - IT 架构
  - 无代码平台
---

# 维护参考

## 系统参数

明道云 预装包包含 明道云 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

本部署方案中的 明道云 采用 Docker 部署，运行 `docker ps` 查看运行的容器。
```
CONTAINER ID   IMAGE                                                                   COMMAND                  CREATED       STATUS       PORTS                       NAMES
1100b00c55ec   registry.cn-hangzhou.aliyuncs.com/mdpublic/mingdaoyun-community:2.4.1   "/Housekeeper/main -…"   2 hours ago   Up 2 hours   0.0.0.0:8880->8880/tcp      script_app_1
d6fa950fb107   registry.cn-hangzhou.aliyuncs.com/mdpublic/mingdaoyun-doc:1.2.0         "/bin/sh -c /app/ds/…"   2 hours ago   Up 2 hours   80/tcp, 443/tcp, 8000/tcp   script_doc_1
```

#### 明道云

明道云目录： */data/wwwroot/mingdao*  
明道云安装管理器目录： */data/wwwroot/mingdao/installer*  
明道云持久化目录： */data/wwwroot/mingdao/volume*  

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

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 38881 | HTTP 访问 明道云初始化页面 | 可选 |
| TCP | 8880 | HTTP 访问 明道云后台（初始化完成后） | 可选 |
| TCP | 80 | Nginx HTTP | 可选 |
| TCP | 443 |  Nginx HTTPS| 可选 |

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

# 明道云 version
docker images
```

### 服务

使用由 Websoft9 提供的 明道云 部署方案，可能需要用到的服务如下：

#### 明道云

```shell
sudo systemctl start mingdao
sudo systemctl stop mingdao
sudo systemctl restart mingdao
sudo systemctl status mingdao
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

1. 通过 SFTP 将网站目录（*/data/mingdao/script/volume/data/*）**压缩后**再完整的下载到本地
   ```
   tar -zcvf /backup/mdybak20210320.tar.gz /data/mingdao/script/volume/data/。
   ```
2. 备份工作完成

### 在线备份与还原

系统超级管理员可通过右上角头像下拉列表进入【系统配置】，然后在【更多设置】通过访问 安装管理器，在 数据管理 功能中完成数据的在线备份或还原。

![](https://docs.pd.mingdao.com/images/docker-compose-standalone-data/193337_9b63776a_7544271.png)

详细参考[官方备份与还原文档](https://docs.pd.mingdao.com/deployment/docker-compose/standalone/data.html)


## 恢复

### 在线备份与还原

系统超级管理员可通过右上角头像下拉列表进入【系统配置】，然后在【更多设置】通过访问 安装管理器，在 数据管理 功能中完成数据的在线备份或还原。

![](https://docs.pd.mingdao.com/images/docker-compose-standalone-data/193337_9b63776a_7544271.png)

详细参考[官方备份与还原文档](https://docs.pd.mingdao.com/deployment/docker-compose/standalone/data.html)

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

### 明道云 升级

明道云官方提供了方便的升级方案（[详情](https://docs.pd.mingdao.com/deployment/docker-compose/standalone/upgrade.html)）

> 升级之前请确保您已经完成了服务器的镜像（快照）备份

## 故障处理

此处收集使用 明道云 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

```
cat /data/mingdao/script/mingdaoyun.log
docker logs $(docker ps | grep mingdaoyun-community | awk '{print $1}')
```

更多与日志香港的操作[参考](https://docs.pd.mingdao.com/deployment/docker-compose/command.html#日志)

#### 明道云服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
systemctl status mingdao
journalctl -u mingdao
```

#### 服务器重启后，程序打不开？

服务器重启后，明道云容器没有启动，使用下面的命令，启动服务，稍等片刻即可打开

```
cd /data/wwwroot/mingdao/installer/
 ./service.sh restartall

```

## 常见问题

#### 明道云 是否支持多语言？

支持中文和英文

#### 明道云有哪些版本？

明道云为不同的用户提供了多种版本，主要包括：

* [SaaS 版本](https://www.mingdao.com/price)，其中又分为：免费版、标准版、专业版、旗舰版四种
* [私有部署版](https://www.mingdao.com/pd)，其中又分为：社区版（免费）、标准版、专业版三种

本部署方案中提供的就是 **私有部署版** 中的免费版本

#### 本项目中 明道云 采用何种安装方式？

采用 Docker 部署

#### Websoft9 与明道云是什么关系？

Websoft9 是明道云的全球战略合作伙伴，主要在全球的主流云平台发布 **明道云私有部署版（免费）** 

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/shouquanshu.jpg)

#### 是否可以通过命令行重置明道云后台密码？

暂无方案

#### 如果没有域名是否可以部署 明道云？

可以，访问`http://服务器公网IP:8880` 即可

#### 是否可以修改明道云的目录？

不可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R nginx.nginx /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```
