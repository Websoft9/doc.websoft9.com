---
title: Zabbix
slug: /zabbix
tags:
  - DevOps
  - 监控
  - 日志
---

import Meta from './\_include/zabbix.md';

<Meta name="meta" />

## Getting Started {#guide}

### Log in to the Backend {#wizard}

After installing Zabbix in the Websoft9 console, you can view the application details through “My Applications” and get the login information in the “Access” tab.

1. Access the application URL, and go to the login screen

2. Successfully log in to the Zabbix backend.
   ! [](. /assets/zabbix-dashboard-websoft9.png)

### Adding a Monitored Host

1. Install Zabbix-Agent on the target host (container installation is recommended). 2.

2. After logging in to the Zabbix console, open: **Configuration > Hosts**, add a new host, and fill in the connection information for the target host.

3. Refresh the host list page, and the host in the columns shows **green**, which indicates that the monitoring has been successful.

## Configuration options {#configs}

- SMTP (√): background **Management > Alarm Media Type > Email**.

- Multi-language (√): switch by background User Profile, no target language needs to be installed first [How to install locale](https://www.zabbix.com/community)

- What to monitor: Monitor various IT components, including networks, servers, virtual machines, and cloud services.

- Components: Zabbix-Server, Zabbix-Web, Zabbix-Proxy, Zabbix-Agent, Zabbix-java-gateway

## Admin Maintenance {#administrator}

- Reset passwords: run SQL in the Zabbix database `update zabbix.users set passwd=md5(new_password) where alias='Admin`

## Troubleshooting
