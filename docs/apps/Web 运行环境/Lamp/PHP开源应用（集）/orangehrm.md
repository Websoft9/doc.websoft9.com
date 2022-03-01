---
slug: /lamp/installation/zh/orangehrm
---

# OrangeHRM

本文档可供使用了 **OrangeHRM 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 OrangeHRM 参考。

OrangeHRM（orangehrm.com）一个开源免费、经典的人力资源系统(HR)，功能包括员工信息管理、休假请假、工时、招聘、绩效管理等核心HRM模块。基于PHP开发，界面简约美观，拥有良好的生态，伙伴遍布全球18个地区。

## 准备

在开始 OrangeHRM 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## OrangeHRM 安装到服务器

**如果你使用的是 *OrangeHRM 镜像*，本节请忽略，直接阅读下一节 【OrangeHRM 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 OrangeHRM 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 OrangeHRM 系统增加一个数据库，假如名称为：`orangehrm`
3. 到 OrangeHRM 官方[下载源码](https://github.com/orangehrm/orangehrm)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 OrangeHRM 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## OrangeHRM 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/orangehrm/orangehrm-startpage-websoft9.png)
2.  通过许可协议，进入数据库配置界面（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)），然后点击"Next"
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/orangehrm/orangehrm-dbconf-websoft9.png)
3.  数据库安装成功后进入系统检测，依次点击“Next”，然后进入管理员账号设置界面
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/orangehrm/orangehrm-adminconf-websoft9.png)
4.  依次点击“Next”，进入系统安装确认页面，点击“Install”
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/orangehrm/orangehrm-startinstall-websoft9.png)
5.  安装成功，系统会有“done”的提示，进入下一步
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/orangehrm/orangehrm-done-websoft9.png)
6.  安装成功提示
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/orangehrm/orangehrm-finish-websoft9.png)
7.  开始体验登录后台
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/orangehrm/orangehrm-login-websoft9.png)
8.  后台设置语言为中文
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/orangehrm/orangehrm-language-websoft9.png)

## 常见问题