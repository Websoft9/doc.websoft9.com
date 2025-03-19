---
title: TeamCity
slug: /teamcity
tags:
  - DevOps
  - CI
  - Pipeline
---

import Meta from './\_include/teamcity.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. After completing the installation of TeamCity in the **Websoft9 Console**, retrieve the application's **Overview** and **Access** information from **My Apps**.

   - Access the URL in the **Access** section.
   - Retrieve the database information from the **Database** section.

2. Access the URL to reach the initialization page and select **proceed** to start the next steps.

3. Fill in the database information in the **Database Connection Setup**:

   - Database Type: MySQL (Select and click the link to download the JDBC driver)
   - Database Host: Retrieve this from the TeamCity application management page.
   - Database Name: `teamcity`
   - Username: `teamcity` or `root`
   - Password: Retrieve this from the TeamCity application management page.

4. After completing the account creation steps, log in to the TeamCity backend.
   ![](./assets/teamcity-main-websoft9.png)

5. Edit the Server URL: Go to **TeamCity Console > Administration > Global Settings**.

### Connect the TeamCity Agent

The TeamCity Agent is launched by default within TeamCity.

Go to **TeamCity Console > Agents > UNAUTHORIZED AGENTS > Authorize** to connect to the TeamCity Agent.

## Configuration Options {#configs}

- Configure Server URL: Go to **TeamCity Console > Administration > Global Settings**.

## Administration {#administrator}

## Troubleshooting {#troubleshooting}

#### Agent Cannot Connect to TeamCity?

Ensure that the TeamCity Agent hostname does not contain an underscore ("\_") when connecting to TeamCity.
