[Traefik Proxy](https://traefik.io/traefik/) 是一个 **云原生应用代理服务器软件**，它被用于 HTTP 服务器 应用网关  等场景。Traefik（发音流量）是一种现代 HTTP 反向代理和负载均衡器，可轻松部署微服务


![Dashboard](https://libs.websoft9.com/Websoft9/DocsPicture/zh/traefik/traefik-gui-websoft9.webp)


## 准备

在参阅本文档使用 Traefik Proxy 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Traefik Proxy：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [MIT](https://opensource.org/licenses/MIT) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口