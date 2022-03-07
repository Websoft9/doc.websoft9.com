---
sidebar_position: 2
slug: /oracle/admin
tags:
  - Oracle Database
  - Cloude Native Database
---

# 维护参考


## 系统参数

Oracle Database 预装包包含 Oracle Database 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

Oracle Database 配置文件路径：*/u01/app/oracle/product/11.2.0/db1/network/admin/listener.ora*


### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

本应用建议开启的端口如下：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| Oracle Database | 1521 | 远程连接Oracle Database | 可选 |


### 版本号

Oracle Database 11g EX 第2版（快捷版）

### 服务

使用由 Websoft9 提供的 Oracle Database 部署方案，可能需要用到的服务如下：

##### Oracle Database

>启动数据库服务
service start oracle
>查看监听状态
在Oracle用户下执行：lsnrctl status
然后使用Oracle工具连接数据库。
>关闭数据库和监听
service stop oracle


## 备份

## 恢复


## 升级

### 系统级更新

运行一条更新命令，即可完成系统级更新：

``` shell
#For Ubuntu&Debian
apt update && apt upgrade -y

#For Centos&Redhat
yum update -y
```
> 本部署包已预配置一个用于自动更新的计划任务。如果希望去掉自动更新，请删除对应的Cron


## 故障处理

此处收集使用 Oracle Database 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)


## 常见问题