---
sidebar_position: 1
slug: /vtiger
tags:
  - VtigerCRM
  - CRM
  - 客户成功
---

# 快速入门

[VtigerCRM](https://vtiger.com)一套开源的客户关系管理系统(CRM)。基于SugarCRM开发的一个衍生版本。适合帮助中小企业从业务，从市场、销售、采购、库存、客服等全程跟踪客户，实现销售自动化，获取更多订单。  


## 演示

VtigerCRM 官网提供了试用环境，您可以直接试用

* 演示地址：https://www.vtiger.com/begin-free-trial/?plan=&email=

> 免责说明：此处仅提供 VtigerCRM 官方的演示，不保证与 Websoft9 部署包功能完全一致，若演示过程中若需要填写个人资料、获取Cookie等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此可能存在的商业纠纷与我司无关。

在云服务器上部署 VtigerCRM 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Moodle，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号

### VtigerCRM

在初始化安装的时候由用户自行设置

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

> 需要登录MySQL，请参考 [MySQL可视化管理](#MySQL-数据管理)

## VtigerCRM 安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install001-websoft9.png)

2. 系统进入环境检测步骤，通过后进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install002-websoft9.png)

3. 填写您的数据库参数（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install003-websoft9.png)

4. 数据库连接正确，点击“Next”进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install004-websoft9.png)

5. 选择一个匹配的行业，然后进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install005-websoft9.png)

6. 选择需要安装的模块，建议全部勾选上，然后进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install006-websoft9.png)

7. 系统提示选择货币、时区等
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install007-websoft9.png)

8. 点击“Get Started”，进入后台，体验系统的完整功能
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-backend-websoft9.png)


> 需要了解更多 VtigerCRM 的使用，请参考官方文档：[Vtiger Help](https://www.vtiger.com/help/)

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

VtigerCRM 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 快速参考

如果你想使用免费证书，只需在服务器中运行一条命令`certbot`就可以启动证书部署

如果你已经申请了商业证书，只需三个步骤，即可完成HTTPS配置

#### VtigerCRM(LAMP)

VtigerCRM(LAMP) 即运行环境采用 **Apache** 作为 Web Server  

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

VtigerCRM支持第三方的SMTP发送邮件模式，具体如下：

1. 打开VtigerCRM->设置按钮 > CRM Settings > Outgoing Server

2. 根据下图的设置，完成SMTP参数的设置
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-smtp-websoft9.png)
	* Server Name 处请填写 SMTP 服务器的地址（前面要加上 ssl:// , 后面要加端口号） ；
	* UseName 处请输入自己的邮箱地址 ；
	* Password 处请输入SMTP密码或授权码（不同于邮箱密码）
	* From Email 处请填写发送邮件地址（请保证与管理员一致）
	* Require Authentication 处勾选表示需要账号验证；

3. 设置完成后，请点击“Send Test Email”测试设置是否成功

> 以上参数设置以163邮箱为例，不同SMTP提供商的设置略有差异，请务必明确您所使用的SMTP所要求的设置方式。

### 安装中文包

VtigerCRM 支持多国语言，中文包安装方法如下：

1.  到官方[MarketPlace](https://marketplace.vtiger.com/app/listings)-Language Pack下载Chinese 简体中文语言包
2.  通过主菜单【Setting – CRM Setting – Module Management – Modules 】进入模块管理界面，点击右上角 “Import Module from Zip”按钮，进入导入模块管理界面，选择语言包进行导入。注意：导入页面这里有个 bug，导入时请直接选择语言包进行导入，不要勾选“ I accept with disclaimer and would like to proceed”否则无法导入。
3.  右上角点击你的登录用户名->My Preferences-> Edit，点击 Language 后面的下拉框选择语言，然后保存
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/change-language-websoft9.jpg)

注意：语言包也可以通过官方扩展应用市场安装。在 VtigerCRM 右上角点齿轮图标进入后台设置界面，左侧菜单栏点击 Extension Store 进入官方扩展应用市场。点击应用市场右上角的 Login to Marketplace 登录或者注册应用市场。搜索 Chinese 找到简体中文语言包进行安装。

### MySQL 数据管理

VtigerCRM 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP/phpmyadmin*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理

#### 浏览器打开IP地址，无法访问 VtigerCRM（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 VtigerCRM 数据？

部署包内置 MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 VtigerCRM 数据？

可以
