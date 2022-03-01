---
slug: /lamp/installation/zh/cmseasy
---

# CmsEasy

本文档可供使用了 **CmsEasy 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 CmsEasy 参考。

CmsEasy（cmseasy.cn）是一个源自中国本土的100%开源免费的CMS，基于PHP+MySQL开发，采用模块化架构，拥有全新的设计体验与传播方式，后台功能让你的创作去繁化简， 响应式UI设计，全面支持PC和移动端访问。功能非常全面，文章、产品、表单、支付等网站所需功能一应具全。

## 准备

在开始 CmsEasy 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## CmsEasy 安装到服务器

**如果你使用的是 *CmsEasy 镜像*，本节请忽略，直接阅读下一节 【CmsEasy 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 CmsEasy 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 CmsEasy 系统增加一个数据库，假如名称为：`cmseasy`
3. 到 CmsEasy 官方[下载源码](http://www.cmseasy.cn/download/)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 CmsEasy 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## CmsEasy 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cmseasy/cmseasy-installward-websoft9.png)
2. 配置数据库后（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)），设置管理员账号密码
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cmseasy/cmseasy-setaccount-websoft9.png)
3. 点击“安装”，系统安装成功，系统提示
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cmseasy/cmseasy-installsuccess-websoft9.png)
4. 进入后台登录,输入设置的管理员账号密码
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cmseasy/cmseasy-login-websoft9.png)
5. 开始体验后台 
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cmseasy/cmseasy-accessbk-websoft9.png)

## 常见问题

#### CmsEasy的后台地址url是什么？

本地浏览器访问：*http://域名/admin*，即可进入后台登陆页面