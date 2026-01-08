---
title: SigNoz
slug: /signoz
tags:
  - Cloud Native APM 
  - Observability Platform 
  - SigNoz
---

import Meta from './_include/signoz.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of SigNoz at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Complete the install wizard step by step

### Monitoring Application 

1. [Compose SigNoz Application](https://support.websoft9.com/docs/app-compose#dynamic), edit the `docker-compose.yml` file to map the otel-collector ports to the external network 

2. Integrate the OpenTelemetry SDK into your application 

3. Configure the OTLP exporter to point to 
    - gRPC: `http://yourip:4317` 
    - HTTP: `http://yourip:4318`

## Configuration options{#configs}

## Administer{#administrator}

## Troubleshooting{#troubleshooting}