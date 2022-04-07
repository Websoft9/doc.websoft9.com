---
sidebar_position: 1
slug: /install/requirements
title: 要求
---

# 安装要求

此页面包含有关支持的操作系统以及安装和使用 Websoft9 所需的最低要求的信息。

## 操作系统

Websoft9 支持在 Red Hat, CentOS, Debian, Ubuntu 等主流 Linux 发行版上安装。

暂不支持 Windows 和 macOS 等操作系统  

## 硬件

### 虚拟化技术

不管是公有云还是私有云，甚至没有使用虚拟化的服务器都可以安装 Websoft9

* 公有云: AWS， Azure， Google Cloud， 阿里云， 腾讯云， 华为云等20多个全球主流云
* 私有云: KVM, VMware, VirtualBox, OpenStack 等主流虚拟化架构
* 物理机：HP，联想、华为、H3C，Dell 等服务器

### CPU

* CPU 架构: Linux x86-64, ARM 32/64, x86/i686
* CPU 核素：最低 1 核

### 内存

内存不少于 2 G


### 磁盘

Websoft9 自身程序以及依赖环境大约 1.5 G，考虑用户增加多个应用，建议磁盘空间不低于 20 G

### 网络

安装过程中会从 Linux 系统仓库，Docker 镜像仓库上拉取相关资源，请确保您的 Internet 网络带宽不低于 10M/s。


## 软件

提供的开源软件集成方案 由 Python 包，Shell 脚本和 JS 前端组成。

### Python

Python 是安装 Websoft9 的必选项，所需版本：Python 3.8 以上 + pip 

### Docker

Docker 19.10 以上，Docker-Compose 1.29 以上。  

如果您的服务器上没有安装 Docker，参考[ Docker 在线安装命令](../docker#install) 快速安装。  

### Git

Websoft9 在线安装过程中需要通过 Git 拉取软件包，所以 Git 是必选项。  

### Nginx (可选)

用户的应用如果需要通过域名开放给外部访问，那么像 Nginx 这种 Web Server 是必不可少的组件。  

### Ansible（可选）

Ansible 是使用 Websoft9 产品在运维过程中的一个高效率工具。  
