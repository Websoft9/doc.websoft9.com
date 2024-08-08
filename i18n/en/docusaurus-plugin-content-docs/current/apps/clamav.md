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

2. Run the following scan command(note that `sudo` is not required) 
    ``` 
    apk add sudo 
    sudo clamscan -ri /scandir --log=myscan.log 
    ``` 

    > `myscan.log` contains the scan results. If it includes information about infected files, it indicates that the system has a virus

## Configuration options{#configs}

- Set Scan Path: Define the scan path using the **W9-SCAN-PATH_SET** variable in the `.env` file.
- Scanning Commands: Use `clamscan` for a deep scan or `clamdscan` as an alternative scanning method.

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### ClamScan Lacks Permission to Scan Files? 

If ClamScan does not have the necessary permissions to scan files, try using sudo to grant the required access. Run the scan with elevated privileges using `sudo clamscan` 
