---
sidebar_position: 2
slug: /superset/solution
tags:
  - Superset
  - Data Analysis
  - BI
---

# Superset Solution

You can use Superset integrated other software for [Data Analysis](https://superset.apache.org/).

## Integrate Superset Charts into other web apps        

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-charts-integrate-websoft9.png)

1. Modify the Superset configuration file (/data/apps/superset/src/docker/pythonpath_dev/superset_config.py)，and restart the Superset container
- Add a global configuration item to the configuration file: PUBLIC_ROLE_LIKE = "Gamma"  
- Run the command to restart the container: docker restart superset-app

2. Edit role Public permissions: Click the blank space at the end of the permission list box to add the 'All Database Access on all_database_access' permission    

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-editrole-websoft9.png)

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-add-role-permissions-websoft9.png)

3. Get the URL of the Charts and embed it on the web app page  

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-copyurl-websoft9.png)

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-chart-in-page-websoft9.png)  

For more information, please refer to [the official documentation](https://github.com/apache/superset/blob/1.5.2/docs/docs/security.mdx)
