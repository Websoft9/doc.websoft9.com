---
sidebar_position: 1
slug: /joomla
tags:
  - Joomla
  - CMS
---

# Joomla Getting Started

[Joomla](https://joomla.org/) is a free and open-source content management system (CMS) for publishing web content. Over the years Joomla! has won several awards. It is built on a model -view-controller web application framework that can be used independently of the CMS that allows you to build powerful online applications.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-gui-websoft9.jpg)  

If you have installed Websoft9 Joomla, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. [Get](./user/credentials) default username and password of Joomla
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Joomla.


## Joomla Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *https://domain* or *https://Internet IP*, start to install  

2. Set the site information and select language,then Cick 'Setup Login Data' button
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-wizard1-websoft9.png)

3. Set the user account inforamton
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-wizard2-websoft9.png)
   > Email is your login ID, not collected by anyone because it stored in your Cloud Server

4. Then configure the database connection information([Don't know password?](./user/credentials))
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-wizard3-websoft9.png)

5. Click "Extra steps: Install languages" to install extra language 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-wizard4-websoft9.png)

6. Follow the prompts to set whether to enable the multi-language feature of the website and set the default front-back language
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-wizard5-websoft9.png)

7. Click the 'Remove installation folder' button

8. Log in Joomla backend (URL is *http://domain/administrator*)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-wizard6-websoft9.png)

9. You can use the Joomla backend to setup your site now
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-wizard7-websoft9.png)

> Refer to [Joomla admin_manual](https://docs.joomla.org/Main_Page) to get more details

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  
  
#### Joomla not the latest version?

Completed the Joomla initial installation, the login console can be updated online to the latest version with one click.

## Joomla QuickStart

下面以 **使用 Joomla 构建内容管理系统** 作为一个任务，帮助用户快速入门：

## Joomla Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console  

2. Log in Joomla backend, open【System】>【Global configuration】>【Server】>【Mail Settings】, mailer is set to **smtp**, 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-opensmtp-websoft9.jpg)

3. Fill in the your correct SMTP items
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-smtpsettings-websoft9.png)
   
    * 发送模式选择“SMTP”，加密方式选择“SSL/TLS”;
    * 输入发送方邮箱地址；
    * 认证方式选择“登录”，并勾选“需要认证”选项；
    * 输入SMTP服务器地址和SMTP服务器的端口号；
    * 输入和发件人邮箱一致的邮箱地址；
    * 输入该邮箱地址的SMTP服务的授权码或密码；
    * 存储凭据；

4. Click "Send test email" to test your SMTP settings

     
### Joomla languages{#setlang}

Joomla supports multiple languages. Here are the main steps to install and set up multiple languages:

1. Log in Joomla, go to【Extension】>【Language(s)】>【installed】, install the languages you want
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-bkinstalllan-websoft9.png)

2. Then set your default language of Joomla Site or Administrator
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-bkenablelang-websoft9.png)


### Joomla extension{#plugin}

[Joomla! Extensions Directory™](https://extensions.joomla.org/) provided lots of extensions for you:

1. Log in Joomla  

2. Go to【Extensions】>【Install】>【Install from Web】and search the extensions
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-bkinstallext-websoft9.png)  

3. Install them online


### Joomla install template{#template}

You can upload your template package to install it:

1. Prepare your template (.zip file)

2. Log in Joomla backend

3. Open 【Extensions】>【Install】, select the tab【Upload package file】to install template
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-upload_install.png)

4. When have completed the installation, go to 【Extensions】>【Templates】>【Styles】, enable your template as default template
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-bkenabletemplate-websoft9.png)

> Some template zip package may have the Joomla source code, at this time **Install template=Install Joomla**


### Joomla Cache

Joomla backend have cache management function, refer to this picture:

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-opencache-websoft9.png)

### Joomla reset administrator password{#setpwd}

If you don't remember your administrator password, please refer to the docs [here](https://docs.joomla.org/How_do_you_recover_or_reset_your_admin_password%3F/en) to reset it


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Joomla

通过运行`docker ps`，可以查看到 Joomla 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

### Path{#path}
  
Joomla installation directory: */data/wwwroot/joomla*  
Joomla configuration file: */data/wwwroot/joomla/configuration.php*   

### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 80 | HTTP requests for Joomla | Required |
| 443 | HTTPS requests Joomla | Optional |
| 3306 | Remote connect MySQL | Optional |
| 9090 | phpMyAdmin on Docker | Optional |


### Version{#version}

```shell
sudo cat /data/logs/install_version.txt
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats joomla
```

### CLI{#cli}



### API

[Joomla! API Documentation](https://api.joomla.org/)