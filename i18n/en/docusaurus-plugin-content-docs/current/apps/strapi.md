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

1. When completed installation of Strapi at Websoft9 console, get the applicaiton's overview and access information from "My Apps"  

2. When the Strapi container starts for the first time, it will pull external software packages online and wait for a few minutes before entering the initial page

### Built data model by self

1. "Plugins" > "Content-type Builder" Add a dataset, if named: websoft9 

2. Add a user under the "Users" and set the role to public 

3. "Settings" > "USERS & PERMISSIONS PLUGIN" > "Roles" Edit public role to grant access to the websoft9 dataset 

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

Problem analysis: When Strapi is first launched, it will install **Node** and download software packages from Github, which may fail due to network issues  
Solution: Ensure that the server can smoothly access the npm repository and Github
