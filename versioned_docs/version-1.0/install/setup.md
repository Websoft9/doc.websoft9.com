---
sidebar_position: 3
slug: /install/setup
---

import DocCardList from '@theme/DocCardList';
import {useCurrentSidebarCategory} from '@docusaurus/theme-common';


# 安装后配置

安装 Websoft9 的产品后，便可以通过**服务器公网IP+端口**的方式访问可视化面板。  

- 默认的访问 URL 是： *http://服务器公网IP:9000*  
- 默认账号是服务器 root 账号

如果上面的说明无法满足您的需求，请参考一下准备步骤：  

## 准备{#prepare}

* [操作云服务器](../user/cloud)：连接服务器和操作云控制台、获取服务器公网IP、开启安全组端口等
* [获取账号密码](../user/credentials)：连接云服务器后，运行获取命令的命令

## 配置域名{#domain}

* [域名五步](../administrator/domain_step)：域名注册、实名制认证、备案、解析、绑定等操作

> 配置域名是可选项，但建议在**初始化向导**之前配置域名，这样可以避免修改应用的 URL。

## 初始化

* [初始化向导](../apps)：本地浏览器访问 *http://服务器公网IP* 可进入初始化向导

## 数据库{#db}

* [管理默认数据库](../user/dbgui)：通过可视化界面管理数据库
* [更换数据库](../administration/db_change)：用户可以将应用预制的数据库更换成其他 RDS

## 安全{#security}

* [配置  HTTPS](../administrator/domain_https)：尽快完成 HTTPS 的设置，保护访问和数据传输安全

## 通知

* [SMTP](../administrator/smtp)：配置 SMTP 以获得正确的电子邮件通知支持

## 备份

* [服务器备份](../administrator/backup_server)：在云控制台设置服务器的自动化备份策略（例如：快照备份）
* [应用备份](../administrator/backup_app)：在应用的控制台设置自动化备份策略（参考每个应用的文档）

## 扩展

* [新增应用](../user/app_create)：预装的应用无法满足需求时，用户还可以很方便的安装更多应用
* [存储扩展](../administrator/storage)：系统盘、数据盘和外部对象存储的扩展

## 升级

* [应用升级](../administrator/upgrade_app)：预装的应用无法满足需求时，参考升级指南
