---
slug: /lamp/installation/zh/zurmo
---
# ZurmoCRM

本文档可供使用了 **ZurmoCRM 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上部署 ZurmoCRM 参考。

[Zurmo](https://zurmo.org)是一个开源的客户关系管理系统(CRM)，使用Yii框架、RedBeanPHP和Jquery实现，界面非常美观，用户体验很好。功能包括：客户、支持、联系人、邮件跟踪、销售机会、产品、报价等。[官方演示](http://demo.zurmo.com/)

## 准备

在开始 ZurmoCRM 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## ZurmoCRM 安装到服务器

**如果你使用的是 *ZurmoCRM 镜像*，本节请忽略，直接阅读下一节 【ZurmoCRM 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 ZurmoCRM 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 ZurmoCRM 系统增加一个数据库，假如名称为：`zurmo`
3. 到 ZurmoCRM 官方[下载源码](https://zurmo.org/download)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 ZurmoCRM 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## ZurmoCRM 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）

3. 安装进入数据库配置界面（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)），然后点击【Install】  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zurmo/zurmo-intall001-websoft9.png)

2. 参考无误，系统进入安装界面  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zurmo/zurmo-intall002-websoft9.png)

3. 安装完成后进入登录页面  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zurmo/zurmo-install003-websoft9.png)

## 常见问题

#### 浏览器打开IP地址，无法访问 ZurmoCRM（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 ZurmoCRM 数据？

部署包内置 MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 ZurmoCRM 数据？

可以

#### ZurmoCRM如何发送邮件？

ZurmoCRM支持第三方的SMTP发送邮件模式，具体如下：

1. 打开ZurmoCRM -> Administrator Home ->Global Configuration，参考下图将两个邮箱改成一致：
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zurmo/zurmo-smtp-1-websoft9.png)

3. 以 163 邮箱为例，根据下图的设置，完成SMTP参数的设置
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zurmo/zurmo-smtp-2-websoft9.png)
	* Host 处请填写 SMTP 服务器的地址；
	* Port 处请填写 SMTP 服务器的端口
	* UseName 处请输入自己的邮箱地址 ；
	* Password 处请输入SMTP授权码（不同于邮箱密码）
	* Extra Mail Settings 处请填写链接协议ssl
	* Send a test email to 处请填写测试收件邮件地址

3. 设置完成后，请点击“Send Test Email”测试设置是否成功

> 以上参数设置以163邮箱为例，不同SMTP提供商的设置略有差异，请务必明确您所使用的SMTP所要求的设置方式。