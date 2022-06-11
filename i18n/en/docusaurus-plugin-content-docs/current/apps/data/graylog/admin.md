---
sidebar_position: 3
slug: /graylog/admin
tags:
  - Graylog
  - Data Analysis
  - Log Management
---

# Graylog Maintenance

This chapter is special guide for Graylog maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Graylog 集群

我们知道，Graylog 运行时，包括如下软件：

- Graylog 日志采集、分析
- ElasticSearch 日志存储
- MongoDB 系统配置系统

Graylog 支持如下最简答的部署方式：  
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-minisetup-websoft9.png)

也支持复杂的[集群](https://docs.graylog.org/v1/docs/multinode-setup)部署：  
![Graylog 集群部署架构图](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-hasetup-websoft9.png)

其中，MongoDB 实际上可以不做集群。

> 更多信息参考官方的[架构指南](https://www.slideshare.net/Graylog/graylog-engineering-design-your-architecture)

### Backup and Restore

### Upgrade

## Troubleshoot{#troubleshoot}

In addition to the Graylog issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### 登录后告警和错误提示 ？

**现象 1**：提示 There is a node without any running inputs. This means ... ？
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-nofiinput-websoft9.png)
**原因**：这只是一个当前没有 input 的提醒，并非错误。  
**方案**：新建一个本地的 input，即可消除此提醒

**现象 2**：提示 Index rotation strategy null not found... ?  
**原因**：磁盘可用空间低于 15% 的时候，会出现这个问题  
**方案**：释放冗余的文件或者增加服务器磁盘空间

## FAQ{#faq}

#### Graylog Architecture?

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-arch-websoft9.png)

#### Graylog HA deployment?

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/architec_bigger_setup.png)