---
sidebar_position: 1
slug: /elastic
tags:
  - ELK Stack
  - 日志管理
  - 数据分析
---

# 快速入门

[ELK Stack](https://www.elastic.co/cn/elastic-stack/) 是 Elastic Stack 的简称，由 Elasticsearch、Kibana、Beats 和 Logstash 等开源软件组成。Elastic Stack 能够获取任何来源、任何格式的数据，然后对数据进行搜索、分析和可视化。Elastic Stack 适用于各种用例，不管是日志，还是你能想到的任何项目，无一不能胜任。

![ELK Stack](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-gui-websoft9.gif)

部署 Websoft9 提供的 Elastic Stack 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网 IP 地址**
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **80** 和 **9200** 端口是否开启
3. 在服务器中查看 ELK 的 **[默认账号和密码](./user/credentials)**
4. 若想用域名访问 ELK **[域名五步设置](./administrator/domain_step)** 过程
5. 登录云服务器，运行下面的命令，拉取 Elastic 相关 Docker 镜像并启动容器

   ```
   cd /data/apps/elastic && docker compose pull && docker compose up -d
   ```

   > Elastic Stack 开源版本 License 不允许第三方的分发行为，但允许用户免费使用。因此，用户使用本方案部署 Elastic Stack，请先执行上述命令自行拉取 Elastic Stack 镜像。  

## Elastic Stack 初始化向导

### 详细步骤

1. 使用本地电脑浏览器访问网址： *http://域名* 或  *http://服务器公网 IP*, 进入 Elastic Stack 登录界面
   ![ELK 登录页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](./user/credentials)），成功登录到 Elastic Stack 后台  
   ![ELK 后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-bkreminder-websoft9.png)
   ![ELK 控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-dashboard-websoft9.png)

> 需要了解更多 Elastic Stack 的使用，请参考官方文档：[ELK Documentation](https://www.elk.com/documentation.html)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或 **[FAQ](./faq#setup)** 尝试快速解决问题。

## Elastic Stack 入门向导

Elastic Stack 的数据源多种多样，这里用常见的日志文件为 Logstash 的输入为例，步骤如下：

1. 在 [Logstash 的配置文件](#path)中设置索引"mytest"，并重启容器
   ```
   input{
      file{
         path => "/var/log/yum.log"
         type => "elasticsearch"
         start_position => "beginning"
      }
   }

   output {
      elasticsearch {
         hosts => "elasticsearch:9200"
         user => "elastic"
         password => "xxxxx"
                  index => "mytest"
      }
   }
   ```

   ```
   cd /data/apps/elastic
   docker-compose down
   docker-compose up -d
   ```

2. 验证 Elasticsearch 和 Logstash 是否成功连接，索引数据是否生效(通过 URL 验证：http://服务器公网 IP:9200/cat/indices?v)

  ![ELK 验证](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizardindex-websoft9.png)

3. 登陆 Kibana，点击【Manage】，再点击右侧菜单的【Index Patterns】

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard1-websoft9.png)

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard2-websoft9.png)

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard3-websoft9.png)

4. 检索"mytest"，根据提示完成创建

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard4-websoft9.png)

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard5-websoft9.png)

5. 索引在 Kibana 创建成功，可以用时间戳在此检索数据

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard6-websoft9.png)

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard7-websoft9.png)

## Elastic Stack 常用操作

### Logstash 连接 Elasticsearch

Logstash 作为数据的采集者，它是如何将数据传输到 Elasticsearch 这个数据存储中的呢？

1. 编辑 [Logstash 配置文件](#path)

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

### 配置 SMTP

Elastic Stack 配置 SMTP 发邮件的步骤：：

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数

2. 登录 Elastic Stack 控制台，依次打开：【Stack Management】>【Watcher】，增加一个 [Email Action](https://www.elastic.co/guide/en/elasticsearch/reference/current/actions.html)

3. 编辑 Elasticsearch 的配置文件，增加 [Email 配置](https://www.elastic.co/guide/en/elasticsearch/reference/current/actions-email.html)

### 重置密码

常用的 Elastic Stack 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码

登录 Kibana 后，右上角用户图标的【用户配置文件】即可修改密码

#### 找回密码

如果用户忘记了密码，需通过重新运行容器的方式重置密码：

```
cd /data/apps/elastic
docker-compose down && docker-compose up -d
```

`.env`文件中的 **DB_ES_PASSWORD** 变量即重置后的密码

## Elastic Stack 参数

Elastic Stack 应用中包含 Nginx, Docker 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 Elastic Stack 运行时所有的 Container：

```
CONTAINER ID   IMAGE                  COMMAND                  CREATED         STATUS         PORTS                                                                                                                                                                        NAMES
4c27ee6b8e98   logstash:7.13.4        "/usr/local/bin/dock…"   4 minutes ago   Up 4 minutes   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp, 0.0.0.0:5044->5044/tcp, :::5044->5044/tcp, 0.0.0.0:9600->9600/tcp, 0.0.0.0:5000->5000/udp, :::9600->9600/tcp, :::5000->5000/udp   elastic-logstash
babdf8193e8d   kibana:7.13.4          "/bin/tini -- /usr/l…"   4 minutes ago   Up 4 minutes   0.0.0.0:9001->5601/tcp, :::9001->5601/tcp                                                                                                                                    elastic-kibana
de14eb80b9f9   elasticsearch:7.13.4   "/bin/tini -- /usr/l…"   4 minutes ago   Up 4 minutes   0.0.0.0:9200->9200/tcp, :::9200->9200/tcp, 0.0.0.0:9300->9300/tcp, :::9300->9300/tcp
```

### 路径{#path}

Elastic Stack 包含：Elasticsearch, Kibana, Logstash 等组件

Elastic Stack 安装目录： */data/apps/elastic*  
Elastic Stack 配置目录： */data/apps/elastic/src*  
Logstash 配置文件： */data/apps/elastic/src/logstash/pipeline/logstash.conf*  
Kibana 配置文件： */data/apps/elastic/src/kibana/config/kibana.yml*   
Elasticsearch 配置文件： */data/apps/elastic/src/elasticsearch/config/elasticsearch.yml*  

### 端口{#port}

| 端口号 | 用途                                         | 必要性 |
| ------ | -------------------------------------------- | ------ |
| 9200   | Elasticsearch HTTP | 必须   |
| 9600   | Logstash API | 可选   |

### 版本

```shell
docker exec -it elastic-elasticsearch bin/elasticsearch --version
```

### 服务

```shell
sudo docker  start | stop | restart | status elastic-elasticsearch
sudo docker  start | stop | restart | status elastic-logstash
sudo docker  start | stop | restart | status elastic-kibana 
```

### 命令行

[SQL CLI](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-cli.html)

### API

[ELK API](https://www.elastic.co/guide/en/elasticsearch/reference/current/http-clients.html) 采用 REST API 2.0 规范。
