---
sidebar_position: 1
slug: /typo3
tags:
  - Typo3
  - CMS
  - 站点管理
---

# 快速入门

[Typo3](https://typo3.org/) 是一个具有大型全球社区的开源企业内容管理系统，由TYPO3协会的大约900名成员支持,TYPO3被许多知名公司和组织使用。


在云服务器上部署 Typo3 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Moodle，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号

### Typo3

在初始化安装的时候由用户自行设置

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

> 需要登录MySQL，请参考 [MySQL可视化管理](#MySQL-数据管理)

## Typo3 安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-installstart-websoft9.png)

   在 Typo3 的根目录下，新建一个名称为 **FIRST_INSTALL** 的空白文件

2. 系统进入环境检测步骤，通过后进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty02.png)

3. 填写您的数据库参数（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty03.png)

4. 选择一个数据库 或 新建一个
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty04.png)

5. 设置管理员账号  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty05.png)

6. 安装完成，根据提示进入后台  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty06.png)

7. 登录后台   
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-login-websoft9.png)

8. Typo3 后台界面  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty08.png)


> 需要了解更多 Typo3 的使用，请参考官方文档：[Typo3 Documentation](https://typo3.org/help/documentation/)

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

CmsEasy 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 快速参考

如果你想使用免费证书，只需在服务器中运行一条命令`certbot`就可以启动证书部署

如果你已经申请了商业证书，只需三个步骤，即可完成HTTPS配置

#### Typo3(LAMP)

Typo3(LAMP) 即运行环境采用 **Apache** 作为 Web Server  

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

### 扩展管理

TYPO3 CMS 提供大量扩展，以增强系统功能。

1. 登录 Typo3后台，打开【ADMIN TOOLS】> 【Extensions】
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-BackendExtensionManager-websoft9.png)

2. 顶部下拉菜单中选择【Get extensions】查看扩展
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-BackendExtensionManagerInstall-websoft9.png)

3. 安装、更新扩展  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-BackendExtensionManagerExtensionVersions-websoft9.png)

### 模板管理

TYPO3 CMS 的模板管理非常细致，能够对模板最小元素进行细微的设置

1. 登录 Typo3后台，打开【WEB】>【Template】
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-template-websoft9.png)

2. 配置模板


### MySQL 数据管理

Typo3 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP/phpmyadmin*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理

#### 浏览器打开IP地址，无法访问 Typo3（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 Typo3 数据？

部署包内置 MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 Typo3 数据？

可以

