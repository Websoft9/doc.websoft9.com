---
title: Alfresco
slug: /alfresco
tags:
  - ECM
  - Document management
  - Content management
---

import Meta from './_include/alfresco.md';

<Meta name="meta" />


## Getting started{#guide}

### Login Verification{#verification}

1. Complete the installation of Alfresco on the  **Websoft9 Console**. Obtain the applicaiton's overview and access credentials from **My Apps**.  

2. Wait 10 minutes for Alfresco to initialize.

3. Use a local browser to access the URL. Once the homepage loads, select **Alfresco Repository** > **Alfresco Share** to access the login page.

4. Log in to the Alfresco console and start using it
   ![](./assets/alfresco-consolegui-websoft9.png)


### Features

The common functions and screenshots are as follows:

- Backend dashboard
  ![Alfresco Backend dashboard](./assets/alfresco-adminui-websoft9.png)

- My Documents
  ![Alfresco My Documents](./assets/alfresco-mydocs-websoft9.png)

- Shared Documents
  ![Alfresco Shared Documents](./assets/alfresco-sharedocs-websoft9.png)

- Add users
  ![Alfresco Add  users](./assets/alfresco-addusers-websoft9.png)

- Add Group
  ![Alfresco Add Group](./assets/alfresco-addgroup-websoft9.png)

- Workflow (Approval)
  ![Alfresco Workflow(Approval)](./assets/alfresco-workflow-websoft9.png)

### Document Editors

Refer to: [Files and folders](https://docs.alfresco.com/content-services/community/using/content/files-folders/)

## Configuration Options{#configs}

- Multilingual(✅): Alfresco will automatically adapt the language based on the client's browser settings and can also be configured to adjust the language in the background.
- SMTP(✅)  
- [Alfresco Community Edition vs Alfresco Content Services Enterprise](https://www.alfresco.com/alfresco-content-services-enterprise-vs-alfresco-community-edition)
- [Alfresco support file format](https://www.alfresco.com.cn/alfresco-formats)
- Data storage directory: dir.root
- Metadata: Alfreco will automatically [create a metadata file](https://docs.alfresco.com/content-services/latest/develop/repo-ext-points/metadata-extractors/) with the suffix **metadata.properties.xml** for the uploaded file  
- Official Documentation: [Alfresco Documentation](https://docs.alfresco.com/content-services/community/using/content/) 
- Official Video: [Alfresco Videos](https://docs.alfresco.com/content-services/latest/tutorial/video/)
- [ReST API Guide](https://docs.alfresco.com/content-services/latest/develop/rest-api-guide/)
- Change password: In the Alfresco backend, go to the top right corner: **Administrator** > **My Profile**

## Administration{#administrator}

- Reset password: Connect to the database, and run the SQL command `UPDATE alf_node_properties SET string_value='209c6174da490caeb422f3fa5a7ae634' WHERE node_id=4 and qname_id=10`, The password will be reset to **admin**
- [Backup and restore](https://docs.alfresco.com/content-services/community/admin/backup-restore/)

## Troubleshooting{#troubleshooting}

#### Chinese Markdown format preview garbled?

Description: **View in browser** is not garbled, but the content is garbled in Alfreco's built-in document details  
Reason: Unknown  
Solution: Currently unavailable  
