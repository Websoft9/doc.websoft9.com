[Apache ZooKeeper](https://zookeeper.apache.org/) 是一个 **分布式应用的协调服务软件**，它被用于 消息队列 负载均衡   等场景。Apache ZooKeeper is an effort to develop and maintain an open-source server which enables highly reliable distributed coordination.


![架构](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zookeeper/zookeeper-archi-websoft9.webp)


## 准备

在参阅本文档使用 Apache ZooKeeper 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议

- 应用具备访问条件：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口