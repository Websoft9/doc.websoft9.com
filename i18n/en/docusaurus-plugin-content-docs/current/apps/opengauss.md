---
title: openGauss
slug: /opengauss
tags:
  - Databases
  - Relational
  - SQL
---

import Meta from './_include/opengauss.md';

<Meta name="meta" />

## Getting started{#guide}

### Connecting to the Database

1. After installing openGauss in the Websoft9 console, view the application details through “My Applications” and get the username and password in the “Access” tab.

2. Enter the command mode of the openGauss container and use gsql to connect to the database:

    ```
    root@58ddfa53f5a8:/# su - omm
    omm@58ddfa53f5a8:~$ gsql -d postgres -U gaussdb
    # Get passwords in the input access tab
    Password for user gaussdb: 
    gsql ((openGauss 6.0.0 build aee4abd5) compiled at 2024-09-29 19:14:27 commit 0 last mr  )
    Non-SSL connection (SSL connection is recommended when requiring high-security)
    Type "help" for help.

    openGauss=>
    ```

## Configuration options{#configs}

- CLI

## Administer{#administrator}

## Troubleshooting{#troubleshooting}