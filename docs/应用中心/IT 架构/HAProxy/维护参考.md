---
sidebar_position: 2
slug: /haproxy/admin
tags:
  - HAProxy
  - IT 架构
  - 中间件
---

# 维护参考

## 系统参数

HAProxy 预装包包含 HAProxy 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### HAProxy Community

HAProxy 配置文件： */etc/haproxy/haproxy.cfg*  
HAProxy 日志目录： */var/log/haproxy.log*  

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 1080 | 通过 HTTP 访问 HAProxy  Statistics Report | 可选 |
| TCP | 5000 | for  HAProxy  | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# HAProxy version
haproxy -v
```

### 服务

使用由Websoft9提供的 HAProxy 部署方案，可能需要用到的服务如下：

### HAProxy

```shell
sudo systemctl start haproxy
sudo systemctl stop haproxy
sudo systemctl restart haproxy
sudo systemctl status haproxy
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
HAProxy通用的手动备份操作步骤如下：

1. 通过 WinSCP 将网站目录（*//etc/haproxy/haproxy.cfg*）完整的下载到本地
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

### HAProxy升级

如果yum/apt更新后的版本无法满足您需求，请通过[源码编译安装](https://github.com/haproxy/haproxy/blob/master/INSTALL)您所需的版本

## 故障处理

此处收集使用 HAProxy 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/var/logs/haproxy`。检索关键词 **Failed** 或者 **error** 查看错误

#### HAProxy服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看数据库状态和日志
systemctl status haproxy
journalctl -u haproxy
```

## 常见问题

#### 本部署方案采用的那种安装方式安装HAProxy？

yum/apt 安装方式

#### 是否可以通过命令行修改HAProxy后台密码？

可以，修改配置文件`/etc/haproxy/haproxy.cfg`

#### 如果没有域名是否可以部署 HAProxy？

可以

#### 是否有可视化的管理工具？

默认开启 HAProxy Statistics Report 可视化界面，访问：*http://Internet IP:1080/haproxy* 即可

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R haproxy.haproxy /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```