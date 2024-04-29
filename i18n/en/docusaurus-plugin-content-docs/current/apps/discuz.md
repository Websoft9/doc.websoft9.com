---
title: Discuz
slug: /discuz
tags:
  - 建站
  - 论坛
  - 网站
---

import Meta from './_include/discuz.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Discuz 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

1. 使用本地电脑浏览器访问，就进入引导首页

2. 首先点击【我同意】，确认用户许可协议
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds01.png)

3. 通过环境检测后，点击【下一步】。  
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds02.png)

4. 选择需要安装的程序组，建议选择【全新安装】，然后点击【下一步】。  
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds03.png)

5. 配置连接信息：请直接点击【下一步】完成连接。（**除设置管理员密码外请不做任何修改**）   
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds04.png)

6. 安装完成后的界面如下  
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds05.png)

7. 进入论坛后，可以通过右上角登录对论坛进行管理。
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/ds06.png)

### 模板/主题/应用中心

Discuz 有非常强大生态，大量在线安装模板、插件，您通过登录到 Discuz 后台，并连接您的【应用中心】账号，你就可以通过后台在线购买（免费或收费）插件模板，并在线安装就可以使用了。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-appcenter-websoft9.png)

### 更换默认 Logo

参考论坛上的热心帖子：[如何替换程序默认Logo](http://www.discuz.net/thread-3185527-1-1.html) 

  
### 修改上传附件大小

但 Discuz 用户上传大小无法满足需求，请通过如下的方式进行修改：

1.进入后台，选择【用户】选项，在【管理者】中选择相应用户组，进入基本设置

  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-modifyfilesize001-websoft9.png)

2.选择【论坛相关】，选中【附件相关】

  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-modifyfilesize002-websoft9.png)

3.进入附件相关，在【论坛最大附件尺寸】中设置附加最大尺寸

  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-modifyfilesize003-websoft9.png)

## 配置选项{#configs}

- 配置文件: */path/config/config_default.php*  
- 多语言（×）
- 移动端：官方没有提供移动端

## 管理维护{#administrator}

### 设置伪静态

Discuz论坛安装完成后，想使连接里面显示文章名，应怎么开启它的伪静态功能？

1. 网站安装完成后，登录进入后台，在全局>SEO优化设置>将要设置的页面勾选上，然后提交； 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-rewrite001-websoft9.png)

2. 重新回到上图页面，点击【查看当前的 Rewrite 规则】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-rewrite002-websoft9.png)

3. 页面会列出多种规则，请选择【Apache Web Server(虚拟主机用户)】模板

4. 在 Discuz 的根目录下，新建一个`.htaccess` 文件，将上面的模板内容拷贝进去，保存
   如果是Windows服务器，请选择【另存为】，文件类型选择【所有文件】，否则无法命名
  
5. 重启应用后生效


### 重置管理员密码

Discuz 密码忘记了，怎么找回？ 如下方案经过实践可用：

1. 编辑 Discuz 根目录下的 *uc_server/data/config.inc.php* 文件
2. 用下面两行代码替换 `config.inc.php` 中已有的同名段
   ```
   define('UC_FOUNDERPW','047099adb883dc19616dae0ef2adc5b6');
   define('UC_FOUNDERSALT','311254');
   ```
3. [重启服务](./administrator/parameter#service)
4. 此时 Ucenter 创始人的密码就变为: `123456789`
5. 访问 *http://服务器公网IP/uc_server*，以`123456789`作为密码登录 Ucenter
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-ucpwlogin-websoft9.png)
6. 通过【用户管理】中修改管理员密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-ucentermodifyadmin-websoft9.png)

### 更换 URL{#url}

Discuz 更换域名非常繁琐，参考论坛上的热心帖子：[discuz! X3 更改域名全程记录](https://www.discuz.net/thread-3528253-1-1.html)

### 配置 SMTP{#smtp}

1. 进入 Discuz 后台，打开：【站长】>【邮件设置】，仔细填写 SMTP 参数项   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-smtp-1-websoft9.png)

	- 选择第二项
	- 根据你的 SMTP 邮箱选择 SMTP服务器域名，前面的”ssl://“一定不能省略
	- 端口栏输入 SMTP 服务器提供的端口号，一般为 465 ，具体的可根据自己的邮箱地址到官网查看
	- 发件人邮件地址输入你自己的邮箱（**需要与SMTP身份验证用户名所填的邮箱地址一致**）
	- 输入提供 SMTP 服务的邮箱地址
	- 输入 SMTP 服务验证码（和邮箱登陆密码不一样）
 
2. 在 Discuz 后台，打开【全局】>【站点信息】，设置全局管理员邮箱，尽量和 SMTP 发件人邮箱保持一致
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-smtp-2-websoft9.png)
    
3. 测试，如出现如图所示的对话框则证明 SMTP 设置正确
	![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-smtp-3-websoft9.png)

### 在线备份与恢复

Discuz 后台提供了非常简单实用的在线备份功能，使用方法如下：

1. 登录 Discuz 后台，打开：【后台】>【站长】>【数据库】，进入备份页面，设置备份策略。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-backup-websoft9.png)

2. 点击备份操作

3. 在线实现的备份可以在线恢复（还原）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/discuz/discuz-restore-websoft9.png)

### 升级

Discuz 需要手工上传升级包方可升级，这项工作对普通用户来说非常有挑战性。  

Discuz 官方提供了一个：[升级参考](https://gitee.com/Discuz/DiscuzX/wikis/%E5%8D%87%E7%BA%A7%E6%96%B9%E6%B3%95?sort_id=9978)

## 故障

#### Discuz 重定向错误？

重定向错误比较常见。处理办法：分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则

#### Discuz 密码被锁，怎么解决？

1. 10分钟后会自动解锁。
2. 管理员登录，组织→用户 操作栏里有解锁按钮。

#### 对不起，您的网站已被设置禁止下载此应用？

问题原因：[Discuz!扩展中心防骗云平台](http://www.kuozhan.net/blacklist-index.html)专门针对盗版网站进行屏蔽网站授权，导致众多无辜站长用户无法更新和下载应用中心插件、模板，并且出现”对不起，您的网站已被设置禁止下载此应用“的提示。  

解决方法：
 1. 连接 Discuz 数据库，找到 **pre_common_setting** 这个表（默认表前缀pre_，请以你自己的为准。）
 2. 在找到的表里删除掉 siteuniqueid 这个数据（pre_common_setting表中的第10页位置。）
 3. 再重新进入网站后台——应用——获取更多应用，再次下载更新试下吧！

#### 手机版报错“接口错误 err05 微社区域名已更换”？

错误原因：Discuz官方提供的接口地址由http://wsq.discuz.qq.com/ 换成了现在 http://wsq.discuz.com/
解决方法：
  1. 登录服务器，找到Discuz根目录下的 */data/wwwroot/discuz/upload/source/class/helper/helper_form.php* 文件
  2. 将 'http://wsq.discuz.qq.com/', 25  改为 'http://wsq.discuz.com/', 22
  3. 清除 data/cache/qrcode 下的所有缓存文件
