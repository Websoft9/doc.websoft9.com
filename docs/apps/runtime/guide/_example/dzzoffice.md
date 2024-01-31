---
slug: /lamp/installation/zh/dzzoffice
---

# DzzOffice

本文档可供使用了 **DzzOffice 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 DzzOffice 参考。

DzzOffice是一套开源办公套件，适用于企业、团队搭建自己的 类似“Google企业应用套件”、“微软Office365”的企业协同办公平台。[官方演示](http://demo.dzzoffice.com/)

## 准备

在开始 DzzOffice 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## DzzOffice 安装到服务器

**如果你使用的是 *DzzOffice 镜像*，本节请忽略，直接阅读下一节 【DzzOffice 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 DzzOffice 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 DzzOffice 系统增加一个数据库，假如名称为：`dzzoffice`
3. 到 DzzOffice 官方[下载源码](https://github.com/zyx0814/dzzoffice/releases/)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 DzzOffice 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## DzzOffice 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
	 ![dzzoffice-install-websoft9](http://libs.websoft9.com/Websoft9/DocsPicture/zh/dzzoffice/dzzoffice-install-1-websoft9.png)
2. 确保环境检查和权限检查通过；
	 ![dzzoffice-install-websoft9](http://libs.websoft9.com/Websoft9/DocsPicture/zh/dzzoffice/dzzoffice-install-2-websoft9.png)
	 ![dzzoffice-install-websoft9](http://libs.websoft9.com/Websoft9/DocsPicture/zh/dzzoffice/dzzoffice-install-3-websoft9.png)
3. 输入数据库连接信息（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）
	![dzzoffice-install-websoft9](http://libs.websoft9.com/Websoft9/DocsPicture/zh/dzzoffice/dzzoffice-install-4-websoft9.png)
4. 输入管理员账户名和密码，点击下一步即可完成安装；
	![dzzoffice-install-websoft9](http://libs.websoft9.com/Websoft9/DocsPicture/zh/dzzoffice/dzzoffice-install-5-websoft9.png)

## 常见问题

#### DzzOffice 如何安装应用？

1. 管理 -》 应用市场 -》 在应用市场内找到对应应用，单击一键安装；
2. 管理 -》 应用市场 -》 已安装 中 点击启用按钮 启用此应用

#### DzzOffice 如何实现在线预览和编辑

1. 管理 -》 应用市场 -》 在应用市场内找到 “onlyoffice” 应用 点击 一键安装，安装完后，你可以通过http://ip:9002地址来测试onlyoffice是否安装成功，成功后进入下一步设置
2. 管理 -》 应用市场 -》 已安装 中 点击设置按钮 进入设置页面
	![dzzoffice-install-websoft9](http://libs.websoft9.com/Websoft9/DocsPicture/zh/dzzoffice/dzzoffice-preview-1-websoft9.png)
   > 这里填写您的文档服务器的地址：如文档服务器地址为 http://192.168.0.2 文档服务器端口为：9002 那么 这里的地址应该是：
http://192.168.0.2:9002。
3. 管理 -》 应用市场 -》 已安装 中 点击启用按钮 启用此应用
4. 网盘内点击文档类文件 就可以使用 onlyoffice 来编辑文档了

>文档服务器可以自行搭建，或者使用 websoft9 提供的 [onlyoffice 文档部署包](https://apps.websoft9.com/onlyoffice)
