---
title: Mediawiki
slug: /mediawiki
tags:
  - Wiki
  - CMS
  - 知识管理
  - 博客系统
---

import Meta from './_include/mediawiki.md';

<Meta name="meta" />

## 入门指南{#guide}

Websoft9 控制台安装 Mediawiki 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  


### 安装扩展{#plugin}

参考官方文档：[Manual:Extensions](https://www.mediawiki.org/wiki/Manual:Extensions/zh)

### 创建或编辑页面{#page}

参考官方文档：[Help:Starting_a_new_page](https://www.mediawiki.org/wiki/Help:Starting_a_new_page/zh)

### 可视化编辑器{#edit}

参考官方文档：[Help:Starting_a_new_page](https://www.mediawiki.org/wiki/Help:VisualEditor/User_guide/zh)

### 定制界面{#theme}

定制界面包括：修改 Logo, 设置导航栏，修改 CSS 等  

参考官方文档：[Help:FAQ:定制界面](https://www.mediawiki.org/wiki/Manual:FAQ/zh#定制界面)

### 允许文件上传{#upload}

Mediawiki 默认并不可以上传文件，需要启动文件上传功能  

参考官方文档：[Help:FAQ:启用文件上传](https://www.mediawiki.org/wiki/Manual:FAQ/zh#如何启用文件上传?)

### 语言设置{#setlang}

参考官方文档：[Help:FAQ:语言设置](https://www.mediawiki.org/wiki/Manual:FAQ/zh#我如何更改界面语言？)

### 设置主页{#sethomepage}

参考官方文档：[Help:FAQ:设置主页](https://www.mediawiki.org/wiki/Manual:FAQ/zh#如何指定首页?)

## 配置选项{#configs}

## 管理维护{#administrator}

- 配置文件：LocalSettings.php
- [API:Main_page](https://www.mediawiki.org/wiki/API:Main_page/zh)
- 多语言（✅）
- 多媒体文件（✅）

### 配置 SMTP{#smtp}

1. 编辑根目录下的 `LocalSettings.php` 配置文件

2. 找到变量 $wgSMTP，并设置它
   
   ```
    $wgSMTP = array(
    'host'     => "smtp.163.com", 
    'IDHost'   => "example.com",      // 邮箱域名，可选.如果不设置的话会设置成 $wgServer 的值.
    'port'     => 465,                 
    'auth'     => true,               
    'username' => "websoft9@163.com",     
    'password' => "#wwBJ8"       
    );
   ```

3. 找到变量 $ wgEnableEmail，设置其值为 true
   
   ```
    $ wgEnableEmail = true
   ```


4. 查找以下变量，将其值设置为发件邮箱
   
   ```
    $wgEmergencyContact = "websoft9@163.com";
    $wgPasswordSender = "websoft9@163.com";
   ```

5. 设置完成后，重启容器生效


### 升级

升级请参考官方文档 [MediaWiki Upgrading](https://www.mediawiki.org/wiki/Manual:Upgrading/zh)

## 故障