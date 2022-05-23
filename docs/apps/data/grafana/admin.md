---
sidebar_position: 3
slug: /grafana/admin
tags:
  - Grafana
  - 大数据分析
  - BI
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### Grafana 升级

请参考官方提供的升级文档：[Upgrading Grafana](https://grafana.com/docs/installation/upgrading/)

## 故障排除

除以下列出的 Grafana 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。

## 问题解答

#### Grafana 支持哪些数据源？

官方支持以下数据源:Graphite，InfluxDB，OpenTSDB，Prometheus，Elasticsearch，CloudWatch 和 KairosDB。