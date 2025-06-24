---
title: RustDesk 
slug: /rustdesk
tags:
  - Remote Support
  - Remote Desktop
  - RustDesk
---

import Meta from './_include/rustdesk.md';

<Meta name="meta" />

## Getting Started {#guide}

### Remoting

Take two Windows as an example, the following describes the process of connecting remotely: 1.

1. Download the RustDesk [client](https://github.com/rustdesk/rustdesk/releases/download/1.4.0/rustdesk-1.4.0-x86_64.exe) for each of the two connected windows and install it.

2. Open the Client Connection Tool, **Settings > Network > ID/Relay Server** Settings
   - ID Server: IP or domain name where RustDesk is deployed
   - Key: the contents of **id_ed25519.pub** under RustDesk volumes

3. Give the ID and one-time password to the control client to start the remote connection.

## Configuration options{#configs}

## Administer{#administrator}

## Troubleshooting{#troubleshooting}