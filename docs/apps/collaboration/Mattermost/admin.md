---
sidebar_position: 2
slug: /mattermost/admin
tags:
  - Mattermost
  - 团队协作
  - 团队通讯
---

# 维护参考

## 系统参数

Mattermost 预装包包含 Mattermost 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

###  路径

####  Mattermost

Mattermost 安装目录： */opt/mattermost/*  
Mattermost 配置文件： */opt/mattermost/config/config.json*  
Mattermost 数据目录： */opt/mattermost/data*  
Mattermost 日志目录： */opt/mattermost/logs*

> Metabase 配置文件中包含数据库连接信息，更改了 MySQL 数据库账号密码，此处也需要对应修改

####  Go

Mattermost 使用 Go 语言开发，镜像默认支持 Go 程序部署

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx/*

#### MYSQL

MySQL 安装路径: */usr/local/mysql*  
MySQL 数据文件 */data/mysql*  
MySQL 配置文件: */etc/my.cnf*    
MySQL 可视化管理地址: *http://服务器公网IP:9090*，用户名和密码请见 [账号密码](/zh/stack-accounts.md) 章节。


###  端口号

下面是您在使用本镜像过程中，需要用到的端口号，请通过 [云控制台安全组](https://support.websoft9.com/docs/faq/zh/tech-instance.html)进行设置

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| MySQL | 3306 | 远程连接MySQL | 可选 |
| HTTP | 80 | 通过http访问Metabase | 必须 |
| HTTPS | 443 | 通过https访问Metabase | 可选 |
| phpMyAdmin on Docker | 9090 | 可视化管理MySQL | 可选 |

###  版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# mattermost version
cd /opt/mattermost/bin
./mattermost version

# Nginx version:
nginx -v

# MySQL version:
mysql -V

# Dokcer:
docker --version
```

### 服务

使用由Websoft9提供的Mattermost部署方案，可能需要用到的服务如下：

#### Mattermost

```shell
sudo systemctl start mattermost
sudo systemctl stop mattermost
sudo systemctl restart mattermost
sudo systemctl status mattermost
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

1. 通过WinSCP将网站目录（*/opt/mattermost*）**压缩后**再完整的下载到本地
2. 通过phpMyAdmin导出Mattermost数据库
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

### Mattermost升级

参考[官方升级文档](https://docs.mattermost.com/administration/upgrade.html)

## 故障处理

我们收集使用Metabase过程中最常见的故障，供您参考：

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查
```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```
## 常见问题

#### Mattermost 与 Slack 有什么区别？

参考官方文档 [Mattermost vs Slack](https://mattermost.com/mattermost-vs-slack/)

#### Mattermost Server, [Mattermost Team Edition](https://docs.mattermost.com/developer/manifesto.html?highlight=mattermost%20team%20edition) 和 Matttermost Enterprise Edition 有什么区别？

Mattermost Server 是它的产品的服务器端（后端）  
Mattermost Team Edition 是它的开源版本    
Matttermost Enterprise Edition 是它的企业版本  

目前官方提供了一致性的软件包下载，安装后默认就是 Enterprise Edition 的程序，但用户界面只有开源版的功能，如果需要企业版的功能，需要通过导入企业版秘钥实现升级。

#### Mattermost提供客户端吗？

提供，[下载地址](https://mattermost.com/download/#mattermostApps)

#### Mattermost提供CLI工具吗？

提供，参考[官网CLI文档](https://docs.mattermost.com/administration/command-line-tools.html#using-the-cli)

#### Mattermost支持多语言吗？

支持多语言（包含中文），可以登录控制台，通过【SITE CONFIGURATION】>【Localization】设置语言 

#### Mattermost数据库连接配置信息在哪里？

数据库配置信息在Mattermost安装目录下的config/config.json中，[查阅安装目录路径](/zh/stack-components.md#mattermost)

#### 如果没有域名是否可以部署 Mattermost？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？
密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP:9090

#### 如何禁止phpMyAdmin访问？

关闭服务器安全组的9090端口即可禁止

#### 是否可以修改Mattermost的源码路径？

可以，通过修改 [Nginx 虚拟主机配置文件](/zh/stack-components.md)中相关参数

#### 如何修改上传的文件权限?

```shell
chown -R nginx.nginx /data/wwwroot
find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```
