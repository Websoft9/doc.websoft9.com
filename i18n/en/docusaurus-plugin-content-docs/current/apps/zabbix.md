---
title: Zabbix
slug: /zabbix
tags:
  - console
  - other
---

import Meta from './_include/zabbix.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Zabbix at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Visit the application URL to access the login screen

3. Successfully log in to the Zabbix backend
   ![](./assets/zabbix-dashboard-websoft9.png)

### Login verification{#verification}

1. Install Zabbix-Agent on the target host (container installation is recommended).

2. After logging in to the Zabbix console, open: "Configuration" > "Hosts", add a new host, fill in the connection information of the target host.

3. Refresh the host list page and the hosts in the columns show **Green** which indicates successful monitoring.

## Configuration options{#configs}

- SMTP（✅）: background "Management" > "Alarm Media Type" > "Email".

- Multilingual（✅）: switch by background User Profile, no target language needs to be installed first [How to install locale](https://www.zabbix.com/community)

- Monitor objects: Monitor various IT components, including networks, servers, virtual machines and cloud services.

- Components: Zabbix-Server, Zabbix-Web, Zabbix-Proxy, Zabbix-Agent, Zabbix-java-gateway.

## Administer{#administrator}

- Reset password: Run SQL `update zabbix.users set passwd=md5(new_password) where alias='Admin` in Zabbix database.

## Troubleshooting{#troubleshooting}


