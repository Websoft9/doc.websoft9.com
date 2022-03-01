---
sidebar_position: 2
slug: /rethinkdb/admin
tags:
  - RethinkDB
  - Cloud Native Database
---

# 维护参考

## 系统参数

RethinkDB 预装包包含 RethinkDB 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### RethinkDB

RethinkDB 安装目录： */data/rethinkdb*  
RethinkDB 日志目录： */data/logs/rethinkdb*  

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*  
Nginx 验证访问文件：*/etc/nginx/.htpasswd/htpasswd.conf*  

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过 HTTP 访问 RethinkDB 控制台 | 可选 |
| TCP | 28015 | RethinkDB connect | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Nginx  Version
nginx -V

# rethinkdb version
rethinkdb --version
```

### 服务

使用由 Websoft9 提供的 RethinkDB 部署方案，可能需要用到的服务如下：

#### RethinkDB

```shell
sudo systemctl start rethinkdb
sudo systemctl stop rethinkdb
sudo systemctl restart rethinkdb
sudo systemctl status rethinkdb
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

### RethinkDB 备份
RethinkDB 主要通过导出的实现备份，通过导入实现恢复：

```
# 导出普通数据库文件
rethinkdb export abc.db

# 导出压缩格式数据库文件
rethinkdb dump [options]
```

## 恢复

```
rethinkdb import -d [options]
```

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

### RethinkDB 升级

官方没有提供版本升级命令，只提供了一个升级后的数据迁移方案：[Migrating](https://rethinkdb.com/docs/migration/)


## 故障处理

此处收集使用 RethinkDB 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### RethinkDB 服务无法启动？

1. 运行 `systemctl status rethinkdb` 命令，便可以查看启动状态和错误
2. 打开日志文件：*/data/logs/rethinkdb-server*，检索 **failed** 关键词，分析错误原因

#### 修改 RethinkDB 控制台密码后，浏览器报错？

浏览器缓存导致，打开新的无痕窗口或清空缓存即可。


## 常见问题

#### 是否有 RethinkDB 的 CLI 工具？

有，安装后存在cli命令，通过 `rethinkdb -h`查看使用详细

#### `rethinkdb repl` 命令如何采用密码登录？

```
rethinkdb repl --password-file /tmp/pw
```

其中 /tmp/pw 为存放密码明文的文件。

#### RethinkDB支持哪些语言？

我们提供Ruby，Python，Java和JavaScript / Node.js的官方驱动程序。社区支持的驱动程序支持十多种其他语言，包括C＃/。NET，Go和PHP。

#### 是否可通过命令行修改 RethinkDB 控制台密码？

可以，运行下面的命令即可：
```
htpasswd -b /etc/nginx/.htpasswd admin new_password
```

#### 是否可以通过 IP+端口的方式访问 RethinkDB？

不可以，为了安全考量默认仅支持 127.0.0.1 访问，所以需通过 Nginx 转发。

#### RethinkDB 控制台的账号密码是什么？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，访问地址：*http://服务器公网IP*

#### 是否可以修改rethinkdb的源码路径？

不可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R nginx.nginx /data/rethinkdb/
# 读写执行权限
find /data/rethinkdb/ -type d -exec chmod 750 {} \;
find /data/rethinkdb/ -type f -exec chmod 640 {} \;
```
