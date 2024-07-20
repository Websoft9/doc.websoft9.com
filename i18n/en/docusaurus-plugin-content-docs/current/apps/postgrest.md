---
title: PostgREST
slug: /postgrest
tags:
  - console
  - other
---

import Meta from './_include/postgrest.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of PostgREST at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. When installing the Websoft9 console, you need to fill in the exact Postgresql connection URI or there will be an error in the container log

## Configuration options{#configs}

- Configuration files: you can transfer configuration items via environment variables
- Connect to Postgres database: apply **orchestration** to modify **W9_POSTGRESQL_URI_SET** in .env file

## Administer{#administrator}


## Troubleshooting{#troubleshooting}

#### Database connection error?

Ensure that the Postgresql URI is correct and can be accessed by PostgREST  

