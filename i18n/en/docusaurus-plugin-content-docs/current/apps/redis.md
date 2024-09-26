---
title: Redis
slug: /redis
tags:
  - Cache
  - databases
---

import Meta from './\_include/redis.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. After completing the installation of Redis in the **Websoft9 Console**, retrieve the application's **Overview** and **Access** information from **My Apps**.

### Connectivity Usage

There are two ways to verify Redis availability:

- Enter the Redis container's command line mode and run `redis-cli` for interactive use.
- Install [Redis Insight](./redisinsight) via the Websoft9 console, then use it to connect to Redis.

## Configuration Options {#configs}

- Data Persistence: Enabled by default.
- Extranet Access: Already enabled with the `-bind 0.0.0.0` setting in the container command.
- [ACL](https://redis.io/topics/acl) Authentication: Enabled by default.
- [Redis API](https://docs.redis.com/latest/rs/references/rest-api/)
- [Redis-CLI](https://redis.io/topics/rediscli): Use `redis-cli help` for command reference.
- Configuration File: This application lacks a configuration file by default. To modify settings, go to **My Apps > Compose > Go to Edit Repository > docker-compose.yml** and configure using the **command** directive.

## Administration {#administrator}

- **Resetting Password**: Enter the Redis container's CML mode, run `redis-cli` to start the interactive shell, and then use the following command to reset the password:
  ```
  CONFIG SET requirepass "newpassword"
  ```

## Troubleshooting {#troubleshooting}
