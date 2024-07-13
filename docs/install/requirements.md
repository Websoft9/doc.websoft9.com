---
sidebar_position: 1
slug: /install-requirements
title: 要求
---

# 安装要求

此页面包含有关支持的操作系统以及安装和使用 Websoft9 所需的服务端最低要求的信息。


## 服务器规格{#server}

- Websoft9 控制台最低要求1核2G，考虑应用所需的资源，综合建议2核4G
- Websoft9 自身程序以及依赖环境大约 1.5 G，考虑用户增加多个应用，建议磁盘空间不低于 20 G
- Websoft9 安装应用时需连接镜像仓库，请确保具有 Internet 网络访问，并且带宽不低于 100M/s。

## 操作系统{#os}

Websoft9 支持在 Red Hat, CentOS, Debian, Ubuntu 等[主流 Linux 发行版](https://websoft9.github.io/websoft9/version.json)上安装。

> 暂不支持 Windows 和 macOS 等操作系统  

## 域名{#domain}

域名不是 Websoft9 运行的必要条件。但如果没有域名，应用访问会受限，建议为应用配置域名。    

Websoft9 支持[全局域名](../domain-set#wildcard)。它一次设置后，所有应用均可使用。  


## 软件

Python 是安装 Websoft9 的必选项，所需版本：Python 3.8 以上 + pip。  

其他组件均通过在线安装脚本自动安装。   

## 客户端浏览器

我们在主流的浏览器中都进行了兼容性测试：

- Chrome
- Edge
- Firefox

## 相关阅读

- [规划整体基础设施](../design-infrastructure)
- [规划带宽和流量](../brandwith-infra)
- [扩充或优化存储](../storage)




