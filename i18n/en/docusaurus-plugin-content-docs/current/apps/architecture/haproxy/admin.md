---
sidebar_position: 3
slug: /haproxy/admin
tags:
  - HAProxy
  - High Availability
---

# HAProxy Maintenance

This chapter is special guide for HAProxy maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Backup and Restore   

### Upgrade

If the version update by YUM/APT it not suitable for you, please use the [resource build installation](https://github.com/haproxy/haproxy/blob/master/INSTALL)to update HAProxy

## Troubleshoot{#troubleshoot}

In addition to the HAProxy issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

## FAQ{#faq}
  
#### What kind of installation method is used in this deployment solution to install HAProxy?

yum or apt
  
#### Can I reset password of HAProxy?

Yes, modify the configuration file `/etc/haproxy/haproxy.cfg`
  
#### Is there a web-base GUI database management tools?

Yes, HAProxy Statistics Report was enabled, you can visit it by URL: *http://Internet IP:1080/haproxy*