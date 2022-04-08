---
sidebar_position: 1
slug: /rabbitmq
tags:
  - RabbitMQ 
  - IT 架构
  - 中间件
---

# 快速入门

[RabbitMQ](https://www.rabbitmq.com) 是 AMQP（高级消息队列协议）的标准实现，用 erlang 语言开，用于在分布式系统中存储转发消息，在易用性、扩展性、高可用性等方面表现不俗。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-gui-websoft9.png)

部署 Websoft9 提供的 RabbitMQ 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:15672** 端口已经开启
3. 在服务器中查看 RabbitMQ 的 **[默认账号和密码](./setup/credentials)**  
4. 若想用域名访问  RabbitMQ，务必先完成 **[域名五步设置](./dns#domain)** 过程

## RabbitMQ 安装向导

### 详细步骤

1. 本地电脑浏览器访问网址：*http://域名:15672* 或 *http://服务器公网:15672*, 进入初始化页面

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](./setup/credentials)），成功登录到 RabbitMQ 后台  

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-bk-websoft9.png)

3. 登录后通过：【Users】>【Admin】>【Permissions】>【Update this user】设置新密码  

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-pw-websoft9.png)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。


## RabbitMQ 使用入门

下面以 **收发消息** 作为一个任务，帮助用户快速入门：


## RabbitMQ 常用操作

下面以 Rabbimtq [官方文档](https://www.rabbitmq.com/documentation.html)为基础，提炼一些常用的操作供用户参考：  

### 创建用户

我们可以把RabbitMQ想象成一个数据库系统，默认提供的 admin 账号就是最高管理员权限的账号。  

`admin` 既是登录 RabbitMQ Web界面的账号，同时也是 RabbitMQ 服务的账号。

通过Web界面我们可以创建更多的账号：

1. 登录 RabbitMQ 后台，依次打开：【Admin】>【Add a user】

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-createuser-websoft9.png)

3. 设置好用户名和密码，以及tag（用户角色，必填项）

### 远程连接

用户可以通过本地的 MQ 工具连接 RabbitMQ 服务器。下面以 [QueueExplorer](https://www.cogin.com/mq/index.php) 这款客户端工具为例进行说明：

1. 下载并安装 [QueueExplorer](https://www.cogin.com/mq/download.php)

2. 开启云控制台服务器安全组 **TCP:5672** 和 **TCP:15672** 端口

3. 打开客户端，填写配置信息
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/queueexplorer-rabbtimq001-websoft9.png)

3. 连接成功

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/queueexplorer-rabbtimq002-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/queueexplorer-rabbtimq003-websoft9.png)


### 配置TLS/SSL

RabbitMQ对外提供服务时，为保证通信的安全性，通常使用SSL/TLS加密通信。  

RabbitMQ 配置TLS/SSL，需要以下4个步骤：

1. 安装证书生成工具 tls-gen

    ```bash
    git clone https://github.com/michaelklishin/tls-gen tls-gen
    cd tls-gen/basic
    # private key password
    make PASSWORD=bunnies
    make verify
    make info
    ls -l ./result
    cp -r result/ /etc/rabbitmq/ssl/  
    ```

2. 追加下面内容到配置文件 `/etc/rabbitmq/rabbitmq.config`

    ```
    ssl_options.cacertfile = /etc/rabbitmq/ssl/ca_certificate.pem
    ssl_options.certfile   = /etc/rabbitmq/ssl/server_certificate.pem
    ssl_options.keyfile    = /etc/rabbitmq/ssl/server_key.pem
    ssl_options.verify     = verify_peer
    ssl_options.fail_if_no_peer_cert = false
    ```

3. 重启服务 `systemctl restart rabbitmq`

4. 验证
    ```bash
    rabbitmq-diagnostics listeners
    ```

## 参数

RabbitMQ 应用中包含 Docker 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。

下面仅列出 RabbitMQ 本身的参数：

### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 15672   | 通过 HTTP 访问 RabbitMQ 控制台 | 可选   |
| 5672 | RabbitMQ 连接端口 | 可选   |
| 4369 | Erlang distribution | 可选   |


### 版本

```shell
# erlang  Version
yum info erlang
apt show erlang

# RabbitMQ version
rabbitmqctl status | grep RabbitMQ*
```

### 服务

```shell
sudo systemctl start | stop | restart | status rabbitmq-server
rabbitmq-server console
```

### 命令行

```
# RabbitMQ CLI
rabbitmqctl 

# Erlang debug
erl
```

### API

[Client Documentation](https://www.rabbitmq.com/dotnet-api-guide.html)





