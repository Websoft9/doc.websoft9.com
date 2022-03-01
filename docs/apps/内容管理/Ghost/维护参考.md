---
sidebar_position: 2
slug: /ghost/admin
tags:
  - Ghost
  - CMS
  - 建站系统
  - 博客系统
---

# 维护参考

## 系统参数

Ghost 预装包包含 Ghost 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### Ghost

Ghost 安装目录： */data/wwwroot/ghost/content*  
Ghost 配置文件： */data/wwwroot/ghost/config.production.json*  
Ghost 容器编排文件： */data/wwwroot/ghost/docker-compose.yml*  

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*

#### MySQL

MySQL 安装路径: */usr/local/mysql*  
MySQL 数据文件 */data/mysql*  
MySQL 配置文件: */etc/my.cnf*  

#### phpMyAdmin

采用容器的方式运行 phpMyAdmin， 环境与 Ghost 容器隔离，稳定可靠。  

访问方式： *http://服务器公网IP：9090*


#### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   
Docker daemon.json 文件：默认没有创建，请到 */etc/docker* 目录下根据需要自行创建   


### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过 HTTP 访问 Ghost | 可选 |
| HTTP | 443 | 通过 HTTPS 访问 Ghost | 可选 |
| TCP | 9090 | 数据库可视化管理工具 phpMyAdmin | 可选 |
| TCP | 3306 | 本地数据库客户端访问数据库 | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Nginx  Version
nginx -V

# Node version
node -v

# Docker Version
docker -v

# MySQL  Version
mysql -V

# Node  Version
sudo docker exec -it ghost /bin/bash -c 'node -v'

# Ghost version
sudo docker exec -it ghost /bin/bash -c 'ls versions'
```

### 服务

使用由Websoft9提供的 Ghost 部署方案，可能需要用到的服务如下：

#### Ghost

```shell
sudo docker stop ghost
sudo docker start ghost
sudo docker restart ghost

# you can use the following CMD to manage Ghost container
sudo docker exec -it ghost /bin/bash
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

#### phpMyAdmin

```shell
sudo docker stop phpmyadmin
sudo docker start phpmyadmin
sudo docker restart phpmyadmin
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

1. 通过 SFTP 将网站目录（*/data/wwwroot/ghost*）**压缩后**再完整的下载到本地

2. 登录 Ghost 后台，导出数据
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/ghost/ghost-exportalldatas-websoft9.png)

3. 通过 phpMyAdmin 逐个导出数据库
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)

4. 将程序文件和数据库文件放到同一个文件夹，根据日期命名

5. 备份工作完成


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


### Ghost升级

不部署采用 Docker 安装 Ghost，官方提供的通过 Node.js 升级 Ghost 不适用。

请按照下面的流程完成升级：

1. 手工[备份 Ghost](/zh/solution-backup.md#程序手工备份)，一定要确保万无一失
2. 登录云服务器，分别运行下面的命令
   ```
   #停止并删除现有的 Ghost 容器
   sudo docker stop ghost && sudo docker rm ghost

   #删除本地 Ghost 镜像
   docker image rm ghost

   #重新运行容器
   cd /data/wwwroot/ghost && docker-compose up -d
   ```
3. 本地浏览器重新访问 Ghost，开始升级


## 故障处理

此处收集使用 Ghost 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### Ghost服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
sudo docker ps
sudo docker logs ghost
```

#### 无法打开默认主题 casper 文件夹？

官方表示，casper 是内核的组成部分，仅自上传的主题方可修改。

## 常见问题

### Ghost 支持中文吗？

Ghost 的后台不支持中文，但是前台支持中文（需主题中有中文）

#### Ghost 系统中的 Post 与 Page 有什么区别？

Post 是文章的意思，每一篇博客文章即一个 Post；Page 是页面的意思，网站中的首页，公司介绍等都可称之为 Page。  

在 Ghost 系统中，每一个新建的 Page，都需要在主题中有对应的模板文件与之匹配。

#### Ghost 有哪些用户角色？

参考官方文档 [Managing your team in Ghost](https://ghost.org/help/managing-your-team/)

#### Ghost 是否支持对默认主题 casper 进行修改？

不支持，只可以修改自上传的主题。

#### 是否可以通过命令行修改Ghost后台密码？

不可以

#### 如果没有域名是否可以部署 Ghost？

可以，访问`http://服务器公网IP` 即可

#### 设置域名访问？

首先要解析域名，然后登录服务完成[域名绑定操作](/zh/solution-more.md#域名绑定)

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：*http://服务器公网IP:9090*

#### 如何禁止外界访问phpMyAdmin？

云控制台安全组中关闭 9090 端口即可

#### 是否可以修改Ghost目录路径？

可以，通过修改 Ghost 容器编排文件： */data/wwwroot/ghost/docker-compose.yml* 中的持久化目录实现

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R root.root /data/wwwroot/ghost
# 读写执行权限
find /data/wwwroot/ghost -type d -exec chmod 750 {} \;
find /data/wwwroot/ghost -type f -exec chmod 640 {} \;
```