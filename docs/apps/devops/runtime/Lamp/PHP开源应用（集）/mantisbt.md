
---
slug: /lamp/installation/zh/mantisbt
---
# MantisBT

本文档可供使用了 **MantisBT 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 MantisBT 参考。

[MantisBT](https://mantisbt.org) 是一个基于PHP技术的轻量级的开源问题（缺陷）跟踪系统，具有项目管理及问题跟踪功能，实现了简单性和功能性之间的微妙平衡，简单易用，易安装，适团队协作使用。

[官方演示](http://mantisbt.org/demo.php)

## 准备

在开始 MantisBT 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## MantisBT 安装到服务器

**如果你使用的是 *MantisBT 镜像*，本节请忽略，直接阅读下一节 【MantisBT 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 MantisBT 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 MantisBT 系统增加一个数据库，假如名称为：`MantisBT`
3. 到 MantisBT 官方[下载源码](https://www.vtiger.com/open-source-crm)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 MantisBT 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## MantisBT 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
2. 系统自动完成许可协议、环境检测之后，进入配置数据库界面（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）。填写数据库信息后，点击“Install/Upgrade Database”，开始安装
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mantisbt/mantisbt-install001-websoft9.png)
3.  系统安装成功，系统提示，点击“Continue”进入下一步
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mantisbt/mantisbt-install002-websoft.png)
4.  进入后台登录（Mantis的默认管理员的用户名为administrator密码为root。）
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mantisbt/mantisbt-login-websoft9.png)![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mantisbt/mantisbt-loginpw-websoft9.png)
5.  开始体验后台（系统默认会建议您修改管理员密码）
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mantisbt/mantisbt-backend-websoft9.png)

> 需要了解更多 MantisBT 的使用，请参考官方文档：[MantisBT Documentation](http://www.mantisbt.org/documentation.php)

## 常见问题

#### 浏览器打开IP地址，无法访问 MantisBT（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 MantisBT 数据？

部署包内置 MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 MantisBT 数据？

可以

#### mantisbt邮件配置

下面以163邮箱为例进行配置说明

1. 使用 WinSCP 连接服务器
2. 编辑配置文件：*/data/wwwroot/default/mantisb/config_defaults_inc.php*
3. 找到以下参数并修改为如下所示(其中第2，3项修改为用户自己的邮箱地址和密码)： 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mantisbt/mantisbt-smtp-websoft9.png)  

   ```
   	    $g_enable_email_notification = ON ;  
		$g_phpMailer_method = PHPMAILER_METHOD_SMTP - SMTP; 
		$g_smtp_host = smtp.163.com;  
		$g_smtp_username = yourname@163.com;  
		$g_smtp_password = yourpassword;  
		$g_smtp_connection_mode = ssl  
		$g_smtp_port = 465;  
		$g_webmaster_email = 'yourname@163.com';  
		$g_from_email = 'yourname@163.com';  
		$g_return_path_email = 'yourname@163.com';   
   ```   

4. 运行修改权限命令
   ```
   chown -R apache: /data/wwwroot
   ```
5. 重启httpd服务
   ```
   systemctl restart httpd
   ```
6. 进入MantisBT，通过注册账号或修改密码的方式验证邮件是否可以发送

> 实践论证，MantisBT不支持免费版QQ邮箱，但支持企业版QQ邮箱下