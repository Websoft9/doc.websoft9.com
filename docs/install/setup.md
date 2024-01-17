---
sidebar_position: 3
slug: /install/setup
---

import DocCardList from '@theme/DocCardList';
import {useCurrentSidebarCategory} from '@docusaurus/theme-common';


# 安装后配置

安装 Websoft9 的产品后，如下几个部署是必要的：

## 登录

登录 Websoft9 不需要额外的特别设置，只需要从本地浏览器访问服务器对应的端口即可：  

- 访问地址： *http://服务器公网IP:9000*  
- 默认密码：服务器的 root 账号与密码
- 需开启安全组端口：**80, 443, 9000**

![Websoft9 登录界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-loginpage.png)


如果没有云服务器使用经验，可以先阅读下面的指引：  

* [操作云服务器](../user/cloud)：连接服务器和操作云控制台、获取服务器公网IP、开启安全组端口等
* [获取账号密码](../user/credentials)：连接云服务器后，运行获取命令的命令

## 配置域名{#domain}

虽然 Websoft9 可以在无域名的情况下访问，但为了更好的用户体验和安全保护，我们强烈您为 Websoft9 [配置域名](../administrator/domain_step)。  


## 备份措施

* [服务器备份](../administrator/backup_server)：在云控制台设置服务器的自动化备份策略（例如：快照备份）
* [应用备份](../administrator/backup_app)：在应用的控制台设置自动化备份策略（参考每个应用的文档）


## 升级

* [应用升级](../administrator/upgrade_app)：预装的应用无法满足需求时，参考升级指南
