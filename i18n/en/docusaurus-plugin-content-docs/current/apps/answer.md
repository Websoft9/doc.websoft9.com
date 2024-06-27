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

1. Completed installation Answer at Websoft9 console, get the applicaiton's overview and access credentials from **My Apps**  

2. Starting to verify it

## Configuration options{#configs}

- Multilingual (√)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### Automatic installation failed?

Two possible reasons for it: 

1. All environment variables of the Answer docker image need to be set, otherwise it will not switch to automatic installation mode 
2. After the Answer container is started, if there is no connection to an available database at the first moment, the automatic installation will be skipped and there will be no attempt to wait or install again
