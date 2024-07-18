---
title: PostgreSQL
slug: /postgresql
tags:
  - Databases
  - Relational
  - SQL
---

import Meta from './_include/postgresql.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of PostgreSQL at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Enter the command mode of the PostgreSQL container and use psql to connect to the database

    ```
    # Test host-based access (password required)
    $ psql -h postgres -U postgres
    Password for user postgres. 
    psql (15.6 (Debian 15.6-1.pgdg120+2))
    Type “help” for help.

    postgres=# 

    # Test local local access (no password required)
    psql -d postgres -U postgres
    ``

### Common SQL statements

```
# Change password
ALTER USER postgres WITH PASSWORD 'postgres'
```

### Graphical tools {#pgadmin}

Reference: [pgAdmin](./pgadmin)

### Remote access

#### Port mapping access

The PostgreSQL application is mapped to the host extranet port by default, so you just need to ensure that the security group is in the correct port  

#### Forwarding Bridge Access

If the PostgreSQL container port is not mapped to the host, it can be accessed through the Websoft9 gateway **Streams** forwarding mode bridge, but you need to ensure:

1. the postgresql.conf configuration entry `listen_addresses = '*'`
2. postgresql.conf configuration `listen_addresses = '*' `. pg_hba.conf configuration `host all all 0.0.0.0/0 md5 `

## Configuration options{#configs}

- Default user: PostgreSQL does not have a regular administrator account, but Websoft9 sets `postgres` as the default account name.
- Clients: psql, clusterdb, pgAdmin, etc
- Server: initdb, pg_ctl, postgres, postmaster, pg_upgrade etc
- [Four types of connection](https://www.cnblogs.com/flying-tiger/p/5983588.html?tdsourcetag=s_pcqq_aiomsg): local, host, hostssl, hostnossl
- [Authentication methods](https://www.postgresql.org/docs/current/auth-methods.html): reject, md5, password, trust, peer, scram-sha-256
- Configuration file (mounted):
  - */var/lib/postgresql/data/postgresql.conf*
  - */var/lib/postgresql/data/pg_hba.conf*
- Command line: `psql`
- [API](https://www.postgresql.org/about/news/postgresql-restful-api-1616/)

## Administer{#administrator}

- **Reset password**: In container command mode, use `psql -d postgres -U postgres` to login without verification, and then run the SQL statement to change the password

## Troubleshooting{#troubleshooting}

