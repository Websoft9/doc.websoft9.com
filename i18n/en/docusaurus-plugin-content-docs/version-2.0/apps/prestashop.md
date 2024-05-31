---
title: Prestashop
slug: /prestashop
tags:
  - PrestaShop
  - 电子商务
  - 建站
  - 跨境电商
---

import Meta from './_include/prestashop.md';

<Meta name="meta" />

## 入门指南{#guide}

### 功能界面

Websoft9 控制台安装 Prestashop 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。 

1. 前台商城
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-site-websoft9.png)

2. 登陆页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-login-websoft9.png)

3. 后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-backend-websoft9.png)


### 安装扩展（Modules）{#module}

Modules 是 PrestaShop 功能扩展，Modules 可以即插即用

1. 登录 PrestaShop 后台，依次打开：【Modules】>【Module Catalog】，找到所需的插件，点击【Install】开始安装
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-installmd-websoft9.png)

3. 依次打开：【Modules】>【Module Manager】，找到所需的插件，点击【Upgrade】即可在线升级  

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-upgrademodules-websoft9.png)

### 连接 Marketplace{#marketplace}

安装 PrestaShop 后，建议把你安装的 PrestaShop 系统与 PrestaShop 官方的 Marketplace 资源进行在线连接，这样便可以在线使用 Marketplace 上的大量资源

1. 登录 PrestaShop 后台

2. 依次打开：【Modules】>【Module Manager】，点击【Connect to Addons marketplace】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-connectmk-websoft9.png) 

3. 开始注册账号
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-registeraccount-websoft9.png)  

4. 注册完成后，登录连接

5. 连接后，就可以很方便的使用 Marketplace 上的资源
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/prestashop-marketplace-websoft9.png)

### 语言包管理{#setlanguage}

Prestashop的多语言支持非常的成熟，系统在后台内置一套多语言体系，只需要选择对应的语言，在线导入到您的 PrestaShop 系统即可。
> 在设置过程中，如提示'This functionality has been disabled.'，请提前修改配置文件：/data/apps/prestashop/data/prestashop/config/defines.inc.php，修改配置项为 false：
```
if (!defined('_PS_MODE_DEMO_')) {
    define('_PS_MODE_DEMO_', false);
}
```

##### 导入语言

1. 登录Prestashop后台，依次打开：【国际】>【本地化】，进入设置界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-setlang-websoft9.png)

2. 选择一个语言包，点击本项之右下角【上传】图标，完成在线导入

3. 选择【语言】选项卡，我们就可以看到成功导入的语言包
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-alllanguage-websoft9.png) 

> 每次导入一个新的语言包，系统会自动为此语言生成一个伪静态规则。如果您的某个语言的伪静态设置出现问题导致了 Redirect（重定向），可以删除这个语言，然后重新导入一次即可。

4. 通过修改个人信息，设置后台显示语言
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-setlanguage-websoft9.png) 

##### 删除语言

1. 登录Prestashop后台，依次打开：【国际】>【本地化】>【语言】，编辑您需要的语言
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-dellanguage001-websoft9.png)

2. 将语言的状态修改为“否”，然后保存

3. 回到【语言】选项开，找到已经打叉的语言，删除之即可
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-dellanguage002-websoft9.png)

### 导入演示数据

登录 PrestaShop 后台，打开：【Advanced Parameters】>【Import】，导入所需的数据 

  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-importdb-websoft9.png)


## 配置选项{#configs}

配置过程可能需要用到的命令、配置文件等

- 后台登录地址：通过 Websoft9 控制台我的应用查看
- [configuring-prestashop](https://devdocs.prestashop-project.org/8/development/configuration/configuring-prestashop/)  
- [list-of-settings](https://devdocs.prestashop-project.org/8/development/configuration/list-of-settings/)
- CLI
  ```
  # list all cli
  php bin/console list

  # get help of prestashop:config
  php bin/console prestashop:config -h
  ```

## 管理维护{#administrator}

### 使用 CLI

- [configuring-prestashop](https://devdocs.prestashop-project.org/8/development/configuration/configuring-prestashop/)  
- [list-of-settings](https://devdocs.prestashop-project.org/8/development/configuration/list-of-settings/)

进入 PrestaShop 容器，运行如下命令：

   ```
   # list all cli
   php bin/console list

   # get help of prestashop:config
   php bin/console prestashop:config -h
   ```

### 设置维护模式{#maintenance}

登录 PrestaShop 后台，打开：【Shop Parameters】>【General】>【Maintenance】，设置维护模式
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-mantmode-websoft9.png)

### 配置 SMTP{#smtp}

1. 登录到 PrestaShop 后台，依次打开：【配置】>【高级参数】>【邮箱】，选择第二项【设置我的SMTP参数】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-smtp-1-websoft9.png)

2. 准确的填写你的 SMTP 参数，发送测试邮件
     

### 修改 URL {#url}

更换域名后，需设置 PrestaShop URL:

1. 登录 PrestaShop 后台，将 PrestaShop [设置为维护模式](#maintenance) （可选操作）

2. 依次打开：Shop Parameters > SEO & URLs > Set shop URL 修改
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-seturl-websoft9.png)

### 数据库备份

PrestaShop 提供了后台数据库备份功能

1. 登录 PrestaShop 后台，依次打开：【Advanced Parameters】>【DB backup】
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-dbbackup-websoft9.png)

3. 创建一个备份，然后下载到本地

### 自动备份

Prestashop 自动备份是通过一个名称为【1-Click Upgrade】的插件实现的，具体步骤如下：

1. 登录 PrestaShop 后台，打开【Modules Catalog】，搜索【upgrade】，安装备份插件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-upgrade001-websoft9.png)

2. 安装完成后，点击【配置】，进入模块设置界面

3. 根据设置建议，将系统置为维护模式（maintenance mode）
   
4. 点击【Upgrade PrestaShop now】按钮，开始升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-upgrade002-websoft9.png)

5. 升级过程中首先会下载最新的安装包，受制于网络因素，这个过程可能会比较慢。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-upgrade003-websoft9.png)

6. 升级过程的例外情况

   - 如果下载新版本这个步骤无法完成，需要多次尝试
   - 若出现 “you don't have permission...ajax-upgradetab.php” 的错误提示，升级失败，暂无解决办法

> 与升级有关的更多方案，请参考官方文档：[PrestaShop Backup](https://doc.prestashop.com/display/PS16/Manual+update)

### Module 升级

PrestaShop 提供了在线 Module（模块）升级能力

1. 登录 PrestaShop 后台，打开【Modules Catalog】

2. 找到需要升级的Module，点击【Upgrade】即可在线升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-upgrademodules-websoft9.png)

## 故障

#### HTTPS 配置后，后台正常，前台访问失败？ 

将数据库表 ps_configuration 属性 PS_SSL_ENABLED_EVERYWHERE 和 PS_SSL_ENABLED 值设为 1

#### Prestashop 重定向错误？

多语言下，重定向错误比较常见。例如：打开您的 Prestashop 商店中文版会出现重定向

处理办法：

1. 分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则
2. 删除自行安装的语言包。再次重新导入，Prestashop 会自动生成伪静态规则，覆盖原有 `.htaccess` 文件