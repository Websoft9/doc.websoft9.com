---
slug: /lamp/installation/zh/zblog
---

# Zblog

本文档可供使用了 **Zblog 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 Zblog 参考。

Z-Blog（zblogcn.com）是由RainbowSoft Studio开发的一款小巧而强大的Blog程序，有ASP和PHP两个版本。Z-Blog针对国内用户习惯，做了大量改进。重点加强静态优化、自动备份、Hook的插件机制、多级评论和会员管理等功能模块。采用模板标签的方式，只要你会HTML+CSS，就可以简单地做出一套主题。

## 准备

在开始 Zblog 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## Zblog 安装到服务器

**如果你使用的是 *Zblog 镜像*，本节请忽略，直接阅读下一节 【Zblog 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 Zblog 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 Zblog 系统增加一个数据库，假如名称为：`zblog`
3. 到 Zblog 官方[下载源码](https://www.zblogcn.com/zblogphp/)
2. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 Zblog 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## Zblog 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/Zblog/Zblog-installwelcome-websoft9.png)
2. 完成通过许可协议、环境检测之后，选择MySql数据库，进入配置数据库界面（默认数据库为：zblog，默认用户名和密码参考本文档”常用账号与密码说明“章节）
3. 设置的管理员帐号密码，牢记之并进入下一步
4. 系统安装成功，进入后台体验