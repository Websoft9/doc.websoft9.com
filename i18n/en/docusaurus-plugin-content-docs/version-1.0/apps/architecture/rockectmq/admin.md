---
sidebar_position: 3
slug: /rocketmq/admin
tags:
  - RocketMQ
  - IT Architecture
  - Broker
---

# RocketMQ Maintenance

This chapter is special guide for RocketMQ maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Backup and Restore 

### Upgrade

RocketMQ upgrade is the same with install a new version, you must completed all resource and data before upgrade.

The following is the step for upgrade:

1. Visit RocketMQ [Download](http://rocketmq.apache.org/docs/quick-start/) to check for the installation requirement

2. Stop RocketMQ service
    ```
    sudo systemctl stop mqnamesrv
    sudo systemctl stop mqbroker
    ```
3. Delete all files in the directory of RocketMQ 
   ```
   rm -rf /data/rocketmq/*
   ```
4. Download the new RocketMQ and unzip it to */data/rocketmq*

5. Modify java runtime memory in the file: *rocketmq/bin/runserver.sh* (Optional)

   > set Xms4g -Xmx4g -Xmn2g to Xms400M -Xmx400M -Xmn200M means reduce the memory limit

6. Modify java runtime memory in the file: *rocketmq/bin/runbroker.sh* (Optional)

7. Restart the RocketMQ and check the status
    ```
    sudo systemctl start mqnamesrv
    sudo systemctl start mqbroker
    systemctl status mqnamesrv
    systemctl status mqbroker
    ```

## Troubleshoot{#troubleshoot}

In addition to the [RocketMQ issues](http://rocketmq.apache.org/docs/faq) listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### 内存不足？

RocketMQ 最低内存设置查看 **runserver.sh** 和 **runbroker.sh**` JAVA_OPT 设置

#### RocketMQ-Console display some error?

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-error-websoft9.png)

Reason: RocketMQ-Console can not connect RocketMQ Server
Solution: Modify the service address of RocketMQ from the docker-compose file

## FAQ{#faq}

#### How is RocketMQ-Console-Ng installed?

Based on Docker

#### RocketMQ-Console-Ng is multilingual supported?

It supports English and simplified Chinese

#### How to install RocketMQ in this project?

Installed by binary package.

#### How long do RocketMQ messages last?

Messages will be saved for up to 3 days, and messages not used for more than 3 days will be deleted.