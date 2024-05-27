---
sidebar_position: 1.0
slug: /app-getdetail
---

# 获取应用详情

应用详情是 Websoft9 托管平台上使用和维护应用时所需的必要参数，它主要通过 "我的应用" 功能界面获取。   

进入到目标应用的**应用管理**窗口后，根据需要获取如下相关的信息：

## 应用概述

- **应用ID**：自定义应用名称+随机字符，它是 Websoft9 托管平台管理应用的唯一标识
- **应用名称**：应用商店的模板名称，具有唯一性
- **应用版本**：应用的发行版本
- **应用 HTTP 端口**：应用绑定到宿主机的可访问端口


## 访问信息

访问标签页包含两个核心功能：

![](./assets/websoft9-myapps-access.png)

- **访问 URL**：应用的 URL，域名优先，无域名时显示 `http://IP:port` 
- **后台地址**：部分应用提供了登录后台的地址链接
- **绑定域名**：对域名进行增删改查，并立即生效
- **初始账号**：查看应用初始化的账号和密码（随机产生强型的密码，每个应用都不一样）

## 容器组件

容器标签页列出本应所包含的所有容器以及其状态等关键信息。同时，还提供了三个操作链接（点击图标使用）：  

![](./assets/websoft9-appmanage-containers.png)

- Logs: 容器的[实时日志](./monitor-logs)，等同于 `docker logs containerID`
- Stats：可视化的容器状态和[实时资源占用情况](./monitor-apm)
- Exec console：[进入容器运行命令行](./inner-container)

还可以查看容器端口情况，显示格式："宿主机端口：容器端口"   

## 容器数据卷

卷存即应用容器的持久化数据存储目录（Volumes），这个目录通常需要考虑做异地备份

![](./assets/websoft9-appmanage-volumes.png)

## 数据库

数据库标签页列出应用包含的主要数据库以及其连接信息。
![](./assets/websoft9-appmanage-dbdetail.png)

参考阅读：[连接和管理应用的数据库](./app-connectdb)


