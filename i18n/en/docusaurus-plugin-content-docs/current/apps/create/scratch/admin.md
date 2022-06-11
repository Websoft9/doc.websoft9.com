---
sidebar_position: 3
slug: /scratch/admin
tags:
  - Scratch
  - Block-based Visual Programming
---

# Scratch Maintenance

This chapter is special guide for Scratch maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Scratch Upgrade

Use the NPM to manage the Scratch Upgrade. Connect instance by SSH, run the following commands:

```shell
cd /data/wwwroot/scratch-gui
npm install https://github.com/LLK/scratch-gui.git
npm run build
```

## Troubleshoot{#troubleshoot}

In addition to the Scratch issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### Is Scratch open very slowly?{#slowly}

Scratch first loaded data over 20M. For example, if you are using 2M bandwidth, then the ideal load time is: 2000k / (128k/s × 2) = 7.8s. Obviously, if the bandwidth is insufficient, the speed will be very slow.

## FAQ{#faq}

#### Scratch support multi-language?

Yes, you can change language online

#### scratch-www project VS scratch-gui project?

[scratch-www](https://github.com/LLK/scratch-www)  = [scratch-gui](https://github.com/LLK/scratch-gui)  + Sharing community, Scratch-www user login function is still under development

#### Where is the database connection configuration of Scratch?

No need database now

#### Scratch 支持用户注册和登录吗？

暂时不支持
