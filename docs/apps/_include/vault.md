[HashiCorp Vault](https://www.vaultproject.io/) 是一个 **密码与敏感信息保护系统**，它被用于 访问控制 秘钥管理  等场景。使用用户界面、CLI 或 HTTP API 安全、存储和严格控制对令牌、密码、证书、加密密钥的访问，以保护机密和其他敏感数据。


![Console](https://libs.websoft9.com/Websoft9/DocsPicture/zh/vault/vault-gui-websoft9.jpeg)


## 准备

在参阅本文档使用 HashiCorp Vault 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）HashiCorp Vault：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [MPL-2.0](https://opensource.org/licenses/MPL-2.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口