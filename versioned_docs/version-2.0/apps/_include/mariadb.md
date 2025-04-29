[MariaDB](https://mariadb.org/) 是一个 **兼容 MySQL 的数据库系统**，它被用于 SQL 数据库/关系数据库  等场景。MariaDB 数据库，是一个企业级产品。它基于 Docker 架构，内置可以通过本地浏览器访问的可视化管理工具 phpMyAdmin，满足企业微服务架构的设计思想。 


![gui](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mariadb/mariadb-gui-websoft9.png)


## 准备

在参阅本文档使用 MariaDB 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）MariaDB：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [GPL-2.0](https://opensource.org/licenses/GPL-2.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口