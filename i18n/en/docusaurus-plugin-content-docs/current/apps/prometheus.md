---
title: Prometheus
slug: /prometheus
tags:
  - console
  - other
---

import Meta from './_include/prometheus.md';

<Meta name="meta" />

## Getting started{#guide}

### Login Verification{#verification}

1. Completed installation Prometheus at **Websoft9 console**, get the applicaiton's overview and access information from **My Apps**  

2. Prometheus can be accessed without authentication.   

   ![](./assets/prometheus-backend-websoft9.png)
   
4. Optional: If want to control access, please set it up through the **Websoft9 Gateway**

### Integrate Grafana{#grafana}

Grafana is visual tool for Prometheus, detail refer to: [GRAFANA SUPPORT FOR PROMETHEUS](https://prometheus.io/docs/visualization/grafana/)

## Configuration options{#configs}

- Configuration file in container (have mounted to server): */etc/prometheus/prometheus.yml* 
- Data collection method: Pull directly from datasource and Pushgateway to receive push data
- [Basic Auth](https://prometheus.io/docs/guides/basic-auth/#hashing-a-password)
- Connecting Alertmanager and Pushgateway: requires adding configuration files to implement the connection

## Administer{#administrator}

## Troubleshooting{#troubleshooting}
