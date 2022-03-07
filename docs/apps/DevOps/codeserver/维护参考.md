---
sidebar_position: 2
slug: /codeserver/admin
tags:
  - code-server
  - 在线编辑器
---

# 维护参考

## 系统参数

code-server 预装包包含 code-server 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### code-server

本部署方案中的 code-server 基于容器安装，实现开发环境与宿主机隔离。

code-server 安装目录： */data/wwwroot/codeserver*  
code-server 日志目录： */data/wwwroot/codeserver/volumes/config/data/logs*  
code-server 工作目录： */data/wwwroot/codeserver/volumes/config/workspace*  
code-server Extension 目录： */data/wwwroot/codeserver/volumes/config/extensions*  
code-server docker-compose 文件： */data/wwwroot/codeserver/docker-compose.yml*  

> code-server 安装目录下的 .env 文件包含端口、后台密码等变量

#### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   
Docker daemon.json 文件：默认没有创建，请到 */etc/docker* 目录下根据需要自行创建  


#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*

#### MySQL

MySQL 安装路径: */usr/local/mysql*  
MySQL 数据文件 */data/mysql*  
MySQL 配置文件: */etc/my.cnf*  

> MySQL 可视化管理参考本文档 [MySQL](/zh/admin-mysql.md) 章节。

#### phpMyAdmin

phpMyAdmin 是一款可视化 MySQL 管理工具，在本项目中它基于 Docker 安装。

phpMyAdmin 应用目录：*/data/apps/phpmyadmin*  
phpMyAdmin docker-compose 文件：*/data/apps/phpmyadmin/docker-compose.yml*  

#### MongoDB

MongoDB 数据目录: */var/lib/mongodb*  
MongoDB 配置文件: */etc/mongod.conf*  
MongoDB 日志文件: */var/log/mongodb*  

> MongoDB 可视化管理参考本文档 [MongoDB](/zh/admin-mongodb.md) 章节。

#### adminMongo

adminMongo 是一款可视化 MySQL 管理工具，在本项目中它基于 Docker 安装。

adminMongo 应用目录：*/data/apps/adminmongo*  
adminMongo docker compose file：*/data/apps/adminmongo/docker-compose.yml*  

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 类型 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 80 | 通过 HTTP 访问 code-server 控制台 | 必须 |
| TCP | 443 | 通过 HTTPS 访问 code-server 控制台 | 可选 |
| TCP | 9090 | 通过 HTTP 访问 phpMyAdmin | 可选 |
| TCP | 3306 | MySQL 端口 | 可选 |
| TCP | 9091 | 通过 HTTP 访问 adminMongo | 可选 |
| TCP | 27017 | MongoDB 端口 | 可选 |

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

# MySQL  Version
mysql -V

# MongoDB version
mongodb -V

# code-server version
docker inspect -f '{{ index .Config.Labels "build_version" }}' codeserver
```

### 服务

使用由 Websoft9 提供的 code-server 部署方案，可能需要用到的服务如下：

### code-server

```shell
sudo docker start codeserver
sudo docker stop codeserver
sudo docker restart codeserver
sudo docker stats codeserver

# you can run the CMD in the code-server container by this way
sudo docker exec -it codeserver bash
```

#### phpMyAdmin

```shell
sudo docker start phpmyadmin
sudo docker stop phpmyadmin
sudo docker restart phpmyadmin
sudo docker stats phpmyadmin
```

#### adminMongo

```shell
sudo docker start adminmongo
sudo docker stop adminmongo
sudo docker restart adminmongo
sudo docker stats adminmongo
```

#### Docker

```shell
sudo systemctl start docker
sudo systemctl stop docker
sudo systemctl restart docker
sudo systemctl status docker
```

#### Nginx

```shell
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
```

#### MySQL

```shell
sudo systemctl start mysql
sudo systemctl stop mysql
sudo systemctl restart mysql
sudo systemctl status mysql
```

#### MongoDB

```shell
sudo systemctl start mongod
sudo systemctl restart mongod
sudo systemctl stop mongodd
sudo systemctl status mongod
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

1. 通过 SFTP 将网站目录（*/data/wwwroot/codeserver*）**压缩后**再完整的下载到本地
2. 通过 phpMyAdmin 逐个导出数据库
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

### code-server 升级

code-server 基于 Docker 部署，其升级流程：拉取镜像 > 删除容器 > 重建容器

> 升级之前请确保您已经完成了服务器的镜像（快照）备份

1. 登录服务器，编辑 */data/wwwroot/codeserver/.env* 文件，将版本变量的值修改为目标版本号

2. 拉取目标版本的镜像
   ```
   cd /data/wwwroot/codeserver
   docker-compose pull
   ```
   > 如果显示没有镜像可拉取，则无需升级

3. 删除旧容器，重新创建 code-server 容器
    ```
    docker-compose down -v
    docker-compose up -d
    ```

## 故障处理

此处收集使用 code-server 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### code-server服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看 code-server 容器运行日志
sudo docker log codeserver

# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```

#### code-server 在线创建文件权限不足？

如果上传的文件存在一些文件权限需要修正。运行如下命令即可解决文件权限问题：
```
chown -R docker.docker /data/wwwroot/codeserver/volumes/config/workspace
```

## 常见问题

#### code-server 是 Microsoft 开发的吗？

不是，它是由一家名为[CODER](https://coder.com/)的公司开发的

#### code-server 支持多账号吗？

不支持，但我们在本部署包中提供了[多开发者方案](/zh/solution-more.md#多开发者)

#### code-server 支持扩展安装吗？

支持

#### 如何退出 code-server 界面？

打开控制台左上角菜单，点击【Log out】即可退出

#### 是否可以通过命令行修改 code-server 后台密码？

不支持

#### 如果没有域名是否可以部署 code-server？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

内置 phpMyAdmin，访问地址：*http://服务器公网IP:9090*
内置 adminMongo*http://服务器公网IP:9091*

#### 如何禁止外界访问 phpMyAdmin 和 adminMongo？

可以关闭安全组 9090 和 9091 端口，也可以通过下面的命令停止服务

```
sudo docker stop phpmyadmin
sudo docker stop adminmongo
```

#### 是否可以修改code-server的源码路径？

可以，通过修改 [docker-compose 文件](/zh/stack-components.md#code-server)实现

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R docker.docker /data/wwwroot/codeserver
# 读写执行权限
find /data/wwwroot/codeserver -type d -exec chmod 750 {} \;
find /data/wwwroot/codeserver -type f -exec chmod 640 {} \;
```

