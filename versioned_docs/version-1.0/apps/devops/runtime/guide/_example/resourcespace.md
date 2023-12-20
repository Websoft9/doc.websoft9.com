---
slug: /lamp/installation/zh/resourcespace
---


# ResourceSpace

本文档可供使用了 **ResourceSpace 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 ResourceSpace 参考。

ResourceSpace（resourcespace.com）是全球是优秀的开源数字资产管理系统（Digital Assets Management），使用PHP+MySQL开发，主要用于集中式、协作化的管理企业的图片、视频、音频和文档等数字资产，完成基于Web，易于搜索，支持数百种文件格式的预览和相互转换，支持视频和音频文件的在线播放。是企业的设计部门和设计公司的效率工具。[官方演示地址](https://www.resourcespace.com/trial)


## 准备

在开始 ResourceSpace 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## ResourceSpace 安装到服务器

**如果你使用的是 *ResourceSpace 镜像*，本节请忽略，直接阅读【ResourceSpace 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 ResourceSpace 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 ResourceSpace 系统增加一个数据库，假如名称为：`resourceSpace`
3. 到 ResourceSpace 官方[下载源码](https://www.resourcespace.com/download)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 ResourceSpace 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## ResourceSpace 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/resourcespace/resourcespace-installcheck-websoft9.png)
2.  选择语言，系统会自动检查是否符合安装条件
3.  填写数据库配置信息（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/resourcespace/resourcespace-installconfig-websoft9.png) 
5.  点击“开始安装”
6.  安装完成后会看到反馈
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/resourcespace/resourcespace-installsuccessful-websoft9.png)
6.  访问后台地址：http://公网IP地址/login.php
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/resourcespace/resourcespace-login-websoft9.png)*
7.  登录后，开始体验后台
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/resourcespace/resourcespace-panel-websoft9.png)

## 常见问题

#### ResourceSpace 默认是否可以编辑 Office 文档？

不可以