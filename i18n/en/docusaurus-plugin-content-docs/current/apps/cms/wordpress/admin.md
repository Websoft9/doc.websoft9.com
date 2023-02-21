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

### WordPress use external images

When there are more than 500 pictures in WordPress, it is recommended to store the pictures in external object storage (OSS) to separate the pictures from the main program and speed up website access.

1. Upload images to Object Storage through OSS client tools

2. Get the address of the image in the object store, similar to:
   ```
   https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-product-screenshot.png
   ```
3. Log in to the WordPress background and open: Page Editing - Insert Multimedia, Insert Pictures into the WordPress System
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-oss-adresstowp-websoft9.png)

### WordPress integration with OSS

The so-called WordPress and object storage integration is actually: mount the object storage to the wp-upload folder of WordPress.
The operation of mounting OSS is not simple. The following **OSS Upload plugin** is an example to illustrate the mounting method:

1. Required to prepare object storage integration: Bucket, read and write permissions, URL, **Access Key** and **Secret Key**

2. WordPress in the background, install the **OSS Upload** plugin and enable it
   
   ![OSS](https://libs.websoft9.com/Websoft9/blog/tmp/wordpress/zh/wordpress-oss-plugin-websoft9.png)
   
3. Configure the OSS Upload plugin to associate the object storage to be connected
   ![OSS](https://libs.websoft9.com/Websoft9/blog/tmp/wordpress/zh/wordpress-oss-websoft9.png)

4. Set up resource local backup and synchronization
  ![OSS](https://libs.websoft9.com/Websoft9/blog/tmp/wordpress/zh/wordpress-oss2-websoft9.png)

### WordPress Multisite

WordPress supports one server, one installation, one database, deploying multiple websites, sharing themes and plugins for multiple websites, and operating the site independently, which is convenient for building and managing a station group system.

1. Initialize WordPress and create a new default website MainSite
   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-install-websoft9.png)

2. Enable WordPress Multisite
   - Use the SSH tool to connect to the server, modify the MainSite configuration file wp-config.php, and add configuration items:
    ```
    define( 'WP_ALLOW_MULTISITE', true );
    /* That's all, stop editing! Happy blogging. */
    ```
    
   - Configure the network: Log in WordPress, , go to Tools -> Network Setup -> Install, and enable the multi-site network function

    ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-network-setup-websoft9.png)

    > If you want to use DNS access, it is recommended to set up DNS access when the main site is installed
    > To access a website through a subdomain, you need to add a wildcard during DNS resolution, such as *.websoft9.com*

3. Modify the configuration: insert the system-generated configuration information into the wp-config.php file, and replace the .htaccess file
   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-multi-config-websoft9.png)

4. Create a new website web1: go to My Sites- > Network Admin -> Sites -> Add New , set the website URL, title, language, etc.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-add-site-websoft9.png)

5. Multi-site management: re-login to WordPress，  go to My Sites- > Network Admin, you can view the dashboard, multi-site management, theme and plug-in maintenance and other operations
   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-sites-admin-websoft9.png)

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
5. Revisit WordPress, the database upgrade steps shown in the image below may appear
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-update-db-websoft9.png)
6. Click [Upgrade WordPress Database]

### Plugins upgrade

Please update plugin online if you need,e.x
   ![Wordpress plugin upgrade](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-pluginsupgrade-websoft9.png)

### Theme upgrade

Most of the time,you may using the business theme which don't provider online update,below is the suggest steps  

1. Using SFTP to delete the theme from wp-contents folder
2. Log in WordPress, go to Appearance->Theme->Add New, upload the theme online
  ![Wordpress theme upgrade](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-themesupgrade-websoft9.png)
3. Enable the theme when complete the installation

### Code implantation{#insertcode}

WordPress due to its widespread use, security vulnerabilities are infinitely magnified, among which WordPress sites are implanted with third-party code is the most common security failure.

* Implant very obvious code in the source code
* Imperceptible code is embedded in the source code
* implanted in the database

After practice, the following introduces a simple and effective treatment method

1. Check website through online security[sitecheck.sucuri.net](https://sitecheck.sucuri.net) conduct an investigation to initially define the implanted content
2. Log in to the WordPress backend and install the security plugin[Wordfence Scan Enabled](https://wordpress.org/plugins/wordfence/)
3. Run Wordfence Scan Enabled, start the website health check
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-wordfence-websoft9.png)
4. For the results marked "Critical", manually process them one by one

Other scanning tools:

1. Quttera Web Malware Scanner 
2. Anti-Malware Security and Brute-Force Firewall

## Troubleshoot{#troubleshoot}

In addition to the WordPress issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### After configuring HTTPS, some resources of the website cannot be loaded?{#httpsmore}

After completing the configuration of https, it may happen that the website cannot load static files such as css, especially for WordPress that has undergone secondary development.

Causes of problems and countermeasures:

1. Caused by special plugins? Some plugins come with an HTTPS switch, which needs to be turned on or off according to the actual situation.
2. Do you have CDN service enabled? Edit the **wp-config.php** file in the WordPress root directory and add the following code

    ```
       define('FORCE_SSL_ADMIN', true);
       define('FORCE_SSL_LOGIN', true);
       $_SERVER['HTTPS'] = 'ON';
       define( 'CONCATENATE_SCRIPTS', false );
    ```

#### HTTPS access "....not completely secure"?

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/https-notallsafe-websoft9.png)

The reason is that the WordPress web page contains some static link resources such as images starting with HTTP, which need to be manually modified one by one

####  Viruses cause garbled characters?

Due to its widespread use, WordPress security vulnerabilities are infinitely magnified, with WordPress sites being [inserted with third-party code](#insertcode) the most common security failure.

#### Frequent database connection errors?

Diagnosing the cause: The most likely cause is insufficient memory causing the WordPress database to behave abnormally
Solution: increase memory + enable CDN

> CDN can greatly reduce the overhead of server memory while accelerating the website

#### Error uploading pictures?

There are several possibilities for the WordPress upload file error:

1. The image size exceeds the server limit
Solution: Please refer to this chapter Environment Management -> Modifying the Upload File Size in PHP Configuration

2. The actual format of the picture is inconsistent with the suffix.
Solution: For example, the real format of a WordPress9.jpg image is WordPress9.jpeg, and an error will be reported when uploading. If the suffix is ​​changed to jpeg, the upload will be normal. In fact, when the real format is inconsistent with the suffix, there will be no preview effect in the file of the Windows system.

3. Permission issues (common in IIS)

#### Performing routine maintenance. Please come back in a minute?

The reason for this prompt is that the .maintenance file is generated under the Wordpressinstallation directory of the website

* If it exists, delete it and return to normal.
* If it does not exist, then create a new .maintenance, the content is blank, refresh, and then delete it after returning to normal

#### Can't send mail?

By default, WordPress sends emails through the mail() function, and the server itself must be configured with the mail function.

In practice, transforming the server into a mail server is a very complicated task and difficult to maintain. Therefore, it is recommended to install an SMTP plugin to solve the problem of sending mail: WP-Mail-SMTP

#### Unable to upgrade due to network failure?

The WordPress upgrade package address is also abroad. Sometimes due to network reasons, the upgrade address is not available. If you urgently need to upgrade, please refer to: [WordPress manual upgrade documentation](#mupgrade)

#### The administrator has lost his authority and cannot log in to the background normally?

The background management of WordPress is divided into permissions, and the highest authority is the super administrator. When the wordpress administrator cannot enter the background normally due to losing permissions, he can restore the permissions by entering the PhpMyAdmin database management tool:

* Log in to the database management tool phpMyAdmin: http://server ip/phpMyAdmin/
* Find data tables related to users: wp_users and wp_usermeta;
* First enter wp_users, check your own administrator user name, the super administrator user id is generally 1, if not, modify it;
* Enter the wp_usermeta table again and find the wp_user_level, wp_capabilities fields. If the value of the corresponding account wp_user_level is not 10, please change it to 10 (half of the super administrators are 10, the highest authority); check the wp_capabilities value, if it is not "administrator", you can directly change it to: a:1:{s:13 :"administrator";b:1;};
* re-register.

#### Wordpress does not have permission to import demo data?

Error message: You don't have permission to access /wp-admin/admin.php on this server?
Solution: To be studied

## FAQ{#faq}

#### WordPress support multi-language?

Yes

#### Can WordPress build a corporate website?

Yes, 34% of the world's websites are built on WordPress

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

#### Switching back to Classic Editor Classic Editor?

After Wordpress5.0, the editor is obviously different from before. We do not discuss the advantages and disadvantages of the editor here. We found that after the editor is upgraded, the user's theme cannot adapt to the new editor, resulting in visual editing. If you want the theme to be editable visually, you must enable the classic editor. The method of enabling is very simple, just install the "Classic Editor" plugin
