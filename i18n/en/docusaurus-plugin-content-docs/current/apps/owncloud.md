---
title: OwnCloud
slug: /owncloud
tags:
  - ownCloud
  - 网盘
  - 知识管理
  - 团队协作
---

import Meta from './_include/owncloud.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 OwnCloud 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 本地浏览器访问成功后，进入引导首页
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-init1-websoft9.png)

2. 填写账号密码后成功登陆到后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-installcomplete-websoft9.png)

### 设置语言

登录 ownCloud，在后台 【Personal】>【General】中设置语言

  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-zh-websoft9.png)

### 安装扩展

ownCloud [Marketplace](https://marketplace.owncloud.com/) 包含大量的扩展（也叫apps），下面介绍如何安装它们

1. 访问 [Marketplace](https://marketplace.owncloud.com/) ，搜索所需的应用（以 OwnBackup 为例）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-searchapps-websoft9.jpg)

2. 下载并解压  

3. 上传到 ownCloud 应用目录：/var/lib/docker/volumes/owncloud_owncloud/_data/apps，并通过chown 命令，改变扩展目录（如 ownbackup）的拥有者和关联组用户为 www-data
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-ftp-websoft9.png)

4. 启用 OwnBackup  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-enableapps-websoft9.png)

> 除了下载安装之外，也可以通过 ownCloud 后台在线安装 Marketplace 应用


### 连接外部存储{#oss}

ownCloud 支持多种流行的企业存储服务，具体使用步骤如下：

1. 登录 ownCloud 后台，安装 **External storage support** 扩展
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-enablestorage-websoft9.png)

2. 打开：【Admin】>【Add storage】>【External Storage】，选择一个外部存储服务
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-enablestorage002-websoft9.png)

3. 根据实际情况进行设置
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-auth_mechanism-websoft9.png)

更多详情参考官方文档：[External Storage](https://doc.owncloud.org/server/admin_manual/configuration/files/external_storage/index.html)

### 数据转移

ownCloud 的程序和数据迁移主要包括两个步骤：

1. 数据从源目录复制（移动）到目标目录
2. 连接到 ownCloud 容器，运行 `occ files:scan --all`命令，重建索引后生效

## 配置选项{#configs}

- 支持第三方存储（√）
- 多语言（√）
- 移动端：OwnCloud Desktop Client, OwnCloud Android App, OwnCloud iOS App
- 文档编辑与预览：需集成 ONLYOFFICE Docs 等第三方中间件实现
- 配置文件：/path/data/ownCloud/config/config.php
- [ownCloudcmd](https://doc.ownCloud.com/desktop/next/advanced_usage/command_line_client.html)
- [API](https://doc.ownCloud.com/server/next/developer_manual/core/apis/provisioning-api.html)

## 管理维护{#administrator}

1. 登录OwnCloud后，打开【admin】>【设置】>【个人】>【常规】，填写发件邮箱地址
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-smtp-1-websoft9.png)

2. 打开【设置】>【管理】>【常规】，依次填写 SMTP 信息
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-smtp-2-websoft9.png)

    * 发送模式选择“SMTP”，加密方式选择“SSL/TLS”;
    * 输入发送方邮箱地址；
    * 认证方式选择“登录”，并勾选“需要认证”选项；
    * 输入SMTP服务器地址和SMTP服务器的端口号；
    * 输入和发件人邮箱一致的邮箱地址；
    * 输入该邮箱地址的SMTP服务的授权码或密码；
    * 存储凭据；

3. 点击“发送邮件”即可测试SMTP是否设置正确。

### 修改 URL{#dns}

Websoft9 提供的 Owncloud 已经将 URL 设置为通配符，即域名的更改不会影响其访问。  

### 在线备份

OwnCloud 后台提供在线备份功能

1. 登录 OwnCloud 后台，安装 **[OwnBackup](https://en.websoft9.com/xdocs/owncloud-image-guide/#using-apps)** 插件

2. 打开：【Admin】>【OwnBackup】，开始备份
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-ownbackup-websoft9.png)

3. 此插件也可以用于恢复
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-restore-websoft9.png)

### 在线升级

OwnCloud提供了非常人性化的升级入口，根据系统的更新提示既可以完成主版本、插件的更新。

#### 插件升级

升级步骤参加如下：

1. 登录 OwnCloud 之后查看右上角是否有更新通知，若有，请点击其中的更新条目
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-updatenotify-websoft9.png)

2. 点击更新条目后 或 访问：*http://域名/index.php/apps/market/#/updates*  进入更新界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-updatelist-websoft9.png)

3. 点击【更新】按钮，系统进入【UPDATING】，耐心等待更新

#### 主程序升级

1. 当有可用升级的主程序时，系统提示“OwnCloud is available. Get more information ...”

2. 依次打开：Admin->设置->常规，找到更新管理器，若有更新请点击“打开更新管理器”按钮
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-openupdater-websoft9.png)

3. 进入 Updater（更新管理器），根据指引开始升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-updater-websoft9.png)


## 故障

#### 更改域名导致无法访问 OwnCloud ？

#### 访问 OwnCloud 出现 502 错误？{#502}