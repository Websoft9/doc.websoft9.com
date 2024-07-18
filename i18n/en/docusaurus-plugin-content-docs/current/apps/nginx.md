---
title: Nginx
slug: /nginx
tags:
  - Directional Proxy
  - HTTP Server
  - Load Balancing
  - Static Sites
---

import Meta from './_include/nginx.md';

<Meta name="meta" />

## Getting started{#guide}

Websoft9 provides Nginx applications for two purposes:

- Running static websites directly
- as a reverse proxy service

Below is a detailed description of how to use each of these applications

### Deploying a static website

1. After installing NGINX in the Websoft9 console, view the application details through **My Applications** and get access information in the **Access**.    

2. Refer to Deploying Applications Based on a Programmatic Environment (runtime) to deploy a static website.


### Reverse proxy other applications

Refer to the following steps to experience the capabilities of NGINX Directional Proxying:

1. Run a **Netdata** and **Caddy** in the Websoft9 console **App Store**. 

2. Modify src/default.conf in **My Applications > NGINX > compose > Go to Edit Repository** , replacing **location /** with the following
   ```
    location / { 
        proxy_pass http://netdata_h31py:19999;
        # Optional proxy settings
        proxy_set_header Host $host; # Optional proxy settings.
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
   ``

3. Restart the NGINX application, access the NGINX URL, and you will see that the application has pointed to the Netdata page

In the Websoft9 hosting platform, the above Netdata access is routed: **User > Websoft9 Gateway > NGINX > Netdata**

## Configuration options{#configs}

- NGINX application root directory (already mounted): */usr/share/nginx/html*
- NGINX Configuration File (mounted): */etc/nginx/conf.d/default.conf*
- NGINX maximum number of open files: set by */etc/security/limits.conf*.
- NGINX container port: 80
- CLI: `nginx -h`
- NGINX Configuration File [Generator](https://www.digitalocean.com/community/tools/nginx) tool
- Pseudo-static rules [template](https://github.com/Websoft9Archive/role_nginx/tree/main/files/rewrite)

## Administer{#administrator}


## Troubleshooting{#troubleshooting}

#### Enable Gzip for HTML, CSS, JS?

By default Nginx does not enable Gzip, you need to add the following code to the configuration file:

```
gzip on.
gzip_types application/xml application/json text/css text/javascript application/javascript;
gzip_vary on;
gzip_comp_level 6; gzip_min_length
gzip_vary on; gzip_comp_level 6; gzip_min_length 500.
```
