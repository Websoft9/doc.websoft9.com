---
sidebar_position: 2
slug: /upgrade-app
---

# 应用程序升级

Websoft9 鼓励应用的不定期升级，以确保更好的体验的同时，减少安全隐患。

## 准备

1. 升级之前请确保您已经完成了服务器的镜像（快照）备份
2. 升级过程中，需停止服务

## 升级应用

应用程序的有多种升级手段，主要有如下两种：  

### 应用程序自带升级

部分应用程序自带的 CLI 或控制台界面、或额外的升级工具（或插件）提供了一种简单可靠的在线升级方式。  

具体需要参考[应用中心](../apps)各个应用的章节。  

### 应用编排升级

应用编排升级是通过修改应用的编排文件，然后重新拉去新的镜像部署应用的升级过程：

1. 通过 Websoft9 控制台【我的应用】，进入[应用编排](../quick/manageapp#howto-reup)界面

2. 修改 .env 和 docker-compose.yml 文件中与版本有关的参数。例如：W9_VERSION 

   > 建议参考 Websoft9 的 [docker-library](https://github.com/Websoft9/docker-library/tree/main/apps) 项目，它是 Websoft9 应用商店的安装编排文件源头。

3. 修改完成后，重建容器