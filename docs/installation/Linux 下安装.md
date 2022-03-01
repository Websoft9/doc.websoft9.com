---
sidebar_position: 1
slug: /install/linux
---


# Linux 下安装

Websoft9 目前仅支持在 Linux 主机下安装。  

## 环境准备

### 基础设施

#### 虚拟机

不管是公有云还是私有云，甚至没有使用虚拟化的服务器都可以安装 Websoft9

* 公有云: AWS， Azure， Google Cloud， 阿里云， 腾讯云， 华为云等20多个全球主流云
* 私有云: KVM, VMware, VirtualBox, OpenStack 等主流虚拟化架构
* 物理机：HP，联想、华为、H3C，Dell 等服务器


#### 配置

* 操作系统: Red Hat, CentOS, Debian, Ubuntu 等主流 Linux 发行版
* CPU架构: Linux x86-64, ARM 32/64, x86/i686
* 配置：CPU 不低于 1 核，内存不少于 2 G，磁盘空间不低于 20 M

#### 网络

安装过程中会从 Linux 系统仓库，Docker 镜像仓库上拉取相关资源，请确保您的 Internet 网络带宽不低于 10M/s。


### 基础组件

#### Python

Python3.8 以上，包含 pip 

#### Docker

Docker 19.10 以上，Docker-Compose 1.29 以上。  

如果您的服务器尚未安装 Docker，请使用如下命令安装它：

```
curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
curl -L "https://github.com/docker/compose/releases/download/1.29.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
ln -sf /usr/local/bin/docker-compose  /usr/bin
sudo systemctl start docker
```

#### Ansible

#### Git

#### Nginx (可选)

## 开始安装


### 脚本安装

如果您不具备以上所需的 Docker, Git, Ansible 等环境，推荐使用我们**脚本安装**。

```
sudo wget -N https://raw.githubusercontent.com/Websoft9/StackHub/main/docker-installer.sh; sudo bash docker-installer.sh -r akeneo
```

### 手动安装

1. 安装命令行工具 StackHub
      ```
   pip install stackhub
   ```
2. 使用 stackhub 安装应用

### 离线安装

针对无法访问 Internet 的政企用户或等保用户，我们即将提供了离线安装包服务。

### 个性化安装
用户朋友可能存在个性化的安装需求，例如：GitLab + Jenkins 集成为 GitOps 方案。  
我们非常乐意提供这种解决方案式的安装与集成[人工服务](../helpdesk)。  

