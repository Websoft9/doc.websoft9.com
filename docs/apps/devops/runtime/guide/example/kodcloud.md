---
slug: /lamp/installation/zh/kodcloud
---

# KodCloud（可道云）

本文档可供使用了 **KodCloud 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 KodCloud 参考。

[KodCloud](https://kodcloud.com)-可道云一个基于Web的在线文件管理和代码编辑器系统，界面风格和操作体验类似Windows，及其好用。合适构建私有企业网盘、云资源管理、多媒体管理、网站管理等场景。 

[官方演示](http://demo.kodcloud.com/index.php)

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodexplorer/kodcloud-gui-websoft9.png)


## 准备

在开始 KodCloud 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## KodCloud 安装到服务器

**如果你使用的是 *KodCloud 镜像*，本节请忽略，直接阅读下一节 【KodCloud 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 KodCloud 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 KodCloud 系统增加一个数据库，假如名称为：`KodCloud`
3. 到 KodCloud 官方[下载源码](https://kodcloud.com/download/)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 KodCloud 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## KodCloud 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）

2. 在下面的界面设置 admin 管理员用户的密码
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodexplorer/kodexplorer-setadminpw-websoft9.png)
3.  设置管理员密码后，系统转到登录界面
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodexplorer/kodexplorer-login-websoft9.png)
4.  登录成功，系统进入后台，如果有新版本，系统会提示是否自动更新。点击“自动更新”，系统会自动完成更换后要求重新登录
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodexplorer/kodexplorer-updateauto-websoft9.png)
5.  登录成功，进入后台，开始体验后台  
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodexplorer/kodexplorer-backend-websoft9.png)
6. 进入后台，体验系统的完整功能

> 需要了解更多 KodCloud 的使用，请参考官方文档：[KodCloud Help](https://kodcloud.com/help/)

## 常见问题

#### 浏览器打开IP地址，无法访问 KodCloud（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 KodCloud 数据？

KodCloud 无需数据库支持

#### 是否可以采用云厂商提供的 RDS 来存储 KodCloud 数据？

可以
