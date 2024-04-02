---
title: PHP
slug: /php
tags:
  - 运行环境
  - runtime
  - PHP
---

import Meta from './_include/php.md';

<Meta name="meta" />

## 入门指南{#guide}

### PHP 环境配置{#environment}

前提：进入容器并安装工具 **wget**

1. 安装系统依赖包

  ```
  wget https://websoft9.github.io/docker-library/apps/php/src/os_packages.sh && bash os_packages.sh
  ```

2. 安装 PHP 扩展包

  ```
  wget https://websoft9.github.io/docker-library/apps/php/src/php_extension.sh && bash php_extension.sh
  ```

3. PHP 其他配置文件设置

  ```
  wget https://websoft9.github.io/docker-library/apps/php/src/php_extra.ini -O /usr/local/etc/php/conf.d/php_extra.ini
  wget https://websoft9.github.io/docker-library/apps/php/src/opcache_recommended.ini -O /usr/local/etc/php/conf.d/opcache_recommended.ini
  ```

4. 退出后重启容器安装包即可生效

### 安装应用{#install}

#### 二进制包安装

下面通过常见的 PHP 应用 **Wordpress**为例，描述应用安装过程：

1. 进入容器准备 **Wordpress** 源码

  ```
  cd /var/www/html 
  wget https://wordpress.org/latest.zip
  unzip latest.zip
  mv wordpress/* ./
  ```

2. Websoft9 控制台安装 MySQL

3. Websoft9 控制台，通过【我的应用】管理应用，在**访问**标签页中获取 PHP 应用登录信息

4. 使用本地浏览器后访问 URL，根据初始化向导输入步骤2中的数据库信息，wordpress即可初始化完成

#### composer 安装

下面通过常见的 PHP 应用 **Laravel**为例，描述安装过程：

1. 进入容器，安装 composer
  ```
  curl -sS https://getcomposer.org/installer -o composer-setup.php
  php composer-setup.php --install-dir=/usr/local/bin --filename=composer
  ```

2. 使用 Composer 创建 Laravel 项目

  ```
  composer create-project laravel/laravel /var/www/html/laravel --prefer-dist
  ```

3. 配置 Apache，修改 **/etc/apache2/sites-available/000-default.conf**，DocumentRoot 指向 Laravel 项目的 public 目录

  ```
  DocumentRoot /var/www/html/laravel/public
  ```

4. 设置文件权限
  ```
  chown -R www-data:www-data /var/www/html/laravel
  chmod -R 755 /var/www/html/laravel/storage
  chmod -R 755 /var/www/html/laravel/bootstrap/cache
  ```

5. 重启容器，即可正常访问 Laravel


## 配置选项{#configs}

- 配置文件: opcache_recommended.ini，php_extra.ini
  >容器内路径：**/usr/local/etc/php/conf.d**


## 管理维护{#administrator}


## 故障

#### PHP7.0以下 **apt update** 报错？

因为 PHP7.0以下的容器 Debian 操作系统版本太老，需要重新设定源，执行下面命令可恢复更新：

```
sed -i s/deb.debian.org/archive.debian.org/g /etc/apt/sources.list
sed -i 's|security.debian.org|archive.debian.org|g' /etc/apt/sources.list
sed -i '/stretch-updates/d' /etc/apt/sources.list
```