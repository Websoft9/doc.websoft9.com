---
sidebar_position: 3
slug: /elastic/admin
tags:
  - ELK Stack
  - 日志管理
  - 数据分析
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### 备份与恢复

Elastic Stack 内置快照备份功能（阅读[官方文档](https://www.elastic.co/guide/en/elasticsearch/reference/7.13/snapshot-restore.html)）

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-backupsp-websoft9.png)

## 故障排除

除以下列出的 ELK 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。

#### Logstash 无法输出到 Elasticsearch？

检查 Logstash 的 pipeline 配置文件中 Elasticsearch 账号密码是否正确

#### Elastic Stack 无法登陆？

如果现实下面的错误信息，即表明磁盘空间不足。  
```
kibana_task_manager_7.17.4_001/_mapping?timeout=60s error: [cluster_block_exception]: index [.kibana_task_manager_7.17.4_001] blocked by: [TOO_MANY_REQUESTS/12/disk usage exceeded flood-stage watermark, index has read-only-allow-delete block];,"}
```

ES 对磁盘空间有较高的要求，建议准备足够的空间。  

## 常见问题

#### Elastic Stack 具体包含哪些应用？

“Elastic Stack” 是三个开源项目的缩写：Elasticsearch，Logstash 和 Kibana。 Elasticsearch 是搜索和分析引擎。

- Elasticsearch 是一个存储数据和检索数据等数据库
- Logstash 是数据提取、清洗和整理的中间件
- Kibana 是 Elasticsearch 的可视化管理分析界面

另外，随着 Elastic 公司不断发展，他们把更多的产品加入到了 ELK 家族，例如：一个日志采集工具 Beats

下面是 Elastic Stack 用于日志场景的典型架构图

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-arch001-websoft9.png)

#### Elastic Stack 认证机制是什么？

Elastic Stack 的[安全](https://elasticstack.blog.csdn.net/article/details/100548174)是由 x-pack 所提供的。在 Elastic Stack 7.0 版本之前，这个是商用的版本，需要进行安装，并购买。从 Elastic Stack 7.0 之后，x-pack 都已经在发布版中，所以不需要进行安装。我们只需要进行配置就可以了。

Elasticsearch 配置文件中启动下面的项，即开启账号密码认证。

```
xpack.security.enabled: true
```

Elasticsearch 镜像支持用户名和密码的环境变量，因此非常方便设置。 Elasticsearch 设置认证后，Kibana 和 Logstash 对应的认证处理方式如下：

- Kibana：镜像提供 **ELASTICSEARCH_USERNAME** 和 **ELASTICSEARCH_PASSWORD** 两个环境变量参数
- Logstash：

#### Elastic Stack 是否支持多语言？

支持，只需在 Kibana 配置文件中增加 `i18n.locale: "zh-CN"` 即可

#### Elastic Stack 采用何种安装方式？

采用 [官方 Docker 镜像](https://github.com/elastic/dockerfiles) 安装方式

#### Elastic Stack 采用哪种开源许可？

[ELASTIC-LICENSE](https://github.com/elastic/elasticsearch/blob/master/licenses/ELASTIC-LICENSE-2.0.txt)

#### Elasticsearch 全部免费吗？

Elasticsearch 由之前的开源版+商业扩展包 xpack 组成。其中 xpack 基本功能免费，需要使用全部功能可以向官方申请 30 天的免费试用期，试用期结束后回归到基本功能或订阅。  
