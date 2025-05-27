---
title: CoreDNS
slug: /coredns
tags:
  - console
  - other
---

import Meta from './_include/coredns.md';

<Meta name="meta" />

## Getting started{#guide}

### Config your DNS{#wizard}

1. When completed installation of CoreDNS at **Websoft9 Console**, start to edit settings files from **Compose** tab of **My Apps**  

2. Complete the install wizard step by step

3. Make sure value of **W9_INNERIP_SET** is Intranet IP of your host machine runing for CoreDNS

4. There have two default config files:

   - Corefile: main config file that include hosts map and includes other files
   - db.demo.inner：[Zone file](https://coredns.io/plugins/file/) template show a wildcard sample

## Configuration options{#configs}

## Administer{#administrator}

## Troubleshooting{#troubleshooting}