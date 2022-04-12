---
sidebar_position: 1
slug: /zentao
tags:
  - ZenTao（禅道）
  - 项目管理
---

# 快速入门

[ZenTao（禅道）](https://www.zentao.net) 是优秀的研发项目管理软件[（演示）](http://demo.zentao.net/)。它细分需求、任务、缺陷和用例，完整覆盖了研发项目管理的核心流程。禅道管理思想注重实效，功能完备丰富，操作简洁高效，界面美观大方，搜索功能强大，统计报表丰富多样。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-gui-websoft9.png)

## 准备

部署 Websoft9 提供的 ZenTao 之后，请参考下面的步骤快速入门。

1. 在云控制台获取您的 **服务器公网 IP 地址**
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 在服务器中查看 ZenTao 的 **[默认账号和密码](./user/credentials)**
4. 若想用域名访问 ZenTao，务必先完成**[域名五步设置](./administrator/domain_step)** 过程

## ZenTao 初始化向导

### 详细步骤

1. 使用本地浏览器访问网址： *http://域名* 或 *http://服务器公网IP*, 就进入引导首页

2. 根据系统提示，选择语言，然后“开始安装”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-install001-websoft9.png)

3. 安装进入环境检测页面，点击下一步
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-install002-websoft9.png)

4. 填写您的数据库参数（[查看数据库账号密码](./user/credentials)）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-install003-websoft9.png)

5. 设置后台账号信息，请务必设置好并牢记之，然后“保存”（建议勾选导入 demo 数据，以便理解系统）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-install005-websoft9.png)

6. 系统完成最后一步安装，登录到禅道管理系统，体验并测试系统功能
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-install006-websoft9.png)

7. 登录后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-login-websoft9.png)

8. 体验后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-gui-websoft9.png)

9. [注册 ZenTao 官网账号](https://www.zentao.net/user-register.html)，便于后续在线安装插件

> 需要了解更多 ZenTao 的使用，请参考官方文档：[ZenTao 开源版手册](https://www.zentao.net/book/zentaopmshelp/40.html) 和 [FAQ](https://www.zentao.net/faq.html)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或 **[FAQ](./faq#setup)** 尝试快速解决问题。

## ZenTao 常用操作

### 配置 SMTP

ZenTao 配置 SMTP 发邮件的步骤：

1. 在邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数

2. 登录禅道，打开：【后台】>【通知】>【邮件】，选择 STMP 作为发信方式

3. 填写准确的 SMTP 设置项信息
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-smtp-websoft9.png)

   - 发送模式选择“SMTP”，加密方式选择“SSL/TLS”;
   - 输入发送方邮箱地址；
   - 认证方式选择“登录”，并勾选“需要认证”选项；
   - 输入 SMTP 服务器地址和 SMTP 服务器的端口号；
   - 输入和发件人邮箱一致的邮箱地址；
   - 输入该邮箱地址的 SMTP 服务的授权码或密码；
   - 存储凭据；

4. 设置完成后，触发消息通知，检验 SMTP 是否正确

### 配置多语言

ZenTao 支持多语言，直接到后台切换即可。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-changelanguage-websoft9.png)

### 安装插件

ZenTao 提供了 [插件市场](https://www.zentao.net/extension-browse.html) 以方便用户扩展功能

1. 登录后台，打开**插件市场**，搜寻所需的扩展
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-dlplugins-websoft9.png)

2. 点击【下载】，开始安装（安装过程中需要登录 ZenTao 官网）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-installplugin-websoft9.png)

3. 如果是收费插件，需要输入本地电脑的 MAC 地址以验证版权

也可以通过手工安装插件：下载插件，并压缩，然后将目录拷贝到禅道对应的目录，比如 _/zentao/module_

### 重置管理员密码

禅道管理员密码忘记了，怎么找回？ 使用 phpMyAdmin 登录禅道数据库 **zt_user** 表，找到用户的记录，把 password 的值改成 `e10adc3949ba59abbe56e057f20f883e` ，登录密码重置为：`123456`。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-recoverpw-websoft9.png)

### ZenTao 集成 Git

参考官方文档：[集成禅道和 Git](https://www.zentao.net/book/zentaopmshelp/207.html)

## ZenTao 参数

ZenTao 应用中包含 PHP, Apache, Docker, MySQL, phpMyAdmin 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。

下面仅列出 ZenTao 本身的参数：

### 路径{#path}

ZenTao 安装目录： */data/wwwroot/zentao*  
ZenTao 配置文件： */data/wwwroot/zentao/config/my.php*

### 端口{#port}

无特殊端口

### 版本

```shell
# ZenTao Version
cat /data/wwwroot/zentao/VERSION
```

### 服务

```shell
sudo docker start | stop | restart | stats zentao
```

### 命令行

ZenTao 提供了一套命令操作，详情参考官方文档：[初始化管理脚本](https://www.zentao.net/book/zentaopmshelp/35.html)

### API

[ZenTao API](https://www.zentao.net/book/api/setting-369.html) 所有请求结果都用 JSON 格式，根据返回结果 status 状态来判断是否请求成功。
