---
sidebar_position: 2
slug: /onlyofficedocs/admin
---

# 维护参考

## 系统参数

本预装包包含 Nginx, ONLYOFFICE Document Server on Docker, Docker 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

> Nginx 用于接受用户访问请求，然后转发给 ONLYOFFICE Document Server on Docker。  

### 路径

#### Parse Server 

Parse Server  程序目录： */usr/lib/node_modules/parse-server*  
Parse Server  配置文件： */etc/parse-server/parse-server.json*  
Parse Server  日志目录： */var/log/parse-server*  

> Parse Server 配置文件中包含数据库连接信息，更改了 MongoDB 账号密码，此处也需要对应修改

#### Parse Dashboard

Parse Dashboard  程序目录： */usr/lib/node_modules/parse-server*  
Parse Dashboard  配置文件： */etc/parse-server/parse-server.json*  
Parse Dashboard  日志文件： *直接在 Parse Dashboard 面板中查看*  


#### Node.js

NPM 程序目录：*/usr/lib/node_modules/npm*  
NPM 模块全局安装路径：*/usr/lib/node_modules/npm/node_modules*  
Node 配置文件：*/usr/include/node/config.gypi*

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx/*

#### MongoDB

MongoDB 存储目录：*/data/mongo*   
MongoDB 配置文件：*/etc/mongod.conf*   
MongoDB 日志目录：*/var/log/mongodb/mongod.log*  
  
MongoDB 可视化管理地址: *http://服务器公网IP:9090*，用户名和密码请见 [账号密码](/zh/stack-accounts.md) 章节。

### 端口号

下面是您在使用本镜像过程中，需要用到的端口号，请通过 [云控制台安全组](https://support.websoft9.com/docs/faq/zh/tech-instance.html)进行设置

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过http访问Parse Server, Parse Dashboard | 必须 |
| HTTPS | 443 | 通过https访问Parse Server, Parse Dashboard   | 可选 |
| MongoDB | 27017 | 远程连接MongoDB | 可选 |
| adminMongo on Docker | 9091 | 可视化管理MongoDB | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Nginx Version
nginx -v

# Node.js Verison
node --version

# MongoDB Verison
mongo --version

# Dokcer:
docker --version
```

### 服务

使用由Websoft9提供的Parse Server 部署方案，可能需要用到的服务如下：

#### Parse Server 

```shell
sudo systemctl start parse-server
sudo systemctl stop parse-server
sudo systemctl restart parse-server
sudo systemctl status parse-server
```

#### Parse Dashboard

```shell
sudo systemctl start parse-dashboard
sudo systemctl stop parse-dashboard
sudo systemctl restart parse-dashboard
sudo systemctl status parse-dashboard
```

#### Nginx

```shell
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
```

#### MongoDB

```shell
sudo systemctl start mongod
sudo systemctl stop mongod
sudo systemctl restart mongod
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

1. 通过WinSCP将 **[网站目录](/zh/stack-components.md#parse-server)** 压缩后再完整的下载到本地
2. 通过 [adminMongo](/zh/admin-mongodb.md) 导出Parse Server 数据库
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

### Parse Server 升级

Parse Server 采用 NPM 来管理升级

```
npm update -g  parse-server
```

### Parse Dashboard 升级

Parse Dashboard 采用 NPM 来管理升级

```
npm update -g  parse-dashboard
```

## 故障处理


我们收集使用 Parse Server 过程中最常见的故障，供您参考：
> 服务器相关故障的诊断和解决，与云平台密切相关，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

### 数据库相关

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```

### 网络相关

## 常见问题

#### Parse 与 Parse Server 有什么区别？

Parse是一个在线的 Serverless 托管平台，现已停止运营。Parse Server 是开源 Parse 的功能，由用户自行下载部署到服务器的开源项目。

#### 如何修改Parse Dashboard 的密码？

修改 Parse Dashboard 的密码（[参考](/zh/solution-more.md#修改-parse-dashboard-账号密码)）

#### Parse Server 提供了哪些SDK？

IOS, Android, JavaScript, .NET + Xamarin, PHP, Arduino, Embedded C等 

#### Parse Server 数据库连接配置信息在哪里？

数据库配置信息在Parse Server 安装目录下的 *parse-server.json* 中，[查阅安装目录路径](/zh/stack-components.md#parse-server)

#### Parse Dashboard 数据库连接配置信息在哪里？ 

Parse Dashboard 不需要数据库支持，数据存储在文本文件中

#### 如果没有域名是否可以部署 Parse Server ？

不可以，必须[绑定域名](/zh/solution-more.md#域名绑定)

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置adminMongo，访问地址：http://服务器公网IP:9090

#### 如何禁止 adminMongo 访问？

关闭服务器安全组的9090端口即可禁止

#### 是否可以修改Parse Server 的源码路径？

不支持修改
