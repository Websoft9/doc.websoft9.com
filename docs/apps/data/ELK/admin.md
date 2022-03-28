---
sidebar_position: 3
slug: /elk/admin
tags:
  - ELK Stack
  - 日志管理
  - 数据分析
---

# 维护指南

## 场景

### 备份与恢复

ELK 内置快照备份功能（阅读[官方文档](https://www.elastic.co/guide/en/elasticsearch/reference/7.13/snapshot-restore.html)）

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-backupsp-websoft9.png)

## 故障速查

除以下列出的 ELK 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。

#### Logstash 无法输出到 Elasticsearch？

检查 Logstash 的 pipeline 配置文件中 Elasticsearch 账号密码是否正确

## 常见问题

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

#### 本项目中 ELK 采用何种安装方式？

采用[官方提供 Docker 安装](https://github.com/elastic/dockerfiles)方式

#### ELK 采用哪种开源许可？

[ELASTIC-LICENSE](https://github.com/elastic/elasticsearch/blob/master/licenses/ELASTIC-LICENSE-2.0.txt)

#### Elasticsearch 全部免费吗？

Elasticsearch 由之前的开源版+商业扩展包 xpack 组成。其中 xpack 基本功能免费，需要使用全部功能可以向官方申请 30 天的免费试用期，试用期结束后回归到基本功能或订阅。

#### 如果没有域名是否可以部署 ELK？

可以，访问`http://服务器公网IP` 即可

#### 是否可以修改 ELK 的源码路径？

可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R nginx.nginx /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```
