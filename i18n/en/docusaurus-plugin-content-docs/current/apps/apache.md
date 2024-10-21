---
title: Apache
slug: /apache
tags:
  - HTTP server
  - https
  - Micro services
  - Cloud Native
---

import Meta from './_include/apache.md';

<Meta name="meta" />

## Getting started{#guide}

Websoft9 provides Apache applications for two purposes:

- Running static websites
- Reverse proxy service (Not recommended)

The Apache container does not include PHP, so if you want to deploy a PHP website, run the [PHP](./php) container through the Websoft9 console.  

### Deploy a static website

1. After installing Apache via the Websoft9 Console, view the application details under **My Apps** and get the access information from the **Access** tab.

2. Click on the URL to see a static page for demo purposes.

3. Refer to: [Deploying Applications Based on Program Environment](./runtime) to deploy a static website.

### Mount the httpd.conf configuration file

The Apache configuration file can be modified with the `sed` command, but it is recommended to mount it outside the container:

1. Enter the Apache container and copy the contents of the file: */usr/local/apache2/conf/httpd.conf*

2. Select **My apps > Apache > Compose**, then access the Git repository page of your Apache application.

3. Paste the copied `httpd.conf` contents into *./src/httpd.conf*, and then modify the **docker-compose.yml** volume mount settings.

4. **Rebuild** the container to apply the changes.

## Configuration options{#configs}

- Apache container port: `80`
- CLI: `httpd -h`
- Apache [Official documentation](https://httpd.apache.org/docs/2.4/)
- Apache [Container Usage Guide](https://hub.docker.com/_/httpd)
- Apache configuration file:*/usr/local/apache2/conf/httpd.conf*

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### You don't have permission...?

Error details: You don't have permission to access this server  
Solution:

1. Check the permissions of the web directory
2. Verify that the Apache configuration file includes **AllowOverride All Require all granted** directives.

#### Frequent 403 Errors in Apache?

A 403 error indicates that access is prohibited or denied. This error can occur in two scenarios:

- The server has been passively attacked by a high volume of requests (DoS or DDoS attack), causing the server to be unable to provide normal service.
- The server's active defense measures (such as Apache's mod_evasive module) have triggered. This may happen if an IP address sends a high number of requests in a short period, causing the server to implement its DoS defense policy and refuse service to that IP address.
