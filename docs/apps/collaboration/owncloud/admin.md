---
sidebar_position: 3
slug: /owncloud/admin
tags:
  - ownCloud
  - 网盘
  - 知识管理
  - 团队协作
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../installation/setup/) 相关章节。

## 场景

### 在线备份

ownCloud 后台提供在线备份功能

1. 登录 ownCloud 后台，安装 **[OwnBackup](https://en.websoft9.com/xdocs/owncloud-image-guide/#using-apps)** 插件
2. 打开：【Admin】>【OwnBackup】，开始备份
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-ownbackup-websoft9.png)
3. 此插件也可以用于恢复
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-restore-websoft9.png)

### 在线升级

ownCloud提供了非常人性化的升级入口，根据系统的更新提示既可以完成主版本、插件的更新。

> 在升级之前请做好服务器的快照备份，这个是必须的步骤，因为谁都无法保证升级100%成功。

#### 插件升级

升级步骤参加如下：

1. 登录 OwnCloud 之后查看右上角是否有更新通知，若有，请点击其中的更新条目
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-updatenotify-websoft9.png)

2. 点击更新条目后 或 访问：*http://域名/index.php/apps/market/#/updates*  进入更新界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-updatelist-websoft9.png)

3. 点击【更新】按钮，系统进入【UPDATING】，耐心等待更新
4. 所有更新完成后，更新清单会显示“所有应用都是最新的”

> 如果升级过程出现问题，例如：无法下载升级包/没有读写权限，请确保网络是通的/OwnCloud目录具有读写权限

#### 主程序升级

主程序升级与插件升级略有差异，具体参考如下：

1. 当有可用升级的程序时，系统提示“ownCloud is available. Get more information ...”
2. 依次打开：Admin->设置->常规，找到更新管理器，若有更新请点击“打开更新管理器”按钮
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-openupdater-websoft9.png)
3. 进入 Updater（更新管理器）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-updater-websoft9.png)
4. 点击【Create a checkpoint】，创建一个核心文件备份
5. 点击【Start】按钮，系统进入自动化升级过程，下载和升级过程比较长，请耐心等待
6. 升级成功提示

> 由于升级过程会下载最新版本，ownCloud的下载服务器在国外，若下载不成功，需要不定期尝试

## 故障速查

####  域名配置后页面显示混乱？

如果先通过 IP 安装，再绑定域名，就会出现这个问题，请分别打开 ownCloud 的 [配置文件](../owncloud#path)，将其中的 IP 地址改成域名。

## 常见问题

#### ownCloud 支持多语言吗？

支持多语言（包含中文）

#### ownCloud 是否提供客户端？

有。包括：ownCloud Desktop Client, ownCloud Android App, ownCloud iOS App

#### ownCloud 可预览和编辑 Office 文档吗？

ownCloud 自身是无法预览和编辑 Office 文档的。但 Websoft9 的部署方案已经安装了文档中间件：[ONLYOFFICE Docs](../owncloud/solution#onlyoffice) 解决此需求。

#### ownCloud 支持集成外部存储吗？

支持多种主流外部存储服务