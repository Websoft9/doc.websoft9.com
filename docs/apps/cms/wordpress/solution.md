---
sidebar_position: 2
slug: /wordpress/solution
tags:
  - WordPress
  - CMS
  - 建站系统
  - 博客系统
---

# 场景方案

WordPress 可以与其他的软件平台**集成**一起使用，解决 构建内容管理 过程中的各种[场景问题](#)。

## WordPress 集成 MinIO 高性能场景方案{#wordpress-minio}

WordPress [集成MinIO](https://benlobaugh.medium.com/build-highly-performant-wordpress-sites-with-minio-and-wp-offload-media-dadc7bb25371) 集成的关键过程如下：

1. WordPress 启用  WP Offload Media 插件
2. WordPress 设置配置文件wp-config.php中 MinIO 相关设置

## WordPress 集成 Matomo 网站优化场景方案{#wordpress-matomo}

WordPress [集成Matomo](https://wordpress.org/plugins/wp-piwik/#installation) 集成的关键过程如下：

1. WordPress 启用 WP-Matomo(WP-Piwik) 插件
2. 在WP-Matomo (WP-Piwik) 设置菜单按照说明配置您的 Matomo 连接即可

## WordPress 与 Discuz 双应用{#wordpress-discuz}

WordPress&Discuz 预装包部署后，浏览器访问：*https://服务器公网ip/9panel* 开始安装向导。

**注意**：应用是否通过域名访问，对应的安装步骤不同，请选择合适的方案：

### 方式一：通过IP访问

如果不打算使用域名访问网站，而是通过IP地址访问网站，安装非常简单：

* WordPress安装入口：*https://服务器公网IP*，进入 [WordPress 安装向导](../wordpress#init)
* Discuz安装入口：*https://服务器公网IP/discuz*，进入 [Discuz 安装向导](../discuz#init))

### 方式二：共用一个域名访问

共用一个域名（假设域名为www.abc.com），类似：

* *https://www.abc.com*   访问 WordPress
* *https://www.abc.com/discuz*   访问 Discuz

这种情况下的安装步骤如下：

1. 登录到域名管理面板，完成解析域名，确保域名解析成功
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/domain-websoft9.png)

2. 分别完成安装向导
   - 本地浏览器访问：*https://www.abc.com*   开始 [WordPress 安装向导](../wordpress#init)
   - 本地浏览器访问：*https://www.abc.com/discuz*   进入 [Discuz 安装向导](../discuz#init))

### 方式三：分别配置域名

给 WordPress 和 Discuz 分别配置不同的域名，例如：

* *https://wordpress.abc.com*  配置给 WordPress
* *https://discuz.abc.com*    配置给 Discuz

此场景下对应的安装步骤如下：

1. 确保域名解析成功

3. 通过 WinSCP 连接服务器，进入*/etc/httpd/conf.d*目录，修改域名的配置文件，绑定各自的域名。 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress-discuz/wpdz-vhostconf-1-websoft9.png)

   - WordPress域名绑定：请修改“vhost.conf”里面的域名信息，然后保存
   - Discuz域名绑定：请修改“discuz.conf.范例”里面的域名信息，保存后再去掉“.范例”后缀使之生效

4. 使用 WinSCP 重启服务 或 云控制台重启服务器
   ```
   systemctl restart httpd
   ```
5. 分别完成安装向导
   - 本地浏览器访问：*https://wordpress.abc.com*   进入 [WordPress 安装向导](../wordpress#init)
   - 本地浏览器访问：*https://discuz.abc.com*   进入 [Discuz 安装向导](../discuz#init))

### FAQ

#### 如何删除引导页面？

打开IP地址显示的是引导页面，引导页面的作用是为了在镜像首次安装的时候给用户以有效提醒。

请到 */data/wwwroot/default* 目录中删除引导页面相关的内容。删除的时候，一定要保留wordpress和discuz文件夹，删除后请清除浏览器缓存，这样引导页面就不会出现了

#### 为什么默认打开是 WordPress？

WordPress相比Discuz来说更为流行，以Wordpress为主页是大多数用户可能的选择。Wordpress对应的配置文件是vhost.conf，可以自行修改

#### 安装的时候显示Discuz!DatabaseError?

如果数据库名称、数据库账号与数据库密码填写与实际不符合，安装就会失败，显示“Discuz!DatabaseError”错误，具体解决办法：

1. 使用phpMyAdmin（登录账号请使用discuz所用到的数据库账号）登录，验证你填写的数据库账号是否与实际匹配
2. 请到服务器上删除./data/install.lock文件
3. 通过网址：*https://ip/discuz/install* 或 *https://域名/install* 重装（一定要加上/install）
  
## Avada 主题指南{#avada}

Avada是一款在热门的WordPress主题，设计简单大方，支持所见即所得的可视化编辑与页面布局，内置超过20个免费模板，能够基于模板快速构建网站。Avada在Themeforest上累计销量超过37万次，其他下载和二次分发不计其数。适用于企业站和相册站、电商站、博客站。

![](https://photogallery.oss.aliyuncs.com/photo/1904996544835414/undefined/483d94c3-51bd-49ce-b5e8-2c86d62a448d.jpg)

### 主题下载与安装

Avada安装和下载有两种方式，请根据实际情况选择合适您的方式：

方式一：使用Avada镜像安装包（推荐）

* [阿里云WordPress镜像（含Aavad中文主题包）](https://market.aliyun.com/products/53616009/cmjj011415.html)
* [腾讯云WordPress镜像（含Avada中文主题包）](https://market.cloud.tencent.com/products/1515#)
* [华为云WordPress镜像（含Aavad中文主题包）](https://app.huaweicloud.com/all/?q=YXZhZGE)  

方式二：到themeforest.net 购买[原版](https://themeforest.net/item/avada-responsive-multipurpose-theme/2833226)  

方式三：在Websoft9下载主题自行安装
* [Avada 7.1.1 官方原版下载](https://libs.websoft9.com/apps/wordpress/avada7.1.1-en.zip)
* [Avada 6.2 汉化版下载](https://libs.websoft9.com/apps/wordpress/avada6.2-cn.zip)

---

**FAQ**

* 镜像包方式中的Avada有没有授权码？没有授权码，但可以正常使用
* Avada授权码有什么作用？可以在线升级主题和导入模板

### 启用 Avada 主题

如果你的 WordPress 预装包中包含了 Avada 主题，请参考本节完成 Avada 启用和模板导入：

#### 在线导入 Avada 模板

完成镜像安装之后，WordPress前台页面并没有模板的效果，请勿在这个时候误以为 Avada 没有高大上的效果而放弃它，那就太可惜了。实际上Avada内置了20+个免费模板，均可以在线导入。步骤如下：

1. 通过后台-插件，选择所有插件后全部启用  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-enableplugins-websoft9.png)

2. 后台-Avada-演示，进入Avada演示界面 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-getdemo-websoft9.png)

3. 选择一个演示，可以进行“预览”和“导入”两种操作

4. 以其中“Science”为例，点击导入，导入内容为“全部”，点击“导入”按钮 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-demoall-websoft9.png)

5. 系统会有一个提示，直接点击OK，进入演示导入过程 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-demook-websoft9.png)

6. 演示导入完成后，系统会提示“完成”（少数时候受制于网络原因，导入可能不成功，需要多次尝试） 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-democomplete-websoft9.png)

7. 点击“完成”，回到演示列表页面，会看到“Science”的状态已经为完全导入了。如果导入不成功，会显示部分导入 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-democomplete2-websoft9.png)

8. 在回到前台页面，看看模板的效果

#### 在线卸载 Avada 模板

导入的模板可以在线卸载（清除干净），如果你想导入新的模板，请先卸载已有模板，卸载步骤如下：

1. 后台-Avada-演示，找到要卸载的演示，点击“修改” 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-uninstall-websoft9.png)
2. 勾选“卸载”，点击移除按钮，开始卸载
3. 卸载成功，系统会提示完成


### 使用 Avada 主题9步建站 

在熟悉了WordPress之后，我们通过如下9个步骤的实践来熟悉Avada，同时将前面导入的演示页面修改成我们自己的页面，那么也就完成了一个网站的初步制作。

第一步 网站通用设置与配置

Avada采用的是配置式的工作方式，即网站的布局、风格、颜色、文字、页眉、页脚、背景等都是通过后台系统设置出来的，无需任何编程就可以应对个性化的需求。

后台-外观-主题选项，我们就进入了如下配置管理界面：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada_gsetting-websoft9.jpg)

**布局：**对网站内容区的宽度进行设置，一般建议布局采用宽屏模式，网站宽度设置为：1140px；

**菜单：**菜单是网站最重要的部分，设置也非常灵活。为了能够快速上手，我们只对“主菜单”和“手机菜单”的内容进行设置

**响应式：**响应式是即多屏幕自适应，默认请开启；

**颜色：**系统预设了10个颜色皮肤（注意是皮肤），尽量选择一个与您企业logo颜色相近似的皮肤颜色。也可以自定义，但自定义颜色需要对所有与颜色有关的设置中进行操作

**页眉：**即网站的顶部区域，通常网站所有页面都使用同样的页眉，以保持网站的整体风格统一。

*   页眉位置：一般选择顶部
*   页眉布局：一共6种选择，建议选择第一种
*   页眉样式：对页眉的css进行更改，高级用户使用
*   置顶页眉：页面在向上滚动的时候，页眉固定便在浏览器的顶部位置，这个就是置顶页眉。默认选择开启，保持较好的访问体验

**Logo：**即管理自己网站的logo，系统可以对主logo、置顶页眉logo、移动端logo、高清屏幕的logo分别进行设置，也可以只上传一个主logo，其他自动调用这个logo

**图标：**即我们常说的favicon.ico，显示在浏览器的Tabs上，非常重要。默认图标网站Favicon的大小为：16px x 16px。

**页面标题栏：**顾名思义即页面的标题区域，是在菜单栏的下方（如果有Slider的话一般在Slider的下方），每个页面的页面标题栏显示的内容有差异。面包屑导航即我们常说的“网站当前路径”

**滑动栏：**指的是网站右上角通过“+”来开启的伸缩内容，默认建议关闭

**页脚：**即网站的底部区域，分为页脚内容区和页脚版权区，其中页脚版权区在网站的最底部。Avada中页脚内容区是通过小工具来控制显示的，页脚列数即页脚内容区进行分割的内容块数，默认为4

**侧边栏：**主要对通用性的网页侧边内容区进行定义，高级用户使用

**背景：**网站背景图片设置

**版式：**即网站排版，设计到字体大小、H1-H6标题定义，是网站最重要的设置部分之一。正文版式中的字体，我们一般选择“微软雅黑”，字体大小为14。标题字体也默认选择“微软雅黑”比较合适。

**简码风格：**简码是插入html代码的短代码，这是WordPress提供的一中功能扩展方案，适合高级用户使用

**博客：**即文章管理，这里可以对文章分类、文章详情进行个性化的版式设计，内容元素显示控制，请保持默认设置

**作品集：**即案例管理，表现形式为图文混排的文字管理，保持默认设置即可

**社交媒体：**对社交媒体的图标和链接进行录入和设置。录入的社交媒体可以显示在页眉，也可以显示在页脚。可以通过“页眉社交图标”和“页脚社交图片”分别进行显示控制。此类别下的“社交分享盒”主要是对页面分享进行设置；

**幻灯片：**高级用户使用

**Elastic幻灯片：**Avada已经禁用了Elastic幻灯片，无需设置

**光盒：**光盒是点击图片的时候，网站自动对图片进行播放，这种效果即光合。高级用户使用

联系表：

**搜索页面：**对搜索图标的显示位置、搜索内容范围、搜索结果显示方式进行设置，高级用户使用

**附加：**高级用户使用

**高级：**高级用户使用

**自定义CSS：**开发者使用

**导入/导出：**对网站通用设置与配置的内容进行备份和导出导入，普通用户慎用

第二步 首页制作

在Avada主题中，首页与其他页面的制作原理是一样的，但显然首页更具有代表性，因此本章重点介绍首页的在线制作。

在学会制作前，请仔细阅读如下的首页布局图：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada_indexmap-websoft9.jpg)

如果我们通过4.1 网站通用设置与配置已经完成了页眉、页脚，那我们制作首页就非常简单了，只需要完成首页对应的Slider（轮播）和内容设置，再套用已经预设值好的页眉、页脚，首页就完成了。

制作首页有两种方式，包括：新建一个页面，命名为首页或在对一个已有的首页页面进行更改。在这里我们假设新建一个首页：

1、后台-页面-新增页面，我们会看到如下页面

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-addnewpage-websoft9.jpg)

上图就是一个页面制作界面，其中“Fusion页面构建器”为可视化模式，“默认编辑器”为code编辑模式，对于普通用户，我们选择可视化编辑模式

四个Tap，分别是列选项、构建器元素、自定义模板、预定模板。

列选项即css中的Div、行、列，全宽包含容器相当于一个全宽的div，div中可以容纳各种不同宽度的列。系统对列进行了比例划分归类，分别是1/1,1/2,1/3等

构建器元素还需要自己反复探索

自定义模板即对自己制作的页面保存为模板，后面新建页面就可以直接套用

预定模板即系统内置的模板，可以套用但是不能更改

2、如果制作首页？我们建议对一个已有的页面进行可视化编辑，这样更有感觉，学习的效率更高

第三步 轮播制作

轮播（Slider）是现代网页制作的一种常见的展现方式，我们务必掌握这个技能。Avada采用知名的轮播插件Slider Revolution作为主要（唯一）的轮播工具。

轮播的制作和使用步骤如下：

1、后台- Slider Revolution-新建滑块

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/Revolutionslider/3bc66360.jpg)

2、输入滑块名称，选择布局和样式，保存。轮播文件就新建好了

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/Revolutionslider/revs-new.jpg)

3、点击“Slider Editor”标签，进入轮播项的设计与处理

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/Revolutionslider/6823997d.png)

接下来，我们就像制作ppt一样制作轮播了

4、轮播完成之后，需要通过页面调用这个轮播。任意一个页面的页面选项，都有幻灯片的调用项。具体如下：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/plugins/Revolutionslider/80427780.png)

第四步 菜单管理

菜单是网站的核心入口，Avada可以把所有内容的标题和链接通过菜单的形式组织起来，然后供页面调用。

那么是如何实现自己的菜单的呢？

1、后台-外观-菜单，进入菜单编辑页面

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-createmenu-websoft9.png)

2、创建一个新菜单，名称定义为“我的菜单”（任意命名）

3、选择左侧菜单来源，分别添加到菜单中。显示位置选择“main navigation”为主菜单位置。菜单添加完成后，保存菜单

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-createmenu002-websoft9.png)

4、我们刷新网站，发现菜单已经更改成我们的菜单了

第五步 文章管理

文章是动态的内容区域，一般网站的新闻主要通过文章管理来实现。

我们以“制作一个动态的新闻中心栏目”来学会文章管理功能。具体操作如下：

1、后台-文章-分类目录-添加新分类目录，例如：公司新闻，保存

2、文章-写文章，其中分类目录勾选我们刚刚新建的“公司新闻”。可以增加多个文章

3、新建一个页面，命名为“新闻中心”，给此页面增加一个行的容器元素

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-rongqi001-websoft9.png)

4、给行内添加一个构建起元素，选择博客

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-rongqi002-websoft9.png)

5、进入博客调用（文章调用）设置页面，其中分类选择刚刚新建的“公司新闻”类目

6、保存页面，完成

第六步 案例管理（作品）

Avada有专有的案例管理功能，在后台体现问“作品”。作品管理与文章管理非常类型，都是建栏目，增加作品项，然后在响应的页面进行调用。

下面以一个“新建一个公司官网的成功案例”为例来进行说明，具体如下：

1、后台-作品-作品分类，我们建立一个“设计案例”分类，保持

2、作品-新文章（即增加案例项），自行填写

3、对作品的特色图像进行设置（这样页面调用的时候才会有图片的动画效果）

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-spepic-websoft9.png)

4、新建一个页面，命名为“案例”，给此页面增加一个行的容器元素

5、给行业增加一个构建器元素-作品

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-rongqi003-websoft9.png)

6、进入作品调用设置页面，可以一般设置一边预览

7、设计完成，保存

第七步 常见问题管理

常见问题是一个服务类或营销型官网必须具备的栏目，通过简单有效的一问一答的方式，快速的解答客户的疑问。Avada 有一个常见问题的模块：

下面以一个“新建一个公司官网的常见问题页面”为例来进行说明，具体如下：

1、后台-常见问题-FAQ目录，我们建立一个“安装问题”分类，保持

2、常见问-写文章（即增加常见问题项），自行填写一个或多个

3、新建一个页面，命名为“常见问题”，给此页面增加一个行的容器元素

4、给行业增加一个构建器元素-常见问题

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-rongqi004-websoft9.png)

6、进入常见问题调用设置页面，可以一般设置一边预览

7、设计完成，保存

第八步 小工具栏的使用

小工具栏是Avada中的高级功能项，小工具的特点就是可以自行定义内容&amp;可以被任何页面调用。因此，小工具对于个性化的建站非常有作用。小工具栏的的使用原理是：把网页的一些元素或功能插到指定的小工具上，然后需要用到这些元素的页面直接调用响应的小工具即可。

系统默认有几个固定的小工具（不可以删除），包括：

*   Blog Sidebar   用于所有文章内容的侧边栏
*   Footer  Widget1   用于页脚的工具栏1
*   Footer  Widget2  用于页脚的工具栏1
*   Footer  Widget3  用于页脚的工具栏1
*   Footer  Widget1  用于页脚的工具栏1

如何自定义自己的小工具栏，并调用呢？

下面我们一个“建立小广告内容小工具”为例来进行演示，具体如下：

1、后台-外观-小工具

2、小工具-添加小工具（名称一定只能是英文，否则无法调用）

3、将左侧的“可用小工具”元素拖到右侧小工具栏中（如果拖拽的是文本项，可以在文本项中自定义任意html或js代码），然后保存

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-widget001-websoft9.png)

4、新建或任何已有的页面进入编辑状态，插入构建器元素-小工具区

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-widget002-websoft9.png)

5、选择您的小工具，保存

备注：小工具一旦与页面实现了关联之后，小工具的内容可以任意更改，页面调用之处都会自动发送变化。实现了一次定义，多处使用的快捷方法。

第九步 SEO

Avada的SEO是通过一个SEO插件来实现的，这里我们推荐使用最广的SEO插件-Yoast SEO。

如何实现网站的SEO呢？

1、安装Yoast SEO（免费插件）

2、按照Yoast SEO的设置向导进行初始化的设置

3、Yoast SEO一旦安装完成之后，所有的页面（文章）类型都嵌入登录SEO选项。我们通过页面-所有页面，会看到所有页面都有SEO的属性（其中圆图标代表SEO的优化程度），如下图：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-seo001-websoft9.png)

4、进入任意一个页面的的编辑状态项，都会出现SEO的选项。一般填写关键字和描述即可。Yoast SEO还有一个分析检查SEO填写的功能，仅供参考

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/avada/avada-seo002-websoft9.png)

说明：以上仅描述了SEO的实现方法。SEO是一门学问（伴随人工智能出现，SEO未来的学问会越来越浅），如何设置关键、描述等信息，还需要自己反复探索。
