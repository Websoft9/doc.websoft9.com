---
title: OwnCloud
slug: /owncloud
tags:
  - ownCloud
  - Web Disk
  - Knowledge Management
  - Team Collaboration
---

import Meta from './\_include/owncloud.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. Once you have completed the installation of OwnCloud via the **Websoft9 Console**, retrieve the application's **Overview** and **Access** information from **My Apps**.

2. Visit the URL of OwnCloud, log in to the backend, and begin using it.  
   ![](./assets/owncloud-backend-websoft9.png)

### Document Preview and Editing with ONLYOFFICE {#onlyoffice}

1. (Optional) Go to the **App Store** in the Websoft9 console and install ONLYOFFICE.

2. Install ONLYOFFICE via the OwnCloud Backend Market.

3. After installation, navigate to **Settings > Admin > Additional** to configure the ONLYOFFICE connection.  
   ![](./assets/owncloud-onlyoffice-websoft9.png)

### Connecting to External Storage {#oss}

- In the OwnCloud backend: You can set up external storage via **Settings > Admin > Storage**.
- Requires S3 support, which can be installed from the Market under **External Storage: S3**.

### Rebuilding Indexes

If you move or copy your OwnCloud data directory to a new location, run the following command to rebuild the index:

```bash
occ files:scan --all
```

## Configuration Options {#configs}

- [Marketplace](https://marketplace.owncloud.com/)

- SMTP (✅): Configured under **Settings > Admin > Email Server**.

- Support for third-party storage (✅).

- Multilingual (✅): Configure language settings via **Personal > General** in the OwnCloud backend.

- Mobile: Available through the OwnCloud Desktop Client, OwnCloud Android App, and OwnCloud iOS App.

- Document Editing and Preview: Integration with [ONLYOFFICE Docs](./onlyofficedocs) and other third-party middleware.

- Configuration File (mounted): `/mnt/data/config/config.php`.

- CLI: [ownCloudcmd](https://doc.owncloud.com/desktop/next/advanced_usage/command_line_client.html).

- [API Documentation](https://doc.owncloud.com/server/next/developer_manual/core/apis/provisioning-api.html).

## Administration {#administrator}

- **Modify URL**: Change the OWNCLOUD_DOMAIN and OWNCLOUD_TRUSTED_DOMAINS environment variables as needed. Modifying the `config.php` file alone will not work. More details can be found [here](https://doc.owncloud.com/server/10.13/admin_manual/configuration/server/config_sample_php_parameters.html#define-list-of-trusted-domains-that-users-can-log-into).

- **Online Backup**: Enable online backups using the **[OwnBackup](https://en.websoft9.com/xdocs/owncloud-image-guide/#using-apps)** application.

## Troubleshooting {#troubleshooting}

#### Untrusted Domain?

**Description**: You are receiving an initialization prompt indicating that you are accessing the server from an untrusted domain.  
**Solution**: Apply real URLs to the `OWNCLOUD_DOMAIN` and `OWNCLOUD_TRUSTED_DOMAINS` variables in the compose file `.env`.
