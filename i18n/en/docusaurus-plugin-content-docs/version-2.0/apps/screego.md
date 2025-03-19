---
title: screego
slug: /screego
tags:
  - P2P
  - Screen Sharing
  - Peer-to-Peer
  - WebRTC
---

import Meta from './\_include/screego.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. After completing the installation of screego in the **Websoft9 Console**, retrieve the application's **Overview** and **Access** information from **My Apps**.

2. Log in to the Websoft9 console and set up HTTPS access for the screego application.

   > The domain name must be configured during installation for screego to work.

3. Optionally, use an external TURN server to start the port as appropriate.

### Use it Now

1. Go to the main screen of screego and click on **CREATE OR JOIN A ROOM** to create a room.

2. Send the URL of the new room to the other clients that need to share the screen.

3. Other clients open the URL and start using it.

## Configuration Options {#configs}

- Used by more than two people (✅)
- STUN/TURN relay server (built-in): The client (browser) first tries **direct connection**. If a direct connection is not possible, the STUN server is used for **penetration**, and if penetration is not possible, the TURN server is used for **relay**.

## Administration {#administrator}

## Troubleshooting {#troubleshooting}
