---
sidebar_position: 2.1
slug: /migratedb
---

# Replace App database

Websoft9 allows users to migrate the default application database to an external one, ensuring flexibility.   

Follow these steps to connect your application to the specified external database.

## Prerequisites

Switching databases is a meticulous process, requiring thorough preparation:

* Ensure target database type/version is supported
* Ensure target database supports necessary configurations
* Ensure network connectivity between app and target database
* Backup existing application data
* Verify backup data can be imported into target database
* Obtain available database host, port, and credentials

## Migrate and replace database

The following is a general steps for replacing a database:

1. Login to Websoft9 Console, [update the application deployment](./app-compose#dynamic)

2. Modify the database connection strings at `.env` or `docker-compose.yml` file

3. It takes effect after redeploy

## Post-change steps

For production application, you should full test the application after import the database.    

