---
sidebar_position: 1
slug: /drupal
tags:
  - Drupal
  - CMS
  - 建站系统
---

# 快速入门

[Drupal](https://www.drupal.org) 是一个 100% 开源的老牌建站系统（CMS），社区生态健康，占据全球 3% 的 CMS 市场。Drupal 自定义权限、页面类型灵活，默认支持多语言，是的其开发的站点具备良好的扩展能力。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-gui-websoft9.png)


## 准备

部署 Websoft9 提供的 Drupal 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Drupal 的 **[默认账号和密码](./setup/credentials)**  
4. 若想用域名访问  Drupal **[域名五步设置](./administrator/domain_step)** 过程


## Drupal 初始化向导

### 详细步骤

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入引导页

2.  选择一门语言，进入下一步
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-install001-websoft9.png)

3.  选择一种安装方式，进入下一步
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-install002-websoft9.png)

4.  填写您的数据库参数（[查看数据库账号密码](./setup/credentials)），保存并继续;
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-install003-websoft9.png)

5.  分别完成网站安装和翻译安装
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-install004-websoft9.png)

6.  设置网站信息。站点维护账号及后台账号，请务必设置好并牢记之。进入下一步
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-install005-websoft9.png)

7.  系统完成最后一步安装

8.  进入Drupal后台，体验完整功能
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-backend-websoft9.png)

> 需要了解更多 Drupal 的使用，请参考官方文档：[Drupal Community Guides](https://www.drupal.org/documentation)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。


## Drupal 使用入门

下面以 **使用 Drupal 构建内容管理系统** 作为一个任务，帮助用户快速入门：


## Drupal 常用操作

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数

2. 获取 [SMTP Authentication Support](https://www.drupal.org/project/smtp) 下载链接（Drupal 默认没有安装 SMTP 模块），在线安装
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-installsmtp-websoft9.png)

3. 打开：【管理】>【扩展】，找到【SMTP Authentication Support】，点击【Install】完成最终安装步骤
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-installsmtp002-websoft9.png)

4. 打开：【管理】>【配置】，找到【SMTP Authentication Support】，配置它
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-setsmtp-websoft9.png)

5. 填写准确的 SMTP 设置项信息
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-smtp-4-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-smtp-5-websoft9.png)

    * 发送模式选择“SMTP”，加密方式选择“SSL/TLS”;
    * 输入发送方邮箱地址；
    * 认证方式选择“登录”，并勾选“需要认证”选项；
    * 输入SMTP服务器地址和SMTP服务器的端口号；
    * 输入和发件人邮箱一致的邮箱地址；
    * 输入该邮箱地址的SMTP服务的授权码或密码；
    * 存储凭据；

6. 设置完成后，勾选【启用调试】，将发出测试邮件
     

### 更换域名

如果 Drupal 需要更换域名，除[ Drupal 配置文件](#path)之外，还需修改 Drupal 根目录下 `.htaccess` 中域名有关的值。  

### 设置多语言{#setlang}

Drupal 支持多语言，下面是安装并设置多语言的主要步骤：

1. 登录 Drupal，在后台 【管理】>【配置】>【地区和语言】中安装语言
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-addlanguage-websoft9.png)

2. 安装新语言后，根据实际需要，设置默认语言

### 安装扩展{#plugin}

Drupal 提供的 [Drupal Modules](https://www.drupal.org/project/project_module)包含大量的扩展，下面介绍如何安装它们

1. 打开 [Drupal Modules](https://www.drupal.org/project/project_module)网站，搜寻所需的扩展
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-searchformodule-websoft9.png)

2. 获取扩展的下载地址
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-dlmodule-websoft9.png)

3. 登录 Drupal 后台，打开安装扩展的界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-extend-websoft9.png)

4. 通过输入下载地址，在线安装扩展
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-installsmtp-websoft9.png)

5. 安装完成
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-moduleinstalled-websoft9.png)

6. 最后，需要到模块管理中启用刚安装的插件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-enablemodule-websoft9.png)

### 安装主题{#theme}

Drupal 提供的 [Drupal Themes](https://www.drupal.org/project/project_theme) 包含大量的主题，下面介绍如何安装它们

1. 打开 [Drupal Themes](https://www.drupal.org/project/project_theme) 网站，搜寻所需的主题
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-searchthemes-websoft9.png)

2. 获取主题的下载地址
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-themesurl-websoft9.png)

3. 打开 【扩展管理】>【安装扩展】，输入下载地址，开始安装
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-installsmtp-websoft9.png)

4. 安装后，打开【外观】，找到已经在线安装的主题，启用它
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-themeenable-websoft9.png)

> 有些模板提供商，提供的模板压缩包中包含 Drupal 内核文件，这种情况下 **安装模板=安装Drupal**

### 重置密码{#resetpwd}

Drupal 官方提供了重置管理员密码的[详细方案](https://www.drupal.org/node/44164) 。


## 参数{#parameter}

Drupal 应用中包含  Nginx, Apache, Docker, MySQL, PHP 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 Drupal 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Drupal 本身的参数：

### 路径{#path}

Drupal 安装目录： */data/wwwroot/drupal*  
Drupal 配置文件： */data/wwwroot/drupal/web/sites/default/settings.php*  


### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 8080   | Drupal 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


### 版本{#version}

登录控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats drupal
```

### 命令行{#cli}

社区为 Drupal 提供了一个[第三方 CLI](https://drupalconsole.com/) 工具

### API

[Drupal APIs](https://www.drupal.org/docs/drupal-apis)