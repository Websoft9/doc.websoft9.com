---
sidebar_position: 3
slug: /metabase/admin
tags:
  - Metabase
  - Data Analysis
  - BI
---

# Metabase Maintenance

This chapter is special guide for Metabase maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Backup and Restore

### Upgrade

Follow the steps below to complete the upgrade:

1. Log in Metabase, go to Admin->Setting->Updates, the system will give you a reminder if there is a new upgrade package
![Metabase updates reminder](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-updatereminder-websoft9.png)

2. Click the **Upgrade** button, go to the [Metabase Install](https://metabase.com/start/) page

3. The deployment package we provide is in the jar package installation mode, so on the installation page we select the **Custom install** mode.
![Metabase install](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatedl-websoft9.png)

3. Download teh Metabase.jar pakage and upload to your instance's directory `/data/wwwroot/metabase`
![Metabase upload](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatereplace-websoft9.png)

4. Overwrite existing files and reload the Metabase

## Troubleshoot{#troubleshoot}

In addition to the Metabase issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

## FAQ{#faq}

#### Metabase support multi-languages?

Yes
