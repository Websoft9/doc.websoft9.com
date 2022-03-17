---
slug: /lamp/installation/zh/suitecrm
---


# SuiteCRM

本文档可供使用了 **SuiteCRM 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 SuiteCRM 参考。

SuiteCRM是一个屡获殊荣的企业级的、强大的、可定制的，免费的CRM系统。包括市场、销售过程管理、协作管理、工作流、门户等功能模块。所有功能全部开源，完全具备商业CRM软件媲美的功能和架构。[官方演示](https://suitecrm.com/demo/)

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-ui.png)

## 准备

在开始 SuiteCRM 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## SuiteCRM 安装到服务器

**如果你使用的是 *SuiteCRM 镜像*，本节请忽略，直接阅读下一节 【SuiteCRM 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 SuiteCRM 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 SuiteCRM 系统增加一个数据库，假如名称为：`suitecrm`
3. 到 SuiteCRM 官方[下载源码](https://suitecrm.com/download/)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 SuiteCRM 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## SuiteCRM 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-accept-websoft9.png)

2. 环境检测会自动通过，选择Next进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-check-websoft9.png)

3. 系统进入配置数据库界面（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）。然后设置管理员账号，牢记之，点击“安装”

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-dbconf-websoft9.png)
4. 系统进入安装过程，耐心等待，安装成功后系统会进行提示

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-login-websoft9.png)
5. 开始体验后台
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-backend-websoft9.png)

> 需要了解更多SuiteCRM 的使用，请参考官方文档：[SuiteCRM Documentation](https://docs.suitecrm.com/)

## 常见问题

#### 浏览器打开IP地址，无法访问 SuiteCRM（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 SuiteCRM 数据？

部署包内置 MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 SuiteCRM 数据？

可以

#### SuiteCRM如何安装中文包？

SuiteCRM默认安装只有英文，需要中文或其他语言，需要下载语言包，然后通过后台进行安装，以中文为例，具体如下：

1.  下载[中文语言包](https://crowdin.com/project/suitecrmtranslations/zh-CN) – 存到本地电脑上
    - 该网站需要先注册/登录，然后加入 join 到 SuiteCRM 项目，等待平台审核后，才能下载。
    ![join](https://libs.websoft9.com/Websoft9/blog/tmp/suitecrm/zh/suitecrm-translation-zh00-websoft9.png)
    ![down](https://libs.websoft9.com/Websoft9/blog/tmp/suitecrm/zh/suitecrm-translation-zh01-websoft9.png)
    
    - 上述方式需要等待7天左右时间，因此也可以到第三方网站 [sourceforge](https://sourceforge.net/projects/suitecrmtranslations/files/) 下载对应版本的语言包


2.  以Admin身份进入SuiteCRM，进入 “Module loader”
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-lmodule-websoft9.png)
3.  Upload file->Install it->Commit
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-linstall-websoft9.png)
4.  Go to “Admin” enter “Repair” and apply “Quick repair and rebuild” for languages
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-repair-websoft9.png)
5.  退出 SuiteCRM
6.  先选择所需的语言，再登录
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-logincn-websoft9.png)

#### SuiteCRM如何发送邮件？

SuiteCRM支持第三方的SMTP发送邮件模式，具体如下：

1. 打开SuiteCRM->Administartor->Admin->Email->Email Setting，打开邮件发送设置项（Outgoing Mail Configuration）

2. 选择匹配的SMTP服务商，参考下图完成SMTP（我们以163为例）；
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-smtp-2-websoft9.png)
	* SMTP Mail Server 处请填写 smtp 服务器的地址 ；
	* SMTP Port 处请填写正确的端口号；
	* Use SMTP Authentication 处选择发送邮件是否需要验证账号
	* Enable SMTP over SSL or TLS 处请邮件服务器支持的连接协议；
	* Use Name 处请输入自己的邮箱地址 ；
	* Password 处请输入SMTP授权码（不同于邮箱密码）
	* Allow users to use this account for... 处请勾选

> 以上参数设置以163为例，不同SMTP提供商的设置略有差异，请务必明确您所使用的SMTP所要求的设置方式。

3. 设置无误后，请点击“Send Test Email”进行测试以验证

另外，SuiteCRM安装过程（第三步）也可以设置SMTP，参考下图：

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-smtp-websoft9.png)

#### 修改了数据库密码SuiteCRM不能访问？

SuiteCRM 在安装的时候已经将数据库账号信息写到配置文件中，若后续修改数据库密码，配置文件不会自动更新。

只需要修改配置文件: */data/wwwroot/default/suitecrm/config.php*，对应的 `db_password` 参数即可

```
'dbconfig' => 
  array (
    'db_host_name' => 'localhost',
    'db_host_instance' => 'SQLEXPRESS',
    'db_user_name' => 'root',
    'db_password' => '123456',  //数据库密码
    'db_name' => 'suitecrm',
    'db_type' => 'mysql',
    'db_port' => '',
    'db_manager' => 'MysqliManager',
  ),
```
#### SuiteCRM 安装向导完整填写了数据库和管理员信息只有，点击【Next】没有任何反应？

**问题原因**：经过排查，发现【Next】动作有文件404（估计是Ajax触发），即有文件无法下载程序没有反应
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-noresponse-websoft9.png)

**解决方案**：临时购买一台香港地区的Windows服务器，在这个服务器打开浏览器安装SuiteCRM即可

