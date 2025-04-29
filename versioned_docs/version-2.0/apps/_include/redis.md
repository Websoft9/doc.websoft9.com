[Redis](https://redis.io/) 是一个 **高性能、实时 key-value 数据库**，它被用于 缓存数据库  等场景。Redis是一个开源的使用ANSI C语言编写、支持网络、可基于内存亦可持久化的日志型、Key-Value数据库，并提供多种语言的API。


![login](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redis/redisinsight-login-websoft9.png)


## 准备

在参阅本文档使用 Redis 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Redis：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [redis](https://redis.io/legal/licenses/) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口