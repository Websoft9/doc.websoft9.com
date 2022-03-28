---
sidebar_position: 3
slug: /erpnext/admin
tags:
  - ERPNext
  - 企业管理
  - ERP
---

# 维护指南

## 场景

### 备份与恢复

ERPNext 提供了自动备份（计划任务）和[手动输入命令](https://frappeframework.com/docs/user/en/bench/reference/backup)的两种备份方式。

1. 登录 ERPNext 后，依次打开：【Settings】>【System Settings】
   ![ERPNext backup](https://libs.websoft9.com/Websoft9/DocsPicture/zh/erpnext/erpnext-autobk-websoft9.png)

2. 进入 ERPNext 主容器
   ```
   docker exec -it erpnext-worker-default  bash
   ```
3. 在容器中运行备份命令
   ```
   # 查询项目文件夹名称（IP 或 域名）
   ls

   # 备份
   bench --site 121.41.86.118 backup
   ```

4. 在宿主机的 Docker VOLUME 中获取备份文件。备份位置：*/var/lib/docker/volumes/docker-erpnext_sites-vol/_data/IP/private/backups*

   > 后台 Download Backups 处下载失败，原因有待研究。故，直接从上面的路径下载即可

### 升级

ERPNext 基于 Docker 部署，其升级流程：拉取镜像 > 删除容器 > 重建容器

> 升级之前请确保您已经完成了服务器的镜像（快照）备份

1. 登录服务器，删除旧容器
   ```
   docker-compose down -v
   ```
2. 编辑 */data/wwwroot/erpnext/.env* 文件，将版本变量的值修改为目标版本号

2. 拉取目标版本的镜像
   ```
   cd /data/wwwroot/erpnext
   docker-compose pull
   ```
   > 如果显示没有镜像可拉取，则无需升级

3. 重新创建 ERPNext 容器
    ```
    docker-compose up -d
    ```


## 故障速查

#### 如何查看错误日志？

ERPNext 报错后，有如下几个可以分析日志的入口：

1. ERPNext 程序运行日志：*/data/logs/erpnext*
2. 进程管理日志，运行 `systemctl status erpnext -l` 查看
3. Nginx日志：*/data/logs/nginx*

检索关键词 **Failed** 或者 **error** 查看错误

#### ERPNext服务无法启动？

1. 运行`docker status erpnext`，便可以查看启动状态和错误

2. 打开日志文件：*/data/logs/erpnext*，检索 **failed** 关键词，分析错误原因


#### 在Chrome下修改密码后报错？

这个并不是服务器端的问题，只要更新浏览器即可。

#### 运行Bench时报错 "You should not run this command as root" when run bench?

Bench只能通过frapper运行,必须先切换到此用户

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

#### Frappe，bench，ERPNext 有什么关系和区别？

ERPNext 是基于 [Frappe](https://github.com/frappe/frappe) 框架开发的免费 ERP 。而 Frappe 是一个用于快速开发JS和Python集成化应用的框架。[Bench](https://github.com/frappe/bench) 是Frappe框架体系中的 CLI 工具，用于创建和管理基于 Frappe 的应用程序。

#### ERPNext 安装的时候需要创建 site 是什么原理？

Frappe 框架主要由两个部分组成：app 和 site，app 是后端Python代码，site 是用于处理 HTTP 请求的前端部分。

#### ERPNext 支持外部数据库吗？

支持，只需在[数据库配置文件](../erpnext#path) 中添加 db_host 为外部数据库地址即可。更多数据库连接参数参考官方文档[Standard Config](https://frappeframework.com/docs/user/en/basics/site_config#mandatory-settings)

#### ERPNext 支持哪些数据库？

MariaDB 和 PostgreSQL

#### 数据库用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有可视化数据库管理工具 phpMyAdmin,访问地址：*http://服务器公网IP:9090*

#### 是否可以修改 ERPNext 的源码路径？

不建议

#### 是否有ERPNext的API文档？

有，包括Python，Javascript，Jinja API等，参考官方文档[ERPNext API](https://frappeframework.com/docs/user/en/api)

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R erpnext.erpnext /data/wwwroot/erpnext
# 读写执行权限
find /data/wwwroot/erpnext -type d -exec chmod 750 {} \;
find /data/wwwroot/erpnext -type f -exec chmod 640 {} \;
```