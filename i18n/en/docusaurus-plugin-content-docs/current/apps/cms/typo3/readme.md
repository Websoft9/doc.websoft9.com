---
sidebar_position: 1
slug: /typo3
tags:
  - Typo3
  - CMS
  - Site Management
---

# Typo3 Getting Started

[Typo3](https://typo3.org/) is a **enterprise-level** website building system (CMS) originating from Germany. It has a mature [business ecological partner](https://typo3.com/partners/professional-service-listing) to provide enterprise customers with comprehensive Serve. Can easily [integrate] seamlessly with digital asset management, e-commerce, translation services, marketing automation, analytics, and more (https://typo3.com/partners/technology-partners).
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/typo3-gui-websoft9.png)

If you have installed Websoft9 Typo3, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. **[Get](./user/credentials)** default username and password of Typo3
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Typo3.
 
## Typo3 Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL http://domain name or http://Internet IP, you will enter the Typo3

2. After passing the system environment test, fill in the database parameters ([View database account password](./user/credentials))
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-installdb-websoft9.png)

4. After the database connection is successful, the system prompts you to select an existing database or create a new database (an existing database is recommended)

5. Set the management account and site information
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-installsetadmin-websoft9.png)

6. After the installation is completed, log in to the background


> To learn more about the use of Typo3, please refer to the official documentation: [Typo3 Documentation](https://typo3.org/help/documentation/)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Typo3 QuickStart


## Typo3 Setup

### Extension management

TYPO3 CMS offers numerous extensions to enhance system functionality.

1. Login to Typo3 backend，go to ADMIN TOOLS  > Extensions

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-BackendExtensionManager-websoft9.png)

2. Select [Get extensions] from the menu to view extensions

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-BackendExtensionManagerInstall-websoft9.png)

3. Install or update extensions

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-BackendExtensionManagerExtensionVersions-websoft9.png)

### Template management

The template management of TYPO3 CMS is very meticulous and can make subtle settings for the smallest elements of the template

1. Login to Typo3 backend，go to WEB > Template

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-template-websoft9.png)

2. Configuration template

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Typo3

Run `docker ps` command, view all Containers when Typo3 is running:

```bash
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                                                  NAMES
a993567e8948   martinhelmich/typo3:latest   "docker-php-entrypoi…"   18 minutes ago   Up 18 minutes   0.0.0.0:9001->80/tcp, :::9001->80/tcp                  typo3
ba3eb402562b   mysql:8                      "docker-entrypoint.s…"   18 minutes ago   Up 18 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   typo3-mysql
```

### Path{#path}

TYPO3 Directory： */data/wwwroot/typo3*

### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 9001   | Typo3 original port | Optional   |

### URL

Backend：*http://URL/typo3*

### Version{#version}



### Service{#service}

```shell
sudo systemctl start | stop | restart | status Typo3
```

### CLI{#cli}

Typo3 has full command line functionality:

* typo3 official core command line
* typo3cms third-party extension command

```
$ php /var/www/html/typo3_src/typo3/sysext/core/bin/typo3
TYPO3 CMS 11.5.12 (Application Context: Production)

Usage:
  command [options] [arguments]

Options:
  -h, --help            Display help for the given command. When no command is given display help for the list command
  -q, --quiet           Do not output any message
  -V, --version         Display this application version
      --ansi|--no-ansi  Force (or disable --no-ansi) ANSI output
  -n, --no-interaction  Do not ask any interactive question
  -v|vv|vvv, --verbose  Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug

Available commands:
  list                   Lists commands
  help                   Displays help for a command
  dumpautoload           [extensionmanager:extension:dumpclassloadinginformation|extension:dumpclassloadinginformation] Updates class loading information in non-composer mode.
 backend
  backend:lock           Lock the TYPO3 Backend
  backend:resetpassword  Trigger a password reset for a backend user
  backend:unlock         Unlock the TYPO3 Backend
 cache
  cache:warmup           Cache warmup for all, system or, if implemented, frontend caches.
  cache:flush            Cache clearing for all, system or frontend caches.
 extension
  extension:list         Shows the list of extensions available to the system
  extension:setup        Set up extensions
 language
  language:update        Update the language files of all activated extensions
 mailer
  mailer:spool:send      [swiftmailer:spool:send] Sends emails from the spool
 referenceindex
  referenceindex:update  Update the reference index of TYPO3
 site
  site:list              Shows the list of sites available to the system
  site:show              Shows the configuration of the specified site
 upgrade
  upgrade:run            Run upgrade wizard. Without arguments all available wizards will be run.
  upgrade:list           List available upgrade wizards.
```


[Symfony Console Commands (cli)](https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/ApiOverview/CommandControllers/Index.html)

### API

[TYPO3 API Documentation](https://api.typo3.org/)