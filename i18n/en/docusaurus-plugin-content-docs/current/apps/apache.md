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

- Running static websites directly
- As a reverse proxy service (Apache reverse proxy is not recommended)

The Apache container does not contain PHP, so if you want to deploy a PHP website, run the [PHP](. /php) container through the Websoft9 console.  

### Deploy a static website

1. After installing Apache in the Websoft9 console, view the application details through "My Applications" and get the access information in the "Access" tab.

2. Click on the URL to see a static page for demonstration purposes.

3. Refer to: [Deploying Applications Based on Program Environment}(runtime) to deploy a static website.

### Mount the httpd.conf configuration file

Although the Apache configuration file can be modified with the `sed` command, it is recommended that it be mounted outside the container:

1. Enter the Apache container and copy the contents of the file: */usr/local/apache2/conf/httpd.conf*

2. Select **My apps > Apache application > Compose > Prompt Adjustment**, go to your application's Git repository 

3. Paste the copied httpd.conf contents into *./src/httpd.conf*, and then modify the **docker-compose.yml** mount settings

4. Rebuild the container to take effect

### Setup pseudo-static

There are three steps to using and setting up Apache pseudo-static:

- Ensure that the Rewirte module is installed and enabled.
- Make sure the Rewirte module is installed and enabled.
- Configure pseudo-static rules in the .htaccess file in the root directory of your website.

### Concurrent connection settings

The following contents of the configuration file can be used as concurrent connection related settings:

```
<IfModule prefork.c>
   StartServers        5
   MinSpareServers     5
   MaxSpareServers     10
   MaxClients          256
   MaxRequestsPerChild 3000
</IfModule>
```

## Configuration options{#configs}

- Apache container port: 80
- CLI: `httpd -h`
- Apache [official documentation](https://httpd.apache.org/docs/2.4/)
- Apache [Container Usage Guide](https://hub.docker.com/_/httpd)
- Apache configuration file:*/usr/local/apache2/conf/httpd.conf*

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### You don't have permission...?

Error details: You don't have permission to access/on this server  
Solution:

1. Check the permissions of the web directory
2. Check whether the Apache configuration file has "AllowOverride All Require all granted" related content.

#### Apache Frequent 403 Errors?

A 403 error is a type of error message during website access that indicates access is prohibited or service is denied. There are two scenarios when a 403 error occurs:

- The server has been passively attacked by a human-saturated DoS or DDoS malicious attack, resulting in the server being unable to provide normal service.
- The server's active defense measures (Apache's mod_evasive module), when a short period of time, an IP continuously send requests to the server, the server to start the DoS defense policy, the use of preset rules to actively refuse to provide services to a certain IP