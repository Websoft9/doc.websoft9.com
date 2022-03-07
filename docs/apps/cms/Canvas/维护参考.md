---
sidebar_position: 2
slug: /canvas/admin
tags:
  - Canvas
  - 在线学习管理
---

# 维护参考

## 系统参数

Canvas 预装包包含 Canvas 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### Canvas

Canvas 安装目录： */data/wwwroot/canvas*  
Canvas 日志目录： */data/wwwroot/canvas/log*  
Canvas 配置目录： */data/wwwroot/canvas/config*  

#### Apache

Apache 虚拟主机配置文件：*/etc/httpd/conf.d/vhost.conf*  
Apache 主配置文件：*/etc/httpd/conf/httpd.conf*  
Apache 日志文件：*/var/log/httpd*

#### Passenger

Passenger 安装目录：*/usr/lib/ruby/vendor_ruby/phusion_passenger*  
Passenger 配置文件：*/etc/apache2/mods-enabled/passenger.conf*

#### Node.js

Node.JS 模块目录: */usr/lib/node_modules*  
Node.js 应用安装目录: */data/wwwroot*  
Node.JS 日志文件: */root/.pm2/pm2.log*

#### Ruby

Ruby 安装目录：*/usr/lib/ruby*  

#### PostgreSQL

PostgreSQL 配置文件: */data/postgresql/config*  
PostgreSQL 数据目录：*/data/postgresql/pgdata*  
PostgreSQL 日志目录: */data/postgresql/log*

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 80 | 通过 HTTP 访问 Canvas | 可选 |
| TCP | 443 | 通过 HTTPS 访问 Canvas  | 可选 |
| TCP | 9090 | PostgreSQL 可视化管理 | 可选 |
| TCP | 5432 | PostgreSQL 服务端 | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Apache version on Centos
httpd -v

# Apache version on Ubuntu
apache2 -v

# Passenger version
passenger -v

# Ruby version
ruby -v

# Node.js version
node -v

# Docker Version
docker -v
```


### 服务

使用由Websoft9提供的 Canvas 部署方案，可能需要用到的服务如下：

#### Canvas 主程序

通过 Apache 服务启停来管理 Canvas

```shell
sudo systemctl start apache
sudo systemctl stop apache
sudo systemctl restart apache
sudo systemctl status apache
```

#### Canvas Job

```shell
sudo systemctl start canvas-init
sudo systemctl stop canvas-init
sudo systemctl restart canvas-init
sudo systemctl status canvas-init
```

#### PostgreSQL

```shell
sudo systemctl start postgresql
sudo systemctl stop postgresql
sudo systemctl restart postgresql
sudo systemctl status postgresql
```

#### Redis

```shell
sudo systemctl start redis
sudo systemctl stop redis
sudo systemctl restart redis
sudo systemctl status redis
```

#### Passenger

```
sudo passenger start
sudo passenger stop
sudo passenger status
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

1. 通过 SFTP 工具将网站目录（*/data/wwwroot/canvas*）**压缩后**再完整的下载到本地
2. 通过 PostgreSQL 管理工具导出数据库
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


### Canvas升级

升级有点小复杂，详情参考官方升级文档：[Upgrading Canvas](https://github.com/instructure/canvas-lms/wiki/Upgrading)


## 故障处理

此处收集使用 Canvas 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

通过如下两种日志检索关键词 **Failed** 或者 **error** 查看错误

* Canvas 日志：`/data/wwwroot/canvas/log/production.log`
* Apache 日志：`/data/logs/apache`

#### Canvas服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
systemctl status apache
journalctl -u apache
```

#### 403 访问权限错误？

需要确保 Canvas 根目录具有 canvas 和 www-data 两个用户的权限


#### 文件上传，不能下载
文件上传后，下载出现“无法访问网站 找不到canvas.example.com服务器IP地址 ”
解决办法：
1. 找到apache配置文件/etc/apache2/conf.d/vhost.conf，将默认的ServerName canvas.example.com更改为 ServerName 实际部署站点域名
2. 找到域名配置文件/data/wwwroot/canvas/config/domain.yml，将 production 配置节点的 **domain** 项的值修改为你的域名

## 常见问题

#### Canvas 开源版是否提供移动端？

支持手机浏览器、Android 和 IOS 移动端。 详情参考：[mobile-guide](https://community.canvaslms.com/community/answers/guides/mobile-guide)

#### Canvas 支持中文吗

支持包括中文、英文等二十多种语言

#### Canvas 怎么安装插件？

通过BigBlueButton为例，步骤如下：

1. 登陆 Canvas 站点

2. 通过URL：*http://域名/plugins* 或 *http://服务器公网IP/plugins*, 进入插件选择页面
   ![canvas 插件](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-plugin01-websoft9.png)

3. 选择您要安装的插件，点击安装

4. 在插件安装页面，去掉勾选【禁用此插件】，输入相关引导信息，点击【申请】
   ![canvas 插件设置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-plugin02-websoft9.png)
   ![canvas 插件设置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-plugin03-websoft9.png)

5. 安装插件前后，页面已经发生变化（课程中追加了BigBlueButton对应的会议功能）
   ![canvas 插件安装前后对比](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-plugin04-websoft9.png)
   ![canvas 插件安装前后对比](https://libs.websoft9.com/Websoft9/DocsPicture/zh/canvas/canvas-plugin05-websoft9.png)

#### 是否可以通过命令行修改或重置 Canvas 管理员密码？

Canvas 官方没有提供。

#### 如果没有域名是否可以部署 Canvas？

可以，部署完成后通过：*http://公网IP* 访问即可

#### Canvas 官方云版本与 OpenSource 版本有区别吗？

有。具体参考 [code differences between the open source and hosted offerings](https://github.com/instructure/canvas-lms/wiki/FAQ#does-canvas-support-any-extensions)

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，参考[PostgreSQL管理](/zh/admin-postgresql.md)

#### 是否可以修改Canvas的源码路径？

可以，通过修改 Apache 虚拟主机配置文件实现

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R canvas.canvas /data/wwwroot/canvas
# 读写执行权限
find /data/wwwroot/canvas -type d -exec chmod 750 {} \;
find /data/wwwroot/canvas -type f -exec chmod 640 {} \;
```

#### Canvas 根目录同时需要赋予用户 canvas 和 www-data （Apache用户）权限，是如何做到的？

拥有者是 canvas，同时通过 setfacl 额外给 www-data 赋予权限

```
setfacl -m u:www-data:rx -R /data/wwwroot/canvas
```
#### 推荐一个国内学习 Canvas 的网站

小编认为[上海交通大学教育技术中心](https://v.sjtu.edu.cn/guide/)还不错

