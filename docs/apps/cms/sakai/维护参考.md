---
sidebar_position: 2
slug: /sakai/admin
tags:
  - Sakai
  - LMS
  - 在线学习系统
---



# 维护参考

## 系统参数

本预装包包含 Sakai 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### tomcat /usr/local/tomcat 

Tomcat 程序目录: */usr/local/tomcat* 

#### Sakai

Sakai 安装目录：*/usr/local/tomcat/webapps*
Sakai 配置目录: */usr/local/tomcat/sakai/sakai.properties*



#### MySQL

MySQL 存储目录：*/data/mysql*   

### 端口号

下面是您在使用本镜像过程中，需要用到的端口号，请通过 [云控制台安全组](https://support.websoft9.com/docs/faq/zh/tech-instance.html)进行设置

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过http访问Sakai| 必须 |
| HTTPS | 443 | 通过https访问 Sakai  | 可选 |
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

使用由Websoft9提供的 Sakai 部署方案，可能需要用到的服务如下：


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
通用的手动备份操作步骤如下：

1. 通过WinSCP将 **[网站目录](#sakai)** 压缩后再完整的下载到本地
2. 通过 [phpMyadmin](/快速入门.md#mysql-数据管理) 导出 Sakai 数据库
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



## 故障处理


我们收集使用 Sakai 过程中最常见的故障，供您参考：
> 服务器相关故障的诊断和解决，与云平台密切相关，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

### 数据库相关

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```
