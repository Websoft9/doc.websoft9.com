---
title: HAProxy
slug: /haproxy
tags:
  - HA
  - Load Balancing
  - HTTP Server
  - High Availability
---

import Meta from './_include/haproxy.md';

<Meta name="meta" />

## Getting started{#guide}

### Login verification{#verification}

1. Completed installation HAProxy at **Websoft9 console**, get the applicaiton's overview and access credentials from **My Apps**.  

2. Set the password in the configuration file.

### Enable HAProxy Monitoring

HAProxy Statistics Report is set by default and can be viewed through the **Websoft9 console > access > Backend**.   

### High Availability

Deploy Keepalived for high availability of HAProxy.

### Cluster Configuration

To enable HAProxy clustering, add cluster server info to the configuration file.  
Examples are as follows:
  ```
  ## HTTP Site Configuration]
  listen http_web 192.168.10.10:80
          mode http
          balance roundrobin # Load Balancing algorithm
          option httpchk
          option forwardfor
          server server1 192.168.10.100:80 weight 1 maxconn 512 check
          server server2 192.168.10.101:80 weight 1 maxconn 512 check

  # [HTTPS Site Configuration]
  listen https_web 192.168.10.10:443
          mode tcp
          balance source# Load Balancing algorithm
          reqadd X-Forwarded-Proto: http
          server server1 192.168.10.100:443 weight 1 maxconn 512 check
          server server2 192.168.10.101:443 weight 1 maxconn 512 check
  ```

## Configuration options{#configs}

- Configuration file (mounted): */usr/local/etc/haproxy/haproxy.cfg*
- Cli: `haproxy`
- [HAProxy APIS](https://www.haproxy.com/blog/haproxy-apis/)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

