[Tailscale](https://tailscale.com) 是一个 **点对点连接的VPN**，它被用于 虚拟网络  等场景。Tailscale 是一个基于 WireGuard 的虚拟私人网络（VPN）解决方案，旨在简化安全的网络连接。它允许用户在不同设备之间建立安全的点对点连接，而无需复杂的网络配置。


![界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tailscale/tailscale-gui-websoft9.png)


## 准备

在参阅本文档使用 Tailscale 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Tailscale：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [bsd3Clause](https://opensource.org/licenses/BSD-3-Clause) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口