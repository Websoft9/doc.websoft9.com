---
title: Typo3
slug: /typo3
tags:
  - CMS
  - Content Management
  - Enterprise website
---

import Meta from './_include/typo3.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Typo3 at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

   - Get access information in the "Access" tab
   - Get **database account** in the "Database" tab 

2. Enter the Typo3 installation wizard, and when the environment check step is passed, start to fill in the database parameters

   - Username: `typo3`
   - Password: get it from the application administration
   - Host: get it from the application administration

     ![](./assets/typo3-installdb-websoft9.png)

3. Login to the backend and start creating your website

4. Login to the backend and start creating the site  
   ![](./assets/typo3-backend-websoft9.png)

5. After completing the installation, login to the backend

## Configuration options{#configs}

- CLI
  * typo3 -- official core command line
  * typo3cms -- third-party extension command

- Multilingual(✅): [Changing The Backend Language](https://docs.typo3.org/m/typo3/tutorial-getting-started/main/en-us/Setup/BackendLanguages.html#backendlanguages)

- Extensions(✅): Typo3 backend **ADMIN TOOLS > Extensions**
- Template(✅): Typo3 backend **WEB > Template**

## Administer{#administrator}

- Online upgrade(✅): Typo3 backend **ADMIN TOOLS > Upgrade**

## Troubleshooting{#troubleshooting}

