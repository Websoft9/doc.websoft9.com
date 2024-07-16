---
title: Syncthing
slug: /syncthing
tags:
  - Real-time synchronization of folders
  - Visualization
  - GUI
---

import Meta from './_include/syncthing.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Syncthing at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. After logining, you will be prompted to set up your account. (It is suggested that you do this setup.)
   
   - General > API Key (recommended)
   - GUI > GUI Username and GUI Password (highly recommended)

### Server synchronization

Syncthing is mainly used to synchronize files or folders between multiple servers. The following describes the specific operation (assuming Server A, Server B):

1. Make sure Syncthing is installed on both servers.

2. Login to Syncthing on Server A, add a remote device, then the device ID of Server B will be found automatically, check it.

3. Login to Syncthing on Server B, then accept the connection request from Server A. Click **+Add Remote Device** and follow the guide to complete the connection.

4. Click **+Add Folder** in the Syncthing console of both servers.

   - General > Folder ID (A and B use the same ID)
   - General > Folder Path
   - Shared (check)

5. All settings are complete, and synchronization will now occur automatically.

## Configuration options{#configs}

- Multilingual(✅)

## Administer{#administrator}

## Trouble
