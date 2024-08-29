---
title: WordPress
slug: /wordpress
tags:
  - WordPress
  - CMS
  - 建站系统
  - 博客系统
---

import Meta from './_include/wordpress.md';

<Meta name="meta" />


## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 WordPress 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取访问信息。  

1. 进入安装向导，选择语言（可安装后切换语言）

2. 设置您的管理员账号、密码和邮箱

3. 安装后，进入后台（后台地址：/wp-admin）
  ![](./assets/wordpress-backend-websoft9.png)

### 建站流程

基于 WordPress 建站的步骤如下：

1. 选用主题：可从官方主题市场或第三方主题市场购买

2. 基于主题定制网站的公共部分：菜单、顶部、底部

3. 定制页面

4. 录入文章，并将文章与页面集成

### 网站统计{#analysis}

有两种可选的方案：

- 集成第三方网站统计软件（推荐），下面是使用范例：

  1. Websoft9 应用商店安装开源网站统计软件 [Matomo](./matomo)
  2. Wordpress 安装 [WP-Matomo](https://wordpress.org/plugins/wp-piwik/) 插件，然后连接 Matomo 服务端

- 使用 WordPress 网站统计相关的插件

## 最佳实践

### 迁移至 Websoft9 托管平台

在迁移之前，先通过 Websoft9 应用市场，安装一个全新的 WordPress 应用，此处称之为目的站。  

然后，采用以下的方案之一开始迁移：

##### 使用插件迁移（推荐）

1. 源站和目的站均安装插件：[All-in-One WP Migration and Backup](https://wordpress.org/plugins/all-in-one-wp-migration/)（免费版支持小于 900M 的网站）

3. 源站中通过插件导出完整的备份文件，并下载到本地

4. 目的站中通过插件导入备份文件

##### 手工迁移

如果不符合通过插件迁移的条件，需要手工迁移：

1. 采用下面的方案之一，将源站的 **wp-content** 目录迁移至目的站：

   - **文件拷贝**：源站与目的站在不属于同一台服务器，通过远程拷贝的方式迁移目录
   - **目录挂载**：源站与目的站在同一台服务器上，修改应用的编排文件，挂载 */var/www/html/wp-content* 

2. 修正目录文件夹权限为 `www-data`
3. 使用 [phpMyAdmin](./phpmyadmin) 等可视化工具从源站导出数据库，再导入到目的站
4. 修正目的站的 **wp-config.php** 文件中的数据库连接信息


### 启用对象存储

当 WordPress 网站的图片和媒体文件已经影响网站的性能时，建议将媒体文件存储到对象存储中：

1. 准备好第三方对象存储服务或 Websoft9 应用商店安装 [MinIO](./minio)

2. Wordpress 安装 [Media Cloud](https://mediacloud.press/) 或 OSS Upload插件，然后连接到对象存储服务

###  维护 WordPress 的三大原则

为了使 WordPress 运行更有效率，方便维护、方便迁移，我们在实践中总结三个重要原则：

##### 效率优先

网站的访问效率往往比美观度更重要，因此需时刻遵循效率优先的原则：

- 图片尽量不超过 100k/张
- 多媒体文件从 WordPress 中剥离
- 减少插件的使用

##### 分离原则

非业务功能需求，尽量避免使用插件，而是采用 WordPress 之外的解决方案：

- HTTPS 设置：使用 Websoft9 网关实现
- 图片存储：集成对象存储
- 网站访问统计：集成 Matomo 等统计系统
- 网站加速：使用 CDN
- Google 字体禁用：插件无法解决时，考虑在网关中处理

##### 推广优先

网站要考虑推广和 SEO，实现价值回报：

- 图片名称、URL 地址采用英文，便于识别
- 使用 SEO 插件设置页面的关键词
- 文章图片大小比例最好为600:400


## 配置选项{#configs}

- 根目录（已挂载）：*/var/www/html*

- 配置文件：*/var/www/html/wp-config.php*

- 插件目录：*/var/www/html/wp-contents/plugins*

- 主题目录：*/var/www/html/wp-contents/themes*

- 数据文件夹：*/var/www/html/wp-contents*

- php 配置文件（已挂载）：*/usr/local/etc/php/conf.d/php_exra.ini*

- 容器用户：`www-data`

- CLI（√）：`wp --info`, `wp plugin install akismet`

- [REST API](https://developer.wordpress.org/rest-api/)（√）
   ```
   curl -X OPTIONS -i http://yourdomain.com/wp-json/
   curl -X GET -i http://yourdomain.com/wp-json/wp/v2/posts
   curl -X GET -i http://yourdomain.com/wp-json/wp/v2/pages
   ```

- SMTP（√）：使用 [WP Mail SMTP by WPForms](https://wordpress.org/plugins/wp-mail-smtp/) 

- 电商：使用 WooCommerce 插件实现电商功能，支持

- 切换经典编辑器：使用 **Classic Editor** 插件

- 第三方主题市场：[themeforest](https://themeforest.net/)

- 第三方插件市场：[codecanyon.net](https://codecanyon.net/?osr=tn)

- 在线升级（√）

- 多站点（√）：默认已允许多站点，通过 WordPress 控制台 **工具 > 配置网络** 实现

## 管理维护{#administrator}

- **更改管理员邮箱**：如果未启用 SMTP，需修改数据库 **wp_option** 表中的邮箱信息

- **找回密码**：修改数据库 **wp_user** 表，将 `admin` 用户的密码文替换为 `21232f297a57a5a743894a0e4a801fc3`，密码重置为 `admin`

- **更换域名 URL**：但 WP 控制台无法登陆修改 URL 时，可修改 **option** 表的 home 和 siteurl 字段实现

- **自动化备份与恢复**：建议使用 [UpdraftPlus WordPress Backup Plugin ](https://wordpress.org/plugins/updraftplus/)

- **计划任务**：建议使用 [WP Crontrol](https://wordpress.org/plugins/wp-crontrol)

- **升级**：除在线升级 WordPress 内核、主题和插件之外，网络不好的情况下，需通过上传源码的方式到指定位置，实现手工升级

- **SSL**：通过 Websoft9 网关实现，请勿安装任何 WordPress SSL 相关插件

- **禁用 Google 字体**：先尝试安装 Disable Gooogle Fonts 插件，如果插件无法解决问题，可以在 Websoft9 网关中处理

- **支持多域名**：修改容器内 *wp-config.php* 文件可避免追加域名后修改 ROOT_URL 的问题

    ```
    # 在 define('WP_DEBUG', false)行后追加如下内容
    if (true) {
      $http_prefix = (!empty($_SERVER['HTTPS']) && strtolower($_SERVER['HTTPS']) !== 'off') ? 'https://' : 'http://';
      //多域名支持
      define('WP_SITEURL', $http_prefix . $_SERVER['HTTP_HOST']);
      define('WP_HOME', $http_prefix . $_SERVER['HTTP_HOST']);
      //媒体路径使用相对路径 如果使用第三方云储存 将下面这段附件路径地址注释即可
      define('WP_CONTENT_URL', '/wp-content');
    }

    ```

## 故障


#### 配置HTTPS后，网站部分资源无法加载？{#httpsmore}

1. 特殊插件导致？ 某些插件自带 HTTPS 开关，需要根据实际情况开启或关闭。 
2. 开了 CDN 服务？ 编辑 WordPress 根目录下的 **wp-config.php** 文件，增加如下代码

    ```
       define('FORCE_SSL_ADMIN', true);
       define('FORCE_SSL_LOGIN', true);
       $_SERVER['HTTPS'] = 'ON';
       define( 'CONCATENATE_SCRIPTS', false );
    ```

#### HTTPS 访问 “....并非完全安全”？

原因：WordPress 网页中含有一部分 HTTP 开头的图片等静态链接资  
方案：需要手工逐一修改  

#### 频繁出现数据库连接错误？

问题原因：内存不足导致 WordPress 数据库运行异常是最常见的   
解决方案：增加内存+启用CDN（CDN可以在给网站加速的同时，大大降低服务器内存的开销）


#### 上传图片出错？

- 多媒体文件夹权限：需确保用户:用户组为 `www-data`
- 大小超过限制：需修改 PHP 配置文件
- 格式与后缀不一致：pic.jpg 实际上是 pic.jpeg，就会导致无法上传，修改为实际后缀名即可


#### 管理员无法正常登录后台？

问题描述：网站可以正常访问，管理员无法正常登录后台  
原因分析：数据库中权限配置被破坏
解决方案：修改 wp_users 和 wp_usermeta 表中与权限有关的字段 wp_user_level, wp_capabilities 等


#### 数据库信息无误，但无法连接？  

问题描述：数据库连接信息完全正确，但仍然显示 Database connection error    
可能原因：容器版 WordPress 不支持 www.abc.com 这种数据库名称  
