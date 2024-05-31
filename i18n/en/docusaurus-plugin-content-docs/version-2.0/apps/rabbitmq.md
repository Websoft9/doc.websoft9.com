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

### 初始化{#wizard}

Websoft9 控制台安装 RabbitMQ 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

1. 本地电脑浏览器访问后，进入初始化页面

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-login-websoft9.png)

2. 输入账号密码，成功登录到 RabbitMQ 后台  

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-bk-websoft9.png)

3. 登录后通过：【Users】>【Admin】>【Permissions】>【Update this user】设置新密码  

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-pw-websoft9.png)


### 创建用户

`admin` 既是登录 RabbitMQ Web界面的账号，同时也是 RabbitMQ 服务的账号。  

通过Web界面我们可以创建更多的账号：

1. 登录 RabbitMQ 后台，依次打开：【Admin】>【Add a user】

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-createuser-websoft9.png)

2. 设置好用户名和密码，以及tag（用户角色，必填项）

### 远程连接

用户可以通过本地的 MQ 工具连接 RabbitMQ 服务器。下面以 [QueueExplorer](https://www.cogin.com/mq/index.php) 这款客户端工具为例进行说明：

1. 下载并安装 [QueueExplorer](https://www.cogin.com/mq/download.php)

2. 打开客户端，填写配置信息（端口根据实际情况填写）   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/queueexplorer-rabbtimq001-websoft9.png)

3. 连接成功

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/queueexplorer-rabbtimq002-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/queueexplorer-rabbtimq003-websoft9.png)


### 配置TLS/SSL

RabbitMQ 配置TLS/SSL，需要以下4个步骤：

1. 安装证书生成工具 [tls-gen](https://github.com/michaelklishin/tls-gen)

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

3. 重启 RabbitMQ 服务后生效

4. 验证
    ```bash
    rabbitmq-diagnostics listeners
    ```

## 配置选项{#configs}

- 容器端口说明

  | 端口号 | 用途                                          | 必要性 |
  | ------ | --------------------------------------------- | ------ |
  | 15672   | 通过 HTTP 访问 RabbitMQ 控制台 | 必选   |
  | 5672 | RabbitMQ 连接端口 | 可选   |
  | 4369 | Erlang distribution | 可选   |

- 命令行：rabbitmqctl
- [API](https://www.rabbitmq.com/dotnet-api-guide.html)

## 管理维护{#administrator}

### 升级

[Upgrading RabbitMQ](https://www.rabbitmq.com/upgrade.html)

### 修改密码

运行命令 `rabbitmqctl change_password  admin newpassword` 即可


## 故障

#### RabbitMQ 远程连接失败？

远程连接失败，请检查如下几点：

* 安全组对应的端口是否开启

* 创建的RabbitMQ 账号是否分配角色（下图的test用户由于没有分配角色，导致它无法远程连接）

  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-createusererror-websoft9.png)

#### RabbitMQ 服务无法启动？

以调试模式运行 `rabbitmq-server console`，便可以查看启动状态和错误

#### 在Chrome下修改密码后报错？

这个并不是服务器端的问题，只要更新浏览器即可。

![chrome error of RabbitMQ](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-chromeerror-websoft9.png)