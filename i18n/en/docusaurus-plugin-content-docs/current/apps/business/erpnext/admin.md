---
sidebar_position: 3
slug: /erpnext/admin
tags:
  - ERPNext
  - 企业管理
  - ERP
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

### 备份

#### 方法一：自动备份（计划任务）

1. 登录 ERPNext 后，依次打开：【Settings】>【System Settings】
   ![ERPNext backup](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-autobk-websoft9.png)

2. 等待计划任务执行


#### 方法二：命令行备份

[手动输入命令](https://frappeframework.com/docs/user/en/bench/reference/backup)也可以备份 ERPNext：

1.. 进入 ERPNext 主容器
   ```
   docker exec -it erpnext-worker-default  bash
   ```
2. 在容器中运行备份命令
   ```
   # 查询项目文件夹名称（IP 或 域名）
   ls

   # 备份
   bench --site 121.41.86.118 backup
   ```

#### 获取备份文件

备份文件存储 ERPNext 的持久存储中。

   > 后台 Download Backups 处下载失败，原因有待研究。故，直接从上面的路径下载即可

## 故障排除

除以下列出的 ERPNext 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 

#### 在Chrome下修改密码后报错？

这个并不是服务器端的问题，只要更新浏览器即可。

#### 运行 Bench 时报错 "You should not run this command as root" when run bench?

Bench 只能通过 frapper 运行,必须先切换到此用户

```shell
su - frapper
```

#### ERPNext 安装向导最后一步出现错误提示？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-wizarderror-websoft9.png)

原因：未知   
方案：重复安装几次直至成功   


## 问题解答

#### 本项目中 ERPNext 采用何种安装方式？

采用 Docker 安装，查看我们提供的 [Docker-Compose for ERPNext](https://github.com/Websoft9/docker-erpnext) 开源项目

#### ERPNext 支持非 Docker 安装方式吗？

支持，具体的安装大致流程如下：

1. 使用Bench命令初始化一个Frappe框架
2. 安装ERPNext app
3. 创建一个名称同样为 ERPNext 的site
4. 将site与app 连接起来

#### Frappe，bench，ERPNext？

ERPNext 是基于 [Frappe](https://github.com/frappe/frappe) 框架开发的免费 ERP 。而 Frappe 是一个用于快速开发JS和Python集成化应用的框架。[Bench](https://github.com/frappe/bench) 是Frappe框架体系中的 CLI 工具，用于创建和管理基于 Frappe 的应用程序。

#### ERPNext 安装时创建 site 是什么原理？

Frappe 框架主要由两个部分组成：app 和 site，app 是后端Python代码，site 是用于处理 HTTP 请求的前端部分。

#### ERPNext 支持哪些数据库？

MariaDB 和 PostgreSQL


#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R erpnext.erpnext /data/wwwroot/erpnext
# 读写执行权限
find /data/wwwroot/erpnext -type d -exec chmod 750 {} \;
find /data/wwwroot/erpnext -type f -exec chmod 640 {} \;
```