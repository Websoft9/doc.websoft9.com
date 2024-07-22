---
title: Redis
slug: /redis
tags:
  - Cache
  - databases
---

import Meta from './_include/redis.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Redis at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

### Connectivity Usage

There are two ways to verify Redis availability:

- Enter the command line mode of the Redis container and run `redis-cli` for interactive use
- Install [Redis Insight](./redisinsight) on the Websoft9 console, and then enter the Redis


## Configuration options{#configs}

- Data persistence: enabled by default
- Extranet access: already enabled by `-bind 0.0.0.0` in container command
- [ACL](https://redis.io/topics/acl) authentication: enabled by default
- [Redis API](https://docs.redis.com/latest/rs/references/rest-api/)
- [Redis-CLI](https://redis.io/topics/rediscli): `redis-cli help`
- Configuration file: This application lacks a configuration file by default, so select **My Apps > Compose > Go to Edit Repository > docker-compose.yml** and set by the **command** directive

## Administer{#administrator}

- Reset the password: enter the Redis container CML mode, run `redis-cli` to enter the interactive, and then run `CONFIG SET requirepass "newpassword"`

## Troubleshooting{#troubleshooting}
