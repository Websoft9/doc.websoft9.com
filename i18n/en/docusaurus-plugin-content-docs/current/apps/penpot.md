---
title: Penpot
slug: /penpot
tags:
  - Prototyping
  - Design Collaboration
  - User Interface
  - Canvas
---

import Meta from './_include/penpot.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

When completed installation of Penpot at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  


## Configuration options{#configs}

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### The cover image of a project cannot be displayed?

Description: When accessing Penpot using **IP:Port**, the cover image of the created project cannot be displayed    
Reason: The application environment variable PENPOT_PUBLIC_URI does not contain a port    

#### Can't complete first time user registration?

Ensure the backend container environment variable **PENPOT_FLAGS** contains: disable-secure-session-cookies

