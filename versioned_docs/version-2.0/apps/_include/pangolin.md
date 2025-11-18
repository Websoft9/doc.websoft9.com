[Pangolin](https://digpangolin.com/) 是一个 **安全隧道工具**，它被用于 虚拟网络  等场景。Pangolin 的核心是一个具有身份和访问管理功能的自托管隧道反向代理，旨在通过在用户空间中运行的加密 WireGuard 隧道安全地公开私有资源。


![gui](https://libs.websoft9.com/Websoft9/DocsPicture/zh/pangolin/pangolin-gui-websoft9.png)


## 准备

在参阅本文档使用 Pangolin 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Pangolin：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [GPL-3.0](https://opensource.org/licenses/GPL-3.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口