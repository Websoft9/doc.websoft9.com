---
sidebar_position: 1
slug: /phpstudy
tags:
  - phpStudy
  - DevOps
---

# 快速入门

phpStudy 是一个中文界面的 PHP 环境集成包，支持 Apache+Nginx+LightTPD+IIS，支持 php5.2-php7.1 自由切换。全部通过图形化界面实现，配置和管理多个网站、配置域名、管理服务、管理端口等

![](https://oss.aliyuncs.com/netmarket/product/f5117a63-085a-4dd3-80d0-414852eb6529.jpg)


部署 Websoft9 提供的 phpStudy 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 phpStudy 的 **[默认账号和密码](./setup/credentials)**  
4. 若想用域名访问  phpStudy，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## phpStudy 初始化向导

### 详细步骤

远程桌面到服务器，点击服务器桌面的 phpStudy 图标，查看其状态

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/phpstudy/phpstudy-restartapache-websoft9.png)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。


## phpStudy 安装网站

phpStudy环境中部署网站主要分为5个步骤： **①**上传网站代码-&gt;**②**配置域名（非必要）-&gt;**③**增加网站对应的数据库（非必要）-&gt;**⑤**完成安装向导

注意：部署一个网站还是多个网站、有无域名这两种情况对应的部署操作细节略有不一样，下面分别说明：

### 部署第一个网站

如果您打算此服务器上只部署一个网站或应用，建议采用此方式：

1.  远程桌面到Windows服务器，将网站源文件拷贝到根目录
2.  如果没有可用域名，请直接通过 **http://公网IP**  的方式来访问应用
3.  如果有可用的域名，请完成 **《域名配置》** 后通过 **http://公网IP** 的方式来访问应用
4.  如果在安装向导过程中提示数据库无法自动创建，需要通过 http://ip/phpmyadmin 创建数据库

网站默认根目录为：C:\websoft9\phpStudy\PHPTutorial\WWW

### 部署第二个网站

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


## 环境配置

### PHP 配置


#### 切换 PHP 版本

切换PHP版本，只需两步：

1.  选择版本 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/phpstudy/phpstudy-version-websoft9.png)
2.  重启服务

#### 修改 php.ini

### Apache 配置

Apache 配置主要通过修改 [虚拟主机配置文件](#path) 中的 [VirtualHost 指令](./apache#virtualHost)去实现各种需求。  

#### 绑定域名

修改 [Apache虚拟机主机配置文件](#apache)，将其中的 **ServerName** 项的值修改为你的域名

#### 修改网站目录

修改 [Apache虚拟机主机配置文件](#apache)，将其中的 DocumentRoot 和 Directory 的值修改成你网站的路径 项的值修改为你的域名


#### 设置伪静态

Apache开启为静态的步骤如下：

1. 在 C:\websoft9\phpStudy\PHPTutorial\Apache\conf\httpd.conf 文件中查找以下语句 LoadModule rewrite_module modules/mod_rewrite.so，若前面有 # 号则需要将其去掉，使之支持 mod_rewrite 模块；

2. 再查找 AllowOverride 语句，若其后为 None 则将其更改为 ALL 使apache支持 .htaccess 文件,若已经是 ALL 则不需要变动；  

4. 重启 Apache，这样就可以在你的 PHP 项目根目录下建立 .htaccess 文件开启伪静态了。

> 大部分开源应用目录下都会自带 .htaccess 文件，不需要另外自己设置


### 数据库配置

#### 重置数据库密码

通过：其他选项菜单-&gt;MySQL工具-&gt;重置密码（忘记时），可以重新修改密码

#### 管理数据库


## 参数

**[通用参数表](../setup/parameter)** 中可查看 Apache, MySQL 等 phpStudy 应用中包含的基础架构组件路径、版本、端口等参数。 

下面仅列出 phpStudy 本身的参数：

### 路径{#path}

| **项** | **路径或说明** |
| :--- | :--- |
| 网站默认根目录 | C:\websoft9\phpStudy\PHPTutorial\WWW |
| PHP配置文件 | C:\websoft9\phpStudy\PHPTutorial\php\php-\*\php.ini  |
| PHP版本 | PHP5.2到PHP7.2可自由切换 |
| Apache虚拟主机文件--根目录对应的文件 |  C:\websoft9\phpStudy\PHPTutorial\Apache\conf\extra\httpd-vhosts.conf |
| Apache日志文件目录 | C:\websoft9\phpStudy\PHPTutorial\apache\logs | 
| Nginx虚拟主机文件--根目录对应的文件 | C:\websoft9\phpStudy\PHPTutorial\nginx\conf\vhosts.conf |
| Nginx日志文件目录 | C:\websoft9\phpStudy\PHPTutorial\nginx\logs |
| MySQL数据目录 | C:\websoft9\phpStudy\PHPTutorial\MySQL\data |
| MySQL配置文件 | C:\websoft9\phpStudy\PHPTutorial\MySQL\my.ini |
| phpMyAdmin目录 | C:\websoft9\phpStudy\PHPTutorial\WWW\phpMyAdmin |
| MySQL管理地址 | [http://服务器公网IP/phpmyadmin](http://服务器公网IP/phpmyadmin) |
| 9Panel访问地址 | [http://服务器公网IP/9panel](http://服务器公网IP/9panel) |


### 版本

界面中查看

### 服务

修改网站配置之后，有时候需要完成相关服务的启动和停止。phpStudy提供了服务重启功能：

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/phpstudy/phpstudy-restartapache-websoft9.png)

### 命令行
无

### API
无

