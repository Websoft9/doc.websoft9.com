---
title: Tinyproxy
slug: /tinyproxy
tags:
  - Lightweight Proxy
  - Proxy Server
  - tinyproxy
---

import Meta from './_include/tinyproxy.md';

<Meta name="meta" />

## Getting started{#guide}

### Using git clone through a proxy

Here's how to use Tinyproxy to implement git clone: 

1. Modify ALLOWED in .env file through console, and changes will take effect after rebuilding the application.

2. Use the following git clone command:
    ```
    git -c http.proxy=http://TinyproxyURL:Port clone --depth=1 https://github.com/Websoft9/docker-library
    ```


## Configuration options{#configs}

- Whitelist Setup: Edit the ALLOWED in the .env file, setting 0.0.0.0/0 means all IPs are allowed to access. Separate all IPs by spaces.

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

