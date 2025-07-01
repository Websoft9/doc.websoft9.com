---
title: Varnish
slug: /varnish
tags:
  - HTTP Caching
  - Reverse Proxy
  - Varnish
---

import Meta from './_include/varnish.md';

<Meta name="meta" />

## Getting started{#guide}

### Reverse proxy application

1. After installing Varnish in the Websoft9 console, view the application details in **My Applications**.

2. Click **My Apps > Varnish app > Compose > Go to Edit Repository** and edit `src/default.vcl`. 

3. Change .host and .port to the container ID and internal port of the Websoft9 console installation.

4. Rebuild the application, the HTTP cache takes effect, and the speed of accessing the application is greatly accelerated.

## Configuration options{#configs}

## Administer{#administrator}

## Troubleshooting{#troubleshooting}