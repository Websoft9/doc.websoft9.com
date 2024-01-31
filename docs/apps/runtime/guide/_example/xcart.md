---
slug: /lamp/installation/zh/xcart
---

# XCart

本文档可供使用了 **XCart 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 XCart 参考。

XCart（x-cart.com）是一个老牌的开源商城软件，采用PHP+MySQL开发，始于2001年，目前支持全球3.5万个独立商城运行。采用自适应设计，移动端界面出色，以易使用、易维护、易修改著称。内置75+个支付接口，模板定制灵活，插件和主题资源丰富。架构灵活，可以方便扩展到各种B2C、B2B和多店铺商城场景。

## 准备

在开始 XCart 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## XCart 安装到服务器

**如果你使用的是 *XCart 镜像*，本节请忽略，直接阅读下一节 【XCart 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 XCart 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 XCart 系统增加一个数据库，假如名称为：`xcart`
3. 到 XCart 官方[下载源码](https://www.x-cart.com/download.html)
2. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 XCart 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## XCart 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/xcart/xcart-installpage-websoft9.png)
2.  进入安装向导第二步，系统提示设置管理员帐号密码，请牢记之，并进入下一步
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/xcart/xcart-install002-websoft9.png)
3.  系统完成一系列自动检测后，进入数据库配置项（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/xcart/xcart-install004-websoft9.png)
4.  系统开始自动安装，完成后提示成功安装信息，请点击链接分别访问前台和后台
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/xcart/xcart-installss-websoft9.png)
5.  进入后台登录，开始体验系统
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/xcart/xcart-login-websoft9.png)

注意：后台登录地址为：*http://域名/admin.php*