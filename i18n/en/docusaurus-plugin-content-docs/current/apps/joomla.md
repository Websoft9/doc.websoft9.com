---
title: Joomla
slug: /joomla
tags:
  - CMS
  - Content management
  - Website
  - Building a Station
---

import Meta from './_include/joomla.md';

<Meta name="meta" />

## Getting started{#guide}

### Login Verification{#verification}

1. Completed installation Joomla at Websoft9 console, get the applicaiton's overview and access credentials from "My Apps"  

2. Starting to verify it, Joomla has powerful management and configuration capabilities, mainly accessed through the "System"

   ![](./assets/joomla-system-websoft9.png)

### Install Language

Joomla language is defaults to English, and requires other languages to login to the backend for installation:

1. Joomla backend: **System > Install > Languages** The language required for installation

2. Edit user attributes: **Edit Profile > Basic Settings** select the language for the front and backend respectively, and save it to take effect

### Install extension{#plugin}

1. Joomla backend: **System > Install > Extensions** access the extension management page

2. Choose the online installation method(Install From Web)

### Install template{#template}

Joomla's template installation is mainly achieved by uploading template installation packages:

1. Prepare the template installation package(.zip file), as the Joomla kernel cannot be packaged in the template

2. Joomla backend: **System > Install > extensions** to enter the extension management interface

3. Choose the upload package file method for installation

4. **System > Templates** Management Template


## Configuration options{#configs}

- [Joomla! Extensions Directory™](https://extensions.joomla.org/)

- SMTP(✅): Backend **System > Global Configuration > Server > Mail > Mailer**, server email type selection: SMTP

- Multilingual(✅): Install the language in the backend **System > Install > Languages**, and select the desired language

- Component Multilingual(✅)

- Cache: Backend **System > Maintenance > Clear Cache**

- Configuration file: */path/configuration.php*

- [Joomla API](https://api.joomla.org/)

- Backend address: `http://URL/administrator`

- Online upgrade(✅)

## Administer{#administrator}

- Online backup: By installing the Joomla extension [Akeeda](https://www.akeebabackup.com/download.html), can achieve online backup in the background

## Troubleshooting{#troubleshooting}