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

2. Select **Settings** at the bottom left corner of ChatGPT Next Web.

3. Locate the **Access Password** in the Settings section and set the password from the Websoft9 console.

4. Select a item from the Model list.

5. Start to use it

### Switch Azure Services

Azure provides optimized OpenAPi services, and ChatGPT Next Web supports access to Azure AI.

1. Select **My Apps > ChatGPT Next Web > Compose > Prompt Adjustment**, edit the file *.env*  

2. Delete OpenAI related variables and enter Azure related information  
   ```
   AZURE_URL=
   AZURE_API_KEY=
   AZURE_API_VERSION=2023-12-01-preview
   ```

3. Rebuild the application to take effect  

### Cost savings

- Use **New Chat** to minimize unnecessary ongoing conversations: ongoing conversations consume a lot of processing power.  
- Set the right number of **Attached Messages Count**: setting it too high consumes a lot of power.  
- Use the preview model: preview is the official preview model, priced at 1/5 the cost of the full version.  

## Purchase OpenAI 

Websoft9 can procure OpenAI API services from Azure on behalf of our [Customer Success Team](./helpdesk).

## Configuration options{#configs}

- Multilingual (√)
- Multi-model provider (√)
- OpenAI Multiple versions (√)
- Multi-user (√)
- Mobile (√)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}