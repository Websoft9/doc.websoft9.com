---
title: Elasticsearch
slug: /elasticsearch
tags:
  - Elastic Stacks
  - ELK
  - Log Analytics
  - Big Data
---

import Meta from './_include/elasticsearch.md';

<Meta name="meta" />

## Getting started{#guide}

### Login verification{#verification}

1. Completed installation Elasticsearch at Websoft9 console, get the applicaiton's overview and access credentials from **My Apps**  

2. Starting to verify it

### Get Enrollment Token{#token}

The Enrollment Token is necessary for Kibana to connection. It can be reseted by running the command in Elasticsearch:  
  ```
  /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
  ```

### Use Kibana{#kibaba}

Elasticsearch applications do not include [Kibana](./kibana) by default, users can install Kibana  by **App Store** of Websoft9 console.  

### Connect to Logstash{#logstash}

[Logstash](./logstash) is a data collection, processing and delivery pipeline, how does it work with Elasticsearch?

1. Edit the Logstash configuration file

2. Add a new pipeline configuration file with the following contents:
   ```
   input{
      file{
         path => "/var/log/*.log"
         type => "elasticsearch"
         start_position => "beginning"
      }
   }

   ## Add your filters / logstash plugins configuration here

   output {
      elasticsearch {
         hosts => "elasticsearch:9200"
         user => "elastic"
         password => "elastic123"
                  index => "mytest"
      }
   }
   ```

3. Run `curl http://URL/cat/indices?v` to verify the connection between Elasticsearch and Logstash, and that the index is working.

4. Login to Kibana, select **Manage**, and create an **Index Patterns**.  

5. Follow the prompts to complete the creation task, and then retrieve the data using the **timestamp**.

## Configuration options{#configs}

- Default administrator account: elastic
- [Elasticsearch API](https://www.elastic.co/guide/en/elasticsearch/reference/current/http-clients.html)
- Multilingual (✅): add `i18n.locale: "zh-CN"` to Kibana configuration file
- Open source license: [ELASTIC-LICENSE](https://github.com/elastic/elasticsearch/blob/master/licenses/ELASTIC-LICENSE-2.0.txt)
- SMTP (√)

## Administer{#administrator}

- [Email Configuration](https://www.elastic.co/guide/en/elasticsearch/reference/current/actions-email.html): Kibana console, select **Stack Management > Watcher**, add an [**Email Action**](https://www.elastic.co/guide/en/elasticsearch/reference/current/actions.html)  

- Reset password: Run `/usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic` in the ElasticSearch container.

- Backup and restore: Elastic built-in snapshots [backup](https://www.elastic.co/guide/en/elasticsearch/reference/7.13/snapshot-restore.html)

## Troubleshooting{#troubleshooting}

#### ERROR: exit code 137?

Description: ERROR: Elasticsearch exited unexpectedly, with exit code 137     
Reason: Insufficient server memory available for ES at startup or runtime.     
Solution: In practice, this ERROR does not appear if the available memory is more than 1G.   

#### Logstash cannot exporting to ES?

Check that the Elasticsearch account and password are correct in the Logstash pipeline configuration file.

#### TOO_MANY_REQUESTS ... disk usage?

If you see the following error message, you are running out of disk space.  
   ```
   kibana_task_manager_7.17.4_001/_mapping?timeout=60s error: [cluster_block_exception]: index [.kibana_task_manager_7.17.4_001] blocked by : [TOO_MANY_REQUESTS/12/disk usage exceeded flood-stage watermark, index has read-only-allow-delete block];,"}
   ```

ES has high disk space requirements and it is recommended to prepare enough space. 

#### What are the applications included in Elastic?

The **Elastic Stack** is an acronym for three open source projects: Elasticsearch, Logstash, and Kibana.

- Elasticsearch is a database that stores and retrieves data.
- Logstash is a middleware for data extraction, cleansing and organization.
- Kibana is the visual management and analysis interface for Elasticsearch, and Kibana relies on Elasticsearch.

In addition, as Elastic continues to grow, they are adding more products to the ELK family, such as Beats, a log collection tool.

Here is a typical architecture of Elastic Stack for logging scenarios.

 ![](./assets/elastic-architecture-websoft9.png)

#### Is Elasticsearch free?

Elasticsearch consists of the previous open source version and the commercial extension xpack. The basic functionality of xpack is free, and if you need to use all the features, you can apply for a 30-day free trial, and then return to the basic functionality or subscription after the trial period is over.  
