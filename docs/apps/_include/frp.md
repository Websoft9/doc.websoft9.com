[frp](https://gofrp.org) 是一个 **Internal network penetration proxy tool**，它被用于 网络  等场景。FRP 是一款高性能的反向代理工具，主要用于内网穿透，帮助用户将内网服务安全地暴露到公网上。


![界面](http://libs.websoft9.com/Websoft9/DocsPicture/zh/frp/frp-gui-websoft9.png)


## 准备

在参阅本文档使用 frp 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）frp：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口