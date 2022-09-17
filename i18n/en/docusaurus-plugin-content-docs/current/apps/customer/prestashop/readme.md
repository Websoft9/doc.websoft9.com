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

1. Using local Chrome or Firefox to visit the URL *https://domain/admin* or *https://Internet IP/admin*, access login page    
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/ps07.png)

2. Input email and password([Don's know password?](./user/credentials)), accesss your administration console
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/ps08.png)

3. Use *http://IP*  to go to your index page.
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

### Prestashop connect Marketplace{#connect-prestashop-marketplace}

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
3. Edit the PrestaShop's [configuration file](#path), modify the domain
4. Log in PrestaShop console, open:【Shop Parameters】>【Traffic&SEO】, modify the shop URL
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-seturl-websoft9.png)

### PrestaShop import

Log in PrestaShop console, open:【Advanced Parameters】>【Import】
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-importdb-websoft9.png)

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage PrestaShop

Run docker ps, view all containers when PrestaShop is running:

```bash
CONTAINER ID   IMAGE                          COMMAND                  CREATED          STATUS          PORTS                                                  NAMES
90426aedeca1   prestashop/prestashop:latest   "docker-php-entrypoi…"   47 minutes ago   Up 47 minutes   0.0.0.0:9001->80/tcp, :::9001->80/tcp                  prestashop
cac699817c8b   mysql:5.7                      "docker-entrypoint.s…"   47 minutes ago   Up 47 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   prestashop-db
489469b66647   phpmyadmin:latest              "/docker-entrypoint.…"   48 minutes ago   Up 48 minutes   0.0.0.0:9090->80/tcp, :::9090->80/tcp                  phpmyadmin
```

### Path{#path}
  
PrestaShop install directory: */data/apps/prestashop*  
PrestaShop site directory: */data/apps/prestashop/data/prestashop*  
PrestaShop configure file: */data/apps/prestashop/data/prestashop/app/config/parameters.php* 

### Port{#port}

In addition to common ports such as 80, 443, etc., the following ports may be used:

No special port

### Version{#version}

```
docker exec -i prestashop cat /var/www/html/app/AppKernel.php|grep "const VERSION"|cut -d= -f2
```

### Service{#service}

```shell
sudo docker start | restart | stop | stats prestashop
sudo docker start | restart | stop | stats prestashop-db
sudo docker start | restart | stop | stats phpmyadmin
```

### CLI{#cli}

PrestaShop 提供了一个用于安装和修改配置的 [CLI](https://doc.prestashop.com/display/PS17/Installing+PrestaShop+using+the+command-line+script)，进入根目录下运行：  

```
php index_cli.php --domain=example.com --db_server=sql.example.com --db_name=prestashop --db_user=root --db_password=123456789
```

### API

[Webservice API](https://devdocs.prestashop.com/1.7/webservice/)
