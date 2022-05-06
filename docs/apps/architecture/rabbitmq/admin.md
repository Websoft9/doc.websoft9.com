---
sidebar_position: 1
slug: /rabbitmq/admin
tags:
  - RabbitMQ 
  - IT 架构
  - 中间件
---

# 维护参考


## 场景

### RabbitMQ 升级

[Upgrading RabbitMQ](https://www.rabbitmq.com/upgrade.html)

## 故障排除

除以下列出的 RabbitMQ 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 

#### RabbitMQ 远程连接失败？

远程连接失败，请检查如下几点：

* 是否开启云控制台上的安全组**TCP:5672**和**TCP:15672**端口

* 创建的RabbitMQ 账号是否分配角色（下图的test用户由于没有分配角色，导致它无法远程连接）

  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-createusererror-websoft9.png)

#### RabbitMQ 服务无法启动？

1. 以调试模式运行 `rabbitmq-server console`，便可以查看启动状态和错误
   ```
   rabbitmq-server console
   ```
2. 打开日志文件：*/data/logs/rabbitmq-server*，检索 **failed** 关键词，分析错误原因


#### 在Chrome下修改密码后报错？

这个并不是服务器端的问题，只要更新浏览器即可。

![chrome error of RabbitMQ](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-chromeerror-websoft9.png)

## 问题解答

#### 如何以调试模式启动RabbitMQ服务？

```
systemctl stop rabbitmq-server
rabbitmq-server console
```

#### 如何用命令行修改 RabbitMQ 后台密码？

可以，`rabbitmqctl change_password  admin newpassword`