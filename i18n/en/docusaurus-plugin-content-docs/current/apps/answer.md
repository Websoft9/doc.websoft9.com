---
title: Answer
slug: /answer
tags:
  - Q&A platform 
  - Forum Community
  - answer
---

import Meta from './_include/answer.md';

<Meta name="meta" />

## Getting started{#guide}

### Login Verification{#verification}

1. Complete the installation. Access the application’s overview and credentials from the **My Apps**  section in the Websoft9 console.  

2. Starting the verification process.

## Configuration Options{#configs}

- Multilingual (√)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### Automatic installation failed?

There are two possible reasons for this: 

1. All environment variables of the Answer docker image need to be set. Otherwise, it will not switch to automatic installation mode. 
2. If the Answer container is started and there is no connection to an available database at that moment, the automatic installation will be skipped and there will be no attempt to wait or reinstall.
