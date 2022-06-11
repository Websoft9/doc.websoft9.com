---
sidebar_position: 1
slug: /activemq
tags:
  - ActiveMQ
  - IT Architecture
  - Broker
---

# ActiveMQ Getting Started

[ActiveMQ](https://activemq.apache.org/) is the most popular and powerful open source messaging and Integration Patterns server.Apache ActiveMQ is fast, supports many Cross Language Clients and Protocols, comes with easy to use Enterprise Integration Patterns and many advanced features while fully supporting JMS 1.1 and J2EE 1.4. Apache ActiveMQ is released under the Apache 2.0 License

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/activemq/activemq-logined-websoft9.png)  

If you have installed Websoft9 ActiveMQ, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** on your Cloud Platform
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:8161** is allowed
3. **[Get](./user/credentials)** default username and password of ActiveMQ
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for ActiveMQ.

## ActiveMQ Installation

### Steps for you
  
1. Using local Chrome or Firefox to visit the URL *http://DNS:8161* or *http://Internet IP:8161*, you will enter installation wizard of ActiveMQ([Don't know password?](./user/credentials))
  ![ActiveMQ console](http://libs.websoft9.com/Websoft9/DocsPicture/zh/activemq/activemq-login-websoft9.png)

2. Click link [Manage ActiveMQ broker] to login ActiveMQ console
  ![ActiveMQ console](http://libs.websoft9.com/Websoft9/DocsPicture/zh/activemq/activemq-logined-websoft9.png)

3. You can reset the password by modify the file */opt/apache-activemq/conf/jetty-realm.properties* 

> More useful ActiveMQ guide, please refer to [Using Apache ActiveMQ](https://activemq.apache.org/using-activemq)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## ActiveMQ QuickStart  

[Using Apache ActiveMQ](https://activemq.apache.org/using-activemq)

## ActiveMQ Setup

### Reset Password

You can reset or set the password by modity the file: */opt/apache-activemq/conf/jetty-realm.properties*, then **systemctl restart activemq**
 
### ActiveMQ Web Demos

ActiveMQ comes with a number of Web demos that illustrate how to use the ActiveMQ broker with REST and AJAX. The Web demos are not activated in the default configuration, so you must follow the steps below to get them running:

1. Edit the */opt/apache-activemq/examples/conf/activemq-demo.xml* file and change the `locations` property to reflect the location of the encrypted credentials file, located at */opt/activemq/conf/credentials-enc.properties*:
  ```shell
  <property name="locations">
        <value>file:${activemq.conf}/credentials-enc.properties</value>
  </property>
  ```

2. If the ActiveMQ server is currently running, stop it:
  ```shell
  systemctl stop activemq
  ```

3. Run the example:
  ```shell
  cd /opt/activemq
  sudo ./bin/activemq console xbean:/opt/activemq/examples/conf/activemq-demo.xml
  ```

4. The ActiveMQ broker should now start.
5. Log in to the Web administration panel and view the demos by browsing to *http://Internet IP:8161/demo*, If needed, use the credentials obtained from the server dashboard to log in.

### Configuration 

Refer to the official docs: http://activemq.apache.org/configuration.html

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage ActiveMQ

### Path
  
You can check the file path by the cmd `whereis` of ActiveMQ, and we have prepared more detail for your reference

```
whereis activemq
whereis java
```
  
ActiveMQ installation directory: */opt/apache-activemq/*  
ActiveMQ configuration directory: */opt/apache-activemq/conf*  
ActiveMQ data directory: */opt/apache-activemq/data*  
ActiveMQ logs directory: */opt/apache-activemq/data/activemq.log*

> you can reset the administrator password of ActiveMQ by modify the file: */opt/apache-activemq/conf/jetty-realm.propertie* 

### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 8161 | HTTP requests for ActiveMQ Console| Optional |
| 5672 | amqp | Optional |

### Version{#version}

```shell
ls /opt/apache-activemq | grep activemq
```

### Service{#service}

```shell
sudo systemctl start | stop | restart | status ActiveMQ
```

### CLI{#cli}
  
```shell
/opt/apache-activemq -h
```
  
### API

[ActiveMQ API](https://activemq.apache.org/maven/apidocs/index.html)