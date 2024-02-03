---
title: Typo3
slug: /typo3
tags:
  - CMS
  - 内容管理
  - 企业建站
---

import Meta from './_include/typo3.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Typo3 后，通过【我的应用】进入它的编辑窗口，在**访问**标签页中获取登录地址和账号。  

1. 进入安装向导后，系统进入环境检测步骤通过后，填写数据库参数
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-installdb-websoft9.png)

2. 数据库连接成功后，系统提示选择一个已有数据库或创建一个新的数据库（推荐前者）

3. 设置管理账号和站点信息  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-installsetadmin-websoft9.png)

4. 完成安装后登录后台

### 快速了解

Typo3 拥有非常全面的命令行功能：  

- CLI
  * typo3 -- 官方核心命令行
  * typo3cms -- 第三方扩展命令

- [API](https://api.typo3.org/)
- 多语言：[Changing The Backend Language](https://docs.typo3.org/m/typo3/tutorial-getting-started/main/en-us/Setup/BackendLanguages.html#backendlanguages)

### 扩展管理

TYPO3 CMS 提供大量扩展，以增强系统功能。

1. 登录 Typo3后台，打开【ADMIN TOOLS】> 【Extensions】
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-BackendExtensionManager-websoft9.png)

2. 顶部下拉菜单中选择【Get extensions】查看扩展
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-BackendExtensionManagerInstall-websoft9.png)

3. 安装、更新扩展  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-BackendExtensionManagerExtensionVersions-websoft9.png)

### 模板管理

TYPO3 CMS 的模板管理非常细致，能够对模板最小元素进行细微的设置

1. 登录 Typo3后台，打开【WEB】>【Template】
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-template-websoft9.png)

2. 配置模板


## 管理维护{#administrator}

### 升级

Typo3 后台提供了在线升级功能，升级非常容易：

1. 登录 Typo3后台，打开【ADMIN TOOLS】> 【Upgrade】
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-upgrade-websoft9.png)
   
2. 根据升级向导开始升级


## 故障
