---
title: ChatGPT Next Web
slug: /chatgptnextweb
tags:
  - ChatGPT
  - AI
  - OpenAI
  - Artificial Intelligence
  - Chat
---

import Meta from './_include/chatgptnextweb.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of ChatGPT Next Web at Websoft9 console, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Open the **Settings** at the bottom left corner of ChatGPT Next Web.

3. Set the password from the Websoft9 Console for the **Access Password** in the Settings section.

4. Select a item from the Model list.

5. Start to use it

### Switch Azure Services

Azure provides optimized OpenAPi services, and ChatGPT Next Web supports access to Azure AI.

1. Select **My Apps > ChatGPT Next Web > Compose > Go to Edit Repository**, edit the file *.env*  

2. Delete OpenAI related variables and enter Azure related information  
   ```
   AZURE_URL=
   AZURE_API_KEY=
   AZURE_API_VERSION=2023-12-01-preview
   ```
3. Redeploy the application to take effect  

## Configuration options{#configs}

- Multilingual (√)
- Multi-model provider (√)
- OpenAI Multiple versions (√)
- Multi-user (√)
- Mobile (√)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}
