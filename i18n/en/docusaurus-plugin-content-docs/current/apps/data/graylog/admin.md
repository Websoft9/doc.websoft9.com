---
sidebar_position: 3
slug: /graylog/admin
tags:
  - Graylog
  - Data Analysis
  - Log Management
---

# Graylog Maintenance

This chapter is special guide for Graylog maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Graylog Cluster

Graylog includes the following software when launched:

- Graylog log collection and analysis
- ElasticSearch log storage
- MongoDB system configuration system

Graylog supports simple deployment：  
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-minisetup-websoft9.png)

Graylog supports complex [cluster](https://docs.graylog.org/v1/docs/multinode-setup) deployments：  
![Graylog cluster](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-hasetup-websoft9.png)

Among them, MongoDB can be used without clustering.



> For more information, please refer to the [official architecture guide](https://www.slideshare.net/Graylog/graylog-engineering-design-your-architecture)

### Backup and Restore

### Upgrade

## Troubleshoot{#troubleshoot}

In addition to the Graylog issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### Log in to the system, have alarms and error prompts?

**Phenomena 1**：Prompt: There is a node without any running inputs. This means ... ？
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-nofiinput-websoft9.png)
**Causes**：This is a reminder without input, not an error
**Solutions**：Create a new local input

**Phenomena 2**：Prompt: Index rotation strategy null not found... ?  
**Causes**：The disk has less than 15 percent free space  
**Solutions**：Free up redundant files or increase server disk space

## FAQ{#faq}

#### Graylog Architecture?

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-arch-websoft9.png)

#### Graylog HA deployment?

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/architec_bigger_setup.png)