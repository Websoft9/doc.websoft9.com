---
title: Apache Traffic Server
slug: /trafficserver
tags:
  - HTTP Caching
  - Reverse Proxy
  - rafficserver
---

import Meta from './_include/trafficserver.md';

<Meta name="meta" />

## Getting started{#guide}

### Configuring WordPress Caching with Apache Traffic Server

1. Install both WordPress and Apache Traffic Server applications in the Websoft9 console
   > Ensure the domain configured for Apache Traffic Server is the final domain accessible to users

2. Edit relevant parameters in the Apache Traffic Server application's `remap.config` file, using the WordPress container name as the connection point
   ```
    map / http://wordpress_7l1io/
   ```
3. After rebuilding the Apache Traffic Server application, WordPress is now cached by Apache Traffic Server

4. Access the domain name bound to Apache Traffic Server to observe significantly improved access speeds 

## Configuration options{#configs}

## Administer{#administrator}

## Troubleshooting{#troubleshooting}