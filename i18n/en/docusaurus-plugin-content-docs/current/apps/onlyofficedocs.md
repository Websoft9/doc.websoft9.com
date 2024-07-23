---
title: ONLYOFFICE Docs
slug: /onlyofficedocs
tags:
  - Office
  - Document editing and previewing
  - Online Office
---

import Meta from './_include/onlyofficedocs.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of ONLYOFFICE Docs at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. When accessing normally, the **ONLYOFFICE Docs Community Edition installed** page will appear

3. Run the test command on the prompt page to test the usability

### Integration with Web Disk System

* [OwnCloud Integration ONLYOFFICE Docs](./owncloud#onlyoffice)
* [Nextcloud Integration ONLYOFFICE Docs](./nextcloud#onlyoffice)
* [Seafile Integration ONLYOFFICE Docs](./seafile#onlyoffice)

### Add fonts {#addfonts}

Refer to the official documentation [Adding fonts to ONLYOFFICE Docs](https://helpcenter.onlyoffice.com/installation/docs-community-install-fonts-linux.aspx) and note the following few points:

1. You need to clear your browser cache or open a new browser page in privacy mode to see the new fonts
2. ttf fonts copied from Windows system or downloaded from font website may not work, so the added fonts have no effect

### Export PDF

After integrating into the cloud disk software, open the document and save it as a PDF file through ONLYOFFICE Docs **File - Save as** or **Download as**

### Configure HTTPS with self-signature

ONLYOFFICE Docs [self-signed certificate](https://helpcenter.onlyoffice.com/installation/docs-community-install-docker.aspx) is configured as follows:

1. Select **My Apps > Compose > Go to Edit Repository > .env** to map port 443 for the container to the host (assuming: 8089)

2. Enter the ONLYOFFICE Docs container, download and run the script that creates the certificate
   ```
   wget -N -P /var/www/onlyoffice/Data https://websoft9.github.io/docker-library/apps/onlyofficedocs/src/createCA.sh
   bash /var/www/onlyoffice/Data/createCA.sh
   ```
3. Modify the container configuration file
   ```
   sed -i 's/“rejectUnauthorized”: true/“rejectUnauthorized”: false/g' /etc/onlyoffice/documentserver/default.json
   supervisorctl restart all
   ```
4. Exit the ONLYOFFICE Docs container and reboot to access it through `http://URL:8089`

## Enterprise Edition

### Why buy through Websoft9?

Websoft9 is ONLYOFFICE Docs [a global partner](https://www.onlyoffice.com/search.aspx?search=websoft9) and one of the technical support centers in China. Purchasing through Websoft9 can help users:

- Purchase paid version with at least 10% discount
- More comprehensive product support
- Integrate technical solutions with more technologies such as web disk, cloud storage, etc 

### Simultaneous connections rule {#onlyofficedocsmaxconn}

ONLYOFFICE Docs Simultaneous Connections: The number of connections open in **edit mode** by all users at the same time, beyond which the document is opened in **preview mode**

### Activate License

Place the License file in the ONLYOFFICE Docs volume **data** directory to take effect immediately

## Configuration options{#configs}

 - [File History (multiple versions)](https://helpcenter.onlyoffice.com/onlyoffice-editors/onlyoffice-document-editor/HelpfulHints/VersionHistory.aspx)(✅): **File > Version History**

 - Support mainstream formats: docx, xlsx, pptx, odt, ods, odp, doc, xls, ppt, pdf, txt, rtf, html, epub, csv, etc

 - OnlyOffice product family is mainly divided into:

    * ENTERPRISE EDITION
    * COMMUNITY EDITION
    * DEVELOPER EDITION

- Authorization Access Control(✅): used for password authentication of third-party software with ONLYOFFICE Docs, ensuring that ONLYOFFICE Docs can be accessed when authorized, supporting protocols like JWT

## Administer{#administrator}

- **Enable JWT Key**: Modify JWT_ENABLED=true in the ONLYOFFICE Docs application **compose** `.env` 

## Troubleshooting{#troubleshooting}

#### csv file containing Chinese characters opens with garbled code?

ONLYOFFICE will let the customer choose the character encoding and field separator when opening a csv file. The following combination generally solves the problem of garbled codes:  

- **GB2313 + comma**  

#### Open Debug log? 

1. Enter the container and modify the */etc/onlyoffice/documentserver/log4js/production.json* file, changing **level**: **WARN** to **level: DEBUG**
2. Run the *supervisorctl restart all* command to take effect 

