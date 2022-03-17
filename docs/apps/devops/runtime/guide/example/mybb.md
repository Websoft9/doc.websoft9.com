---
slug: /lamp/installation/zh/mybb
---

# MyBB

本文档可供使用了 **MyBB 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 MyBB 参考。

MyBB（mybb.com）是全球知名的开源PHP论坛软件之一。使用了标准的论坛结构和模式，充分根据用户的使用习惯而设计，简单易用。支持MySQL、PostgreSQL、SQLite三种数据库。经过10几年的发展，拥有完善的开发者生态，有数百万站点使用，主题、插件资源非常丰富。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mybb/Emerald-themes.png)

## 准备

在开始 MyBB 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## MyBB 安装到服务器

**如果你使用的是 *MyBB 镜像*，本节请忽略，直接阅读下一节 【MyBB 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 MyBB 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 MyBB 系统增加一个数据库，假如名称为：`mybb`
3. 到 MyBB 官方[下载源码](https://mybb.com/download)
2. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 MyBB 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## MyBB 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mybb/mybb-installwelcome-websoft9.png)
2. 系统通过许可协议、环境检测之后，进入配置数据库界面（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mybb/mybb-installdb-websoft9.png)
3. 继续下一步，直至进入如下的配置论坛步骤，然后下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mybb/mybb-installconfigforum-websoft9.png)
4. 进入填写管理员信息步骤，设置并牢记之，然后进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mybb/mybb-installadmin-websoft9.png)
5. 完成安装，获得安装成功的提示
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mybb/mybb-installsuccess-websoft.png)
6. 进入根提示进入系统后台（/admin），体验系统的完整功能
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mybb/mybb-installlogin-websoft9.png)
7. 开始体验后台
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mybb/mybb-installbackend-websoft.png)

## 常见问题