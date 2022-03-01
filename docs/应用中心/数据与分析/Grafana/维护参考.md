---
sidebar_position: 2
slug: /grafana/admin
tags:
  - Grafana
  - 大数据分析
  - BI
---

# 维护参考

## 系统参数

Grafana 预装包包含 Grafana 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### Grafana

Grafana 安装目录： */usr/share/grafana*  
Grafana 配置文件： */usr/share/grafana/conf/defaults.ini*  
Grafana 日志文件： */var/log/grafana/grafana.log*  
Grafana 数据存储路径：*/usr/share/grafana/data*   
Grafana 数据日志路径：*/usr/share/grafana/data/log*

> Grafana 配置文件中包含数据库连接信息，数据存储路径、日志存储路径、STMP等重要配置

#### Go

Grafana 基于 Go 语言开发

#### Node.js

Grafana 前端采用 Node.js 开发，本预装包基于 apt/yum 安装，前端已经构建好，服务器上无需安装 Node.js

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx/*

#### SQLite

SQLite 数据库默认位于: /var/lib/grafana/grafana.db。 请在升级前备份此数据库。

### 端口号

下面是您在使用本镜像过程中，需要用到的端口号，请通过 [云控制台安全组](https：//support.websoft9.com/docs/faq/zh/tech-instance.html)进行设置

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过 http 访问Grafana by Nginx proxy| 必须 |
| HTTPS | 443 | 通过 https 访问 Grafana by Nginx proxy | 可选 |
| Grafana | 3000 | Grafana 端口 | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Nginx version：
nginx -v
```

### 服务

使用由Websoft9提供的Grafana部署方案，可能需要用到的服务如下：

#### Grafana

```shell
sudo systemctl start grafana-server
sudo systemctl stop grafana-server
sudo systemctl restart grafana-server
sudo systemctl status grafana-server
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

1. 通过WinSCP将程序目录（*/usr/share/grafana*）**压缩后**再完整的下载到本地
2. [备份数据库](https://grafana.com/docs/installation/upgrading/#database-backup)
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

### Grafana升级

请参考官方提供的升级文档：[Upgrading Grafana](https://grafana.com/docs/installation/upgrading/)

## 故障处理

此处收集使用 Grafana 过程中最常见的故障，供您参考

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

#### Grafana支持哪些数据源？

官方支持以下数据源:Graphite，InfluxDB，OpenTSDB，Prometheus，Elasticsearch，CloudWatch 和 KairosDB。

#### Grafana数据库连接配置信息在哪里？

数据库配置信息在Grafana安装目录下的 *defaults.ini* 中，[查阅安装目录路径](/zh/stack-components.md#grafana)

#### Grafana 是否提供CLI工具？

SSH登录服务器，即可运行 grafana-cli。功能非常强大，包括配置系统、修改密码等
```
# 修改管理员密码
grafana-cli admin reset-admin-password admin123
```

#### 如果没有域名是否可以部署 Grafana？

可以，访问`http://服务器公网IP` 即可

#### 是否可以修改 Grafana 的访问端口？

可以，通过修改 [Nginx 虚拟主机配置文件](/zh/stack-components.md)中相关参数
