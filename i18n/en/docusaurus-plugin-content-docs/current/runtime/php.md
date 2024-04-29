---
title: PHP
slug: /php
tags:
  - 运行环境
  - runtime
  - PHP
---

import Meta from '../apps/_include/php.md';

<Meta name="meta" />

## 配置选项{#configs}

- PHP 大版本切换（√）：切换后需重建容器，并根据需要重新安装 PHP 扩展
- 多应用支持：一个 PHP 容器仅支持一个应用，多个应用建议运行多个 PHP 容器
- 应用根目录：*/var/www/html*
- PHP 额外配置文件目录：*/usr/local/etc/php/conf.d*
- Apache 配置文件：*/etc/apache2/sites-available/000-default.conf* 
- 查询已安装的 PHP 扩展：`php -m`
- PHP 扩展安装管理器：`install-php-extensions` 
- 容器中安装操作系统包： 以安装 git 为例，安装命令为 `apt update -y && apt install git -y`
- 命令行：`composer`, `php`
- [phar](https://www.php.net/manual/zh/intro.phar.php) 包支持（？）
- 支持的缓存扩展：OPcache, XCache, APCU, eAccelerator

## PHP 扩展管理器

[PHP 原生容器](https://hub.docker.com/_/php) 仅包含 PHP 核心，而部署应用可能需要额外安装 PHP 扩展包，故掌握安装系统包和 PHP 扩展是必须的工作。  

### 下载扩展管理器{#download-extension-installer}

下载 Docker 官方推荐的 [PHP 扩展安装管理器](https://github.com/mlocati/docker-php-extension-installer) 到容器，实现安装和管理扩展。

1. Websoft9 控制台进入容器的命令模式后，下载 PHP 扩展安装管理器到容器：
    ```
    curl -o /usr/local/bin/install-php-extensions -L https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions
    chmod 0755 /usr/local/bin/install-php-extensions
    ```
2. 测试 install-php-extensions 可用性

### 安装所需的 PHP 扩展

1. Websoft9 控制台进入容器的命令模式后，安装所需的扩展

   ```
   install-php-extensions mysqli jd
   ```

2. 运行 `php -m` 查看扩展的安装情况


### 安装 PHP Composer

1. 确保已经下载 [PHP 扩展安装管理器](#download-extension-installer) 

2. Websoft9 控制台进入容器的命令模式后，安装所需的 Composer

    ```
    # Install the latest version
    install-php-extensions @composer

    # Install the latest 1.x version
    install-php-extensions @composer-1
    # Install a specific version
    install-php-extensions @composer-2.0.2
    ```

## 部署 PHP 网站{#sample}

### 下载源码部署

以 **Wordpress** 为例，描述应用部署过程：

1. Websoft9 控制台 exec 进入容器后
    ```
    # 下载并解压 **Wordpress** 源码到根目录下
    cd /var/www/html 
    curl -O https://wordpress.org/latest.zip
    unzip latest.zip
    mv wordpress/* ./

    # 修正网站文件权限
    chown -R www-data:www-data /var/www/html
    ```

2. Websoft9 控制台，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取 PHP 应用访问链接 URL


3. 本地浏览器后访问 URL，便进入 WordPress 的安装向导

   > 安装过程可能会提示缺少某些 PHP 扩展，此时必须先完成所需的[扩展安装](#download-extension-installer)

### Composer 部署

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



## 管理维护{#administrator}

### 修改 PHP 配置文件

PHP 容器通过 */usr/local/etc/php/conf.d* 目录增加自己所需的配置文件，Websoft9 已经将配置文件挂载到容器。  

有两种修改它的方式：

- 在 Websoft9 控制台 exec 到容器，通过 vim 命令修改
- 在 Websoft9 控制台 修改 PHP 应用的编排文件 src/php_extra.ini，重建应用后生效

> 重建应用会删除已经安装的扩展，需慎重使用

### PHP 版本切换

1. 通过 Websoft9 控制台 PHP 编排文件修改 W9_VERSION

2. 重建容器后生效

3. 进入容器的 exec 模式，使用 [PHP 扩展管理器](#download-extension-installer) 安装所需的 PHP 扩展。  

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

## 故障

#### PHP 7.0 以下 **apt update** 报错？

原因：PHP7.0 以下的容器 Debian 操作系统版本太旧，导致源不可用   

方案：需要重新设定源  

  ```
  sed -i s/deb.debian.org/archive.debian.org/g /etc/apt/sources.list
  sed -i 's|security.debian.org|archive.debian.org|g' /etc/apt/sources.list
  sed -i '/stretch-updates/d' /etc/apt/sources.list
  ```

#### 应用目录没有写权限？

容器中运行 `chown -R www-data:www-data /var/www/html` 修正权限即可

#### 如何修改 Apache 配置？

建议在容器中运行命令修改 Apache 配置，下面是范例：

```
sed -i 's|DocumentRoot /var/www/html|DocumentRoot /var/www/html/laravel/public|' /etc/apache2/sites-available/000-default.conf
```

#### 什么是 PHP-FPM？

PHP-FPM 用于管理 PHP 进程池，接受 Apache/Nginx 等 Web 服务器的请求。PHP-FPM 提供了更好的 PHP 进程管理方式，可以有效控制内存和进程、可以平滑重载 PHP 配置。

#### 推荐流行的 PHP 框架？

- Symfony
- Laravel
- CodeIgniter
- Yii

#### 支持应用 .htaccess 中修改 php.ini？

支持

#### PHP 不支持 SMTP？

PHP 与 SMTP 相关的问题

1.  需要了解你所使用的STMP功能是否调用了PHP软件包（或扩展类）

   	* php官方提供的mail()类，这个类不支持SMTP验证
    * php扩展包-[PHPMailer](https://github.com/PHPMailer/PHPMailer)，这个类功能比较全面

2.  php_openss 版本过低或者没有安装，php_openssl 的 CA 证书缺失或异常

#### PHP 扩展为何对操作系统有依赖？

PHP 的扩展（extension）这里应称为“模块（module）”是 C、C++ 编写的功能合集，扩展大多以动态链接 .dll、.so 形式加载。php扩展是php核心并不支持的功能，然后可以通过扩展的方式进行扩展PHP的功能，常见的扩展如MySQL，gb2等等。

#### 如何引入 PHP 包？

包则是直接引入通过 require/include 方式加载