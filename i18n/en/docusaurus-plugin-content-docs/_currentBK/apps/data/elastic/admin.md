---
sidebar_position: 3
slug: /elastic/admin
tags:
  - ELK Stack
  - Data Analysis
---

# ELK Stack Maintenance

This chapter is special guide for ELK Stack maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### ELK Stack Backup and Restore

ELK 内置快照备份功能（Refer to[官方文档](https://www.elastic.co/guide/en/elasticsearch/reference/7.13/snapshot-restore.html)）

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-backupsp-websoft9.png)

### ELK Stack Upgrade

## Troubleshoot{#troubleshoot}

In addition to the ELK Stack issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### Logstash 无法输出到 Elasticsearch？

检查 Logstash 的 pipeline 配置文件中 Elasticsearch 账号密码是否正确

## FAQ{#faq}

#### How can I enable the debug mode of ELK service?

```
systemctl stop elk-server
elk-server console
```

#### Can I reset password of ELK by command?

Yes, e.g `elkctl change_password  admin newpassword`

#### ELK 具体包含哪些应用？

“ELK” 是三个开源项目的缩写：Elasticsearch，Logstash 和 Kibana。 Elasticsearch 是搜索和分析引擎。

- Elasticsearch 是一个存储数据和检索数据等数据库
- Logstash 是数据提取、清洗和整理的中间件
- Kibana 是 Elasticsearch 的可视化管理分析界面

另外，随着 Elastic 公司不断发展，他们把更多的产品加入到了 ELK 家族，例如：一个日志采集工具 Beats

下面是 ELK 用于日志场景的典型架构图

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-arch001-websoft9.png)

#### ELK 认证机制是什么？

Elastic Stack 的[安全](https://elasticstack.blog.csdn.net/article/details/100548174)是由 x-pack 所提供的。在 Elastic Stack 7.0 版本之前，这个是商用的版本，需要进行安装，并购买。从 Elastic Stack 7.0 之后，x-pack 都已经在发布版中，所以不需要进行安装。我们只需要进行配置就可以了。

Elasticsearch 配置文件中启动下面的项，即开启账号密码认证。

```
xpack.security.enabled: true
```

Elasticsearch 镜像支持用户名和密码的环境变量，因此非常方便设置。 Elasticsearch 设置认证后，Kibana 和 Logstash 对应的认证处理方式如下：

- Kibana：镜像提供 **ELASTICSEARCH_USERNAME** 和 **ELASTICSEARCH_PASSWORD** 两个环境变量参数
- Logstash：

#### ELK 是否支持多语言？

支持，只需在 Kibana 配置文件中增加 `i18n.locale: "zh-CN"` 即可

#### ELK 采用何种安装方式？

采用 [官方 Docker 镜像](https://github.com/elastic/dockerfiles) 安装方式

#### ELK 采用哪种开源许可？

[ELASTIC-LICENSE](https://github.com/elastic/elasticsearch/blob/master/licenses/ELASTIC-LICENSE-2.0.txt)

#### Elasticsearch 全部免费吗？

Elasticsearch 由之前的开源版+商业扩展包 xpack 组成。其中 xpack 基本功能免费，需要使用全部功能可以向官方申请 30 天的免费试用期，试用期结束后回归到基本功能或订阅。  
