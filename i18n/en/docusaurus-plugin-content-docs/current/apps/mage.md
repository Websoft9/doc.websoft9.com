---
title: Mage
slug: /mage
tags:
  - Integrated Data
  - Mage
---

import Meta from './_include/mage.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completing the installation of Mage in the **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

### Run pipelines {#pipelines}

The following is how to run pipelines by migrating MySQL data tables:

1. Prepare two databases: the source database and the target database.

2. Click **New Pipelines > Data Integration**, enter a name and create the pipeline.

3. Choose **Select Source**, select "MySQL", fill in the original database information in **Configuration** (Click **Test Connection** to verify the database information).

4. **Select the table you want to migrate.

5. **Select destination** select "MySQL", fill in the destination database information in **Configuration** (Click **Test Connection** to verify the database information).

6. Click on the left menu **Triggers > Run@once > Run now**, the corresponding table will be imported into the target database after execution.

## Configuration options{#configs}

- Multilingual (×)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}
