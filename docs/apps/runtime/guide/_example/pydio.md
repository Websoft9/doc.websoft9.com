---
slug: /lamp/installation/zh/pydio
---

# Pydio

本文档可供使用了 **Pydio 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 Pydio 参考。

Pydio（pydio.com）是一个功能强大在线文件管理系统（ECM），采用PHP+MySQL开发，用于构建自托管的企业网盘和云存储系统，支持多用户的文档协作、分享、设备同步。功能全面，包括：文档管理、用户管理、权限管理，甚至还有能够恢复删除的文件等功能，开源版支持的设备APP非常全面，包括：IOS、Android、Windows、OSX、Linux五个客户端同步APP。

## Pydio演示（截图）

Pydio官网提供了演示环境，您可以直接访问演示地址体验

* 演示地址：https://pydio.typeform.com/to/AUvlCj

> 免责说明：此处仅提供KodCloud官方的演示地址，不保证与Websoft9镜像功能完全一致，若演示过程中若需要填写个人资料、提交调研问题、获取Cookie等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此产生的可能存在的商业纠纷与我们司无关。

*****

以下为Pydio的主要功能截图

* 登录后默认界面
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-adminui-websoft9.png)

* 多用户管理
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-addusers-websoft9.png)

* 私人空间与公共空间
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-workspace-websoft9.png)

* 插件扩展
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-plugins-websoft9.png)

* 一键在线升级
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-upgrade-websoft9.png)

## 准备

在开始 Pydio 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## Pydio 安装到服务器

**如果你使用的是 *Pydio 镜像*，本节请忽略，直接阅读下一节 【Pydio 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 Pydio 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 Pydio 系统增加一个数据库，假如名称为：`pydio`
3. 到 Pydio 官方[下载源码](https://pydio.com/en/download)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 Pydio 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## Pydio 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
2. 选择语言，点击"Start Wizard"
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-install001-websoft9.png)
3. 设置管理员账号，进入下一步
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-install002-websoft9.png)
4. 选择Mysql数据库，填写数据库信息（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)），点击“test db connection”进入下一步
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-install003-websoft9.png)
5. 进入高级设置，设置默认语言为“简体中文”，点击“Install Pydio”，开始安装
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-install004-websoft9.png)
6. 安装完成后，登录后台
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-login-websoft9.png)
7. 后台界面
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-bk-websoft9.png)

## 常见问题

#### Pydio 是否提供移动端

提供了移动端，[下载地址](https://pydio.com/en/download)

#### Pydio 默认是否可以编辑 Office 文档？

不可以，需要自行配置文档预览服务器