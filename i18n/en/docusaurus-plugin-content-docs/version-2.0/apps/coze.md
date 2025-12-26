---
title: Coze
slug: /coze
tags:
  - Programming Assistant
  - AI Agent
  - Coze
---

import Meta from './_include/coze.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Coze at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Complete the install wizard step by step

### Setting Up AI Models

The Coze installed via the Websoft9 console cannot yet utilize its core functionality. Follow these steps:

1. [Orchestrate the HuggingChat application](https://support.websoft9.com/docs/app-compose#dynamic), edit the `.env` file, and set the following variables (using the Deepseek model as an example):

   ```
   MODEL_PROTOCOL_0=“ark”
   MODEL_OPENCOZE_ID_0="100001"
   MODEL_NAME_0="deepseek"                      # Model name (customizable)
   MODEL_ID_0="deepseek-reasoner"               # Model ID provided by the vendor
   MODEL_API_KEY_0=“sk-xxxxxxxxxxxxxxxxxxxxxxx” # API key
   MODEL_BASE_URL_0="https://api.deepseek.com"  # Model base URL
   ```

2. After rebuilding the application, create an AI agent to begin operations.

## Configuration options{#configs}

## Administer{#administrator}

## Troubleshooting{#troubleshooting}
