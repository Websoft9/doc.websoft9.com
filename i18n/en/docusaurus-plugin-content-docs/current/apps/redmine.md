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

1. After installing Redmine in the **Websoft9 console**, view the application details through **My Applications** and get the login information in the “Access”.

2. After entering the Redmine interface, click **Login** in the upper right corner.

3. According to the system prompts, change the password and officially access the console.

### Manage plugins  

Manage Redmine plugin is manage plugin sources at Redmine container directory */usr/src/redmine/plugins* and need restart Redmine container takes effect

- Install Plugins: Run below commands at Redmine container
   ``` 
   apt update -y && apt install unzip 
   curl -L -o plugin_name.zip  https://url/plugin_name.zip 
   unzip rplugin_name.zip -d /usr/src/redmine/plugins 
   ``` 
- Uninstall Plugin: Delete the plugin directory  

- After downloading and unzipping the plug-in, restart the container to take effect

- Plugin version mismatch will cause the container can not start, need to uninstall the plugin

### Set SMTP{#smtp}  

1. Prepare the your SMTP  
2. Modify the `configuration. yml` file in the Redmine container and add below SMTP configurations at **production**:  
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
2. It works after restarting the Redmine container
3. Redmine Console Settings for SMTP: **Administration > Configuration > Email Notification**

## Configuration options{#configs}

- [Plugin Center](https://www.redmine.org/plugins)(✅)  
- Multilingual(✅): Support project multilingualism and user multilingualism  
- Site directory in container(Have mounted): */usr/src/redmine*  
- Configuration directory in container(Have mounted): */usr/src/redmine/configure*  
- Configuration file in container (Have mounted): */usr/src/redmine/configuration/configuration.yml*  
- [CLI](https://pypi.org/project/Redmine-CLI/)  
- [API](https://www.redmine.org/projects/redmine/wiki/Rest_api)  
- [SMTP](https://www.redmine.org/projects/redmine/wiki/EmailConfiguration) (✅) 

## Administer{#administrator}

- Backup and Restore: [Redmine BackupRestore](https://redmine.org/projects/redmine/wiki/RedmineBackupRestore)

## Troubleshooting{#troubleshooting}

#### System error when project name is Chinese?

Redmine Database character encoding needs to be modified to `utf8`

#### New registered users cannot login?

Administrator needs to activate in the background before logging in
