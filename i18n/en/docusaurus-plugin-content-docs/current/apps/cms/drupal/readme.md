---
sidebar_position: 1
slug: /drupal
tags:
  - Drupal
  - CMS
  - 建站系统
---

# Drupal Getting Started

[Drupal](https://www.drupal.org/)  is content management software. It’s used to make many of the websites and applications you use every day. Drupal has great standard features, like easy content authoring, reliable performance, and excellent security. But what sets it apart is its flexibility; modularity is one of its core principles. Its tools help you build the versatile, structured content that dynamic web experiences need.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-gui-websoft9.png)


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. **[Get](./user/credentials)** default username and password of Drupal
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Drupal
 

## Drupal Initialization

### Steps for you

1. Using browser to access URL: *https://domain* or *https://Server's Internet IP*, start to install  

2. Choose a language, go to next step 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/dp01.png)

3. Select an installation profile 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/dp02.png)

3. Then configure the database connection information([Don't know password?](./user/credentials))
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/dp03.png)

5. Wait for installing
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/dp04.png)

6. Set your administrator account for Drupal
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/dp05.png)

7. Installed successfully
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/dp07.png)

> More useful Drupal guide, please refer to [Drupal Documentation](https://www.drupal.org/documentation)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Drupal QuickStart

下面以 **使用 Drupal 构建内容管理系统** 作为一个任务，帮助用户快速入门：

## Drupal Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console  

2. Copy [SMTP Authentication Support](https://www.drupal.org/project/smtp) plugin URL and install it
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-installsmtp001-websoft9.png)

3. Open:【Manage】>【Extend】, select【SMTP Authentication Support】and click 【install】 button
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-installsmtp002-websoft9.png)

4. Open:【Manage】>【Configuration 】, click【SMTP Authentication Support】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-setsmtp001-websoft9.png)

5. Set the SMTP configuration items
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-setsmtp002-websoft9.png)
   
    * 发送模式选择“SMTP”，加密方式选择“SSL/TLS”;
    * 输入发送方邮箱地址；
    * 认证方式选择“登录”，并勾选“需要认证”选项；
    * 输入SMTP服务器地址和SMTP服务器的端口号；
    * 输入和发件人邮箱一致的邮箱地址；
    * 输入该邮箱地址的SMTP服务的授权码或密码；
    * 存储凭据；

6. Select【Enable debugging】when complete setting and will send test mail

4. Test it

### DNS Additional Configure (Modify URL){#dns}

如果 Drupal 需要更换域名，除[ Drupal 配置文件](#path)之外，还需修改 Drupal 根目录下 `.htaccess` 中域名有关的值。

### Set languages{#setlang}

Drupal supports multiple languages. Here are the main steps to install and set up multiple languages:

1. Log in Drupal, go to【Manage】>【Configuration】>【Regional and Language】, install your languge
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-addlanguage-websoft9.png)

2. After installing a new language, set the default language according to actual needs.

### Install plugin{#installplugin}

[Drupal Modules](https://www.drupal.org/project/project_module) have lots of Modules, below is the step for you to install it

1. Visit [Drupal Modules](https://www.drupal.org/project/project_module) website, and search the Module you want to use
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-searchformodule-websoft9.png)

2. Get the dowload URL of your Module
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-dlmodule-websoft9.png)

3. Log in Drupal,open the Extend installation interface  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-extend-websoft9.png)

4. Go to【Mange】>【Extend】>【Install Extend】, input the URL for Extend installation  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-install_manager_module-websoft9.png)

5. Install successfully
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-moduleinstalled-websoft9.png)

6. At last, enable the Theme you have installed online
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-enablemodule-websoft9.png)

### Install Themes{#theme}

[Drupal Themes](https://www.drupal.org/project/project_theme) have lots of Themes, below is the step for you to install it

1. Visit [Drupal Themes](https://www.drupal.org/project/project_theme) website, and search the Theme you want to use
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-searchthemes-websoft9.png)

2. Get the dowload URL of your Theme
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-themesurl-websoft9.png)

3. Open【Mange】>【Extend】>【Install Extend】, input the URL for Extend installation 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-install_manager_module-websoft9.png)

4. Then, open【Appearance】 page, enable the Theme you have installed online
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/drupal/drupal-completeinstall-theme-websoft9.png)

> Some Themes's zip package may have the Drupal core, at this time **Install Theme= Install Drupal**

### Reset password{#resetpwd}

If you don't remember your administrator password, please refer to the docs [here]((https://www.drupal.org/node/44164)) to reset it

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Drupal

通过运行`docker ps`，可以查看到 Drupal 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

### Path{#path}

Drupal installation directory: */data/wwwroot/drupal*  
Drupal configuration file: */data/wwwroot/drupal/web/sites/default/settings.php*

### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 3306 | Remote connect MySQL | Optional |
| 80 | HTTP requests for Drupal | Required |
| 443 | HTTPS requests Drupal | Optional |
| 9090 | HTTP request for phpMyAdmin | Optional |


### Version{#version}

登录控制台查看

### Service{#service}

```shell
sudo docker start | stop | restart | stats drupal
```

### CLI{#cli}

社区为 Drupal 提供了一个[第三方 CLI](https://drupalconsole.com/) 工具

### API

[Drupal APIs](https://www.drupal.org/docs/drupal-apis)