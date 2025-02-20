[Keycloak](https://www.keycloak.org) 是一个 **Keycloak是一个开源IAM解决方案，通过用户联合、强认证和细粒度授权简化认证并保护服务。**，它被用于 秘钥管理  等场景。Keycloak是一个开源身份和访问管理解决方案，它能够在各种应用程序之间实现单点登录（SSO）并以最小的努力保护它们。它支持OpenID Connect、OAuth 2.0和SAML 2.0等标准协议，并提供身份经纪、社交登录、与LDAP和Active Directory的用户联合以及管理员和用户的集中管理等功能。Keycloak的高性能架构是云原生的，可扩展且可扩展，非常适合现代应用程序和服务。


![界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/keycloak/keycloak-gui-websoft9.png)


## 准备

在参阅本文档使用 Keycloak 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Keycloak：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口