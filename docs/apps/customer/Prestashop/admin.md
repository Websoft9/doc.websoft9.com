---
sidebar_position: 3
slug: /prestashop/admin
tags:
  - PrestaShop
  - 电子商务
---

# 维护指南

## 场景

### 备份与恢复

PrestaShop 提供了后台数据库备份功能

1. 登录 PrestaShop 后台
2. 依次打开：【Advanced Parameters】>【DB backup】
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-dbbackup-websoft9.png)
3. 创建一个备份，然后下载到本地

### 升级

Prestashop 自动备份是通过一个名称为“1-Click Upgrade”的插件实现的，具体步骤如下：

1. 登录 PrestaShop 后台，打开【Modules Catalog】，搜索“upgrade”，安装备份插件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-upgrade001-websoft9.png)

2. 安装完成后，点击“配置”，进入模块设置界面

3. 根据设置建议，将系统置为维护模式（maintenance mode）
   
4. 点击【Upgrade PrestaShop now】按钮，开始升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-upgrade002-websoft9.png)

5. 升级过程中首先会下载最新的安装包，受制于网络因素，这个过程可能会比较慢。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-upgrade003-websoft9.png)

6. 升级过程的例外情况
   - 如果下载新版本这个步骤无法完成，需要多次尝试
   - 若出现 “you don't have permission...ajax-upgradetab.php” 的错误提示，升级失败，暂无解决办法

> 与升级有关的更多方案，请参考官方文档：[PrestaShop Backup](https://doc.prestashop.com/display/PS16/Manual+update)

### PrestaShop Module 升级

PrestaShop 提供了在线插件升级能力

1. 登录 PrestaShop 后台，打开【Modules Catalog】

2. 找到需要升级的插件，点击【Upgrade】即可在线升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-upgrademodules-websoft9.png)


## 故障速查

除以下列出的 PrestaShop 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

#### Prestashop 重定向错误？

多语言下，重定向错误比较常见。例如：打开您的Prestashop商店中文版会出现重定向

处理办法：

1. 分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则
   
2. 进入后台先删除中文，然后再重新导入中文。重新导入的时候，Prestashop会自动生成伪静态规则，覆盖您网站根目录的 `.htaccess` 文件


#### 修改了数据库密码 PrestaShop 不能访问？

若已完成 PrestaShop 安装向导，再通过 phpMyAdmin 修改数据库密码，PrestaShop 就会连不上数据库

需要修改 [PrestaShop 配置文件](../prestashop#path) 对应的数据库 password 参数即可。


## 问题解答

#### PrestaShop 支持多语言吗？

支持多语言（包含中文），通过[后台设置](../prestashop#setlanguage)即可

#### 为什么要连接 PrestaShop Marketplace？

只有连接 PrestaShop Marketplace，才可以使用其资源。连接教程[参考](../prestashop#marketplace)

#### PrestaShop(LAMP)，PrestaShop(LNMP)等商品括号中的 LAMP,LNMP 是什么意思？

LAMP和LNMP代表支持 PrestaShop 运行所对应的基础环境，具体参考[环境说明](../prestashop#ref)

#### 是否可以使用云平台的 RDS 作为 PrestaShop 的数据库？

可以，修改 [PrestaShop 配置文件](../prestashop#path) 即可

#### PrestaShop能在Windows服务器上运行吗？

可以，但是我们推荐在运行 PrestaShop 效率更高的 Linux 服务器上运行

#### PrestaShop数据库连接配置信息在哪里？

数据库配置信息 [PrestaShop 配置文件](../prestashop#path))中

#### 如果没有域名是否可以部署 PrestaShop？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP/phpmyadmin

#### 如何禁止phpMyAdmin访问？

连接服务器，编辑 phpMyAdmin 配置文件，将其中的 Require all granted 更改为 Require ip 192.160.1.0，然后重启 Apache 服务

#### 是否可以修改 PrestaShop 的源码路径？

可以，通过修改 [虚拟主机配置文件](./apache#virtualHost)中相关参数