---
sidebar_position: 1
slug: /migration
---

import DocCardList from '@theme/DocCardList';
import {useCurrentSidebarCategory} from '@docusaurus/theme-common';

# Migration

Application migration refers to the process of moving software applications from one computing environment to another.  

## Prepare

The basic goal of migration is to guarantee consistency before and after migration. Therefore, the following elements must be removed for the migration:

- **Migration target**: source code, running data, configuration files and database files
- **Migration location**: on-premises or cloud providers

## Use case

<DocCardList items={useCurrentSidebarCategory().items}/>

