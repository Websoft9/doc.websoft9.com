---
sidebar_position: 2
slug: /rabbitmq/admin
tags:
  - RabbitMQ 
  - IT 架构
  - 中间件
---

# 维护参考

## 系统参数

RabbitMQ 预装包包含 RabbitMQ 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

虽然运行 `whereis` 命令可以查看相关安装路径，但接下来我们仍然对路径信息进行更为准确的说明。

```shell
whereis rabbitmq-server
whereis erlang

#For Centos&Redhat
rpm -ql rabbitmq-server
rpm -ql erlang

#For Ubuntu&Debian
dpkg -L rabbitmq-server
```

#### RabbitMQ

RabbitMQ 安装目录： */data/rabbitmq*  
RabbitMQ 日志目录： */data/logs/rabbitmq*  

#### Erlang

Erlang 安装目录： */data/erlang*  

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp`查看相关端口，下面列出本应用可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 15672 | 通过 HTTP 访问 RabbitMQ 控制台 | 必须 |
| TCP | 5672 | RabbitMQ连接端口 | 可选 |
| TCP | 4369 | Erlang distribution | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Linux Version
lsb_release -a

# erlang  Version
yum info erlang
apt show erlang

# RabbitMQ version
rabbitmqctl status | grep RabbitMQ*
```

### 服务

使用由Websoft9提供的 RabbitMQ 部署方案，可能需要用到的服务如下：

#### RabbitMQ

```shell
sudo systemctl start rabbitmq-server
sudo systemctl stop rabbitmq-server
sudo systemctl restart rabbitmq-server
sudo systemctl status rabbitmq-server

# you can use this debug mode if RabbitMQ service can't run
rabbitmq-server console
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

1. 通过WinSCP将网站目录（*/usr/lib/rabbitmq*）**压缩后**再完整的下载到本地
2. 备份工作完成


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

### RabbitMQ升级

详情参考官方升级文档：[Upgrading RabbitMQ](https://www.rabbitmq.com/upgrade.html)

## 故障处理

此处收集使用 RabbitMQ 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### RabbitMQ服务无法启动？

1. 以调试模式运行`rabbitmq-server console`，便可以查看启动状态和错误
   ```
   rabbitmq-server console
   ```
2. 打开日志文件：*/data/logs/rabbitmq-server*，检索 **failed** 关键词，分析错误原因


#### 在Chrome下修改密码后报错？

这个并不是服务器端的问题，只要更新浏览器即可。

![chrome error of RabbitMQ](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-chromeerror-websoft9.png)

## 常见问题

#### 如何以调试模式启动RabbitMQ服务？

```
systemctl stop rabbitmq-server
rabbitmq-server console
```

#### 是否可以通过命令行修改RabbitMQ后台密码？

可以，`rabbitmqctl change_password  admin newpassword`

#### 如果没有域名是否可以部署 RabbitMQ？

可以，访问`http://服务器公网IP` 即可

#### 是否可以修改RabbitMQ的源码路径？

不可以
