---
title: WordPress
slug: /wordpress
tags:
  - WordPress
  - CMS
  - Website Building System
  - Blog System
---

import Meta from './\_include/wordpress.md';

<Meta name="meta" />

## Getting Started {#guide}

1. After completing the installation of WordPress via the **Websoft9 Console**, retrieve the application’s **Overview** and **Access** information from **My Apps**.

2. Enter the installation guide and select the language (you can change the language after installation).

3. Set your administrator account, password, and e-mail address.

4. After installation, access the backend (admin dashboard URL: `/wp-admin`).

   ![](./assets/wordpress-backend-websoft9.png)

### Building a Website

Steps to build a website using WordPress:

1. Choose a theme: You can purchase it from the official theme marketplace or a third-party marketplace.
2. Customize the public parts of the website based on the theme: Menu, header, footer, etc.
3. Customize the pages.
4. Add articles and integrate them with the pages.

### Website Statistics {#analysis}

There are two options available for tracking statistics:

- **Third-party web statistics software (recommended)**:

  1. Install the open-source web statistics software **Matomo**.
  2. Install the [WP-Matomo](https://wordpress.org/plugins/wp-piwik/) plugin in WordPress and connect it to the Matomo server.

- **WordPress Plugins**: Use WordPress-specific plugins for basic statistics tracking.

## Best Practices {#best-practices}

### Migrating to Websoft9 Hosting Platform

1. Install a new WordPress instance via the Websoft9 App Marketplace (destination site).
2. Follow one of these migration methods:

#### Migrate using a Plugin (Recommended)

1. Install the [All-in-One WP Migration and Backup](https://wordpress.org/plugins/all-in-one-wp-migration/) plugin on both source and destination sites.
2. Export the complete backup from the source site and download it locally.
3. Import the backup file on the destination site using the same plugin.

#### Manual Migration

1. Transfer the **wp-content** directory from the source to the destination site:
   - **File Copy**: If the source and destination are on different servers, use remote copying to transfer files.
   - **Directory Mount**: If both sites are on the same server, modify the application’s orchestration file and mount `/var/www/html/wp-content`.
2. Update the directory permissions to `www-data`.
3. Export the database using [phpMyAdmin](./phpmyadmin) from the source site and import it into the destination site.
4. Update the database connection details in the destination site's `wp-config.php` file.

### Enabling Object Storage

To improve performance, move media files to an external object storage system:

1. Prepare a third-party object storage service or install [MinIO](./minio).
2. Install the [Media Cloud](https://mediacloud.press/) or OSS Upload plugin in WordPress to connect to the object storage service.

## Three Principles for Maintaining WordPress

1. **Efficiency First**:

   - Images should be optimized (under 100k per image).
   - Offload multimedia files from WordPress to separate storage.
   - Minimize the use of plugins for better performance.

2. **Separation Principle**:

   - Use external services for non-core features like HTTPS setup, object storage, or analytics.

3. **Promotion Priority**:
   - Optimize URLs and image names for SEO.
   - Use an SEO plugin to configure keywords.
   - Maintain a 600:400 aspect ratio for featured images.

## Configuration Options {#configs}

- **Root Directory**: `/var/www/html`
- **Configuration File**: `/var/www/html/wp-config.php`
- **Plugin Directory**: `/var/www/html/wp-content/plugins`
- **Theme Directory**: `/var/www/html/wp-content/themes`
- **Data Folder**: `/var/www/html/wp-content`
- **PHP Configuration File**: `/usr/local/etc/php/conf.d/php_extra.ini`
- **CLI Support (✅)**: `wp --info`, `wp plugin install akismet`
- **[REST API](https://developer.wordpress.org/rest-api/)**:
  ```
  curl -X OPTIONS -i http://yourdomain.com/wp-json/
  curl -X GET -i http://yourdomain.com/wp-json/wp/v2/posts
  curl -X GET -i http://yourdomain.com/wp-json/wp/v2/pages
  ```
- **SMTP (✅)**: Use [WP Mail SMTP by WPForms](https://wordpress.org/plugins/wp-mail-smtp/).
- **E-commerce**: Install the WooCommerce plugin for e-commerce functionality.
- **Multisite (✅)**: Enable multi-site through **Tools > Configure Network** in the WordPress dashboard.

## Administration {#administrator}

- **Change Administrator Email**: If SMTP is not enabled, update the email in the **wp_option** table in the database.
- **Retrieve Password**: Modify the **wp_user** table and change the password for the `admin` user to `21232f297a57a5a743894a0e4a801fc3` (default password: `admin`).
- **Replace Domain URL**: If you cannot access the WordPress dashboard, update the home and site URL values in the **option** table in the database.
- **Scheduled Tasks**: Use [WP Crontrol](https://wordpress.org/plugins/wp-crontrol) to manage scheduled tasks.
- **SSL**: Managed by the Websoft9 gateway. Avoid using WordPress SSL-related plugins.
- **Disable Google Fonts**: If the Disable Google Fonts plugin does not work, manage the issue using the Websoft9 gateway.

## Troubleshooting {#troubleshooting}

#### After configuring HTTPS, some resources are not loading? {#httpsmore}

1. Caused by certain plugins? Check whether the plugin has an HTTPS switch.
2. CDN enabled? Edit the **wp-config.php** file and add the following:

   ```
   define('FORCE_SSL_ADMIN', true);
   define('FORCE_SSL_LOGIN', true);
   $_SERVER['HTTPS'] = 'ON';
   define('CONCATENATE_SCRIPTS', false);
   ```

#### HTTPS access shows “.... Not completely secure”?

Reason: WordPress contains static link resources like images with an HTTP header.  
Solution: Manually modify the affected links.

#### Frequent database connection errors?

Reason: Insufficient memory can cause the WordPress database to fail.  
Solution: Increase memory and enable CDN to reduce server memory usage.

#### Image upload errors?

- **Permissions**: Ensure the **wp-content** folder's permissions are set to `www-data`.
- **Size Limit**: Modify the PHP configuration to allow larger files.
- **Incorrect Format**: Check the image extension and ensure it matches the actual file type.

#### Administrator can’t log in?

Reason: Database permissions are misconfigured.  
Solution: Modify the **wp_user_level** and **wp_capabilities** fields in the **wp_users** and **wp_usermeta** tables.

#### Correct database info but can't connect?

Reason: The containerized version of WordPress does not support database names like `www.abc.com`.  
Solution: Use a different database name format.
