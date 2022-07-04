---
sidebar_position: 1
slug: /wordpress
tags:
  - WordPress
  - CMS
  - Website
  - Blog
---

# WordPress Getting Started test sync

[WordPress](https://www.wordpress.org) is open source software you can use to create a beautiful website, blog, or app.There are 28% of the web uses WordPress, from hobby blogs to the biggest news sites online in the world. Beautiful designs, powerful features, and the freedom to build anything you want. WordPress is both free and priceless at the same time.Extend WordPress with over 45,000 plugins to help your website meet your needs. Add an online store, galleries, mailing lists, forums, analytics, and much more.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-product-screenshot.png)  

If you have installed Websoft9 WordPress, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. **[Get](./user/credentials)** default username and password of WordPress
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for WordPress
 

## WordPress Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://domain name* or *http://Internet IP*, you will enter the WordPress   
   ![Wordpress installation language](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-installsetlanguage-websoft9.png)  

2. Select your language, then go to next step  

3. Set administrator user, password and mail, then click **Install WordPress**
   ![Wordpress installation administrator](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-installsetadmin-websoft9.png)  

4. OK, it has been installed successfully.
   ![Wordpress installation ok](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-installss-websoft9.png)  

5. Use *http://domain or Internet IP/wp-admin*  to login to WordPress's dashboard
   ![Wordpress installation dashbaord](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-bkdashboard-websoft9.png)

> More useful WordPress guide, please refer to [WordPress Documentation](https://wordpress.org/support/)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**使用 Avada 等主题，当 WordPress 升级后，页面编辑乱码了**

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/wordpress-avadaeditp-websoft9.png)

**问题原因**： Wordpress升级到5.0版本之后，WordPress 官方提供的默认编辑器发生了本质的变化，导致已有主题无法适应新的 WordPress 编辑器内核  

**解决方案**：安装一个名称为“Classic Editor”的插件，继续使用旧的编辑器内核  

  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/wordpress-classiceditor-websoft9.png)

## WordPress QuickStart

下面以 **[WordPress 使用 Avada 主题建站](./wordpress/solution#avada)** 作为一个任务，帮助用户快速入门。

## WordPress Setup

### SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console  

2. Log in WordPress Console  

3. Go to Setting->General Settings, set your email which will diplay in the email sended for users
   ![WordPress SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-setdmail-websoft9.png)  

4. Install the plugin: [WP Mail SMTP by WPForms](https://wordpress.org/plugins/wp-mail-smtp/)  

5. Start to configure the WP Mail SMTTP(This sample is SendGrid)
   ![WordPress SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-smtpsetdetail-websoft9.png)  

6. Click the **Send Email**, you can get the feedback *"Your email was sent successfully!..."* if SMTP is useful
   ![WordPress SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-mailss-websoft9.png)


### DNS Additional Configure（Modify URL）{#dns}

Complete **[Five steps for Domain](./administrator/domain_step)** ，Set the URL for WordPress：

1. Connect Cloud Server, complete the Domain binding
   ![Wordpress modify URL](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-changeurl-websoft9.png)
  
2. Save it

> 如果更换域名后，网站中有一部分图片地址还是原来的域名，此时需要手工逐一修正
> 如果在第2步操作完成后，无法进入第3步访问后台操作，请访问 Wordpress 数据库，将 option 表中的 home 和 siteurl 两个属性修改为【新的域名】
> 通过 Websoft9 已经配置好的 MySQL 可视化工具 phpMyAdmin (http://ip/phpmyadmin 或 http://ip:9090 )进行快捷操作

### HTTPS Additional Configure {#https}

**[标准 HTTPS 配置](./administrator/domain_https)** 完成后，可能会遇到如下的异常情况：

- [配置HTTPS后，网站部分资源无法加载？](./wordpress/admin#httpsmore)

### WordPress File type limit extend

WordPress supports uploading of most image formats such as images by default, but some file formats are not supported. According to personal needs, we need to add some formats. Of course, some formats can be prohibited from being uploaded. 

1. Edit `function.php` file on your Theme directory
2. Copy the code section to functions.php file
  ```
  function edit_upload_types($existing_mimes = array()) {

  // Allowed file types to upload
  $existing_mimes['woff'] = 'application/woff';
  $existing_mimes['rar'] = 'application/rar';

  // To add more file type support, add code later.

  // File types that are not allowed to be uploaded
  unset( $existing_mimes['jpg'] );

  return $existing_mimes;
  }
  add_filter('upload_mimes', 'edit_upload_types');
  ```

### 增加备案号

如果你使用的WordPress默认自带主题，需要在页面底部增加ICP备案以及链接。具体操作步骤如下：

1. 登录WordPress后台，依次打开【外观】>【小工具】

2. 从左侧的【可用小工具】中拖拽一个【文本】小工具到右侧的【页脚1】

3. 填写好备案号相关信息，增加链接，并分别点击【回车符】按钮和【保存】按钮
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-beian.png)

4. 刷新网页看效果

### Managing Plugins

Plugins are ways to extend and add to the functionality that already exists in WordPress.

For instructions and information on downloading, installing, upgrading, troubleshooting, and managing your WordPress Plugins, see [Managing Plugins](https://codex.wordpress.org/Managing_Plugins). If you want to develop your own plugin, there is a comprehensive list of resources in Plugin Resources.

**寻找插件**

寻找所需的插件，有三种方式：

1. 通过WordPress后台-外观-安装插件，在线获取[WordPress插件库](https://wordpress.org/plugins/)的插件 
2. 通过百度、google等搜索“WordPress插件”，淘到自己喜欢的主题
3. 通过插件交易市场购买功能强大的插件，例如：[codecanyon.net](https://codecanyon.net/?osr=tn)

**Add new plugins**

1. Administration Screen > Plugins > Add New
   ![WordPress add plugin](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-addnewplugin-websoft9.png)  

2. Search the plugins which you want,and install it,active it  

3. you can also add plugins by upload you package of zip

**Top20 插件**

如下插件在使用 WordPress 中会经常用到：

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
| Fat Rat Collect | 数据采集 | 批量采集文章数据的开源插件，采集含括微信、简书、知乎、列表详情等 | 免费 |  

### Adding New Themes

1. Download or prepare a theme which has been packaged and the suffix of the package is zip
2. Login to the WordPress,go to Administration Screen -> Appearance -> Themes -> Add new
   ![WordPress add new plugin](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-addnewtheme-websoft9.png)
3. upload Themes or one Click the online themes,you can install the theme
   ![WordPress add plugin](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-uploadtheme-websoft9.png)
4. After installation of theme,you should active it by Administration Screen > Appearance > Themes  
5. From the Themes panel, roll over the Theme thumbnail image for the Theme to activate the Theme click the Activate button.  

### WooCommerce 支付配置

WooCommerce 是 WordPress 的一个电子商务插件，在 WordPress 上安装这个插件，就可以将你的 WordPress 改造成电商网站。据说 WooCommerce 已超过上亿次下载，市场占有率领先于同类软件。  

WooCommerce 官方提供了 主题市场和插件市场 以扩展 WooCommerce 的功能。

WooCommerce 默认提供了国外主流的支付插件，下面重点介绍中国本地化支付的两个支付配置

**支付宝即时到账支付**

1. 申请支付宝商家账户，申请开通即时到账；

2. 在商城中安装支付宝支付插件（如果没有支付宝插件，请通过此处购买）

3. 在商城中配置支付宝参数。配置界面如下：
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/intallalipay-websoft9.png)

**微信扫描支付**

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

### Manage WordPress Password

We may **Modify** or **recover** WordPress administrator password

**Modify WordPress administrator password**

Log in Wordpress, go to Users->Your Profile,update your password
![Wordpress Modify WordPress administrator password](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-modifypw-websoft9.png)

**Recover WordPress administrator password**

If you don't remember the WordPress administrator password, you can retrieve it in the following two ways.

**Recover by Email**

WordPress can retrieve the password by sending an email, but only if your WordPress site has already configured SMTP.
![Wordpress Modify WordPress administrator password](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-forgetpw-websoft9.png)

**Recover by database**

If the server does not support the function of sending email passwords, the database management panel phpmyadmin will modify it.

1. Log in to phpMyAdmin, find the *wp_user* table of your WordPress database
   ![Wordpress database](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-wpusers-websoft9.png)  

2. Edit the user(e.g. your username is `admin`)  
   ![Wordpress database](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-wpuserspw-websoft9.png)  

3. Replace the data with `21232f297a57a5a743894a0e4a801fc3`(MD5)  

4. Click **run**  

5. The new password is `admin` now

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage WordPress

通过运行`docker ps`，可以查看到 WordPress 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

下面仅列出 WordPress 本身的参数：

### Path{#path}

WordPress installation directory: */data/wwwroot/wordpress*  
WordPress configuration file: */data/wwwroot/wordpress/wp-config.php*   

### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 3306 | Remote connect MySQL | Optional |
| 80 | HTTP requests for WordPress | Required |
| 443 | HTTPS requests WordPress | Optional |
| 9090 | Web managment GUI for MySQL | Optional |

### Version{#version}

WordPress 控制台查看

### Service{#service}

```shell
sudo docker start | stop | restart | stats wordpress
```

### CLI{#cli}

[wp-cli](https://wp-cli.org/)

### API

[REST API](https://developer.wordpress.org/rest-api/)
