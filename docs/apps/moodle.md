---
title: Moodle
slug: /moodle
tags:
  - 在线学习
  - LMS
  - 教学管理
  - 课程管理
---

import Meta from './_include/moodle.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Moodle 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 使用本地电脑的浏览器访问，进入引导首页

2. 点击【login】 ，进入登陆页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install2-websoft9.png)

3. 登陆成功后，进入 Moodle 后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install3-websoft9.png) 

Moodle 旗下其他产品说明：  

* Moodle LMS：开源的在线学习系统
* Moodle Workplace：Moodle LMS + 高级功能，不开源
* MoodleCloud：Moodle LMS 托管服务，即 SaaS 版
* Moodle App：移动端
* MoodleNet：共享和管理开放教育资源

### 向 Moodle 注册你的网站{#register}

Moodle 初始化之后，建议注册为 Moodle 官方会员以便获取升级通知，课程共享，在线安装插件等

1. 以管理员身份登录 Moodle 后台
2. 依次打开：【网站管理】>【注册】
   ![Moodle 注册](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-registermd-websoft9.png)
3. 注册完成后登陆，这样你的 Moodle 与官方便建立了一个连接关系

### 移动端{#client}

1. 以管理身份登录 Moodle 后台

2. 依次打开：【网站管理】>【移动应用程序】>【移动设备设置】
   ![moodle-apps](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-app-1-websoft9.jpg)

3. 将【为移动设备启用网络服务】设为 **启用** 状态；
   ![moodle-apps](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-app-2-websoft9.jpg)

4. 安装 [Moodle 手机客户端](https://download.moodle.org/mobile/)

5. 打开后在地址栏输入 Moodle 的访问地址，就可以开始使用移动端
   ![moodle-apps](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-mobile-websoft9.png)

### 插件{#plugin}

Moodle 是一个非常灵活的平台，大部分核心功能以插件的形式存在，系统默认安装了400多个插件。同时，官方提供了[插件市场](https://moodle.org/plugins/)供用户作用更多功能扩展。

1. [注册 Moodle 官方账号](#register)，打通你的 Moodle 与官方的连接，便于在线安装插件。

2. 以管理员身份登录 Moodle 后台

3. 依次打开：【网站管理】>【插件】，会看到**安装插件**和**插件概况**两个链接
   ![moodle 插件](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-plugins-websoft9.png)

   * 安装插件：安装新插件入口
   * 插件概况：查看已经安装的插件列表

4. 点击【安装插件】，提供**从Moodle插件目录安装插件**和**从ZIP文件中安装插件**两种安装插件的方式
   ![moodle 安装插件](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-pluginsmk-websoft9.png)

   * 从Moodle插件目录安装插件：自动跳转并登录到 Moodle 的[官方插件市场](https://moodle.org/plugins/)，便可以在线安装
   * 从ZIP文件中安装插件：需提前下载插件压缩文件，再从此处**上传**安装

5. 点击【插件概况】，列出默认安装的插件，可以进行停用、卸载等操作
   ![moodle 插件概况](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-plugininfo-websoft9.png)

### 主题{#theme}

Moodle 主题实际上是一个插件，因此需要安装新主题，必须通过【安装插件】的方式先进行安装。  

1. 以管理员身份登录 Moodle

2. 依次打开：【网站管理】>【插件】，进入[插件市场](https://moodle.org/plugins/)后，选择【Theme】类型的插件,并下载
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-mktheme-websoft9.png)

3. 在线安装所需的主题

4. 打开【网站管理】>【外观】>【主题选择器】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-addtheme001-websoft9.png)

5. 点击【更改主题】即可完成主题更换
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-addtheme002-websoft9.png)

## 配置选项{#configs}

- 配置文件：/path/config.php
- 媒体文件（✅）
- 多语言（✅）：【Site administration】>【language】>【Language Packs】
- SMTP（✅）：【网站管理】>【服务器】>【电子邮件】>【发送邮件设置】
- 移动端（✅）：【网站管理】>【移动应用程序】>【移动设备设置】>【为移动设备启用网络服务】
- [Plugins](https://docs.moodle.org/37/en/Installing_plugins)
- [Administration via command line](https://docs.moodle.org/311/en/Administration_via_command_line)
    ```
    $ sudo -u apache /usr/bin/php admin/cli/somescript.php --params
    $ sudo -u apache /usr/bin/php admin/cli/install.php --help
    ```
- [Core APIs](https://docs.moodle.org/dev/Core_APIs)

## 管理维护{#administrator}


### 修改 URL{#url}

配置文件的配置项：$CFG->wwwroot 设置 URL

### HTTPS 额外设置{#https}

配置文件的配置项：$CFG->wwwroot 设置 URL

### 找回密码

Moodle 支持邮件找回密码。如果没有配置邮件，需通过修改数据库的方式找回密码：

1. 使用 phpMyAdmin 等可视化工具，修改数据库的 *mdl_user* 表
2. 编辑【admin】用户，将其中的 `password` 字段的值用 `21232f297a57a5a743894a0e4a801fc3` 替换
3. 点击【执行】，新的密码就被重置为`admin`

### 在线备份

课程是 Moodle 最重要的资源，Moodle 后台提供了自动备份课程的功能

1. 以管理员身份登录 Moodle 后台

2. 依次打开：【网站管理】>【课程】>【备份】，开始进行备份设置
  ![Moodle 课程备份](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-coursebk-websoft9.png)

3. 详细设置请自行研究

4. 依次打开：【网站管理】>【报表】>【备份】，查看备份执行情况
  ![Moodle 查看备份](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-coursebkrp-websoft9.png)

## 故障