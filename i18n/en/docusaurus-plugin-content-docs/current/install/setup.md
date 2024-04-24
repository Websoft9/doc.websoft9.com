---
sidebar_position: 3
slug: /install/setup
---

# 安装后配置

安装 Websoft9 到服务器后，便可以参考一下章节完成开始正式使用：

## 登录控制台

登录 Websoft9 不需要额外的特别设置，只需要从**本地浏览器**访问服务器对应的端口即可：  

- 访问地址： *http://服务器公网IP:9000*  
- 默认密码：服务器的 root 账号与密码
- 需开启安全组端口：**80, 443, 9000**

![Websoft9 登录界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-loginpage.png)


如果没有云服务器使用经验，可以先阅读下面的指引：  

* [操作云服务器](../user/cloud)：连接服务器和操作云控制台、获取服务器公网IP、开启安全组端口等
* [获取账号密码](../user/credentials)：连接云服务器后，运行获取命令的命令

## 配置域名{#domain}

虽然 Websoft9 可以在无域名的情况下访问，但为了更好的用户体验和安全保护，我们强烈您为 Websoft9 [配置域名](../guide/appsetdomain.md)。  

## 备份措施

需要尽早设置备份策略，不能存在侥幸心理。建议的备份优先级如下：

1. [服务器备份](../administrator/backup_server)：在云控制台设置服务器的自动化备份策略（例如：快照备份）
2. [Websoft9 备份](../administrator/backup_app)：Websoft9 平台以及所安装的应用的备份

## 升级

如果您安装的不是最新的 Websoft9，建议您立即进行[更新升级](../administrator/upgrade_app)
