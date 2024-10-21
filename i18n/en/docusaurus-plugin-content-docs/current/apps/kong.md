---
title: Kong
slug: /kong
tags:
  - API
  - gateway
  - Nginx
---

import Meta from './_include/kong.md';

<Meta name="meta" />

## Getting started{#guide}

### Install Verification{#verification}

Completed the installation of Kong at the Websoft9 console, and get the applicaiton's overview and access credentials from **My Apps**  

1. Kong services: Kong operates with three services: Kong HTTP, Kong Admin API, and Kong GUI. Open the necessary ports based on your access method:
   - Access by domain: Only enable the Kong Admin API port
   - Access by IP and Port: Enable the Kong HTTP port, Kong Admin API port, and Kong GUI port

2. Local browser access:
   - Access by domain: `http://domain/admin`
   - Access by IP and Port: `http://Internet IP:Kong GUI port/admin`

3. Verify Kong HTTP service
   ```
   curl -i -X GET --url http://URL/services
   ```

4. Configure the Kong Admin API through the Kong Manager backend or using `curl`

### Kong Manager Authentication

Kong Manager OSS does not support account and password authentication by default. Set access control through the **Websoft9 Gateway**.

### Kong Admin API Authentication

Use Kong authentication plugins for access control, such as Key Authentication, Basic Authentication, or OAuth 2.0 Authentication

For details, refer to: [Authentication Reference](https://docs.konghq.com/gateway/latest/kong-plugins/authentication/reference/)

## Configuration options{#configs}

- GUI console Kong Manager OSS(✅): Note that only the enterprise distribution supports account and password authentication

- [Kong CLI](https://docs.konghq.com/gateway/latest/reference/cli)(✅)

- Kong Manager interface: `http://URL/admin`

- Port description:
  - Kong HTTP Port(Gateway HTTP service API port)
  - Kong Admin API Port(Management API service port)
  - Kong GUI Port(Management GUI console port)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}
