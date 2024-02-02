# Traefik Proxy

Traefik (pronounced traffic) is a modern HTTP reverse proxy and load balancer that makes deploying microservices easy. 

简而言之，[Traefik Proxy](https://traefik.io/traefik/) 是一个 **The Cloud Native Application Proxy**，它被用于 HTTP Server Application Gateway  等场景


![Dashboard](https://libs.websoft9.com/Websoft9/DocsPicture/zh/traefik/traefik-gui-websoft9.webp)


## 准备

在参阅本文档使用 Traefik Proxy 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [MIT](https://opensource.org/licenses/MIT) 开源许可协议

- 应用具备访问条件：[配置域名](./guide/appsetdomain) 或 **服务器安全组**开启网外端口