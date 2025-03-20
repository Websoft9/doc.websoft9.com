---
title: Logstash
slug: /logstash
tags:
  - ELK 
  - Data Collection
  - Log Collection
  - Inputs and outputs
---

import Meta from './_include/logstash.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completing the installation of Logstash in the **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

### Capturing (Input) Data

In Logstash's configuration file, specify one or more input plugins to define the source of your data. Logstash provides a variety of built-in input plugins, such as File, TCP, UDP, HTTP, and more. Choose the appropriate input plugin based on your needs and configure its parameters.

### Filtering data
For data processing, configure filtering plugins (for example, grok, mutate, date) to parse, modify, or enrich data based on its structure and your requirements.

### Exporting data

#### To Elasticsearch 

Refer to: [Elasticsearch Connection Logstash](./elasticsearch#logstash)

#### To Kafka

1. Install the Kafka plugin.
2. Add the connection configuration to the configuration file. 
   ```
   output {
      kafka {
        bootstrap_servers => "kafka_host:port" # Kafka server host and port
        topic_id => "your_topic" # Name of the Kafka topic
      }
    }
   ```

## Configuration options{#configs}

- Logstash configuration file (mounted): *usr/share/logstash/pipeline/logstash.conf*

## Administer{#administrator}


## Troubleshooting{#troubleshooting}

