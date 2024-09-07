---
title: Moodle
slug: /moodle
tags:
  - Online learning 
  - LMS
  - Teaching management
  - Course management
---

import Meta from './_include/moodle.md';

<Meta name="meta" />

## Getting started{#guide}

### Login Verification{#verification}

1. After completing the installation of Moodle in the Websoft9 console, get the applicaiton's overview and access credentials from **My Apps**

2. Verify the installation
   ![](./assets/moodle-backend-websoft9.png)
   
### Install plugin{#plugin}
 
1. Log in to the Moodle backend as an administrator  

2. Open **Site administration > Plugins** to view or install plugins  

3. Moodle supports two methods for installing plugins: 
    
   - Online installation: Install plugins directly from the Moodle plugin directory 
   - Offline installation: Upload a ZIP file to install the plugin.

### Install Theme{#theme}  

1. A Moodle theme is essentially a type of plugin. You can install it using the **install Plugin** method

2. To change the theme, navigate to **Site administration > Appearance > Theme selector**

## Configuration options{#configs}

- [Plugin](https://moodle.org/plugins/)(✅) : Install plugin online. Note that registration on the Moodle website is required. Go to "Site administration" > "Registration" in your Moodle console.
- [Topic](https://moodle.org/plugins/)(✅): Themes are also considered plugins.
- Configuration file: Located in the container at /bitnami/moodle/config.php (mounted).
- PHP configuration modification: Modify related variables in the `.env` file
- Media files(✅) 
- Multilingual(✅): Enable via "Site administration" > "Language" > "Language Packs"  
- SMTP(✅): Configure through "Site administration" > "Server" > "Email" > "Sending Email Settings"  
- Mobile Support(✅): Configure via "Site administration" > "Mobile Applications" > "Mobile Device Settings" > "Enable Network Services for Mobile Devices" 
- [Plugins](https://docs.moodle.org/37/en/Installing_plugins) 
- [Administration via command line]( https://docs.moodle.org/311/en/Administration_via_command_line ) 
   ``` 
   $sudo - u Apache/usr/bin/php admin/cli/somescript.php -- params 
   $sudo - u Apache/usr/bin/php admin/cli/install.php -- help 
   ``` 
- [Core APIs](https://docs.moodle.org/dev/Core_APIs) 
- Online backup: Set up automated backups via "Website Management" > "Courses" > "Automated backup setup"

## Administer{#administrator}

- **Retrieve Password**: To reset the administrator password, modify the `mdl_user` table in the Moodle database. Replace the value of the `password` field with `21232f297a57a5a743894a0e4a801fc3` (the hashed value for admin), then reset the password to `admin`.

## Troubleshooting{#troubleshooting}
