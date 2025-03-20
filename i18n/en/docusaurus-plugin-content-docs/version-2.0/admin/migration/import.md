---
sidebar_position: 1
slug: /migration-to-websoft9
---

# Migrate to Websoft9

Websoft9 applications hosting platform that can host websites, business software, databases and other types of applications.   

Therefore, migrating distributed applications to Websoft9 for unified management is a common requirement.   

This chapter describes how to migrate applications to Websoft9.  

## Prepare

Prepare the following before migrating your application to Websoft9: 

1. [Install Websoft9 Console](./install) to your target server 

2. Backup all HTTP server configurations for your source server

3. Install the migration tools in the **Websoft9 Console** as follows

   - [phpMyAdmin](./phpmyadmin)
   - [Syncthing](./syncthing)
   - [Duplicati](./duplicati)

4. Binding domain to target server

## Migration Samples

#### Migrating WordPress

1. Export your database to SQL file for your source WordPress

2. Compress the source WordPress **wp-content** folder to zip file

3. Install **WordPress** at your target server by Websoft9 Console and make sure it can be access

4. Recover source WordPress to target server

   - Import SQL file by phpMyAdmin for new WordPress
   - Delete **wp-content** folder of new Wordpress, then unzip **wp-content** zip file to the same path
   - Run command `chown -R user:gourp /var/www/html/wp-content` in WordPress container

5. Change domain URL at WordPress

6. Testing new WordPress


#### Migrating Databases

Tools must be used to migrate databases, and there are three types of tools for database migration:

- Database Original Vendor Tools, e.g mysqldump
- Tools at Websoft9 App Store, e.g phpMyAdmin
- Other online SaaS/PaaS tools

## Post migration

There are some important tasks after the migration:

- Domain name re-resolution and binding
- Fix file or folder permission
- Verify application's account availability
- Fix [root URL](./url) of application
- Delete source application



