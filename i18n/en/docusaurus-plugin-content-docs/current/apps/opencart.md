---
title: OpenCart
slug: /opencart
tags:
  - 电子商务
  - 建站
  - 电商
---

import Meta from './_include/opencart.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 OpenCart 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 使用本地电脑浏览器后，就进入引导首页

2. 根据引导，依次完成协议勾选、环境检测等步骤
   ![oc1](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/opencart-install01-websoft9.png)  

3. 设置数据库连接和管理员账号
   ![oc1](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/opencart-install03-websoft9.png)

  > 数据库连接信息可以更改为自己所需，也可以使用默认值

4. 安装成功后，系统提示【删除安装目录】，需进入 OpenCart 的数据目录删除 install 文件夹


### 安装插件{#installplugin}

OpenCart 提供了大量的扩展发布在 Marketplace 上，下面是具体的安装扩展步骤：

1. 在 Marketplace 上下载所需的扩展

2. 登录 OpenCart 后台，依次打开：【Extensions】>【Installer】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/opencart-installex-websoft9.png)

3. 上传扩展文件

4. 等待安装完成


### 安装语言包{#setlanguage}

在 Opencart 中增加一个新的语言（以中文包为例），主要有三个步骤：

1. 到 [OpenCart Marketplace](https://www.opencart.com/index.php?route=marketplace/extension&filter_search=chinese&filter_category_id=2)找到目标语言包；

2. 根据语言包自身的说明，进行在线上传安装并配置

5. 安装成功后，店铺前后台分别选择所需的语言：【System】>【Settings】  

   - Language 为前台默认语言
   - Administration Language 为后台默认语言

	![websoft9](https://libs.websoft9.com/Websoft9/DocsPicture/zh/opencart/opencart-language-2-websoft9.png)

6. 刷新前后台页面，系统显示新的语言

### 更改 URL {#dns}

更换域名后，需重新设置 **前台和后台**的配置文件中的 *HTTP_SERVER* 和 *HTTP_CATALOG*  

## 配置选项{#configs}

- 配置文件
  - 前台： /path/config.php
  - 后台： /path/admin/config.php

- [OpenCart API](http://docs.opencart.com/en-gb/system/users/api/)


## 管理维护{#administrator}

### 备份

OpenCart 后台提供了数据库备份功能

1. 登录 OpenCart 后台
2. 打开：【System】>【Maintenance】>【Backup/Restore】，开始备份数据库
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/opencart-backupdb-websoft9.png)

### 升级

参考：[官方升级文档](https://docs.opencart.com/en-gb/upgrading/)

## 故障

#### Dashboard 提示移动 Storage 文件夹？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/opencart/opencart-storagepath-websoft9.png)  

建议忽略此提示，因为移动文件夹会导致不可知的代码错误

####  域名配置后，页面布局混乱？

**原因分析**：先通过 IP 安装，再绑定域名，导致默认 URL 发生变化   

**解决方案**：[修改 URL](../opencart#dns)

#### 安装插件，显示403权限不足？

**现象描述**：错误信息 "you dont have permession to access /admin/index.php"   
**解决方案**：修改文件：/etc/httpd/conf.d/mod\_evasive.conf 中  DOSPageCount 2 改为 DOSPageCount 12

