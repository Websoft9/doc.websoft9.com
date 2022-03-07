---
sidebar_position: 1
slug: /phpstudy
tags:
  - phpStudy
  - DevOps
---

# 快速入门

[phpStudy](https://www.xp.cn/) 是一个PHP环境集成包，支持Apache+Nginx+LightTPD+IIS等Web服务器，支持php5.2/php5.3/php5.5/php7.0自由切换。全部通过图形化界面实现，配置和管理多个网站、配置域名、管理服务、管理端口等

![](https://oss.aliyuncs.com/netmarket/product/f5117a63-085a-4dd3-80d0-414852eb6529.jpg)


在云服务器上部署 phpStudy 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问网站，请先到 **域名控制台** 完成一个域名解析

## 账号密码

## phpStudy 入门向导

### phpStudy环境中部署网站

phpStudy环境中部署网站主要分为5个步骤： **①**上传网站代码-&gt;**②**配置域名（非必要）-&gt;**③**增加网站对应的数据库（非必要）-&gt;**⑤**完成安装向导

注意：部署一个网站还是多个网站、有无域名这两种情况对应的部署操作细节略有不一样，下面分别说明：

#### 部署第一个网站

如果您打算此服务器上只部署一个网站或应用，建议采用此方式：

1.  远程桌面到Windows服务器，将网站源文件拷贝到根目录
2.  如果没有可用域名，请直接通过 **http://公网IP**  的方式来访问应用
3.  如果有可用的域名，请完成 **《域名配置》** 后通过 **http://公网IP** 的方式来访问应用
4.  如果在安装向导过程中提示数据库无法自动创建，需要通过 http://ip/phpmyadmin 创建数据库

网站默认根目录为：C:\websoft9\phpStudy\PHPTutorial\WWW

#### 部署第二个网站

1. 在 WWW 下新建一个网站目录，假设命名为“mysite2”
2. 将网站源文件上传到：*C:\websoft9\phpStudy\PHPTutorial\WWW\mysite2* 
3. 根据是否有域名，选择一种操作：
     * **有可用域名**，请将下面 **VirtualHost** 模板拷贝到 httpd-vhosts.conf 中，将ServerName , ServerAlias , DocumentRoot , ErrorLog,CusomLog , Directory 等参数相关值更换成你的实际内容。
       ```
       <VirtualHost *:80>
       ServerName www.mydomain.com
       ServerAlias other.mydomain.com
       DocumentRoot "C:\websoft9\phpStudy\PHPTutorial\WWW\mysite2"
       # ErrorLog "logs\mydomain.com_error_apache.log"
       # CustomLog "logs\mydomain.com_error_apache.log" common
       <Directory "C:\websoft9\phpStudy\PHPTutorial\WWW\mysite2">
       Options Indexes FollowSymlinks
       AllowOverride All
       Require all granted
       </Directory>
       </VirtualHost>
        ```
    * **无可用域名**，请将下面 **Alias** 模板拷贝到 httpd-vhosts.conf 中，将Alias，Directory等参数相关之更换成你的实际内容。
      ```
      Alias /mysite2 C:\websoft9\phpStudy\PHPTutorial\WWW\mysite2
      <Directory "C:\websoft9\phpStudy\PHPTutorial\WWW\mysite2">
	  Options Indexes FollowSymlinks
	  AllowOverride All
	  Require all granted
	  </Directory>
      ```
3. 保存 httpd-vhosts.conf，然后重启Apache服务。

4. 本地浏览器访问：http://域名 或 http://服务器公网IP/mysite2  就可以访问本次安装的网站

> 最后我们温故而知新，总结了WAMP部署网站步骤： 1.上传网站代码-&gt;2.绑定域名（非必要）3.新增站点配置或修改示例站点配置-&gt;4.增加网站对应的数据库（非必要）-&gt;5.进入安装向导

#### 附：配置文件项说明

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

修改网站配置之后，有时候需要完成相关服务的启动和停止。phpStudy提供了服务重启功能：

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/phpstudy/phpstudy-restartapache-websoft9.png)

### PHP 配置与管理

使用PHP应用程序的时候，php组件的启用或停用、邮件设置、上传文件大小等控制都会涉及修改php配置文件。phpStudy集成了一个PHP配置管理器。

点击phpStudy-&gt;其他选项菜单-&gt;PHP扩展及设置，就进入了PHP配置与管理功能界面：

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/phpstudy/phpstudy-phpset-websoft9.png)

#### 切换 PHP 版本

切换PHP版本，只需两步：

1.  选择版本 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/phpstudy/phpstudy-version-websoft9.png)
2.  重启服务

### 域名绑定

请远程登录到Windows服务器后，通过phpStudy面板绑定域名，具体如下：

1. phpStudy-&gt;其他选项菜单-&gt;站点域名管理，新增或修改，弹出域名设置界面 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/phpstudy/phpstudy-adddomain-websoft9.png)
2. 填写完整后，点击“保存设置并生成配置文件”
3. 重启Apache服务 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/phpstudy/phpstudy-restartapache-websoft9.png)

**说明：**新增或修改的操作是一样的

### SSL/HTTPS

在设置https访问之前，请开启安全组的443端口，如果不开启，https访问是不可用的。

如果您已经申请了证书（请保证证书可用），请参考如下的配置方式：

1.  将证书上传到服务器证书目录：C:\wwwrootcert（没有cert目录可以自己新建）
2.  打开配置文件：C:\websoft9\phpStudy\PHPTutorial\Apache\conf\extra\httpd-vhosts.conf
3.  拷贝下面的*https配置文件模板* 到配置文件中，并保存

    ```
    <VirtualHost *:443>
       ServerName www.mydomain.com
       # ServerAlias other.mydomain.com
       DocumentRoot "C:\websoft9\phpStudy\PHPTutorial\WWW"
       ErrorLog " logs\mydomain.com_error_apache.log"
       CustomLog "logs\mydomain.com_error_apache.log" common
       <Directory "C:\websoft9\phpStudy\PHPTutorial\WWW">
       Options Indexes FollowSymlinks
       AllowOverride All
       Require all granted
       </Directory>
        SSLEngine on
        SSLCertificateFile  C:\wwwroot\cert\server.crt
        SSLCertificateKeyFile  C:\wwwroot\cert\server.key
        SSLCertificateChainFile  C:\wwwroot\cert\server-ca.crt
     </VirtualHost>
    ```

4.  修改配置文件中相关项，并保存。
   ServerName  为主域名，务必修改 
   ServerAlias   为副域名，可选项 
   DocumentRoot 网站路径，务必填写网站实际路径
   Directory 网站路径，务必填写网站实际路径
   SSLCertificateFile 证书，务必填写实际存放路径 
   SSLCertificateKeyFile 证书私钥，务必填写实际存放路径 
   SSLCertificateChainFile 证书链（CA文件），务必填写实际存储路径 
   
 > 注意：证书的后缀一般是：.crt或者 .pem，私钥的后缀是：.key

5. 保存httpd-vhosts.conf，然后重启Apache服务。

#### 证书FAQ

证书的申请注意事项：

*   免费证书只能用于明细域名,例如: buy.example.com,或next.buy.example.com,
*   example.com是通配符域名方式，不能用于申请免费证书
*   申请证书的时候，请先解析好域名，有些证书会绑定域名对应的IP地址，即一旦申请后，IP地址不能更换，否则证书不可用

### 设置伪静态

Apache开启为静态的步骤如下：
1. 在 C:\websoft9\phpStudy\PHPTutorial\Apache\conf\httpd.conf 文件中查找以下语句 LoadModule rewrite_module modules/mod_rewrite.so，若前面有 # 号则需要将其去掉，使之支持 mod_rewrite 模块；
2. 再查找 AllowOverride 语句，若其后为 None 则将其更改为 ALL 使apache支持 .htaccess 文件,若已经是 ALL 则不需要变动；  
4. 重启 Apache，这样就可以在你的 PHP 项目根目录下建立 .htaccess 文件开启伪静态了。

> 一般情况下，如果您的网站是基于第三方开源网站（如：wordpress等）建立的，则网站目录下都会自带 .htaccess 文件，不需要另外自己设置

### 修改网站根目录

也许你希望将网站根目录设置到D盘或不喜欢现在根目录的位置，这个时候就需要修改网站默认根目录了。WAMP环境的根目录是可以被修改的，具体只需2个步骤：

1.  打开phpStudy-&gt;其他选项菜单-&gt;打开配置文件-&gt;vhosts-ini ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/phpstudy/phpstudy-vhost-websoft9.png)
2.  将配置文件中C:\websoft9\phpStudy\PHPTutorial\WWW的路径改成你的路径（例如：D:\wwwroot）

    ```
    <VirtualHost _default_:80>
    DocumentRoot "C:\websoft9\phpStudy\PHPTutorial\WWW"
      <Directory "C:\websoft9\phpStudy\PHPTutorial\WWW">
        Options -Indexes -FollowSymLinks +ExecCGI
        AllowOverride All
        Order allow,deny
        Allow from all
        Require all granted
      </Directory>
    </VirtualHost>

    <VirtualHost *:80>
        DocumentRoot "C:\websoft9\phpStudy\PHPTutorial\WWW\9panel"
        ServerName www.example.com
        ServerAlias example.com
      <Directory "C:\websoft9\phpStudy\PHPTutorial\WWW\9panel">
          Options FollowSymLinks ExecCGI
          AllowOverride All
          Order allow,deny
          Allow from all
         Require all granted
      </Directory>
    </VirtualHost>

    ```

3.  将原来WWW文件夹的phpmyadmin,9panel文件夹拷贝到自定义的目录
4.  phpStudy-&gt;服务管理器-&gt;重启全部


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
默认情况下 C:\websoft9\phpStudy\PHPTutorial\WWW 是在系统盘的，当需要转移到数据盘，步骤如下：
	1. 停止 Apache 服务
	2. 将 C:\websoft9\phpStudy\PHPTutorial\WWW 下所有文件拷贝新的目录，假如为：D:\wwwroot
	3. 修改 C:\websoft9\phpStudy\PHPTutorial\Apache\conf\extra\httpd-vhosts.conf 文件，	将“C:\websoft9\phpStudy\PHPTutorial\WWW”修改为“D:\wwwroot”
	4. 重启Apache后生效

2. 转移数据库文件
	1. 停止MySQL服务
	2. 将 C:\websoft9\phpStudy\PHPTutorial\MySQL\data 下所有文件拷贝到新目录，例如：D:\data
	3. 修改 C:\websoft9\phpStudy\PHPTutorial\MySQL\my.ini 文件，将以下语句
		~~~
        datadir="C:\websoft9\phpStudy\PHPTutorial\MySQL\data"
        log-error="C:\websoft9\phpStudy\PHPTutorial\MySQL\data\mysqld.log"
        ~~~
        修改为：
        ~~~
        datadir="D:\data"
        log-error="D:\data\mysqld.log"
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
```
//测试qq邮箱 端口有465和587
telnet smtp.qq.com 465

//测试网易邮箱 端口有465和994
telnet smtp.163.com 465
```
如果出现一个只有光标没有任何内容的界面，这样的反馈信息说明是可以连接的。

> 注意：本地Telnet测试成功，不代表服务器Telnet成功，因为您的服务器IP地址由于某些原因可能会被STMP服务器列入黑名单。

2.  需要了解你所使用的STMP功能是否调用了PHP软件包（或扩展类）
   	* php官方提供的mail()类，这个类不支持SMTP验证
    * php扩展包-[PHPMailer](https://github.com/PHPMailer/PHPMailer)，这个类功能比较全面

2.  安全组（出设置）禁止外部访问
3.  系统iptables，firewall设置关闭了465等端口
4.  php_openss版本过低或者没有安装，php_openssl的CA证书确实或异常

### 重置数据库root密码？

通过：其他选项菜单-&gt;MySQL工具-&gt;重置密码（忘记时），可以重新修改密码

## 异常处理

#### 服务无法启动？

请检查网站路径和日志文件路径准确无误（特别是日志文件路径非常容易出错）

#### 找不到示例网站？

历史版本中历史网站路径与文档中描述有差异
历史版本的示例网站路径为：C:\websoft9\wampstack\apache2\htdocs

#### 总是显示9Panel？

请删除示例中的index文件，并清空浏览器缓存
