---
sidebar_position: 1
slug: /suitecrm
tags:
  - SuiteCRM
  - CRM
  - 客户成功
---

# 快速入门

[SuiteCRM](https://suitecrm.com/) 是一个屡获殊荣的企业级的、强大的、可定制的，免费的CRM系统。包括市场、销售过程管理、协作管理、工作流、门户等功能模块。所有功能全部开源，完全具备商业CRM软件媲美的功能和架构。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-ui.png)


## 演示

SuiteCRM 官网提供了试用环境，您可以直接试用

* 演示地址：https://suitecrm.com/demo/

> 免责说明：此处仅提供SuiteCRM官方的演示，不保证与 Websoft9 部署包功能完全一致，若演示过程中若需要填写个人资料、获取Cookie等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此可能存在的商业纠纷与我司无关。


在云服务器上部署 SuiteCRM 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Moodle，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号

### SuiteCRM

在初始化安装的时候由用户自行设置

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

> 需要登录MySQL，请参考 [MySQL可视化管理](#MySQL-数据管理)

## SuiteCRM 安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-accept-websoft9.png)

2. 环境检测会自动通过，选择Next进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-check-websoft9.png)

3. 系统进入配置数据库界面（[查看数据库账号密码](#账号密码)）。然后设置管理员账号，牢记之，点击“安装”

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-dbconf-websoft9.png)
4. 系统进入安装过程，耐心等待，安装成功后系统会进行提示

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-login-websoft9.png)
5. 开始体验后台
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-backend-websoft9.png)

> 需要了解更多SuiteCRM 的使用，请参考官方文档：[EspoCRM Documentation](https://suitecrm.com/wiki/index.php/Main_Page)

## 常用操作

### 域名绑定

当服务器上只有一个网站时，不做域名绑定也可以访问网站。但从安全和维护考量，**域名绑定**不可省却。

以示例网站为例，域名绑定操作步骤如下：

1. 确保域名解析已经生效  
2. 使用 WinSCP 等工具登录云服务器
3. 修改 [Apache虚拟机主机配置文件](/维护参考.md#apache)，将其中的 **ServerName** 项的值修改为你的域名
   ```text
   <VirtualHost *:80>
   ServerName www.mydomain.com # 此处修改为你的域名
   DocumentRoot "/data/wwwroot/mysite2"
   ...
   ```
4. 保存配置文件，重启 [Apache 服务](/维护参考.md#apache-1)


### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

SuiteCRM 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 快速参考

如果你想使用免费证书，只需在服务器中运行一条命令`certbot`就可以启动证书部署

如果你已经申请了商业证书，只需三个步骤，即可完成HTTPS配置

#### SuiteCRM(LAMP)

SuiteCRM(LAMP) 即运行环境采用 **Apache** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/httpd/conf.d/vhost.conf* ，插入如下的 **HTTPS 配置项** 到配置文件中
   ``` shell
      #-----HTTPS template start------------
      <VirtualHost *:443>
       ServerName  mysite1.yourdomain.com
       DocumentRoot "/data/wwwroot/mysite1"
       #ErrorLog "logs/mysite1.yourdomain.com-error_log"
       #CustomLog "logs/mysite1.yourdomain.com-access_log" common
       <Directory "/data/wwwroot/mysite1">
       Options Indexes FollowSymlinks
       AllowOverride All
       Require all granted
       </Directory>
       SSLEngine on
       SSLCertificateFile  /data/cert/mysite1.yourdomain.com.crt
       SSLCertificateKeyFile  /data/cert/mysite1.yourdomain.com.key
       SSLCertificateKeyFile  /data/cert/mysite1.yourdomain.com.key
       </VirtualHost>
      #-----HTTPS template end------------
   ```
3. 修改其中的 ServerName, DocumentRoot, ErrorLog, CusomLog, Directory等项的值（[修改参考](/zh/solution-deployment.md#virtualhost)）
4. 保存 vhost.conf，然后在 WinSCP 中运行重启服务命令 或 云控制台重启服务器 ：
    ~~~
    # 重启Apache服务命令
    systemctl restart httpd
    ~~~
5. 保存， [重启 Apache 服务](/维护参考.md#apache-1)


#### 专题指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

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

### 安装中文包

SuiteCRM默认安装只有英文，需要中文或其他语言，需要下载语言包，然后通过后台进行安装，以中文为例，具体如下：

1.  下载[中文语言包](https://crowdin.com/project/suitecrmtranslations/zh-CN) – 存到本地电脑上
2.  以Admin身份进入SuiteCRM，进入 “Module loader”
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-lmodule-websoft9.png)
3.  Upload file->Install it->Commit
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-linstall-websoft9.png)
4.  Go to “Admin” enter “Repair” and apply “Quick repair and rebuild” for languages
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-repair-websoft9.png)
5.  退出 SuiteCRM
6.  先选择所需的语言，再登录
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/suitecrm/suitecrm-logincn-websoft9.png)

### MySQL 数据管理

SuiteCRM 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP/phpmyadmin*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理

#### 浏览器打开IP地址，无法访问 SuiteCRM（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 SuiteCRM 数据？

部署包内置 MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 SuiteCRM 数据？

可以