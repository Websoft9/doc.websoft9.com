---
sidebar_position: 3
slug: /haproxy/admin
tags:
  - HAProxy
  - IT 架构
  - 中间件
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### HAProxy 升级

如果 yum/apt 更新后的版本无法满足您需求，请通过[源码编译安装](https://github.com/haproxy/haproxy/blob/master/INSTALL)您所需的版本

## 故障排除

除以下列出的 HAProxy 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 

## 问题解答

#### 如何安装的 HAProxy？

yum/apt 安装方式

#### 可否命令行修改 HAProxy 后台密码？

可以，修改配置文件`/etc/haproxy/haproxy.cfg`

#### 是否有可视化的管理工具？

默认开启 HAProxy Statistics Report 可视化界面，访问：*http://服务器公网IP:1080/haproxy* 即可