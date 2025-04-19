[Headscale](https://headscale.net) 是一个 **VPN，内网穿透，Tailscale的替代方案**，它被用于 虚拟网络  等场景。​Headscale​​ 是一款开源的、自托管的​​Tailscale控制服务器​​，用于构建基于WireGuard的点对点（P2P）虚拟专用网络（VPN）。


![界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/headscale/headscale-gui-websoft9.png)


## 准备

在参阅本文档使用 Headscale 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Headscale：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [LGPL-3.0](https://opensource.org/licenses/LGPL-3.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口