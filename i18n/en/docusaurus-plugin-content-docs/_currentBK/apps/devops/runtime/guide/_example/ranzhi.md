---
slug: /lamp/installation/zh/ranzhi
---

# Ranzhi（然之）

本文档可供使用了 **Ranzhi 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 Ranzhi 参考。

Ranzhi 一款开源的OA&CRM系统，完全免费。采用PHP+MySql开发。由客户管理、订单管理、报销、审批、应收应付、财务记账和团队分享等功能组成，是一款非常合适中小企业的内部一体化管理软件。桌面式操作体验，优雅流畅、快捷方便。[官方演示](http://demo.ranzhi.org/)

## 准备

在开始 Ranzhi 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## Ranzhi 安装到服务器

**如果你使用的是 *Ranzhi 镜像*，本节请忽略，直接阅读下一节 【Ranzhi 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 Ranzhi 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 Ranzhi 系统增加一个数据库，假如名称为：`ranzhi`
3. 到 Ranzhi 官方[下载源码](https://www.ranzhi.org/download.html)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 Ranzhi 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## Ranzhi 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ranzhi/ranzhi-install001-websoft9.gif)

2. 系统检查，通过后进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ranzhi/ranzhi-install002-websoft9.gif)

3.  进入配置数据库界面（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ranzhi/ranzhi-install003-websoft9.gif)

4.  继续下一步，直至进入管理员账号设置界面，请设置好并牢记之，然后进入下一步
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ranzhi/ranzhi-install005-websoft9.gif)

5.  安装完成后，系统进入管理员登录界面，输入上一步填写的账号信息
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ranzhi/ranzhi-install006-websoft9.png)

6.  成功登录后台，开始体验
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ranzhi/ranzhi-backend-websoft9.png)

更多详情参考[然之官方SMTP文档](http://www.ranzhi.org/book/ranzhi)

## Ranzhi&EspoCRM&Zentao 初始化向导

Ranzhi&EspoCRM&禅道 是一个组合类部署包，内置了 Ranzhi, EspoCRM, Zentao 三个产品。初始化向导如下：

1. 通过访问 *http://公网IP地址/9panel* 了解初始化安装
2. 通过 WinSCP 登录服务器，进入 */etc/httpd/conf.d* 目录，分别将“ranzhi.conf.范例”、“zentao.conf.范例”和“espocrm.conf.范例”内容中的示例域名（类似：mydomain.com等字样）替换成您的域名，然后保存，并去掉“.范例”后缀
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ranzhi-zentao-espocrm/chanzhizentaoespocrm-conf-websoft9.png)
3. 逐个完成初始化

## 常见问题

#### 浏览器打开IP地址，无法访问 Ranzhi（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 Ranzhi 数据？

部署包内置 MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 Ranzhi 数据？

可以

#### Ranzhi 如何发送邮件？

Ranzhi支持第三方的SMTP发送邮件模式，具体如下：

1. 后台管理 -> 发信设置 ->编辑配置，进入邮箱配置

2. 以 163 邮箱为例，根据下图的设置，完成SMTP参数的设置
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ranzhi/ranzhi-smtp-websoft9.png)

3. 设置完成后，请点击“Send Test Email”测试设置是否成功

> 以上参数设置以163邮箱为例，不同SMTP提供商的设置略有差异，请务必明确您所使用的SMTP所要求的设置方式。Password 处填写邮箱密码 还是 授权码，这个需要严格参考SMTP提供商的说明。

#### Ranzhi 后台的管理员密码忘了怎么办？

使用 phpMyAdmin 登录 MySQL, 修改 Ranzhi 对应的数据库 `sys_user`表，具体参考官方文档：[如何重置密码？](https://www.ranzhi.org/book/faq1/78.html#4)

#### Ranzhi 如何备份？

##### 然之后台手工备份（建议） 
超级管理员登录然之---后台管理---系统---备份 页面点击 备份 按钮进行备份。
* 可以设置备份保存的天数。
* 备份的数据和附件会显示具体的路径名，方便查看。
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ranzhi/ranzhi-manulbk-websoft9.png)

##### 然之后台计划任务呢备份（必做）
也可以在后台管理---系统---计划任务里，打开计划任务自动备份数据和附件。
计划任务列表里，你可以编辑定时备份任务的时间和频率。
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ranzhi/ranzhi-autobk-websoft9.png)

#### Ranzhi 如何升级？

请参考：[官方升级文档](http://www.ranzhi.org/book/ranzhi/ranzhiupgrade-7.html)