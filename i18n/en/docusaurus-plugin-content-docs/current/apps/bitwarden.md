---
title: Bitwarden
slug: /bitwarden
tags:
  - Secure Password Storage
  - Password Management
  - bitwarden
---

import Meta from './_include/bitwarden.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Bitwarden at Websoft9 console, get the applicaiton's overview and access information from "My Apps"  

2. Ensure that you have the ID and Key for the installation. If not, go to the Bitwarden to [applicate](https://bitwarden.com/host) and rebuild the container by **Compose**.  

3. Set up the Bitwarden application for HTTPS access (required)

4. Access Bitwarden via the domain name and start initialization (including creation of the initial administrator account)

## Configuration options{#configs}

- Multilingual (√)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### Initialization fails to create account ?

Must use https access, otherwise account creation fails.