---
title: Zabbix
slug: /zabbix
tags:
  - console
  - other
---

import Meta from './\_include/zabbix.md';

<Meta name="meta" />

## Getting Started {#guide}

1. After completing the installation of Zabbix via the **Websoft9 Console**, retrieve the application’s **Overview** and **Access** information from **My Apps**.

2. Visit the application URL to access the login screen.

3. Log in to the Zabbix backend successfully.
   ![](./assets/zabbix-dashboard-websoft9.png)

### Login Verification {#verification}

1. Install **Zabbix-Agent** on the target host (container installation is recommended).

2. After logging in to the Zabbix console, navigate to **Configuration > Hosts**, add a new host, and fill in the connection information for the target host.

3. Refresh the host list page; if the hosts show **Green**, monitoring is successful.

## Configuration Options {#configs}

- **SMTP (✅)**: Configure SMTP under **Management > Alarm Media Type > Email**.
- **Multilingual (✅)**: Switch language via **User Profile**. [How to install locale](https://www.zabbix.com/community).
- **Monitor Objects**: Zabbix supports monitoring of various IT components, including networks, servers, virtual machines, and cloud services.
- **Components**: Includes Zabbix-Server, Zabbix-Web, Zabbix-Proxy, Zabbix-Agent, and Zabbix-java-gateway.

## Administration {#administrator}

- **Reset Password**: To reset the admin password, run the following SQL command in the Zabbix database:
  ```sql
  update zabbix.users set passwd=md5('new_password') where alias='Admin';
  ```

## Troubleshooting {#troubleshooting}

1. **Connection Issues**:

   - **Symptom**: Unable to connect to the Zabbix server or dashboard.
   - **Solution**: Check that the necessary ports are open and the Zabbix components are properly configured.

2. **Agent Not Showing in Host List**:
   - **Symptom**: The Zabbix-Agent host is not appearing in the host list.
   - **Solution**: Verify the agent is correctly installed on the target host and the connection details are accurate.
