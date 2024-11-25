---
sidebar_position: 1.0
slug: /appstore-guide
---

# 使用模板一键部署应用

已经 [安装](./install) Websoft9 到云服务器，并 [登录 Websoft9 控制台](./login-console) 验证可用后，接下来便开始规划应用的部署。    

Websoft9 控制台的 **应用商店** 模块预制 200+ 个应用模板，包含：数据分析、AI、网站、企业运营、设计创作、低代码、数据库等细分领域数百个顶尖工具。  

![](./assets/websoft9-appstore.png)

本入门教程指导用户通过 Websoft9 控制台的 **应用商店** 部署模板化应用，只需单击几下即可将您的应用程序部署到您自己的云设施中。

接下来，我们分步骤介绍如何快速部署应用：

## 第1步：设置全局域名（可选）

虽然 Websoft9 支持在无域名下使用，但仍然建议先为 Websoft9 设置**全局域名**，这样今后安装每个应用都不需额外再配置域名。 

![](./assets/websoft9-settings-globaldomain.png)

详情参考相关章节：

- [为 Websoft9 设置全局域名](./domain-set#wildcard)

## 第2步：设置镜像加速地址（可选）

Websoft9 部署模板化应用时，会从 DockerHub 在线拉取镜像。 

如果服务器访问 DockerHub 存在网络问题，那么就需要为 Docker 服务端设置镜像加速地址： **Websoft9 控制台 > 设置 > 系统设置 > 镜像加速**


## 第3步：部署应用

进入 Websoft9 控制台的 **应用商店** 窗口，找到所需的应用后，即可一键部署目标应用。   



详情参考相关章节：

- [搜索 Websoft9 模板化应用](./appstore)
- [部署 Websoft9 模板化应用](./deployment#appstore)

## 第4步：访问与管理应用

部署应用后，通过 Websoft9 控制台 **我的应用** 窗口，查看所有正在部署或运行中的应用。  

每个运行中的应用，都可以通过 **应用管理** 界面查看访问信息，管理应用的生命周期。  

另外，Websoft9 内置的专业[网关](./gateway)，为应用程序提供域名绑定、HTTPS设置、安全访问与控制服务。  

详情参考相关章节：

- [获取应用的访问信息](./app-getdetail#access)
- [管理应用生命周期](./app-lifecycle)
- [配置应用域名与安全访问](./gateway)
- [设置应用的 HTTPS 访问](./domain-https)


## 第5步：重新部署

Websoft9 支持应用在运行后重新部署，并保留数据，以满足用户的个性化部署与设置。  

详情参考相关章节：

- [应用编排与个性化配置](./app-compose) 