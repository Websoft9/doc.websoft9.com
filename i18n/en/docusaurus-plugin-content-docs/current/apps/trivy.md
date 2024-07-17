---
title: Trivy
slug: /trivy
tags:
  - Antivirus
  - Security protection
  - trivy
---

import Meta from './_include/trivy.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Trivy at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Access Trivy container, start virus protection scanning
  ```
  trivy fs /scandir
  ```

## Configuration options{#configs}

- CLI (√): `trivy`

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### How to scan quickly?

Access to Trivy container, run command as follow:
  ```
  apk add --no-cache python3 && ln -sf python3 /usr/bin/python 
  trivy fs  --scanners vuln /tmp/usr/share 
  ```