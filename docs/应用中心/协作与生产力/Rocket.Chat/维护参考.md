---
sidebar_position: 2
slug: /rocketchat/admin
tags:
  - Rocket.Chat
  - 团队协作
  - 团队通讯
---

# 维护参考

## 系统参数

Rocket.Chat 预装包包含 Rocket.Chat 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### Rocket.Chat

Rocket.Chat 安装目录： */data/wwwroot/rocketchat*  
Rocket.Chat 日志目录： */data/logs/nginx*  

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*

#### MongoDB

MongoDB 数据目录: /var/lib/mongodb
MongoDB 配置文件: /etc/mongod.conf
MongoDB 日志文件: /var/log/mongodb   
MongoDB 可视化管理地址: *http://服务器公网IP/9091*，用户名和密码请见 [账号密码](/zh/stack-accounts.md) 章节。

#### adminMongo

adminMongo installation directory: */data/apps/adminmongo*  
adminMongo configuration file: */data/apps/adminmongo/config* 

#### Node.JS
Node.JS 模块目录: /usr/lib/node_modules
Node.js 应用安装目录: /data/wwwroot
Express 示例目录: /data/wwwroot/express.example.com
Node.JS 日志文件: /root/.pm2/pm2.log

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 3000 | 通过 HTTP 访问 Rocket.Chat 控制台 | 可选 |
| TCP | 27017 | mongodb | 可选 |

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

# mongo  Version
mongo --version | grep MongoDB

# Rocket.Chat version
curl  localhost/api/info
```

### 服务

使用由Websoft9提供的 Rocket.Chat 部署方案，可能需要用到的服务如下：

#### Rocket.Chat

```shell
sudo systemctl start rocketchat
sudo systemctl stop rocketchat
sudo systemctl restart rocketchat
sudo systemctl status rocketchat

```

#### PM2

```shell
systemctl start pm2-root
systemctl stop pm2-root
systemctl restart pm2-root
systemctl status pm2-root
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
systemctl start mongod
systemctl stop mongod
systemctl restart mongod
systemctl status mongod
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

1. 通过 WinSCP 将网站目录（*/data/wwwroot/*）**压缩后**再完整的下载到本地
2. 通过  `mongodump` 逐个导出数据库
   ```
   #1 backup
   mongodump --authenticationDatabase admin --username root --password PASSWORD -d DATABASE_NAME -h localhost

   # check you backup
   cd dump/admin
   ls
   ```
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

### Rocket.Chat升级

详情参考官方升级文档：[Upgrading Rocket.Chat](https://www.rocketchat.com/upgrade.html)

## 故障处理

此处收集使用 Rocket.Chat 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### Rocket.Chat服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
sudo systemctl status rocketchat
sudo journalctl -u rocketchat
```

## 常见问题

#### 如何以调试模式启动Rocket.Chat服务？

```
systemctl stop rocketchat
rocketchat-server console
```

#### 是否可以通过命令行修改Rocket.Chat后台密码？

可以，`rocketchatctl change_password  admin newpassword`

#### 如果没有域名是否可以部署 Rocket.Chat？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置adminMongo，访问地址：*http://服务器公网IP/9091*

#### 如何禁止外界访问adminMongo？

连接服务器，编辑 [adminMongo 配置文件](/zh/stack-components.md#adminMongo)，将其中的 `Require all granted` 更改为 `Require ip 192.160.1.0`，然后重启 Apache 服务

#### 是否可以修改Rocket.Chat的源码路径？

不可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R apache.apache /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```
