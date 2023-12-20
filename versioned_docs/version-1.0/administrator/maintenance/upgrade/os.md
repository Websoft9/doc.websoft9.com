---
sidebar_position: 1
slug: /administrator/upgrade_os
---

# 操作系统更新

## Linux 更新{#linux}

Linux服务器以及组件的更新，只需要运行一条命令即可完成：  

```
# CentOS or Redhat
sudo yum update -y

# Ubuntu & Debian
apt update && apt upgrade -y
```

> 建议用户将更新命令设置成**计划任务**，实现自动升级。  

## Windows 更新{#windows}

Windows服务器的更新与本地电脑类似，手动找到更新管理程序，设置自动下载自动更新即可。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/windows/windows-upgrade-websoft9.png)