---
sidebar_position: 1
slug: /opencart
tags:
  - OpenCart
  - eCommerce
---

# OpenCart Getting Started

[OpenCart](https://opencart.com)  is an easy to-use, powerful, open source online store management program that can manage multiple online stores from a single back-end. Administrative area simply by filling in forms and clicking “Save”. There are many professionally-written extensions available to customize the store to your needs.it have 13000+ modules and themes on Marketplace for all your needs.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/opencart/opencart-gui-websoft9.png)  

If you have installed Websoft9 OpenCart, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** on your Cloud Platform
2. Check you **[Inbound of Security Group Rule](https://support.websoft9.com/docs/faq/tech-instance.html)** of Cloud Console to ensure the **TCP:80** is allowed
3. **[Get](./user/credentials)** default username and password of OpenCart  
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for OpenCart

## OpenCart Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *https://domain* or *https://Internet IP*, start to install    
2. Agree license, Click "Continue"
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/oc1.png)
3. Verify the environment and go to next step  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/oc2.png)
4. Database connection configuration, you can use the MySQL in this Server([Don's know password?](./user/credentials)), and you can use other database services
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/oc3.png)
5. When the installation is completed,it will go the following interface
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/oc4.png)
6. Please delete */data/wwwroot/opencart/install* folder.
7. You can use OpenCart now

> More useful OpenCart guide, please refer to [OpenCart Docs](https://docs.opencart.com/) to get more details

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## OpenCart QuickStart

下面以 **使用 OpenCart 构建在线商城** 作为一个任务，帮助用户快速入门：

## OpenCart Setup

### OpenCart Extension

OpenCart have 13000+ extention published on the Marketplace, how to insatll them?

1. Find the extension you want to used on Marketplace and download it
  
2. Log in OpenCart console, open:【Extensions】>【Installer】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/opencart-installex-websoft9.png)
  
3. Upload your extension compressed file
  
4. Installing it

### OpenCart language

Enable a new language package in Opencart have the following steps(e.g Chinese lanuage)

1. Go to [OpenCart Marketplace](https://www.opencart.com/index.php?route=marketplace/extension/info&extension_id=19126&filter_category_id=2&page=8), download suitable lanuage package
2. Unzip package, you can see a folder name `upload` that includes two folder `admin`, `catalog`
3. Use SFTP to upload them to your Server
   ```
   admin->language->zh_cn  to  ```/data/wwwroot/opencart/admin/language``` 
   catalog->language->zh-cn to ```/data/wwwroot/opencart/catalog/language```
   ```
4. Log in OpenCart, go to【System】>【localization】>【languages】, add new language and configure it
	![websoft9](https://libs.websoft9.com/Websoft9/DocsPicture/zh/opencart/opencart-language-1-websoft9.png)

5. Enable language both for catalog and admin: open 【System】>【Settings】, the 【Language】 for catalog, 【Administration Language】for admin
	   ![websoft9](https://libs.websoft9.com/Websoft9/DocsPicture/zh/opencart/opencart-language-2-websoft9.png)

6. Refresh OpenCart, display the new language

### OpenCart vQmod

Opencart 2.0 using **vQmod** for installing extensions, so you need to install and enable vQmod:

1. [Download vQmod](https://github.com/vqmod/vqmod)
2. Go to Extensions > Installer, upload **vqmod.zip**
3. Go to Extensions > Extensions > Modules > Integrated VQmod to install and then edit to enable this module

### SMTP

1. Log in SendGrid console, prepare your SMTP settings like the follow sample
   ```
   SMTP host: smtp.sendgrid.net
   SMTP port: 25 or 587 for unencrypted/TLS email, 465 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9smpt
   SMTP password: #fdfwwBJ8f    
   ```
2. Log in OpenCart console as administrator, configure SMTP  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/opencart-smtp-websoft9.png)
  
   - SMTP Hostname: tls:// or ssl:// is need
   - Make sure you have input correct SMTP items

3. Send testing Email

### OpenCart change domain

You can change the domain of OpenCart by the following steps:

1. Complete the new **Domain resolution and Domain binding**
2. Modify the OpenCart configuration `config.php` in the root directory
   ```
   // HTTP
   define('HTTP_SERVER', 'http://example.com/');
   // HTTPS
   define('HTTPS_SERVER', 'https://example.com/');
   ```
3. Modify the OpenCart configuration `admin/config.php` in the root directory
   ```
   // HTTP
   define('HTTP_SERVER', 'http://www.example.com/admin/');
   define('HTTP_CATALOG', 'http://www.example.com/');
   // HTTPS
   define('HTTPS_SERVER', 'http://www.example.com/admin/');
   define('HTTPS_CATALOG', 'http://www.example.com/');
   ```
3. [Restart PHP-FPM Service](#service)

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage OpenCart

通过运行`docker ps`，可以查看到 OpenCart 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

### Path{#path}
  
OpenCart installation directory: */data/wwwroot/OpenCart*  
OpenCart catalog configuration file: */data/wwwroot/opencart/config.php*   
OpenCart admin configuration file: */data/wwwroot/opencart/admin/config.php*
  
### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 3306 | Remote connect MySQL | Optional |
| 80 | HTTP requests for OpenCart | Required |
| 443 | HTTPS requests OpenCart | Optional |


### Version{#version}

```shell
sudo cat /data/logs/install_version.txt
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats opencart
```

### CLI{#cli}

无

### API

```
curl http://myopencart.example.com/index.php?route=api/cart/add
```

Refer to [OpenCart API](http://docs.opencart.com/en-gb/system/users/api/)