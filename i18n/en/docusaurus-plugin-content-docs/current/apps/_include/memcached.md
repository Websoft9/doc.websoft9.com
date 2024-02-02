# memcached

Memcached is an in-memory key-value store for small chunks of arbitrary data (strings, objects) from results of database calls, API calls, or page rendering. 

简而言之，[memcached](https://www.memcached.org/) 是一个 **a free & open source, high-performance, distributed memory object caching system**，它被用于 In-memory Database  等场景


![gui](https://libs.websoft9.com/Websoft9/DocsPicture/en/memcached/memcached-gui-websoft9.png)


## 准备

在参阅本文档使用 memcached 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [bsd3Clause](https://opensource.org/licenses/BSD-3-Clause) 开源许可协议

- 应用具备访问条件：[配置域名](./guide/appsetdomain) 或 **服务器安全组**开启网外端口