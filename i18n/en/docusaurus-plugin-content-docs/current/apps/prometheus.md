---
title: Prometheus
slug: /prometheus
tags:
  - console
  - other
---

import Meta from './\_include/prometheus.md';

<Meta name="meta" />

## Getting Started {#guide}

### Login Verification {#verification}

1. After completing the installation of Prometheus in the **Websoft9 Console**, retrieve the application's overview and access details from **My Apps**.

2. Prometheus can be accessed without authentication by default.

   ![](./assets/prometheus-backend-websoft9.png)

3. (Optional) If you want to control access, you can configure it through the **Websoft9 Gateway**.

### Integrating Grafana {#grafana}

Grafana is a powerful visualization tool for Prometheus. For detailed instructions, refer to: [Grafana Support for Prometheus](https://prometheus.io/docs/visualization/grafana/).

## Configuration Options {#configs}

- Configuration file location (mounted to the server): `/etc/prometheus/prometheus.yml`
- Data collection methods:
  - **Pull**: Directly pull data from the datasource.
  - **Push**: Use Pushgateway to receive pushed data.
- [Basic Authentication](https://prometheus.io/docs/guides/basic-auth/#hashing-a-password)
- Connecting **Alertmanager** and **Pushgateway**: Requires adding configuration files to establish the connection.

## Administration {#administrator}

## Troubleshooting {#troubleshooting}
