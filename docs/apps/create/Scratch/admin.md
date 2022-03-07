---
sidebar_position: 2
slug: /scratch/admin
tags:
  - Scratch
  - 少儿编程
---

# 维护参考

## 系统参数

Scratch 预装包包含 Scratch 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### Scratch

Scratch 项目目录： */data/wwwroot/scratch*  
Scratch 静态页面目录： */data/wwwroot/scratch/build*  

> Scratch 基于Node开发，可以通过修改Node.js后再次构建发布

#### Node.js

NPM 路径: */usr/lib/node_modules/npm*  
Module 全局路径：*/usr/lib/node_modules/npm/node_modules*
Node 可执行文件路径：*usr/bin*

#### Nginx

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx/*

#### MYSQL

暂无数据库

### 端口号

下面是您在使用本镜像过程中，需要用到的端口号，请通过 [云控制台安全组](https://support.websoft9.com/docs/faq/zh/tech-instance.html)进行设置

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过http访问Scratch | 必须 |
| HTTPS | 443 | 通过https访问Scratch | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Node.js Version
node --version

# Nginx version:
nginx -v

```

### 服务

使用由Websoft9提供的Scratch部署方案，可能需要用到的服务如下：


#### Nginx

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

1. 通过WinSCP将网站目录（*/data/wwwroot/scratch-gui*）**压缩后**再完整的下载到本地
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


### Scratch升级

Scratch的升级是通过NPM来实现的，通过SSH工具，依次运行如下命令：

```
cd /data/wwwroot/scratch-gui
npm install https://github.com/LLK/scratch-gui.git
npm run build

```

## 故障处理


此处收集使用 Scratch 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### Scratch 访问很慢？

Scratch首次加载数据超过20M。例如：您使用的是2M带宽，那么理想情况下的加载时间为：20000k/(128k/s×2)=78s。显然，如果带宽不足，速度会非常慢。


## 常见问题

#### Scratch支持多语言吗？

支持多语言（包含中文），系统默认根据浏览器自动选择语言，并可以实时切换 

#### Scratch 支持用户注册和登录吗？

暂时不支持

#### scratch-www 项目 和 scratch-gui 项目 有什么区别？

[scratch-www](https://github.com/LLK/scratch-www)  = [scratch-gui](https://github.com/LLK/scratch-gui)  + 分享社区，现在 scratch-www 用户登录功能还在开发中

#### 如果没有域名是否可以部署 Scratch？

可以，访问`http://服务器公网IP` 即可

#### 是否可以修改Scratch的源码路径？

可以，通过修改 [Nginx 虚拟主机配置文件](/zh/stack-components.md)中相关参数

#### 如何修改上传的文件权限?

```shell
chown -R nginx.nginx /data/wwwroot
find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```