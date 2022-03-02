---
sidebar_position: 2
slug: /wdcp/admin
tags:
  - WDCP
  - DevOps
---


# 维护参考

## 系统参数

本预装包包含 WDCP 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

* 网站根目录：*/www/web*
* 备份目录：*/www/backup* 
* 日志目录：*/www/weblogs*
* 运行环境:*PHP5.4~7.1,Apache2.4,Nginx 1.8*
* PHP配置文件:*/www/wdlinux/etc/php.ini*

### 证书

nginx证书文件存储在/www/wdlinux/nginx/conf/cert目录下 
apache证书文件存储在/www/wdlinux/apache/conf/cert目录下 

> N+A环境，指定PHP版本等，只需要上传nginx的证书文件就可以 Apache引擎启用https证书时，需在“系统设置”里的“web服务端口”增加443，以及防火墙开放443端口

### 端口号

下面是您在使用本镜像过程中，需要用到的端口号，请通过 [云控制台安全组](https://support.websoft9.com/docs/faq/zh/tech-instance.html)进行设置

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 8080 | 通过http访问 WDCP| 必须 |
| HTTPS | 443 | 通过https访问 WDCP  | 可选 |
| MySQL | 3306 | 远程连接MySQL | 可选 |


### 版本号


组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Nginx Version
nginx -v

# Node.js Verison
node --version

# MongoDB Verison
mysql --version

# Dokcer:
docker --version
```

### 服务

使用由Websoft9提供的 WDCP 部署方案，可能需要用到的服务如下：

#### Nginx

```shell
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
```

#### MySQL

```shell
sudo systemctl start mysql
sudo systemctl stop mysql
sudo systemctl restart mysql
sudo systemctl status mysql
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

手工本地备份主要是通过下载应用程序文件和备份导出数据库文件，建议备份周期每月一次，备份文件保存6个月左右。下面就具体的备份操作进行说明：

1. 通过WinSCP将网站目录完整的下载到本地（如果文件数量比较多，建议压缩后再下载） 
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/winscp-download-websoft9.png)
2. 通过浏览器访问：http://公网IP/phpMyAdmin ，进入数据库管理界面)
3. 左侧菜单中选择所需的数据库，顶部导航栏上选择“导出”标签 
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)
4. 选择导出方式和格式（建议SQL），点击“执行”，导出文件后下载到本地
5. 将程序文件和数据库文件放到同一个文件夹，根据日期命名，备份工作完成

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

## 网站加速

用心留意，会发现网上关于速度问题的帖子非常多，方案也非常多。包括：数据库采用RDS，用云存储，动静分离等。经过我们大量实践之后，我们认为从两个方面改善网站访问速度：

1. 采用CDN
2. 网站图片超过1000张，建议放到对象存储中

以上方案简单可靠，降低服务器资源消耗，实现成本较低，效果好。


### 技巧1：如何不增加成本的情况提高带宽？

请采用按量带宽计费的方式（不限带宽大小）或采用CDN加速。


## 故障处理


我们收集使用 WDCP 过程中最常见的故障，供您参考：
> 服务器相关故障的诊断和解决，与云平台密切相关，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

