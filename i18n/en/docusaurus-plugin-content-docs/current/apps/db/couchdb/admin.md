---
sidebar_position: 2
slug: /couchdb/admin
tags:
  - CouchDB
  - Cloud Native Database
---

# CouchDB Maintenance

This chapter is special guide for CouchDB maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### CouchDb Backup

CouchDB has three different types of files it can create during runtime:Database files，Configuration files，Log files 
Refer to the official docs：[Backing up CouchDB](https://docs.couchdb.org/en/latest/maintenance/backups.html)

### CouchDB Upgrade

Refer to the official docs: [Upgrading CouchDB](https://docs.couchdb.org/en/latest/install/upgrading.html)

## Troubleshoot{#troubleshoot}

In addition to the CouchDb issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### CouchDB service can't start?

1. Execute `systemctl status couchdb` and you can see the errors

2. Search the keywords **Failed** or **error** from logs: */data/logs/couchdb-server*

## FAQ{#faq}

#### If there is no domain name, can I deploy CouchDB?

Yes, visit CouchDB by *http://Internet IP/_utils*