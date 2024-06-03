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

1. Completed installation Prometheus at Websoft9 console, get the applicaiton's overview and access information from "My Apps"  

2. Prometheus can be accessed without authentication. To control access, please set it up through the Websoft9 gateway

### Integrate Grafana{#grafana}

Grafana can be used as a visual representation for Prometheus, detail refer to: [GRAFANA SUPPORT FOR PROMETHEUS](https://prometheus.io/docs/visualization/grafana/)

## Configuration options{#configs}

- Configuration file (mounted): */etc/prometheus/prometheus.yml* 
- Data collection method: Mainly using Pull method, while introducing Pushgateway to receive push data from the collected end, and then pulling it from Pushgateway
- [basic auth](https://prometheus.io/docs/guides/basic-auth/#hashing -A-password)
- Connecting Alertmanager and Pushgateway: requires adding configuration files to implement the connection

## Administer{#administrator}

## Troubleshooting{#troubleshooting}
