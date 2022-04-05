---
sidebar_position: 3
slug: /onlyofficedocs/admin
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../installation/setup/) 相关章节。

## 场景

## 故障速查

除以下列出的 ONLYOFFICE Docs 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 


## 问题解答

#### ONLYOFFICE Docs 同时连接数规则？{#onlyofficedocsmaxconn}

ONLYOFFICE Docs 同时连接数是指用户在编辑模式下打开文档的数量。  
例如，对于具有200个同时连接的许可证，一个用户可以打开200个文档，200个用户每个可以打开一个，50个用户每个可以打开4个文档等。  
以何种方式并不重要，但文档服务器只会根据您购买的许可证处理编辑请求的数量。  
超过此数量的连接以预览模式打开文档。  

#### ONLYOFFICE Docs 有哪些版本？

OnlyOffice的产品家族比较复杂，根据官方的介绍，可以分为：

* ENTERPRISE EDITION：企业版
* COMMUNITY EDITION：开源版
* DEVELOPER EDITION：开发者版本

COMMUNITY EDITION 是一个完全免费的版本。

DEVELOPER EDITION 和 ENTERPRISE EDITION 是收费版本，Websoft9 可以帮助用户采购收费版本，最少 10% 的折扣。  