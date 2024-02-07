---
title: Zentao（禅道）
slug: /zentao
tags:
  - 禅道
  - git
  - 需求
  - 看板
  - 项目管理
---

import Meta from './_include/zentao.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Zentao（禅道） 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。 

1. 访问地址可用，即进入引导首页。根据系统提示，选择语言，然后“开始安装”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-init1-websoft9.png)

3. 接受License许可，安装进入环境检测页面，点击下一步
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-init2-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-init3-websoft9.png)

4. 系统初始化已经设置好数据库参数，点击下一步
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-init4-websoft9.png)

5. 保存配置文件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-init5-websoft9.png)

6. 设置后台账号信息，请务必设置好并牢记之，然后“保存”（建议勾选导入 demo 数据，以便理解系统）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-init6-websoft9.png)

7. 系统完成最后一步安装，提示安装成功
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-init7-websoft9.png)

8. 根据您设置的用户和密码登录后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-init8-websoft9.png)

9. 体验后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-init9-websoft9.png)

10. [注册 ZenTao 官网账号](https://www.zentao.net/user-register.html)，便于后续在线安装插件

### 快速了解

ZenTao 是一个国家化的软件，支持后台切换多语言。  

需要了解更多 ZenTao 的使用，请参考官方文档：

- [ZenTao 开源版手册](https://www.zentao.net/book/zentaopmshelp/40.html)
- [FAQ](https://www.zentao.net/faq.html)
- 命令行：[初始化管理脚本](https://www.zentao.net/book/zentaopmshelp/35.html)
- API：[ZenTao API](https://www.zentao.net/book/api/setting-369.html) 所有请求结果都用 JSON 格式，根据返回结果 status 状态来判断是否请求成功。
- 客户端：手机客户端 IOS 版本和安卓版本， 专为禅道专业版和企业版用户提供。
- [注册](https://www.zentao.net/user-register.html)官网账号，你可以将 ZenTao 系统与官网连接，在线安装插件。
- [企业版、集团办](https://www.zentao.net/page/professional.html)

### 安装插件{#plugin}

ZenTao 提供了 [插件市场](https://www.zentao.net/extension-browse.html) 以方便用户扩展功能

1. 登录后台，打开**插件市场**，搜寻所需的扩展
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-dlplugins-websoft9.png)

2. 点击【下载】，开始安装（安装过程中需要登录 ZenTao 官网）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-installplugin-websoft9.png)

3. 如果是收费插件，需要输入本地电脑的 MAC 地址以验证版权

也可以通过手工安装插件：下载插件，并压缩，然后将目录拷贝到禅道对应的目录，比如 _/zentao/module_

### 集成 Git

参考官方文档：[集成禅道和 Git](https://www.zentao.net/book/zentaopmshelp/207.html)


## 管理维护{#administrator}

### 配置 SMTP{#smtp}

1. 登录禅道，打开：【后台】>【通知】>【邮件】，选择 STMP 作为发信方式

2. 填写准确的 SMTP 设置项信息
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-smtp-websoft9.png)

   - 发送模式选择“SMTP”，加密方式选择“SSL/TLS”;
   - 输入发送方邮箱地址；
   - 认证方式选择“登录”，并勾选“需要认证”选项；
   - 输入 SMTP 服务器地址和 SMTP 服务器的端口号；
   - 输入和发件人邮箱一致的邮箱地址；
   - 输入该邮箱地址的 SMTP 服务的授权码或密码；
   - 存储凭据；

3. 设置完成后，触发消息通知，检验 SMTP 是否正确

### 重置管理员密码{#resetpw}

修改数据库 **zt_user** 表，把对应用户的 password 的值改成 `e10adc3949ba59abbe56e057f20f883e` ，登录密码即重置为：`123456`。


### 备份与恢复

ZenTao 后台提供了非常简单实用的在线备份功能，使用方法如下：

1. 登录 ZenTao 后台，打开：【管理】>【数据】，进入备份页面，设置备份策略。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-backupstr-websoft9.png)

2. 点击备份操作
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-backup-websoft9.png)

3. 在线实现的备份可以在线恢复（还原）

4. ZenTao 提供的回收站功能，也可以恢复手工删除的数据
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-recycle-websoft9.png)

### 升级

请参考官方升级文档 [ZenTao 升级](https://www.zentao.net/book/zentaopmshelp/67.html)


## 故障

#### 密码输入错误多次被锁？

1. 10 分钟后会自动解锁。
2. 管理员登录，组织 → 用户 操作栏里有解锁按钮。