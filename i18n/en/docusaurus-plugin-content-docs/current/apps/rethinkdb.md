---
title: RethinkDB
slug: /rethinkdb
tags:
  - RethinkDB
  - Cloud Native Database
---

import Meta from './_include/rethinkdb.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of RethinkDB at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

   - The user name and password displayed on the page are the database account, not the console account
   - The console does not need account authentication

2. Use the browser on your local computer and go to the RethinkDB console
   ![](./assets/rethinkdb-gui-websoft9.png)

### Running commands in Data Explorer 

Most of the operations can be achieved by running the ReQL command directly Data Explorer interface in the console :

- Change password:
  ```
  r.db('rethinkdb').table('users').get('admin').update({password: 'newpassword'})
  ```
- Clear password:
  ```
  r.db('rethinkdb').table('users').get('admin').update({password: 'newpassword'})
  ```
- Add a user:
  ```
   r.db('rethinkdb').table('users').insert({
      id: 'new_username',
      password: 'new_password'
   })
  ```

## Configuration options{#configs}

- Server command line: `rethinkdb -h`

- Backup and Restore:
  - `rethinkdb export abc.db`
  - `rethinkdb dump [options]`
  - `rethinkdb import -d [options]`

- Client command line: The client CLI is not provided, only the development package is provided [RethinkDB client drivers](https://rethinkdb.com/docs/install-drivers/)  
- Configuration file:
  - Input personalized configuration through command in docker-compose.yml file (recommended)
  - Container */etc/rethinkdb/instances.d/instance.conf* increase the configuration file of instance.conf

- Query language: [ReQL](https://rethinkdb.com/docs/introduction-to-reql/) 

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

