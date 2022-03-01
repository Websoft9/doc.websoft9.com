---
slug: /lamp/installation/zh/espocrm
---

# EspoCRM

本文档可供使用了 **EspoCRM 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 EspoCRM 参考。

[EspoCRM](https://espocrm.com)是一个开源免费的轻量级CRM系统，采用响应式设计，界面非常美观大方，能够自动适应PC、平板和手机访问。功能非常全面，包括销售自动化、市场、销售过程、文档、产品、合同、知识库和工作流等功能。采用PHP+MySQL开发，支持字段和表单布局客制化。[官方演示](http://www.espocrm.com/demo/)

![](http://libs.websoft9.com/Websoft9/DocsPicture/en/espocrm/espocrm-gui-websoft9.jpg)

## 准备

在开始 EspoCRM 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## EspoCRM 安装到服务器

**如果你使用的是 *EspoCRM 镜像*，本节请忽略，直接阅读下一节 【EspoCRM 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 EspoCRM 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 EspoCRM 系统增加一个数据库，假如名称为：`espocrm`
3. 到 EspoCRM 官方[下载源码](https://www.espocrm.com/download/)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 EspoCRM 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## EspoCRM 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-lan-websoft9.png)

2. 选择语言之后（中国支持非常好），系统进入环境检测步骤
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-check-websoft9.png)

3. 然后点击“Install”，进入数据库参数设置界面（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-dbconf-websoft9.png)

4. 数据库连接正确，点击“Next”进入管理员账号设置界面，填写管理员信息，牢记之，并进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-adminconf-websoft9.png)

5. 配置时区
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-timeconf-websoft9.png)

6. 系统提示安装成功
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-login-websoft9.png)
7. 进入后台，体验系统的完整功能

> 需要了解更多 EspoCRM 的使用，请参考官方文档：[EspoCRM Documentation](https://www.espocrm.com/documentation/)

## 常见问题

#### 浏览器打开IP地址，无法访问 EspoCRM（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 EspoCRM 数据？

部署包内置 MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 EspoCRM 数据？

可以

#### EspoCRM 如何发送邮件？

EspoCRM支持第三方的SMTP发送邮件模式，具体如下：

1. 待EspoCRM安装完成后，点击右上角菜单->admin，点击Email项
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-smtp-1-websoft9.png)
2. 根据下图的设置，完成SMTP参数的设置
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/espocrm/espocrm-smtp-2-websoft9.png)
	* Server 处请填写 smtp 服务器的地址 ；
	* Port 处请填写正确的端口号；
	* Auth 处勾选表示发邮件需要验证账号
	* Security 处请邮件服务器支持的连接协议；
	* UseName 处请输入自己的邮箱地址 ；
	* Password 处请输入SMTP密码或授权码（不同于邮箱密码）
3. 设置完成后，请点击“Send Test Email”测试设置是否成功

> 以上参数设置以163为例，不同SMTP提供商的设置略有差异，请务必明确您所使用的SMTP所要求的设置方式。