---
title: RabbitMQ
slug: /rabbitmq
tags:
  - RabbitMQ 
  - IT 架构
  - 中间件
---

import Meta from './_include/rabbitmq.md';

<Meta name="meta" />

## 入门指南{#guide}

### 登录后台{#wizard}

1. Websoft9 控制台安装 RabbitMQ 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

2. 登录成功后，会进入 RabbitMQ 控制台界面
   ![](./assets/rabbitmq-backend-websoft9.png)

### 远程连接

RabbitMQ 默认已开启远程连接，但通过本地客户端（例如：[QueueExplorer](https://www.cogin.com/mq/index.php)）访问 RabbitMQ 服务时，需注意：

- 远程访问的端口务必开放
- 登录账号需设置 **Tags**（相当于分配角色）

### 创建用户

RabbitMQ 控制台支持创建用户，需要注意的是创建用户是，务必给用户设置 **Tags** 




## 配置选项{#configs}

- 配置文件目录（已挂载）：*/etc/rabbitmq/conf.d*
- 多用户（√）：控制台增加
- 容器端口：
  - 15672：RabbitMQ 控制台
  - 5672：AMQP 端口
  - 4369：Erlang 端口
- 命令行：`rabbitmqctl`
- [API](https://www.rabbitmq.com/dotnet-api-guide.html)

## 管理维护{#administrator}

### 容器内配置 TLS/SSL

RabbitMQ 配置TLS/SSL，需要以下4个步骤：

1. 将申请好的证书下载到 RabbitMQ 容器的 `/etc/rabbitmq/ssl` 目录

2. 配置文件 `/etc/rabbitmq/rabbitmq.config`

    ```
    ssl_options.cacertfile = /etc/rabbitmq/ssl/ca_certificate.pem
    ssl_options.certfile   = /etc/rabbitmq/ssl/server_certificate.pem
    ssl_options.keyfile    = /etc/rabbitmq/ssl/server_key.pem
    ssl_options.verify     = verify_peer
    ssl_options.fail_if_no_peer_cert = false
    ```

3. 重启 RabbitMQ 应用后生效

### 升级

[Upgrading RabbitMQ](https://www.rabbitmq.com/upgrade.html)

### 重置密码

在 RabbitMQ 容器中，运行命令 `rabbitmqctl change_password  admin newpassword`


## 故障