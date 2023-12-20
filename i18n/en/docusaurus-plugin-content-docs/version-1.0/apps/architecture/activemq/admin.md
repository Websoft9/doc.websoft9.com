---
sidebar_position: 3
slug: /activemq/admin
tags:
  - ActiveMQ
  - IT Architecture
  - Broker
---

# ActiveMQ Maintenance

This chapter is special guide for ActiveMQ maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Backup and Restore   

### Upgrade

ActiveMQ upgrade is similar to installation, you can upgrade it by the following steps

1. Prepare for upgrade
   ```
   docker exec -it activemq bash
   # stop ActiveMQ service
   systemctl stop activemq

   # rename the dir of ActiveMQ for backup
   mv /opt/activemq  /opt/activemqBK
   ```
2. [Download ActiveMQ](http://activemq.apache.org/components/classic/download/) and upload it to the directory */opt* after unzip it, then renamed the directory to *activemq*
3. Run the following modify permissions separately
   ```
   chown -R activemq. /opt/activemq
   chmod 640  /opt/activemq/examples/stomp/php/*
   chmod +x /opt/activemq/bin/activemq
   ```
4. Restart the [ActiveMQ Service](../activemq#service)

## Troubleshoot{#troubleshoot}

In addition to the ActiveMQ issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### ActiveMQ service can't start?

1. Use the debug mode of `activemq console` and you can see the errors
   ```
   docker exec -it activemq bash
   /opt/activemq/bin/activemq
   ```
2. Search the keywords **Failed** or **error** in the log file: */opt/activemq/data/activemq.log*

3. The most common reasons are as follows:

   * The hostname have "." string, e.g: activemq5.6, you must rename it and restart the service by the following commands
   ```
   hostnamectl set-hostname activemq
   systemctl restart activemq
   ```
   * Java environment variable problem. you can use the command `echo $JAVA_HOME` or `which java` to check it

## FAQ{#faq}

#### What the difference between Active Classic and ActiveMQ Artemis?

ActiveMQ Artemis is the next generation of ActiveMQClassic. Refer to: [ActiveMQ Classic](https://activemq.apache.org/getting-started), [ActiveMQ Artemis](https://activemq.apache.org/components/artemis/documentation/)

#### How can I enable the debug mode of ActiveMQ service?

```
docker exec -it activemq bash  
systemctl stop activemq
/opt/activemq/bin/activemq console
```

#### How can I log out ActiveMQ console?

coming soon...
  
#### Is the Tomcat included in the ActiveMQ directory?

Yes, ActiveMQ integrated the Tomcat
  
#### Is it possible to modify the source path of ActiveMQ?

Yes, but you should reset the PATH of ActiveMQ by the following command
  
```
echo 'export PATH="$PATH:/opt/activemq/bin"' >> /etc/profile
```

#### How to change the permissions of file system?

```shell
docker exec -it activemq bash
chown -R activemq.activemq /opt/activemq
find /opt/activemq -type d -exec chmod 750 {} \;
find /opt/activemq -type f -exec chmod 640 {} \;
```