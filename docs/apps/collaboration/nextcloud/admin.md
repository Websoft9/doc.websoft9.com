---
sidebar_position: 3
slug: /nextcloud/admin
tags:
  - Nextcloud
  - 网盘
  - 知识管理
  - 团队协作
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### 在线备份

Nextcloud 后台提供在线备份功能

1. 登录 Nextcloud 后台，安装 **[OwnBackup](https://apps.nextcloud.com/apps/ownbackup)** 插件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-backupapps-websoft9.png)
2. 打开：【Admin】>【Additional settings】>【OwnBackup】，开始备份
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-backupapp002-websoft9.png)

### 手工升级

有时候由于网络问题，上面的基于升级界面的升级会由于网络下载速度太慢，导致升级失败。  

此时，可以考虑采用如下的手工升级方案：

1. 将 Nextcloud 的 data, config, apps 目录临时复制到服务器其他目录下

2. 上传 Nextcloud 安装目录下的所有文件
   ```
   rm -rf /data/wwwroot/nextcloud/*
   ```
3. 将本地下载的 Nextcloud 源码（除 config, apps 目录之外）上传到 /data/wwwroot/nextcloud 目录

4. 将第1步备份的几个目录还原到 */data/wwwroot/nextcloud* 中

5. 使用 *php occ* 命令进行升级处理
   ```
   cd /data/wwwroot/nextcloud
   php occ upgrade
   ```

6. 登录到 Nextcloud 后台界面，启用所需的插件

7. 手工升级完成

### 在线升级

Nextcloud 提供了非常人性化的升级功能，根据系统的更新提示既可以完成主版本、插件的更新。

> 在升级之前请做好服务器的快照备份，这个是必须的步骤，因为谁都无法保证升级100%成功。

#### 主程序升级

主程序升级与插件升级略有差异，具体参考如下：

1. 登录 Nextcloud 后台，进入【管理】>【基本设置】，若有更新请点击【打开更新管理器】按钮
   ![Nextcloud 升级](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-openupdater-websoft9.png)

2. 进入 Updater（更新管理器）
   ![Nextcloud 升级](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-updater-websoft9.png)

3. 点击【Start update】开始更新

4. 系统进入自动化升级过程，下载和升级过程比较长，请耐心等待

> 由于升级过程会下载最新版本，Nextcloud的下载服务器在国外，若下载不成功，需要不定期尝试

#### 插件升级

升级步骤参加如下：

1. 登录 Nextcloud 后台，进入【应用】，在应用列表中找到需更新的应用
   ![Nextcloud 升级](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-updatelist-websoft9.png)

2. 点击【更新】按钮，耐心等待更新

3. 所有更新完成后，更新清单会显示“所有应用都是最新的”

> 如果升级过程出现问题，例如：无法下载升级包/没有读写权限，请确保网络是通的/Nextcloud目录具有读写权限

## 故障排除

####  域名配置后页面显示混乱？

如果先通过 IP 安装，再绑定域名，就会出现这个问题，请分别打开 Nextcloud 的 [配置文件](../nextcloud#path)，将其中的 IP 地址改成域名。

#### 网络超时导致无法安装插件？

采用[手工安装](../nextcloud#minstallplugin)方式

## 常见问题

#### Nextcloud 支持多语言吗？

支持多语言（包含中文）

#### Nextcloud 与 ownCloud 有什么关系？

Nextcloud 是由 ownCloud 创始人带来开源社区其他人创建的一个分支项目，类似 MariaDB 与 MySQL 的关系

#### Nextcloud 是否提供客户端？

有。包括：Nextcloud Desktop Client, Nextcloud Android App, Nextcloud iOS App

#### Nextcloud 可预览和编辑 Office 文档吗？

Nextcloud 自身是无法预览和编辑 Office 文档的。但 Websoft9 的部署方案已经安装了文档中间件：[ONLYOFFICE Docs](../nextcloud/solution#onlyoffice) 解决此需求。

#### Nextcloud 支持集成外部存储吗？

支持多种[主流外部存储服务](https://docs.nextcloud.com/server/latest/admin_manual/configuration_files/external_storage_configuration_gui.html#storage-configuration)