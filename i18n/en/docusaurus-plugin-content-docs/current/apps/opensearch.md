---
title: OpenSearch
slug: /opensearch
tags:
  - Search engines
  - Data Observability
  - opensearch
---

import Meta from './_include/opensearch.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of OpenSearch at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

## Configuration options{#configs}

- [vm.max_map_count=262144](https://opensearch.org/docs/latest/opensearch/install/important-settings/) on Linux (set automatically at application startup)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### OpenSearch not starting?

Ensure host parameters [vm.max_map_count=262144](https://opensearch.org/docs/latest/opensearch/install/important-settings/) 

#### Panel can't connect to OpenSearch?

Make sure OPENSEARCH_HOSTS does not contain an underscore _
