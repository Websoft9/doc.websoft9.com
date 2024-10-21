---
title: RethinkDB
slug: /rethinkdb
tags:
  - RethinkDB
  - Cloud Native Database
---

import Meta from './\_include/rethinkdb.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. After completing the installation of RethinkDB in the **Websoft9 Console**, retrieve the application's **Overview** and **Access** information from **My Apps**.

   - The username and password displayed are for the database account, not the console account.
   - The console does not require account authentication.

2. Use a browser on your local computer to access the RethinkDB console:
   ![](./assets/rethinkdb-gui-websoft9.png)

### Running Commands in Data Explorer

Most operations can be performed by running ReQL commands directly in the Data Explorer interface of the console:

- Change password:
  ```bash
  r.db('rethinkdb').table('users').get('admin').update({password: 'newpassword'})
  ```
- Clear password:
  ```bash
  r.db('rethinkdb').table('users').get('admin').update({password: ''})
  ```
- Add a user:
  ```bash
  r.db('rethinkdb').table('users').insert({
      id: 'new_username',
      password: 'new_password'
  })
  ```

## Configuration Options {#configs}

- Server CLI: `rethinkdb -h`

- Backup and Restore:

  - `rethinkdb export abc.db`
  - `rethinkdb dump [options]`
  - `rethinkdb import -d [options]`

- Client Command Line: The client CLI is not provided, only the development package is available [RethinkDB client drivers](https://rethinkdb.com/docs/install-drivers/).

- Configuration File:

  - Input personalized configuration through commands in the docker-compose.yml file (recommended).
  - Container path: `/etc/rethinkdb/instances.d/instance.conf` for the instance configuration file.

- Query Language: [ReQL](https://rethinkdb.com/docs/introduction-to-reql/)

## Administration {#administrator}

## Troubleshooting {#troubleshooting}
