---
title: ERPNext
slug: /erpnext
tags:
  - console
  - other
---

import Meta from './_include/erpnext.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

After installing ERPNext in Websoft9 console, view the application details through "My Applications" , get the login information in the "Access" tab.
1.Use your local computer browser to access the URL and enter the login screen. After login, the initialization process will start, please choose your own configuration to complete each step.

2.After the installation is complete, the following interface will be poped up.

If there is an installation error occur, you will need to repeat the installation:

## Configuration options{#configs}

- Multi-language (✅)
- SMTP (✅): 
  1. Console [Settings] 
  2. [Email Domain] fill in the SMTP parameters

## Administer{#administrator}

- Reset the administrator password: Go to the ERPNext container and run the command
  '''export GIT_PYTHON_REFRESH=quiet && /usr/local/bin/bench set-admin-password newpassword'''

- Automatic backup (recommended): Log into ERPNext, open: 
  1. [Settings] 
  2. [System Settings] in order.

- Command line backup: 
  '''bench --site URL backup'''

## Troubleshooting{#troubleshooting}

#### 502 failed code?  ranslated with DeepL.com (frrsion)

- Failed to download from Download Backups?

  Reason to be researched.

- Frappe, Bench, ERPNext?

  > ERPNext is a free ERP based on the Frappe framework.
  > Frappe is a framework for rapid development of integrated JS and Python applications.
  > Bench is the CLI tool in the Frappe framework architecture for creating and managing Frappe-based applications.
  > Frappe framework consists of two main parts: 
      - app ( back-end Python code ) 
      - site ( front-end part that handles HTTP requests )

- ERPNext service startup failed?
  Make sure the hostname contains the string "." , e.g. erpnext12.14.0 is a non-compliant hostname for ERPNext!
You can use the following command to change the hostname:

'''hostnamectl set-hostname erpnext''''

- Error reported after changing password in Chrome?

  This is not a server side issue, just update your browser.

- Error when running Bench command ?

  > Error message: You should not run this command as root" when run bench
  > Cause: Bench can only be run from frapper, you must switch to this user first:

  '''su - frapper'''

- ConnectionError: Error 111 for erpnext?
  ERP initialization process will appear ConnectionError: Error 111 for erpnext.The official reply that this kind of error is a normal phenomenon. Because Only configuration job container completed, redis connection is correct.

