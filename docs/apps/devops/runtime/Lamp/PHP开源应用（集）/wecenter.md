---
slug: /lamp/installation/zh/wecenter
---
# WeCenter

本文档可供使用了 **WeCenter 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 WeCenter 参考。

WeCenter（wecenter.com）是一款建立知识社区的开源程序（免费版），诞生于中国，专注于企业和行业社区内容的整理、归类、检索和分享，使用WeCenter能够快速搭建一个类似知乎这样的网站，是知识化问答社区的首选软件。后台使用PHP开发，MVC架构，前端使用Bootstrap框架，优雅大方。

## 准备

在开始 WeCenter 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## WeCenter 安装到服务器

如果你使用的是 **WeCenter 专属运行环境镜像**，参考下面步骤：

1. 到WeCenter官方网站下载 [WeCenter官方源码](http://www.wecenter.com/downloads/)，本地解压
2. 通过 WinSCP 上传源码到 */data/wwwwroot/wecenter* 目录
	![](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/wecenter/wecenter-upload-websoft9.png)
3. 进入【WeCenter 初始化安装向导】

如果你使用的是 **LAMP 镜像**，请先将 WeCenter 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 WeCenter 系统增加一个数据库，假如名称为：`wecenter`
3. 到 WeCenter 官方[下载源码](http://www.wecenter.com/downloads/)
2. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 WeCenter 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## WeCenter 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wecenter/wecenter-startins-websoft9.png)
2. 根据系统提示，进入数据库连接信息安装项，请填写数据库连接信息（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wecenter/wecenter-confdb-websoft9.png)
3. 设置您的管理员账号、密码和邮箱，牢记之， 点击“完成”;
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wecenter/wecenter-setadmin-websoft9.png)
4. 成功安装提示
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wecenter/wevcenter-installss-websoft9.png)
5. 在前台之后，登录后点击“管理”
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wecenter/wecenter-loginadmin-websoft9.png)
6. 系统提示进入后台
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wecenter/wecenter-loginadmin2-websoft9.png)
7. 开始体验后台
 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wecenter/wecenter-backend-ui.png)

## 常见问题

#### WeCenter如何发送邮件  

 WeCenter可以通过设置SMTP来实现发送邮件的功能，具体设置步骤如下：  

1. 以管理员身份登录到网站后台，点击**全局设置**，切换到**邮件设置**页面； 
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wecenter/wecenter-smtp-websoft9.png) 
2. 系统邮件发送方式选择**通过SOCKET连接SMTP发送**；
3. 输入SMTP服务器地址；
4. 使用安全链接(SSL)连接主服务器选择**是**；
5. 输入SMTP服务器的端口号；
6. 输入提供SMTP服务的邮箱地址；
7. 输入该邮箱地址的SMTP服务授权码或密码；
8. 系统邮件来源地址必须和**主SMTP账户**的邮箱地址保持一致；
