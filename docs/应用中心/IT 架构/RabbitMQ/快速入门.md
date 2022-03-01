---
sidebar_position: 1
slug: /rabbitmq
tags:
  - RabbitMQ 
  - IT 架构
  - 中间件
---

# 快速入门

[RabbitMQ](https://www.rabbitmq.com) 流行的开源消息队列系统，用erlang语言开，是AMQP（高级消息队列协议）的标准实现。用于在分布式系统中存储转发消息，在易用性、扩展性、高可用性等方面表现不俗。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-gui-websoft9.png)

在云服务器上部署 RabbitMQ 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:15672** 端口是否开启
3. 若想用域名访问 RabbitMQ，请先到 **域名控制台** 完成一个域名解析

## 账号密码

使用RabbitMQ，可能会用到的几组账号密码如下：

### RabbitMQ

管理员账号: `admin`  
管理员密码: `admin` 或 存储在您的服务器中的文件中 */credentials/password.txt*  

运行 `cat /credentials/password.txt` 命令，可以查看其中内容  

> 本地浏览器访问：http://服务器公网IP:15672 即可打开RabbitMQ 控制台

## RabbitMQ 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名:15672* 或 *http://Internet IP:15672*, 进入初始化页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](#账号密码)），成功登录到 RabbitMQ 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-bk-websoft9.png)

3. 登录后通过：【Users】>【Admin】>【Permissions】>【Update this user】设置新密码  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-pw-websoft9.png)

> 需要了解更多 RabbitMQ 的使用，请参考官方文档：[RabbitMQ Documentation](https://www.rabbitmq.com/documentation.html)


## 常用操作

### 配置

参考官方方案：https://www.rabbitmq.com/configure.html

### 创建用户

我们可以把RabbitMQ想象成一个数据库系统，默认提供的admin账号就是最高管理员权限的账号。admin既是登录RabbitMQ Web界面的账号，同时也是RabbitMQ服务的账号。

通过Web界面我们可以创建更多的账号：

1. 本地浏览器Chrome or Fixfox 访问：http://服务器公网IP:15672，登录RabbitMQ后台
2. 依次打开：【Admin】>【Add a user】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-createuser-websoft9.png)
3. 设置好用户名和密码，以及tag（用户角色，必填项）

### 远程连接

用户可以通过本地的MQ工具连接RabbitMQ服务器。下面以[QueueExplorer](https://www.cogin.com/mq/index.php)这款客户端工具为例进行说明：

1. 下载并安装[QueueExplorer](https://www.cogin.com/mq/download.php)
2. 开启云控制台服务器安全组**TCP:5672**和**TCP:15672**端口
3. 打开客户端，填写配置信息
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/queueexplorer-rabbtimq001-websoft9.png)
3. 连接成功
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/queueexplorer-rabbtimq002-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/queueexplorer-rabbtimq003-websoft9.png)

如何远程连接失败，请检查如下几点：

* 是否开启云控制台上的安全组**TCP:5672**和**TCP:15672**端口
* 创建的RabbitMQ账号是否分配角色（下图的test用户由于没有分配角色，导致它无法远程连接）
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-createusererror-websoft9.png)


### 配置TLS/SSL

RabbitMQ配置TLS/SSL，需要以下4个步骤：

1. 安装tls-gen

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

2. 追加下面内容到配置文件`/etc/rabbitmq/rabbitmq.config`
```
ssl_options.cacertfile = /etc/rabbitmq/ssl/ca_certificate.pem
ssl_options.certfile   = /etc/rabbitmq/ssl/server_certificate.pem
ssl_options.keyfile    = /etc/rabbitmq/ssl/server_key.pem
ssl_options.verify     = verify_peer
ssl_options.fail_if_no_peer_cert = false
```
3. 重启服务`systemctl restart rabbitmq`

4. 验证
```bash
rabbitmq-diagnostics listeners
```

## 异常处理

#### 浏览器打开IP地址，无法访问 RabbitMQ（白屏没有结果）？

您的服务器对应的安全组15672端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### RabbitMQ 服务启动失败？

暂无


