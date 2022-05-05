---
sidebar_position: 3
slug: /cloudbeaver/admin
tags:
  - CloudBeaver
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

### CloudBeaver 升级

CloudBeaver 基于 Docker 部署，其升级流程：拉取镜像 > 删除容器 > 重建容器

> 升级之前请确保您已经完成了服务器的镜像（快照）备份

1. 登录服务器，编辑 */data/apps/cloudbeaver/.env* 文件，将版本变量的值修改为目标版本号

2. 拉取目标版本的镜像
   ```
   cd /data/apps/cloudbeaver
   docker-compose pull
   ```
   > 如果显示没有镜像可拉取，则无需升级

3. 删除旧容器，重新创建 CloudBeaver 容器
    ```
    docker-compose down -v
    docker-compose up -d
    ```


## 故障排除{#troubleshooting}

除以下列出的 CloudBeaver 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

## 问题解答

#### CloudBeaver 是否支持多语言？

支持（包含中文）后台直接切换语言，但目前中文语言包不完整

#### CloudBeaver 支持哪些数据库？

默认支持 

#### CloudBeaver 采用何种驱动连接数据库？

JDBC 驱动

#### CloudBeaver 是否支持创建数据库？

暂未发现此功能


#### 如何更改 CloudBeaver 的默认访问方式？

修改 **Nginx虚拟机主机文件**，将其中的 **server_name** 项 `listen 80` 修改成类似 `listen 8090` 即可
