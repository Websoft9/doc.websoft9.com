---
sidebar_position: 2
slug: /administrator/upgrade_app
---

# 应用程序升级

应用程序除了自身通过 CLI 或在线升级方式之外，

## 在线升级

在线升级是利用应用程序自身的 CLI 或控制台界面提供的升级工具（或插件）的一种简单可靠的升级方式。  

具体需要参考[应用中心](../apps)各个应用的章节。  

## 手工升级

本节，只介绍基于 Docker 部署的应用的升级流程（通用型强）：拉取镜像 > 删除容器 > 重建容器

> 升级之前请确保您已经完成了服务器的镜像（快照）备份

1. 修改 Docker 应用的根目录 [.env 文件](../administrator/parameter)中的版本号

2. 拉取目标版本的镜像
   ```
   cd /data/wwwroot/appname
   docker-compose pull
   ```
   > 如果显示没有镜像可拉取，则无需升级

3. 删除旧容器，重新创建 appname 容器
    ```
    docker-compose down
    docker-compose up -d
    ```