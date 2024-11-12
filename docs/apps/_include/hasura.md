[Hasura](https://hasura.io/) 是一个 **将 MySQL 等数据库实时转换为 GraphQL/REST APIs**，它被用于 API 网关  等场景。Blazing fast, instant realtime GraphQL APIs on your DB with fine grained access control, also trigger webhooks on database events.


![架构](https://libs.websoft9.com/Websoft9/DocsPicture/zh/hasura/hasura-gui-websoft9.png)


## 准备

在参阅本文档使用 Hasura 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Hasura：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口