---
title: Aria2
slug: /aria2
tags:
  - Offline Download
  - Web Download
  - Bittorrent
---

import Meta from './_include/aria2.md';

<Meta name="meta" />

## Getting started{#guide}

### Connect to the Aria2 RPC Service{#wizard}

After installing Aria2 on the Websoft9 console, view the application details through **My Apps** and get the RPC service connection information in the **Access** section.

1. Access the AriaNg page from your local computer's browser

2. Select **AriaNg Settings**, configure the RPC connection information

   - Address: http:Aria2 access address
   - Port: RPC port

    ![Aria2 Configuration](./assets/aria2-rpc-websoft9.png)

3. Reload the AriaNg page and the status should change to **Connected**.

## Configuration options{#configs}

- Multilingual (√)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### Aria2 connection failed?
 
Make sure the RPC Secret for Aria2 is correct. For example, a password that contains **@** will fail to connect. 