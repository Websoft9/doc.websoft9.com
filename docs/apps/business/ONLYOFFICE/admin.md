---
sidebar_position: 3
slug: /onlyoffice/admin
tags:
  - ONLYOFFICE Workspace
  - 企业管理
  - CRM
---

# 维护指南

## 场景

### 备份与恢复


### 升级

ONLYOFFICE 采用 [Docker 部署](https://github.com/ONLYOFFICE/Docker-CommunityServer#upgrading-onlyoffice-community-server)，其升级流程：拉取镜像 > 删除容器 > 重建容器

> 升级之前请完成服务器的快照备份，以防不测。

1. 使用 SSH 登录服务，进入到 ONLYOFFICE 目录后，拉取最新版本镜像
   ```
   cd /data/wwwroot/onlyoffice
   sudo docker-compose pull
   ```
   > 系统会自动拉取最新版镜像，如果没有镜像可拉取，则无需更新

2. 停止并删除当前的 ONLYOFFICE 容器

   ```
   sudo docker-compose down -v
   ```

3. 重新创建 ONLYOFFICE 容器
    ```
   docker-compose up -d
   ```


## 故障速查

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### ONLYOFFICE 服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看容器服务
sudo docker inspect onlyofficecommunityserver
sudo docker logs onlyofficecommunityserver
```

#### 修改 MySQl 数据库密码之后 ONLYOFFICE 无法启动？

修改密码之后需要需改 ONLYOFFICE docker-compose 文件中对应的数据库密码： */data/wwwroot/onlyoffice/docker-compose.yml*，然后运行如下命令：

```
cd /data/wwwroot/onlyoffice
docker-compose down -v
docker-compose up -d
```

#### ONLYOFFICE 显示502错误？

首先通过命令 `sudo docker logs onlyofficecommunityserver`，查看是否有错误日志。  

一般是由文件权限不足或数据连接问题导致。

#### 重新安装了数据库导致 ONLYOFFICE 无法运行？

ONLYOFFICE 对数据库的配置有严格的要求，保证符合如下要求：

```
echo "[mysqld]
sql_mode = 'NO_ENGINE_SUBSTITUTION'
max_connections = 1000
max_allowed_packet = 1048576000
group_concat_max_len = 2048
log-error = /var/log/mysql/error.log" > /app/onlyoffice/mysql/conf.d/onlyoffice.cnf
```

## 问题解答

#### ONLYOFFICE 是否支持中文？

支持，可以在线切换多种语言

#### Community Edition vs Enterprise Edition？

参考官方说明 [Compare Community Edition and Enterprise Edition](https://github.com/ONLYOFFICE/CommunityServer#compare-community-edition-and-enterprise-edition)

#### 能否介绍 ONLYOFFICE 各种版本的关系？

OnlyOffice的产品家族比较复杂，根据官方的介绍，可以分为：

* ENTERPRISE EDITION：企业版
* COMMUNITY EDITION：开源版
* INTEGRATION EDITION：比如集成了 ownCloud 的版本
* DEVELOPER EDITION：开发者版本

其中每一个版本都是由：Community Server, Document Server, Mail Server 组成。  

COMMUNITY EDITION 是一个完全免费的版本。DEVELOPER EDITION 是适用于开发者的[收费版本](https://www.onlyoffice.com/zh/developer-edition-prices.aspx)。

#### ONLYOFFICE 开源版并发连接数有限制吗？

并发连接数不超过20个（Up to 20 Simultaneous connections）

#### ONLYOFFICE Document Server 同时连接数是如何规定的？

ONLYOFFICE Document Server 同时连接数是指用户在编辑模式下打开文档的数量。  
例如，对于具有200个同时连接的许可证，一个用户可以打开200个文档，200个用户每个可以打开一个，50个用户每个可以打开4个文档等。  
以何种方式并不重要，但文档服务器只会根据您购买的许可证处理编辑请求的数量。  
超过此数量的连接以预览模式打开文档。  

#### 数据库密码可以修改吗？

可以，但是修改后需要同步修改 ONLYOFFICE docker-compose 文件，然后通过 docker-compose 重新运行容器。

#### 如果没有域名是否可以部署 ONLYOFFICE？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：*http://服务器公网IP:9090*

#### 如何禁止外界访问phpMyAdmin？

服务器安全组中关闭 9090 端口即可

#### 是否可以修改ONLYOFFICE的源码路径？

不可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R onlyoffice.onlyoffice /data/wwwroot/onlyoffice
# 读写执行权限
find /data/wwwroot/onlyoffice -type d -exec chmod 750 {} \;
find /data/wwwroot/onlyoffice -type f -exec chmod 640 {} \;
```
