---
title: Redpanda Console
slug: /redpandaconsole
tags:
  - Kafka
  - Visualization
  - Console
---

import Meta from './_include/redpandaconsole.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Redpanda Console at **Websoft9 Console**, if Kafka brokers are not filled in or filled incorrectly, they can be reset by **application orchestration**  

2. When the connection is successful, the following screen will be displayed

   ![](./assets/redpandaconsole-console-websoft9.png)

3. To add the Schema Registry, modify the .env file of the application orchestration.

4. To add Kafka brokers, add the host information (separated by ,) after the `Kafka brokers` variable in the .env file of the application orchestration.

## Configuration options{#configs}

- Kafka connection information: in the .env file of the application orchestration
- Configuration items can be converted to [environment variables](https://docs.redpanda.com/current/reference/console/config/#configuration-sources), e.g: **kafka.brokers > KAFKA_BROKERS**
- Redpanda Console [login authentication](https://docs.redpanda.com/current/reference/console/config/#redpanda-console-configuration-file): Enterprise Edition functions

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### When Redpanda Console container startup exit suddenly?

Ensure Kafka brokers are filled correctly and reachable.

#### Security > Create user function failed?

Description: Failed to create user Redpanda Admin API is not enabled (Status 503).  
Reason: This feature requires Redpanda support and Redpanda is not installed in the application.  
Solution: Install Redpanda and configure Redpanda Console. 
