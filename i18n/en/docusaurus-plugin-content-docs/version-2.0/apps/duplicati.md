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

### Initial setup{#wizard}

1. After completing the installation of Duplicati in the **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

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
