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

Completed installation Kong at Websoft9 console, get the applicaiton's overview and access credentials from "My Apps"  

1. Kong has three services: Kong HTTP, Kong Admin API, and Kong GUI. Ports need to be opened as needed
   - If access by domain: simply enable the Kong Admin API port
   - If access by ip and port: it is necessary to enable Kong HTTP port, Kong Admin API port , and Kong GUI port

2. Local browser access to the Kong Manager interface:
   - Access by domain: `http://domain/admin`
   - Access by ip and port: `http://IP:Kong GUI Port/admin`

3. Verify Kong HTTP service
   ```
   curl -i -X GET --url http://URL/services
   ```

4. Configure the Kong Admin API through the Kong Manager backend or curl

### Kong Manager Authentication

Kong Manager OSS access is not supported account and password authentication by default. Users need to set access control for it through the **Websoft9 Gateway**.

### Kong Admin API Authentication

To set up authentication access for the Kong Admin API, you can use Kong's own authentication plugin. Kong provides various authentication plugins, For example, Key Authentication, Basic Authentication, OAuth 2.0 Authentication, etc. 

Detail refer to: [Authentication Reference](https://docs.konghq.com/gateway/latest/kong-plugins/authentication/reference/)

## Configuration options{#configs}

- GUI console Kong Manager OSS (√): Only the enterprise distribution supports account and password authentication

- [Kong CLI](https://docs.konghq.com/gateway/latest/reference/cli) (√)

- Management access method: URL/admin(Changed Kong's default settings)

- Port Description:
  - Kong HTTP Port(Gateway HTTP service API port)
  - Kong Admin API Port(Management API service port)
  - Kong GUI Port(Management GUI console port)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}
