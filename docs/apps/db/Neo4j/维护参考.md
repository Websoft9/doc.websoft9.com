---
sidebar_position: 2
slug: /neo4j/admin
tags:
  - Neo4j 
  - Cloud Native Database
---

# 维护参考

## 系统参数

Neo4j 预装包包含 Neo4j 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### Neo4j

运行 `neo4j console` 命令查看安装相关的路径：

Neo4j 程序路径：*/var/lib/neo4j*  
Neo4j 配置文件路径：*/etc/neo4j/neo4j.conf*   
Neo4j 日志路径：*/var/log/neo4j*  
Neo4j 插件路径：*/var/lib/neo4j/plugins*  
Neo4j 数据路径：*/var/lib/neo4j/data*  
Neo4j 证书路径：*/var/lib/neo4j/certificates*  
Neo4j 启动路径：*/var/run/neo4j*  

> 更多安装路径请查看 *neo4j.conf* 文件，配置文件设置参考[此处](https://neo4j.com/docs/operations-manual/current/configuration)

#### Java

Java Directory: */usr/lib/jvm*

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx/*


### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过http访问 Neo4j Browser| 必须 |
| HTTPS | 443 | 通过https访问 Neo4j Browser| 可选 |
| Neo4j | 7687 | Neo4j Browser 远程连接 Neo4j database | 可选 |

Neo4j 使用中可能需要用到更多的端口，详情参考官方文档：[Port on Configuration file](https://neo4j.com/docs/operations-manual/current/configuration/ports/)

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Nginx  Version
nginx -V

# Java version
java -v

# Neo4j version
neo4j-admin -V
neo4j version
```

### 服务

使用由 Websoft9 提供的 Neo4j 部署方案，可能需要用到的服务如下：

### Neo4j

```shell
sudo systemctl start neo4j
sudo systemctl stop neo4j
sudo systemctl restart neo4j
sudo systemctl status neo4j
```

### Nginx

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

### Neo4j 官方方案

请参考 [Neo4j's Backup Docs](https://neo4j.com/docs/operations-manual/current/backup/)

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

### Neo4j 升级

Neo4j 升级有一定的复杂性，请参考[官方升级文档](https://neo4j.com/docs/operations-manual/current/upgrade/)

升级对象一般指的是：Neo4j 4.1.2 to Neo4j 4.2.0，下面说明主要步骤：

1. 停止 Neo4j 服务之后，安装指定的版本
    ```
    sudo systemctl stop neo4j
    sudo apt-get update
    sudo sudo apt-get install neo4j=1:4.2.2
    ```
2. 修改 Neo4j 配置文件，取消 `dbms.allow_upgrade=true` 前面的 # 号

3. 运行 Neo4j 启动服务的命令
    ```
    sudo systemctl start neo4j
    ```
4. 系统升级开始
5. 升级完成之后，恢复 `dbms.allow_upgrade=true`之前的 # 号

## 故障处理

此处收集使用 Neo4j 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### Neo4j 服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
systemctl status neo4j
journalctl -u neo4j
```

## 常见问题

#### Neo4j支持多语言吗？

支持多语言（包含中文），系统默认根据浏览器自动选择语言 

#### 社区版 vs 企业版？

参考：[Neo4j 功能细节对比](https://neo4j.com/docs/operations-manual/current/introduction/#edition-details)

#### Neo4j 支持哪些连接协议？

Neo4j 支持三种不同的连接方式：Bolt、HTTP、HTTPS。

#### Neo4j browser 是什么？

Neo4j浏览器是一个可以通过Web浏览器运行的图形用户界面（GUI）。 Neo4j浏览器可用于添加数据，运行查询，创建关系等。 它还提供了一种可视化数据库中数据的简便方法。

#### Neo4j 一个实例支持多个数据库吗？

支持，但社区版仅支持一个默认的系统库和用户库

#### Neo4j 有行和列的概念吗？

有，但存储的是数据节点以及节点之间的关系

#### Cypher 是什么？

Cypher是操作Neo4j的语句，等同于SQL

#### 如果没有域名是否可以部署 Neo4j？

可以，访问`http://服务器公网IP` 即可

#### 是否有可视化的数据库管理工具(GUI)？

有，内置 Neo4j Browser，访问地址：*http://服务器公网IP* 即可

#### 如何禁止Neo4j Browser 访问？

关闭服务器安全组的 80 端口即可禁止

#### 是否可以修改Neo4j的源码路径？

不可以
