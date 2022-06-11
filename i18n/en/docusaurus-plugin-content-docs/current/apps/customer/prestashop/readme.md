---
sidebar_position: 1
slug: /prestashop
tags:
  - PrestaShop
  - eCommerce
---

# PrestaShop Getting Started

[PrestaShop](https://prestashop.com) is one of the world's most popular ecommerce platforms, and most successful open source projects. It is a company and a global community.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/pretashopui-websoft9.png)  

If you have installed Websoft9 PrestaShop, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** on your Cloud Platform
2. Check you **[Inbound of Security Group Rule](https://support.websoft9.com/docs/faq/tech-instance.html)** of Cloud Console to ensure the **TCP:80** is allowed
3. **[Get](./user/credentials)** default username and password of PrestaShop  
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for PrestaShop

## PrestaShop Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *https://domain* or *https://Internet IP*, start to install    
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/ps01.png)

2. Agree license, Click "Next"
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/ps02.png)

3. Set your store information and administration account, Click "Next"
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/ps03.png)
   
   > Email is your login ID, not collected by anyone because it stored in your Cloud Server

4. Database connection configuration, you can use the MySQL in this Server([Don's know password?](/stack-accounts.html#mysql)), and you can use other database services
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/ps04.png)

5. Installation is finished
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/ps05.png)

6. Please delete */data/wwwroot/prestashop/install* folder by SSH
   ```
   rm -rf /data/wwwroot/prestashop/install
   ```
7. Click "Manage your store" to enter your administration account, Click "Login IN"
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/ps07.png)

8. This is your administration console
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/ps08.png)

9. Use *http://IP*  to go to your index page.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/ps09.png)

> Refer to [PrestaShop Docs](https://www.prestashop.com/en/resources/documentations) to get more details

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## PrestaShop QuickStart

下面以 **使用 PrestaShop 构建在线商城** 作为一个任务，帮助用户快速入门：

## PrestaShop Setup

### PrestaShop Modules

Modules is a very import function for PrestaShop to extend the business requirement

1. Log in PrestaShop console,
2. Open:【Modules】>【Module Catalog】, find the module you want to install and click the【Install】button
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-installmd-websoft9.png)
3. Open:【Modules】>【Module Manager】, find the module you want to upgrade and click the【Upgrade】button
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-upgrademodules-websoft9.png)

### Prestashop connect Marketplace

Completed installation of PrestaShop, suggest you make your PrestaShop system connect PrestaShop's Marketplace. Once you have connected it, you can use many resourses on Marketplace.

1. Log in PrestaShop Console as administrator
2. Open 【Modules】>【Module Manager】, click【Connect to Addons marketplace】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-connectmk-websoft9.png)  
3. Register an account if you don't have it
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-registeraccount-websoft9.png)  
4. Connect to Marketplace using your Marketplace's account
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/prestashop-marketplace-websoft9.png)

### PrestaShop language

Prestashop's multi-language support is very mature. The system has a multi-language system built in the background. You only need to select the corresponding language and import it online to your PrestaShop system.

##### Import language

1. Log in PrestaShop console, open:【International】>【Localization】>【language】, enter the interface of language settings
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/prestashop-local-websoft9.png)
2. Select the language you want to use and click【import】 icon to import online
3. Click 【language】 tab, you can see all language packages been installed successfully
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/prestashop-alllanguage-websoft9.png) 

> When add new language for PrestaShop, it will add redirects rules in the  `.htaccess` file of PrestaShop root directory.

##### Delete language

1. Log in PrestaShop console, open:【International】>【Localization】>【language】,edit your language
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/prestashop-dellanguage001-websoft9.png)
2. Set the Status to 【No】
3. Click 【language】 tab, you can delete the language you have disabled
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-dellanguage002-websoft9.png)

### PrestaShop Maintenance mode

Log in PrestaShop console, open:【Shop Parameters】>【General】>【Maintenance】
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-mantmode-websoft9.png)

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console
  
2. Log in PrestaShop console as administrator, configure SMTP  
  
   - Open:【Advanced Parameters】>【Email】,selecting 【Set my own SMTP parameters】
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/prestashop-smtp001-websoft9.png)
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/prestashop-smtp002-websoft9.png)
   - Fill in your correct SMTP information
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/prestashop-smtp003-websoft9.png)

3. Send test mail
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/prestashop-smtp004-websoft9.png)
     

### Prestashop change domain

If you want to change domain for PrestaShop, these steps you need to do:

1. Completed domain resolution and domain binding
2. Enable PrestaShop's Maintenance mode
3. Edit the PrestaShop's configuration file([path](/stack-components.html#prestashop)), modify the domain
4. Log in PrestaShop console, open:【Shop Parameters】>【Traffic&SEO】, modify the shop URL
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-seturl-websoft9.png)

### PrestaShop import

Log in PrestaShop console, open:【Advanced Parameters】>【Import】
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-importdb-websoft9.png)

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage PrestaShop

通过运行`docker ps`，可以查看到 PrestaShop 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

### Path{#path}
  
PrestaShop installation directory: */data/wwwroot/PrestaShop*  
PrestaShop configuration file: */data/wwwroot/prestashop/app/config/parameters.php*

### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 3306 | Remote connect MySQL | Optional |
| 80 | HTTP requests for PrestaShop | Required |
| 443 | HTTPS requests PrestaShop | Optional |
| 9090 | phpMyAdmin on Docker | Optional |

### Version{#version}

You can see the version from product page of Marketplace.

### Service{#service}

```shell
sudo docker start | restart | stop | stats prestashop
```

### CLI{#cli}

PrestaShop 提供了一个用于安装和修改配置的 [CLI](https://doc.prestashop.com/display/PS17/Installing+PrestaShop+using+the+command-line+script)，进入根目录下运行：  

```
php index_cli.php --domain=example.com --db_server=sql.example.com --db_name=prestashop --db_user=root --db_password=123456789
```

### API

[Webservice API](https://devdocs.prestashop.com/1.7/webservice/)