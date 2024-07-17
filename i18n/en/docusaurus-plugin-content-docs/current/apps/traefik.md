---
title: Traefik
slug: /traefik
tags:
  - HTTP Server
  - Direction Broker
  - Certificates
  - Gateway
---

import Meta from './_include/traefik.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Traefix at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Optional: Forward Traefik Dashboard port 8080 to extranet by Websoft9 gateway

## Configuration options{#configs}

- Container ports: 80 is the HTTP service port, 8080 is the Dashboard port

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### Can't access Traefik Dashboard?

Port 8080 is not directly mapped to the host for security reasons.
