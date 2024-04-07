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

本环境所采用的 [PHP 原生容器](https://hub.docker.com/_/php) 仅包含 PHP 核心，而安装 PHP 应用时可能需要安装更多系统包和 PHP 扩展。  

所以，掌握安装系统包和 PHP 扩展是必须的工作。  

### PHP 扩展安装管理器（推荐）{#download-extension-installer}

[PHP 扩展安装管理器](https://github.com/mlocati/docker-php-extension-installer)是 Docker 官方推荐的一个命令行工具，它可以很方便的在容器中安装你想要的 PHP 扩展

1. Websoft9 控制台 exec 到容器后，下载 PHP 扩展安装管理器到容器：
    ```
    curl -o /usr/local/bin/install-php-extensions -L https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions
    chmod 0755 /usr/local/bin/install-php-extensions
    ```

2. 安装所需的 PHP 扩展
   ```
   install-php-extensions mysqli jd
   ```

### 安装 PHP Composer

使用 [PHP 扩展安装管理器](#download-extension-installer) 命令，可以很方便的安装所需的 Composer 版本：

    ```
    # Install the latest version
    install-php-extensions @composer

    # Install the latest 1.x version
    install-php-extensions @composer-1
    # Install a specific version
    install-php-extensions @composer-2.0.2
    ```
   

### 其他 PHP 扩展安装方法

本容器还支持[其他扩展安装](https://hub.docker.com/_/php)的命令：

- docker-php-ext-install：内置命令，安装 PHP 扩展时对操作系统包有依赖
- pecl install redis-5.3.7; docker-php-ext-enable redis：内置命令
- Websoft9 提供的一键安装 PHP 扩展脚本（这个脚本中包含了常见的扩展包，适应于许多 PHP 热门应用）
   ```
   # install some OS packages
   curl -sS https://websoft9.github.io/docker-library/apps/php/src/os_packages.sh | bash

   # install some PHP extension
   curl -sS https://websoft9.github.io/docker-library/apps/php/src/php_extension.sh | bash
   ```


### 部署 PHP 网站{#sample}

#### 下载源码部署

以 **Wordpress** 为例，描述应用部署过程：

1. Websoft9 控制台 exec 进入容器后

    - 下载并解压 **Wordpress** 源码到根目录下
      ```
      cd /var/www/html 
      curl -O https://wordpress.org/latest.zip
      unzip latest.zip
      mv wordpress/* ./
      ```
    
    - 修正网站文件权限
      ```
      chown -R www-data:www-data /var/www/html
      ```

2. Websoft9 控制台，通过【我的应用】管理应用，在**访问**标签页中获取 PHP 应用访问链接 URL


3. 本地浏览器后访问 URL，便进入 WordPress 的安装向导

   > 安装过程可能会提示缺少某些 PHP 扩展，此时必须先完成所需的[扩展安装](#download-extension-installer)

#### Composer 部署

确保已经安装 Composer，再以 **Laravel** 为例，描述部署过程：

1. 进入容器 exec 模式，使用 Composer 创建 Laravel 项目，并修正权限

    ```
    composer create-project laravel/laravel /var/www/html/laravel --prefer-dist
    chown -R www-data:www-data /var/www/html/laravel
    ```

2. 配置 Apache 配置文件的 DocumentRoot 指向 */var/www/html/laravel/public*

    ```
    sed -i 's|DocumentRoot /var/www/html|DocumentRoot /var/www/html/laravel/public|' /etc/apache2/sites-available/000-default.conf
    ```

3. 重启容器后，即可正常访问 Laravel


### 修改 PHP 配置文件

PHP 容器通过 */usr/local/etc/php/conf.d* 目录增加自己所需的配置文件，Websoft9 已经将配置文件挂载到容器。  

有两种修改它的方式：

- 在 Websoft9 控制台 exec 到容器，通过 vim 命令修改
- 在 Websoft9 控制台 修改 PHP 应用的编排文件 src/php_extra.ini，重建应用后生效

> 重建应用会删除已经安装的扩展，需慎重使用

## 配置选项{#configs}

- PHP 大版本切换（√）：切换后再根据需要安装所需的扩展
- 多应用支持：一个 PHP 容器仅支持一个应用，多个应用建议运行多个 PHP 容器
- 应用根目录：*/var/www/html*
- PHP 额外配置文件目录：*/usr/local/etc/php/conf.d*
- Apache 配置文件：*/etc/apache2/sites-available/000-default.conf* 
- 查询已安装的 PHP 扩展：`php -m`
- PHP 扩展安装管理器：`install-php-extensions` 
- 容器中安装操作系统包： 以安装 git 为例，安装命令为 `apt update -y && apt install git -y`

## 管理维护{#administrator}

### PHP 版本切换

1. 通过 Websoft9 控制台 PHP 编排文件修改 W9_VERSION

2. 重建容器后生效

3. 进入容器的 exec 模式，使用 [PHP 扩展管理器](#download-extension-installer) 安装所需的 PHP 扩展。  

## 故障

#### PHP7.0 以下 **apt update** 报错？

原因：PHP7.0 以下的容器 Debian 操作系统版本太旧，导致源不可用   

方案：需要重新设定源  

  ```
  sed -i s/deb.debian.org/archive.debian.org/g /etc/apt/sources.list
  sed -i 's|security.debian.org|archive.debian.org|g' /etc/apt/sources.list
  sed -i '/stretch-updates/d' /etc/apt/sources.list
  ```

#### 应用目录没有写权限？

容器中运行 `chown -R www-data:www-data /var/www/html` 修正权限即可