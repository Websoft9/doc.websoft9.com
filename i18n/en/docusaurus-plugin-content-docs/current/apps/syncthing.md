---
title: Syncthing
slug: /syncthing
tags:
  - Real-time synchronization of folders
  - Visualization
  - GUI
---

import Meta from './\_include/syncthing.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. After completing the installation of Syncthing in the **Websoft9 Console**, retrieve the application's **Overview** and **Access** information from **My Apps**.

2. After logging in, you will be prompted to set up your account (recommended).

   - **General > API Key** (recommended)
   - **GUI > GUI Username and GUI Password** (highly recommended)

### Server Synchronization

Syncthing is primarily used to synchronize files or folders between multiple servers. The following describes the operation (assuming Server A and Server B):

1. Ensure Syncthing is installed on both servers.

2. Log in to Syncthing on Server A, add a remote device, and the device ID of Server B will be found automatically. Check it.

3. Log in to Syncthing on Server B, accept the connection request from Server A. Click **+Add Remote Device** and follow the guide to complete the connection.

4. Click **+Add Folder** in the Syncthing console of both servers.

   - **General > Folder ID** (A and B should use the same ID)
   - **General > Folder Path**
   - **Shared (check)**

5. All settings are complete, and synchronization will now occur automatically.

## Configuration Options {#configs}

- Multilingual (✅)

## Administration {#administrator}

## Troubleshooting {#troubleshooting}
