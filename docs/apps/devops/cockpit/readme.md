---
sidebar_position: 100
slug: /cockpit
tags:
  - Web 面板
  - 可视化
  - GUI
---

# 快速入门

Cockpit 是 RedHat 维护的 Linux 服务器面板工具。它具备很强的开放能力，可以集成各种应用到面板的菜单上，如果善于使用它，你会发现它就是容器时代最好的面板之一。 

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cockpit/cockpit-gui-websoft9.png)

部署 Websoft9 提供的 Cockpit 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:9099** 端口已经开启
4. 若想用域名访问  Cockpit，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## Cockpit 初始化向导{#wizard}

### 详细步骤

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## Cockpit  使用入门{#quickstart}

## 常用操作{#guide}

## 参数

Cockpit 应用中包含 Nginx, Docker 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。  

下面仅列出 Cockpit 本身的参数：

### 路径{#path}

### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9099   | Cockpit 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


### 版本

```shell

```

### 服务

```shell
sudo systemctl start | stop | restart | status cockpit
```

### 命令行

### API

