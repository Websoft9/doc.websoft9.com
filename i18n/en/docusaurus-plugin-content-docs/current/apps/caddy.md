---
title: Caddy
slug: /caddy
tags: /caddy
  - HTTP Server
  - https
  - Microservice
  - Cloud Native
---

import Meta from './_include/caddy.md';

<Meta name="meta" />

## Getting started{#guide}

Websoft9 provides two uses for the Caddy:

- Run static websites directly
- As a reverse proxy service

We'll explain how to use each of them in more detail below.

### Deploy a static website

1. When completed installation of Caddy at **Websoft9 Console**, get the applicaiton's overview and **access** information from **My Apps**  

2. Refer to [Deploying Applications Based on Program Environment](runtime) to deploy a static website.

### Reverse proxy applications

Follow the steps below to experience the power of Caddy's reverse proxy:

1. Select **Websoft9 Console > App Store**, install applications **Netdata** and **Caddy**

2. Select **My Apps > Caddy > Compose > Prompt Adjustment**, modify the *src/Caddyfile* as follows:
   ```
   :80 {
    reverse_proxy http://netdata_h31py:19999
   }
   ```

3. Restart the Caddy application, access by the Caddy URL, and you will see the Netdata page

In the Websoft9 hosting platform, the above Netdata access is routed: User > Websoft9 Gateway > Caddy > Netdata

## Configuration options{#configs}

- Application root directory in the container: */srv*
- Caddy container port: 80
- Monitor wildcard writing for all URLs: `:80`
- [API](https://caddyserver.com/docs/quick-starts/api)
- CLI: `caddy help`
- Configuration [template](https://caddy.community/c/wiki/13)
- Caddy configuration file: */etc/caddy/Caddyfile*, bind mount to */src/Caddyfile*

## Administer{#administrator}

## Troubleshooting{#troubleshooting}