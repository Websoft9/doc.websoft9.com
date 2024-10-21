---
title: Mage
slug: /mage
tags:
  - Integrated Data
  - Mage
---

import Meta from './\_include/mage.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. After completing the installation of Mage via the **Websoft9 Console**, retrieve the application's **Overview** and **Access** information from **My Apps**.

### Run Pipelines {#pipelines}

The following steps explain how to run pipelines by migrating MySQL data tables:

1. Prepare two databases: the source database and the target database.

2. Click **New Pipelines > Data Integration**, enter a name, and create the pipeline.

3. Choose **Select Source**, select "MySQL", and fill in the source database information in **Configuration** (Click **Test Connection** to verify the database information).

4. **Select the table** you want to migrate.

5. **Select Destination**, choose "MySQL", and fill in the destination database information in **Configuration** (Click **Test Connection** to verify the database information).

6. In the left menu, click **Triggers > Run@once > Run now**, and the corresponding table will be imported into the target database after execution.

## Configuration Options {#configs}

- Multilingual (×)

## Administration {#administrator}

## Troubleshooting {#troubleshooting}
