---
sidebar_position: 7
slug: /administrator/firewall
---

# 防火墙与安全组

## 关于防火墙

在 Linux 中，防火墙是以一个守护进程的方式存在，服务的名字是 firewalld ，它能够定义一组规则来控制外部传入系统中的网络访问。  

虽然与 Linux 防火墙流行的工具有：[firewalld](https://firewalld.org/)、iptables 和 nftables，但 firewalld 功能最为强大，它甚至支持图形化。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/firewalld-gui-websoft9.png)

## 安全组设置{#security}

但是为了简化安全使用，云平台通过一个可视化的管理界面--**安全组**，来实现与防火墙的同等功能。  

所以，一般使用云服务器的时候会关闭防火墙，用安全组替代它。不同的云平台安全组操作有一定的差异：  

* [Azure 安全组设置](../azure#securitygroup)
* [AWS 安全组设置](../aws#securitygroup)
* [阿里云 安全组设置](../alibabacloud#securitygroup)
* [腾讯云 安全组设置](../tencentcloud#securitygroup)
* [华为云 安全组设置](../huaweicloud#securitygroup)

## 问题解答

#### 如何判断端口是否放通？

除了检查本机防火墙和云控制台安全组之外，可以通过 **telnet** 去连接
