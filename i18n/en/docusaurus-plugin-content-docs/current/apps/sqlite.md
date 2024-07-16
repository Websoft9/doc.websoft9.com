---
title: SQLite
slug: /sqlite
tags:
  - SQL Server
  - Cloud Database
---

import Meta from './_include/sqlite.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of SQLite at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Enter the command mode of the SQLite container and run the `sqlite3` command.
   ```
   [root@VM-0-11-centos ~]# sqlite3
   SQLite version 3.29.0 2019-07-10 17:32:03
   Enter ".help" for usage hints.
   Connected to a transient in-memory database.
   Use ".open FILENAME" to reopen on a persistent database.
   sqlite>
   ```

## Configuration options{#configs}

- CLI: `sqlite3 --help`

## Administer{#administrator}

- Upgrade: Binary Replacement and  sqlite3.conf Migration

## Troubleshooting{#troubleshooting}

