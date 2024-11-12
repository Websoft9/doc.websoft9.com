[Apache ZooKeeper](https://zookeeper.apache.org/) 是一个 **分布式应用的协调服务软件**，它被用于 消息队列 负载均衡   等场景。Apache ZooKeeper 致力于开发和维护一个开源服务器，以实现高度可靠的分布式协调。


![架构](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zookeeper/zookeeper-archi-websoft9.webp)


## 准备

在参阅本文档使用 Apache ZooKeeper 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Apache ZooKeeper：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口