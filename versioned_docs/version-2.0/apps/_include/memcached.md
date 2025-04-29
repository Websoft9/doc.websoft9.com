[memcached](https://www.memcached.org/) 是一个 **高性能缓存数据库系统**，它被用于 缓存数据库  等场景。Memcached是一个自由开源的，高性能，分布式内存对象缓存系统。是一种基于内存的key-value存储，用来存储小块的任意数据（字符串、对象）。


![gui](https://libs.websoft9.com/Websoft9/DocsPicture/zh/memcached/memcached-gui-websoft9.png)


## 准备

在参阅本文档使用 memcached 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）memcached：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [bsd3Clause](https://opensource.org/licenses/BSD-3-Clause) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口