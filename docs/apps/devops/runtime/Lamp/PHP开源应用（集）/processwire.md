---
slug: /lamp/installation/zh/processwire
---

# ProcessWire

本文档可供使用了 **ProcessWire 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 ProcessWire 参考。

ProcessWire（processwire.com）是一个开源内容管理系统，是基于PHP的Web应用程序框架，针对设计师，开发人员和他们的客户的需求，简单而且强大的控制网站的搭建过程，提供强大的模板系统，基于 jQuery 的 Ajax API。

## 准备

在开始 ProcessWire 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## ProcessWire 安装到服务器

**如果你使用的是 *ProcessWire 镜像*，本节请忽略，直接阅读下一节 【ProcessWire 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 ProcessWire 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 ProcessWire 系统增加一个数据库，假如名称为：`processwire`
3. 到 ProcessWire 官方[下载源码](https://processwire.com/download/)
2. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 ProcessWire 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## ProcessWire 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
2. 选择一个配置文件安装方式，建议选择“Classic”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/processwire/processwire-install001-websoft9.png)
3. 系统完成环境检测之后，进入配置数据库界面（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/processwire/processwire-dbset-websoft9.png)
4. 系统进入管理员账号设置，请自行填写并牢记之，然后进入下一步
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/processwire/processwire-adminset-websof9.png)
5. 系统成功安装，提示相关信息
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/processwire/processwire-ss-websoft9.png)
6. 开始体验后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/processwire/processwire-backend-websoft.png)

说明：后台地址为http://域名或公网ip/admin