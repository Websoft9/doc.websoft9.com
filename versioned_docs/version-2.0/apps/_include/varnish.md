[Varnish](https://varnish-cache.org) 是一个 **高性能HTTP缓存​​**，它被用于 HTTP 服务器  等场景。Varnish 是高性能 HTTP 反向代理和缓存加速器，提升网站速度。​​


![gui](https://libs.websoft9.com/Websoft9/DocsPicture/zh/varnish/varnish-gui-websoft9.png)


## 准备

在参阅本文档使用 Varnish 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Varnish：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [BSD2Clause](https://opensource.org/licenses/BSD-2-Clause) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口