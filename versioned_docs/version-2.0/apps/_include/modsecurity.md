[ModSecurity](https://modsecurity.org) 是一个 **开源 Web 应用防火墙**，它被用于 IT 安全  等场景。ModSecurity是一个开源Web应用防火墙，提供实时监控、攻击检测和防护功能，增强Web安全性。


![界面](http://libs.websoft9.com/Websoft9/DocsPicture/zh/modsecurity/modsecurity-gui-websoft9.png)


## 准备

在参阅本文档使用 ModSecurity 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）ModSecurity：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口