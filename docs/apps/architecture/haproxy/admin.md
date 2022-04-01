---
sidebar_position: 3
slug: /haproxy/admin
tags:
  - HAProxy
  - IT 架构
  - 中间件
---

# 维护参考

## 场景

### HAProxy 升级

如果 yum/apt 更新后的版本无法满足您需求，请通过[源码编译安装](https://github.com/haproxy/haproxy/blob/master/INSTALL)您所需的版本

## 故障速查

除以下列出的 HAProxy 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

## 问题解答

#### 如何安装的 HAProxy？

yum/apt 安装方式

#### 可否命令行修改 HAProxy 后台密码？

可以，修改配置文件`/etc/haproxy/haproxy.cfg`

#### 是否有可视化的管理工具？

默认开启 HAProxy Statistics Report 可视化界面，访问：*http://服务器公网IP:1080/haproxy* 即可