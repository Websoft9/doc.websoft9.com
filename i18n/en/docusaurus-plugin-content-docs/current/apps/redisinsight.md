---
title: RedisInsight
slug: /redisinsight
tags:
  - Redis
  - Visualization
  - GUI
---

import Meta from './_include/redisinsight.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

After installing Redash in the Websoft9 console, view the application details through **My Applications** and get URL in the **Access** tab

### Connecting to a Redis Database {#wizard}

1. Prepare the Redis database (you can install [Redis](./redis) through the Websoft9 App Store)

2. Open the RedisInsight interface, accept the license, and start using it
   ![Open RedisInsight](./assets/redisinsight-backend-websoft9.png)

3. Click **Add Database Manually** to connect to the Redis database.

   * HOST:
     - Intranet: IP/Container name/Service name
     - Extranet: Get URL from service provider

   * Port: 6379

   * Name: redis

   * Username: empty

   * Password: Redis database password


## Configuration options{#configs}

- Connect to multiple databases(✅)
- Console Authentication: RedisInsight Console without Account Authentication

## Administer{#administrator}


