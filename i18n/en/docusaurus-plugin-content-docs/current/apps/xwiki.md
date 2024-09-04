---
title: XWiki
slug: /xwiki
tags:
  - Knowledge Management
  - wiki
  - Documentation
---

import Meta from './\_include/xwiki.md';

<Meta name="meta" />

## Getting Started {#guide}

1. After completing the installation of XWiki via the **Websoft9 Console**, retrieve the application’s **Overview** and **Access** information from **My Apps**.

2. Enter the setup wizard and allow XWiki to initialize. Be patient, as this process may take some time.

3. Set up an admin account and install the pre-made templates (this is a mandatory step for enabling full functionality).
   ![](./assets/xwiki-install-websoft9.png)

4. Wait for all installations to complete and verify that XWiki is properly initialized.

## Configuration Options {#configs}

- **Pre-installed Templates (✅)**: Required during the setup process to enable XWiki's core features and functionality.
- **Domain Configuration**: Ensure that external network ports are open and the domain is properly configured for external access.

## Administration {#administrator}

1. **User Management**:

   - Add, remove, and manage users from the XWiki admin panel.
   - Assign roles and permissions to different users based on their responsibilities.

2. **Backup and Restore**:

   - Use the Websoft9 Console to schedule regular backups of your XWiki instance to ensure data safety.
   - Restore backups through the console if necessary.

3. **Extension Manager**:
   - Install and manage extensions through XWiki’s Extension Manager to expand functionality.
   - Keep extensions updated for security and performance improvements.

## Troubleshooting {#troubleshooting}

1. **XWiki Initialization Issues**:

   - **Symptom**: XWiki setup wizard fails or hangs during initialization.
   - **Solution**: Ensure that sufficient server resources are available. Restart the XWiki container via the Websoft9 Console and retry the initialization.

2. **Admin Account Setup Issues**:

   - **Symptom**: Issues encountered during the admin account setup.
   - **Solution**: Double-check the database connection and ensure that all required services are running.

3. **Performance Issues**:
   - **Symptom**: XWiki is running slowly after installation.
   - **Solution**: Review the installed extensions and remove any that are not necessary. Additionally, check the server resources and optimize them if needed.
