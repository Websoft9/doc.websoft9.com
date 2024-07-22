---
sidebar_position: 1
slug: /automation
---

import DocCardList from '@theme/DocCardList';
import {useCurrentSidebarCategory} from '@docusaurus/theme-common';

# Workflow automation 

This chapter explores the concept of automated tasks that go beyond traditional server scheduling tasks such as Crontab.  

Here, automated tasks are defined as periodic, rule-based activities that are executed through scripts or specialized tools.  

Automation not only increases work efficiency and reduces error rates, it also frees up human resources. This allows them to focus on more creative and complex tasks.  

Websoft9 suggest you use [n8n](./n8n) for automation, n8n is a user-friendly UI workflow automation with many use cases:  

1. **Server Maintenance Tasks**: Automated data backup, log cleanup, time synchronization, and security scans.  
2. **DevOps Workflows**: Automated processes like code review, source code compilation, and automated testing.  
3. **Application Integration**: Automating data and process integration between different application systems.  

## Launch n8n

1. Login to Websoft9 Console, and install [n8n](./n8n) by App Store

2. Login to n8n console to start automation workflow

## Use cases

Use cases for using [n8n](./n8n):

<DocCardList items={useCurrentSidebarCategory().items}/>

## FAQ

#### Can I use n8n replace Linux Crontab?

Yes, n8n can have more ability
