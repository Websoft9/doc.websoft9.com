---
slug: /lamp/installation/zh/tiki
---
# Tiki

本文档可供使用了 **Tiki 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 Tiki 参考。

Tiki是一个集Wiki/CMS/Groupware（维基百科/内容管理/协同）于一体的开源软件，始于2002年，采用PHP+MySQL开发，全球有100万安装量。其独特之处在于，除了Wiki之外，还有Bug跟踪、论坛、新闻博客、文件图片管理、邮件订阅等功能。通过TikiWiki，您可以很轻松的搭建各种类型的Wiki网站、支持门户、知识库、内部研发协作等。

## 准备

在开始 Tiki 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## Tiki 安装到服务器

**如果你使用的是 *Tiki 镜像*，本节请忽略，直接阅读下一节 【Tiki 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 Tiki 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 Tiki 系统增加一个数据库，假如名称为：`tiki`
3. 到 Tiki 官方[下载源码](https://tiki.org/Download)
2. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 Tiki 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## Tiki 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/Tiki/Tiki-installwelcome-websoft9.png)
2. 同意版权协议后，选择语言
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/tiki/tiki-install-selectlanguage-websoft9.png)
3. 系统进入环境检测，点击“Continue”进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/tiki/tiki-installcheck-websoft9.png)
4. 根据下图填写您的数据库参数（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/tiki/tiki-installdb-websoft9.png)
5. 数据库连接成功，系统会显示"Installation complete"字样，点击“Continue”进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/tiki/tiki-review-websoft9.png)
6. 本步骤是通用配置，建议全部选用默认配置，点击“Continue”进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/tiki/tiki-install7-websoft9.png)
7. 安装完成，选这个一个登录方式
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/tiki/tiki-installenter-websoft9.png)
8. 设置登录密码和管理员邮箱，然后登录
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/tiki/tiki-login-websoft9.png)