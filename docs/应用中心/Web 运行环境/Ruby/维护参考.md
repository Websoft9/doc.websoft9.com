---
sidebar_position: 2
slug: /ruby/admin
tags:
  - Ruby
  - 运行环境
---


# 维护参考

## 系统参数

Ruby 预装包包含 Ruby 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### Ruby

本环境采用 [RVM](https://rvm.io/)预装了 Ruby 以及所需的其他软件包：[gem](https://rubygems.org/), rake, bundler 等。  

Ruby 安装目录： */usr/local/rvm/rubies/ruby-version*  
Ruby 命令命令： */usr/local/rvm/rubies/ruby-2.4.10/bin*  
RVM 安装目录： */usr/local/rvm*  
Ruby 网站目录： */data/wwwroot*  

> version 为版本号，例如：2.4.10。gem, bundler 等工具与版本强相关

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*  
Nginx 验证访问文件：*/etc/nginx/.htpasswd/htpasswd.conf*  

#### MySQL

MySQL 安装路径: */usr/local/mysql*  
MySQL 数据文件 */data/mysql*  
MySQL 配置文件: */etc/my.cnf*  

MySQL 可视化管理参考 [MySQL 管理](/zh/admin-mysql.md) 章节。

#### phpMyAdmin

phpMyAdmin 是一款可视化 MySQL 管理工具，在本项目中它基于 Docker 安装。  

phpMyAdmin directory：*/data/apps/phpmyadmin*  
phpMyAdmin docker compose file：*/data/apps/phpmyadmin/docker-compose.yml* 

#### MongoDB

MongoDB 数据目录: */var/lib/mongodb*  
MongoDB 配置文件: */etc/mongod.conf*  
MongoDB 日志文件: */var/log/mongodb*  

#### adminMongo

adminMongo 是一款可视化 MongoDB 管理工具，采用 Docker 安装

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*  

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
| TCP | 80 | 通过 HTTP 访问 Rails 演示页面 | 可选 |
| TCP | 3306 | MySQL 远程端口 | 可选 |
| TCP | 27017 | MongoDB 远程端口 | 可选 |
| TCP | 9090 | phpMyAdmin 访问端口| 可选 |
| TCP | 9091 | AdminMongo 访问端口| 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Nginx  Version
nginx -V

# Apache version
apache -v

# Docker Version
docker -v

# MySQL version
mysql -V

# MongoDB version
mongodb -V

# Ruby version
ruby -v
bundler -v
gem -v
rails -v
```

### 服务

使用由Websoft9提供的 Ruby 部署方案，可能需要用到的服务如下：

#### Rails

```shell
sudo systemctl start rails
sudo systemctl stop rails
sudo systemctl restart rails
sudo systemctl status rails
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
sudo systemctl start mongo
sudo systemctl stop mongo
sudo systemctl restart mongo
sudo systemctl status mongo
```

#### Redis

```shell
systemctl start redis
systemctl stop redis
systemctl restart redis
systemctl status redis
```

#### phpMyAdmin

```shell
sudo docker start phpmyadmin
sudo docker stop phpmyadmin
sudo docker restart phpmyadmin
sudo docker stats pgadmin
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

1. 通过 SFTP 将网站目录（*/data/wwwroot/rails*）**压缩后**再完整的下载到本地

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

### Ruby 升级

> 升级之前请确保您已经完成了服务器的镜像（快照）备份

#### Patch 升级

Ruby 基于 RVM 部署，小版本的更新非常简单

```
rvm upgrade 1.9.2-p136 1.9.2-p180
rvm upgrade ree-2011.01 ree-2011-02
```

#### 版本升级

例如需将 Ruby 2.5 升级到 Ruby 2.6，只需一条命令

```
rvm install 2.6
```

## 故障处理

此处收集使用 Ruby 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### MySQL 服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
systemctl status mysql
```

#### 通过 Ansible 无法运行 `gem install bundler` 这样的程序？

原因：有待进一步研究  
方案：通过 bash -lc 运行 gem install 命令  

```
- name: Install version {{ruby_bundle_version}} of bundler
  shell: bash -lc "gem install bundler -v {{ ruby_bundle_version }} -N"
```

#### /urs/bin 目录下找不到 gem, ruby 等可执行文件或链接？

本项目通过 RVM 安装，通过 `source /etc/profile.d/rvm.sh` 实现 gem, ruby 等命令的全局化。

## 常见问题

#### Ruby 体系中 Gem, Bundler, Rake, Rails 是什么？

- RubyGems 是 Ruby 的包管理工具，类似 Python 中的 pip
- Gems 是 Ruby 通过 RubyGems 安装的包，为例避免误解，建议用“包”这个名字替代
- Bundler 是基于 Ruby 应用程序目录中的 Gemfile ，用于拉取依赖包的管理工具
- Gemfile 是 Ruby 依赖包清单文件
- Rake 是 Ruby 的构建程序，类似 Linux 中的 make
- Rails 是一个流行的 Ruby 应用程序开发框架

#### RVM 是什么？

RVM 是一个用于安装和管理多版本 Ruby 的命令行工具，虽然不是 Ruby 官方出品，但非常流行。

#### 什么是 Gemset？

Ruby RVM 允许我们为依赖项创建一个隔离的环境，这意味着 ruby，gems和irb都是独立的，与系统以及其他环境独立。如果你对 Python 非常熟悉，那么 RVM Gemset 就类似于 Python3 中的 VENV 或者 Python 2 中的 Virtualenv。RVM为每个Ruby版本和 gemset 提供了一个单独的 gem 目录。

#### Ruby 体系中有哪些常用的应用程序服务器？

WEBrick, passenger, Puma 等

#### Ruby 是否支持多版本？

Ruby 的多版本管理非常灵活。

* RVM 支持多个 Ruby 版本安装和切换（包括默认设置）
* 每个 Ruby 版本下，都可以通过 gem 安装同一个包的多个版本（参考 [Rails 多版本](/zh/solution-rails.md#多版本)）

#### Rails 如何才能被外网访问？

```text
rails s -b 0.0.0.0
```

#### 本项目中 Ruby 采用何种安装方式？

采用 rvm 安装，支持多版本

#### 推荐 Ruby 的学习资源？

[Awesome Ruby](https://github.com/chendelin1982/awesome-ruby)

#### 如果没有域名是否可以部署 Ruby 程序？

可以，访问`http://服务器公网IP:端口` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：*http://服务器公网IP:9090*

#### 是否可以修改Ruby的源码路径？

可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R ruby.ruby /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```
