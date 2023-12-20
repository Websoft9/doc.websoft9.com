---
sidebar_position: 1
slug: /administrator/upgrade_os
---

# System Update

## Linux Update{#linux}

Run an update command to complete the system update:

``` shell
#For Ubuntu&Debian
apt update && apt upgrade -y

#For Centos&Redhat
yum update -y --skip-broken
``` 

## Windows Update{#windows}

The update of the Windows server is similar to that of the local computer. Manually find the update management program and set the automatic download automatic update.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/windows/windows-upgrade-websoft9.png)