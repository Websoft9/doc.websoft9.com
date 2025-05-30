[PostgREST](https://postgrest.org) 是一个 **Postgres 数据库 API 转换中间件**，它被用于 SQL 数据库/关系数据库 数据库工具 后端即服务  等场景。PostgREST 是一个独立的 Web 服务器，可将您的 PostgreSQL 数据库直接转换为 RESTful API。数据库中的结构约束和权限决定了 API 端点和操作。


![gui](http://libs.websoft9.com/Websoft9/DocsPicture/zh/postgrest/postgrest-gui-websoft9.png)


## 准备

在参阅本文档使用 PostgREST 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）PostgREST：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [MIT](https://opensource.org/licenses/MIT) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口