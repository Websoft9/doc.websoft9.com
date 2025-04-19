---
sidebar_position: 3
slug: /private-cloud
---

# 私有云安装

Websoft9 支持在 [Proxmox VE](https://www.proxmox.com/), Microsoft Hyper-V, VMware vSphere, OpenStack 等各种不同的私有云解决方案中部署。

## 准备

为了能够更好的使用私有云，需要提前准备资源或知识储备：

- 架设好裸金属服务器（或工作站），并确保可以在内网访问它。同时，它可以访问互联网下载软件包

- 进入服务器自带的管理平台，熟悉其操作。主流的服务器厂商的服务器管理控制台软件的名称

   - Dell OpenManage
   - HPE OneView
   - Lenovo XClarity
   - Inspur Server Manager

- 准备虚拟机镜像

  - 理解 ISO, img, OVA, OVF, VHD 等镜像格式的差异
  - 准备镜像下载地址。例如：[Ubuntu Server ISO 安装包](https://ubuntu.com/download/server), [Ubuntu Cloud Images](https://cloud-images.ubuntu.com/)

  
## Proxmox 虚拟化实践{#proxmox}

Proxmox（[官方文档](https://pve.proxmox.com/pve-docs/index.html)） 是一个开源产品，它支持 Linux 和 Windows，并有完善的多语言。

### 安装 Proxmox 到裸金属服务器

1. 在裸金属服务器上下载 [Proxmox 安装包](https://www.proxmox.com/en/downloads)，然后通过服务器厂商的管理控制台安装 Proxmox。  

2. 安装完成后，相当于在裸金属服务上部署了 **一个轻量级 Linux（宿主机） + Proxmox 虚拟机管理软件**

3. 登录到 Proxmox 控制台，完成必要配置，根据参考举例：

   - 进入 **数据中心 > 主节点 > 更新 > 存储库**，点击 **添加** 按钮，创建一个 **No-Subscription** 软件仓库以便后续升级
   

### 下载虚拟机镜像

Proxmox 支持通过控制台在线下载镜像，也支持上传镜像。

1. 录到 Proxmox 控制台，进入 **数据中心 > 存储**，编辑名称为 **local** 存储，勾选所有的内容，确保它可以支持各种镜像源

2. 然后，打开 **数据中心 > 管理节点 > local**
   
   - 其中的 **ISO 镜像**标签页，通过 **从 URL 下载** 或 **上传** 的方式，下载 ISO 或 img 镜像
   - 其中的 **CT 模板**标签页，可以在线下载容器镜像
   - 其中的 **导入**标签页，通过 **从 URL 下载** 或 **上传** 的方式，下载 OVA 镜像

### 创建虚拟机