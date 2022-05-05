---
sidebar_position: 3
slug: /graylog/admin
tags:
  - Graylog
  - 日志管理
  - 数据分析
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

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

## 故障排除

除以下列出的 Graylog 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案：

#### 登录后告警和错误提示 ？

**现象 1**：提示 There is a node without any running inputs. This means ... ？
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-nofiinput-websoft9.png)
**原因**：这只是一个当前没有 input 的提醒，并非错误。  
**方案**：新建一个本地的 input，即可消除此提醒

**现象 2**：提示 Index rotation strategy null not found... ?  
**原因**：磁盘可用空间低于 15% 的时候，会出现这个问题  
**方案**：释放冗余的文件或者增加服务器磁盘空间

## 常见问题

#### Graylog 架构原理图？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-arch-websoft9.png)

#### Graylog 集群原理图？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/architec_bigger_setup.png)