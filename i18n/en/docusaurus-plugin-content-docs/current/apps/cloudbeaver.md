---
title: CloudBeaver
slug: /cloudbeaver
tags:
  - Database Management
  - Visualization
  - Web Interface
  - MySQL
  - Postgres
  - Oracle
---

import Meta from './_include/cloudbeaver.md';

<Meta name="meta" />

## Getting started{#guide}

### Prepare the database

CloudBeaver is a tool for managing databases. If you don't have a database yet, you can install one through the Websoft9. 

- The Websoft9 provides one-click installation templates for various databases, including MySQL, PostgreSQL, SQLite, SQLServer, and Oracle.
- Databases installed through Websoft9 can be connected to CloudBeaver using the container ID as the Host without the need to open an external network port.

### Verify CloudBeaver Installation

After completing the installation of CloudBeaver in the **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from the **My Apps** section.  

1. Open your local computer's browser and visit the URL to complete the installation wizard step by step.
   ![Initialize CloudBeaver](./assets/cloudbeaver-wizard001-websoft9.png)

2.  Navigate to **Administrator > Connection Management**, and delete the **SQLite-Chinook (Sample)** connection to prevent potential SQL injection attacks.
   ![Initialize CloudBeaver](./assets/cloudbeaver-wizard005-websoft9.png)

3. Go back to the homepage, the default SQLite demo connection should no longer exist.

### Managing Databases

1. Navigate to **Settings > Administration > Connection Management** in the CloudBeaver console, and add the required database connection.
   ![](./assets/cloudbeaver-connection-websoft9.png)

2. Enter the connection information, including the host address, port, account password, and then click **Save**.

3. Test the connection availability.


### Shared Data Connection

A Shared Data Connection allows an administrator to grant access to a team of users by modifying the connection configuration.

1. Configure the connection as shared

   ![](./assets/cloudbeaver-share-set-websoft9.png)

2. Authorize the user

   ![](./assets/cloudbeaver-access-set-websoft9.png)

## Configuration options{#configs}

- Multilingual(✅): Chinese not supported
- Database connection driver: JDBC
- Configuration file: */opt/cloudbeaver/workspace/GlobalConfiguration/.dbeaver/data-sources.json*
- [Supported databases](https://dbeaver.com/databases/)
- Export data(✅): only table export is supported

## Administer{#administrator}

- [Driver managements](https://cloudbeaver.io/docs/Driver-managements/)

## Troubleshooting{#troubleshooting}

#### Failed to connect to Oracle database?

If the account is correct, you still cannot connect to the Oracle database. In this case, check if the CloudBeaver database driver matches the Oracle version. 
