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

Use Caddy on Websoft9 for the following:

- Deploy a static website
- Running the reverse proxy service for application

### Deploy a static website

1. When completed installation of Caddy at **Websoft9 Console**, get the applicaiton's overview and **access** information from **My Apps**  

2. Refer to [Deploying Applications Based on Program Environment](./runtime) to deploy a static website.

### Reverse proxy applications

Follow the steps below to learn Caddy's reverse proxy:

1. Select **Websoft9 Console > App Store**, install applications **Netdata** and **Caddy**

2. Select **My Apps > Caddy > Compose > Go to Edit Repository**, modify the *src/Caddyfile* as follows:
   ```
   :80 {
    reverse_proxy http://netdata_h31py:19999
   }
   ```

3. Restart the Caddy application, access Caddy URL, and you will see the Netdata page

In the Websoft9, the Netdata access is routed: `User browser> Websoft9 Gateway > Caddy > Netdata container`

## Configuration options{#configs}

- Application root directory in the container: */srv*
- Caddy container port: `80`
- [API](https://caddyserver.com/docs/quick-starts/api)
- CLI: `caddy help`
- Configuration [template](https://caddy.community/c/wiki/13)
- Caddy configuration file in container(have mounted bind): */etc/caddy/Caddyfile*

## Administer{#administrator}

## Troubleshooting{#troubleshooting}
