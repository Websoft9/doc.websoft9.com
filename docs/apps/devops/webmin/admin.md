---
sidebar_position: 3
slug: /webmin/admin
tags:
  - Webmin
  - 虚拟桌面
  - Web 可视化 Linux 管理员工具
---

# 维护参考

## 系统参数

Webmin 预装包包含 Webmin 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### Webmin

Webmin 安装目录： */data/apps/webmin*  
Webmin 日志文件： */data/apps/webmin/webmin.log*  
Webmin 模块目录： */data/apps/webmin/modules*  

#### Apache

Apache 虚拟主机配置文件：*/etc/httpd/conf.d/vhost.conf*  
Apache 主配置文件： */etc/httpd/conf/httpd.conf*  
Apache 日志文件： */var/log/httpd*  
Apache 模块配置文件： */etc/httpd/conf.modules.d/00-base.conf*

#### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   
Docker daemon.json 文件：默认没有创建，请到 */etc/docker* 目录下根据需要自行创建   

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 10000 | 通过 HTTP 访问 Webmin 控制台 | 可选 |
| TCP | 80 | Apache 转发访问 Webmin 控制台 | 可选 |
| TCP | 443 | Apache 转发加密访问 Webmin 控制台 | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Docker Version
docker -v

# Apache Version
httpd -v

# Webmin version
cat /data/apps/webmin/
```

### 服务


使用由Websoft9提供的 Webmin 部署方案，可能需要用到的服务如下：

#### Webmin

```shell
sudo systemctl start webmin
sudo systemctl stop webmin
sudo systemctl restart webmin
sudo systemctl status webmin
```

#### Apache

```shell
sudo systemctl start apache
sudo systemctl stop apache
sudo systemctl restart apache
sudo systemctl status apache
```

#### Docker

```shell
sudo systemctl start docker
sudo systemctl restart docker
sudo systemctl stop docker
sudo systemctl status docker
```

#### Docker-Compose
```
#创建容器编排
sudo docker-compose up -d

#删除容器编排
sudo docker-compose up -d

#启动/停止/重启
sudo docker-compose start
sudo docker-compose stop
sudo docker-compose restart
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

1. 通过 SFTP 将网站目录（*/data/apps/webmin*）**压缩后**再完整的下载到本地
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

### Webmin 升级

Webmin 提供了可视化的在线升级功能，升级非常方便

![升级](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-upgrade-websoft9.png)


## 故障处理

此处收集使用 Webmin 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### Webmin服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
systemctl status webmin
journalctl -u webmin
```

## 常见问题

#### Webmin 是否支持多语言？

支持（包含中文），控制台自由切换

#### 本项目中 Webmin 采用何种安装方式？

采用 rpm/deb 包的安装方式

#### 新装的 Webmin 模块为何任然显示在 Un-used Modules 菜单下？

安装模块后，点击【刷新模块】才可将模块自动显示在正常的菜单下

#### HTTP Tunnel 有什么作用？

待研究

#### 如何禁用 Webmin 继承操作系统账号？

默认的【Unix验证】 更改为 【设置为】，同时设置新密码和用户

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-usermode-websoft9.png)

#### Webmin 中是否包含 Apache？

不包含。但本部署方案中我们额外安装了 Apache

#### 是否可以通过命令行修改 Webmin 后台密码？

Webmin 使用的是服务器 root 密码，因此用 `passwd` 系统命令即可

#### 如果没有设置 HTTP 是否运行 Webmin？

可以，访问`http://服务器公网IP:10000` 即可

#### 是否可以修改Webmin的源码路径？

不可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R apache.apache /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```

