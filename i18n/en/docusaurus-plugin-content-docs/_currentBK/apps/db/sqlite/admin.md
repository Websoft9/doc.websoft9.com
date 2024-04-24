---
sidebar_position: 3
slug: /sqlite/admin
tags:
  - SQLite
  - DevOps
---

# SQLite Maintenance

This chapter is special guide for SQLite maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### SQLite Backup

The general steps to make a manual backup are as follows:

1. Compress and download the SQLite database file (.db) by SFTP.
2. Complete a backup.

### SQLite Upgrade

If there no newer rpm/deb package for you SQLite, you should update it as below steps:  

> You should complete an image or snapshot backup for instance before upgrade

1. Access the [Download](https://www.sqlite.org/chronology.html) URL of SQLite

2. Run these commands
   ```
   # Download sources of SQLite, the URL below only for your reference
   wget https://www.sqlite.org/2019/sqlite-autoconf-3290000.tar.gz

   # Make it
   tar zxvf sqlite-autoconf-3290000.tar.gz 
   cd sqlite-autoconf-3290000/
   ./configure --prefix=/usr/local
   make && make install
   
   # Replace the old version
   mv /usr/bin/sqlite3  /usr/bin/sqlite3_old
   ln -s /usr/local/bin/sqlite3   /usr/bin/sqlite3
   echo "/usr/local/lib" > /etc/ld.so.conf.d/sqlite3.conf
   sudo echo "/usr/local/lib" |tee /etc/ld.so.conf.d/sqlite3.conf
   ldconfig
   sqlite3 -version
   ```

## Troubleshoot{#troubleshoot}

In addition to the SQLite issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### How can I use CloudBeaver to manage SQLite databases?

CloudBeaver just only manage database in the directory: */data/apps/cloudbeaver/volumes*

## FAQ{#faq}

#### Does SQLite need username and password?

No

#### What is the installation method of SQLite in this project?

Make

#### SQLite 有系统服务吗？

没有