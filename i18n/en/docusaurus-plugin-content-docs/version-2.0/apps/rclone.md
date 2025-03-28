---
title: Rclone
slug: /rclone
tags:
  - Cloud Storage
  - File Synchronization
  - Rclone
---

import Meta from './_include/rclone.md';

<Meta name="meta" />

## Getting started{#guide}

### Login verification{#verification}

1. Completed installation Rclone at Websoft9 console, get the applicaiton's overview and access credentials from **My Apps**  

2. Starting to verify it

### Perform synchronization

You can configure the source and target in the visual interface, but you can't perform synchronization, you need to go into the container and execute the following command:.

   ``
   rclone sync <Source's Config_Name>:<bucket_name> <Destination's Config_Name>:<bucket_name>

## Configuration options{#configs}

## Administer{#administrator}

## Troubleshooting{#troubleshooting}