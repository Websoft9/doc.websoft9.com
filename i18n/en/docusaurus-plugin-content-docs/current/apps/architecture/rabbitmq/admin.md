---
sidebar_position: 3
slug: /rabbitmq/admin
tags:
  - RabbitMQ
  - IT Architecture
  - Broker
---

# RabbitMQ Maintenance

This chapter is special guide for RabbitMQ maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Backup & Restore
  
### Upgrade

Refer to the official docs: [Upgrading RabbitMQ](https://www.rabbitmq.com/upgrade.html)


## Troubleshoot{#troubleshoot}

In addition to the RabbitMQ issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### Can't remote connect RabbitMQ?

* Enable the **TCP:5672** and **TCP:15672** ports of your Security Group of your Cloud Platform
* The user of RabbitMQ was assigned the suitable role (The user **test** can't connect from remote because it has not been assigned any role in the the picture below)
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-createusererror-websoft9.png)

#### RabbitMQ service can't start?

1. Use the debug mode of `rabbitmq-server console` and you can see the errors
   ```
   rabbitmq-server console
   ```
2. Search the keywords **Failed** or **error** from logs: */data/logs/rabbitmq-server*

#### Error in Chrome when modify password?

This error is not attribute to RabbitMQ server, once you have upgraded you local Chrome, it solved

![chrome error of RabbitMQ](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rabbitmq/rabbitmq-chromeerror-websoft9.png)

## FAQ{#faq}

#### How can I enable the debug mode of RabbitMQ service?

```
systemctl stop rabbitmq-server
rabbitmq-server console
```

#### Can I reset password of RabbitMQ by command?

Yes, e.g `rabbitmqctl change_password  admin newpassword`