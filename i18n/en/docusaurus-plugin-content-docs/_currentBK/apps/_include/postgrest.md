[PostgREST](https://postgrest.org) 是一个 **Web server turns PostgreSQL into a RESTful API**，它被用于 Relational Databases Database Management Tools BaaS  等场景。PostgREST is a standalone web server that turns your PostgreSQL database directly into a RESTful API. The structural constraints and permissions in the database determine the API endpoints and operations.


![gui](http://libs.websoft9.com/Websoft9/DocsPicture/zh/postgrest/postgrest-gui-websoft9.png)


## 准备

在参阅本文档使用 PostgREST 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [MIT](https://opensource.org/licenses/MIT) 开源许可协议

- 应用具备访问条件：[配置域名](./guide/appsetdomain) 或 **服务器安全组**开启网外端口