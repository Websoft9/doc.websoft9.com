# TiDB

TiDB is an open-source distributed SQL database that supports Hybrid Transactional and Analytical Processing (HTAP) workloads. It is MySQL compatible and features horizontal scalability, strong consistency, and high availability.

简而言之，[TiDB](https://github.com/pingcap/tidb) 是一个 **Database support Hybrid Transactional and Analytical Processing (HTAP) workloads**，它被用于 NewSQL Database  等场景


![gui](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tidb/tidb-gui-websoft9.png)


## 准备

在参阅本文档使用 TiDB 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [](https://opensource.org/licenses/Apache-2.0) 开源许可协议

- 应用具备访问条件：[配置域名](./guide/appsetdomain) 或 **服务器安全组**开启网外端口