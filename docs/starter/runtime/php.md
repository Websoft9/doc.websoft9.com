---
title: PHP
slug: /php
sidebar_position: 1.4
tags:
  - 运行环境
  - runtime
  - PHP
---


Websoft9 将 Docker 官方的 [php](https://hub.docker.com/_/php) 镜像以模板化的方式，集成到 Websoft9 控制台，实现自动化的部署和发布 PHP 应用程序。   

主要的功能包括：

- 100% 可视化操作
- 配置文件和应用程序数据持久化
- 提供了 **PHP + Apache(mod-php)** 和 **PHP-FPM + NGINX** 两个可选的运行环境
- 支持 Dockerfile 编写和自动构建、运行
- 预制容器启动后运行的脚本 cmd.sh，便于用户实现自动化部署
- 支持 php 模块以及 apt 包的申明式安装
- [phar](https://www.php.net/manual/zh/intro.phar.php) 包支持
- 支持的缓存扩展：OPcache, XCache, APCU, eAccelerator
- 框架：Symfony, Laravel, CodeIgniter, Yii 等
- 应用：WordPress, Joomla, Drupal 等
- 支持 PHP 多版本切换

## 配置选项{#configs}

### 配置文件路径和修改{#modify-configs}

PHP 程序环境对应的主要路径与配置文件一览表如下：

  | 项                 | 容器内路径                                      | 挂载路径                               |
  | ------------------ | ----------------------------------------------- | -------------------------------------- |
  | **应用根目录**        | */var/www/html*                                 | 名称为 `source` 的 Docker 卷           |
  | **自动化脚本文件**     | */usr/local/bin/cmd.sh*                         | 应用 Git 仓库下 `src/cmd.sh`           |
  | **PHP 配置文件**       | */usr/local/etc/php/conf.d/php_extra.ini*       | 应用 Git 仓库下 `src/php_extra.ini     |
  | **扩展申明式配置文件** | Dockerfile 构建时解析配置并安装包               | 应用 Git 仓库下 `src/extensions.ini    |
  | **Apache 配置文件**    | */etc/apache2/sites-available/000-default.conf* | 应用 Git 仓库下 `src/000-default.conf* |
  | **NGINX 配置文件**     | */etc/nginx/sites-available/default*            | 应用 Git 仓库下 `src/nginx.conf`       |
  | **NGINX 配置目录**     | */etc/nginx/conf.d*                             | 名称为 `nginx_conf` 的 Docker 卷       |
  | **PHP-FPM 配置文件**   | */usr/local/etc/php-fpm.d*/fpm_extra.conf       | 应用 Git 仓库下 `src/fpm_extra.conf    |

  - 挂载到应用 Git 仓库下的配置文件，请选择一种配置方式：

    - 在 Websoft9 控制台通过 **编排** 操作进行修改，重建应用后**持久生效**
    - 在 Websoft9 控制台 exec 到容器，通过 vim 命令修改可**临时生效**，重建应用后会丢失配置

  - 挂载到 Docker 卷的配置项目，请在对应的目录中增加配置文件，重启应用后持久生效
  

### 其他配置说明

- **应用目录用户**：**www-data**
- **PHP 大版本切换（√）**：切换后需重建容器，并根据需要重新安装 PHP 扩展
- **多应用支持**：一个 PHP 容器仅支持一个应用，多个应用建议运行多个 PHP 容器
- **php-fpm 和 mod-php 容器可选**
- **命令行**：
  - `php`：PHP 标准命令，例如 `php -m` 查看已安装的 PHP 扩展
  - `composer`：PHP 包管理器命令
  - `install-php-extensions`：安装 PHP 扩展的命令行，它支持[数百种 php 包](https://github.com/mlocati/docker-php-extension-installer?tab=readme-ov-file#supported-php-extensions)，首选推荐它
  - `docker-php-ext-install`, `pecl`：其他包管理工具

## 部署网站{#deploy}

参考：[Web Runtime 入门指南](./runtime)

## 环境管理{#administrator}

### 数据持久化

由于 Websoft9 PHP Runtime 是基于 Docker 容器，故用户需要特别注意数据的持久化问题：

- 所有的配置均以声明式的方式存放到 PHP 应用的对应的 Git 仓库中，虽然它们是持久化的，但需重建应用才可将更改在容器中生效
- 通过修改 `cmd.sh` 脚本实现自动化部署时，用户需编写应用重建时数据可迁移的程序段

### 安装 PHP 扩展

Websoft9 提供了申明式安装 PHP 扩展以及操作系统包的功能，大大简化用户安装包的困扰：

1. 登录 Websoft9 控制台，对正在运行的 PHP 容器应用进行 **编排** 操作

2. 修改 `src/extensions.ini` 文件，根据扩展安装方式，向其中增加所需的扩展名称

   - install-php-extensions：这是 Websoft9首选推荐的方式。先[查询支持的 php 包名](https://github.com/mlocati/docker-php-extension-installer?tab=readme-ov-file#supported-php-extensions) ，然后将包名称增加到此配置项中

   - docker-php-ext-install 和 pecl 两种包安装方式，请参考 [php 官方镜像](https://hub.docker.com/_/php) 的使用方法。

3. 重建应用后生成新的镜像，并基于新镜像启动容器

4. 运行 `php -m` 查看扩展的安装情况


> 也可以 docker exec 到 php 容器后，运行 `install-php-extensions mysqli jd` 命令直接安装扩展。但是，容器重建后扩展会丢失。  


## 问题与故障

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

#### 应用根目录可更换吗？

修改 Apache 配置文件中的 **DocumentRoot** 项，即可更换目录。但是新的目录必须是 */var/www/html* 的子目录，例如：*/var/www/html/laravel/public*

#### 支持应用 .htaccess 中修改 php.ini？

支持

#### PHP 扩展为何对操作系统有依赖？

PHP 的扩展（extension）这里应称为“模块（module）”是 C、C++ 编写的功能合集，扩展大多以动态链接 .dll、.so 形式加载。php扩展是php核心并不支持的功能，然后可以通过扩展的方式进行扩展PHP的功能，常见的扩展如MySQL，gb2等等。

#### 如何引入 PHP 包？

包则是直接引入通过 require/include 方式加载