---
title: Nextcloud
slug: /nextcloud
tags:
  - Netdisk
  - Knowledge Management
  - Teamwork
---

import Meta from './\_include/nextcloud.md';

<Meta name="meta" />

## Getting Started {#guide}

### Login Verification {#verification}

1. After completing the installation of Nextcloud via the **Websoft9 Console**, retrieve the application's **Overview** and **Access** information from **My Apps**.

2. Access the Nextcloud URL and log in to the backend to get started.
   ![](./assets/nextcloud-backend-websoft9.png)

### Enable Online meetings{#talk}

1. Set HTTPS for your Nextcloud on your **Websoft9 Gateway**

2. Login to Nextcloud Console, and enable **Nextcloud Talk** at **App Store**

3. Create a talk and send links for users

### Document Preview and Edit {#onlyoffice}

#### Integration of Nextcloud Office

Nextcloud has built-in Nextcloud Office (based on Collabora Online Development Edition, or CODE). Install the CODE plugin to enable it.

#### Integration with ONLYOFFICE Docs

1. (Optional) In the Websoft9 console **App Store**, install ONLYOFFICE.

2. In the Nextcloud console, click the top-right gear icon, select **+Apps > Office & Text**, and install ONLYOFFICE.

3. In the Nextcloud console, click the top-right gear icon, select **Administration Settings**, and find ONLYOFFICE settings. Follow the [Integration Guide](https://api.onlyoffice.com/editors/nextcloud) for ONLYOFFICE.
   ![](./assets/nextcloud-setonlyoffice-websoft9.png)

4. After the installation is complete, locate the **SETUP** page and configure ONLYOFFICE as shown ([refer to the official documentation](https://api.onlyoffice.com/editors/nextcloud)).

### Install the Application Offline {#offline}

1. From the Nextcloud [App Market](https://apps.nextcloud.com/), find the app package URL and download it to the server.

2. Extract it to the Nextcloud container's _/var/www/html/apps_ directory.

3. Enter the container CLI and change the permissions of the apps directory:

   ```
   chown -R www-data:www-data /var/www/html/apps/appname
   ```

4. Log in to the Nextcloud backend, enter the application center, and enable the extension.

### WebDAV Service

WebDAV is used to establish a connection between a local computer and Nextcloud:

1. In the Nextcloud console, go to **File > File Settings** to get the WebDAV URL.
2. On a local Windows PC, configure the [WebDAV client](https://www.thewindowsclub.com/how-to-map-webdav-in-windows).

### Connecting to External Storage {#oss}

Nextcloud supports many popular enterprise storage services. The steps to use them are as follows:

1. Log in to the Nextcloud backend, select **Apps > Your Apps**, and enable **External storage support**.

2. In **Administration Settings** of the Nextcloud backend, set up external storage with S3 compatibility protocol settings:

   - Bucket: Corresponds to the storage bucket of some vendors.
   - Hostname: Corresponds to the Endpoint of some vendors.
   - Access Key: Generally required.

   ![](./assets/nextcloud-s3-websoft9.png)

### Rebuild Indexes

After moving or copying the Nextcloud data directory to another location, run `occ files:scan --all` to rebuild the index.

### Secure Use of HTTPS

1. In the Websoft9 console, select **Gateway**, edit the proxy for the Nextcloud application, clear **Custom Nginx Configuration** in **Advanced**, and save it.

2. Select **My Apps > Compose > Go to Edit Repository > .env** and uncomment the line **OVERWRITEPROTOCOL** to rebuild the application.

## Configuration Options {#configs}

- [App Market](https://apps.nextcloud.com/) (✅)

- Configuration file (mounted): `/var/www/html/config/config.php`

- Multilingual (✅): Configured through **Personal Settings**.

- SMTP (✅): Configured via **Administration Settings > Basic Settings > Email Servers**

- [LDAP](https://docs.nextcloud.com/server/latest/admin_manual/configuration_user/user_auth_ldap.html)

- [Mainstream External Storage Service](https://docs.nextcloud.com/server/latest/admin_manual/configuration_files/external_storage_configuration_gui.html): Amazon S3, Dropbox, FTP, Google Drive, SMB, WebDAV, SFTP, etc.

- Mobile (✅): Nextcloud Desktop Client, Nextcloud Android App, Nextcloud iOS App.

- CLI: `occ` for installing and upgrading Nextcloud, managing users, managing passwords, and more.

- [Basic APIs](https://docs.nextcloud.com/server/latest/developer_manual/client_apis/WebDAV/basic.html)

## Administration {#administrator}

- **Modify URL**: The configuration file parameter `overwrite.cli.url` defaults to wildcard, which can automatically apply to any URL change.

- **Online Backup**: Install **[OwnBackup](https://apps.nextcloud.com/apps/ownbackup)** to achieve online backup.

## Troubleshooting {#troubleshooting}

#### Not find Talk and Assistant of Nextcloud?

You should enable these modules after your first starting Nextcloud. 

#### Disable ONLYOFFICE Certificate Validation?

If Nextcloud is using HTTPS, ONLYOFFICE must also use HTTPS, or the connection will fail.

You can disable certificate verification by configuring the Nextcloud backend plugin or adding the following to the configuration file:

```
'onlyoffice' =>
array (
'verify_peer_off' => TRUE,
),
```

#### Can't Install Apps Due to Network Timeout?

Refer to the [Install Apps Offline](#offline) scenario.
