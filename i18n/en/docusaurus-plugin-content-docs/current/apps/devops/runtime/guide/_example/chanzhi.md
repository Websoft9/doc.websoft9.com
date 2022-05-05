---
slug: /lamp/installation/zh/chanzhi
---

# Chanzhi（禅知）

本文档可供使用了 **Chanzhi 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 Chanzhi 参考。

蝉知门户系统（chanzhiEPS）是一款开源免费的企业门户系统，企业建站系统，CMS系统。它专为企业营销设计，功能专业全面，内置了文章发布、会员管理、论坛评论、产品展示、在线销售、客服跟踪等功能。以ZPL协议发布，真开源，真免费。注重SEO，注重营销，支持移动设备。界面简洁大方，使用简单方便，功能专业强大。

## 准备

在开始 Chanzhi 的安装部署之前，建议完成如下事情：

* 本地浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## Chanzhi 安装到服务器

**如果你使用的是 *Chanzhi 镜像*，本节请忽略，直接阅读下一节 【Chanzhi 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 Chanzhi 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 Chanzhi 系统增加一个数据库，假如名称为：`chanzhieps`
3. 到 Chanzhi 官方[下载源码](https://www.chanzhi.org/download.html)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 chanzhi 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## Chanzhi 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/chanzhieps/chanzhi-startpage-websoft9.png)
2. 通过许可协议，安装进入环境检测步骤，点击“下一步”
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/chanzhieps/chanzhi-check-websoft9.png)
3. 进入配置数据库界面（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/chanzhieps/chanzhi-dbconf-websoft9.png)
4. 设置管理员账号，牢记之，点击“保存”
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/chanzhieps/chanzhi-adminconf-websoft9.png)
5. 系统安装成功，进入后台登录
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/chanzhieps/chanzhi-login-websoft9.png)
6. 开始体验后台
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/chanzhieps/chanzhi-backend-websoft9.png)
7. 禅知的功能使用，请参考[官方教程](http://www.chanzhi.org/book/)

## 常见问题