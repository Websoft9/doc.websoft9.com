[Caddy](https://caddyserver.com/) 是一个 **自动 HTTPS 开源 Web 服务器**，它被用于 HTTP 服务器 HTML  等场景。Caddy 是一个强大且可扩展的 HTTP/2 Web 服务器，它默认使用 HTTPS 并自动获取和更新 TLS 证书


![architecture](https://libs.websoft9.com/Websoft9/DocsPicture/zh/caddy/caddy-arch-websoft9.svg)


## 准备

在参阅本文档使用 Caddy 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Caddy：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口