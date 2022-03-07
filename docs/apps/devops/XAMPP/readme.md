---
sidebar_position: 1
slug: /xampp
tags:
  - XAMPP
  - DevOps
---

# 快速入门

[XAMPP Stack](https://www.apachefriends.org/index.html)（Linux/Windows-Apache-MySQL-PHP-Perl）集成包是全球最流行的Web运行环境之一，基于免费、开源软件构建。框架中包括：Linux或Windows操作系统，Apache Web服务器软件、Tomcat Web服务器软件，MySQL数据库，Java、Perl、PHP编程语言等多种核心组件以及其他相关辅助组件。通过组合、优化和兼容性处理，将所有组件打包成一个高性能、高集成性的Web运行环境解决方案包，保证能够兼容运行绝大部分PHP应用程序。

![](https://oss.aliyuncs.com/photogallery/photo/1904996544835414/4537/d72fb19c-1661-403c-8e0a-929652474de6.png)



在云服务器上部署 XAMPP 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问网站，请先到 **域名控制台** 完成一个域名解析

## 账号密码

## XAMPP 入门向导

XAMPP环境中部署网站主要分为5个步骤：

**①**上传网站代码-&gt;**③**配置域名（根据情况而定）-&gt;**④**增加网站对应的数据库（根据程序要求而定）-&gt;**⑤**完成安装向导

XAMPP环境中只部署一个网站还是多个网站、有无域名这两种情况对应的部署操作细节略有不一样，下面分别说明：

### 部署第一个网站

如果您打算此服务器上只部署一个网站或应用，建议采用此方式：

1.  远程桌面到Windows服务器，将网站源文件拷贝到根目录
2.  如果没有可用域名，请直接通过 **http://公网IP**  的方式来访问应用
3.  如果有可用的域名，请完成 **《域名配置》** 后通过 **http://公网IP** 的方式来访问应用
4.  如果在安装向导过程中提示数据库无法自动创建，需要通过 http://ip/phpmyadmin 创建数据库

网站默认根目录为：C:\xampp\htdocs

### 部署第二个网站

1. 在 WWW 下新建一个网站目录，假设命名为“mysite2”
2. 将网站源文件上传到：*C:\xampp\htdocs\mysite2* 
3. 根据是否有域名，选择一种操作：
	* **有可用域名**，请将下面 **VirtualHost** 模板拷贝到 httpd-vhosts.conf 中，将ServerName , ServerAlias , DocumentRoot , ErrorLog,CusomLog , Directory 等参数相关值更换成你的实际内容。

    ```
    NameVirtualHost *:80

    <VirtualHost *:80>
    DocumentRoot "C:/xampp/htdocs/"
    ServerName localhost
    </VirtualHost>

    <VirtualHost *:80>
       ServerAdmin help@websoft9.com
        DocumentRoot "C:/xampp/htdocs/mysite2"
        ServerName www.mydomain.com
       ErrorLog "logs/www.mydomain.com-error.log"
        CustomLog "logs/www.mydomain.com-access.log" common

       <Directory "C:/xampp/htdocs/mysite2" >
        Options Indexes FollowSymLinks
      AllowOverride all
        Order allow,deny
         Allow from all
       </Directory>
    </VirtualHost>
    ```
	 * **无可用域名**，请将下面 **Alias** 模板拷贝到 httpd-vhosts.conf 中，将Alias，Directory等参数相关之更换成你的实际内容。
      ```
      Alias /mysite2 C:/xampp/htdocs\mysite2
      <Directory "C:/xampp/htdocs\mysite2">
	  Options Indexes FollowSymlinks
	  AllowOverride All
	  Require all granted
	  </Directory>
      ```
4. 保存 httpd-vhosts.conf，然后重启Apache服务。

5. 本地浏览器访问：http://域名 或 http://服务器公网IP/mysite2  就可以访问本次安装的网站

> 最后我们温故而知新，总结了WAMP部署网站步骤： 1.上传网站代码-&gt;2.绑定域名（非必要）3.新增站点配置或修改示例站点配置-&gt;4.增加网站对应的数据库（非必要）-&gt;5.进入安装向导

### 附：配置文件项说明

|  项  |  说明  |
| --- | --- |
|  ServerName  |  主域名   |
|  ServerAlias  |   辅域名，可以不填 |
|   DocumentRoot |  真实的网站存放目录，务必准确无误  |
|  Directory |  真实的网站存放目录，务必准确无误  |
|  ErrorLog  | 错误日志路径，路径务必准确无误   |
|  CustomLog  | 访问日志路径，路径务必准确无误  |


## 常用操作

### 服务启动停止

*服务随操作系统自动启动，如果手工修改配置参数后，需要重新启停服务。**

*   **方法一**：远程桌面点击XAMPP图标，然后点击需要启动或停止的服务 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xampp/xampp-ss-websoft9.png)
*   **方法二**：打开xampp安装的文件夹，点击对应的服务启停exe/bat文件 
	 MySQL start: \xampp\xampp_start.exe 
     MySQL stop: \xampp\xampp_stop.exe 
     Apache start: \xampp\apache_start.bat 
     Apache stop: \xampp\apache_stop.bat 
     MySQL start: \xampp\mysql_start.bat 
     MySQL stop: \xampp\mysql_stop.bat 
     Mercury Mailserver start: \xampp\mercury_start.bat 
     Mercury Mailserver stop: \xampp\mercury_stop.bat 
     FileZilla Server start: \xampp\filezilla_start.bat 
     FileZilla Server stop: \xampp\filezilla_stop.bat

### PHP 配置与管理

与PHP相关的操作

#### 修改 PHP 配置

通过修改C:\xampp\php\php.ini即可修改php配置：

*   何修改系统最大响应时间？将max_execution_time设置成你需要的值
*   如何修改上传文件大小限制？将post_max_size = 64M,upload_max_filesize = 64M设置成你需要的值

修改后重启Apache

#### 升级 PHP 版本

待续…

#### 安装 PHP 扩展

待续…

### 域名绑定


**XAMPP**环境下，请远程桌面到服务器，打开C:\xampp\apache\conf\extra\httpd-vhosts.conf文件，将其中的ServerName,ServerAlias的值替换成你的域名信息，重启Apache服务后生效。

### SSL/HTTPS

在设置https访问之前，请提前开启服务器安全组的443端口，如果不开启，https访问是不可用的。

#### HTTPS访问配置（需自己准备证书）

如果您已经申请了证书（请保证证书可用），请参考如下的配置方式：

1.  将证书上传到服务器证书目录：conf/ssl.*（*为目录后缀名）
2.  打开C:\xampp\apache\conf\extra\httpd-ssl.conf配置文件
3.  找到httpd-ssl.conf中的https配置内容模板（下面是去掉注释后的效果）

    ```
    <VirtualHost _default_:443>
    DocumentRoot "C:/xampp/htdocs"
    ServerName www.example.com:443
    ServerAdmin admin@example.com
    ErrorLog "C:/xampp/apache/logs/error.log"
    TransferLog "C:/xampp/apache/logs/access.log"

    SSLEngine on
    SSLCertificateFile "conf/ssl.crt/server.crt"
    SSLCertificateFile "conf/ssl.crt/server.crt"
    SSLCertificateFile "conf/ssl.crt/server.crt"

    #<Location />
    #SSLRequire (    %{SSL_CIPHER} !~ m/^(EXP|NULL)/ \
    #            and %{SSL_CLIENT_S_DN_O} eq "Snake Oil, Ltd." \
    #            and %{SSL_CLIENT_S_DN_OU} in {"Staff", "CA", "Dev"} \
    #            and %{TIME_WDAY} >= 1 and %{TIME_WDAY} <= 5 \
    #            and %{TIME_HOUR} >= 8 and %{TIME_HOUR} <= 20       ) \
    #           or %{REMOTE_ADDR} =~ m/^192\.76\.162\.[0-9]+$/
    #</Location>

    <FilesMatch "\.(cgi|shtml|phtml|php)$">
        SSLOptions +StdEnvVars
    </FilesMatch>
    <Directory "C:/xampp/apache/cgi-bin">
        SSLOptions +StdEnvVars
    </Directory>

    BrowserMatch "MSIE [2-5]" \
             nokeepalive ssl-unclean-shutdown \
             downgrade-1.0 force-response-1.0

    CustomLog "C:/xampp/apache/logs/ssl_request.log" \
              "%t %h %{SSL_PROTOCOL}x %{SSL_CIPHER}x \"%r\" %b"

    </VirtualHost>     
    ```

4.  修改配置文件中相关项，并保存 ServerName  #主域名，务必修改 DocumentRoot #网站路径，务必填写网站实际路径，例如:C:/xampp/htdocs/wordpress SSLCertificateFile #证书File，务必填写网站实际路径 SSLCertificateKeyFile #证书KeyFile，务必填写网站实际路径 SSLCertificateChainFile #证书ChainFile，务必填写网站实际路径 注意：证书的后缀一般是：.crt或者 .pem，私钥的后缀是：.key
5.  重启Apache服务 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xampp/xampp-ss-websoft9.png)

#### 证书FAQ

证书的申请注意事项：

*   免费证书只能用于明细域名,例如: buy.example.com,或next.buy.example.com,
*   example.com是通配符域名方式，不能用于申请免费证书
*   申请证书的时候，请先解析好域名，有些证书会绑定域名对应的IP地址，即一旦申请后，IP地址不能更换，否则证书不可用

### 设置伪静态

Apache开启为静态的步骤如下：
1. 在 C:\xampp\apache\conf\httpd.conf 文件中查找以下语句 LoadModule rewrite_module modules/mod_rewrite.so，若前面有 # 号则需要将其去掉，使之支持 mod_rewrite 模块；
2. 再查找 AllowOverride 语句，若其后为 None 则将其更改为 ALL 使apache支持 .htaccess 文件,若已经是 ALL 则不需要变动；  
4. 重启 Apache，这样就可以在你的 PHP 项目根目录下建立 .htaccess 文件开启伪静态了。

> 一般情况下，如果您的网站是基于第三方开源网站（如：wordpress等）建立的，则网站目录下都会自带 .htaccess 文件，不需要另外自己设置。

### 修改网站根目录

如果你希望将网站根目录设置到D盘或不喜欢现在根目录的位置，这个时候就需要修改网站默认根目录了。WAMP环境的根目录是可以被修改的，具体只需2个步骤：

1.  修改配置文件：C:\xampp\apache\conf\extra\httpd-vhosts.conf，将 DocumentRoot 和 Directory 的值修改成你网站的路径

2.   保存后，重启Apache服务

### 网站迁移

网站迁移的基本步骤如下：

1. 搭建新环境
2. 迁移代码
3. 迁移数据库
4. 解析域名
5. 测试可用
6. 正式发布

### 将数据转移到数据盘

1. 转移网站数据
默认情况下 C:\xampp\htdocs 是在系统盘的，当需要转移到数据盘，步骤如下：
	1. 停止 Apache 服务
	2. 将 C:\xampp\htdocs 下所有文件拷贝新的目录，假如为：D:\wwwroot
	3. 修改 C:\xampp\apache\conf\extra\httpd-vhosts.conf 文件，	将“C:\xampp\htdocs”修改为“D:\wwwroot”
	4. 重启Apache后生效

2. 转移数据库文件
	1. 停止MySQL服务
	2. 将 C:\xampp\mysql\data 下所有文件拷贝到新目录，例如：D:\data
	3. 修改 C:\xampp\mysql\my.ini 文件，将以下语句
		~~~
        datadir="C:\xampp\mysql\data"
        log-error="C:\xampp\mysql\data\mysqld.log"
        ~~~
        修改为：
        ~~~
        datadir="D:/data"
        log-error="D:/data/mysqld.log"
        ~~~
     4. 重启MySQL服务

### SMTP

应用中发送邮件是一个很常见的功能。经过大量用户实践反馈，只推荐一种发邮件的方式，即安装邮件插调用第三方邮件系统的STMP相关账号来进行邮件发送。

SMTP发送邮件有三个步骤：

1. 申请一个可用的[SMTP服务](http://service.mail.qq.com/cgi-bin/help?id=28)（例如：stmp.qq.com，端口号465，账号...）
2. 打开应用软件中的SMTP配置界面（类似WordPress默认没有SMTP配置项，则需要额外安装一个SMTP插件）
3. 测试SMTP

> 请忘掉在本机上安装sendmail等邮件服务器的方案，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，导致不稳定、不容易维护、不好诊断问题。

#### SMTP测试失败

如果使用第三方提供的SMTP服务（如qq邮箱、网易邮箱等），配置也没有问题，但是仍然无法发送邮件。请检查如下两个问题：

1.  登录服务器，验证是否可以连接SMTP，按 Windows+R 输入 CMD 打开 CMD 命令窗口，命令如下
~~~
//测试qq邮箱 端口有465和587
telnet smtp.qq.com 465

//测试网易邮箱 端口有465和994
telnet smtp.163.com 465
~~~
如果出现一个只有光标没有任何内容的界面，这样的反馈信息说明是可以连接的。

> 注意：本地Telnet测试成功，不代表服务器Telnet成功，因为您的服务器IP地址由于某些原因可能会被STMP服务器列入黑名单。

2.  需要了解你所使用的STMP功能是否调用了PHP软件包（或扩展类）
   	* php官方提供的mail()类，这个类不支持SMTP验证
    * php扩展包-[PHPMailer](https://github.com/PHPMailer/PHPMailer)，这个类功能比较全面

2.  安全组（出设置）禁止外部访问
3.  系统iptables，firewall设置关闭了465等端口
4.  php_openss版本过低或者没有安装，php_openssl的CA证书确实或异常

### 重置数据库root密码

若 MySQL 的 root 用户密码忘记了，可以按照以下步骤来重置密码：
1. 停止 MySQL 服务
   
2. 在命令行窗口用安全模式启动 mysql ,执行命令后窗口可能没有反应，这时请注意，不要关闭该窗口，再打开另一个命令行窗口	
   
   ~~~
    mysqld --skip-grant-tables
   ~~~
   
3. 在新的命令行窗口执行以下命令，免密码登录到 MySQL
   
   ~~~
   mysql -uroot
   ~~~
4. 执行以下三条命令，重置密码（这里将密码重置为`123456`）
   ~~~
   use mysql;
   
   //适用于 MySQL5.7
   update user set authentication_string=password("123456") where user="root";
   
   flush privileges;
   ~~~
   如果MySQL的版本是5.5或5.6，则执行以下三条命令：
   ~~~
   use mysql;
   
   //适用于 MySQL5.5和5.6 
   update mysql.user set password=password('123456') where user='root';  
   
   flush privileges;
   ~~~
   
5. 打开任务管理器，在“进程”中结束 mysqld.exe 进程，然后重新启动MySQL服务


## 异常处理

#### 服务无法启动？

请检查网站路径和日志文件路径准确无误（特别是日志文件路径非常容易出错）

#### 找不到示例网站？

历史版本中历史网站路径与文档中描述有差异
历史版本的示例网站路径为：C:\websoft9\wampstack\apache2\htdocs

#### 总是显示9Panel？

请删除示例中的index文件，并清空浏览器缓存
