---
title: Grafana
slug: /grafana
tags:
  - Analytics
  - Visualization
  - Log Analysis
  - Time-series data
  - Internet of Things
  - Data Analytics
---

import Meta from './_include/grafana.md';

<Meta name="meta" />

## Getting started{#guide}

### Verify the installation {#wizard}

After installing Grafana in the **Websoft9 console**, view the application details through **My Applications** and get the login information in the **Access** tab.  

- Grafana console page  
   ![Grafana Console](./assets/grafana-dashboard-websoft9.png)

- Select **Administration > Plugins**, and add a plugin    
   ![Grafana Add Plugins](./assets/grafana-plugins-websoft9.png)

- Select **connections > Data Sources**, and add a data source (analysis object)    
   ![Grafana Add Data Sources](./assets/grafana-datasource-websoft9.png)

## Configuration options{#configs}

- Configuration file (path within container): /etc/grafana/grafana.ini
- [Grafana API](https://grafana.com/docs/grafana/latest/http_api)
- Command line: `grafana-cli`
- Default database: Built-in SQLite

## Administer{#administrator}

- **smtp configuration**: add the smtp configuration segment to the configuration file

   ```
   #################################### SMTP / Send e-mail #####################
   [smtp]
   enabled = false
   host = localhost:25
   user =
   # If the password contains # or ;, it must be enclosed in triple quotes. ex """#password;"""
   password =
   cert_file =
   key_file =
   skip_verify = false
   from_address = admin@grafana.localhost
   from_name = Grafana
   ehlo_identity =

   [email]
   welcome_email_on_sign_up = false
   templates_pattern = emails/*.html
   ```

- **Reset admin password**: run the command `grafana-cli admin reset-admin-password admin123` in the container

- **Upgrade**: Follow the instruction to [Upgrade Grafana](https://grafana.com/docs/installation/upgrading/)


## Troubleshooting{#troubleshooting}

#### How do I change the database?

Prepare the database, then select **My Apps > compose > Go to Edit Repository > .env**. Add the **GF_DATABASE_URL** environment variable to the  **.env** file, and rebuild the application to apply the changes.
```
# mysql example
GF_DATABASE_URL=mysql://grafana:123456@172.17.0.1:3306/grafana
```
