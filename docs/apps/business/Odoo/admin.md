---
sidebar_position: 2
slug: /odoo/admin
tags:
  - Odoo
  - 企业管理
  - ERP
---

# 维护参考

## 系统参数

Odoo 预装包包含 Odoo 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

Linux 和 Windows 版本的 Odoo 路径完全不同，请根据你的操作系统参考对应项：

#### Linux

##### Odoo

Odoo 安装目录： */usr/lib/python3/dist-packages/odoo*  
Odoo 配置文件： */etc/odoo/odoo.conf*  
Odoo 日志目录： */var/log/odoo*

##### Python

Python 安装目录： */usr/lib/python**  
Python 虚拟机目录: */usr/bin/python**  
*is version 2.7/3/3.6/3.7

##### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/sites-available/default*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志目录： */var/log/nginx/*

##### PostgreSQL

PostgreSQL 安装路径：*/usr/bin/psql*  
PostgreSQL 数据文件：*/var/lib/postgresql*   
PostgreSQL 配置文件：*/etc/postgresql/10/main/postgresql.conf*      
PostgreSQL 日志文件：*/var/log/postgresql*  
PostgreSQL 可视化管理地址: Odoo 登录界面提供了数据库的导入和密码修改等功能

#### Windows

##### Odoo

Odoo 安装目录： *C:\Program Files (x86)\Odoo-v*  
Odoo 配置文件： *C:\Program Files (x86)\Odoo-v\server\odoo.conf*    
Odoo 日志文件： *C:\Program Files (x86)\Odoo-v\server\odoo*

##### PostgreSQL

PostgreSQL 安装路径: *C:\Program Files (x86)\Odoo-v\PostgreSQL*  
PostgreSQL 数据目录: *C:\Program Files (x86)\Odoo-v\PostgreSQL\base*  
PostgreSQL 可视化管理地址：服务器上安装了 pgAdmin 用于可视化管理 PostgreSQL

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

本应用建议开启的端口如下：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过 HTTP 访问 Odoo | 必须 |
| HTTPS | 443 | 通过 HTTPS 访问 Odoo | 可选 |
| PostgreSQL | 5432 | 远程连接 PostgreSQL | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Linux Version
lsb_release -a

# Python Version
python --version  
python3 --version

# Nginx version:
nginx -v

# PostgeSQL version:
psql --version
```

### 服务

使用由Websoft9提供的 Odoo 部署方案，可能需要用到的服务如下：

#### Linux

##### Odoo

```shell
sudo systemctl start odoo
sudo systemctl stop odoo
sudo systemctl restart odoo
sudo systemctl status odoo
```

##### Nginx

```shell
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
```

##### PostgreSQL

```shell
sudo systemctl start postgresql
sudo systemctl stop postgresql
sudo systemctl restart postgresql
sudo systemctl status postgresql
```

#### Windows

如果您使用的是 Windows系统，Odoo 服务重启两种方式：

*  方式1: 【开始】>【管理工具】>【服务】，找到 odoo-server，便可以完成**重启/停止/暂停**等操作
*  方式2: 【开始】>【运行】，输入`cmd`，打开命令操作窗口
   ```
   net start odoo-server-12.0 #启动服务
   net stop odoo-server-12.0 #停止服务
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

1. 通过WinSCP将网站目录（*/usr/lib/python3/dist-packages/odoo*）**压缩后**再完整的下载到本地
2. 通过 Odoo 自带的数据库管理工具备份数据库
   ![Odoo 备份数据库](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-managesbk-websoft9.png)
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

### Odoo升级

Odoo 后台提供了在线升级能力，让升级工作变得非常简单。参考下面的步骤完成升级：

1. 登录 Odoo 后台，[启动开发者模式](/zh/solution-odoo.md#开发者模式)
2. 通过 【Settings】>【Updates】开始更新 Odoo 主程序
   ![Odoo升级提示](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-upgradesui-websoft9.png)
3. 升级成功会有 “Well done...” 的提示
4. 点击 【Update Apps list】，开始更新 Odoo 模块

更多更新方案和注意事项请参考官方文档：[Odoo Update](https://www.odoo.com/documentation/master/setup/update.html)


## 故障处理

此处收集使用 Odoo 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

最简单的方式是通过SSH连接服务器，运行`odoo`这个命令，就会显示错误日志以及Odoo的运行情况

#### 恢复数据库、上传附件等操作，出现 “413 Request Entity Too Large” 错误？

这是由于 Nginx 默认安装下，上传文件最大为 1M，因此需要修改 Nginx 这个限制：
1. 使用 WinSCP 远程连接服务器
2. 编辑 [Nginx 虚拟机主机配置文件](/zh/stack-components.md#nginx)
3. 插入一行 `client_max_body_size 0;` 解除上传文件限制的配置项
   ```
   server {
    listen 80;
    server_name _;
    client_max_body_size 0; #解除上传文件限制
    ...
   ```
4. 保存并[重启 Nginx 服务](/zh/admin-services.md#nginx)

#### 访问Odoo总是出现数据库设置提醒？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/odoo/odoo-setpasswodrem-websoft9.png)

这个提醒的是要求你尽快给数据库设置一个高强度的管理员密码，如果不设置将面临很大的风险。一旦设置后，此界面就不会再弹出了

#### 无法通过 SFTP 上传文件到Odoo程序目录问题

由于部分 Ubuntu系统 默认创建了默认用户名 ubuntu ,ubuntu为普通用户没有对odoo程序的源码或目录有操作的权限,需要执行一下命令:

```
sudo chmod o+rw  /usr/lib/python2.x/dist-packages/odoo   # odoo10版本
sudo chmod o+rw  /usr/lib/python3/dist-packages/odoo   # odoo11版本以上
```

#### PDF无法打印中文

Odoo11之前的版本，在使用Odoo打印功能时，下载的PDF文件只有英文，没有中文，导致打印不完整。

**问题原因**：系统环境里没有下载所需的中文字体

**解决方案**：执行以下命令下载字体

~~~
sudo apt-get install ttf-wqy-zenhei
sudo apt-get install ttf-wqy-microhei
~~~

#### Odoo 备份出现 Command pg_dump not found
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/odoo/odoo-backuperror-websoft9.png)
原因：PostgreSQL的备份命令没有找到
解决方案：需要进一步查看PostgreSQL安装问题，还是Odoo本身的问题

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

#### Odoo支持多语言吗？

支持多语言（包含中文），参考：[语言设置](/zh/solution-odoo.md#增加语言)

#### Odoo数据库连接配置信息在哪里？

Odoo 采用 [Peer Authentication](https://www.postgresql.org/docs/10/auth-methods.html#AUTH-PEER) 方式连接 PostgreSQL，即以操作系统用户登录数据库，无需密码。

#### 为什么在设置面板看不到 Odoo 更新（Updates）操作功能？

此功能只能在开发者模式下使用，请确保你的 Odoo 控制台是否已经切换成[开发者管理模式](zh/solution-odoo.md#开发者模式)

#### 如何删除 Odoo 演示数据？

由于 Odoo 支持多企业组织方式，建议新增一个企业组织（不要勾选演示数据）后，再删除带演示的数据库。具体操作方式参考：[ Odoo 数据库管理](/zh/admin-postgresql.md#新增)

#### Odoo 是否可以导出 PDF 文件？

可以。安装 Invoice, Purchase 等模块可以测试 print to PDF 功能
![Odoo 打印PDF](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-printtopdf-websoft9.png)

#### 如果没有域名是否可以部署 Odoo？

可以，访问`http://服务器公网IP` 即可

#### Windows版的 Odoo 的 PostgreSQL 用户对应的密码是多少？

请在[账号密码](/zh/stack-components.md#postgresql)章节查看

#### 是否有可视化的数据库管理工具？

请直接通过 [Odoo 自带的数据库管理工具](/zh/admin-postgresql.md)操作

#### 是否可以修改Odoo的源码路径？

不可以

#### 如何修改上传的文件权限?

```shell
chown -R nginx.nginx /data/wwwroot/
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```
