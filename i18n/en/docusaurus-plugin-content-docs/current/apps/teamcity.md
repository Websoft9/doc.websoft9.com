---
title: TeamCity
slug: /teamcity
tags:
  - DevOps
  - CI
  - Pipeline
---

import Meta from './_include/teamcity.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of TeamCity at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  
   - Get the access URL in the **Access**.
   - Get the database information in the **Database**.  

2. Access the URL to the initialization page and select **proceed** to start the next steps.

3. Fill in the database the application in **Database connection setup**:

   - Database type: MySQL (Select and click the link to download the JDBC driver)   
   - Database host: Get from the TeamCity application management page.
   - Database Name: `teamcity`
   - User name: `teamcity` or `root`
   - Password: Get from the TeamCity application management page.

5. After completing the account creation steps, login to the TeamCity backend.
   ![](./assets/teamcity-main-websoft9.png)

6. Edit the Server URL：Select **TeamCity console > Administration > Global Settings**.

### Connect the TeamCity Agent

The TeamCity Agent is launched by default in the TeamCity.  

Select **TeamCity console > Agents > UNAUTHORIZED AGENTS > Authorize**, to connect to TeamCity Agent.

## Configuration options{#configs}

- Configure Server URL：Select **TeamCity console > Administration > Global Settings**

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### Agent cannot connect to TeamCity?

Ensure TeamCity Agent hostname has no "_" when connecting to TeamCity.