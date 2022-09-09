---
sidebar_position: 1
slug: /wordpress
tags:
  - WordPress
  - CMS
  - Website
  - Blog
---

# WordPress Getting Started

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

**Using Avada and other themes, when WordPress is upgraded, the page editing is garbled**

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/wordpress-avadaeditp-websoft9.png)

**Cause of problem**： After Wordpress upgrading to version 5.0, the default editor officially provided by WordPress has changed fundamentally, resulting in that the existing theme cannot adapt to the new WordPress editor core  

**Solution**：Install a plug-in named "classic editor" and continue to use the old editor core 

  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/wordpress-classiceditor-websoft9.png)

## WordPress QuickStart

The following is ** xxx ** as a task, it helps users get started quickly.

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

> If after changing the domain name, some of the picture addresses in the website are still the original domain name, you need to manually correct them one by one

> If you cannot access the background operation in step 3 after step 2 is completed, please visit the WordPress database and change the home and siteurl attributes in the option table to [new domain name]

> Through the MySQL visualization tool phpMyAdmin that has been configured in websoft9(http://ip:phpmyadmin or http://ip:9090)Perform shortcuts


### HTTPS Additional Configure {#https}

**[Standard HTTPS configuration](./administrator/domain_https)** After completion, the following exceptions may be encountered:

- [After HTTPS is configured, some resources of the website cannot be loaded?](./wordpress/admin#httpsmore)

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

### Add record number

If you use WordPress with its own theme by default, you need to add ICP filing and links at the bottom of the page. The specific operation steps are as follows:

1. Log in to WordPress background and open 【appearance】> 【gadget】 in turn

2. Drag a text widget from the available widgets on the left to the footer 1 on the right

3. Fill in the relevant information of the record number, add a link, and click the 【Enter】and the【save】respectively
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-beian.png)

4. Refresh the page to see the effect

### Managing Plugins

Plugins are ways to extend and add to the functionality that already exists in WordPress.

For instructions and information on downloading, installing, upgrading, troubleshooting, and managing your WordPress Plugins, see [Managing Plugins](https://codex.wordpress.org/Managing_Plugins). If you want to develop your own plugin, there is a comprehensive list of resources in Plugin Resources.

**Looking for plug-ins**

There are three ways to find the required plug-ins:

1. Through WordPress background - appearance - install plug-ins,Get [WordPress plug-in library](https://wordpress.org/plugins/) Online
2. Search "WordPress plug-in" on Baidu, Google, etc., and find your favorite theme
3. Purchase powerful plug-ins through the plug-in trading market, such as:[codecanyon.net](https://codecanyon.net/?osr=tn)

**Add new plugins**

1. Administration Screen > Plugins > Add New
   ![WordPress add plugin](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-addnewplugin-websoft9.png)  

2. Search the plugins which you want,and install it,active it  

3. you can also add plugins by upload you package of zip

**Top20 plugins**

The following plug-ins are often used in WordPress:

|Name | category | purpose | paid or free|
| :--- | :--- | :--- | :--- |
|Woocommerce | e-commerce | expand WordPress into an e-commerce website | free|
|Woocommerce tab manager | e-commerce | e-commerce page tab extension | free|
|Updraftplus WordPress backup plugin | backup | automatic backup of WordPress | free|
|Visual Composer: page builder for WordPress | typesetting and layout | customized editor | charge|
|Slider revolution responsive WordPress plugin | layout and layout | powerful round robin animation production and management | charging|
|Ninja forms – the easy and powerful forms builder | forms | form plug-ins | free|
|Duplicator – WordPress migration plugin | system management | website overall packaging tool with backup and migration | free|
|All in one WP migration | system management | website overall packaging and recovery tool | free|
|Download monitor | download management | download management | free|
|File manager | file management | online file management tool | free|
|Yoast SEO | SEO | SEO optimization suggestions and settings by page | free|
|All in one SEO | SEO | SEO optimization suggestions and settings by page | free|
|Remove Google fonts | system management | block Google fonts and improve speed | free|
|WP optimize | system management | system optimization and slimming | free|
|WP job manager | business application | recruitment and position management | free|
|WP mail SMTP by wpforms | business application | SMTP mail sending settings | free|
|Wedocs – the documentation plugin | business applications | online documentation tools | free|
|Smartideo | business application | video insertion such as Youku | free|
|Essential grid | typesetting and layout | article and page grid tools | free|
|Post grid, list for WordPress – content views | typesetting and layout | document and page calling tools | free|
|Fat rat collect | data collection | open source plug-in for bulk collection of article data, including wechat, Jianshu, Zhihu, list details, etc. | free|

### Adding New Themes

1. Download or prepare a theme which has been packaged and the suffix of the package is zip
2. Login to the WordPress,go to Administration Screen -> Appearance -> Themes -> Add new
   ![WordPress add new plugin](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-addnewtheme-websoft9.png)
3. upload Themes or one Click the online themes,you can install the theme
   ![WordPress add plugin](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-uploadtheme-websoft9.png)
4. After installation of theme,you should active it by Administration Screen > Appearance > Themes  
5. From the Themes panel, roll over the Theme thumbnail image for the Theme to activate the Theme click the Activate button.  

### Woocommerce payment configuration

Woocommerce is an e-commerce plug-in for WordPress. By installing this plug-in on WordPress, you can transform your WordPress into an e-commerce website. It is said that woocommerce has been downloaded more than 100 million times, and its market share is ahead of similar software.

Woocommerce officially provides a theme market and a plug-in market to expand woocommerce's functions.

Woocommerce provides mainstream foreign payment plug-ins by default. The following focuses on two payment configurations for localized payment in China

**Alipay instant payment**

1. Apply for a Alipay merchant account, and apply for instant arrival;

2. Install the Alipay payment plug-in in the mall (if there is no Alipay plug-in, please buy it here)

3. Configure Alipay parameters in the mall. The configuration interface is as follows:
 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/intallalipay-websoft9.png)

**Wechat scanning payment**

The woocommerce wechat payment plug-in is very simple to use. You can add wechat payment function to your WordPress mall just by following the steps below.

1. Install wechat payment plug-in (if you don't have Alipay plug-in, please buy it here)

2. Obtain wechat official account appid, key, wechat payment key and wechat payment authorization directory
-Get appid and appsecret of wechat official account application IDand application key are the authorization ID and password for wechat official account to communicate with the third-party website (WordPress). They are very important and must be filled in. Please log in to [wechat public platform](https://mp.weixin.qq.com), Click development-configuration to get appid and appsecret
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/wechatpay-help001-websoft9.png)
-Get wechat payment key and log in to [wechat payment merchant platform](https://pay.weixin.qq.com) Find and set the key in account settings-API security. The key is 32 bits. Please note that it is reserved for use after obtaining the key
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/weichatpay-help002-websoft9.png)

3. Add authorized payment directory on [wechat public platform](https://mp.weixin.qq.com).Click wechat payment-development configuration, and set the authorized payment directory. The authorized payment directory of wechat payment plug-in is: (https://your domain/WP content/plugins/wechat Weixin payments for woocommerce)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/weichatpay-help003-websoft9.png)

4. Set callback domain name on [wechat public platform](https://mp.weixin.qq.com). In development-Interface permissions, find Web Services-web account modification authorization callback page domain name. The domain name is your website domain name. Pay attention to distinguish between WWW and without WWW;
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/weichatpay-help004-websoft9.png)

5. Configure wechat payment plug-in. Find wechat payment settings in woocommerce settings and fill in wechat official account appid and wechat payment key
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

Run `docker ps`, view all containers when WordPress is running:  

```bash
CONTAINER ID   IMAGE               COMMAND                  CREATED          STATUS          PORTS                                       NAMES
2fe10a179a6c   phpmyadmin:latest   "/docker-entrypoint.…"   16 seconds ago   Up 16 seconds   0.0.0.0:9090->80/tcp, :::9090->80/tcp       phpmyadmin
d43ecff5608c   wordpress:latest    "docker-entrypoint.s…"   39 seconds ago   Up 38 seconds   0.0.0.0:9001->80/tcp, :::9001->80/tcp       wordpress
9f4aa7ad771b   mariadb:10.4        "docker-entrypoint.s…"   39 seconds ago   Up 38 seconds   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp   wordpress-db
```

### Path{#path}

WordPress installation directory: */data/apps/wordpress*  
WordPress configuration file: */data/apps/wordpress/data/wordpress/wp-config.php*   
WordPress data directory: /data/apps/wordpress/data/mysql_data

### Port{#port}

In addition to common ports such as 80, 443, etc., the following ports may be used:

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 3306 | Remote connect MariaDB | Optional |
| 9090 | Web managment GUI for MySQL | Optional |

### Version{#version}

WordPress view it on console

### Service{#service}

```shell
sudo docker start | stop | restart  wordpress
sudo docker start | stop | restart  wordpress-db
sudo docker start | stop | restart  phpmyadmin
```

### CLI{#cli}

[wp-cli](https://wp-cli.org/)

### API

[REST API](https://developer.wordpress.org/rest-api/)
