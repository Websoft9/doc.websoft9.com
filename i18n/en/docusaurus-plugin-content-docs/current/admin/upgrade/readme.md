---
sidebar_position: 1
slug: /upgrade
---

import DocCardList from '@theme/DocCardList';
import {useCurrentSidebarCategory} from '@docusaurus/theme-common';

# Upgrade



## Upgrade Object

The upgrade objects that may be involved in using Websoft9 include:

<DocCardList items={useCurrentSidebarCategory().items}/>

## FAQ

#### Update vs Upgrade?

- **Update**: Involves minor changes such as bug fixes, performance improvements, or small feature additions. It occurs frequently and has minimal impact.  

   e.g. MySQL5.6.25 > MySQL5.6.30, PHP5.6.33 > PHP5.6.37

- **Upgrade**: Involves major changes such as new features, interface improvements, or performance enhancements. It occurs less frequently and has a significant impact.   
 
   e.g. MySQL5.6 > MySQL5.7, PHP5.6 > PHP7.0

#### Need to redeploy the source code to upgrade my application?

No, all application is running at containers by Websoft9, just need to upgrade container 
