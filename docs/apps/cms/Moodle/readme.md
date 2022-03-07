---
sidebar_position: 1
slug: /moodle
tags:
  - Moodle
  - 在线学习管理
---

# 快速入门

[Moodle](https://moodle.org) 是一个开源的在线教育系统（慕课）。采用PHP+Mysql开发，界面友好，符合SCORM/AICC标准。以功能强大、而界面简单、精巧而著称。它是eLearning技术先驱，是先进在线教学理念和实践的集大成者，已成为全球大中学院校建立开放式课程系统的首选软件。主要模块：课程管理、作业模块、聊天模块、投票模块、论坛模块、测验模块、资源模块、问卷调查模块、互动评价（workshop）。Moodle具有先进的教学理念，创设的虚拟学习环境中有三个维度：技术管理维度、学习任务维度和社会交往维度，以社会建构主义教学法为其设计的理论基础，它提倡师生或学生彼此间共同思考，合作解决问题。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodlegui-websoft9.jpg)


## 演示

Moodle官网提供了试用环境，您可以直接试用

* 演示地址：https://moodle.org/demo/

> 免责说明：此处仅提供Moodle官方的演示，不保证与 Websoft9 部署包功能完全一致，若演示过程中若需要填写个人资料、获取Cookie等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此可能存在的商业纠纷与我司无关。


在云服务器上部署 Moodle 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Moodle，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号

### Moodle

在初始化安装的时候由用户自行设置

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

> 需要登录MySQL，请参考 [MySQL可视化管理](#MySQL-数据管理)

## Moodle 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 就进入引导首页
2. 根据系统提示，选择语言，进入下一步 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install001-websoft9.png)

3. 选择数据库类型，默认为【改进的MySQL】，然后进入确认路径设置（保持默认设置），进入下一步 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install002-websoft9.png)

4. 填写数据库连接信息，建议采用预装环境自带的 MySQL 数据库([不知道账号密码？](#账号密码))
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install003-websoft9.png)

5. 经过几次确认后，安装进入环境检测步骤，继续后续步骤 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install004-websoft9.png)

6. 设置后台账号信息，请务必设置好并牢记之。进入下一步 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install005-websoft9.png)

7. 设置网站初始化信息 
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install006-websoft9.png)

8. 跟随安装提示直到完成，过程中尽量选择默认设置，勾选安装所有模块

9. 系统完成最后一步安装，建议进入 Moodle 后台（以管理身份登录即进入后台），体验完整功能 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install007-websoft9.png)

10. [注册 Moodle 官方账号](#向-moodle-注册你的网站)，打通你的 Moodle 与官方的连接，便于在线安装插件。

> 需要了解更多Moodle的使用，请参考官方文档：[Moodle Documentation](https://docs.moodle.org)

## Moodle 入门向导

[Moodle 快速搭建学习管理系统](https://cloud.tencent.com/developer/article/1822682)

## 常用操作

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

Moodle 域名绑定操作步骤：

1. 使用 SFTP 工具登录云服务器
2. 修改 [虚拟机主机配置文件](moodle/admin#apache)，将其中的域名相关的值
   ```text
   #### Moodle(LAMP) bind domain #### 

     <VirtualHost *:80>
     ServerName  www.mydomain.com # 修改成您的实际域名
     DocumentRoot "/data/wwwroot/moodle"
     ...
     
   #### Moodle(LNMP) bind domain #### 

     server {
      listen 80;
      server_name moodle.example.com; # 修改成您的实际域名
     ...

   ```
3. 保存配置文件，[重启服务](moodle/admin#apache-1)


### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

Moodle预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

#### 快速参考

如果你想使用免费证书，只需在服务器中运行一条命令`certbot`就可以启动证书部署

如果你已经申请了商业证书，只需三个步骤，即可完成HTTPS配置

#### Moodle(LAMP)

Moodle(LAMP) 即运行环境采用 **Apache** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件： */etc/httpd/conf.d/vhost.conf* 
3. 将如下的 **HTTPS 配置段模板**  `<VirtualHost *:443>--</VirtualHost>` 插入到`vhost.conf` 文件中
   ``` text
   #-----HTTPS template start------------
   <VirtualHost *:443>
    ServerName  moodle.yourdomain.com
    DocumentRoot "/data/wwwroot/moodle"
    #ErrorLog "logs/moodle.yourdomain.com-error_log"
    #CustomLog "logs/moodle.yourdomain.com-access_log" common
    <Directory "/data/wwwroot/moodle">
    Options Indexes FollowSymlinks
    AllowOverride All
    Require all granted
    </Directory>
    SSLEngine on
    SSLCertificateFile  /data/cert/moodle.yourdomain.com.crt
    SSLCertificateKeyFile  /data/cert/moodle.yourdomain.com.key
    SSLCertificateChainFile  /data/cert/moodle.yourdomain.com_chain.crt
    </VirtualHost>
   #-----HTTPS template end------------
   ```
4. 修改 ServerName, SSLCertificateFile, SSLCertificateKeyFile等参数的值
5. 保存， [重启 Apache 服务](/维护参考.md#apache-1)

#### Moodle(LEMP)

Moodle(LEMP) 即运行环境采用 **Nginx** 作为 Web Server  

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到 Moodle 的 *server{ }* 中
 ``` text
   #-----HTTPS template start------------
   listen 443 ssl; 
   ssl_certificate /data/cert/xxx.crt;
   ssl_certificate_key /data/cert/xxx.key;
   ssl_trusted_certificate /data/cert/chain.pem;
   ssl_session_timeout 5m;
   ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
   ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
   ssl_prefer_server_ciphers on;
   #-----HTTPS template end------------
   ```
4. 修改 ssl_certificate, ssl_certificate_key 的值
5. 保存，[重启 Nginx 服务](/维护参考.md#nginx-1)

#### 详细指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面以**网易邮箱**为例，提供设置 Moodle 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 以管理员身份登录 Moodle控制台
3. 依次打开：【网站管理】>【服务器】>【电子邮件】>【发送邮件设置】
   ![Moodle SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-smtp-websoft9.png)
4. 点击【Test outgoing mail configuration】测试设置

更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### 向 Moodle 注册你的网站

Moodle 初始化安装完成之后，建议注册成为 Moodle 官方网站的会员，注册好处包括：升级通知，课程共享，在线安装插件等

1. 以管理员身份登录 Moodle 后台
2. 依次打开：【网站管理】>【注册】
   ![Moodle 注册](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-registermd-websoft9.png)
3. 注册完成后登陆，这样你的 Moodle 与官方便建立了一个连接关系

### Moodle 语言设置

1. 以管理员身份登录 Moodle 后台
2. 依次打开：【网站管理】>【语言】
   ![Moodle 语言设置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-languageset-websoft9.png)
3. 根据实际情况进行语言设置
   * 语言设置：即在线切换语言
   * 定制语言：即在线编辑语言翻译内容
   * 语言包： 即上传系统默认没有内置的语言

### Moodle 客户端

1. 以管理身份登录 Moodle 后台
2. 依次打开：【网站管理】>【移动应用程序】>【移动设备设置】
   ![moodle-apps](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-app-1-websoft9.jpg)
3. 将【为移动设备启用网络服务】设为 **启用** 状态；
   ![moodle-apps](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-app-2-websoft9.jpg)
4. 保存设置；
5. 安装 [Moodle 手机客户端](https://download.moodle.org/mobile/)
6. 打开后在地址栏输入 Moodle 的访问地址，就可以开始使用移动端
   ![moodle-apps](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-mobile-websoft9.png)

### Moodle 插件

Moodle 是一个非常灵活的平台，大部分核心功能以插件的形式存在，系统默认安装了400多个插件。同时，官方提供了[插件市场](https://moodle.org/plugins/)供用户作用更多功能扩展。

1. [注册 Moodle 官方账号](/zh/solution-more.html#moodle-注册)，打通你的 Moodle 与官方的连接，便于在线安装插件。

2. 以管理员身份登录 Moodle 后台

3. 依次打开：【网站管理】>【插件】，会看到**安装插件**和**插件概况**两个链接
   ![moodle 插件](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-plugins-websoft9.png)

   * 安装插件：安装新插件入口
   * 插件概况：查看已经安装的插件列表

4. 点击【安装插件】，提供**从Moodle插件目录安装插件**和**从ZIP文件中安装插件**两种安装插件的方式
   ![moodle 安装插件](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-pluginsmk-websoft9.png)

   * 从Moodle插件目录安装插件：自动跳转并登录到 Moodle 的[官方插件市场](https://moodle.org/plugins/)，便可以在线安装
   * 从ZIP文件中安装插件：需提前下载插件压缩文件，再从此处**上传**安装

5. 点击【插件概况】，列出默认安装的插件，可以进行停用、卸载等操作
   ![moodle 插件概况](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-plugininfo-websoft9.png)
   
6. 点击[插件概况](https://moodle.org/plugins/)寻找所需的插件，然后安装它们

> 更多插件管理查看官方文档 [Moodle Plugins](https://docs.moodle.org/37/en/Installing_plugins)

### Moodle 主题

Moodle 主题实际上是一个插件，因此需要安装新主题，必须通过【安装插件】的方式先进行安装。  

1. 以管理员身份登录 Moodle
2. 依次打开：【网站管理】>【插件】，进入插件市场后，选择【Theme】类型的插件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-mktheme-websoft9.png)

3. 在线安装所需的主题

3. 打开【网站管理】>【外观】>【主题选择器】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-addtheme001-websoft9.png)

4. 点击【更改主题】即可完成主题更换
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-addtheme002-websoft9.png)

### 重置密码

常用的 Moodle 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码

1. 登录 Moodle 后台，点击头像，进入【个人档案】设置下的**小齿轮图标**
  ![Moodle 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-modifypw-websoft9.png)

2. 点击【更改密码】链接，开始修改密码

#### 找回密码

如果用户忘记了密码，有两种找回密码的方案：

* 登录界面通过邮件找回密码（需提前完成 [SMTP 设置](/zh/solution-smtp.md)）
* 数据库中重置密码两种方案

下面介绍通过数据库找回密码的方案：

1. 登录 [phpMyAdmin](#mysql-数据管理)，并找到你的网站数据库下的 *mdl_user*表

  ![Moodle user表](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-phpmyadminuser-websoft9.png)

2. 编辑【admin】用户，将其中的 `password` 字段的值用 `21232f297a57a5a743894a0e4a801fc3` 替换

3. 点击【执行】，新的密码就被重置为`admin`


### MySQL 数据管理

OpenCart 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP/phpmyadmin*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理

#### 浏览器打开IP地址，无法访问 Moodle（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 Moodle 数据？

是MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 Moodle 数据？

可以