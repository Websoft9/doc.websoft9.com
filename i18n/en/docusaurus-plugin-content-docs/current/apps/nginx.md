---
title: Nginx
slug: /nginx
tags:
  - Directional Proxy
  - HTTP Server
  - Load Balancing
  - Static Sites
---

import Meta from './\_include/nginx.md';

<Meta name="meta" />

## Getting Started {#guide}

Websoft9 provides Nginx applications for two purposes:

- Running static websites directly
- As a reverse proxy service

Below is a detailed description of how to use each of these applications.

### Deploying a Static Website

1. After installing NGINX via the Websoft9 console, view the application details through **My Applications** and retrieve access information from **Access**.

2. Refer to "Deploying Applications Based on a Programmatic Environment (runtime)" to deploy a static website.

### Reverse Proxy Other Applications

Follow these steps to experience the capabilities of NGINX as a directional proxy:

1. Run **Netdata** and **Caddy** from the Websoft9 console **App Store**.

2. Modify `src/default.conf` in **My Applications > NGINX > compose > Go to Edit Repository**, replacing **location /** with the following:

   ```
    location / {
        proxy_pass http://netdata_h31py:19999;
        # Optional proxy settings
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
   ```

3. Restart the NGINX application, access the NGINX URL, and you should see the application pointing to the Netdata page.

On the Websoft9 hosting platform, the above Netdata access is routed as follows: **User > Websoft9 Gateway > NGINX > Netdata**

## Configuration Options {#configs}

- NGINX application root directory (mounted): `/usr/share/nginx/html`
- NGINX Configuration File (mounted): `/etc/nginx/conf.d/default.conf`
- NGINX maximum number of open files: set by `/etc/security/limits.conf`
- NGINX container port: 80
- CLI: `nginx -h`
- NGINX Configuration File [Generator](https://www.digitalocean.com/community/tools/nginx) tool
- Pseudo-static rules [template](https://github.com/Websoft9Archive/role_nginx/tree/main/files/rewrite)

## Administration {#administrator}

## Troubleshooting {#troubleshooting}

#### Enable Gzip for HTML, CSS, JS?

By default, NGINX does not enable Gzip. Add the following code to the configuration file:

```
gzip on;
gzip_types application/xml application/json text/css text/javascript application/javascript;
gzip_vary on;
gzip_comp_level 6;
gzip_min_length 500;
```
