---
sidebar_position: 3
slug: /wordpress/admin
tags:
  - WordPress
  - CMS
  - Website
  - Blog
---

# WordPress Maintenance

This chapter is special guide for WordPress maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide
  
### WordPress 10 major points

In order to make WordPress run more efficiently, easy to maintain, and easy to migrate, we have summarized 10 key points that WordPress administrators and content managers need to pay attention to in practice:

1. Upload pictures as far as possible no more than 100k/sheet
2. If the total number of pictures exceeds 500, it is recommended to put the picture in the object storage to achieve dynamic separation and easy maintenance.
3. All picture names are in English
4. The image size ratio of the news is preferably 600:400 to ensure uniformity. Each news must be accompanied by pictures, beautiful and easy to display.
5. All pages and news URL addresses are in English
6. The password of the background account is more complicated.
7. Carousel Banner no more than 3
8. The number of plugins does not exceed 20, and the plugins that are not used must be uninstalled to avoid the conflict of plugins and the website is unavailable.
9. The content of the website is king. Please concentrate on the update of the content and the establishment of the knowledge base.
10. Please put large files such as video in other storage.

### WordPress 使用外部图片

当 WordPress 的图片超过 500 张的时候，建议将图片存放到外部对象存储中（OSS），实现图片与主程序分离，加速网站访问。  

1. 通过OSS的客户端工具，上传图片到对象存储

2. 获取对象存储中图片的地址，类似：
   ```
   https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-product-screenshot.png
   ```
3. 登录Wordpress后台，依次打开：页面编辑-插入多媒体，将图片插入到WordPress系统中
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-oss-adresstowp-websoft9.png)

### WordPress integration with OSS

所谓 WordPress 与 对象存储集成实际上就是：将对象存储挂载到 WordPress 的 wp-upload 文件夹上。

挂载 OSS 的操作并不简单，下面**OSS Upload 插件** 为例说明挂载的方法：  


1. 准备对象存储集成所需的：Bucket，读写权限、URL、**Access Key**和**Secret Key**

2. WordPress后台，安装 **OSS Upload** 插件并启用
   
   ![OSS](https://libs.websoft9.com/Websoft9/blog/tmp/wordpress/zh/wordpress-oss-plugin-websoft9.png)
   
3. 对 OSS Upload 插件进行配置，关联将要连接的对象存储
   ![OSS](https://libs.websoft9.com/Websoft9/blog/tmp/wordpress/zh/wordpress-oss-websoft9.png)

4. 设置资源本地备份与同步
  ![OSS](https://libs.websoft9.com/Websoft9/blog/tmp/wordpress/zh/wordpress-oss2-websoft9.png)

### WordPress Multisite

WordPress supports one server, one installation, one database, deploying multiple websites, sharing themes and plugins for multiple websites, and operating the site independently, which is convenient for building and managing a station group system.

1. Initialize WordPress and create a new default website MainSite
   
   [](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-install-websoft9.png)

2. Enable WordPress Multisite
   - Use the SSH tool to connect to the server, modify the MainSite configuration file wp-config.php, and add configuration items:
    ```
    define( 'WP_ALLOW_MULTISITE', true );
    /* That's all, stop editing! Happy blogging. */
    ```

   - Configure the network: Log in WordPress, , go to Tools -> Network Setup -> Install, and enable the multi-site network function

    [](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-network-setup-websoft9.png)

    > If you want to use DNS access, it is recommended to set up DNS access when the main site is installed
    > To access a website through a subdomain, you need to add a * wildcard during DNS resolution, such as *.websoft9.com

3. Modify the configuration: insert the system-generated configuration information into the wp-config.php file, and replace the .htaccess file
   
   [](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-multi-config-websoft9.png

4. Create a new website web1: go to My Sites- > Network Admin -> Sites -> Add New , set the website URL, title, language, etc.
   [](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-add-site-websoft9.png)

5. Multi-site management: re-login to WordPress，  go to My Sites- > Network Admin, you can view the dashboard, multi-site management, theme and plug-in maintenance and other operations
   
   [](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-sites-admin-websoft9.png)

   [](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-sites-admin2-websoft9.png)

### Backup and Restore

There are many WordPress plugins for backup, we recommend [UpdraftPlus WordPress Backup Plugin ](https://wordpress.org/plugins/updraftplus/) 

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-updraftplus-websoft9.png)

UpdraftPlus simplifies backups (and restoration). Backup into the cloud, Dropbox, Google Drive, Rackspace Cloud, DreamObjects, FTP, Openstack Swift, UpdraftPlus Vault and email and restore with a single click. Backups of files and database can have separate schedules. The paid version also backs up to Microsoft OneDrive, Microsoft Azure, Google Cloud Storage, SFTP, SCP, and WebDAV.

* Backup scope: Database,Wordpress
* Backup effect: Very Good
* Backup frequency: Automatic backup per day if you need
* Recommended reason : Automation Backup

### WordPress Upgrade

WordPress Upgrade includes: WordPress core upgrade, Plugin upgrade, Theme upgrade. You can upgrade them by the dashboard of WordPress. Following is the reminder links for WordPress Upgrade

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-upgrade-websoft9.png)

WordPress core, Plugin, Theme are developed by different organization, so their may have the incompatible problem after any upgrade like below

- The website cannot be opened, showing 500 program errors
- Website structure has become confusing
- The topic part feature is not available

The above incompatibility is normal, and the best solution is to adapt the theme and plugin version to the WordPress kernel version.

### Worpress Core upgrade

#### One-click upgrade

When new version for Wordpress Core,you can see the upgrade reminder link, click it to start updates

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-wordpresscoreupdate-websoft9.png)

#### Manual upgrade{#mupgrade}

Sometimes, you can't upgrade WordPress by On-Click for the reason of networ, manual upgrade for you

1. [Download](https://github.com/WordPress/WordPress/tags) a new WordPress version and unzip it
2. Log in to Cloud Server and go to the [WordPress root directory](../wordpress#path)
3. Delete the `wp-admin` and `wp-includes` 
4. Upload local WordPress to Cloud Server, cover all files if have the same file name
5. 重新访问WordPress，可能会出现下图所示的数据库升级步骤
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-update-db-websoft9.jpg)
6. 点击【升级WordPress数据库】即可

### Plugins upgrade

Please update plugin online if you need,e.x
   ![Wordpress plugin upgrade](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-pluginsupgrade-websoft9.png)

### Theme upgrade

Most of the time,you may using the business theme which don't provider online update,below is the suggest steps  

1. Using SFTP to delete the theme from wp-contents folder
2. Log in WordPress, go to Appearance->Theme->Add New, upload the theme online
  ![Wordpress theme upgrade](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-themesupgrade-websoft9.png)
3. Enable the theme when complete the installation

### 代码植入处理{#insertcode}

WordPress 由于被广泛使用，导致安全漏洞被无限放大，其中WordPress网站被植入第三方代码是最常见的安全故障。

* 源码中植入非常明显的代码
* 源码中植入难以察觉的代码
* 数据库中被植入

经过实践，下面介绍一种简单有效的处理办法

1. 通过在线安全检查网站[sitecheck.sucuri.net](https://sitecheck.sucuri.net)进行排查，初步定义被植入的内容
2. 登录WordPress后台，安装安全插件[Wordfence Scan Enabled](https://wordpress.org/plugins/wordfence/)
3. 运行Wordfence Scan Enabled，启动网站健康检查
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-wordfence-websoft9.png)
4. 对于“Critical”标记的结果，手工一一处理

其他扫描工具：

1. Quttera Web Malware Scanner 
2. Anti-Malware Security and Brute-Force Firewall

## Troubleshoot{#troubleshoot}

In addition to the WordPress issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### 配置HTTPS后，网站部分资源无法加载？{#httpsmore}

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

#### HTTPS 访问 “....并非完全安全”？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/https-notallsafe-websoft9.png)

原因是由于 WordPress 网页中含有一部分 HTTP 开头的图片等静态链接资源，需要手工逐一修改

####  出现病毒导致乱码？

由于被广泛使用，导致 WordPress 安全漏洞被无限放大，其中WordPress网站被[植入第三方代码](#insertcode)是最常见的安全故障。 

#### 频繁出现数据库连接错误？

诊断原因：可能性最大的原因是内存不足导致 WordPress 数据库运行异常  
解决方案：增加内存+启用CDN  

> CDN可以在给网站加速的同时，大大降低服务器内存的开销

#### 上传图片出错？

WordPress上传文件出错，有几种可能性： 

1. 图片大小超过服务器限定的要求  
解决方案：请参考本章环境管理-&gt;PHP配置中的修改上传文件大小  

2. 图片实际的格式与后缀不一致。  
解决方案：例如一个 WordPress9.jpg的图片的真实格式是Wordpress9.jpeg，上传的时候会报错，如果把后缀改为jpeg，上传正常。实际上，真实格式与后缀不一致的时候，在Windows系统的文件中也不会有预览效果

3. 权限问题（IIS中比较常见）

#### 正在执行例行维护请一分钟后回来？

出现这个提示的原因是在网站Wordpressinstallation directory下生成了.maintenance文件

* 如果存在将其删除即可,恢复正常. 
* 如果不存在,那么新建一个.maintenance，内容为空白，刷新，恢复正常后再删除它

#### 不能发送邮件？

WordPress 默认是通过mail()函数发送邮件，必须要求服务器本身配置好了邮件功能。  

实际中，将服务器改造成邮件服务器，是一件非常复杂的工作，且难以维护。因此，建议安装一个SMTP插件来解决发送邮件问题：WP-Mail-SMTP

#### 网络不通导致无法升级？

WordPress 升级包地址也是国外的。有时候由于网络原因，升级地址不可用。如果您迫切需要升级，请参考：[WordPress手工升级文档](#mupgrade)

#### 管理员失去权限，无法正常登录后台？

WordPress 的后台管理是分权限的，而最高权限是超级管理员。当wordpress管理员因失去权限无法正常进入后台，可以通过进入PhpMyAdmin数据库管理工具，来进行权限恢复：

* 登录数据库管理工具phpMyAdmin:  http:// 服务器ip/phpMyAdmin/
* 找到跟用户相关的数据表：wp_users和wp_usermeta;
* 先进入wp_users,查看自己的管理员用户名，超级管理员用户id一般都是1，不是就修改；
* 再进入wp_usermeta表，找到wp_user_level，wp_capabilities字段。如果对应账号wp_user_level的值不是10 ，请修改为10（超级管理员一半都是10，最高权   限）；查看wp_capabilities值，如果里面不是 “administrator”，可以直接改成：a:1:{s:13:"administrator";b:1;} ；
* 重新登录。

#### Wordpress 导入演示数据没权限？

错误信息： You don't have permission to access /wp-admin/admin.php on this server?  
解决方案：待研究

## FAQ{#faq}

#### WordPress support multi-language?

Yes

#### WordPress能建企业网站吗？

可以，全球34%的网站都是基于 WordPress 构建

#### If there is no domain name, can I deploy WordPress?

Yes, visit WordPress by *http://Internet IP*

#### How to enable HTTTS for log in WordPress?

Insert these codes below in you `wp-config.php` file

```
### Insert start ###
define('FORCE_SSL_ADMIN', true);
define('FORCE_SSL_LOGIN', true);
### Insert end ###

if ( !defined(‘ABSPATH’) )
        define(‘ABSPATH’, dirname(__FILE__) . ‘/’)
```

#### How to change the permissions of filesytem?

```shell
#WordPress(LAMP)
chown -R apache.apache /data/wwwroot

#WordPress(LNMP)
chown -R nginx.nginx /data/wwwroot

find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```

#### 换回 Classic Editor 经典编辑器？

Wordpress5.0 之后的版本，编辑器与之前有了明显的区别。这里不探讨编辑器孰优孰劣，我们发现编辑器升级之后，用户的主题无法适应新的编辑器，导致做不到可视化编辑。如果您希望主题可以可视化编辑，您必须启用经典编辑器。启用的方法非常简单，安装“Classic Editor”这个插件即可