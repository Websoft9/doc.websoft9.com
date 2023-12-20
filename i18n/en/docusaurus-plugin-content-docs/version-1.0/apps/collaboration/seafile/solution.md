---
sidebar_position: 2
slug: /seafile/solution
tags:
  - Seafile
  - File sync and share
  - knowledge Management
---

# Seafile Solution

Seafile 可以与其他的软件平台**集成**一起使用，解决 构建企业网盘系统 过程中的各种[场景问题](#)。

## Seafile Integrate ONLYOFFICE Docs{#onlyoffice}

Seafile opensource edition supports the **OnlyOffice Document Server** for file preview and edit. This deployment solution have installed the **OnlyOffice Document Server**, so you just need to configure it if you want to use it

1. Enable the **TCP:9002** port on ,and check that [OnlyOffice Docs](../onlyofficedocs) is available
2. Use the **SFTP** to connect Server, edit the Seafile's configuration file: /opt/seafile-data/seafile/conf/seahub_settings.py
3. Insert the template like below
   ```
   # Enable Only Office
   ENABLE_ONLYOFFICE = True
   VERIFY_ONLYOFFICE_CERTIFICATE = False
   ONLYOFFICE_APIJS_URL = 'https://example.seafile.com:9002/web-apps/apps/api/documents/api.js'
   ONLYOFFICE_FILE_EXTENSION = ('doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'odt', 'fodt', 'odp', 'fodp', 'ods', 'fods')
   ONLYOFFICE_EDIT_FILE_EXTENSION = ('docx', 'pptx', 'xlsx')
   ```
   > Set **ONLYOFFICE_APIJS_URL**, e.g example.seafile.com to your domain or Internet IP

4. Restart the Docker of Seafile
   ```
   sudo docker restart seafile
   ```

5. Test the previwe and edit
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-onlyofficepr-websoft9.png)