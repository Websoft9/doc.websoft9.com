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

### WordPress Setting up the Varnish Cache 

1. Install the WordPress and Varnish applications in the Websoft9 console 
    > Make sure that the domain name configured for Varnish is the one that will eventually be made available for users to access 

2. Edit the Varnish application's `. /src/default.vcl` file with the WordPress container name and container port as the connection point 
  ``` 
    backend default { 
    .host = "wordpress_shlez"; 
    .port = "80"; 
    } 
  ```
3. rebuild the Varnish application, Varnish has cached WordPress.

4. Visiting the domain that Varnish is bound to, you can see that the access speed is greatly improved! 

## Configuration options{#configs}

## Administer{#administrator}

## Troubleshooting{#troubleshooting}