---
sidebar_position: 1
slug: /wordpress
tags:
  - WordPress
  - CMS
  - 建站系统
  - 博客系统
---

# 快速入门

[WordPress](https://wordpress.org) 简称 WP，它是一个企业级开源 CMS（内容管理/建站系统），因易用性、易扩展性（ 插件 、模板、二次开）形成了完美的生态体系。全球互联网上有 34% 的网站都基于 WordPress 构建，它的影响力无与伦比。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-product-screenshot.png)

## 准备

部署 Websoft9 提供的 WordPress 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 WordPress 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  WordPress **[域名五步设置](./administrator/domain_step)** 过程


## WordPress 初始化向导{#init}

### 详细步骤

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*https://域名* 或 *https://服务器公网IP*, 进入安装向导  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wp01.png)

2. 设置您的管理员账号、密码和邮箱， 点击“安装WordPress”; 
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-install004-websoft9.png)

3. 恭喜，成功安装
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-install005-websoft9.png)

4. 进入后台（http//域名或IP/wp-admin），试试 WordPress 的功能 
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-install006-websoft9.png)

5. 开始使用商业主题（部分产品预装）：

   - [Avada 主题](./wordpress/solution#avada)

6. WordPress 和 Minio 可以组合成[【高性能网站方案】](./wordpress/solution#wordpress-minio)

7. WordPress 和 Matomo 可以组合成[【网站统计优化方案】](./wordpress/solution#wordpress-matomo)

> 需要了解更多WordPress的使用，请参考官方文档：[WordPress Documentation](https://wordpress.org/support/)

### 组合应用

如果您安装了 Websoft9 提供的 WordPress 和其他组合应用，请提前获取 **[端口和账号密码](./user/credentials)** ，并完成它们的初始化过程。

被组合的应用以及其参考文档如下：  

* [MinIO 指南](./minio)
* [Matomo 指南](./matomo)

### 免费主题

如果您安装了 Websoft9 提供的 WordPress 免费主题版，请通过下面地址下载:  

* [Avada 主题](https://libs-websoft9-com.oss-accelerate.aliyuncs.com/apps/wordpress/avada/avada.zip),其下插件：[LayerSlider](https://libs-websoft9-com.oss-accelerate.aliyuncs.com/apps/wordpress/avada/LayerSlider.zip)、[fusion-builder](https://libs-websoft9-com.oss-accelerate.aliyuncs.com/apps/wordpress/avada/fusion-builder.zip)、[ fusion-core](https://libs-websoft9-com.oss-accelerate.aliyuncs.com/apps/wordpress/avada/fusion-core..zip)、[revslider](https://libs-websoft9-com.oss-accelerate.aliyuncs.com/apps/wordpress/avada/revslider.zip)
* [Divi 主题](https://libs-websoft9-com.oss-accelerate.aliyuncs.com/apps/wordpress/divi/divi.zip),其下插件：[Divi-Builder-Layouts-147](https://libs-websoft9-com.oss-accelerate.aliyuncs.com/apps/wordpress/divi/Divi-Builder-Layouts-147.zip)
* [Porto 主题](https://libs-websoft9-com.oss-accelerate.aliyuncs.com/apps/wordpress/porto/porto.zip),其下插件：
* [The7 主题](https://libs-websoft9-com.oss-accelerate.aliyuncs.com/apps/wordpress/the7/dt-the7.zip),其下插件：[dt-the7-core](https://libs-websoft9-com.oss-accelerate.aliyuncs.com/apps/wordpress/the7/dt-the7-core.zip)、[go_pricing](https://libs-websoft9-com.oss-accelerate.aliyuncs.com/apps/wordpress/the7/go_pricing.zip)、[js_composer](https://libs-websoft9-com.oss-accelerate.aliyuncs.com/apps/wordpress/the7/js_composer.zip)、[Ultimate_VC_Addons](https://libs-websoft9-com.oss-accelerate.aliyuncs.com/apps/wordpress/the7/Ultimate_VC_Addons.zip)、[revslider](https://libs-websoft9-com.oss-accelerate.aliyuncs.com/apps/wordpress/the7/revslider.zip)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**使用 Avada 等主题，当 WordPress 升级后，页面编辑乱码了**

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/wordpress-avadaeditp-websoft9.png)

**问题原因**： Wordpress升级到5.0版本之后，WordPress 官方提供的默认编辑器发生了本质的变化，导致已有主题无法适应新的 WordPress 编辑器内核  

**解决方案**：安装一个名称为“Classic Editor”的插件，继续使用旧的编辑器内核  

  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/wordpress-classiceditor-websoft9.png)


## WordPress 使用入门

下面以 **[WordPress 使用 Avada 主题建站](./wordpress/solution#avada)** 作为一个任务，帮助用户快速入门。


## WordPress 常用操作

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数
   
2. 登录 WordPress后台-设置-常规，设置好需要用于发件的邮件地址 
   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-mailcg-websoft9.png)
3. 安装SMTP插件：[WP Mail SMTP by WPForms](https://wordpress.org/plugins/wp-mail-smtp/)
   
4. 后台-设置-Email，配置WP Mail SMTTP 插件的参数
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-mailconf-websoft9.png)

5. 填写参数后保存，然后最后输入一个收件地址用于测试是否可用

   - 如果测试成功，会看到”Your email was sent successfully!”
   - 如果邮件配置不可用，则会显示“There was a problem while sending the test email.”

    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-mailss-websoft9.png)

6. SMTP 配置成功后，所有的 WordPress 后台邮件发送就会使用这个配置

### 域名额外配置（修改 URL）{#dns}

**[域名五步设置](./administrator/domain_step)** 完成后，需重置 WordPress URL:

1. 登录 WordPress 后台，依次打开：【设置】>【常规】，将网站路径和安装路径设置为新的域名
   ![Wordpress 修改URL](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-modifyurls-websoft9.png)

2. 保存后生效

> 如果更换域名后，网站中有一部分图片地址还是原来的域名，此时需要手工逐一修正
> 如果在第2步操作完成后，无法进入第3步访问后台操作，请访问 Wordpress 数据库，将 option 表中的 home 和 siteurl 两个属性修改为【新的域名】
> 通过 Websoft9 已经配置好的 MySQL 可视化工具 phpMyAdmin (http://ip/phpmyadmin 或 http://ip:9090 )进行快捷操作

### HTTPS 额外设置{#https}

**[标准 HTTPS 配置](./administrator/domain_https)** 完成后，可能会遇到如下的异常情况：

- [配置HTTPS后，网站部分资源无法加载？](./wordpress/admin#httpsmore)


### 修改上传文件类型

WordPress 默认支持大部分图片等文件格式的上传，但也有一些文件格式是不支持的，根据实际需要，可以增加或禁止一些格式的文件上传。设置方法如下：

把以下代码加到主题目录（```/wp-content/themes/twentysixteen```）下的 functions.php 文件中：
	
   	function edit_upload_types($existing_mimes = array()) {
	// 允许上传的文件类型
	$existing_mimes['woff'] = 'application/woff';
	$existing_mimes['rar'] = 'application/rar';
	
    // 如需添加更多文件类型支持，在其后增加代码即可

	// 不允许上传的的文件类型
	unset( $existing_mimes['jpg'] );

	return $existing_mimes;
	}
	add_filter('upload_mimes', 'edit_upload_types');
    
> 以上是以自带主题 twentysixteen 为例，如果您使用的不是这款主题，则需要到对应主题目录下的 functions.php 文件中添加。

### 增加备案号

如果你使用的WordPress默认自带主题，需要在页面底部增加ICP备案以及链接。具体操作步骤如下：

1. 登录WordPress后台，依次打开【外观】>【小工具】

2. 从左侧的【可用小工具】中拖拽一个【文本】小工具到右侧的【页脚1】

3. 填写好备案号相关信息，增加链接，并分别点击【回车符】按钮和【保存】按钮
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-beian.png)

4. 刷新网页看效果

### 插件管理

插件是WordPress功能的扩展，也是WordPress得以独步天下的“杀手锏”，其插件实现了名副其实的“即插即用”。全球有超过100万的WordPress插件，涵盖电商、表单、邮件、论坛、备份、美化、社交分享、轮播等领域。

##### 寻找插件

寻找所需的插件，有三种方式：

1. 通过WordPress后台-外观-安装插件，在线获取[WordPress插件库](https://wordpress.org/plugins/)的插件 
2. 通过百度、google等搜索“WordPress插件”，淘到自己喜欢的主题
3. 通过插件交易市场购买功能强大的插件，例如：[codecanyon.net](https://codecanyon.net/?osr=tn)

##### 安装插件

安装插件一般有两种方式

1. 通过WordPress后台-插件-安装插件，后台上传插件安装（推荐）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-addplugins-websoft9.png)
2. 通过FTP工具，将主题文件上传到 WordPress 根目录下 */wp-content/plugin*

##### Top20 插件

如下插件在使用 WordPress 中会经常用到：

| 名称 | 类别 | 用途 | 付费 or 免费 |
| :--- | :--- | :--- | :--- |
| WooCommerce | 电商 | 将WordPress扩展成电子商务网站 | 免费 |
| WooCommerce Tab Manager | 电商 | 电商页面Tab扩展 | 免费 |
| UpdraftPlus WordPress Backup Plugin | 备份 | 自动备份WordPress | 免费 |
| Visual Composer: Page Builder for WordPress | 排版与布局 | 客户化编辑器 | 收费 |
| Slider Revolution Responsive WordPress Plugin | 排版与布局 | 强大无比的轮播动画制作与管理 | 收费 |
| Ninja Forms – The Easy and Powerful Forms Builder | 表单 | 表单插件 | 免费 |
| Duplicator – WordPress Migration Plugin | 系统管理 | 网站整体打包工具，拥有备份与迁移 | 免费 |
| All-in-One WP Migration | 系统管理 | 网站整体打包与恢复工具 | 免费 |
| download-monitor | 下载管理 | 下载管理 | 免费 |
| File Manager | 文件管理 | 在线文件管理工具 | 免费 |
| Yoast SEO | SEO | SEO优化建议和按页面设置 | 免费 |
| All in One SEO | SEO | SEO优化建议和按页面设置 | 免费 |
| Remove Google Fonts | 系统管理 | 屏蔽google字体，提升速度 | 免费 |
| WP-Optimize | 系统管理 | 系统优化和瘦身 | 免费 |
| WP Job Manager | 业务应用 | 招聘、职位管理 | 免费 |
| WP Mail SMTP by WPForms | 业务应用 | SMTP邮件发送设置 | 免费 |
| weDocs – the documentation plugin | 业务应用 | 在线文档工具 | 免费 |
| Smartideo | 业务应用 | 优酷等视频插入 | 免费 |
| Essential Grid | 排版与布局 | 文章、页面网格工具 | 免费 |
| Post Grid, List for WordPress – Content Views | 排版与布局 | 文档、页面调用工具 | 免费 |
| Fat Rat Collect | 数据采集 | 批量采集文章数据的开源插件，采集含括微信、简书、知乎、列表详情等 | 免费 |
### 主题管理

WordPress 官方仅提供简单外观的背后有着数十万社区驱动的精美主题：  

1. 方式一：通过WordPress后台-外观-主题-添加，后台上传主题安装（推荐）
2. 方式二：通过FTP工具，将主题文件上传到 */wp-content/theme* 目录下

### WooCommerce 支付配置

WooCommerce 是 WordPress 的一个电子商务插件，在 WordPress 上安装这个插件，就可以将你的 WordPress 改造成电商网站。据说 WooCommerce 已超过上亿次下载，市场占有率领先于同类软件。  

WooCommerce 官方提供了 主题市场和插件市场 以扩展 WooCommerce 的功能。

WooCommerce 默认提供了国外主流的支付插件，下面重点介绍中国本地化支付的两个支付配置

##### 支付宝即时到账支付

1. 申请支付宝商家账户，申请开通即时到账；

2. 在商城中安装支付宝支付插件（如果没有支付宝插件，请通过此处购买）

3. 在商城中配置支付宝参数。配置界面如下：
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/intallalipay-websoft9.png)

##### 微信扫描支付

WooCommerce微信支付插件使用非常简单，只需要如下步骤，就可以让你的WordPress商城添加微信支付功能。

1. 安装微信支付插件（如果没有支付宝插件，请通过此处购买）

2. 获取微信公众号APPID，密钥，微信支付密钥以及微信支付授权目录
   - 获取微信公众号的AppID\(应用ID\) 和AppSecret\(应用密钥\) AppID\(应用ID\) 和AppSecret\(应用密钥\)是微信公众号与第三方网站（wordpress）通信的授权ID和密码，非常重要，必须填写。 请登录微信公众平台（https://mp.weixin.qq.com），点击开发-配置获取：AppID 和AppSecret
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/wechatpay-help001-websoft9.png)
   - 获取微信支付密钥登录微信支付商户平台（https://pay.weixin.qq.com），在账户设置-API安全中找到并设置密钥，密钥为32位，注意一下，获取密钥后保留备用
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/weichatpay-help002-websoft9.png)

3. 添加授权支付目录在微信公众平台（https://mp.weixin.qq.com）点击-微信支付-开发配置，设置授权支付目录 微信支付插件的授权支付目录为：https://你的域名/wp-content/plugins/wechat-weixin-payments-for-woocommerce/
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/weichatpay-help003-websoft9.png)

4. 设置回调域名在微信公众平台（https://mp.weixin.qq.com）-开发-接口权限中找到-网页服务-网页账号修改授权回调页面域名，域名为你的网站域名，注意区分www和不带www；
      ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/weichatpay-help004-websoft9.png)

5. 配置微信支付插件在woocommerce设置，支付设置中找到微信支付设置，填入微信公众号appid和微信支付密钥
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/woocommerce/weichatpay-help005-websoft9.png)

### 管理员密码

实际工作中，我们可能会 **修改** 或 **找回** WordPress 管理员密码

#### 修改密码

1. 以管理员账号登录后台
2. 依次打开：【用户】>【所有用户】，编辑需要修改密码的账号
3. 往下拉倒【账号管理】项，点击【生成密码】，然后修改密码，并更新个人资料 
   ![Wordpress 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-modifypw-websoft9.png)

#### 找回密码

若不记得 WordPress 管理员密码，可以通过如下两个方式找回

方案一：通过邮件找回密码

WordPress可以通过发送邮件找回密码，但前提条件是您的 WordPress 网站已经配置好SMTP
![Wordpress 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-forgetpw-websoft9.png)

方案二：修改数据库中的密码字段

如果不能发邮件，请登录数据库管理面板 phpMyAdmin 进行修改

1. 登录 phpMyAdmin，并找到你的网站数据库下的 *wp_user* 表
   ![Wordpress 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-wpusers-websoft9.png)
2. 编辑管理员用户（下图以用户名 `admin`为例）  
   ![Wordpress 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-wpuserspw-websoft9.png)
3. 截图的地方数据库密码(MD5加密后的密文)，用`21232f297a57a5a743894a0e4a801fc3`替换之
4. 点击【执行】
5. 新的密码为`admin`

## WordPress 参数{#parameter}

WordPress 应用中包含 PHP, Nginx, MariaDB, phpMyAdmin 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 WordPress 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE               COMMAND                  CREATED          STATUS          PORTS                                       NAMES
2fe10a179a6c   phpmyadmin:latest   "/docker-entrypoint.…"   16 seconds ago   Up 16 seconds   0.0.0.0:9090->80/tcp, :::9090->80/tcp       phpmyadmin
d43ecff5608c   wordpress:latest    "docker-entrypoint.s…"   39 seconds ago   Up 38 seconds   0.0.0.0:9001->80/tcp, :::9001->80/tcp       wordpress
9f4aa7ad771b   mariadb:10.4        "docker-entrypoint.s…"   39 seconds ago   Up 38 seconds   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp   wordpress-db
```

下面仅列出 WordPress 本身的参数：

### 路径{#path}

WordPress 安装目录： */data/apps/wordpress*  
WordPress 配置文件： */data/apps/wordpress/data/wordpress/wp-config.php*   
WordPress 数据目录： */data/apps/wordpress/data/mysql_data*   

### 端口{#port}

除 80, 443 等常见端口需开启之外，以下端口可能会用到：

| 端口号 | 用途                                           | 必要性 |
| ------ | ---------------------------------------------- | ------ |
| 9090   | phpmyadmin端口 | 可选   |
| 3306   | Mariadb的数据库端口 | 可选   |

### 版本{#version}

WordPress 控制台点击【升级】即可查看当前版本

### 服务{#service}

```shell
sudo docker start | stop | restart  wordpress
sudo docker start | stop | restart  wordpress-db
sudo docker start | stop | restart  phpmyadmin
```

### 命令行{#cli}

下面通过具体示例展示 wp-cli 的用法：

1. 验证  wp-cli 是否安装成功
  ```
  $ docker exec -it wordpress bash
  $ wp --info
  OS:  Linux 3.10.0-1160.25.1.el7.x86_64 #1 SMP Wed Apr 28 21:49:45 UTC 2021 x86_64
  Shell:  
  PHP binary:  /usr/local/bin/php
  PHP version:  8.0.26
  php.ini used:  
  MySQL binary:  
  MySQL version:  
  SQL modes:  
  WP-CLI root dir:  phar://wp-cli.phar/vendor/wp-cli/wp-cli
  WP-CLI vendor dir:  phar://wp-cli.phar/vendor
  WP_CLI phar path:  /var/www/html
  WP-CLI packages dir:  
  WP-CLI cache dir:  /root/.wp-cli/cache
  WP-CLI global config:  
  WP-CLI project config:.
  ```

2. 如果您尚未完成初始化向导，也可通过 wp-cli 创建新的站点（如已完成初始化向导，可直接使用 wp-cli ）

  ```
  $wp core install --url=http://yourIP --title="WP-CLI" --admin_user=youradmin --admin_password=yourpassword --admin_email=your_email
  Success: WordPress installed successfully.
  ```

3. 通过 wp-cli 安装插件

  ```
  $ wp plugin install akismet
  Warning: akismet: Plugin already installed.
  Success: Plugin already installed. 
  ```

  > 更多用法请参照 [ wp-cli ](https://wp-cli.org/)

### API

[REST API](https://developer.wordpress.org/rest-api/)

WordPress 初始化完成之后，无需任何设置即可调用 API 查看网站相关数据：  

```
curl -X OPTIONS -i http://yourdomain.com/wp-json/
curl -X GET -i http://yourdomain.com/wp-json/wp/v2/posts
curl -X GET -i http://yourdomain.com/wp-json/wp/v2/pages
```


