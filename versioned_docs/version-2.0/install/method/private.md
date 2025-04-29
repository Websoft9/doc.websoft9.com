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

  - 理解 ISO 与 img, raw, OVA, OVF, VHD 等通用镜像和虚拟机软件专有镜像格式的差异
  - ISO 镜像与其他镜像有比较大的差异，它等同于操作系统安装包
  - 准备镜像下载地址。例如：[Ubuntu Server ISO 安装包](https://ubuntu.com/download/server), [Ubuntu Cloud Images](https://cloud-images.ubuntu.com/)

  
## Proxmox 虚拟化实践{#proxmox}

Proxmox（[官方文档](https://pve.proxmox.com/pve-docs/index.html)） 是一个开源产品，它支持 Linux 和 Windows，社区提供了完善的多语言。

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

#### 基于 ISO 镜像创建

Proxmox 默认提供的便是基于 ISO 镜像创建虚拟机。启动虚拟机后，还需要进行操作系统的初始化安装。

#### 基于 OVA 镜像创建

OVA 是 VMware 虚拟化软件的专有镜像格式，它无需初始化安装，但它需要通过 Web 界面的 **local（节点）> 存储** 的 **导入** 创建虚拟机。   

> 参考文档：[Import OVA on Proxmox 8.3](https://homelab.sacentral.info/posts/import-ova-on-proxmox-8_3/)。

配置向导要关注的特殊选项包括：

- CPU 类型： lvm64
- SCSI 控制器：VMware PVSCSI
- 网络接口：VMware vmxnet3

#### 为虚拟机增加 cloud-init

1. 先通过 Proxmox 控制台创建虚拟机，并确保虚拟机安装 [cloud-init](https://cloudinit.readthedocs.io/en/latest/index.html)

2. 进行虚拟机的 **硬件** 标签页，点击 **添加 > CloudInit 设置** 增加用于存储 cloud-init 元数据的存储

3. 重启虚拟机，进入 **Cloud-Init** 标签页测试功能是否可用


