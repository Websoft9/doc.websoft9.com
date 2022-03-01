---
sidebar_position: 2
slug: /superset/admin
tags:
  - Metabase
  - 大数据分析
  - BI
---

# 维护参考

## 系统参数

Metabase 预装包包含 Metabase 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### Metabase

Metabase 安装目录： */data/wwwroot/metabase*  
Metabase 配置文件： */data/wwwroot/metabase/metabase.conf*  

> Metabase 配置文件中包含数据库连接信息，更改了 MySQL 数据库账号密码，此处也需要对应修改

#### Java

Java Directory: */usr/lib/jvm*

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/sites-available/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx/*

#### MYSQL

MySQL 安装路径: */usr/local/mysql*  
MySQL 数据文件 */data/mysql*  
MySQL 配置文件: */etc/my.cnf*    
MySQL 可视化管理地址: *http://服务器公网IP:9090*，用户名和密码请见 [账号密码](/zh/stack-accounts.md) 章节。


### 端口号

系统所用到的端口号，请通过官方文档 [Package defaults](https://docs.gitlab.com/omnibus/package-information/defaults.html) 查阅。在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

本应用建议开启的端口如下：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过 HTTP 访问 Odoo | 必须 |
| HTTPS | 443 | 通过 HTTPS 访问 Odoo | 可选 |
| MySQL | 3306 | 远程连接 MySQL | 可选 |
| phpMyAdmin on Docker | 9090 | 可视化管理 MySQL | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Linux Version
lsb_release -a

# Java Version
java --version

# Nginx version:
nginx -v

# MySQL version:
mysql -V

# Dokcer:
docker --version
```

### 服务

使用由Websoft9提供的Metabase部署方案，可能需要用到的服务如下：

#### Metabase

```shell
sudo docker start metabase
sudo docker stop metabase
sudo docker restart metabase
sudo docker status metabase
```

#### Nginx

```shell
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
```

#### MySQL

```shell
sudo docker start metabase-mysql
sudo docker stop metabase-mysql
sudo docker restart metabase-mysql
sudo docker status metabase-mysql
```

#### Docker
```shell
sudo systemctl star docker
sudo systemctl stop docker
sudo systemctl restart docker
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

1. 通过WinSCP将网站目录（*/data/wwwroot/metabase*）**压缩后**再完整的下载到本地
2. 通过phpMyAdmin导出Metabase数据库
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)
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

### Metabase升级

Metabase有升级包的时候，后台会及时给出提示。参考下面的步骤完成升级：

1. Metabase后台->设置->升级，如果有新的升级包，系统会给与提示
![Metabase升级提示](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatereminder-websoft9.png)

2. 点击“更新”按钮后，系统会跳转到Metabase官方的安装页面。
3. 我们提供的部署包采用的是jar包安装模式，因此在安装页面我们选择“Custom install”模式，
![Metabase升级提示](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatedl-websoft9.png)

3. 下载Metabase.jar包后，上传到服务器 `/data/wwwroot/metabase`, 覆盖已有的同名文件
![Metabase升级提示](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatereplace-websoft9.png)

4. 重新加载Metabase，升级成功

## 故障处理

我们收集使用Metabase过程中最常见的故障，供您参考：

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

#### Metabase支持多语言吗？

支持多语言（包含中文），系统默认根据浏览器自动选择语言 

#### Metabase数据库连接配置信息在哪里？

数据库配置信息在Metabase安装目录下的 *metabase.conf* 中，[查阅安装目录路径](/zh/stack-components.md#metabase)

#### 如果没有域名是否可以部署 Metabase？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP:9090

#### 如何禁止phpMyAdmin访问？

关闭服务器安全组的9090端口即可禁止

#### 是否可以修改Metabase的源码路径？

可以，通过修改 [Nginx 虚拟主机配置文件](/zh/stack-components.md)中相关参数

#### 如何修改上传的文件权限?

```shell
chown -R nginx.nginx /data/wwwroot/metabase
find /data/wwwroot/metabase -type d -exec chmod 750 {} \;
find /data/wwwroot/metabase -type f -exec chmod 640 {} \;
```
