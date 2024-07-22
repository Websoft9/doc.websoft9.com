---
title: Strapi
slug: /strapi
tags:
  - Backend as a Service 
  - Headless CMS
  - strapi
---

import Meta from './_include/strapi.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Strapi at **Websoft9 console**, get the applicaiton's overview and access information from **My Apps**  

2. Wait for Strapi container starting: At the first time starting, Strapi will pull external software packages online and wait for a few minutes before entering the initial page

### Create your Data model

1. Login to Strapi, go to **Plugins > Content-type Builder** Add a dataset, if named: `websoft9`

2. Add a user under the **Users** and set the role to `public` 

3. Go to **Settings > USERS & PERMISSIONS PLUGIN > Roles**, and edit public role to grant access to the `websoft9` dataset 

4. Access the following URL to obtain data 
    ``` 
    #Get all data 
    http://URL/websoft9 
        
    #Get the first piece of data 
    http://URL/websoft9/1 
    ```

## Configuration options{#configs}

- Multilingual (√)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### Strapi first startup error?

**Reason**: When Strapi is first launched, it will install some **Node.js** packages from Github, which may fail due to network issues    
**Solution**: Ensure that the server can smoothly access the npm repository and Github
