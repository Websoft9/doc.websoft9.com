---
title: ONLYOFFICE Docs
slug: /onlyofficedocs
tags:
  - Office
  - Document editing and previewing
  - Online Office
---

import Meta from './\_include/onlyofficedocs.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. After completing the installation of ONLYOFFICE Docs via the **Websoft9 Console**, retrieve the application's **Overview** and **Access** information from **My Apps**.

2. Once accessed, the **ONLYOFFICE Docs Community Edition installed** page will appear.

3. Run the test command on the prompt page to verify usability.

### Integration with Web Disk System

- [OwnCloud Integration ONLYOFFICE Docs](./owncloud#onlyoffice)
- [Nextcloud Integration ONLYOFFICE Docs](./nextcloud#onlyoffice)
- [Seafile Integration ONLYOFFICE Docs](./seafile#docs)

### Add Fonts {#addfonts}

Refer to the official documentation [Adding fonts to ONLYOFFICE Docs](https://helpcenter.onlyoffice.com/installation/docs-community-install-fonts-linux.aspx), and note the following:

1. Clear your browser cache or open a new browser page in privacy mode to see the new fonts.
2. TTF fonts copied from Windows or downloaded from a font website may not work, resulting in no visible effect for the added fonts.

### Export PDF

After integrating into cloud disk software, open the document and save it as a PDF file through ONLYOFFICE Docs **File - Save as** or **Download as**.

### Configure HTTPS with Self-Signature

ONLYOFFICE Docs [self-signed certificate](https://helpcenter.onlyoffice.com/installation/docs-community-install-docker.aspx) is configured as follows:

1. Select **My Apps > Compose > Go to Edit Repository > .env** to map port 443 for the container to the host (e.g., 8089).

2. Enter the ONLYOFFICE Docs container, download and run the script to create the certificate:
   ```
   wget -N -P /var/www/onlyoffice/Data https://websoft9.github.io/docker-library/apps/onlyofficedocs/src/createCA.sh
   bash /var/www/onlyoffice/Data/createCA.sh
   ```
3. Modify the container configuration file:
   ```
   sed -i 's/“rejectUnauthorized”: true/“rejectUnauthorized”: false/g' /etc/onlyoffice/documentserver/default.json
   supervisorctl restart all
   ```
4. Exit the ONLYOFFICE Docs container and reboot to access it through `http://URL:8089`.

## Enterprise Edition

### Why Buy Through Websoft9?

Websoft9 is an ONLYOFFICE Docs [global partner](https://www.onlyoffice.com/search.aspx?search=websoft9) and one of the technical support centers in China. Purchasing through Websoft9 offers:

- At least a 10% discount on the paid version
- More comprehensive product support
- Integration with technologies like web disk, cloud storage, etc.

### Simultaneous Connections Rule {#onlyofficedocsmaxconn}

ONLYOFFICE Docs Simultaneous Connections: This refers to the number of connections open in **edit mode** by all users at the same time. Beyond this limit, the document will open in **preview mode**.

### Activate License

Place the license file in the ONLYOFFICE Docs volume **data** directory to take effect immediately.

## Configuration Options {#configs}

- [File History (multiple versions)](https://helpcenter.onlyoffice.com/onlyoffice-editors/onlyoffice-document-editor/HelpfulHints/VersionHistory.aspx)(✅): **File > Version History**

- Support for mainstream formats: docx, xlsx, pptx, odt, ods, odp, doc, xls, ppt, pdf, txt, rtf, html, epub, csv, etc.

- ONLYOFFICE product family includes:

  - ENTERPRISE EDITION
  - COMMUNITY EDITION
  - DEVELOPER EDITION

- Authorization Access Control (✅): Used for password authentication with third-party software, ensuring ONLYOFFICE Docs can be accessed when authorized, supporting protocols like JWT.

## Administration {#administrator}

- **Enable JWT Key**: Modify JWT_ENABLED=true in the ONLYOFFICE Docs application **compose** `.env` file.

## Troubleshooting {#troubleshooting}

#### CSV File Containing Chinese Characters Opens with Garbled Code?

ONLYOFFICE will prompt users to choose the character encoding and field separator when opening a CSV file. The following combination typically solves garbled code issues:

- **GB2313 + comma**

#### Open Debug Log?

1. Enter the container and modify the _/etc/onlyoffice/documentserver/log4js/production.json_ file, changing **level**: **WARN** to **level**: **DEBUG**.
2. Run the _supervisorctl restart all_ command to apply the changes.
