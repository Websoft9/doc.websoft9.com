---
slug: /lamp/installation/zh/hdwiki
---

# HDWiki

本文档可供使用了 **HDWiki 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 HDWiki 参考。

HDWiki（hudong.com）是专为中文用户设计和开发的中文百科建站解决方案。简单易用、功能全面，中小站长利用HDWiki均能够在较短的时间内，花费较低的费用，采用较少的人力，架设一个性能优异、安全稳定的百科网站平台。采用PHP+MySQL开发，简单易用，界面友好，神似百度百科。内置的可视化编辑器可以让百科爱好者的知识录入与编辑如同操作word软件一样方便快捷。

## 准备

在开始 HDWiki 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## HDWiki 安装到服务器

**如果你使用的是 *HDWiki 镜像*，本节请忽略，直接阅读下一节 【HDWiki 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 HDWiki 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 HDWiki 系统增加一个数据库，假如名称为：`hdwiki`
3. 到 HDWiki 官方[下载源码](http://kaiyuan.hudong.com/)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 HDWiki 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## HDWiki 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
2. 系统进入环境检测步骤，通过后进入下一步
3. 填写您的数据库参数（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/hdwiki/hdwiki-install-setpw-websoft9.png)
4. 数据库连接正确，点击“下一步”后进入填写管理员信息，牢记之，并进入下一步
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/hdwiki/hdwiki-install-setadmin-websoft9.png)
5. 进入HDwiki前台，体验系统的完整功能
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/hdwiki/hdwiki-install-frontpage-websoft9.png)

## 常见问题

#### 为什么HDwiki某些页面总是提示“注意敏感词”？

HDwiki对select delete update insert from 等一些敏感词进行了过滤，比如程序的function名称中包含类似关键字，HDwiki站长可通过修改该方法名称，然后在将页面中的href链接修改为最新修改的方法名，即可恢复正常。