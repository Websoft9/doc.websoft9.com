[Tinyproxy](https://github.com/tinyproxy/tinyproxy) 是一个 **轻量级 HTTP/HTTPS 代理软件**，它被用于 HTTP 服务器 应用网关  等场景。Tinyproxy 是一个小型、高效的 HTTP/SSL 代理守护进程，在 GNU 通用公共许可证。Tinyproxy 在小型网络中非常有用 设置，其中较大的代理要么过于占用资源，要么 安全风险。Tinyproxy 的主要功能之一是缓冲 连接概念。


![Dashboard](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tinyproxy/tinyproxy-gui-websoft9.png)


## 准备

在参阅本文档使用 Tinyproxy 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Tinyproxy：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [GPL-2.0](https://opensource.org/licenses/GPL-2.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口