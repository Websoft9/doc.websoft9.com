---
sidebar_position: 3
slug: /grafana/admin
tags:
  - Grafana
  - 大数据分析
  - BI
---

# 维护指南

## 场景

除以下列出的 Grafana 维护场景问题之外， [管理员指南](../administrator) 专题提供了通用的维护方案：

### Grafana升级

请参考官方提供的升级文档：[Upgrading Grafana](https://grafana.com/docs/installation/upgrading/)

## 故障速查

除以下列出的 Grafana 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。

## 问题解答

#### Grafana支持哪些数据源？

官方支持以下数据源:Graphite，InfluxDB，OpenTSDB，Prometheus，Elasticsearch，CloudWatch 和 KairosDB。

#### Grafana数据库连接配置信息在哪里？

数据库配置信息在Grafana安装目录下的 */usr/share/grafana/conf/defaults.ini* 中

#### Grafana 是否提供CLI工具？

SSH登录服务器，即可运行 grafana-cli。功能非常强大，包括配置系统、修改密码等
```
# 修改管理员密码
grafana-cli admin reset-admin-password admin123
```

#### 如果没有域名是否可以部署 Grafana？

可以，访问`http://服务器公网IP` 即可