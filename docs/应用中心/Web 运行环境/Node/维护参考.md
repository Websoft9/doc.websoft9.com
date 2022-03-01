---
sidebar_position: 2
slug: /nodejs/admin
tags:
  - Node.js
  - Node
  - 运行环境
---


# 维护参考

## 系统参数

Node.js 预装包包含 Node.js 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

接下来我们对路径信息进行准确的说明

#### Node.js

除Node.js之外，本部署方案还包括：NPM,Yarn,PM2,Express等组件  

Node.JS 模块目录: */usr/lib/node_modules*  
Node.js 应用安装目录: */data/wwwroot*  
Express 示例目录: */data/wwwroot/express.example.com*  
Node.JS 日志文件: */root/.pm2/pm2.log*  

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*

**default.conf** 默认存在一个 [server（虚拟主机）](https://support.websoft9.com/docs/linux/zh/webs-nginx.html#虚拟主机) 配置项，对应的就是 **示例网站**
```
server {
    listen 80;
    server_name _;
    location / {
        proxy_pass  http://127.0.0.1:3000;
        proxy_redirect     off;
        proxy_set_header   Host             $host;
        proxy_set_header   X-Real-IP        $remote_addr;
        proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
        proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
        proxy_max_temp_file_size 0;
        proxy_connect_timeout      90;
        proxy_send_timeout         90;
        proxy_read_timeout         90;
        proxy_buffer_size          4k;
        proxy_buffers              4 32k;
        proxy_busy_buffers_size    64k;
        proxy_temp_file_write_size 64k;
   }
   include extra/*.conf;
}
```

> 有多少个网站，就需要在 default.conf 中增加同等数量的 server 配置项

#### MongoDB

MongoDB 配置文件: */etc/mongod.conf*  
MongoDB 数据目录: */data/mongo*  
MongoDB 日志文件: */var/log/mongodb/mongod.log*

#### MySQL

MySQL 安装目录: *usr/local/mysql*  
MySQL 配置文件: *etc/my.cnf*   
MySQL 数据目录：*/data/mysql*   
MySQL 日志文件: */var/log/mysql/mysqld.log*   
MySQL PIN: */run/mysqld/mysqld.pid*   
MySQL Socket: */var/lib/mysql/mysql.sock*

#### Docker

本部署环境默认已安装Docker，Docker主要用于部署下面两个数据库可视化管理工具：

* phpMyAdmin on Docker，通过：*http://服务器公网IP:9090* 端口访问
* adminMongo on Docker，通过：*http://服务器公网IP:9091* 端口访问

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp`查看相关端口，下面列出本应用可能要用到的端口：

| 类型 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 80/443 | Nginx, 通过 HTTP 访问 Express 框架 | 可选 |
| TCP | 9090 | 通过 HTTP 访问 phpMyAdmin | 可选 |
| TCP | 9091 | 通过 HTTP 访问 adminMongo | 可选 |
| TCP | 27017 |MongoDB 端口 | 可选 |
| TCP | 6379 | Redis 端口 | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Linux Version
lsb_release -a

# Node.js  Version
node -v

# PM2  Version
pm2 -V

# NPM version
npm -v

# yarn version
yarn --version

# MongoDB version
mongo --version

# Nginx version
nginx -v

# List Installed Nginx Modules
nginx -V

# MySQL version
mysql -V

# Redis version
redis-server -v

# Docker version
docker -v
```

### 服务

使用由Websoft9提供的 Node.js 部署方案，可能需要用到的服务如下：

#### PM2

```shell
systemctl start pm2-root
systemctl stop pm2-root
systemctl restart pm2-root
systemctl status pm2-root
```

#### Nginx

```shell
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
```

#### MongoDB

```shell
systemctl start mongod
systemctl stop mongod
systemctl restart mongod
systemctl status mongod
```

#### MySQL

```shell
sudo systemctl start mysql
sudo systemctl stop mysql
sudo systemctl restart mysql
sudo systemctl status mysql
```

#### Redis

```shell
systemctl start redis
systemctl stop redis
systemctl restart redis
systemctl status redis
```

#### Docker

```shell
sudo systemctl start docker
sudo systemctl restart docker
sudo systemctl stop docker
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

1. 通过WinSCP将网站目录（*/data/wwwroot*）**压缩后**再完整的下载到本地
2. 分别导出数据库
3. 备份工作完成


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

### Node.js升级

#### Upgrade NPM

When you install node.js, npm is automatically installed. However, npm gets updated more frequently than Node.js, so be sure that you have the latest version.

```shell
#view the version of NPM
npm -v

#install the latest official, tested version of npm.
npm install npm@latest -g

#install a version that will be released in the future
npm install npm@netx -g

# upgrade node.js
npm install -g n
n stable
```

#### Upgrade PM2

```shell
npm install pm2@latest -g
```

## 故障处理

此处收集使用 Node.js 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### NPM 如何防止权限错误

如果您在尝试全局安装软件包时看到`EACCES`错误，[参考](https://www.npmjs.com.cn/getting-started/fixing-npm-permissions/)

#### 如果 NMP 坏了
用下列命令重装

```shell
curl -L https://www.npmjs.org/install.sh | sh
```

使用Windows，请下载并重新安装。[注意事项]（https://www.npmjs.com.cn/troubleshooting/try-the-latest-stable-version-of-npm#upgrading-on- windows）。

#### 清除 npm 缓存
有时 npm 的缓存会混淆。 您可以使用以下方法重置它：

```shell
npm cache clean
```

## 常见问题

#### 默认字符集是什么？
UTF-8

#### What's different between YARN and NPM?

[Yarn](https://yarnpkg.com/en/) 是在NPM之后推出的一个包管理解决方案

| npm | yarn |
| ---: | :--- |
| npm install | yarn |
| npm install react --save | yarn add react |
| npm uninstall react --save | yarn remove react |
| npm install react --save-dev | yarn add react --dev |
| npm update --save | yarn upgrade |

#### Nginx 虚拟主机配置文件是什么？

虚拟主机配置文件是 Nginx 用于管理多个网站的**配置段集合**，路径为：*/etc/nginx/conf.d/default.conf*。  
每个配置段的形式为： `server{ }`，有多少个网站就有多少个配置段

#### 如何修改示例网站根目录？

待续...

#### Node.js 环境是否支持部署多个网站？

支持。每增加一个网站，只需在[Nginx 虚拟主机配置文件](/zh/stack-components.md#nginx)中增加对应的 **server{ }** 即可。

#### 如果没有域名是否可以部署 Node.js 应用？

可以，访问`http://服务器公网IP:端口号` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin 和 adminMongo

#### 如何删除9Panel?

删除 */data/apps/9panel* 下的所有数据即可，但需要保留文件夹

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R nginx.nginx /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```
#### 如果设置 HTTP 跳转到 HTTPS？

只需在网站对应的 server{} 配置段中增加规则即可：
```
 if ($scheme != "https") 
    {
    return 301 https://$host$request_uri;
    }
```

#### 如何启用或禁用 Nginx 模块？

不支持模块启用或关闭
