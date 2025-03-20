---
title: Traefik
slug: /traefik
tags:
  - HTTP Server
  - Direction Broker
  - Certificates
  - Gateway
---

import Meta from './\_include/traefik.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. After completing the installation of Traefik via the **Websoft9 Console**, retrieve the application's **Overview** and **Access** information from the **My Apps** section.

2. (Optional) Forward the Traefik Dashboard port (8080) to the external network using the Websoft9 gateway.

## Configuration Options {#configs}

- **Container Ports**:
  - `80`: HTTP service port
  - `8080`: Dashboard port

## Administration {#administrator}

## Troubleshooting {#troubleshooting}

#### Can't access the Traefik Dashboard?

Port 8080 is not mapped directly to the host for security reasons.
