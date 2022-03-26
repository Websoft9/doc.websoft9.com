---
sidebar_position: 3
slug: /mediawiki/admin
tags:
  - Mediawiki
  - CMS
  - 知识管理
  - 博客系统
---

# 维护指南

## 场景

### 备份与恢复

### 升级

升级请参考官方文档 [MediaWiki Upgrading](https://www.mediawiki.org/wiki/Manual:Upgrading/zh)

## 故障速查

除以下列出的 MediaWiki 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 


## 问题解答

#### MediaWiki 支持多语言吗？

支持多语言（包含中文），后台可以[设置语言](../mediawiki#setlang)

#### MediaWiki 能上传多媒体文件吗？

可以，但需要提前[启用 MediaWiki 文件上传](../mediawiki#upload)功能

#### MediaWiki(LAMP)，MediaWiki(LNMP)等商品括号中的 LAMP,LNMP 是什么意思？

LAMP和LNMP代表支持MediaWiki运行所对应的基础环境，具体参考[环境说明](./runtime/php)

#### 是否可以使用云平台的 RDS 作为 MediaWiki 的数据库？

可以，修改 MediaWiki 根目录下的[配置文件 ](../mediawiki#path)`config.php` 即可

#### MediaWiki能在Windows服务器上运行吗？

可以，但是我们推荐在运行 MediaWiki 效率更高的 Linux 服务器上运行

#### MediaWiki数据库连接配置信息在哪里？

数据库配置信息在MediaWiki安装目录下的 *LocalSettings.php* 中，[查阅安装目录路径](../mediawiki#path)

#### 如果没有域名是否可以部署 MediaWiki？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP/phpmyadmin

#### 如何禁止phpMyAdmin访问？

连接服务器，编辑 phpMyAdmin 配置文件，将其中的 Require all granted 更改为 Require ip 192.160.1.0，然后重启 Apache 服务

#### 是否可以修改 MediaWiki 的源码路径？

可以，通过修改 [虚拟主机配置文件](../apache#virtualHost)中相关参数