---
sidebar_position: 1
slug: /install/requirements
title: 要求
---

# 安装要求

此页面包含有关支持的操作系统以及安装和使用 Websoft9 所需的最低要求的信息。

## 操作系统{#os}

Websoft9 支持在 Red Hat, CentOS, Debian, Ubuntu 等[主流 Linux 发行版](https://websoft9.github.io/websoft9/version.json)上安装。

> 暂不支持 Windows 和 macOS 等操作系统  

## 域名{#domain}

域名不是 Websoft9 运行的必要条件，但没有域名，应用访问会造成比必要的麻烦，故建议配置域名。    

Websoft9 支持**泛解析的域名**。一次设置后，所有应用均可使用。  

> 泛解析通过 A 记录的一种类型，它主要是以 * 替代部分或全部的主机记录。  

假设您有 abc.com 这个域名，下面是使用泛解析的几个范例：

| 类型 | 主机记录（域名前缀） | 记录值（服务器 IP） | 结果                                                         |
| -------- | -------------------- | ------------------- | ------------------------------------------------------------ |
| A        | *                    | 47.92.175.172       | 以 abc.com 结尾的域名可用，例如：n1.abc.com, n2.abc.com ...  |
| A        | *.test               | 47.92.175.172       | 以 test.abc.com 结尾的域名可用。例如：n1.test.abc.com, n2.test.abc.com ... |
| A        | *.test.web           | 47.92.175.172       | 以 test.web.abc.com 结尾的域名可用。例如：n1.test.web.abc.com, n2.test.web.abc.com ... |


## 浏览器

我们在主流的浏览器中都进行了兼容性测试：

- Chrome
- Edge
- Firefox

## 服务器{#hd}

### 云架构

不管是公有云还是私有云，甚至没有使用虚拟化的服务器都可以安装 Websoft9

* 公有云: AWS， Azure， Google Cloud， 阿里云， 腾讯云， 华为云等20多个全球主流云
* 私有云: KVM, VMware, VirtualBox, OpenStack 等主流虚拟化架构
* 物理机：HP，联想、华为、H3C，Dell 等服务器

### CPU

* CPU 架构: Linux x86-64, ARM 32/64, x86/i686
* CPU 核数：最低 1 核

### 内存

内存不少于 2 G

### 磁盘

Websoft9 自身程序以及依赖环境大约 1.5 G，考虑用户增加多个应用，建议磁盘空间不低于 20 G

### 网络

安装过程中会从 Linux 系统仓库，Docker 镜像仓库上拉取相关资源，请确保您的 Internet 网络带宽不低于 10M/s。

## 软件

Python 是安装 Websoft9 的必选项，所需版本：Python 3.8 以上 + pip。  

其他组件均通过在线安装脚本自动安装。   