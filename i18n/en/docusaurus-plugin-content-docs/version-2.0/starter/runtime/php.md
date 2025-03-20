---
slug: /php
sidebar_position: 1.4
tags:
  - PHP extension
  - runtime
  - PHP
---

# For PHP Apps

Websoft9 integrated [PHP official docker image](https://hub.docker.com/_/php) to Websoft9 Console for PHP application deployment and pulish.  

The features below:  

- 100% Web-based GUI
- Persistent storage for Apps data and configuration files
- Three deployment templates: **PHP + Apache(mod-php)** 、**PHP-FPM + NGINX** 和 **PHP-FPM + Apache** for user selections
- Dockerfile editor and build
- Built-in `cmd.sh` for deployment automation and individualized deployment Process
- Declarative installation of php modules and apt packages
- [phar](https://www.php.net/manual/zh/intro.phar.php) supported
- Cache extentsions: OPcache, XCache, APCU, eAccelerator
- PHP framework supported: Symfony, Laravel, CodeIgniter, Yii and so on
- PHP application supported: WordPress, Joomla, Drupal, Moodle and so on
- Multiple versions of PHP supported
- Selectable Databases 

## PHP Configs{#configs}

### Configs path{#modify-configs}

The main paths and configuration files for the PHP program environment are listed below:

  | Item                 | Path in container                                      | Mount path of host machine                              |
  | ------------------ | ----------------------------------------------- | -------------------------------------- |
  | **App root path**        | */var/www/html*                                 | Docker volume named `source`    |
  | **Automation script for personalized deployment**     | */usr/local/bin/cmd.sh*                         | App Git repository path `src/cmd.sh`           |
  | **PHP configuration file**       | */usr/local/etc/php/conf.d/php_extra.ini*       | App Git repository path `src/php_extra.ini`     |
  | **Extended declarative profile** | It for Dockerfile build               | App Git repository path `src/extensions.ini`    |
  | **Apache vhost file**    | */etc/apache2/sites-available/000-default.conf* | App Git repository path `src/000-default.conf` |
  | **NGINX vhost file**     | */etc/nginx/sites-available/default*            | App Git repository path `src/nginx.conf`       |
  | **NGINX extra configs directory**     | */etc/nginx/conf.d*                             | Docker volume named `nginx_conf` |
  | **PHP-FPM config file**   | */usr/local/etc/php-fpm.d*/fpm_extra.conf       | App Git repository path `src/fpm_extra.conf`    |

  - **For Git repository configs**, you can set it by below methods:

    - **For permanent settings**: **My Apps > Application Management > Compose** of your PHP
    - **For temp settings**: Modify it by `vim` at PHP container by docker exec

  - **For Docker volume configs**, you can modify the files directly and restart the PHP container to take effect
  

### Configs reference

- **user:group**: `www-data:www-data`
- **PHP major version changed(√)**: You should reinstall PHP modules after change PHP major version, then migrate your applications
- **Multiple Apps**: Not recommended, suggest one application at one PHP container
- **PHP server**: php-fpm or mod-php for your selections
- **Commands**：
  - `php`: php cli, e.g `php -m` to list all installed modules
  - `composer`: PHP packages management tools
  - `install-php-extensions`: Top recommended PHP extension install command, it supported[100+ PHP extensions](https://github.com/mlocati/docker-php-extension-installer?tab=readme-ov-file#supported-php-extensions)
  - `docker-php-ext-install`, `pecl`: Other PHP packages management tool

## Deploy a PHP application{#deploy}

Refer to: [App Runtime tutorials](./runtime)

## Manage runtime{#administrator}

### Persistent your data

Since the Websoft9 PHP Runtime is based on a Docker container, you need to know the data persistence:

- All configurations are stored declaratively in the PHP application's corresponding Git repository, and although they are persistent, you need to rebuild the application for the changes to take effect in the container.

- When automating deployment by modifying the `cmd.sh` script, you will need to write segments that migrate data when the application is rebuilt.

### Install PHP extensions
 
Websoft9 provides declarative installation of PHP extensions and operating system packages, simplifying installation of packages:

1. Login to **Websoft9 Console**, open the **My Apps > Application Management > Compose** of your PHP

2. Modify the file `src/extensions.ini` and add your PHP extension names to it

   - **install-php-extensions**: Top recommended PHP extension command, and you can [get the package names](https://github.com/mlocati/docker-php-extension-installer?tab=readme-ov-file#supported-php-extensions) first and then add it to `extensions.ini` file

   - **docker-php-ext-install** and  **pecl** php extension command, please read the usage of [php official image docs](https://hub.docker.com/_/php) 

3. Generate a new image after rebuilding the application and start the container based on the new image

4. You can check new modules by `php -m` in your container

> You can run command `install-php-extensions mysqli jd` at your container directly, but it not a persistent method

### Command samples

```
# Install the latest version
install-php-extensions mysqli jd
install-php-extensions @composer

# Install the latest 1.x version
install-php-extensions @composer-1

# Install a specific version
install-php-extensions @composer-2.0.2

# pecl install extensions
pecl install redis-5.3.7; docker-php-ext-enable redis
```

## Troubleshoot

### apt update error in PHP7.0?

The apt repository url is unreachable, you should reset it by below commands:  

  ```
  sed -i s/deb.debian.org/archive.debian.org/g /etc/apt/sources.list
  sed -i 's|security.debian.org|archive.debian.org|g' /etc/apt/sources.list
  sed -i '/stretch-updates/d' /etc/apt/sources.list
  ```

### Permission problem of root directory?

Run command `chown -R www-data:www-data /var/www/html` in your PHP container

### How to modify Apache configurations?

You can modify **DocumentRoot** item at container. But it must the sub directory of */var/www/html*, e.g */var/www/html/laravel/public*

### Does this runtime support php configuration in .htaccess?

Yes