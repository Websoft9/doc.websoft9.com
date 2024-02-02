# Caddy

Caddy 2 is a powerful, enterprise-ready, open source web server with automatic HTTPS written in Go

简而言之，[Caddy](https://caddyserver.com/) 是一个 **The Ultimate Server with Automatic HTTPS**，它被用于 HTTP Server  等场景


![architecture](https://libs.websoft9.com/Websoft9/DocsPicture/zh/caddy/caddy-arch-websoft9.svg)


## 准备

在参阅本文档使用 Caddy 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议

- 应用具备访问条件：[配置域名](./guide/appsetdomain) 或 **服务器安全组**开启网外端口