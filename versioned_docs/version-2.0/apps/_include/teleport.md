[Teleport](https://goteleport.com/) 是一个 **开源堡垒机，基础设施安全访问平台**，它被用于 堡垒机 数据库工具  等场景。Teleport 被 DevSecOps 团队用于 SSH、Kubernetes、数据库、内部 Web 应用程序和 Windows。


![控制面板](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teleport/teleport-gui-websoft9.png)


## 准备

在参阅本文档使用 Teleport 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Teleport：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口