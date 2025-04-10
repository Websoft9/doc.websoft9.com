---
title: Mediawiki
slug: /mediawiki
tags:
  - Wiki
  - CMS 
  - Knowledge Management
  - Blog System - Online Drawing
  - Visual Whiteboard
  - excalidraw
---

import Meta from './_include/mediawiki.md';

<Meta name="meta" />

## Getting started{#guide}

### initialization

1. After installing MediaWiki in the Websoft9 console, view the application details in "My Apps"

  - Get access URLs in **Access** tabs
  - Get **Intranet Host** and **Password** in the **Database** tab 

2. Local browser access URL to Mediawiki initialization wizard

3. The database configuration provided by default is as follows:

   ![mediawiki Connecting to the database](./assets/mediawiki-connectdb-websoft9.png)

      - Database type : `MySQL`
      - Database host : Step 1 **Intranet Host** obtained
      - Database name : `mediawiki`
      - Database username : `mediawiki`
      - Database password : **Password** obtained at step 1 

   > Fill in the information and select Install wiki

4. After MediaWiki is installed, download the LocalSettings.php file generated by the installer

5. Return to Websoft9 Console, view app details via "My Apps". Click on **Go to Edit Repository** in the **Compose** tab. Go to the */src* directory, click **Add File**. Select **Upload File**, upload the LocalSettings.php file, and click **Commit Changes** 

6. Go back to the previous directory in the */src* directory, go to the docker-compose.yml file. Uncomment the following code, and then click **Commit Changes** 
   ```
   # - ./src/LocalSettings.php:/var/www/html/LocalSettings.php
   ```

7. Return to "My Apps" and click **Redeploy App** in the **Compose** tab or click the **Redeploy App** icon in the upper right corner to rebuild the app

8. Visit the URL again in your local browser to log in
 

### Quick setup
 
- Install extensions: [Manual:Extensions](https://www.mediawiki.org/wiki/Manual:Extensions/zh)
- Visual Editor: [Help:Starting_a_new_page](https://www.mediawiki.org/wiki/Help:VisualEditor/User_guide/zh)
- File Upload: [Help:FAQ:Enabling File Upload](https://www.mediawiki.org/wiki/Manual:FAQ/zh#如何启用文件上传?)
- Language Settings: [Help:FAQ:Language Settings](https://www.mediawiki.org/wiki/Manual:FAQ/zh#我如何更改界面语言?)
- Interface Customization: [Help:FAQ:Customize Interface](https://www.mediawiki.org/wiki/Manual:FAQ/zh#定制界面), including modifying the logo, setting up the navigation bar, and customizing CSS.

### Setting up SMTP{#smtp}

1. Edit the `/bitnami/mediawiki LocalSettings.php` configuration file.

2. Locate the variable $wgSMTP and configure it as follows: 
   
   ```
    $wgSMTP = array(
    'host' => "smtp.163.com", 
    'IDHost' => "example.com", // Mailbox domain, optional. If not set, it will be set to the value of $wgServer. 
    'port' => 465, /> 'auth' => true, // The value of $wgServer if not set.    
        
    'username' => "websoft9@163.com", 'password' => "#wwgServer    
    'password' => "#wwBJ8"    
    ).
   ```

3. Find the variable $wgEnableEmail and set its value to true.
   
   ```
    $wgEnableEmail = true
   ```


4. Locate the following variables and set their values to the sender's email address.
   
   ```
    $wgEmergencyContact = "websoft9@163.com";
    $wgPasswordSender = "websoft9@163.com";
   ```

5. After making these changes, restart the application for the settings to take effect.

## Configuration options{#configs}

- Configuration file (mounted): */bitnami/mediawiki/LocalSettings.php*
- [API:Main_page](https://www.mediawiki.org/wiki/API:Main_page/zh)
- Multilingual(✅)
- Multimedia files(✅)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

