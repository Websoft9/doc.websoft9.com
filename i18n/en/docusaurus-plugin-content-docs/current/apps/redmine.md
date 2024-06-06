---
title: Redmine
slug: /redmine
tags:
  - Agile development 
  - Project manageme
---

import Meta from './_include/redmine.md';

<Meta name="meta" />

## Getting started{#guide}

### Login to reset password{#wizard}

1. When completed installation of Redmine at Websoft9 console, get the applicaiton's overview and access information from "My Apps"   

2. Aceess the Redmine index page, click the "login"  

3. According to the system prompt, change the password and use it  

### Manage plugins  

After get the matching plugin version, download and extract the plugin to the Redmine container directory */usr/src/redmine/plugins*

- Example command for downloading and decompressing plugins within a container: 
   ``` 
   apt update -y && apt install unzip 
   curl -L -o plugin_name.zip  https://url/plugin_name.zip 
   unzip rplugin_name.zip -d /usr/src/redmine/plugins 
   ``` 
- Delete the plugin directory to uninstall the plugin 
- After downloading the decompression plugin, restarting the container takes effect 
- Incompatible plugin versions can cause the container to fail to start, so the plugin needs to be uninstalled

### Set SMTP{#smtp}  

1. Modify the `configuration. yml` file in the Redmine container and add SMTP under production:  

- Ensure the accuracy of the SMTP host/account/password  
- Pay attention to indentation/spaces, otherwise Redmine will report an error 
   ``` 
   production: 
   delivery_method: smtp 
   smtp_settings: 
   address: smtp.exmail.qq.com 
   port: 465 
   ssl: true 
   enable_starttls_auto: true 
   domain: websoft9.com 
   authentication: :login 
   user_name:  help@websoft9.com 
   password: ******** 
   ``` 
2. It works after restarting the Redmine container service 
3. Redmine Console Settings for SMTP: "Administration" > "Configuration" > "Email Notification"

## Configuration options{#configs}

- [Plugin Center](https://www.redmine.org/plugins)(✅)  
- Multilingual(✅): Support project multilingualism and user multilingualism  
- Site directory (mounted): */usr/src/redmine*  
- Configuration directory (mounted): */usr/src/redmine/configure*  
- Configuration file (mounted): */usr/src/redmine/configuration/configuration.yml*  
- [CLI](https://pypi.org/project/Redmine-CLI/)  
- [API](https://www.redmine.org/projects/redmine/wiki/Rest_api)  
- [SMTP](https://www.redmine.org/projects/redmine/wiki/EmailConfiguration) 

## Administer{#administrator}

- Backup and Restore: [Redmine BackupRestore](https://redmine.org/projects/redmine/wiki/RedmineBackupRestore)

## Troubleshooting{#troubleshooting}

#### When the project name is Chinese, the system reports an error?

Database character encoding needs to be modified to utf8

#### New registered users cannot login?

Administrator needs to activate in the background before logging in