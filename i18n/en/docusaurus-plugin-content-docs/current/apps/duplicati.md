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

1. When completed installation of Duplicati at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. **Account** can be set for initial access

### Backup guide

Refer to: [Websoft9 Backup](./backup/websoft9)

## Configuration options{#configs}

- Multi-language (✅)
- Backup path settings: SOURCE_PATH and BACKUP_PATH in the *.env* file

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### Installing multiple Duplicati exceptions?

Description: Installing multiple Duplicati exceptions  
Reason: Duplicati is bind to the host's **Fixed Path** by default, so when installing a second Duplicati, it will use the same path, and therefore attempts permissions issues.     
Solution: It is not recommended to install more than one Duplicati.