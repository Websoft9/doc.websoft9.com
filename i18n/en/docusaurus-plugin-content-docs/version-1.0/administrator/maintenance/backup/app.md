---
sidebar_position: 3
slug: /administrator/backup_app
---

# Application Backup

Unlike whole [server backups](../administrator/backup_server), application backups primarily backup application-related: source code, configuration files, data, and databases.  

There are two paths for application backup:  

## Automation

The application itself provides automatic backup tools (CLI or GUI) to help users achieve planned automatic backups.  

For details, refer to the application-related chapters.  

## Manual

Manual backup for application is based on the **Exporting source code and database of application** to achieve a minimized backup scheme.

```
- Backup scope: Source code and database of application
- Backup effect: Good
- Backup frequency: You can operate when you need
- Recovery method: Import
- Skill requirement: Easy 
- Automation: manual
```


### Application based on Docker

It is very easy for you backup application based on Docker

```
# backup
docker-compose run --rm backup  

# restore
docker-compose run --rm restore  
```

### Application based on Linux

Below is the steps for you backup application based on Linux:  

1. Just compression and download the entire */data/wwwroot/application** directory by SFTP 
2. Export Database
3. Put the source code file and database file in the same folder, named according to the date
4. Backup completed