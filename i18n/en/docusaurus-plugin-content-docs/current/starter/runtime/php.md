---
slug: /php
sidebar_position: 1.4
tags:
  - PHP extension
  - runtime
  - PHP
---

# For PHP App

## Configuration options{#configs}

- Change PHP version: You can change PHP verion by image verion, then need reinstall PHP extensions
- App root directory: */var/www/html*
- user: **www-data**
- php-fpm (×)
- PHP extra configurations: */usr/local/etc/php/conf.d*
- Apache configuration file: */etc/apache2/sites-available/000-default.conf* 
- Get installed php extension: `php -m`
- PHP extension install tool: `install-php-extensions` 
- Install linux software:   `apt update -y && apt install git -y`
- CLI: `composer`, `php`
- Caches: OPcache, XCache, APCU, eAccelerator
- Web framework: Symfony, Laravel, CodeIgniter, Yii

## Deploy a PHP application{#deploy}

Refer to: [App Runtime tutorials](../runtime#quick)

## Manage runtime{#administrator}

### PHP extension installer

[PHP docker image](https://hub.docker.com/_/php) only have PHP core, but deploying apps requires installing system packages and PHP extensions.  

#### Download PHP extension installer {#download-extension-installer}

Below steps for you to download [PHP extension installer](https://github.com/mlocati/docker-php-extension-installer) to your container

1. Login to Websoft9 Console

2. Docker exec to PHP container and run below commands
    ```
    curl -o /usr/local/bin/install-php-extensions -L https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions
    chmod 0755 /usr/local/bin/install-php-extensions
    ```
2. Test `install-php-extensions` command

#### Install php extension by installer

1. Docker exec to your PHP container, run below command

   ```
   install-php-extensions mysqli jd
   ```

2. Test it by `php -m`


#### Install PHP Composer

1. Make sure you have download [PHP extension installer](#download-extension-installer) 

2. Docker exec to PHP container and run below commands to install PHP Composer

    ```
    # Install the latest version
    install-php-extensions @composer

    # Install the latest 1.x version
    install-php-extensions @composer-1
    # Install a specific version
    install-php-extensions @composer-2.0.2
    ```

### Customize PHP Configuration

PHP container have preset directory */usr/local/etc/php/conf.d* for customized PHP configuration file. And Websoft9 have mount a configuration file `src/php_extra.ini` to container.  

There are two ways to modify this customized PHP configuration file:  

- Docker exec to PHP container by Websoft9 Console, and modify it by `vim` (Recommendation)
- Modify `src/php_extra.ini` by Websoft9 Git, and redepoy PHP application


### Other tool to install PHP extensions

This [PHP container](https://hub.docker.com/_/php) support more methods for PHP extension installation: 

- docker-php-ext-install
- pecl install redis-5.3.7; docker-php-ext-enable redis
- Websoft9 PHP runtime scripts
   ```
   # install some OS packages
   curl -sS https://websoft9.github.io/docker-library/apps/php/src/os_packages.sh | bash

   # install some PHP extension
   curl -sS https://websoft9.github.io/docker-library/apps/php/src/php_extension.sh | bash
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

You should modify it at container, below is command sample:  

```
sed -i 's|DocumentRoot /var/www/html|DocumentRoot /var/www/html/laravel/public|' /etc/apache2/sites-available/000-default.conf
```

### Does this runtime support php configuration in .htaccess?

Yes