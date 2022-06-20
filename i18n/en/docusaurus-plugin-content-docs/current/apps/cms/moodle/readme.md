---
sidebar_position: 1
slug: /moodle
tags:
  - Moodle
  - elearning
---

# Moodle Getting Started

[Moodle](https://moodle.org) is a learning platform designed to provide educators, administrators and learners with a single robust, secure and integrated system to create personalised learning environments.Moodle is built by the Moodle project which is led and coordinated by Moodle HQ, an Australian company of 30 developers which is financially supported by a network of over 60 Moodle Partner service companies worldwide.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodlegui-websoft9.jpg)  

If you have installed Websoft9 Moodle, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. **[Get](./user/credentials)** default username and password of Moodle
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Moodle  

## Moodle Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *https://domain name* or *https://Internet IP*, enter to Moodle installation page

2. Choose a language, then go to next step
   ![Moodle-install-language](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/md01.png)

3. Set the Moodle source code and data directory
   ![Moodle set directory](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/md02.png)

4. Choose the database type
   ![Moodle Choose database](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/md03.png)

5. Fill in your database connection information ([Don't know password?](./user/credentials))
   ![Moodle set database connection](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/md04.png)

6. Confirm the Copyright
   ![Moodle Confirm the Copyright](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/md05.png)

7. Installing
   ![Moodle start install](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/md06.png)
   ![Moodle start install](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/md07.png)

8. Set administrator account
   ![Moodle set administrator account](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/md08.png)

   > Email is your system ID, not collected by anyone because it stored in your Cloud Server

9. Set site name, short name, front page summary...
   ![Moodle set site information](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/md09.png)

10. Installed successfully.
   ![Moodle installation successfully](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/md10.png)

11. [Register a Moodle account](#register) to connect Moodle official website for more extension

> More useful Moodle guide, please refer to [Moodle Documentation](https://docs.moodle.org)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Moodle QuickStart

下面以 **使用 Moodle 构建学习管理系统** 作为一个任务，帮助用户快速入门：

[Moodle 快速搭建学习管理系统](https://cloud.tencent.com/developer/article/1822682)

## Moodle Setup

### DNS Additional Configure (Modify URL){#dns}

Complete **[Five steps for Domain](./administrator/domain_step)** ，Set the URL for Moodle:

1. 修改 Moodle [配置文件](#parameter)，将配置项 $CFG->wwwroot   = 'http://www.abc.com' 修改成域名;

2. 保存后生效

### HTTPS{#https}  

**[标准 HTTPS 配置](./administrator/domain_https)** 完成后，可能会遇到如下的异常情况：

- [配置HTTPS后，网站部分资源无法加载？](./wordpress/admin#httpsmore)

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Log in to Moodle console as administrator  

3. Open **Site administrator** > **Server** > **Email** > **Outgoing mail configuration**
   ![Moodle SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-smtp-websoft9.png)
   ![Moodle SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-smtps-websoft9.png)  

4. Click the **Test outgoing mail configuration** to test your settings

### Register your Moodle site{#register}

Once completed your Moodle installation wizard, suggest you to register Moodle's website account. This account can help you to get upgrade message, get share course of Moodle.NET, install plugins online

1. Log in Moodle console as administrator  

2. Open **Site administrator** > **Registation**
   ![Moodle register](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-registermd-websoft9.png)  

3. When you completed it, Moodle.net may stay in touch and provide you with important things for your Moodle site

### Moodle languages{#setlanguge}

1. Log in Moodle console as administrator  

2. Open **Site administrator** > **Language**
   ![Moodle language setting](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-languageset-websoft9.png)  

3. Set it by yourself
   * Language settings: choose your language online
   * Language customization: edit your language files online
   * Language packs: upload your language packs
   
### Moodle Mobile{#client}

1. Log in Moodle console as administrator  

2. Open **Site administrator** > **Mobile app** > **Mobile settings**
   ![moodle-apps](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-app-1-websoft9.png)  

3. Check **Enable web services for mobile devices** is selected
   ![moodle-apps](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-app-2-websoft9.png)  

4. Save settings  

5. Install [Moodle APPS](https://download.moodle.org/mobile/) in your phone  

6. Open the Moodle app in your phone, configure the Moodle's URL to your app and start to use it
   ![moodle-apps](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-mobile-websoft9.png)
   

### Moodle plugins{#plugin}

Moodle is very scalable platform, most of function were as plugins. Moodle have installed 400+ plugins by default and you can install plugins from [Plugins Marketplace](https://moodle.org/plugins/) to extend your functions

1. Log in Moodle console as administrator  

2. Open **Site administrator** > **Plugins** 
   ![moodle plugins](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-plugins-websoft9.png)  

3. Click **Plugins Overview** to list all plugins installed, you can disable and uninstall it also  

4. Visit [Plugins Marketplace](https://moodle.org/plugins/) to search more plugins  

5. Start to install plugins in the Moodle's console
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-intallplugins001-websoft9.png)  

6. Upload plugin online
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-intallplugins-uploadfile-websoft9.png) 

> More details about manage plugins please refer to official docs [Moodle Plugins](https://docs.moodle.org/37/en/Installing_plugins)

### Moodle theme{#theme}

Moodle 主题实际上是一个插件，因此需要安装新主题，必须通过【安装插件】的方式先进行安装。  

1. 以管理员身份登录 Moodle

2. 依次打开：【网站管理】>【插件】，进入插件市场后，选择【Theme】类型的插件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-mktheme-websoft9.png)

3. 在线安装所需的主题

4. 打开【网站管理】>【外观】>【主题选择器】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-addtheme001-websoft9.png)

5. 点击【更改主题】即可完成主题更换
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-addtheme002-websoft9.png)  

### Reset Password{#resetpwd}

There are two main measures to reset Moodle's password：

**Changing password**

Take the steps below:

1. log in the Moodle console, click 【Profile】 link of user icon on the top menu, then click the **setting icon**
  ![Moodle console modify password](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-modifypw-websoft9.png)

2. start to change the password.

**Forgot Password**

If you have forgotten the password of Moodle, two methods for you tor retrieve it:

* Retrieve it by Email from login page (you must completed the [SMTP settings](./administrator/smtp))
* Retrieve it by modify database

Follow the steps of retrieve database by modify database:

1. Login [phpMyAdmin](./administrator/parameter#managedb), and find the database table *mdl_user*

  ![Moodle user table](https://libs.websoft9.com/Websoft9/DocsPicture/en/moodle/moodle-phpmyadminuser-websoft9.png)

2. Edit the 【admin】user, replace the column `password` 's value to `21232f297a57a5a743894a0e4a801fc3`

3. Click 【Go】 button, the password has been set to `admin`

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Moodle

通过运行`docker ps`，可以查看到 Moodle 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

### Path{#path}

Moodle installation directory: */data/wwwroot/moodle*  
Moodle configuration file: */data/wwwroot/moodle/config.php*

### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 3306 | Remote connect MySQL | Optional |
| 80 | HTTP requests for Moodle | Required |
| 443 | HTTPS requests Moodle | Optional |
| 9090 | Web managment GUI for MySQL | Optional |


### Version{#version}

控制台查看

### Service{#service}

```shell
sudo docker start | stop | restart | stats moodle
```

### CLI{#cli}

[Administration via command line](https://docs.moodle.org/311/en/Administration_via_command_line)

```
$ cd /path/to/your/moodle/dir
$ sudo -u apache /usr/bin/php admin/cli/somescript.php --params
$ sudo -u apache /usr/bin/php admin/cli/install.php --help
```

### API

[Core APIs](https://docs.moodle.org/dev/Core_APIs)