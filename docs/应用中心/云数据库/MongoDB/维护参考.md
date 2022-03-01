---
sidebar_position: 2
slug: /mongodb/admin
tags:
  - MongoDB
  - Cloud Native Database
---

# 维护参考

## 系统参数

MongoDB 预装包包含 MongoDB 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### MongoDB

MongoDB 数据目录: */var/lib/mongodb*  
MongoDB 配置文件: */etc/mongod.conf*  
MongoDB 日志文件: */var/log/mongodb*  

#### adminMongo on Docker

adminMongo 是一款可视化 MongoDB 管理工具，采用 Docker 安装

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*  

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

本应用建议开启的端口如下：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| adminMongo on Docker | 9091 | 通过 HTTP 访问 adminMongo | 可选 |
| MongoDB Server | 27017 | 远程连接 MongoDB | 可选 |


### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# MongoDB version
mongodb -V

# Docker Version
docker -v
```


### 服务

使用由 Websoft9 提供的 MongoDB 部署方案，可能需要用到的服务如下：

#### MongoDB
```shell
sudo systemctl start mongod
sudo systemctl restart mongod
sudo systemctl stop mongodd
sudo systemctl status mongod
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

### MongoDB 应用备份

MongoDB上的应用备份主要通过**下载Volume**实现最小化的备份方案。

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

1. 使用`mongodump`工具，导致数据库
   ```
   #1 备份
   mongodump --authenticationDatabase admin --username root --password PASSWORD -d DATABASE_NAME -h localhost

   # 查看备份
   cd dump/admin
   ls
   ```
2. 使用`mongorestore`工具，恢复数据库
   ```
   mongorestore --authenticationDatabase admin --username root --password PASSWORD PATH_TO_BACKUP_FILE

   ```

详情参考官方文档：[MongoDB Backup Methods](https://docs.mongodb.com/manual/core/backups/)

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

### MongoDB 更新升级

请参考官方文档：[Upgrade to the Latest Revision of MongoDB](https://docs.mongodb.com/manual/tutorial/upgrade-revision/)


## 故障处理

此处收集使用 MongoDB 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 使用 /credentials/password.txt 中的账号密码无法登录？

可能密码修改没有成功，请使用[重置密码](/zh/solution-more.md#重置密码)

#### MongoDB数据库服务无法启动？

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看数据库状态以日志
systemctl status mongod
journalctl  -u mongod.service
```
## 常见问题

#### 本地 MongoDB compass 无法连接数据库？

检查27017端口，bindIP和账户认证等连接字段是否满足条件

#### 什么是 MongoDB 的 Client 和 Server？

MongoDB Server 是指 MongoDB 程序本体，而 MongoDB Client 指采用TCP协议用于连接程序本地的客户端。它们是两个完全不同的程序，也就是说它们并需要同时安装到同一台服务上。

#### mongod 和 mongo 命令有什么区别？

mongod 是 MongoDB 的服务端管理命令，用于启动数据库服务  
mongo 是用于访问 MongoDB 服务的客户端  

#### MongoDB Community vs MongoDB Enterprise？

MongoDB Community is the source available and free to use edition of MongoDB.  
MongoDB Enterprise is available as part of the MongoDB Enterprise Advanced subscription and includes comprehensive support for your MongoDB deployment.   MongoDB Enterprise also adds enterprise-focused features such as LDAP and Kerberos support, on-disk encryption, and auditing.  

#### 是否可以不进行身份验证就直接访问 MongoDB？

可以，默认安装时 MongoDB 没有开启访问控制，无需MongoDB 用户名密码就可以访问，例如通过此URL访问：mongodb://localhost/admin。
 > MongoDB [访问控制参考](https://docs.mongodb.com/manual/tutorial/enable-authentication/)

#### MongoDB 中的 admin 数据库是什么？

安装 MongoDB 时会默认包含一个 admin 数据库，如果你创建管理员账户就必须存储到这个admin中

#### 是否可以修改 MongoDB 数据目录？

可以，通过修改 /etc/mongod.conf 配置文件

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置 [adminMongo](/zh/solution-gui.md#adminmongo)

#### MongoDB 提供哪些安全认证？

MongoDB provides various features, such as authentication, access control, encryption, to secure your MongoDB deployments. Some key security features include:

| Authentication | Authorization | TLS/SSL | Enterprise Only |
| :--- | :--- | :--- | :--- |
| [Authentication](https://docs.mongodb.com/manual/core/authentication/)<br />[SCRAM](https://docs.mongodb.com/manual/core/security-scram/)<br />[x.509](https://docs.mongodb.com/manual/core/security-x.509/) | [Role-Based Access Control](https://docs.mongodb.com/manual/core/authorization/)<br />[Enable Auth](https://docs.mongodb.com/manual/tutorial/enable-authentication/)<br />[Manage Users and Roles](https://docs.mongodb.com/manual/tutorial/manage-users-and-roles/) | [TLS/SSL (Transport Encryption)](https://docs.mongodb.com/manual/core/security-transport-encryption/)<br />[Configure mongod and mongos for TLS/SSL](https://docs.mongodb.com/manual/tutorial/configure-ssl/)<br />[TLS/SSL Configuration for Clients](https://docs.mongodb.com/manual/tutorial/configure-ssl-clients/) | [Kerberos Authentication](https://docs.mongodb.com/manual/core/kerberos/)<br />[LDAP Proxy Authentication](https://docs.mongodb.com/manual/core/security-ldap/)<br />[Encryption at Rest](https://docs.mongodb.com/manual/core/security-encryption-at-rest/)<br />[Auditing](https://docs.mongodb.com/manual/core/auditing/) |

> MongoDB also provides the [Security Checklist](https://docs.mongodb.com/manual/administration/security-checklist/) for a list of recommended actions to protect a MongoDB deployment.

#### MongoDB 支持哪些平台？

所支持的平台[参考](https://docs.mongodb.com/manual/administration/production-notes/#prod-notes-supported-platforms)
