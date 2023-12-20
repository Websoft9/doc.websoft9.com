---
slug: /lamp/installation/zh/concrete5
---

# Concrete5

本文档可供使用了 **Concrete5 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 Concrete5 参考。

Concrete5（concrete5.org）是一个全新的开源CMS，采用PHP+MySQL开发，知名度很高。完全所见所得编辑，可以支持直接在页面上进行编辑、排版，支持大量主题和插件功能扩展。

## 准备

在开始 Concrete5 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## Concrete5 安装到服务器

**如果你使用的是 *Concrete5 镜像*，本节请忽略，直接阅读下一节 【Concrete5 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 Concrete5 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 Concrete5 系统增加一个数据库，假如名称为：`concrete5`
3. 到 Concrete5 官方[下载源码](http://www.concrete5.org/download)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 Concrete5 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## Concrete5 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/concrete5/concrete5-installpage-websoft9.png)
2. 选择一种语言、环境检测之后，进入管理员和数据库设置界面。先设置好管理员账号，并牢记之 
 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/concrete5/concrete5-setadmin-websoft9.png)
3. 然后配置数据库信息（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)），locale请选择“Shanghai”，然后点击安装系统 
 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/concrete5/concrete5-setdb-websoft9.png)
4. 安装成功后，系统会显示安装成功信息，然后点击“Edit your site”可以进入后台 
 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/concrete5/concrete5-installss-websoft9.png)
5. 如果退出了后台系统，请通过 *http://域名/index.php/login* 进入后台（默认用户名为admin，密码是第二步设置的） 
 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/concrete5/concrete5-login-websoft9.png)
6. 开始体验后台 
 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/concrete5/concrete5-backend-websoft9.png)

## 常见问题