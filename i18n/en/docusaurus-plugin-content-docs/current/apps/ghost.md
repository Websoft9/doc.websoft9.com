---
title: Ghost
slug: /ghost
tags:
  - CMS
  - Building a website
  - Blog
  - Content subscription
---

import Meta from './_include/ghost.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Ghost at Websoft9 console, get the applicaiton's overview and access information from "My Apps"  

2. Access by `http://URL/ghost`, complete the install wizard  

   ![](./assets/ghost-register001-websoft9.png)

## Configuration options{#configs}

- Code embedding(✅): Ghost backend[SETTING]>[Code Injection]  

- SMTP(✅): Modify configuration file  

- [Ghost Theme Multilingual](https://ghost.org/docs/faq/translation/) (✅)

- Configuration file(ounted): */var/lib/host/config.production.json*  

- Theme directory(mounted): */var/lib/ghost/themes*  

- [Ghost CLI](https://ghost.org/docs/ghost-cli/)  

- [Content API](https://ghost.org/docs/content-api/)
  
- Subscription for reader (✅): "SETTING" > "Labs" and Enable members, Connect to Stripe, Subscription pricing

- Theme market(✅)  

- Change theme: "SETTING" > "Design" 

- Custom menu(✅)："SETTING" > Design"

## Administer{#administrator}

- **Change URL**: After changing the domain, it is necessary to reset the URL related values in the Ghost **configuration file** 
   ```
   {
   "url": "http://ghost.yourdomain.com",
   "server": {
      "port": 2368,
      "host": "0.0.0.0"
   }
   ```

- **Configure SMTP**: Modify [mail settings](https://forum.ghost.org/t/how-to-setup-basic-smtp-for-ghost/29166/4) in the configuration file

## Troubleshooting{#troubleshooting}
