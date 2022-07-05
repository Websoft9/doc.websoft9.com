---
sidebar_position: 3
slug: /wordpress/admin
tags:
  - WordPress
  - CMS
  - 建站系统
  - 博客系统
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### WordPress 维护 10 大原则

为了使 WordPress 运行更有效率，方便维护、方便迁移，我们在实践中总结了需要注意的 10 个要点：

1. 上传图片尽量不超过100k/张
2. 如果总图片数量超过500张，建议将图片放到对象存储中，实现动静分离，也便于维护
3. 所有图片名称为英文
4. 新闻的图片大小比例最好为600:400，保证统一性。每篇新闻都要配套图片，美观大方，便于展示
5. 所有页面、新闻 URL 地址均采用英文
6. 后台账号的密码要复杂一些
7. 轮播 Banner 不超过3张
8. 插件数量不超过20个，不用的插件务必卸载，以避免插件冲突而导致网站不可用
9. 网站内容为王，请将精力集中于内容的更新、知识库的建立
10. 视频等大文件请放到其他存储中

### WordPress 使用外部图片

当 WordPress 的图片超过 500 张的时候，建议将图片存放到外部对象存储中（OSS），实现图片与主程序分离，加速网站访问。  

1. 通过OSS的客户端工具，上传图片到对象存储

2. 获取对象存储中图片的地址，类似：
   ```
   https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-product-screenshot.png
   ```
3. 登录Wordpress后台，依次打开：页面编辑-插入多媒体，将图片插入到WordPress系统中
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-oss-adresstowp-websoft9.png)

### WordPress 多站点
WordPress 支持一台服务器，一次安装，一个数据库，部署多个网站，多个网站共享主题、插件，站点单独操作，方便构建和管理站群系统。
1. 初始化 WordPress ，新建默认网站 MainSite 
   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-install-websoft9.png)

2. 启用 WordPress 多站点
   - 使用 SSH 工具连接服务器，修改 MainSite 配置文件 wp-config.php，添加配置项：
    ```
    define( 'WP_ALLOW_MULTISITE', true );
    /* That's all, stop editing! Happy blogging. */
    ```

   - 配置网络： 登录 WordPress 后台，通过【工具】-【站点网络配置】，点击【安装】,启用多站点网络功能

    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-network-setup-websoft9.png)

    > 如需用域名访问，建议在主站安装时就设置好域名访问
    > 通过子域名访问网站，需要在域名解析时添加 * 通配符，如 *.websoft9.com

3. 修改配置，使 WordPress 支持多站点：将系统生成的配置信息分别插入到 wp-config.php 文件，及替换 .htaccess文件
   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-multi-config-websoft9.png)

4. 新建网站 web1 ：【我的站点】-【管理网站】-【站点】-【添加新站点】，设置网站URL、标题、语言等。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-add-site-websoft9.png)

5. 多站点管理：重新登录后台，通过【我的站点】-【管理网站】，可以进行查看仪表盘、多网站管理、主题及插件维护等操作
   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-sites-admin-websoft9.png)

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-sites-admin2-websoft9.png)


### WordPress 集成对象存储

所谓 WordPress 与 对象存储集成实际上就是：将对象存储挂载到 WordPress 的 wp-upload 文件夹上。

挂载 OSS 的操作并不简单，下面**OSS Upload 插件** 为例说明挂载的方法：  


1. 准备对象存储集成所需的：Bucket，读写权限、URL、**Access Key**和**Secret Key**

2. WordPress后台，安装 **OSS Upload** 插件并启用
   
   ![OSS](https://libs.websoft9.com/Websoft9/blog/tmp/wordpress/zh/wordpress-oss-plugin-websoft9.png)
   
3. 对 OSS Upload 插件进行配置，关联将要连接的对象存储
   ![OSS](https://libs.websoft9.com/Websoft9/blog/tmp/wordpress/zh/wordpress-oss-websoft9.png)

4. 设置资源本地备份与同步
  ![OSS](https://libs.websoft9.com/Websoft9/blog/tmp/wordpress/zh/wordpress-oss2-websoft9.png)

### 备份与恢复

WordPress插件库中有数量众多的备份插件，我们推荐使用：[UpdraftPlus WordPress Backup Plugin ](https://wordpress.org/plugins/updraftplus/)

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-updraftplus-websoft9.png)

这个插件特点和好处包括：

* 可以预设备份时间点，实现自动备份
* 可以备份网站文件和数据库
* 可以实现一键恢复

### 升级

升级之前必须备份，这个是基本素养。  

WordPress 升级包括：内核升级、插件升级和主题升级。这三者都可以通过 WordPress 后台进行在线升级，下图是升级提醒：  

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-upgrade-websoft9.png)

由于这三者分别属于不同的开发者，升级后可能会导致不兼容的现象。具体表现有：

- 网站打不开，显示500程序错误
- 网站结构变得混乱
- 主题部分功能不可用

以上不兼容现象是正常的，最好的解决办法是让 主题和插件的版本 适应 WordPress 内核版本。

#### 内核升级

##### 一键升级

WordPress 内核升级非常简单，当进入后台之后系统会提示需要升级，点击升级即可。

 ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-wordpresscoreupdate-websoft9.png)

##### 手动升级{#mupgrade}

有的时候，由于网络原因，在线一键升级不可用，那么就需要手工升级

1. [下载](https://github.com/WordPress/WordPress/tags)最新的 WordPress 版本，并解压
2. 登录云服务器，进入 [WordPress 的根目录](../wordpress#path)
3. 删除此目录下的 `wp-admin` 和 `wp-includes` 文件夹
4. 上传本地解压后的 WordPress代码，有同名文件提醒的时候选择覆盖上传
5. 重新访问WordPress，可能会出现下图所示的数据库升级步骤
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-update-db-websoft9.jpg)
6. 点击【升级WordPress数据库】即可

#### 插件升级

插件一般采用在线升级的方式，并逐一升级  

 ![WordPress 插件升级](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-pluginupdate-websoft9.png)

#### 主题升级

主题升级建议采用的方式：

1. 使用 WinSCP 登录服务，删除原有主题（或对其改名）
2. 通过 【WordPress 后台】>【外观】>【主题】>【添加】>【上传主题】的方式，完成主题安装
   ![Wordpress 上传主题](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-addthemes-websoft9.png)


### 代码植入处理{#insertcode}

WordPress 由于被广泛使用，导致安全漏洞被无限放大，其中WordPress网站被植入第三方代码是最常见的安全故障。

* 源码中植入非常明显的代码
* 源码中植入难以察觉的代码
* 数据库中被植入

经过实践，下面介绍一种简单有效的处理办法

1. 通过在线安全检查网站[sitecheck.sucuri.net](https://sitecheck.sucuri.net)进行排查，初步定义被植入的内容
2. 登录WordPress后台，安装安全插件[Wordfence Scan Enabled](https://wordpress.org/plugins/wordfence/)
3. 运行Wordfence Scan Enabled，启动网站健康检查
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-wordfence-websoft9.png)
4. 对于“Critical”标记的结果，手工一一处理

其他扫描工具：

1. Quttera Web Malware Scanner 
2. Anti-Malware Security and Brute-Force Firewall  

## 故障排除

#### 配置HTTPS后，网站部分资源无法加载？{#httpsmore}

在完成 https 的配置后，可能会出现网站无法加载 css 等静态文件，特别是是对于经过二次开发过的 WordPress 会更为常见。

问题原因及对策

1. 特殊插件导致？ 某些插件自带 HTTPS 开关，需要根据实际情况开启或关闭。 
2. 开了 CDN 服务？ 编辑 WordPress 根目录下的 **wp-config.php** 文件，增加如下代码

    ```
       define('FORCE_SSL_ADMIN', true);
       define('FORCE_SSL_LOGIN', true);
       $_SERVER['HTTPS'] = 'ON';
       define( 'CONCATENATE_SCRIPTS', false );
    ```

#### HTTPS 访问 “....并非完全安全”？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/https-notallsafe-websoft9.png)

原因是由于 WordPress 网页中含有一部分 HTTP 开头的图片等静态链接资源，需要手工逐一修改

####  出现病毒导致乱码？

由于被广泛使用，导致 WordPress 安全漏洞被无限放大，其中WordPress网站被[植入第三方代码](#insertcode)是最常见的安全故障。 

#### 频繁出现数据库连接错误？

诊断原因：可能性最大的原因是内存不足导致 WordPress 数据库运行异常  
解决方案：增加内存+启用CDN  

> CDN可以在给网站加速的同时，大大降低服务器内存的开销

#### 上传图片出错？

WordPress上传文件出错，有几种可能性： 

1. 图片大小超过服务器限定的要求  
解决方案：请参考本章环境管理-&gt;PHP配置中的修改上传文件大小  

2. 图片实际的格式与后缀不一致。  
解决方案：例如一个 WordPress9.jpg的图片的真实格式是Wordpress9.jpeg，上传的时候会报错，如果把后缀改为jpeg，上传正常。实际上，真实格式与后缀不一致的时候，在Windows系统的文件中也不会有预览效果

3. 权限问题（IIS中比较常见）

#### 正在执行例行维护请一分钟后回来？

出现这个提示的原因是在网站Wordpress安装目录下生成了.maintenance文件

* 如果存在将其删除即可,恢复正常. 
* 如果不存在,那么新建一个.maintenance，内容为空白，刷新，恢复正常后再删除它

#### 不能发送邮件？

WordPress 默认是通过mail()函数发送邮件，必须要求服务器本身配置好了邮件功能。  

实际中，将服务器改造成邮件服务器，是一件非常复杂的工作，且难以维护。因此，建议安装一个SMTP插件来解决发送邮件问题：WP-Mail-SMTP

#### 网络不通导致无法升级？

WordPress 升级包地址也是国外的。有时候由于网络原因，升级地址不可用。如果您迫切需要升级，请参考：[WordPress手工升级文档](#mupgrade)

#### 管理员失去权限，无法正常登录后台？

WordPress 的后台管理是分权限的，而最高权限是超级管理员。当wordpress管理员因失去权限无法正常进入后台，可以通过进入PhpMyAdmin数据库管理工具，来进行权限恢复：

* 登录数据库管理工具phpMyAdmin:  http:// 服务器ip/phpMyAdmin/
* 找到跟用户相关的数据表：wp_users和wp_usermeta;
* 先进入wp_users,查看自己的管理员用户名，超级管理员用户id一般都是1，不是就修改；
* 再进入wp_usermeta表，找到wp_user_level，wp_capabilities字段。如果对应账号wp_user_level的值不是10 ，请修改为10（超级管理员一半都是10，最高权   限）；查看wp_capabilities值，如果里面不是 “administrator”，可以直接改成：a:1:{s:13:"administrator";b:1;} ；
* 重新登录。

#### Wordpress 导入演示数据没权限？

错误信息： You don't have permission to access /wp-admin/admin.php on this server?  
解决方案：待研究


## 问题解答

#### WordPress支持多语言吗？

支持多语言（包含中文），后台可以设置语言

#### WordPress能建企业网站吗？

可以，全球34%的网站都是基于 WordPress 构建

#### 如果没有域名是否可以部署 WordPress？

可以，访问`http://服务器公网IP` 即可

#### WordPress 登录后台如何使用 SSL？

在 wp-config.php 文件中的特定位置，添加如下两行代码

```
### 添加代码开始 ###
define('FORCE_SSL_ADMIN', true);
define('FORCE_SSL_LOGIN', true);
### 添加代码结束 ###

if ( !defined(‘ABSPATH’) )
        define(‘ABSPATH’, dirname(__FILE__) . ‘/’)
```

#### 如何修改上传的文件权限?

```shell
#WordPress(LAMP)
chown -R apache.apache /data/wwwroot

#WordPress(LNMP)
chown -R nginx.nginx /data/wwwroot

find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```

#### 换回 Classic Editor 经典编辑器？

Wordpress5.0 之后的版本，编辑器与之前有了明显的区别。这里不探讨编辑器孰优孰劣，我们发现编辑器升级之后，用户的主题无法适应新的编辑器，导致做不到可视化编辑。如果您希望主题可以可视化编辑，您必须启用经典编辑器。启用的方法非常简单，安装“Classic Editor”这个插件即可