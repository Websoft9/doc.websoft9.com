---
sidebar_position: 3
slug: /knowage/admin
tags:
  - Knowage
  - 大数据分析
  - BI
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

## 故障排除

除以下列出的 Knowage 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。

## 问题解答

#### Knowage 支持多语言吗？

支持，但不包含中文

#### 采用哪种方式安装 Knowage？

本项目采用官方的 Docker 镜像安装，同时预设了持久化存储

#### Knowage 与 SpagoBI 有什么关系？

Knowage 是 SpagoBI 更名后的产品

#### 如果没有域名是否可以部署 Knowage？

可以，直接通过： *http://服务器公网 IP:8080/knowage* 或 *http://服务器公网 IP* 访问即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置 phpMyAdmin，访问地址： *http://服务器公网 IP:9090*

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R knowage.knowage /data/wwwroot/knowage
# 读写执行权限
find /data/wwwroot/knowage -type d -exec chmod 750 {} \;
find /data/wwwroot/knowage -type f -exec chmod 640 {} \;
```
