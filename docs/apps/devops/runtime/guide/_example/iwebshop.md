---
slug: /lamp/installation/zh/iwebshop
---

# iWebShop

本文档可供使用了 **iWebShop 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 iWebShop 参考。

iWebShop 是一款基于PHP语言及MYSQL数据库开发的B2B2C单用户和多用户开源商城系统，系统支持平台自营和多商家入驻、集成微信商城、手机商城、移动端APP商城、三级分销、微信小程序等于一体，它可以承载大数据量且性能优良，还可以跨平台，界面美观功能丰富是电商建站首选源码。 系统分为：【免费试用版本】 和 【商业付费版本】

## 准备

在开始 iWebShop 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## iWebShop 安装到服务器

**如果你使用的是 *iWebShop 镜像*，本节请忽略，直接阅读下一节 【iWebShop 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 iWebShop 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 iWebShop 系统增加一个数据库，假如名称为：`iwebshop`
3. 到 iWebShop 官方[下载源码](http://www.aircheng.com/down)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 iWebShop 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## iWebShop 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/iwebshop/iwebshop-install001-websoft9.png)
2.  完成许可协议、环境检测之后，进入配置数据库界面（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)），并设置的管理员帐号密码，然后继续
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/iwebshop/iwebshop-install002-websoft9.png)
3.  系统安装成功

## 常见问题

#### iWebShop 是免费的吗？

不是免费的，官方只是提供了免费使用版

#### 如何设置SMTP发邮件？

iWeShop可以通过设置SMTP来实现发送邮件的功能，具体设置步骤如下：  
1. 进入网站设置--邮箱设置页面；  
2. 输入提供SMTP服务的服务器地址；  
3. 选择SSL加密方式；  
4. 输入提供SMTP服务的服务器地址；  
5. 输入提供SMTP服务的邮箱地址；  
6. 输入该邮箱的SMTP服务密码(有的也叫做授权码)；  
7. 输入SMTP服务器的端口号；  
8. 输入测试收件人邮件地址，若测试邮箱接收到邮件，则设置正确，可以点击保存邮箱设置，完成iWeShop的邮件功能设置。  
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/iwebshop/iweshop-smtp-websoft9.png)