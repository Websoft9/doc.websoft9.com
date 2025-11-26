---
title: Checkmate
slug: /checkmate
tags:
  - Website Monitoring
  - Real-time Alerts
  - Checkmate
---

import Meta from './_include/checkmate.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Checkmate at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Complete the install wizard step by step

## Configuration options{#configs}

- Multilingual (√)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### MongoDB Container Keeps Restarting, Application Unavailable?

Description: MongoDB fails to start normally. Logs indicate lack of AVX instruction set support.
Reason: MongoDB 4.2 and later require CPU support for the AVX instruction set to start.
Solution: Deploy using a CPU that supports the AVX instruction set. 