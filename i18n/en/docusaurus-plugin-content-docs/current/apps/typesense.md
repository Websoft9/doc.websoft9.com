---
title: Typesense
slug: /typesense
tags:
  - Instant Search
  - Full-text website search
  - typesense
  - Algolia
---

import Meta from './_include/typesense.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Typesense at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Browser access: URL + path **health** to see whether the Typesense service is up and running
    ```
    # test health
    curl "http://URL/health"

    # test collections
    curl "http://URL/collections" -H "X-TYPESENSE-API-KEY: f324f596-f07b-XP7bz4lUmA@Ln6XH"
    ```

## Configuration options{#configs}

- Scraper Config File configuration: environment variables for the typesense-scraper container in docker-compose.yml **CONFIG**
- Architecture: typesense-scraper is the data crawler, typesense is the data store and search engine

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

