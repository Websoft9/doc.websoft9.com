---
title: Tinyproxy
slug: /tinyproxy
tags:
  - Lightweight Proxy
  - Proxy Server
  - tinyproxy
---

import Meta from './\_include/tinyproxy.md';

<Meta name="meta" />

## Getting Started {#guide}

### Using Git Clone Through a Proxy

Follow these steps to use Tinyproxy for `git clone`:

1. Modify the `ALLOWED` field in the `.env` file via the console. The changes will take effect after you rebuild the application.

2. Use the following command to clone the repository through Tinyproxy:
   ```bash
   git -c http.proxy=http://TinyproxyURL:Port clone --depth=1 https://github.com/Websoft9/docker-library
   ```

## Configuration Options {#configs}

- **Whitelist Setup**: To allow specific IP addresses, edit the `ALLOWED` field in the `.env` file. Using `0.0.0.0/0` will allow all IPs to access. Separate multiple IP addresses with spaces.

## Administration {#administrator}

## Troubleshooting {#troubleshooting}
