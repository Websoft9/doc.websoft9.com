---
title: ClamAV
slug: /clamav
tags:
  - Antivirus
  - Security protection
  - clamav
---

import Meta from './_include/clamav.md';

<Meta name="meta" />

## Getting started{#guide}

### Start scan  

1. Access the container through the Exec console  

2. Run the following scan command(sudo is not necessary) 
    ``` 
    apk add sudo 
    sudo clamscan -ri /scandir --log=myscan.log 
    ``` 

    > Myscan.log is the scan result. If it contains Infected files information, it indicates that the system has a virus

## Configuration options{#configs}

- Set scan path: **W9-SCAN-PATH_SET**  in the .env file
- Scanning commands: clamscan(deep scan) and clamdscan

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### clamscan doesn't have the permission to scan files? 

After installing sudo, use `sudo clamscan` to scan