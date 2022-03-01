---
sidebar_position: 2
slug: /python/admin
tags:
  - Python
  - 运行环境
---


# 维护参考

## 系统参数

Python 预装包包含 Python 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### Python

除了 Python3 之外，预装包中还安装了 Virtualenv, pip 等常用的 Python 工具。

Python 应用目录： */data/wwwroot*  
Python 框架目录： */data/apps*  
Python 源码目录： */usr/lib/python*  
Python 日志目录： */data/logs/python*  

> 操作系统一般默认自带 Python2，部分操作系统默认也安装了 Python3

#### Django

##### Linux

Django 安装目录： */data/wwwroot/django*  
Django systemctl 名称： *django.service*  

##### Windows

采用 [Bitnami Django](https://bitnami.com/stack/django) 安装包制作而成。  

Django 安装目录： *C:\websoft9\django*  
Django 安装目录： *C:\websoft9\django\apache2\htdocs*  

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*

#### MySQL

MySQL 安装路径: */usr/local/mysql*  
MySQL 数据文件 */data/mysql*  
MySQL 配置文件: */etc/my.cnf*  

MySQL 可视化管理参考 [MySQL 管理](/zh/admin-mysql.md) 章节。

#### phpMyAdmin

phpMyAdmin 是一款可视化 MySQL 管理工具，在本项目中它基于 Docker 安装。  

phpMyAdmin directory：*/data/apps/phpmyadmin*  
phpMyAdmin docker compose file：*/data/apps/phpmyadmin/docker-compose.yml* 

#### MongoDB

MongoDB 数据目录: */var/lib/mongodb*  
MongoDB 配置文件: */etc/mongod.conf*  
MongoDB 日志文件: */var/log/mongodb*  

#### adminMongo

adminMongo 是一款可视化 MongoDB 管理工具，采用 Docker 安装

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*  

#### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   
Docker daemon.json 文件：默认没有创建，请到 */etc/docker* 目录下根据需要自行创建   

#### Redis

Redis 配置文件： */etc/redis.conf*  
Redis 数据目录： */var/lib/redis*  
Redis 日志文件： */var/log/redis/redis.log*

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 8000 | 通过 HTTP 直接访问 Django 演示页面 | 可选 |
| TCP | 80 | 通过 HTTP 直接访问 Python 应用 | 必选 |
| TCP | 443 | 通过 HTTPS 直接访问 Python 应用 | 可选 |
| TCP | 3306 | MySQL 远程访问端口 | 可选 |
| TCP | 9090 | 通过 HTTP 访问 phpMyAdmin | 可选 |
| TCP | 27017 | MongoDB 远程访问端口 | 可选 |
| TCP | 9091 | 通过 HTTP 访问 adminMongo | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Nginx  Version
nginx -V

# Python version
python3 -V
python -V

# Docker Version
docker -v

# MySQL version
mysql -V

# MongoDB version
mongodb -V

# Django version
/data/wwwroot/django/bin/pip show django
```

### 服务

使用由 Websoft9 提供的 Python 部署方案，可能需要用到的服务如下：

#### Django

##### On Linux

```shell
systemctl start django
systemctl stop django
systemctl restart django
systemctl status django
```

##### On Windows

服务随操作系统自动启动，如果手工修改配置参数后，需要重新启停服务，有两种方法。

* 方法一：在“开始”-> “管理工具”->“服务”中重启django***服务。

* 方法二：在C:\websoft9\django*中找到“manager-windows”。

双击打开“manager-windows”，可以进行服务启停、参数配置。


#### Nginx

```shell
systemctl start nginx
systemctl stop nginx
systemctl restart nginx
systemctl status nginx
```

#### MySQL

```shell
sudo systemctl start mysql
sudo systemctl stop mysql
sudo systemctl restart mysql
sudo systemctl status mysql
```

#### phpMyAdmin

```shell
sudo docker start phpmyadmin
sudo docker stop phpmyadmin
sudo docker restart phpmyadmin
sudo docker stats pgadmin
```

#### MongoDB

```shell
sudo systemctl start mongo
sudo systemctl stop mongo
sudo systemctl restart mongo
sudo systemctl status mongo
```

#### adminMongo

```shell
sudo docker start adminmongo
sudo docker stop adminmongo
sudo docker restart adminmongo
sudo docker stats adminmongo
```

#### Docker

```shell
sudo systemctl start docker
sudo systemctl restart docker
sudo systemctl stop docker
sudo systemctl status docker
```

#### Docker-compose 服务

```
#创建容器编排
sudo docker-compose up

#创建容器编排并重建有变化的容器
sudo docker-compose up -d

#启动/重启
sudo docker-compose start
sudo docker-compose stop
sudo docker-compose restart
```

#### Redis

```shell
systemctl start redis
systemctl stop redis
systemctl restart redis
systemctl status redis
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

1. 通过 SFTP 将网站目录（*/data/wwwroot/*）**压缩后**再完整的下载到本地
2. 通过 phpMyAdmin 逐个导出数据库
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

### Python升级

对 Python 来说，大版本之间有较大的差异，官方表示没有升级的方案，只能安装更高的版本，可以实现多版本共存。

## 故障处理

此处收集使用 Python 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### Python服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
systemctl status python
journalctl -u python
```

#### 执行 django 启动命令报错？

错误信息：You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

解决方案：运行下面的命令后再启动项目  

```
python manage.py migrate
```

#### `pip install uwgsi` 报错？

错误信息如下：  
```
ERROR: Command errored out with exit status 1:
     command: /usr/bin/python3 -u -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-v02o0o80/uwsgi_6afc0c5595704f599e64e6aa41047052/setup.py'"'"'; __file__='"'"'/tmp/pip-install-v02o0o80/uwsgi_6afc0c5595704f599e64e6aa41047052/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /tmp/pip-record-oovzq0ap/install-record.txt --single-version-externally-managed --compile --install-headers /usr/local/include/python3.6m/uwsgi
```

错误原因：  
解决方案：  


## 常见问题

#### Python 运行环境中是否支持多个 Python 版本？

除了操作系统自带的 Python2 之外，默认安装了 Python3.x 中的版本之一。  
用户可以自由安装更多的 Python3.x 版本，然后使用虚拟隔离环境，可以方便的安装应用而互不影响。

#### 终端中输入 `python` 命令为何显示的版本是 2.7？

部分云平台默认已经安装 Python2，且设置为默认版本。

#### Python 默认字符编码是什么？

For python2.x, default encoding is ASCII   
For python3.x, default encoding is UTF-8  

#### Python 包是否可以被编译成二进制文件？

可以。建议使用 pyinstaller 或 cpython 这两种工具之一

#### Python 有哪些解释器？

| **Implementation** | **Virtual Machine**        | **Compatible Language** |
| ------------------ | -------------------------- | --------------------------- |
| [CPython](http://www.python.org/) (default)  | CPython VM                 | C                           |
| [Jython](https://www.jython.org/)             | JVM                        | Java                        |
| [IronPython](http://ironpython.net/)         | CLR                        | C#                          |
| Brython            | Javascript engine(e.g. V8) | JavaScript                  |
| RubyPython         | Ruby VM                    | Ruby                        |
| [PyPy](http://pypy.org)               | PyPy Executable            | JIT                         |
| [PythonNet](http://pythonnet.github.io/)          | PythonNet Executable            | .NET                         |

> 其中 CPython 是官方默认的解释器。

#### Python 解释器是如何工作的？

In a CPython interpreter, bytecode is fed to PVM (Python Virtual Machine) which is responsible for running your code.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/python-interpreter-websoft9.png)

#### 本项目中 Python 采用何种安装方式？

采用 RPM/Deb 包的安装方式

#### 如果没有域名是否可以部署 Python 应用？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：*http://服务器公网IP:9090*

#### 是否可以修改Python的源码路径？

可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R apache.apache /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```
