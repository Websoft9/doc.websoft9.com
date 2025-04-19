[Docker Mailserver](https://docker-mailserver.github.io/docker-mailserver/latest/) 是一个 **邮件服务器**，它被用于 企业邮箱  等场景。Docker 邮件服务器，简称 DMS，是一款可投入生产的全栈式但简单的邮件服务器（支持 SMTP、IMAP、LDAP 协议，具备反垃圾邮件、防病毒等功能）。它仅使用配置文件，无需 SQL 数据库。该镜像围绕 “保持简洁且有版本控制” 这一口号打造


![界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/dockermailserver/dockermailserver-gui-websoft9.png)


## 准备

在参阅本文档使用 Docker Mailserver 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Docker Mailserver：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [MIT](https://opensource.org/licenses/MIT) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口