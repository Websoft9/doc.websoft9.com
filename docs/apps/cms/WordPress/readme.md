---
sidebar_position: 1
slug: /wordpress
tags:
  - WordPress
  - CMS
  - 建站系统
  - 博客系统
---

# 快速入门

[WordPress](https://wordpress.org) 简称WP，最初是一款博客系统，后逐步演化成一款功能强大的企业级 CMS（内容管理/建站系统），目前是公认的全球最佳建站系统，互联网上有34%的网站都基于 WordPress构建。这套系统因易用性、易扩展性（ 插件 、模板、二次开发）、功能强大、美观、搜索引擎友好等而全世界著名。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-product-screenshot.png)

WordPress 官方提供了大量免费的主题和插件，你可以在线查看演示或安装

- [官方插件演示](https://wordpress.org/plugins/)
- [官方主题演示](https://wordpress.org/themes/)




## 准备

在云服务器上部署 WordPress 预装包之后，还需完成如下准备方可进入初始化向导

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 WordPress，请先到 **域名控制台** 完成一个域名解析

## WordPress 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*https://域名* 或 *https://Internet IP*, 进入安装向导  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wp01.png)

2. 选择语言后，进入 WordPress 安装要求说明，点击“现在就开始”进入下一步 
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-install001-websoft9.png)

3. 系统进入数据库连接信息安装项，请填写数据库连接信息（[不知道账号密码？](/zh/stack-accounts.md#mysql)） 
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-install002-websoft9.png)

4. 数据库验证通过后，系统提示正式“进行安装” 
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-install003-websoft9.png)

5. 设置您的管理员账号、密码和邮箱， 点击“安装WordPress”; 
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-install004-websoft9.png)

6. 恭喜，成功安装 
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-install005-websoft9.png)

7. 进入后台（http//域名或IP/wp-admin），试试WordPress的功能 
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-install006-websoft9.png)

8. WordPress的安装已经全部完成。

> 需要了解更多WordPress的使用，请参考官方文档：[WordPress Documentation](https://wordpress.org/support/)


### 启用 Avada 主题

如果你的 WordPress 预装包中包含了 Avada 主题，请参考本节完成 Avada 启用和模板导入：

#### 在线导入Avada模板

完成镜像安装之后，WordPress前台页面并没有模板的效果，请勿在这个时候误以为 Avada 没有高大上的效果而放弃它，那就太可惜了。实际上Avada内置了20+个免费模板，均可以在线导入。步骤如下：

1. 通过后台-插件，选择所有插件后全部启用  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-enableplugins-websoft9.png)

2. 后台-Avada-演示，进入Avada演示界面 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-getdemo-websoft9.png)

3. 选择一个演示，可以进行“预览”和“导入”两种操作

4. 以其中“Science”为例，点击导入，导入内容为“全部”，点击“导入”按钮 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-demoall-websoft9.png)

5. 系统会有一个提示，直接点击OK，进入演示导入过程 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-demook-websoft9.png)

6. 演示导入完成后，系统会提示“完成”（少数时候受制于网络原因，导入可能不成功，需要多次尝试） 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-democomplete-websoft9.png)

7. 点击“完成”，回到演示列表页面，会看到“Science”的状态已经为完全导入了。如果导入不成功，会显示部分导入 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-democomplete2-websoft9.png)

8. 在回到前台页面，看看模板的效果

#### 在线卸载Avada模板

导入的模板可以在线卸载（清除干净），如果你想导入新的模板，请先卸载已有模板，卸载步骤如下：

1. 后台-Avada-演示，找到要卸载的演示，点击“修改” 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-uninstall-websoft9.png)
2. 勾选“卸载”，点击移除按钮，开始卸载
3. 卸载成功，系统会提示完成

### 启用 Porto 主题

如果你的 WordPress 预装包中包含了 Porto 主题，请参考本节完成 Porto 启用和模板导入：

#### 在线导入Porto模板

完成镜像安装之后，WordPress前台页面并没有模板的效果，请勿在这个时候误以为Porto没有高大上的效果而放弃它，那就太可惜了。实际上Porto内置了20+个免费模板，均可以在线导入。导入界面步骤如下：

1. 后台-Porto-安装演示，进入安装演示页面，例如：点击Business Consultant来安装 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/porto/porto-demoyes-websoft9.png)
2. 演示安装过程会有进度条提示，请耐心等待5分钟左右 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/porto/porto-demoing-websoft9.png)
3. 演示导入完成，我们回到前台，发现演示可用，但是轮播区提示错误（…home-bc not found）
4. 是因为在线导入不能导轮播，还需单独导入轮播（Slider）数据

#### 在线导入Revolution Sliders

导入轮播数据的操作步骤如下：

1. 下载Revolution Sliders演示包到本地电脑（下载地址：[https://服务器公网ip/slidersdemo.zip）](https://服务器公网ip/slidersdemo.zip）)
2. 解压之
3. 后台-革命滑块-导入幻灯片 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/porto/porto-siderimport001-websoft9.png)
4. 选择对应的幻灯片压缩包（根据Porto模板提示而选择，例如…home-bc not found，那么这时候就选择home-BC.zip） 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/porto/porto-siderimport002-websoft9.png)
5. 在查看网站首页，我们发现轮播导入成功了。

#### 在线卸载Porto模板

Porto的演示模板导入之后，就可以根据演示来个性化您的网站了，如果对于导入的效果不满意，希望导入其他演示，那么最好删除演示，否则新导入的数据会累加到已有Porto系统中，显得非常的臃肿不堪。

删除步骤：

1. 后台-媒体-媒体库，删除所有图片
2. 后台-页面管理，删除所有页面
3. 后台-外观-菜单，删除所有菜单
4. 后台-文章，删除所有文章

如果觉得以上步骤太过于繁琐，请直接清空WordPress的数据库，重新安装也是可以的。

## WordPress&Discuz 安装向导

WordPress&Discuz 预装包部署后，浏览器访问：*https://服务器公网ip/9panel* 开始安装向导。

**注意**：应用是否通过域名访问，Linux系统 或 Windows系统，对应的安装步骤不同，请选择合适的方案：

### 方式一：通过IP访问

如果不打算使用域名访问网站，而是通过IP地址访问网站，安装非常简单：

* WordPress安装入口：*https://服务器公网IP*，进入 [WordPress 安装向导](/zh/stack-installation.md#wordpress-安装向导)
* Discuz安装入口：*https://服务器公网IP/discuz*，进入 [Discuz 安装向导](https://support.websoft9.com/docs/discuz/zh/stack-installation.md#discuz-安装向导)

### 方式二：共用一个域名访问

共用一个域名（假设域名为www.abc.com），类似：

* *https://www.abc.com*   访问 WordPress
* *https://www.abc.com/discuz*   访问 Discuz

这种情况下的安装步骤如下：

1. 登录到域名管理面板，完成解析域名，确保域名解析成功
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/domain-websoft9.png)
2. 分别完成安装向导
   - 本地浏览器访问：*https://www.abc.com*   开始 [WordPress 安装向导](/zh/stack-installation.md#wordpress-安装向导)
   - 本地浏览器访问：*https://www.abc.com/discuz*   开始 [Discuz 安装向导](https://support.websoft9.com/docs/discuz/zh/stack-installation.md#discuz-安装向导)

### 方式三：分别配置域名（LAMP版）

给 WordPress 和 Discuz 分别配置不同的域名，例如：

* *https://wordpress.abc.com*  配置给 WordPress
* *https://discuz.abc.com*    配置给 Discuz

> LAMP版即表明你是的服务器是 Linux 系统，请使用 WinSCP 连接服务器  

此场景下对应的安装步骤如下：

1. 登录到域名管理面板，分别完成域名解析（增加一个A记录到服务器公网IP地址），参考下图：
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/domain-websoft9.png)
2. 确保域名解析已经成功
3. 通过 WinSCP 连接服务器，进入*/etc/httpd/conf.d*目录，修改域名的配置文件，绑定各自的域名。 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress-discuz/wpdz-vhostconf-1-websoft9.png)
   - WordPress域名绑定：请修改“vhost.conf”里面的域名信息，然后保存
   - Discuz域名绑定：请修改“discuz.conf.范例”里面的域名信息，保存后再去掉“.范例”后缀使之生效
4. 使用 WinSCP 重启服务 或 云控制台重启服务器
   ```
   systemctl restart httpd
   ```
5. 分别完成安装向导
   - 本地浏览器访问：*https://wordpress.abc.com*   开始 [WordPress 安装向导](/zh/stack-installation.md#wordpress-安装向导)
   - 本地浏览器访问：*https://discuz.abc.com*   开始 [Discuz 安装向导](https://support.websoft9.com/docs/discuz/zh/stack-installation.md#discuz-安装向导)

### 方式三：分别配置域名（WAMP版）

给 WordPress 和 Discuz 分别配置不同的域名，例如：

* *https://wordpress.abc.com*  配置给 WordPress
* *https://discuz.abc.com*    配置给 Discuz

> WAMP 版即表明你是的服务器是 Windows 系统，请使用 远程桌面工具 连接服务器  

此场景下对应的安装步骤如下：

1. 登录到域名管理面板，分别完成域名解析（增加一个A记录到服务器公网IP地址），参考下图：
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/domain-websoft9.png)
2. 请检验域名解析是否成功
3. 远程到Windows服务器，进行域名配置文件 **http-vhosts.conf** 修改，具体操作如下：
   - 单击（鼠标左键）绿色的 WAMPserver 图标，依次点击：【Apache】>【http-vhosts.conf】 
   - 将标注红框的 ServerName 值换成您自己的域名 
   - 保存后修改 
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress-discuz/wordpressdiscuz-domain-1-websoft9.png)
4. 退出 WAMPserver 
5. 重新启动WAMPServer，单击（鼠标左键）绿色的 WAMPserver 按钮，点击“重新启动所有服务”
6. 分别完成安装向导
   - 本地浏览器访问：*https://wordpress.abc.com*   开始 [WordPress 安装向导](/zh/stack-installation.md#wordpress-安装向导)
   - 本地浏览器访问：*https://discuz.abc.com*   开始 [Discuz 安装向导](https://support.websoft9.com/docs/discuz/zh/stack-installation.md#discuz-安装向导)

---

### FAQ

#### 如何删除引导页面？

打开IP地址显示的是引导页面，引导页面的作用是为了在镜像首次安装的时候给用户以有效提醒。

请到 */data/wwwroot/default* 目录中删除引导页面相关的内容。删除的时候，一定要保留wordpress和discuz文件夹，删除后请清除浏览器缓存，这样引导页面就不会出现了

#### 为什么默认打开是 WordPress？

WordPress相比Discuz来说更为流行，以Wordpress为主页是大多数用户可能的选择。Wordpress对应的配置文件是vhost.conf，可以自行修改

#### 安装的时候显示Discuz!DatabaseError?

如果数据库名称、数据库账号与数据库密码填写与实际不符合，安装就会失败，显示“Discuz!DatabaseError”错误，具体解决办法：

1. 使用phpMyAdmin（登录账号请使用discuz所用到的数据库账号）登录，验证你填写的数据库账号是否与实际匹配
2. 请到服务器上删除./data/install.lock文件
3. 通过网址：*https://ip/discuz/install* 或 *https://域名/install* 重装（一定要加上/install）

## 常用操作

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

WordPress 域名绑定操作步骤：

1. 登录云服务器
2. 修改 [虚拟机主机配置文件](/维护参考.md#wordpress路径)，将其中的域名相关的值
   ```text
   #### WordPress(LAMP) bind domain #### 

     <VirtualHost *:80>
     ServerName www.mydomain.com # 修改成您的实际域名
     DocumentRoot "/data/wwwroot/wordpress"
     ...
     
   #### WordPress(LNMP) bind domain #### 

     server {
      listen 80;
      server_name    wordpress.example.com; # 修改成您的实际域名
     ...

   ```
3. 保存配置文件，重启服务

### 更换域名

正确的WordPress域名更换方法为：

1. 打开域名控制台，完成域名解析
2. 连接云服务器，完成域名绑定
3. 登录 WordPress 后台，依次打开：【设置】>【常规】，将网站路径和安装路径设置为新的域名
   ![Wordpress 修改URL](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-modifyurls-websoft9.png)
4. 保存后生效

> 如果更换域名后，网站中有一部分图片地址还是原来的域名，此时需要手工逐一修正
> 如果在第2步操作完成后，无法进入第3步访问后台操作，请访问 Wordpress 数据库，将 option 表中的 home 和 siteurl 两个属性修改为【新的域名】
> 通过 Websoft9 已经配置好的 MySQL 可视化工具 phpMyAdmin (http://ip/phpmyadmin 或 http://ip:9090 )进行快捷操作

### SSL/HTTPS

网站完成[域名绑定](/zh/solution-more.html#域名绑定)且可以通过HTTP访问之后，方可设置HTTPS。

WordPress预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改 Web 服务器的任何其他文件

#### 配置参考

不同的环境，配置方式不一样，请选择对应的方案：

* [WordPress（LAMP） HTTPS 配置方案](https://support.websoft9.com/docs/lamp/zh/solution-https.html)
* [WordPress（LNMP） HTTPS 配置方案](https://support.websoft9.com/docs/lnmp/zh/solution-https.html)
* [WordPress（WAMP） HTTPS 配置方案 ](https://support.websoft9.com/docs/wampserver/zh/solution-https.html)
* [WordPress（IIS） HTTPS 配置方案 ](https://support.websoft9.com/docs/windows/zh/solution-https.html)

#### 疑难问题

##### 配置HTTPS后，网站部分资源无法加载？

在完成 https 的配置后，可能会出现网站无法加载 css 等静态文件，特别是是对于经过二次开发过的 WordPress 会更为常见。

问题原因及对策

1. 特殊插件导致？ 某些插件自带 HTTPS 开关，需要根据实际情况开启或关闭。 
2. 开了 CDN 服务？ 编辑 WordPress 根目录下的 **wp-config.php** 文件，增加如下代码

    ```
       define('FORCE_SSL_ADMIN', true);
       define('FORCE_SSL_LOGIN', true);
       $_SERVER['HTTPS'] = 'ON';
       define( 'CONCATENATE_SCRIPTS', false );
    ```

##### “....并非完全安全”？
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/https-notallsafe-websoft9.png)

原因是由于 WordPress 网页中含有一部分 HTTP 开头的图片等静态链接资源，需要手工逐一修改

#### 专题指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面以**网易邮箱**为例，提供设置 WordPress 发邮件的步骤：

1. 在QQ邮箱管理控制台[获取 SMTP 相关参数](https://service.mail.qq.com/cgi-bin/help?subtype=1&&no=166&&id=28)
   ```
   SMTP host: smtp.qq.com
   SMTP port: 465 or 587 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: 21323232@qq.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过QQ邮箱后台设置去获取的[授权码](https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256)
   ```
2. 登录 WordPress后台-设置-常规，设置好需要用于发件的邮件地址 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-mailcg-websoft9.png)
3. 安装SMTP插件：[WP Mail SMTP by WPForms](https://wordpress.org/plugins/wp-mail-smtp/)
3. 后台-设置-Email，配置WP Mail SMTTP 插件的参数
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-mailconf-websoft9.png)
4. 填写参数后保存，然后最后输入一个收件地址用于测试是否可用
   - 如果测试成功，会看到”Your email was sent successfully!”
   - 如果邮件配置不可用，则会显示“There was a problem while sending the test email.”
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-mailss-websoft9.png)
5. SMTP配置成功后，所有的WordPress后台邮件发送就会使用这个配置

更多邮箱设置（网易邮箱、QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### 主题

WordPress初始化的前台只是一个博客界面，读者千万不要因此而误认为伟大的WordPress仅仅能够建博客。实际上世界上有21%的网站是由WordPress平台支持的，其中极少数才是博客，大部分都是企业站。

那这些企业如何通过WordPress建立精美而且功能强大的的网站呢？答案就是WordPress的主题机制。 把WordPress比作一个毛坯房，那主题就是装修好了的套餐，世界上有几十万套由WordPress生态中的爱好者或服务商提供的主题可选，想必其中一定有你喜欢或接近你喜欢的主题。

#### 寻找

1. 通过WordPress后台-外观-主题-添加，在线获取WordPress主题库的主题 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-addthemes-websoft9.png)
2. 通过百度等搜索“WordPress主题”，淘到自己喜欢的主题
3. 通过主题交易市场购买美轮美奂的主题，例如：themeforest.net

#### 安装

1. 通过WordPress后台-外观-主题-添加，后台上传主题安装
2. 通过FTP工具，将主题文件上传到 */wp-content/theme* 目录下

推荐使用第一种安装方式

#### 热门主题：Avada

Avada是一款在热门的WordPress主题，设计简单大方，支持所见即所得的可视化编辑与页面布局，内置超过20个免费模板，能够基于模板快速构建网站。Avada在Themeforest上累计销量超过37万次，其他下载和二次分发不计其数。适用于企业站和相册站、电商站、博客站。

![](https://photogallery.oss.aliyuncs.com/photo/1904996544835414/undefined/483d94c3-51bd-49ce-b5e8-2c86d62a448d.jpg)

##### 下载与安装

Avada安装和下载有两种方式，请根据实际情况选择合适您的方式：

###### 方式一：使用Avada镜像安装包（推荐）

* [阿里云WordPress镜像（含Aavad中文主题包）](https://market.aliyun.com/products/53616009/cmjj011415.html)
* [腾讯云WordPress镜像（含Avada中文主题包）](https://market.cloud.tencent.com/products/1515#)
* [华为云WordPress镜像（含Aavad中文主题包）](https://app.huaweicloud.com/all/?q=YXZhZGE)

###### 方式二：到themeforest.net购买原版

购买地址：https://themeforest.net/item/avada-responsive-multipurpose-theme/2833226

###### 方式三：在Websoft9下载主题自行安装
* [Avada 7.1.1 官方原版下载](https://libs.websoft9.com/apps/wordpress/avada7.1.1-en.zip)
* [Avada 6.2 汉化版下载](https://libs.websoft9.com/apps/wordpress/avada6.2-cn.zip)

---

**FAQ**

* 镜像包方式中的Avada有没有授权码？没有授权码，但可以正常使用
* Avada授权码有什么作用？可以在线升级主题和导入模板

##### Avada主题教程（9步建站） 

在熟悉了WordPress之后，我们通过如下9个步骤的实践来熟悉Avada，同时将前面导入的演示页面修改成我们自己的页面，那么也就完成了一个网站的初步制作。

###### 第一步 网站通用设置与配置

Avada采用的是配置式的工作方式，即网站的布局、风格、颜色、文字、页眉、页脚、背景等都是通过后台系统设置出来的，无需任何编程就可以应对个性化的需求。

后台-外观-主题选项，我们就进入了如下配置管理界面：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada_gsetting-websoft9.jpg)

**布局：**对网站内容区的宽度进行设置，一般建议布局采用宽屏模式，网站宽度设置为：1140px；

**菜单：**菜单是网站最重要的部分，设置也非常灵活。为了能够快速上手，我们只对“主菜单”和“手机菜单”的内容进行设置

**响应式：**响应式是即多屏幕自适应，默认请开启；

**颜色：**系统预设了10个颜色皮肤（注意是皮肤），尽量选择一个与您企业logo颜色相近似的皮肤颜色。也可以自定义，但自定义颜色需要对所有与颜色有关的设置中进行操作

**页眉：**即网站的顶部区域，通常网站所有页面都使用同样的页眉，以保持网站的整体风格统一。

*   页眉位置：一般选择顶部
*   页眉布局：一共6种选择，建议选择第一种
*   页眉样式：对页眉的css进行更改，高级用户使用
*   置顶页眉：页面在向上滚动的时候，页眉固定便在浏览器的顶部位置，这个就是置顶页眉。默认选择开启，保持较好的访问体验

**Logo：**即管理自己网站的logo，系统可以对主logo、置顶页眉logo、移动端logo、高清屏幕的logo分别进行设置，也可以只上传一个主logo，其他自动调用这个logo

**图标：**即我们常说的favicon.ico，显示在浏览器的Tabs上，非常重要。默认图标网站Favicon的大小为：16px x 16px。

**页面标题栏：**顾名思义即页面的标题区域，是在菜单栏的下方（如果有Slider的话一般在Slider的下方），每个页面的页面标题栏显示的内容有差异。面包屑导航即我们常说的“网站当前路径”

**滑动栏：**指的是网站右上角通过“+”来开启的伸缩内容，默认建议关闭

**页脚：**即网站的底部区域，分为页脚内容区和页脚版权区，其中页脚版权区在网站的最底部。Avada中页脚内容区是通过小工具来控制显示的，页脚列数即页脚内容区进行分割的内容块数，默认为4

**侧边栏：**主要对通用性的网页侧边内容区进行定义，高级用户使用

**背景：**网站背景图片设置

**版式：**即网站排版，设计到字体大小、H1-H6标题定义，是网站最重要的设置部分之一。正文版式中的字体，我们一般选择“微软雅黑”，字体大小为14。标题字体也默认选择“微软雅黑”比较合适。

**简码风格：**简码是插入html代码的短代码，这是WordPress提供的一中功能扩展方案，适合高级用户使用

**博客：**即文章管理，这里可以对文章分类、文章详情进行个性化的版式设计，内容元素显示控制，请保持默认设置

**作品集：**即案例管理，表现形式为图文混排的文字管理，保持默认设置即可

**社交媒体：**对社交媒体的图标和链接进行录入和设置。录入的社交媒体可以显示在页眉，也可以显示在页脚。可以通过“页眉社交图标”和“页脚社交图片”分别进行显示控制。此类别下的“社交分享盒”主要是对页面分享进行设置；

**幻灯片：**高级用户使用

**Elastic幻灯片：**Avada已经禁用了Elastic幻灯片，无需设置

**光盒：**光盒是点击图片的时候，网站自动对图片进行播放，这种效果即光合。高级用户使用

联系表：

**搜索页面：**对搜索图标的显示位置、搜索内容范围、搜索结果显示方式进行设置，高级用户使用

**附加：**高级用户使用

**高级：**高级用户使用

**自定义CSS：**开发者使用

**导入/导出：**对网站通用设置与配置的内容进行备份和导出导入，普通用户慎用

###### 第二步 首页制作

在Avada主题中，首页与其他页面的制作原理是一样的，但显然首页更具有代表性，因此本章重点介绍首页的在线制作。

在学会制作前，请仔细阅读如下的首页布局图：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada_indexmap-websoft9.jpg)

如果我们通过4.1 网站通用设置与配置已经完成了页眉、页脚，那我们制作首页就非常简单了，只需要完成首页对应的Slider（轮播）和内容设置，再套用已经预设值好的页眉、页脚，首页就完成了。

制作首页有两种方式，包括：新建一个页面，命名为首页或在对一个已有的首页页面进行更改。在这里我们假设新建一个首页：

1、后台-页面-新增页面，我们会看到如下页面

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-addnewpage-websoft9.jpg)

上图就是一个页面制作界面，其中“Fusion页面构建器”为可视化模式，“默认编辑器”为code编辑模式，对于普通用户，我们选择可视化编辑模式

四个Tap，分别是列选项、构建器元素、自定义模板、预定模板。

列选项即css中的Div、行、列，全宽包含容器相当于一个全宽的div，div中可以容纳各种不同宽度的列。系统对列进行了比例划分归类，分别是1/1,1/2,1/3等

构建器元素还需要自己反复探索

自定义模板即对自己制作的页面保存为模板，后面新建页面就可以直接套用

预定模板即系统内置的模板，可以套用但是不能更改

2、如果制作首页？我们建议对一个已有的页面进行可视化编辑，这样更有感觉，学习的效率更高

###### 第三步 轮播制作

轮播（Slider）是现代网页制作的一种常见的展现方式，我们务必掌握这个技能。Avada采用知名的轮播插件Slider Revolution作为主要（唯一）的轮播工具。

轮播的制作和使用步骤如下：

1、后台- Slider Revolution-新建滑块

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/Revolutionslider/3bc66360.jpg)

2、输入滑块名称，选择布局和样式，保存。轮播文件就新建好了

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/Revolutionslider/revs-new.jpg)

3、点击“Slider Editor”标签，进入轮播项的设计与处理

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/Revolutionslider/6823997d.png)

接下来，我们就像制作ppt一样制作轮播了

4、轮播完成之后，需要通过页面调用这个轮播。任意一个页面的页面选项，都有幻灯片的调用项。具体如下：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/Revolutionslider/80427780.png)

###### 第四步 菜单管理

菜单是网站的核心入口，Avada可以把所有内容的标题和链接通过菜单的形式组织起来，然后供页面调用。

那么是如何实现自己的菜单的呢？

1、后台-外观-菜单，进入菜单编辑页面

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-createmenu-websoft9.png)

2、创建一个新菜单，名称定义为“我的菜单”（任意命名）

3、选择左侧菜单来源，分别添加到菜单中。显示位置选择“main navigation”为主菜单位置。菜单添加完成后，保存菜单

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-createmenu002-websoft9.png)

4、我们刷新网站，发现菜单已经更改成我们的菜单了

###### 第五步 文章管理

文章是动态的内容区域，一般网站的新闻主要通过文章管理来实现。

我们以“制作一个动态的新闻中心栏目”来学会文章管理功能。具体操作如下：

1、后台-文章-分类目录-添加新分类目录，例如：公司新闻，保存

2、文章-写文章，其中分类目录勾选我们刚刚新建的“公司新闻”。可以增加多个文章

3、新建一个页面，命名为“新闻中心”，给此页面增加一个行的容器元素

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-rongqi001-websoft9.png)

4、给行内添加一个构建起元素，选择博客

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-rongqi002-websoft9.png)

5、进入博客调用（文章调用）设置页面，其中分类选择刚刚新建的“公司新闻”类目

6、保存页面，完成

###### 第六步 案例管理（作品）

Avada有专有的案例管理功能，在后台体现问“作品”。作品管理与文章管理非常类型，都是建栏目，增加作品项，然后在响应的页面进行调用。

下面以一个“新建一个公司官网的成功案例”为例来进行说明，具体如下：

1、后台-作品-作品分类，我们建立一个“设计案例”分类，保持

2、作品-新文章（即增加案例项），自行填写

3、对作品的特色图像进行设置（这样页面调用的时候才会有图片的动画效果）

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-spepic-websoft9.png)

4、新建一个页面，命名为“案例”，给此页面增加一个行的容器元素

5、给行业增加一个构建器元素-作品

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-rongqi003-websoft9.png)

6、进入作品调用设置页面，可以一般设置一边预览

7、设计完成，保存

###### 第七步 常见问题管理

常见问题是一个服务类或营销型官网必须具备的栏目，通过简单有效的一问一答的方式，快速的解答客户的疑问。Avada有一个常见问题的模块：

下面以一个“新建一个公司官网的常见问题页面”为例来进行说明，具体如下：

1、后台-常见问题-FAQ目录，我们建立一个“安装问题”分类，保持

2、常见问-写文章（即增加常见问题项），自行填写一个或多个

3、新建一个页面，命名为“常见问题”，给此页面增加一个行的容器元素

4、给行业增加一个构建器元素-常见问题

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-rongqi004-websoft9.png)

6、进入常见问题调用设置页面，可以一般设置一边预览

7、设计完成，保存

###### 第八步 小工具栏的使用

小工具栏是Avada中的高级功能项，小工具的特点就是可以自行定义内容&amp;可以被任何页面调用。因此，小工具对于个性化的建站非常有作用。小工具栏的的使用原理是：把网页的一些元素或功能插到指定的小工具上，然后需要用到这些元素的页面直接调用响应的小工具即可。

系统默认有几个固定的小工具（不可以删除），包括：

*   Blog Sidebar   用于所有文章内容的侧边栏
*   Footer  Widget1   用于页脚的工具栏1
*   Footer  Widget2  用于页脚的工具栏1
*   Footer  Widget3  用于页脚的工具栏1
*   Footer  Widget1  用于页脚的工具栏1

如何自定义自己的小工具栏，并调用呢？

下面我们一个“建立小广告内容小工具”为例来进行演示，具体如下：

1、后台-外观-小工具

2、小工具-添加小工具（名称一定只能是英文，否则无法调用）

3、将左侧的“可用小工具”元素拖到右侧小工具栏中（如果拖拽的是文本项，可以在文本项中自定义任意html或js代码），然后保存

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-widget001-websoft9.png)

4、新建或任何已有的页面进入编辑状态，插入构建器元素-小工具区

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-widget002-websoft9.png)

5、选择您的小工具，保存

备注：小工具一旦与页面实现了关联之后，小工具的内容可以任意更改，页面调用之处都会自动发送变化。实现了一次定义，多处使用的快捷方法。

###### 第九步 SEO

Avada的SEO是通过一个SEO插件来实现的，这里我们推荐使用最广的SEO插件-Yoast SEO。

如何实现网站的SEO呢？

1、安装Yoast SEO（免费插件）

2、按照Yoast SEO的设置向导进行初始化的设置

3、Yoast SEO一旦安装完成之后，所有的页面（文章）类型都嵌入登录SEO选项。我们通过页面-所有页面，会看到所有页面都有SEO的属性（其中圆图标代表SEO的优化程度），如下图：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-seo001-websoft9.png)

4、进入任意一个页面的的编辑状态项，都会出现SEO的选项。一般填写关键字和描述即可。Yoast SEO还有一个分析检查SEO填写的功能，仅供参考

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-seo002-websoft9.png)

说明：以上仅描述了SEO的实现方法。SEO是一门学问（伴随人工智能出现，SEO未来的学问会越来越浅），如何设置关键、描述等信息，还需要自己反复探索。

#### 热门主题：Porto

Porto是自适性的Wordpress + 电子商务主题，具有超强的自定义，易于使用和完全自适性。适合各种类型的企业网站和电子商务网站。Porto包括30个首页布局和皮肤，提供了大量变量使用任何类型网站。

![](https://oss.aliyuncs.com/netmarket/product/48635c98-5516-441d-99aa-1724d36b2dd8.png)

##### 下载和安装

Porto的安装和下载有两种方式，请根据实际情况选择合适您的方式：

###### 方式一：使用Porto镜像安装包（推荐）

* [阿里云WordPress镜像（含Porto中文主题包）](https://market.aliyun.com/products/53616009/cmjj023934.html)
* [华为云WordPress镜像（含Porto中文主题包）](https://app.huaweicloud.com/product/00301-84814-0--0)

###### 方式二：到themeforest.net购买

购买地址：https://themeforest.net/item/porto-responsive-wordpress-ecommerce-theme/9207399

###### 方式三：向 Websoft9 下载主题自行安装
* [Porto 4.7.3 官方原版下载](https://libs.websoft9.com/apps/wordpress/wordpress5.2.3-porto4.7.3-zh.tar.gz)
---

**FAQ**

* 镜像包方式中的Porto有没有授权码？没有授权码，但可以正常使用
* Porto授权码有什么作用？可以在线升级主题和导入模板

##### Porto主题教程（9步建站）

在熟悉了WordPress之后，我们通过如下9个步骤的实践来熟悉Porto，同时将前面导入的演示页面修改成我们自己的页面，那么也就万完成了一个网站的初步制作。

教程努力编写中...

### 插件

插件是WordPress功能的扩展，也是WordPress得以独步天下的“杀手锏”，其插件实现了名副其实的“即插即用”。全球有超过100万的WordPress插件，涵盖电商、表单、邮件、论坛、备份、美化、社交分享、轮播等领域。

#### 寻找插件

寻找所需的插件，有三种方式：

1. 通过WordPress后台-外观-安装插件，在线获取[WordPress插件库](https://wordpress.org/plugins/)的插件 
2. 通过百度、google等搜索“WordPress插件”，淘到自己喜欢的主题
3. 通过插件交易市场购买功能强大的插件，例如：[codecanyon.net](https://codecanyon.net/?osr=tn)

#### 安装插件

安装插件一般有两种方式

1. 通过WordPress后台-插件-安装插件，后台上传插件安装（推荐）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-addplugins-websoft9.png)
2. 通过FTP工具，将主题文件上传到 WordPress 根目录下 */wp-content/plugin*

#### Top20常用插件

如下插件在使用WordPress中会经常用到：

| 名称 | 类别 | 用途 | 付费 or 免费 |
| :--- | :--- | :--- | :--- |
| WooCommerce | 电商 | 将WordPress扩展成电子商务网站 | 免费 |
| WooCommerce Tab Manager | 电商 | 电商页面Tab扩展 | 免费 |
| UpdraftPlus WordPress Backup Plugin | 备份 | 自动备份WordPress | 免费 |
| Visual Composer: Page Builder for WordPress | 排版与布局 | 客户化编辑器 | 收费 |
| Slider Revolution Responsive WordPress Plugin | 排版与布局 | 强大无比的轮播动画制作与管理 | 收费 |
| Ninja Forms – The Easy and Powerful Forms Builder | 表单 | 表单插件 | 免费 |
| Duplicator – WordPress Migration Plugin | 系统管理 | 网站整体打包工具，拥有备份与迁移 | 免费 |
| All-in-One WP Migration | 系统管理 | 网站整体打包与恢复工具 | 免费 |
| download-monitor | 下载管理 | 下载管理 | 免费 |
| File Manager | 文件管理 | 在线文件管理工具 | 免费 |
| Yoast SEO | SEO | SEO优化建议和按页面设置 | 免费 |
| All in One SEO | SEO | SEO优化建议和按页面设置 | 免费 |
| Remove Google Fonts | 系统管理 | 屏蔽google字体，提升速度 | 免费 |
| WP-Optimize | 系统管理 | 系统优化和瘦身 | 免费 |
| WP Job Manager | 业务应用 | 招聘、职位管理 | 免费 |
| WP Mail SMTP by WPForms | 业务应用 | SMTP邮件发送设置 | 免费 |
| weDocs – the documentation plugin | 业务应用 | 在线文档工具 | 免费 |
| Smartideo | 业务应用 | 优酷等视频插入 | 免费 |
| Essential Grid | 排版与布局 | 文章、页面网格工具 | 免费 |
| Post Grid, List for WordPress – Content Views | 排版与布局 | 文档、页面调用工具 | 免费 |

### 电商 WooCommerce

WooCommerce 是 WordPress 的一个电子商务插件，在 WordPress 上安装这个插件，就可以将你的 WordPress 改造成电商网站。据说 WooCommerce 已超过上亿次下载，市场占有率领先于同类软件。  

因此，我们拿出一个章节来对 WooCommerce 进行说明

#### 功能扩展

WooCommerce 官方提供了 主题市场和插件市场 以扩展 WooCommerce 的功能。

#### 支付配置

WooCommerce 默认提供了国外主流的支付插件，下面重点介绍中国本地化支付的两个支付配置

##### 配置支付宝即时到账支付

1. 申请支付宝商家账户，申请开通即时到账；
2. 在商城中安装支付宝支付插件（如果没有支付宝插件，请通过此处购买）
3. 在商城中配置支付宝参数。配置界面如下：
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/intallalipay-websoft9.png)

##### 配置微信扫描支付

WooCommerce微信支付插件使用非常简单，只需要如下步骤，就可以让你的WordPress商城添加微信支付功能。

1. 安装微信支付插件（如果没有支付宝插件，请通过此处购买）
2. 获取微信公众号APPID，密钥，微信支付密钥以及微信支付授权目录
   - 获取微信公众号的AppID\(应用ID\) 和AppSecret\(应用密钥\) AppID\(应用ID\) 和AppSecret\(应用密钥\)是微信公众号与第三方网站（wordpress）通信的授权ID和密码，非常重要，必须填写。 请登录微信公众平台（https://mp.weixin.qq.com），点击开发-配置获取：AppID 和AppSecret
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/wechatpay-help001-websoft9.png)
   - 获取微信支付密钥登录微信支付商户平台（https://pay.weixin.qq.com），在账户设置-API安全中找到并设置密钥，密钥为32位，注意一下，获取密钥后保留备用
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/weichatpay-help002-websoft9.png)
3. 添加授权支付目录在微信公众平台（https://mp.weixin.qq.com）点击-微信支付-开发配置，设置授权支付目录 微信支付插件的授权支付目录为：https://你的域名/wp-content/plugins/wechat-weixin-payments-for-woocommerce/
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/weichatpay-help003-websoft9.png)
4. 设置回调域名在微信公众平台（https://mp.weixin.qq.com）-开发-接口权限中找到-网页服务-网页账号修改授权回调页面域名，域名为你的网站域名，注意区分www和不带www；
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/weichatpay-help004-websoft9.png)
5. 配置微信支付插件在woocommerce设置，支付设置中找到微信支付设置，填入微信公众号appid和微信支付密钥
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/weichatpay-help005-websoft9.png)

### 管理员密码

实际工作中，我们可能会 **修改** 或 **找回** WordPress 管理员密码

#### 修改WordPress管理员密码？

1. 以管理员账号登录后台
2. 依次打开：【用户】>【所有用户】，编辑需要修改密码的账号
3. 往下拉倒【账号管理】项，点击【生成密码】，然后修改密码，并更新个人资料 
   ![Wordpress 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-modifypw-websoft9.png)

#### 找回 WordPress 管理员密码？

若不记得 WordPress 管理员密码，可以通过如下两个方式找回

##### 方案一：通过邮件找回密码

WordPress可以通过发送邮件找回密码，但前提条件是您的 WordPress 网站已经配置好SMTP
![Wordpress 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-forgetpw-websoft9.png)

##### 方案二：修改数据库中的密码字段

如果不能发邮件，请登录数据库管理面板 phpMyAdmin 进行修改

1. 登录 phpMyAdmin，并找到你的网站数据库下的 *wp_user* 表
   ![Wordpress 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-wpusers-websoft9.png)
2. 编辑管理员用户（下图以用户名 `admin`为例）  
   ![Wordpress 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-wpuserspw-websoft9.png)
3. 截图的地方数据库密码(MD5加密后的密文)，用`21232f297a57a5a743894a0e4a801fc3`替换之
4. 点击【执行】
3. 新的密码为`admin`

### 修改上传文件类型的限制

WordPress默认支持大部分图片等文件格式的上传，但也有一些文件格式是不支持的，根据实际需要，可以增加或禁止一些格式的文件上传。设置方法如下：

把以下代码加到主题目录（```/wp-content/themes/twentysixteen```）下的 functions.php 文件中：
	
   	function edit_upload_types($existing_mimes = array()) {
	// 允许上传的文件类型
	$existing_mimes['woff'] = 'application/woff';
	$existing_mimes['rar'] = 'application/rar';
	
    // 如需添加更多文件类型支持，在其后增加代码即可

	// 不允许上传的的文件类型
	unset( $existing_mimes['jpg'] );

	return $existing_mimes;
	}
	add_filter('upload_mimes', 'edit_upload_types');
    
> 以上是以自带主题 twentysixteen 为例，如果您使用的不是这款主题，则需要到对应主题目录下的 functions.php 文件中添加。

### WordPress 与 Discuz 集成

搭建网站时很有可能遇到这样的问题：使用WordPress搭建了页面，又使用Discuz搭建了一个论坛，两者的用户数据存在不同的数据库中，这样就无法统一整理了。

为了解决这一问题，可以使用 Discuz 提供的 [UCenter插件](https://wordpress.org/plugins/ucenter-integration/) 功能来将两者的用户数据进行统一整合。

> Wordpress与Discuz集成是一件复杂的事情，UCenter插件方案我们在WordPress4.6版本上测试可用，其他版本没有测试过。

### WordPress 使用对象存储

当WordPress的图片超过500张的时候，建议将图片存放到对象存储中（一般称之为OSS）  

WordPress使用OSS有两种方式，第一种是通过OSS客户端上传文件，然后在WordPress中调用；第二种是将OSS与WordPress集成，通过WordPress后台上传的文件就自动存放到OSS中。

#### 手工上传文件到OSS（推荐）

1. 通过OSS的客户端工具，上传图片到对象存储
2. 获取对象存储中图片的地址，地址一般类似如下：
   ```
   https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-product-screenshot.png
   ```
3. Wordpress后台-页面编辑-插入多媒体，将图片插入到WordPress系统中
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-oss-adresstowp-websoft9.png)

#### WordPress与OSS集成

1. 将OSS挂载到 WordPress的 wp-upload 文件夹
2. 每次通过WordPress上传的文件，就自动存放到了OSS中

> 挂载 OSS 的操作比较复杂，需要用户自主研究

#### WordPress使用阿里云OSS对象储存

下面以阿里云OSS对象存储为例，介绍在WordPress中使用OSS，实现WordPress后台的页面或文章使用资源时自动上传到OSS，并关联使用。具体的操作分两步：在阿里云OSS管理中创建Bucket存储空间；在WordPress后台中配置OSS。

1. 创建 Bucket存储空间

   进入阿里云控制台，可通过菜单的【产品与服务】>【对象存储 OSS】进入OSS控制台，然后点击创建 Bucket按钮创建存储空间，如图：
   ![OSS](https://libs.websoft9.com/Websoft9/blog/tmp/wordpress/zh/oss-websoft9.png)
   
   创建 Bucket 存储空间
   ![OSS](https://libs.websoft9.com/Websoft9/blog/tmp/wordpress/zh/oss-bucket-websoft9.png)
   ![OSS](https://libs.websoft9.com/Websoft9/blog/tmp/wordpress/zh/oss-bucket2-websoft9.png)
   
   > 1、【地域】建议与服务器所在地就近选择，如果使用的是阿里云的服务器，建议选择和服务器同区域，这样可以通过内网互通节约上传流量成本，同时上传速度也快很多的。
   > 
   > 2、【读写权限】选择【公共读】，这样可以实现图片正常访问。

   ![OSS](https://libs.websoft9.com/Websoft9/blog/tmp/wordpress/zh/oss-bucket3-websoft9.png)
   > 通过【概述】查看OSS存储空间对外的访问URL，通过【传输管理】-【域名管理】可以通过CNAME域名解析，将一个更加友好的域名，如 images.websoft9.com ，指向默认的URL。

2. WordPress后台OSS配置

   进入 WordPress 后台，进入【插件】管理，下载阿里云 OSS Upload 插件并启用
   
   ![OSS](https://libs.websoft9.com/Websoft9/blog/tmp/wordpress/zh/wordpress-oss-plugin-websoft9.png)
   
   对 OSS Upload 插件进行配置，使之关联阿里云的OSS对象存储
   
   ![OSS](https://libs.websoft9.com/Websoft9/blog/tmp/wordpress/zh/wordpress-oss-websoft9.png)
   ![OSS](https://libs.websoft9.com/Websoft9/blog/tmp/wordpress/zh/oss-bucket3-websoft9.png)
   
   > **Access Key**和**Secret Key**登录阿里云后台获取：点击阿里云右上角用户头像，选择**accesskeys**，然后创建好AccessKey
   > 
   > 在阿里云的OSS管理界面的【概述】【访问域名】【外网访问】获取相关访问链接和地域节点。配置后点击【地域节点】下方的【测试一下】查看网络连通及读写操作，出现“写入正常, 读取正常, 删除正常”，表示配置成功。

  设置资源本地备份与同步。建议勾选，在网站的前期配置和文件同步过程中，可避免图片丢失无法恢复的问题。
  
  设置完成后点击【保存更改】按钮，然后可以再点击【上传整个本地存储目录】来同步文件到OSS，这个过程可能需要些时间，同步完成后，网站前台页面的图片可以正常访问，表示配置成功。
  ![OSS](https://libs.websoft9.com/Websoft9/blog/tmp/wordpress/zh/wordpress-oss2-websoft9.png)
  

### WordPress 后台10大要点

为了使WordPress运行更有效率，方便维护、方便迁移，我们在实践中总结了WordPress管理员和内容管理者需要注意的10个要点：

1. 上传图片尽量不超过100k/张
2. 如果总图片数量超过500张，建议将图片放到对象存储中，实现动静分离，也便于维护
3. 所有图片名称为英文
4. 新闻的图片大小比例最好为600:400，保证统一性。每篇新闻都要配套图片，美观大方，便于展示
5. 所有页面、新闻 URL 地址均采用英文
6. 后台账号的密码要复杂一些
7. 轮播 Banner 不超过3张
8. 插件数量不超过20个，不用的插件务必卸载，以避免插件冲突而导致网站不可用
9. 网站内容为王，请将精力集中于内容的更新、知识库的建立
10. 视频等大文件请放到其他存储中

### 安装更多的 WordPress 网站

我们的 WordPress 部署包支持用户自主安装更多的 WordPress网站

* [Wordpress(LAMP) 安装一个新的网站](https://support.websoft9.com/docs/lamp/solution-deployment.html#deploy-second-application)
* [Wordpress(LEMP) 安装一个新的网站](https://support.websoft9.com/docs/lnmp/solution-deployment.html#deploy-second-application)

### 增加备案号

如果你使用的WordPress默认自带主题，需要在页面底部增加ICP备案以及链接。具体操作步骤如下：

1. 登录WordPress后台，依次打开【外观】>【小工具】
2. 从左侧的【可用小工具】中拖拽一个【文本】小工具到右侧的【页脚1】
3. 填写好备案号相关信息，增加链接，并分别点击【回车符】按钮和【保存】按钮
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-beian.png)
4. 刷新网页看效果

### MySQL 数据管理

WordPress 预装包中内置 MySQL 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组80端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP/phpmyadmin*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
3. 输入数据库用户名和密码([不知道密码？](#账号密码))
4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MySQL教程》](https://support.websoft9.com/docs/mysql/zh/admin-phpmyadmin.html) ，掌握更多的MySQL实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

## 异常处理

#### 浏览器打开IP地址，无法访问 WordPress（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 WordPress 数据？

是MySQL

#### 我使用的是 Avada 等主题，当 WordPress 升级后，页面编辑乱码了？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/wordpress-avadaeditp-websoft9.png)

**问题原因**： Wordpress升级到5.0版本之后，WordPress 官方提供的默认编辑器发生了本质的变化，导致已有主题无法适应新的 WordPress 编辑器内核  

**解决方案**：安装一个名称为“Classic Editor”的插件，继续使用旧的编辑器内核  

  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/wordpress-classiceditor-websoft9.png)