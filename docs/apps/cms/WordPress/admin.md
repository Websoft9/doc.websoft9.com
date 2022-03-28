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

## 场景

### 备份与恢复

WordPress插件库中有数量众多的备份插件，我们推荐使用：[UpdraftPlus WordPress Backup Plugin ](https://wordpress.org/plugins/updraftplus/)

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-updraftplus-websoft9.png)

这个插件特点和好处包括：

* 可以预设备份时间点，实现自动备份
* 可以备份网站文件和数据库
* 可以实现一键恢复

### 升级

WordPress 升级包括：WordPress 内核升级、插件升级和主题升级。这三者都可以通过 WordPress 后台进行在线升级，下图是升级提醒：  
![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-upgrade-websoft9.png)

由于这三者分别属于不同的开发者，升级后可能会导致不兼容的现象。具体表现有：

- 网站打不开，显示500程序错误
- 网站结构变得混乱
- 主题部分功能不可用

以上不兼容现象是正常的，最好的解决办法是让 主题和插件的版本 适应 WordPress 内核版本。

#### 内核升级

##### 一键升级

WordPress 内核升级非常简单，当进入后台之后系统会提示需要升级，点击升级即可（ 特别注意：Wordpress应用程序升级之前务必进行完整备份，以保证备份出现差错之后能够复原。）

 ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-wordpresscoreupdate-websoft9.png)

##### 手动升级

有的时候，由于网络原因，在线一键升级不可用，那么就需要手工升级

1. [下载](https://github.com/WordPress/WordPress/tags)最新的 WordPress 版本，并解压
2. 登录云服务器，进入 [WordPress 的根目录](/zh/stack-components.html#wordpress路径)
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

## 故障速查

####  WordPress 出现病毒导致乱码？

由于被广泛使用，导致安全漏洞被无限放大，其中WordPress网站被[植入第三方代码](././administrator/security/emergency#insertcode)是最常见的安全故障。 

#### WordPress 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```

#### WordPress运行中，频繁出现数据库连接错误？

诊断原因：可能性最大的原因是内存不足导致数据库运行异常
解决方案：增加内存+启用CDN

> CDN可以在给网站加速的同时，大大降低服务器内存的开销

#### WordPress上传图片出错？

WordPress上传文件出错，有几种可能性：  
1. 图片大小超过服务器限定的要求  
解决方案：请参考本章环境管理-&gt;PHP配置中的修改上传文件大小  
2. 图片实际的格式与后缀不一致。  
解决方案：例如一个 WordPress9.jpg的图片的真实格式是Wordpress9.jpeg，上传的时候会报错，如果把后缀改为jpeg，上传正常。实际上，真实格式与后缀不一致的时候，在Windows系统的文件中也不会有预览效果
3. 权限问题（IIS中比较常见）

#### WordPress出现解决正在执行例行维护请一分钟后回来

出现这个提示的原因是在网站Wordpress安装目录下生成了.maintenance文件

* 如果存在将其删除即可,恢复正常. 
* 如果不存在,那么新建一个.maintenance，内容为空白，刷新，恢复正常后再删除它

#### WordPress不能发送邮件的原因

WordPress默认是通过mail\(\)函数发送邮件，必须要求服务器本身配置好了邮件功能。实际中，将服务器改造成邮件服务器，是一件非常复杂的工作，且难以维护。因此，建议安装一个SMTP插件来解决发送邮件问题：WP-Mail-SMTP

#### WordPress 5.0 换回老版”Classic Editor”经典编辑器

Wordpress5.0之后的版本，编辑器与之前有了明显的区别。这里不探讨编辑器孰优孰劣，我们发现编辑器升级之后，用户的主题无法适应新的编辑器，导致做不到可视化编辑。如果您希望主题可以可视化编辑，您必须启用经典编辑器。启用的方法非常简单，安装“Classic Editor”这个插件即可

#### WordPress 后台升级网络不通，官网也打不开？

WordPress是国外的网站，后台升级地址也是国外的，如果网站打不开，后台升级同样就无法进行。如果您迫切需要升级，请参考我们的[WordPress手工升级文档](/zh/solution-upgrade.md#手动升级)

#### WordPress 管理员失去权限，无法正常登录后台？

WordPress的后台管理是分权限的，而最高权限是超级管理员。当wordpress管理员因失去权限无法正常进入后台，可以通过进入PhpMyAdmin数据库管理工具，来进行权限恢复：
* 登录数据库管理工具phpMyAdmin:  http:// 服务器ip/phpMyAdmin/
* 找到跟用户相关的数据表：wp_users和wp_usermeta;
* 先进入wp_users,查看自己的管理员用户名，超级管理员用户id一般都是1，不是就修改；
* 再进入wp_usermeta表，找到wp_user_level，wp_capabilities字段。如果对应账号wp_user_level的值不是10 ，请修改为10（超级管理员一半都是10，最高权   限）；查看wp_capabilities值，如果里面不是 “administrator”，可以直接改成：a:1:{s:13:"administrator";b:1;} ；
* 重新登录。

#### Wordpress导入一个演示数据显示 You don't have permission to access /wp-admin/admin.php on this server?

待研究


## 问题解答

#### WordPress支持多语言吗？

支持多语言（包含中文），后台可以设置语言

#### WordPress能建企业网站吗？

可以，全球34%的网站都是基于 WordPress 构建

#### WordPress(LAMP)，WordPress(LNMP)等商品括号中的 LAMP,LNMP 是什么意思？

LAMP和LNMP代表支持WordPress运行所对应的基础环境，具体参考[环境说明](./runtime/php)

#### 是否可以使用云平台的 RDS 作为 WordPress 的数据库？

可以，修改 WordPress 根目录下的配置文件 `wp-config.php` 即可

#### WordPress能在Windows服务器上运行吗？

可以，但是我们推荐在运行 WordPress 效率更高的 Linux 服务器上运行

#### WordPress数据库连接配置信息在哪里？

数据库配置信息在WordPress安装目录下的 *wp-config.php* 中，[查阅安装目录路径](../wordpress#path)

#### 如果没有域名是否可以部署 WordPress？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`（Linux） 或 服务器桌面（Windows）

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP/phpmyadmin

#### 如何禁止phpMyAdmin访问？

连接服务器，编辑 phpMyAdmin 配置文件，将其中的 Require all granted 更改为 Require ip 192.160.1.0，然后重启 Apache 服务

#### 是否可以修改WordPress的源码路径？

可以，通过修改 [虚拟主机配置文件](../apache#virtualHost)中相关参数

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
