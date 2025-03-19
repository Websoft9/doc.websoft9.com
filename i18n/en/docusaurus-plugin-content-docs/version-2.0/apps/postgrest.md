---
title: PostgREST
slug: /postgrest
tags:
  - console
  - other
---

import Meta from './\_include/postgrest.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. After completing the installation of PostgREST via the **Websoft9 Console**, retrieve the application's **Overview** and **Access** information from **My Apps**.

2. When installing using the Websoft9 console, ensure you fill in the exact PostgreSQL connection URI; otherwise, an error will appear in the container log.

## Configuration Options {#configs}

- Configuration files: You can pass configuration items via environment variables.
- Connect to PostgreSQL database: Modify **W9_POSTGRESQL_URI_SET** in the .env file using **orchestration**.

## Administration {#administrator}

## Troubleshooting {#troubleshooting}

#### Database Connection Error?

Ensure that the PostgreSQL URI is correct and accessible by PostgREST.
