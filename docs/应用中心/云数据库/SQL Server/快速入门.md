---
sidebar_position: 1
slug: /bt
tags:
  - BT
  - 宝塔面板
  - 运行环境
---

# 快速入门

[BT（宝塔）](https:/www.bt.cn) 面板是提升运维效率的服务器管理软件，支持一键LAMP/LNMP/集群/监控/网站/FTP/数据库/JAVA等100多项服务器管理功能。支持windows和linux系统，可以通过Web端轻松管理服务器，提升运维效率。例如：创建管理网站、FTP、数据库，拥有可视化文件管理器，可视化软件管理器，可视化CPU、内存、流量监控图表，计划任务等功能。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btlinux/bt-linux_pc.png)

## IIS解析漏洞告警及处理方案

云鼎实验室在日常安全运营中发现，宝塔 Windows 面板默认安装的 IIS+PHP 环境存在 IIS 解析漏洞，攻击者可以在任意文件上传点上传一个包含着恶意 PHP 代码的文件（图片、TXT、压缩包等）后，通过利用 IIS 解析漏洞即可执行 PHP 代码，可能会导致用户代码、数据库泄露。

如果您通过宝塔安装了IIS，就会产生一个IIS的解析漏洞，您需要做出如下修改：

1.修改由IIS在根目录中自动生成“web.config”的文件（路径：“C:\inetpub\wwwroot”），将“resourceType”对应的"Unspecified"修改为“File”。
2.如果您新建了网站中包含了web.config文件，也需要做出上述修改

..............................................................

如果安装了IIS，又安装了PHP，您需要修改如下配置：

1. 打开“C:\Windows\System32\inetsrv\config\applicationHost.config”文件
2. 将“<add name="PHP_FastCGI" path="*.php" verb="*" modules="FastCgiModule" scriptProcessor="C:\BtSoft\WebSoft\php\5.4\php-cgi.exe" resourceType="Unspecified" />”中“resourceType”对应的"Unspecified"修改为“File”。

以上路径以PHP5.4为例，如果安装了多个php版本，每个PHP目录均需要进行修改


在云服务器上部署 BT 预装包之后，请参考下面的步骤快速入门。

> 宝塔 Linux 面板和宝塔 Windows 面板有一定的功能差异，后续文档会在必要的时候做出说明。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:8888** 端口是否开启
3. 若想用域名访问 BT，请先到 **域名控制台** 完成一个域名解析

## 账号密码

使用BT，可能会用到的几组账号密码如下：

### BT

* 管理员用户名：administrator
* 管理员密码：admin123
* 登录方式：http://服务器公网IP:8888

密码安全性提示：BT密码是为了帮助您简化安装和使用的，但默认密码并不安全，因此在完成镜像安装之后，立即通过管理地址修改默认密码。
> 密码安全性提示：初始密码仅为了简化首次登录，但默认密码并不安全，请登录后记得修改它。

若以上账号无法登录后台，参考[旧版本 Windows 面板初始化指南](#旧版本-windows-面板初始化指南)


## BT 入门向导

### 登录

BT 部署到你的服务器后，即可开始使用：

1. 使用 Chrome 或 Firefox 浏览器访问：*http://服务器公网IP:8888* ，进入登录页面（[打不开？](#异常处理)）  
   ![BT 登录界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/btlinux/bt-login-websoft9.png)

2. 输入默认账号密码（[不知道密码？](#账号密码)），进入宝塔后台
   ![BT 后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/btlinux/bt-console-websoft9.png)

3. 如果出现下面的绑定宝塔账号提示，访问：*http://服务器公网IP:8888/soft* 即可绕开
   ![BT 后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/btwin/bt-registerneed-websoft9.png)

  > 绑定宝塔官方账号不是必须的步骤

### 升级

在使用宝塔之前，建议首先检查升级，保证系统为最新状态  

![宝塔升级](https://libs.websoft9.com/Websoft9/DocsPicture/zh/btlinux/bt-update001-websoft9.png)

### 搭建环境

升级完成后，就可以开始使用宝塔搭建你所需的环境。

#### 安装推荐套件

宝塔默认会推荐一个组合的安装套件，如果套件合适你的需求，可以安装它：

1. 确定所需的套件，在套件界面上选择组件版本，例如：PHP7.4, MySQL 5.6
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btlinux/bt02.png)

2. 组件选择完成后，点击【一键安装】，耐心等待安装直至结束
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btlinux/bt03.png) 


#### 安装更多软件

初始化安装之外的安装，都可以通过【软件商店（管理）】去安装更多的组件。

* 宝塔 Linux 面板之【软件商店】
  ![宝塔 Linux 软件商店](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btlinux/bt-linuxapps-websoft9.png) 

* 宝塔 Windows 面板之【软件管理】
  ![宝塔 Windows 软件管理](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btwin/bt-winapps-websoft9.png) 

**示例1 安装Tomcat：** 打开宝塔【软件管理】>【运行环境】>【Tomcat】，点击【安装】即可  

**示例1 安装Node.js：** 打开宝塔【软件管理】>【运行环境】>【PM2管理器】，点击【安装】即可

## 常用操作

### 安装网站示例

安装完整的经典步骤包括：①上传网站代码->②修改文件系统用户权限->③配置域名（非必要）->④增加网站对应的数据库（非必要）->⑤完成安装向导

在BT面板中，基本遵循以上原则（步骤先后顺序略有差异）

#### 示例：安装WordPress

具体操作如下：

1.  打开宝塔Web界面-->网站-->添加站点，完成必要的配置，并牢记相关账号和密码
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btwin/bt-deploysite001-websoft9.png)

    * 域名必须填写
    * 建议创建FTP（如不创建，通过使用宝塔的在线文件管理）
    * 创建数据库
    * 选择程序和版本

3.  上传文件到网站目录或上传压缩包到目录后解压；
6.  到云控制台中完成域名解析
8.  打开网址 http://您的域名 ,即可开始进行wordpress配置。

#### FAQ

##### 添加站点，提示PHP版本不能为空？
**问题描述：** 当只安装一个PHP版本的时候，增加网站会提示“PHP版本不能为空”，这是系统的一个Bug
**解决方案：** 再安装一个PHP版本即可

### 上传和管理文件

我们知道文件管理主要包括：复制、粘贴、剪切、删除、重命名、压缩、刷新、新建文件、新建目录等操作，宝塔Linux面板支持两种文件管理方式，下面分别描述：

#### 方案一：使用在线文件管理

打开宝塔->文件管理界面：

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btwin/bt-filemanage-websoft9.png)


可以进行新增、删除、编辑、解压、权限设置、压缩等几乎所有的操作

具体参考《[宝塔官方文档-文件管理](https://www.kancloud.cn/chudong/bt2017/424266)》

#### 方案二：使用FTP

当每个网站分属于不同的客户的时候，给每个网站分配对应的FTP是必要的：

* 建立网站
* 设置FTP账号
* 下载FTP客户端，推荐Filezella
* 连接FTP，上传文件

若FTP无法正常连接，请根据以下说明排除错误
1. 安全组的21端口是否打开
2. 是否主动/被动模式都不能连接
3. 宝塔中的防火墙设置禁止了21端口

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

BT 域名绑定操作步骤：

![](http://libs.websoft9.com/Websoft9/DocsPicture/en/bt/bt-setdns-websoft9.png)


### 如何找回BT后台密码?

如果是忘记了密码，请使用WinSCP或Putty运行如下命令，重置密码
~~~

//示例：将admin用户的密码重置为admin123

cd /www/server/panel && python tools.pyc panel admin123 admin

//如果提示多次登录失败，暂时禁止登录 请输入以下命令，清除登录限制
rm -f /www/server/panel/data/*.login

~~~

### 挂载数据盘

宝塔镜像默认安装都在系统盘，如果您购买了额外的数据盘，如何挂载呢？

1. 将数据盘格式化
2. 面板设置-默认建站目录，将C:\wwwroot目录更改为数据盘对应的目录
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btwin/btwin-wwwroot-websoft9.png)

注意：如果已有多个网站，建议先完成如下两个操作以不影响原网站：
1. 先将wwwroot的数据备份下来
2. 将原wwwroot中的文件拷贝到数据盘对应的目录
3. 通过网站管理修改网站路径

### 安装PHP扩展

打开宝塔面板->软件管理，找到PHP，点击设置，我们会看到“安装扩展项”

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btwin/btwin-phpset-websoft9.png)

安装完成后，请点击“PHP服务”重启服务

### 设置HTTPS

宝塔中设置HTTPS两种方式，请根据您的实际情况进行选择：

* 注册宝塔官方账号，绑定后一键完成HTTPS部署
* 自行上传SSL证书，完成部署。（[官方帮助](https://www.bt.cn/bbs/thread-704-1-1.html)）

> 宝塔SSL申请的是免费版TrustAsia DV SSL CA - G5(1年）

### 查看和管理日志文件

日志文件是诊断故障和问题的重要手段，宝塔使用中可能会用到与日志相关的操作包括：

####  宝塔面板操作日志

登录宝塔面板->安全，会看到面板操作日志，点击“清空”按钮会清空所有操作记录

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btlinux/btlinux-panellogs-websoft9.png)

#### Web日志、网站日志

通过宝塔在线文件管理，进入：C:\BtSoft\WebSoft\apache\logs 目录，管理Web日志、网站日志

### 管理数据库

在宝塔面板中，尽量使用 phpMyAdmin 来管理数据库

1. 进入宝塔面板-数据库，找到root密码和phpMyAdmin链接
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btlinux/bt-linux_phpmyadmin-websoft9.png)
2. 点击“root密码”，设置好您的默认密码
2. 点击phpMyAdmin，输入root和对应的密码，然后登录到系统中
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

### 重置（修改）MySQL密码

对于宝塔面板来说，重置密码与修改密码是同样的操作。

进入宝塔面板->数据库，点击“root密码”链接，修改后点击提交即可

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btlinux/btlinux-mysqlpw-websoft9.png)

### 宝塔 Windows 指南

#### 找回BT面板密码

当忘记了宝塔Web端密码时，请远程桌面到Windows服务器，打开客户端->右上角菜单->修改密码 ，即可修改用户名和密码

![宝塔Windows 重置密码](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btwin/bt-winresetpw-websoft9.png)

### 旧版本 Windows 面板初始化指南

以下内容适用于 Windows 宝塔面板 V6.9 以下的版本：

#### 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:888** 端口是否开启
3. 若想用域名访问 BT，请先到 **域名控制台** 完成一个域名解析

#### Web 后台初始化

默认不能访问 Web 端（[桌面端和 Web 后台](/zh/win/stack-installation.md#桌面端和web端)），需远程到服务器，完成进行**初始化设置**后方可。

1. 远程桌面到服务器->打开Windows面板软件端，打开软件右上角的菜单，选择（初始化/修改密码）功能，输入您的账号和密码
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btwin/btwin-inti-websoft9.png)
2. 本地电脑打开浏览器，访问：http://服务IP:888 ，使用上一步设置的密码登录进入Web后台
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btwin/bt-winbackend-websoft9.png)
3. 如果有更新提示，请先点击“立即更新”后再使用宝塔


> 注意：宝塔的历史版本，是直接通过http://服务IP:888 设置后台密码的  

  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btwin/bt-winstart-websoft9.png)

#### 网站环境安装

镜像中只安装了干净的面板工具。登录面板工具-->软件管理-->运行环境

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/btwin/bt-win-intallhj-websoft9.png)

参考上图，找到需要安装的软件，点击安装即可

#### 常见问题

##### 浏览器无法访问 BT（白屏没有结果）？

您的服务器对应的安全组 888 端口没有开启（入规则），且没有远程桌面初始化宝塔之前，浏览器无法访问到服务器的任何内容

##### 桌面端和Web端

宝塔 Windows 面板有两个访问端口：一个是服务器的桌面端，一个是通过PC浏览器访问的Web端。

##### 桌面应用端

*   传统的软件端操作界面，可以对服务器的站点进行高效的管理
*   高效的操作管理，可快速搭建站点、数据库、FTP等服务
    ![](https://www.bt.cn/Public/images/win_pc.png)

##### Web应用端

*   相对于桌面应用端有更好的体验，跨终端、跨平台
*   高效的操作管理，可快速搭建站点、数据库、FTP等服务
*   完善的在线文件管理器，轻松实现图片查看，文本编辑，文件打包解压
    ![](https://www.bt.cn/Public/images/win_web.png)
    

> Web端的功能更为全面，只要SQLServer的安装需要使用客户端，其他的都可以在Web端完成，因此后续的指南我们均以Web端作为范例来进行具体说明。


## 异常处理

#### 浏览器访问 *http://服务器公网IP：8888* 没有内容（白屏没有结果）？

您的服务器对应的安全组 8888 端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容。

#### 8888 端口成功开启仍然无法访问？

可能您安装了旧版本（低于宝塔Windows版 V6.9），需参考[旧版本 Windows 面板初始化指南](#旧版本-windows-面板初始化指南)

#### 能否将 PHP, Java 和 Node.js 安装到一起？

可以。虽然宝塔可选的组件很多，但请把握一个原则："不用的不装，什么时候用什么时候装"。

#### 需要运行 PHP 网站怎么安装环境？

安装推荐套餐，即安装：Apache，MySQL，PHP， phpMyAdmin 等

#### 安装哪个 PHP 版本合适？

根据你的应用决定 PHP 版本，如果应用没有明确所需的版本，建议安装 PHP7.2 或以上版本。另外，除非有多版本需求，请不要主动安装多个PHP版本

#### 有哪些软件是必须安装的吗？

没有必须安装的软件，请根据应用要求去安装。原则："不用的不装，什么时候用什么时候装"。

#### 宝塔 Windows 面板中 SQLServer 怎么安装？

建议自行下载 Microsoft 官方的包进行安装。

#### IIS 与 Apache，Nginx 可以同时安装吗？

三者选其一，否则会引起不必要的软件冲突

#### 宝塔 Windows 面板究竟安装那个 Web 服务器呢？

推荐使用 IIS
