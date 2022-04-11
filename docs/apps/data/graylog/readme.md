---
sidebar_position: 1
slug: /graylog
tags:
  - Graylog
  - 日志管理
  - 数据分析
---

# 快速入门

[Graylog](https://graylog-server.apache.org/) 是一个基于 Java 开发的开源的日志聚合、分析、审计、展现和预警工具，它是 ELK 的替代解决方案。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/graylog/graylog-gui-websoft9.png)

## 准备

部署 Websoft9 提供的 Graylog 之后，请参考下面的步骤快速入门。

1. 在云控制台获取您的 **服务器公网 IP 地址**
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 和 **TCP:9001** 端口是否开启
3. 在服务器中查看 Graylog 的 **[默认账号和密码](./setup/credentials)**
4. 若想用域名访问 Graylog，务必先完成**[域名五步设置](./administrator/domain_step)** 过程

## Graylog 初始化向导

### 详细步骤

1. 使用浏览器访问网址： *http://域名* or *http://服务器公网 IP*，进入 Graylog 登录界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-login-websoft9.png)

2. 输入账号密码后，登入到 Graylog 控制台 ([不知道密码?](./setup/credentials))  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-console-websoft9.png)

> 需要了解更多 Graylog 的使用，请参考官方文档：[Configuring Graylog](https://docs.graylog.org/en/latest/pages/installation/docker.html)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或 **[FAQ](./faq#setup)** 尝试快速解决问题。

## Graylog 使用入门

正在编写

## Graylog 常用操作

### 配置 SMTP

Graylog 配置 SMTP 发邮件的步骤：：

1. 在邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数

2. 修改 Graylog 配置文件中的 Refer to [transport_email 参数](https://docs.graylog.org/en/3.3/pages/configuration/server.conf.html#email)

3. 重启 Graylog 后生效
   ```
   sudo docker restart graylog
   ```

### 重置密码

如果无法找回管理员密码，可以通过下面的步骤重置密码

1. 使用 SSH 工具登录服务器，运行下面的密码重置命令

   ```
   new_password=admin123@graylog
   sha_password=$(echo -n $new_password | sha256sum | awk '{ print $1 }')
   sudo sed -i "s/8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918/$sha_password/g" /data/wwwroot/graylog/.env
   ```

2. 重新运行容器编排命令，密码就被重置为 `admin123@graylog`
   ```
   cd /data/wwwroot/graylog && sudo docker-compose up -d
   ```

> 你可以将 new_password 设置为任何你想要的密码

### 配置 Graylog

针对于 Docker 安装，Graylog 每个配置选项都可以加上大写的前缀 GRAYLOG_ 实现环境变量化： 

```
version: '2'
  services:
    mongo:
      image: "mongo:4.2"
      # Other settings [...]
    elasticsearch:
      image: docker.elastic.co/elasticsearch/elasticsearch-oss:7.10.2
      # Other settings [...]
    graylog:
      image: graylog/graylog:4.2
      # Other settings [...]
      environment:
        GRAYLOG_TRANSPORT_EMAIL_ENABLED: "true"
        GRAYLOG_TRANSPORT_EMAIL_HOSTNAME: smtp
        GRAYLOG_TRANSPORT_EMAIL_PORT: 25
        GRAYLOG_TRANSPORT_EMAIL_USE_AUTH: "false"
        GRAYLOG_TRANSPORT_EMAIL_USE_TLS: "false"
        GRAYLOG_TRANSPORT_EMAIL_USE_SSL: "false"
```

同时，也支持直接修改配置文件 server.conf

## Graylog 参数

Graylog 应用中包含 Nginx, Docker, MongoDB, Elasticsearch 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 安装，Graylog 运行时所有的 Container：

```
CONTAINER ID   IMAGE                                                      COMMAND                  CREATED         STATUS                   PORTS                                                                                                                                                                                                                           NAMES
dffc0d802a26   graylog/graylog:4.1                                        "/usr/bin/tini -- wa…"   2 minutes ago   Up 2 minutes (healthy)   0.0.0.0:1514->1514/tcp, 0.0.0.0:1514->1514/udp, :::1514->1514/tcp, :::1514->1514/udp, 0.0.0.0:12201->12201/tcp, 0.0.0.0:12201->12201/udp, :::12201->12201/tcp, :::12201->12201/udp, 0.0.0.0:9001->9000/tcp, :::9001->9000/tcp   graylog
7c0a42a383c3   mongo:4.2                                                  "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes             27017/tcp                                                                                                                                                                                                                       graylog-mongo
f4cd00fc5f58   docker.elastic.co/elasticsearch/elasticsearch-oss:7.10.2   "/tini -- /usr/local…"   2 minutes ago   Up 2 minutes             9200/tcp, 9300/tcp                                                                                                                                                                                                              graylog-elasticsearch
9497147a0263   mrvautin/adminmongo                                        "docker-entrypoint.s…"   8 minutes ago   Up 3 minutes             0.0.0.0:9091->1234/tcp, :::9091->1234/tcp                                                                                                                                                                                       adminmongo
```

下面仅列出 Graylog 本身的参数：

### 路径{#path}

Graylog 安装路径:  */data/wwwroot/graylog*  
Graylog 配置文件:  */data/wwwroot/volumes/graylog/config/server.conf*  
Graylog 日志目录:  */data/wwwroot/volumes/graylog/log*

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9001   | Graylog 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |

### 版本

```shell
# Superset Version
docker images |grep graylog/graylog |awk '{print $2}'
```

### 服务

```shell
sudo docker  start | stop | restart | status graylog
sudo docker  start | stop | restart | status graylog-mongo
sudo docker  start | stop | restart | status graylog-elasticsearch
```

### 命令行

Graylog 暂未提供命令行工具

### API

[Graylog API](https://docs.graylog.org/v1/docs/rest-api) 采用 REST API 2.0 规范, 功能强大甚至 Graylog Web 界面也专门使用 Graylog REST API 与 Graylog 集群交互。

API 访问方式：*https://服务器公网IP:9001/api/api-browser/global/index.html*， 缺少 /global/index.html 是无法访问的。
