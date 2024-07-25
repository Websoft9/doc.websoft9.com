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

1. After completing the installation of Bitwarden on the Websoft9 console, get the applicaiton's overview and access information from **My Apps**  

2. Ensure that you have the ID and Key for the installation. If not, go to the Bitwarden at [applicate](https://bitwarden.com/host) and rebuild the container using **Compose**.  

3. Set up the Bitwarden application for HTTPS access (this is required)

4. Access Bitwarden through the domain and start the initialization process (including creating the initial administrator account)

## Configuration options{#configs}

- Multilingual (√)

## Administration{#administrator}

## Troubleshooting{#troubleshooting}

#### Initialization fails to create account ?

You must use HTTPS to access the site; otherwise, account creation will fail.