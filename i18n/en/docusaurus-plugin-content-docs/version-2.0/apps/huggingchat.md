---
title: HuggingChat
slug: /huggingchat
tags:
  - AI Chat Assistant
  - Chatbot
  - HuggingChat
---

import Meta from './_include/huggingchat.md';

<Meta name="meta" />

## Getting started{#guide}

### Login verification{#verification}

1. Completed installation HuggingChat at Websoft9 console, get the applicaiton's overview and access credentials from **My Apps**  

2. Starting to verify it

### Model Acquisition and Authorization

HuggingChat installed via the Websoft9 console cannot initiate AI chat immediately. The following steps are required:

1. Register an account on the [Hugging Face official website](https://huggingface.co/).

2. Generate an Access Token in your personal settings. This Token serves as your "key" for downloading certain models from the platform and interacting with the API.

3. [Configure the HuggingChat application](https://support.websoft9.com/docs/app-compose#dynamic). Set `OPENAI_API_KEY_SET` in the `.env` file to the Token generated in step 2.

4. Rebuild the application to select suitable models for AI chat.

## Configuration options{#configs}

## Administer{#administrator}

## Troubleshooting{#troubleshooting}