---
sidebar_position: 100
slug: /influxdb
tags:
  - Web 面板
  - 可视化
  - GUI
---

# 快速入门

InfluxDB 介绍

部署 Websoft9 提供的 InfluxDB 之后，请参考下面的步骤快速入门。

## 准备{#prepare}

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 InfluxDB 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问 InfluxDB，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## InfluxDB 初始化向导{#wizard}

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入初始化页面

2. 完成初始化工作

### 碰到问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

**InfluxDB 能打开，但总是出现 502 错误？**  

参阅：

## InfluxDB 使用入门{#quickstart}

下面以 **××××** 作为一个任务，帮助用户快速入门：

## InfluxDB 常用操作{#guide}

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数

2. 填写 InfluxDB 邮件相关配置

3. 测试邮件发送是否可用

### 安装插件{#plugin}

### 重置管理员密码{#resetpw}

忘记管理员密码时，请参考如下方案重置密码：  

### 域名额外配置（修改 URL）{#dns}

**[域名五步设置](./administrator/domain_step)** 完成后，需设置 InfluxDB 的 URL:  

1. 步骤1

2. 步骤2

### HTTPS 额外设置{#https}

**[标准 HTTPS 配置](./administrator/domain_https)** 完成后，可能还需要如下步骤： 

1. 步骤1

2. 步骤2

## 参数{#parameter}

通过运行 `docker ps`，查看 InfluxDB 运行时所有的服务组件：   

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

**[通用参数表](./administrator/parameter)** 获取组件的路径、服务、端口等参数，InfluxDB 自身的参数列出如下：   

### 路径{#path}

InfluxDB 配置文件： *path/config.php*    

### 端口{#port}

除 80, 443 等常见端口需开启之外，以下端口可能会用到：  

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 8080   | InfluxDB 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |

### 版本{#version}

控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats influxdb
```

### 命令行{#cli}

### API{#api}