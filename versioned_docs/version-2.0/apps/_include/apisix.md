[Apache APISIX]() 是一个 **高性能的云原生 API 网关**，它被用于 API 网关  等场景。Apache APISIX provides rich traffic management features like Load Balancing, Dynamic Upstream, Canary Release, Circuit Breaking, Authentication, Observability, etc.


![路由列表](https://libs.websoft9.com/Websoft9/DocsPicture/zh/apisix/apisix-routelist-websoft9.png)


## 准备

在参阅本文档使用 Apache APISIX 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Apache APISIX：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的

- 请检查应用的使用许可协议，确保符合要求


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口