---
title: Duplicati
slug: /duplicati
tags:
  - Incremental Backup
  - Backup Recovery Software
  - duplicati
---

import Meta from './_include/duplicati.md';

<Meta name="meta" />

## Getting started{#guide}

### Login verification{#verification}

1. Completed installation Duplicati at Websoft9 console, get the applicaiton's overview and access credentials from **My Apps**  

2. Starting to verify it

### Backup guide

Refer to: [Websoft9 Backup](./backup-websoft9)

## Configuration options{#configs}

- Multi-language (✅)
- Backup path settings: SOURCE_PATH and BACKUP_PATH in the *.env* file

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### Installing Multiple Instances of Duplicati 

Description: Installing multiple instances of Duplicati
Reason: Duplicati is bound to the host's **Fixed Path** by default. When installing a second instance of Duplicati, it uses the same path, leading to  permissions issues.     
Solution: It is not recommended to install more than one Duplicati.
