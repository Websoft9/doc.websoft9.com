---
title: Nextcloud
slug: /nextcloud
tags:
  - 网盘
  - 知识管理
  - 团队协作
---

import Meta from './_include/nextcloud.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Nextcloud 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

1. 使用本地电脑浏览器，进入引导首页
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-wizard-websoft9.png)
   
2. 设置用户名和密码并牢记，点击【安装】，安装完成后提示可继续安装插件，根据需求选择安装或者跳过    
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-plugin-websoft9.png)

3. 关闭弹窗，开始体验后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-main-websoft9.png)

4. 进入Marketplace，扩展更多的功能
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-app-websoft9.png)

### 文档预览与编辑

#### 集成 Nextcloud Office

Nextcloud 内置 Nextcloud Office（基于 Collabora Online 开发版，简称 CODE）。 

只需安装 CODE 插件，即可启用内置的 CODE 服务器，实现文档编辑与预览。

#### 集成 ONLYOFFICE Docs

Nextcloud 也支持集成第三方文档服务器，下面介绍集成 OnlyOffice Docs 的详细使用方案：

1. 登陆到 Websoft9 控制台的“应用商店”，安装 OnlyOffice Docs

2. 登录到 Nextcloud ，单击右上角上角齿轮图标，点击【应用】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-olpreview-1-websoft9.png)

3. 找到【ONLYOFFICE】插件，安装并启用它

4. 安装完成后，找到**设置**页面，对 ONLYOFFICE 进行如图所示的设置（[参考官方文档](https://api.onlyoffice.com/editors/nextcloud)）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-setonlyoffice-websoft9.png)

   > 图中涂抹处应修改为 ONLYOFFICE Docs 的 ** HTTPS URL** 

5. 返回到首页，刷新或重新登录，然后单击 Office 文件即可在线预览和编辑。

### 在线安装扩展

Nextcloud 后台集成了 [Marketplace](https://apps.nextcloud.com) 大量的扩展（也叫apps），下面介绍如何安装它们

1. 登录 Nextcloud，在后台 【应用】>【应用软件包】中寻找所需的应用
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-backendmk-websoft9.png)

2. 在线安装它

### 手工安装扩展{#minstallplugin}

网络问题可能会导致无法在线安装扩展，此时就需要手工安装（下面以 ONLYOFFICE 为例）：

1. 到 Nextcloud [官方应用商店](https://apps.nextcloud.com/apps/onlyoffice/releases?platform=22#22)找到下载路径

2. docker exec 到容器，下载并解压到扩展目录，并注意**修改文件夹权限**与其他插件一致。

3. 登录 Nextcloud 后台，进入应用中心，启用扩展

### 连接 WebDAV

NextCloud 支持 WebDAV 协议，用户可以通过 WebDAV 来连接并同步文件，比如在 Windows10 系统映射磁盘到 NextCloud，用于本地访问云盘文档。

1. 登录 NextCloud，点击【文件】>【设置】，获取 WebDav URL
   > 注意：每个用户都有自己的 URL，使用对应的 URL 和用户名登录才能正确访问文件

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-webdavurl-websoft9.jpg)

2. 在本地 Windows 电脑配置 [WebDAV as a Network Drive in Windows 11/10](https://www.thewindowsclub.com/how-to-map-webdav-in-windows)

### 连接外部存储{#oss}

Nextcloud 支持多种流行的企业存储服务，具体使用步骤如下：

1. 登录 Nextcloud 后台，通过 **应用** 管理，启用 **External storage support** 扩展
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-enablestorage-websoft9.png)

2. 打开：【管理设置】>【外部存储】>【Add storage】>【External Storage】，选择一个外部存储服务。选择S3能兼容目前大多数对象存储工具，如S3,OSS,OBS等。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-enablestorage002-websoft9.png)

3. 根据实际情况配置，连接到相应的对象存储。使用云平台的秘钥对连接成功后，会在 Nextcloud 中生成对应的外部存储目录。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-auth_mechanism-websoft9.png)

### 设置语言

登录 Nextcloud，在后台 【个人】>【个人信息】中设置语言

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-mylanguage-websoft9.png)

## 配置选项{#configs}

- CLI：`occ` 命令是 Nextcloud 的命令行界面。可以安装和升级 Nextcloud，管理用户，密码管理等。 
- 配置文件：/path/config/config.php
- SMTP（✅）
- [User Authentication with LDAP](https://docs.nextcloud.com/server/latest/admin_manual/configuration_user/user_auth_ldap.html)
- 多语言（✅）
- [主流外部存储服务](https://docs.nextcloud.com/server/latest/admin_manual/configuration_files/external_storage_configuration_gui.html#storage-configuration)：Amazon S3、Dropbox、FTP、Google Drive、SMB、WebDAV、SFTP等
- 移动端（✅）：Nextcloud Desktop Client, Nextcloud Android App, Nextcloud iOS App
- Nextcloud 与 ownCloud：Nextcloud 是由 ownCloud 创始人带来开源社区其他人创建的一个分支项目，类似 MariaDB 与 MySQL 的关系
- [Basic APIs](https://docs.nextcloud.com/server/latest/developer_manual/client_apis/WebDAV/basic.html)

## 管理维护{#administrator}

### 数据转移

Nextcloud 数据迁移主要是将数据目录移动或复制到其他的存储中，转移过程主要是文件操作。  

此处提醒需要注意的，完全数据迁移后，需要运行 `occ files:scan --all` 重建索引

### 修改 URL{#dns}

Websoft9 提供的 Nextcloud 已经将 URL 设置为通配符，即域名的更改不会影响其访问。  

如果不想使用通配符，可以在配置文件中修改 overwrite.cli.url 的值

   ```
   'overwrite.cli.url' => 'nextcloud.yourdomain.com', # 修改为新域名
   ```

### 配置 SMTP{#smtp}

1. 登录 Nextcloud 后，点击齿轮图标，打开【个人】设置页面，填写发件邮箱地址
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-smtp-2-websoft9.png)

2. 点击【其他设置】>【电子邮件服务器】，依次填写 SMTP 信息
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-smtp-1-websoft9.png)

    * 发送模式选择“SMTP”，加密方式选择“SSL/TLS”;
    * 输入发送方邮箱地址；
    * 认证方式选择“登录”，并勾选“需要认证”选项；
    * 输入SMTP服务器地址和SMTP服务器的端口号；
    * 输入和发件人邮箱一致的邮箱地址；
    * 输入该邮箱地址的SMTP服务的授权码或密码；
    * 存储凭据；

3. 点击“发送邮件”即可测试SMTP是否设置正确。

### 在线备份

Nextcloud 后台提供在线备份功能

1. 登录 Nextcloud 后台，安装 **[OwnBackup](https://apps.nextcloud.com/apps/ownbackup)** 插件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-backupapps-websoft9.png)
2. 打开：【Admin】>【Additional settings】>【OwnBackup】，开始备份
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-backupapp002-websoft9.png)

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

> 由于升级过程会下载最新版本，Nextcloud 的下载服务器在国外，若下载不成功，需要不定期尝试

#### 插件升级

升级步骤参加如下：

1. 登录 Nextcloud 后台，进入【应用】，在应用列表中找到需更新的应用
   ![Nextcloud 升级](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-updatelist-websoft9.png)

2. 点击【更新】按钮，耐心等待更新

3. 所有更新完成后，更新清单会显示“所有应用都是最新的”

> 如果升级过程出现问题，例如：无法下载升级包/没有读写权限，请确保网络是通的/Nextcloud目录具有读写权限


## 故障

#### 关闭 ONLYOFFICE 证书验证？

Nextcloud 若为 HTTPS 访问，则ONLYOFFICE 也需 HTTPS，否则连接异常。    

可以通过 Nextcloud 后台插件中设置 或 配置文件中增加下面一段关闭证书验证：  

```
'onlyoffice' =>
array (
'verify_peer_off' =>TRUE,
), 
```

#### 网络超时导致无法安装扩展？

请手工下载后安装
