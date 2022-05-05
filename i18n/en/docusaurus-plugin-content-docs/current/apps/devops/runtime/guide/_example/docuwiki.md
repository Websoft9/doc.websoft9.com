---
slug: /lamp/installation/zh/docuwiki
---

# DokuWiki

本文档可供使用了 **DokuWiki 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 DokuWiki 参考。

DokuWiki（docuwiki.org）是一个开源Wiki系统，程序小巧而功能强大、灵活，使用PHP开发而无需数据库支持，适合中小团队和个人网站的知识库管理。它因简洁易读的语法、易维护、备份和整合则使它成为技术爱好者的推崇。功能和界面类似Mediawiki，强大的访问控制列表 (ACL)功能，支持各种层次上的定制，可以从管理界面轻松配置，下载模板和扩展，也可以开发您自己的扩展。

## 准备

在开始 DokuWiki 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## DokuWiki 安装到服务器

**如果你使用的是 *DokuWiki 镜像*，本节请忽略，直接阅读下一节 【Concrete5 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 DokuWiki 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 DokuWiki 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## DokuWiki 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP*，即可打开DokuWiki的首页，无需任何安装
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/dokuwiki/dokuwiki-homepage-websoft9.png)

2. DokuWiki后台账号和密码\*\*：需要单独配置，默认是没有后台的

## 常见问题