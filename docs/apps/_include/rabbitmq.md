[RabbitMQ](https://www.rabbitmq.com/) 是一个 **流行的开源消息队列系统**，它被用于 消息队列  等场景。流行的开源消息队列系统，用erlang语言开发，用于在分布式系统中存储转发消息，在易用性、扩展性、高可用性等方面表现不俗


![gui](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-gui-websoft9.png)


## 准备

在参阅本文档使用 RabbitMQ 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）RabbitMQ：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [MPL-2.0](https://opensource.org/licenses/MPL-2.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口