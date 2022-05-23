---
sidebar_position: 3
slug: /jenkins/admin
tags:
  - Jenkins
  - DevOps
---

# Jenkins Maintenance

This chapter is special guide for Jenkins maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Jenkins Backup and Restore

[Backup plugin](https://plugins.jenkins.io/backup/) can help you Backup and restore Jenkins very easy.   

### Jenkins Upgrade

Jenkins recommended upgrade scheme:  

1. Login Jenkins. a prompt will appear in the warning bar if the current version is not the latest stable version.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/jenkins/jenkins-warning-websoft9.png)

2. Click warning and select auto upgrade on the pop-up page
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/jenkins/jenkins-selectauto-websoft9.png)

3. Wait on the upgrade page until the auto upgrade is complete
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/jenkins/jenkins-autoupdate-websoft9.png)

4. Restart jenkins service, Jenkins has been updated to the latest stable version 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/jenkins/jenkins-updatecok-websoft9.png)


## Troubleshoot{#troubleshoot}

In addition to the Jenkins issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

## FAQ{#faq}

#### Jenkins support multi-languages?

Yes, you can change you language very easy in you Jenkins Console,Jenkins displays text depending on the language of the browser, refer to[Jenkins Using local language](https://www.jenkins.io/doc/book/using/using-local-language/).

#### How can I extend more functions for Jenkins?

Install more [plugins](https://plugins.jenkins.io/)
