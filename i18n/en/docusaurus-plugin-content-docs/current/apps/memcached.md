---
title: Memcached
slug: /memcached
tags:
  - Cached Databases
  - In-Memory Computing
  - Acceleration
---

import Meta from './_include/memcached.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Memcached at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

### Login to the Console

**Memcached-admin** is pre-built in this application orchestration but is not enabled by default. If you need to enable it, please refer to the following steps:

1. Select **Websoft9 console > My apps > compose > Go to Edit Repository**.

2. Modify the Memcached docker-compose.yml.

   - Host ports in the ports element
   - Remove the profiles element.

3. After rebuilt the application, your can access the control panel through `http:/URL:port`.
  ![Memcached-admin](./assets/memcached-gui-websoft9.png)

### Telnet Connection

1. Run the telnet command to connect to Memcached.

   ```
   telnet 127.0.0.1 11211
   Trying 127.0.0.1...
   Connected to 127.0.0.1.
   Escape character is '^]'.
   ^]'.
   ```

3. Connected successfully, the system enters the Memcached CLI, and inputs the command `stats`.

   ```
   $ stats
   STAT pid 651
   STAT uptime 891
   STAT time 1585225158
   STAT version 1.4.15
   STAT libevent 2.0.21-stable
   ...
   ```

## Configuration options{#configs}

- Client command: [Memcached Commands](https://github.com/memcached/memcached/wiki/Commands) is run through Telnet.
- Server-side commands: `memcached -h`.
- Memcached-admin: You need to modify the compose file to enable it.

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

