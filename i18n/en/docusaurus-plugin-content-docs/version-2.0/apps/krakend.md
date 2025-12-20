---
title: KrakenD
slug: /krakend
tags:
  - Unified Gateway
  - API Gateway
  - KrakenD
---

import Meta from './_include/krakend.md';

<Meta name="meta" />

## Getting started{#guide}

### Login verification{#verification}

1. Completed installation KrakenD at Websoft9 console, get the applicaiton's overview and access credentials from **My Apps**  

2. Starting to verify it

### Add Upstream API

1. [Arrange the KrakenD application](https://support.websoft9.com/docs/app-compose#dynamic), adding an entry to the endpoints array in `src/krakend.json` as follows:

```
{
  “endpoint”: “/api/users”,
  “method”: “GET”,
  “timeout”: “5000ms”,
    {
      “url_pattern”: “/api/users”,
      “host”: [“http://localhost:9000”],
      “method”: “GET”
    }
  ]
}
```

2. After rebuilding the application, you can access the upstream API via the unified path.

## Configuration options{#configs}

## Administer{#administrator}

## Troubleshooting{#troubleshooting}