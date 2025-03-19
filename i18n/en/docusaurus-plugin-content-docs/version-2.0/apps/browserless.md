---
title: Browserless
slug: /browserless
tags:
  - Headless Browser 
  - API Driven
  - Browserless
---

import Meta from './_include/browserless.md';

<Meta name="meta" />

## Getting started{#guide}

### Test the application

1. After installing Browserless in the Websoft9 console, view the application details through **My Applications** and get the access URL in the **Access** tab.

2. Run the following script to test the application, and it will download the website images successfully

    ```
    curl -X POST \
      http://访问URL/screenshot?token=YOUR_API_TOKEN_HERE \
      -H 'Cache-Control: no-cache' \
      -H 'Content-Type: application/json' \
      -d '{
      "url": "https://www.websoft9.com/",
      "options": {
        "fullPage": true,
        "type": "png"
      }
    }' \
      --output "screenshot.png"
    ```

## Configuration options{#configs}

## Administer{#administrator}

## Troubleshooting{#troubleshooting}