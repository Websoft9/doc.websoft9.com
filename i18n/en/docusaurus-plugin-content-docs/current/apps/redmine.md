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

2. Login the Redmine and change password by system prompt

### Manage plugins  

Manage Redmine plugin is manage plugin sources at Redmine container directory */usr/src/redmine/plugins* and need restart Redmine container takes effect

- Install Plugins: Run below commands at Redmine container
   ``` 
   apt update -y && apt install unzip 
   curl -L -o plugin_name.zip  https://url/plugin_name.zip 
   unzip rplugin_name.zip -d /usr/src/redmine/plugins 
   ``` 
- Uninstall Plugin: Delete the plugin directory

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
3. Redmine Console Settings for SMTP: "Administration" > "Configuration" > "Email Notification"

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
