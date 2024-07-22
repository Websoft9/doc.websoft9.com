---
title: APEX
slug: /apex
tags:
  - Low-code
  - Oracle database
  - Table
---

import Meta from './_include/apex.md';

<Meta name="meta" />

## Getting started{#guide}

### Login Verification{#verification}

1. Completed installation APEX at **Websoft9 Console**, get the applicaiton's overview and access credentials from **My Apps**     

2. Wait 10 minutes until APEX initialization is complete to access the login page.
   ![](./assets/apex-init-websoft9.png)

3. After successfully logging in, you will be prompted to change your password and enter the APEX console.
   ![](./assets/apex-index-websoft9.png)    

### Create a WorkSpace{#workspace}

Although APEX has a workspace named internal by default, it is only used for administrative purposes.   

You must create a new workspace if want to use APEX: 

1. Login to the backend and click Create New WorkSpace
   ![](./assets/apex-createwp-websoft9.png)

2. Follow the wizard: create a new schema and set the username, password and emailof the new workspace until you have finished creating the WorkSpace.
   ![](./assets/apex-createdone-websoft9.png)

### Create an application

After creating the workspace, you need to **login with the new workspace** and then [create application](https://docs.oracle.com/en/database/oracle/apex/23.2/htmdb/choosing-an-application-creation-method.html). 

## Configuration options{#configs}

- Multilingual (√): Login to the console to change the language (Chinese included)
- [API](https://apex.oracle.com/api)
- Application Backup: You can easily import and export applications to **APP Builder** from APEX console to realize backup.

## Administer{#administrator}

## Troubleshooting{#troubleshooting}
