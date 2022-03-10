---
slug: /wampserver/installation/zh/wordpress
---

# WordPress

本文档可供使用了 **WordPress 镜像** 用户参考，也可以供准备在 **WampServer 镜像** 上自行部署 WordPress 参考。

[WordPress](https://wordpress.org) 简称WP，最初是一款博客系统，后逐步演化成一款功能强大的企业级 CMS（内容管理/建站系统），目前是公认的全球最佳建站系统，互联网上有34%的网站都基于 WordPress构建。这套系统因易用性、易扩展性（ 插件 、模板、二次开发）、功能强大、美观、搜索引擎友好等而全世界著名。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-product-screenshot.png)

## 准备

在开始 WordPress 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/wampserver/zh/stack-components.html)）

## WordPress 安装到服务器

**如果你使用的是 *WordPress 镜像*，本节请忽略，直接阅读下一节 【WordPress 初始化安装向导】**

如果你使用的是 WampServer 镜像，请先将 WordPress 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/wampserver/zh/admin-mysql.html)，为 WordPress 系统增加一个数据库，假如名称为：`wordpress`
3. 到 WordPress 官方[下载源码](https://wordpress.org/download/)
4. 参考[《如何在 WampServer 上增加网站》](https://support.websoft9.com/docs/wampserver/zh/solution-deployment.html#安装第二个网站) ，将 WordPress 安装到服务器的 [WampServer](https://support.websoft9.com/docs/wampserver/zh/) 环境中

---

## WordPress 初始化安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*https://域名* 或 *https://Internet IP*, 进入安装向导  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wp01.png)
2. 选择语言后，进入 WordPress 安装要求说明，点击“现在就开始”进入下一步 
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-install001-websoft9.png)
3. 系统进入数据库连接信息安装项，请填写数据库连接信息（[不知道账号密码？](/zh/stack-accounts.md#mysql)） 
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-install002-websoft9.png)
4. 数据库验证通过后，系统提示正式“进行安装” 
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-install003-websoft9.png)
5. 设置您的管理员账号、密码和邮箱， 点击“安装WordPress”; 
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-install004-websoft9.png)
6. 恭喜，成功安装 
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-install005-websoft9.png)
7. 进入后台（http//域名或IP/wp-admin），试试WordPress的功能 
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-install006-websoft9.png)
8. WordPress的安装已经全部完成。

## 常见问题

请参考 [《WordPress 专题指南》](http://support.websoft9.com/docs/wordpress/zh/solution-plugin.html)