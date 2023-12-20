---
slug: /lamp/installation/zh/typecho 
---
# Typecho

本文档可供使用了 **Typecho 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 Typecho 参考。

Typecho是一个轻量级博客系统，源自中国，以极简、美观和大方著称

![](https://oss.aliyuncs.com/netmarket/product/68b593ac-a0dc-4472-a573-85559e2afd5d.png)

## 准备

在开始 Typecho 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## Typecho 安装到服务器

**如果你使用的是 *Typecho 镜像*，本节请忽略，直接阅读下一节 【Typecho 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 Typecho 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 Typecho 系统增加一个数据库，假如名称为：`typecho`
3. 到 Typecho 官方[下载源码](http://typecho.org/download)
2. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 Typecho 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## Typecho 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/typecho/Typecho-install001-websoft9.png)
2. 按照程序安装向导的要求填写相关服务器参数和初始化设置信息，完成后点击下一步。 
3. 注意配置数据库界面（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）
4. 在安装成功界面中会显示自动生成的初始登录密码，请务必牢记或马上进入后台按提示更改。
5. 完成安装，获得安装成功的提示

## 常见问题

#### 忘记管理员密码了怎么办？

万一不慎丢失初始密码可以删除installation directory下生成的config.inc.php文件，然后重新安装选择保留原有数据库即可。