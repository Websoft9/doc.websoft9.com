---
title: Drupal
slug: /drupal
tags:
  - CMS
  - Content Management
  - Website Building
---

import Meta from './_include/drupal.md';

<Meta name="meta" />

## Getting started{#guide}

### Login verification{#verification}

1. Completed installation Drupal at Websoft9 console, get the applicaiton's overview and access credentials from **My Apps**  

2. Starting to verify it
   ![](./assets/drupal-boardpage-websoft9.png)

### Setting up multilingual{#setlang}

Drupal supports multi-language, but you need to do as following:

1. Login to Drupal, and install the language in the background **Admin > Configuration > Region and Language**.

2. After installing a new language, set the default language.

### Install themes and modules

1. Get downloads from [Drupal Themes](https://www.drupal.org/project/project_theme) or [Drupal Modules](https://www.drupal.org/project/project_module).

2. Select **Extension Management > Install Extension**, enter the download address, and start [installation](https://www.drupal.org/docs/extending-drupal/installing-modules).

3. After successful installation, enable.

## Configuration options{#configs}

- Configuration file: /path/sites/default/settings.php
- Multilingual (✅)
- SMTP (✅): Install [SMTP Authentication Support](https://www.drupal.org/project/smtp) plugin for SMTP.
- [3rd Party CLI](https://drupalconsole.com/) 
- [APIs](https://www.drupal.org/docs/drupal-apis)

## Administer{#administrator}

- [Reset Password](https://www.drupal.org/node/44164) 

- Changing URLs: Change the value of `.htaccess` in the Drupal root directory with respect to the domain name.

- Online backup: Install the Drupal extension [Backup and Migrate](https://www.drupal.org/project/backup_migrate) to enable online backup policy settings.

## Troubleshooting{#troubleshooting}

#### Always report an error when initializing [Install Translation]?

Description: During installing translation, you need to download the translation file, and there may be timeout.  
Reason: poor network  
Solution: Retry several times until it succeeds.

#### Drupal status report has an error?

This "Error" is actually a "Warning" and can be ignored.

#### Protecting against HTTP ...?

Description: Drupal version 8.x or above, after installation, it prompts **Protecting against HTTP HOST Header attacks**.  
Reason: domain format error  
Solution: Go to the settings.php file in the Drupal directory and insert the domain name as following:
  ```
  $settings['trusted_host_patterns']=['^www\.webosft9\.com$'];
  ```

#### Still suggesting security vulnerability after installation?

Refer to: [Trusted Host settings](https://www.drupal.org/node/1992030)