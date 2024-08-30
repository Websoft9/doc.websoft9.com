---
title: SQLServer
slug: /sqlserver
tags:
  - SQL Server
  - Cloud Database

---

import Meta from './_include/sqlserver.md';

<Meta name="meta" />

### Intellectual Property Statement {#license}

The SQLServer covered in this document are all Express editions and may be used or distributed free of charge [(detailed terms)](https://www.microsoft.com/zh-cn/download/details.aspx?id=29693)

- Linux Server for: SQL Server Express 2017 2019 2022

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of SQLServer at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Complete the install wizard step by step

### Client Remote Connection

SQL Server installed under Linux can be used to connect to the database remotely through a client tool as long as the server allows it:

1. Install the common database management tool [CloudBeaver](./cloudbeaver)

2. Login to CloudBeaver and create a new SQL Server connection.

You can also install tools such as Navicat on your local computer to manage the database.


## Configuration options{#configs}

- Path on Linux

  - Data directory (mounted):*/var/opt/mssql*

- Command line: [mssql-cli](https://docs.microsoft.com/en-us/sql/tools/mssql-cli)

- To change the database path: Under SQL Server Enterprise Manager **Properties**, open the **Database Settings** tab under **Database Default Location**.

- [Express upgrades to other versions of SQL Server](https://docs.microsoft.com/zh-cn/sql/database-engine/install-windows/upgrade-to-a-different-edition-of-sql-server-setup?view=sql-server-ver15)


## Administer{#administrator}

### Manual backup {#backup}

The generic manual backup procedure is as follows:

1. SQL Server Enterprise Manager: Right-click the target database and select **Tasks > Backup** to bring up the Backup Database window. 

2. Follow the backup wizard to complete the backup step by step

### Auto Backup {#autobackup}

SQL Server Express does not have a SQL Server Agent service, i.e. you cannot directly use the automatic backup feature that comes with SQL Server.  

However, there are still alternative autobackup solutions that are widely used:

- Use [SQL Backup Master](https://www.sqlbackupmaster.com/), a professional free backup tool (recommended).
  ![](./assets/sqlserver-sqlbackupmaster-websoft9.png)

- Write a backup script and run it in a scheduled task on your Windows system.


## Troubleshooting{#troubleshooting}

#### Can't login with SQLServer password?

Reference: enable password

#### SQLServer local connection failed?

Please check if the server name is correct: in **Server Name** by **Browse More...** Select the correct server

#### Backup failed: ensure correct media...?

Reason: This is not a failure of the database itself, but a problem with the usage of the backup.  
Solution: Remove a backup file, and overwrite it in the existing backup for each backup.

