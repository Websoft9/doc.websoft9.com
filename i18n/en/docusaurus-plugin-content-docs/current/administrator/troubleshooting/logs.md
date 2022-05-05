---
sidebar_position: 2
slug: /troubleshooting/logs
---

# 日志诊断技术

日志就是证据，它蕴含了问题的原因。“通过日志找问题，预判问题找日志”是最常见的解决故障的办法。  

## Linux

应用报错后，有如下几个可以分析日志的入口： 

1. 日志文件路径：*/data/logs/appname*

2. 日志管理查看方法

   ```
   # 指定服务日志
   systemctl status appname
   journalctl -u appname

   # 查看 systemd 的错误日志，-p 支持 emerg alert err crit warning notice info debug 等值
   journalctl -p err

   # 查看指定服务的日志
   journalctl -u httpd

   # 查看内核日志
   journalctl -k

   # 查看脚本的日志
   journalctl /usr/bin/bash

   # 查看指定用户的日志
   journalctl UID=33 --since today
   ```

3. Docker 容器日志查看方法
   ```
   docker status appname
   ```

检索关键词 **Failed** 或者 **error** 查看错误

## Windows

按照下列图中所示，进入到 Windows 系统的**事件查看器**，选择 Windows 日志下的应用程序，然后在右侧的事件列表查看出现错误的应用程序，单击即可在下方弹出详细的错误信息，最后就可以根据错误原因来纠正错误。

![event](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-eventerror-websoft9-1.png)
![event](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wampserver/wampserver-eventerror-websoft9-2.png)