# TiDB

TiDB 是一个开源的分布式 SQL 数据库，支持混合事务和分析处理 （HTAP） 工作负载。它与 MySQL 兼容，并具有水平可扩展性、强一致性和高可用性。

简而言之，[TiDB](https://github.com/pingcap/tidb) 是一个 **支持事务与分析的融合性数据库**，它被用于  等场景


![structure](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tidb/tidb-gui-websoft9.png)


## 准备

在参阅本文档使用 TiDB 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [](https://some_license_url) 开源许可协议

- 应用具备访问条件：[配置域名](./guide/appsetdomain) 或 **服务器安全组**开启网外端口