---
title: Typesense
slug: /typesense
tags:
  - Instant Search
  - Full-text website search
  - typesense
  - Algolia
---

import Meta from './\_include/typesense.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. After completing the installation of Typesense via the **Websoft9 Console**, retrieve the application's **Overview** and **Access** information from the **My Apps** section.

2. To check if the Typesense service has started correctly, append the **/health** path to the URL:

   ```bash
   # Test service health
   curl "http://URL/health"

   # Test collections
   curl "http://URL/collections" -H "X-TYPESENSE-API-KEY: f324f596-f07b-XP7bz4lUmA@Ln6XH"
   ```

## Configuration Options {#configs}

- **Scraper Config File**: Configure the environment variables **CONFIG** for the `typesense-scraper` container in `docker-compose.yml`.
- **Architecture**: `typesense-scraper` serves as the data crawler, while `typesense` is the data store and search engine.

## Administration {#administrator}

## Troubleshooting {#troubleshooting}
