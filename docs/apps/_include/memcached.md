# memcached

Memcached是一个自由开源的，高性能，分布式内存对象缓存系统。是一种基于内存的key-value存储，用来存储小块的任意数据（字符串、对象）。

简而言之，[memcached](https://www.memcached.org/) 是一个 **一个自由开源的，高性能，分布式内存对象缓存系统**，它被用于 缓存数据库  等场景


![gui](https://libs.websoft9.com/Websoft9/DocsPicture/zh/memcached/memcached-gui-websoft9.png)


## 准备

在参阅本文档使用 memcached 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [bsd3Clause](https://opensource.org/licenses/BSD-3-Clause) 开源许可协议

- 应用具备访问条件：[配置域名](./guide/appsetdomain) 或 **服务器安全组**开启网外端口