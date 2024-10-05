---
title: OpenSearch
slug: /opensearch
tags:
  - Search engines
  - Data Observability
  - opensearch
---

import Meta from './\_include/opensearch.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. After successfully installing OpenSearch from the **Websoft9 Console**, retrieve the application's **Overview** and **Access** details from **My Apps**.

## Configuration Options {#configs}

- Ensure the host parameter [vm.max_map_count=262144](https://opensearch.org/docs/latest/opensearch/install/important-settings/) is set on Linux. This setting is automatically applied at application startup.

## Administration {#administrator}

## Troubleshooting {#troubleshooting}

#### OpenSearch Not Starting?

Ensure that the host parameter [vm.max_map_count=262144](https://opensearch.org/docs/latest/opensearch/install/important-settings/) is correctly configured.

#### Panel Can't Connect to OpenSearch?

Check that `OPENSEARCH_HOSTS` does not include an underscore (`_`) in the hostname.
