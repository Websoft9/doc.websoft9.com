[Debezium](https://debezium.io) 是一个 **一个用于变更数据捕获的开源分布式平台**，它被用于 数据采集/编排/集成 实时流式分析  等场景。Debezium是一款开源工具，通过捕获数据库变更流，实现低延迟的数据变更事件流，助力实时数据同步。


![界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/debezium/debezium-gui-websoft9.png)


## 准备

在参阅本文档使用 Debezium 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Debezium：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口