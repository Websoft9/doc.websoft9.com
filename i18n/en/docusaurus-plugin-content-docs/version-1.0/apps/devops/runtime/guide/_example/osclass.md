---
slug: /lamp/installation/zh/osclass
---
# Osclass

本文档可供使用了 **Osclass 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 Osclass 参考。

Osclass（osclass.com）是一个构建分类信息网站的开源软件，使用PHP+MySQL开发，用于搭建类似58同城、百姓网等门户网站而不需要任何技术，并支持广告管理。官方提供了有大量的主题、模板、插件可供使用，系统也可以深度客户化定制。

## 准备

在开始 Osclass 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## Osclass 安装到服务器

**如果你使用的是 *Osclass 镜像*，本节请忽略，直接阅读下一节 【Osclass 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 Osclass 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 Osclass 系统增加一个数据库，假如名称为：`osclass`
3. 到 Osclass 官方[下载源码](https://github.com/osclass/Osclass)
2. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 Osclass 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## Osclass 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
2. 根据系统提示，点击“Install”进入安装
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/osclass/osclass-install001-websoft9.png)
3. 填写您的数据库参数（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)），保存并继续;
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/osclass/osclass-install002-websoft9.png)
4. 设置网站信息。站点维护账号及后台账号，请务必设置好并牢记之。进入下一步
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/osclass/osclass-install003-websoft9.png)
5. 系统完成最后一步安装，建议进入Osclass后台（后台地址参考常见《账号与密码说明章节》），体验完整功能
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/osclass/osclass-install004-websoft9.png)

说明：后台地址为http://域名/os-admin


## 常见问题