---
sidebar_position: 3
slug: /prestashop/admin
tags:
  - PrestaShop
  - 电子商务
---

# 维护指南

## 场景

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


## 故障速查

除以下列出的 PrestaShop 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

#### Prestashop 重定向错误？

多语言下，重定向错误比较常见。例如：打开您的 Prestashop 商店中文版会出现重定向

处理办法：

1. 分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则
2. 删除自行安装的语言包。再次重新导入，Prestashop 会自动生成伪静态规则，覆盖原有 `.htaccess` 文件


## 问题解答

#### PrestaShop 支持多语言吗？

支持多语言（包含中文），通过[后台设置](../prestashop#setlanguage)即可

#### 为什么要连接 PrestaShop Marketplace？

只有连接 PrestaShop Marketplace，才可以使用其资源。连接教程[参考](../prestashop#marketplace)