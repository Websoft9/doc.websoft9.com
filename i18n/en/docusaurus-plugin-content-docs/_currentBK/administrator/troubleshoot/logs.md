---
sidebar_position: 2
slug: /troubleshoot/logs
---

# Log analysis

The log is the evidence, it contains the cause of the issue. "Looking for the problem through the log, predicting the issue and looking for the log" is the most common way to solve the issue.  

## Linux

You can get logs from these methods:  

1. Logs directory: */data/logs/appname*

2. System logs

   ```
   # get service logs
   systemctl status service_name
   journalctl -u service_name

   # get error logs
   journalctl -p err

   # get Linux core logs
   journalctl -k

   # get the bash bin logs
   journalctl /usr/bin/bash

   # get the logs of user by ID
   journalctl UID=33 --since today
   ```

3. Docker logs
   ```
   docker logs appname
   ```

## Windows

Get the logs from **Event Viewer** of Windows Server

![event](https://libs.websoft9.com/Websoft9/DocsPicture/en/windows/open-event-viewer.jpg)
![event](https://libs.websoft9.com/Websoft9/DocsPicture/en/windows/windows-eventerror2-websoft9.png)