---
title: Seafile
slug: /seafile
tags:
  - Document Management
  - Office
  - Archives
---

import Meta from './_include/seafile.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Seafile at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Local browser access, enter Seafile login page

3. Enter your username and password to login to the Seafile backend management interface.
   ![Seafile Backend Interface](./assets/seafile-backend-websoft9.png)

4. **System Administration > Settings**, check whether the URL of Seafile is correct, otherwise the file cannot be uploaded and downloaded properly.


### Document Editing and Previewing {#docs}

1. Install ONLYOFFICE Docs or Collabora Online through the Websoft9 App Store.

2. Add connection configuration to seahub_settings.py and restart the app to take effect.
   - [ONLYOFFICE Docs](https://cloud.seafile.com/published/seafile-manual-cn/advanced_setup/only_office.md)
   - [Collabora Online](https://cloud.seafile.com/published/seafile-manual-cn/advanced_setup/libreoffice_online.md)

## Enterprise Edition

### Why buy through Websoft9?

Websoft9 is Seafile Enterprise Edition partner and purchasing through Websoft9 helps users:

- Purchase paid version with at least 10% discount
- More comprehensive product support
- Integrate with more technologies such as Web Disk, Cloud Storage, etc. 

### Activate License

Place the license file in the license directory (mounted), and restart the application to take effect. 

## Configuration options{#configs}

- Configuration file (mounted): */shared/seafile/conf/seahub_settings.py*
- License repository directory (mounted): */shared/seafile*
- STMP(✅): [Settings](https://cloud.seafile.com/published/seafile-manual-cn/config/sending_email.md) through configuration file, takes effect after restarting the application
- Mobile support(✅): consistent with computer login URLs
- Multilingual(✅)
- Multi-user(✅)
- Document sharing(✅)
- Document preview and editing (third-party middleware required)

## Administer{#administrator}

- Reset password: Edit the user in the *EmailUser* table of the database, update the password field to the following value, and the password will be reset to `123456`
  ```
  PBKDF2SHA256$10000$7289a20ae4fc2329415b0645fa3d106019cc61952ae1bc2f9eeef7b30dc47d88$5418ac28f06bd84f2bb701a10dbea6b0bd30676c8042e1f73b9ce12aac302a8d
  ```

- SERVICE_URL: Seafile console open: **System Management > Settings > URL**

- Modify email notification signature: Seafile console open: **System Management > Settings > Branding**

## Troubleshooting{#troubleshooting}

#### Seafile can't upload files?

Check if the Seafile URL matches the actual one!
   
#### Seafile cannot edit and preview files?

- Ensure that document middleware such as ONLYOFFICE Docs has been configured properly
- Ensure that the URL of Seafile matches the actual one.

#### Document security token not properly formed?

Description: After completing the ONLYOFFICE Docs configuration, Seafile Edit and Preview displays the error **Document security token not properly formed**   
Reason: ONLYOFFICE docs security settings do not match  
Solution: Modify the environment variable JWT_ENABLED in the ONLYOFFICE docs .env file and set it to false  

