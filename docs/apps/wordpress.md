---
title: WordPress
slug: /wordpress
tags:
  - WordPress
  - CMS
  - 建站系统
  - 博客系统
---

import Meta from './\_include/wordpress.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initializing {#wizard}

After installing WordPress in the Websoft9 console, you can view the application details through “My Applications” and get the access information in the “Access” tab.

1. Go to the installation wizard and select the language (you can switch the language after installation)

2. Set your administrator account, password and email address

3. After installation, enter the backend (backend address: /wp-admin)
   ! [](. /assets/wordpress-backend-websoft9.png)

### Website Setup Process

The steps to build a website based on WordPress are as follows:

1. Selected themes: can be purchased from the official theme marketplace or third-party theme marketplaces

2. Theme-based customization of the public parts of the site: menu, top, bottom

3. Customize the page

4. Entering articles and integrating articles with pages

### Website Analytics {#analysis}

There are two available options:

- Integration of third-party web statistics software (recommended), the following is an example of use:

  1. Websoft9 App Store installs the open source web statistic software [Matomo](. /matomo)
  2. Wordpress install [WP-Matomo](https://wordpress.org/plugins/wp-piwik/) plugin, and then connect to the Matomo server.

- Using WordPress Website Statistics Related Plugins

## Best Practices

### Migration to Websoft9 hosting platform

Before migrating, first install a new WordPress application through the Websoft9 App Marketplace. This will be referred to as the destination site.

Then, start the migration using one of the following options:

##### Migrate Using a Plugin (Recommended)

1. Install the plug-in: [All-in-One WP Migration and Backup](https://wordpress.org/plugins/all-in-one-wp-migration/) on both the source and destination sites (the free version supports sites smaller than 900M).

2. Export a full backup file from the source site using a plugin and download it to your local machine.

3. Import the backup file into the destination site using a plugin.

##### Manual Migration

If the conditions for plugin migration are not met, manual migration is required:

1. Use one of the following options to migrate the **wp-content** directory from the source site to the destination site:

   - **File copy**: the source and destination are not on the same server, migrate the directory by remote copy.
   - **Directory mount**: The source and destination are on the same server, modify the application's orchestration file, and mount _/var/www/html/wp-content_.

2. Change directory folder permissions to `www-data`.
3. use [phpMyAdmin](. /phpmyadmin) to export the database from the source site and import it to the destination site.
4. fix the database connection information in the **wp-config.php** file of the destination site.

### Enable Object Storage

When the images and media files on your WordPress site start affecting its performance, it is recommended to store the media files in object storage:

1. Prepare a third-party object storage service or install [MinIO](./minio) from the Websoft9 App Store.

2. Install the [Media Cloud](https://mediacloud.press/) or OSS Upload plugin on WordPress, and then connect it to the object storage service.

### Three Principles for Maintaining WordPress

In order to make WordPress run more efficiently, be easier to maintain, and easier to migrate, we summarize three important principles in our practice:

##### Efficiency First

The efficiency of a website is often more important than its aesthetics, so the principle of prioritizing efficiency needs to be followed at all times:

- Images should ideally not exceed 100k per file.
- Separate multimedia files from WordPress.
- Minimize the use of plugins.

##### Separation Principle

For non-business functionality needs, try to avoid plugins and instead use solutions outside of WordPress:

- HTTPS setup: Implement using the Websoft9 gateway.
- Image storage: Integrate object storage.
- Website analytics: Integrate Matomo or other analytics systems.
- Website acceleration: Use CDN.
- Google Fonts disabling: If the plugin doesn’t solve it, consider handling it at the gateway level.

##### Promotion First

The website should be considered for promotion and SEO to realize the return of value:

- Image names, URL addresses in English for easy recognition
- Use SEO plugin to set keywords for the page
- Article image size ratio should be 600:400.

## Configuration options {#configs}

- Root directory (mounted): _/var/www/html_

- Configuration File: _/var/www/html/wp-config.php_

- Plugins directory: _/var/www/html/wp-contents/plugins_

- Theme directory: _/var/www/html/wp-contents/themes_

- Data folder: _/var/www/html/wp-contents_

- php configuration file (mounted): _/usr/local/etc/php/conf.d/php_exra.ini_

- Container user: `www-data`

- CLI (√): `wp --info`, `wp plugin install akismet`

- [REST API](https://developer.wordpress.org/rest-api/)（√）

  ```
  curl -X OPTIONS -i http://yourdomain.com/wp-json/
  curl -X GET -i http://yourdomain.com/wp-json/wp/v2/posts
  curl -X GET -i http://yourdomain.com/wp-json/wp/v2/pages
  ```

- SMTP (√): use [WP Mail SMTP by WPForms](https://wordpress.org/plugins/wp-mail-smtp/)

- E-commerce: Use the WooCommerce plugin to implement e-commerce functionality, support for

- Toggle Classic Editor: use **Classic Editor** plugin

- Third party theme market: [themeforest](https://themeforest.net/)

- Third-party plugin marketplace: [codecanyon.net](https://codecanyon.net/?osr=tn)

- Online upgrade (√)

- Multisite (√): multisite is already allowed by default, via WordPress console **Tools > Configure Networking**

## Administrative maintenance {#administrator}

- **Change administrator mailbox**: If SMTP is not enabled, you need to modify the mailbox information in the database **wp_option** table.

- **Retrieve password**: Modify database **wp_user** table, replace the password text of `admin` user with `21232f297a57a5a743894a0e4a801fc3`, and reset the password to `admin`.

- **Replace domain URL**: If you can't log in to change the URL in the WP console, you can change the home and siteurl fields in the **option** table.

- **Automated Backup and Restore**: We recommend [UpdraftPlus WordPress Backup Plugin](https://wordpress.org/plugins/updraftplus/).

- **Scheduled Tasks**: [WP Crontrol](https://wordpress.org/plugins/wp-crontrol) is recommended.

- **Upgrade**: In addition to upgrading the WordPress kernel, themes and plugins online, if the network is not good, you need to manually upgrade by uploading the source code to a specified location.

- **SSL**: realized by Websoft9 gateway, please don't install any WordPress SSL related plugins.

- **Disable Google Fonts**: Try to install Disable Gooogle Fonts plugin first, if the plugin can't solve the problem, you can deal with it in Websoft9 gateway.

- **Multi-domain support**: Modify the _wp-config.php_ file in the container to avoid the problem of modifying the ROOT_URL after appending a domain name.

  ```
  # Append the following after the define('WP_DEBUG', false) line
  if (true) {
      $http_prefix = (!empty($_SERVER['HTTPS']) && strtolower($_SERVER['HTTPS']) !== 'off') ? 'https://' : 'http://';
      // Multi-domain support
      define('WP_SITEURL', $http_prefix . $_SERVER['HTTP_HOST']);
      define('WP_HOME', $http_prefix . $_SERVER['HTTP_HOST']);
      // Use relative paths for media. If using third-party cloud storage, comment out the following media path.
      define('WP_CONTENT_URL', '/wp-content');
    }

  ```

## Troubleshooting

#### After configuring HTTPS, some website resources fail to load? {#httpsmore}

1. Special plug-ins cause? Some plugins come with HTTPS switch, you need to turn it on or off according to the actual situation.
2. Enabled CDN service? Edit the **wp-config.php** file in the WordPress root directory and add the following code:

   ```
      define('FORCE_SSL_ADMIN', true);
      define('FORCE_SSL_LOGIN', true);
      $_SERVER['HTTPS'] = 'ON';
      define('CONCATENATE_SCRIPTS', false);
   ```

#### HTTPS access '...is not fully secure'?

Reason: WordPress webpage contains some static link resources such as images with HTTP header.  
Solution: You need to manually modify them one by one

#### Frequent database connection errors?

Cause：Insufficient memory is the most common reason for WordPress database errors.  
Solution：Increase memory and enable CDN (CDN can accelerate the website while significantly reducing server memory usage).

#### Error uploading images?

- Multimedia folder permissions: make sure user:usergroup is `www-data`
- Size exceeds the limit: need to modify the PHP configuration file
- Format and suffix inconsistency: pic.jpg is actually pic.jpeg, which prevents uploading, change it to the actual suffix.

#### Administrator unable to log in to the backend?

Issue：The website is accessible, but the administrator cannot log in to the backend.  
Cause：The permission settings in the database have been corrupted.
Solution：Modify the `wp_user_level`, `wp_capabilities`, and other related fields in the `wp_users` and `wp_usermeta` tables.

#### Database information is correct, but unable to connect?

Issue：The database connection information is entirely correct, but a "Database connection error" is still displayed.  
Possible Cause：The containerized version of WordPress does not support database names like `www.abc.com`.
