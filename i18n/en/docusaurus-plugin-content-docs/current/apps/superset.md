---
title: Superset
slug: /superset
tags:
  - Superset
  - Big Data Analytics
  - BI
---

import Meta from './_include/superset.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Superset at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Access the login page through your browser 

3. Enter your password and login to the Superset backend.  
   ![](./assets/superset-console-websoft9.png)

### Analyzing data

1. After logining to Superset, open the **Datasets** page and create a new database connection.

2. After successful connection, the system will import the database tables.

3. Start analyzing the table.

## Configuration options{#configs}

- Multilingual(✅):Support for background switching
- CLI: `superset [OPTIONS] COMMAND [ARGS]...`
- [Configuration file](https://github.com/apache/superset/blob/master/superset/config.py)：*./src/docker/pythonpath_dev/superset_config.py*
- SMTP(0✅): Add the following SMTP configuration segment in the configuration file and it will take effect after restarting the application.

   ```
   # smtp server configuration
   EMAIL_NOTIFICATIONS = True  # all the emails are sent using dryrun
   SMTP_HOST = 'smtp.163.com'
   SMTP_STARTTLS = True
   SMTP_SSL = True
   SMTP_USER = 'websoft9@163.com'
   SMTP_PORT = 465
   SMTP_PASSWORD = '#wwBJ8'
   SMTP_MAIL_FROM = 'websoft9@163.com'
   ```

## Administer{#administrator}

- Replacement of Logo: Replacement of Container Files */app/superset/static/assets/images/superset-logo-horiz.png*
- Password recovery: After running the following SQL statement in the Superset database, the password for user `admin` is set to `admin123`.
   ```
   update ab_user set password='pbkdf2:sha256:150000$w8vfDHis$b9c8fa353137417946766ed87cf20510da7e1e3a7b79eef37426330abef552bf' where username='admin';
   ```
- Install database driver: Superset needs to install [database driver](https://superset.apache.org/docs/databases/installing-database-drivers) in the container to connect to the corresponding database.
   ```
   # Example: Installing the MySQL driver
   pip install mysqlclient

   # Example: Installing the PostgreSQL driver
   pip install psycopg2

   # Example: Installing the PostgreSQL driver via the pip mirror repository to solve a slow network problem
   pip install psycopg2 -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```


## Troubleshooting{#troubleshooting}

#### Superset Container Installation Driver Error?

**Phenomenon description**: ERROR: Could not install packages due to an OSError: [Errno 13]
Check the permissions.

**Cause Analysis**: Insufficient permissions

**Solution**: Enter the container command mode as `root` and install the driver.

