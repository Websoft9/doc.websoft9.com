---
title: WordPress
slug: /wordpress
tags:
  - WordPress
  - CMS
  - Website Building System
  - Blog System
---

import Meta from './_include/wordpress.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of WordPress at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Enter the installation guide, select the language (you can switch the language after installation)

3. Set your administrator account, password and e-mail address

4. After installation, enter the backend (backend address: /wp-admin)  
  ![](./assets/wordpress-backend-websoft9.png)

### The process of building a website

The steps to build a website based on WordPress are as follows:

1. Choose a theme: you can buy it from the official theme marketplace or a third-party theme marketplace

2. Customize the public parts of the website based on the theme: menu, top, bottom

3. Customize the pages

4. Enter articles and integrate them with the pages

### Website statistics {#analysis}

There are two options available:

- Integration of third-party web statistics software (recommended), below is an example of usage:

  1. Install the open source web statistics software Matomo
  2. Wordpress install [WP-Matomo](https://wordpress.org/plugins/wp-piwik/) plugin, and then connect to the Matomo server

- Use WordPress website statistics related plugins

## Best practices

### Migrating to Websoft9 Hosting Platform

Before migrating, install a brand new WordPress application through the Websoft9 App Marketplace, called the destination here  

Then, start the migration using one of the following options:

##### Migrate using a plugin (recommended)

1. Source and destination sites are installed plug-in: [All-in-One WP Migration and Backup](https://wordpress.org/plugins/all-in-one-wp-migration/) (free version supports sites smaller than 900M)

2. The source site export the complete backup file through the plug-in, and download it to local

3. Import the backup file in the destination site through the plugin

##### Manual Migration

If you do not meet the conditions for migrating through the plugin, you need to migrate manually:

1. Use one of the following options to migrate the **wp-content** directory from the source to the destination:

   - **File Copy**: Migrate the directory by remote copy if the source and destination are not on the same server.
   - **Directory mount**: Source and destination are on the same server, modify the orchestration file of the application and mount */var/www/html/wp-content*. 

2. Modify the directory folder permissions to `www-data`
3. use [phpMyAdmin](./phpmyadmin) to export the database from the source site and import it to the destination site
4. fix the database connection information in the **wp-config.php** file of the destination site


### Enable Object Storage

When images and media files of a WordPress website have affected the performance of the website, it is recommended to store the media files in Object Storage:

1. Prepare a third-party object storage service or install [MinIO](./minio)

2. Wordpress install [Media Cloud](https://mediacloud.press/) or OSS Upload plugin and connect to the object storage service

### Three Principles for Maintaining WordPress

In order to make WordPress run more efficiently, be easier to maintain, and easier to migrate, we summarize three important principles in practice:

##### Efficiency First

Efficiency is often more important than beauty, so you should always follow the principle of efficiency first:
- Images should not exceed 100k per image
- Strip multimedia files from WordPress
- Reduce the use of plugins

##### Separation principle

For non-business functionality, try to avoid plugins and use solutions beyond WordPress:

- HTTPS setup: realized using the Websoft9 gateway
- Image storage: integrate object storage
- Website access statistics: integrate Matomo and other statistical systems
- Website acceleration: use CDN
- Google Fonts Disable: when plugins can't solve the problem, consider handling it in the gateway

##### Promotion Priority

The website should be considered for promotion and SEO to realize the return of value:

- Image name, URL address in English for easy recognition
- Use SEO plugin to set keywords for pages
- Article image size ratio should be 600:400

## Configuration options{#configs}

- Root directory (already mounted): */var/www/html*

- Configuration file：*/var/www/html/wp-config.php*

- Plugin Directory: */var/www/html/wp-contents/plugins*

- Theme directory：*/var/ww/html/wp-contents/themes*

- Data folder: */var/www/html/wp-contents*

- Php configuration file (mounted):*/usr/local/etc/php/conf.d/php_exra.ini*

- Container user: `www-data`

- CLI(✅): `wp --info`, `wp plugin install akismet`

- [REST API](https://developer.wordpress.org/rest-api/)（√）
   ```
   curl -X OPTIONS -i http://yourdomain.com/wp-json/
   curl -X GET -i http://yourdomain.com/wp-json/wp/v2/posts
   curl -X GET -i http://yourdomain.com/wp-json/wp/v2/pages
   ```

- SMTP(✅): use [WP Mail SMTP by WPForms](https://wordpress.org/plugins/wp-mail-smtp/) 

- E-commerce: use WooCommerce plugin for e-commerce functionality
- Toggle Classic Editor: use **Classic Editor** plugin

- Third party theme market: [themeforest](https://themeforest.net/)

- Third-party plugin marketplace: [codecanyon.net](https://codecanyon.net/?osr=tn)

- Online upgrade(✅)

- Multisite(✅): multi-site is already allowed by default, through WordPress console **Tools > Configure Network**

## Administer{#administrator}

- **Change administrator mailbox**: If SMTP is not enabled, you need to modify the mailbox information in the database **wp_option** table

- **Retrieve password**: Modify database  table **wp_user**, replace the password of `admin` user with `21232f297a57a5a743894a0e4a801fc3`, and reset the password to `admin`

- **Replace domain URL**: If you can't login to the WP console to change the URL, you can change the home and siteurl in the **option** table

- **Automated Backup and Restore**: We recommend [UpdraftPlus WordPress Backup Plugin](https://wordpress.org/plugins/updraftplus/)

- **Scheduled Tasks**: [WP Crontrol](https://wordpress.org/plugins/wp-crontrol) is recommended

- **Upgrade**: In addition to upgrading the WordPress kernel, themes and plugins online, if the network is not good, you need to manually upgrade by uploading the source code to a specified location

- **SSL**: Realized by Websoft9 gateway, please don't install any WordPress SSL related plugins

- **Disable Google Fonts**: Try to install Disable Gooogle Fonts plugin first, if can't solve the problem, deal with it in Websoft9 gateway

## Troubleshooting{#troubleshooting}


#### After configuring HTTPS, some of the resources on the website are not loading? {#httpsmore}

1. caused by special plug-ins? Some plugins have HTTPS switch, you need to turn it on or off based on the actual situation 
2. CDN service is enabled? Edit the **wp-config.php** file in the WordPress root directory and add the following code

    ```
       define('FORCE_SSL_ADMIN', true);
       define('FORCE_SSL_LOGIN', true);
       $_SERVER['HTTPS'] = 'ON';
       define( 'CONCATENATE_SCRIPTS', false );
    ```

#### HTTPS access to “.... Not completely secure”?

Reason: WordPress webpage contains some static link resources such as images with HTTP header.  
Solution: You need to manually modify them one by one  

#### Frequent database connection error?

Reason: Insufficient memory causes WordPress database to run abnormally, which is the most common problem.   
Solution: Increase memory + enable CDN (CDN can accelerate the website while greatly reducing the server memory overhead)


#### Error uploading image?

- Multimedia folder permissions: Ensure that the user:user group is `www-data`
- Size limit exceeded: Modify the PHP configuration file
- Format and suffix are not consistent: pic.jpg is actually pic.jpeg, it will cause failure to upload, change it to the actual suffix


#### Administrator can't log in the background normally?

Description: The website can be accessed normally, but the administrator cannot login the background normally  
Reason: The permission configuration in the database has been broken
Solution：Modify the fields wp_user_level, wp_capabilities and so on in the wp_users and wp_usermeta tables


#### Database information is correct, but cannot connect?  

Description: The database connection information is correct, but it still shows Database connection error  Reason: The containerized version of WordPress does not support the database name www.abc.com  

