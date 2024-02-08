---
title: Elasticsearch
slug: /elasticsearch
tags:
  - ELK
  - 日志分析
  - 大数据
---

import Meta from './_include/elasticsearch.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Elasticsearch 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 使用本地电脑浏览器访问，进入 Elastic Stack 登录界面
   ![ELK 登录页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](./user/credentials)），成功登录到 Elastic Stack 后台  
   ![ELK 后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-bkreminder-websoft9.png)
   ![ELK 控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-dashboard-websoft9.png)

### 安装 Logstash

Elasticsearch 应用中默认不含 Logstash，可在 Websoft9 应用商店中安装或提前准确其他的 Logstash。

### 连接 Logstash 并分析

Logstash 作为数据的采集者，它是如何将数据传输到 Elasticsearch 这个数据存储中的呢？

1. 编辑 Logstash 配置文件

2. 新增一个 pipeline 的配置文件，其内容如下：
   ```
   input{
      file{
         path => "/var/log/*.log"
         type => "elasticsearch"
         start_position => "beginning"
      }
   }

   ## Add your filters / logstash plugins configuration here

   output {
      elasticsearch {
         hosts => "elasticsearch:9200"
         user => "elastic"
         password => "elastic123"
                  index => "mytest"
      }
   }
   ```

  > 以上配置段中的 **output** 需要使用 elasticsearch 的数据库连接账号。

3. 运行命令`curl http://URL/cat/indices?v` 验证 Elasticsearch 和 Logstash 的连接，索引是否生效

4. 登陆 Kibana，点击【Manage】，再点击右侧菜单的【Index Patterns】

   ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard1-websoft9.png)

   ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard2-websoft9.png)

   ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard3-websoft9.png)

5. 检索"mytest"，根据提示完成创建

   ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard4-websoft9.png)

   ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard5-websoft9.png)

6. 索引在 Kibana 创建成功，可以用时间戳在此检索数据

   ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard6-websoft9.png)

   ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard7-websoft9.png)

## 配置选项{#configs}

- Kibana 配置文件：*/path/kibana/config/kibana.yml*   
- Elasticsearch 配置文件：*/path/elasticsearch/config/elasticsearch.yml*  
- Logstash 配置文件：*/path/logstash/pipeline/logstash.conf*  
- [SQL CLI](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-cli.html)
- [Elasticsearch API](https://www.elastic.co/guide/en/elasticsearch/reference/current/http-clients.html)
- 多语言（✅）：Kibana 配置文件中增加 `i18n.locale: "zh-CN"`
- 开源许可：[ELASTIC-LICENSE](https://github.com/elastic/elasticsearch/blob/master/licenses/ELASTIC-LICENSE-2.0.txt)

## 管理维护{#administrator}

### 配置 SMTP

Elasticsearch 配置 SMTP 发邮件的步骤：：

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数

2. 登录 Elasticsearch 控制台，依次打开：【Stack Management】>【Watcher】，增加一个 [Email Action](https://www.elastic.co/guide/en/elasticsearch/reference/current/actions.html)

3. 编辑 Elasticsearch 的配置文件，增加 [Email 配置](https://www.elastic.co/guide/en/elasticsearch/reference/current/actions-email.html)

### 修改密码

登录 Kibana 后，右上角用户图标的【用户配置文件】即可修改密码

### 重置密码

修改编排文件 `.env` 中的 **DB_ES_PASSWORD** 变量即重置密码

### 备份与恢复

Elastic 内置快照备份功能（参考：[官方文档](https://www.elastic.co/guide/en/elasticsearch/reference/7.13/snapshot-restore.html)）

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-backupsp-websoft9.png)

## 故障

#### Logstash 无法输出到 ES？

检查 Logstash 的 pipeline 配置文件中 Elasticsearch 账号密码是否正确

#### Elasticsearch 无法登陆？

如果现实下面的错误信息，即表明磁盘空间不足。  
```
kibana_task_manager_7.17.4_001/_mapping?timeout=60s error: [cluster_block_exception]: index [.kibana_task_manager_7.17.4_001] blocked by: [TOO_MANY_REQUESTS/12/disk usage exceeded flood-stage watermark, index has read-only-allow-delete block];,"}
```

ES 对磁盘空间有较高的要求，建议准备足够的空间。 

## 常见问题

#### Elastic 具体包含哪些应用？

“Elastic Stack” 是三个开源项目的缩写：Elasticsearch，Logstash 和 Kibana。

- Elasticsearch 是一个存储数据和检索数据等数据库
- Logstash 是数据提取、清洗和整理的中间件
- Kibana 是 Elasticsearch 的可视化管理分析界面，Kibana 依赖 Elasticsearch，不能单独运行

另外，随着 Elastic 公司不断发展，他们把更多的产品加入到了 ELK 家族，例如：一个日志采集工具 Beats

下面是 Elastic Stack 用于日志场景的典型架构图

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-arch001-websoft9.png)

#### Elastic 认证机制是什么？

Elastic 的[安全](https://elasticstack.blog.csdn.net/article/details/100548174)是由 x-pack 所提供的。在 7.0 版本之前，这个是商用的版本，需要进行安装，并购买。从 Elastic Stack 7.0 之后，x-pack 都已经在发布版中，只需配置即可。

Elasticsearch 配置文件中启动下面的项，即开启账号密码认证。

```
xpack.security.enabled: true
```

Elasticsearch 镜像支持用户名和密码的环境变量，因此非常方便设置。   

Elasticsearch 设置认证后，Kibana 和 Logstash 对应的认证处理方式如下：

- Kibana：镜像提供 **ELASTICSEARCH_USERNAME** 和 **ELASTICSEARCH_PASSWORD** 两个环境变量参数

#### Elasticsearch 全部免费吗？

Elasticsearch 由之前的开源版+商业扩展包 xpack 组成。其中 xpack 基本功能免费，需要使用全部功能可以向官方申请 30 天的免费试用期，试用期结束后回归到基本功能或订阅。  
