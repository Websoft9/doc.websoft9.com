---
sidebar_position: 2
slug: /upgrade-app
---

# Upgrade application

Websoft9 suggest application upgrades to ensure a better experience while minimizing security risks.  

## Prepare

1. Before upgrading, please make sure that you have completed the server image (snapshot) backup.
2. When upgrading, stop the server and do not affect the business use.

## Upgrade application

There are two ways to upgrade your application: 

### Upgrade tool comes with the application

Some applications come with their own online upgrade methonds:

- Upgrade interface
- Upgrade plugin
- Upgrade CLI

You can refer to upgrade content at [Apps docs](./apps) of Websoft9.  


### Upgrade by Application Compose

Modify the image version at [Application Compose](./app-compose) and redeploy application for upgrade

1. Login to Websoft9 Console and go to **My Apps**

2. Modify the version-related parameters in the `.env` and `docker-compose.yml` files, e.g: **W9_VERSION**

3. Redeploy application at Websoft9 Console, then upgrade completed