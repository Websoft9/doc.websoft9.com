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

### Initial setup{#wizard}

1. When completing the installation of Mediawiki in the **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

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

