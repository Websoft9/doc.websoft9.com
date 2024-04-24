---
sidebar_position: 1
slug: /onlyoffice
tags:
  - ONLYOFFICE Workspace
  - 企业管理
  - CRM
---

# ONLYOFFICE Getting Started

[ONLYOFFICE](https://onlyoffice.com) is a free open source collaborative system developed to manage documents, projects, customer relationship and email correspondence, all in one place. It includes Community Server, Document Server and Mail Server three major cores.

![ONLYOFFICE Console Websoft9](http://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-websoft9-001.png)

If you have installed Websoft9 ONLYOFFICE, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80,9002** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for ONLYOFFICE
4. [Get](./user/credentials) default username and password of ONLYOFFICE

## ONLYOFFICE Initialization

### Steps for you

1. Use local Chrome or Firefox to access the URL *http://domain* or *http://Internet IP*.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-installwait-websoft9.png)

2. Wait for the start up process (which may last for 2-5 mins) until the following page is displayed.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-install-websoft9.png)

3. Set your password, type your email as the username, check the terms and click【Continue】.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-bk-websoft9.png)

4. Log in ONLYOFFICE console and begin your actions.  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-websoft9-001.png)

   * **Documents**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-websoft9-002.png)

   * **Projects**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-websoft9-003.png)

   * **CRM**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-websoft9-004.png)

   * **Document edit and preview**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-websoft9-005.png)

   * **Community**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-function-club-websoft9.png)

   * **Email Portal**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-function-email-websoft9.png)

   * **APPS integration**
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-function-apps-websoft9.png)

> More guide about ONLYOFFICE, please refer to [ONLYOFFICE Documentation](https://helpcenter.onlyoffice.com/server/docker/opensource/index.aspx).


### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  


**Why ONLYOFFICE runs slowly?**

ONLYOFFICE requires much memory, at least 8G is recommended.

## ONLYOFFICE QuickStart

The following uses **ONLYOFFICE Build an Integrated Mail Server** as a task to help users get started quickly:

## ONLYOFFICE Setup

### Document Preview and Editing

The ONLYOFFICE deployment solution provided by Websoft9 contains [ONLYOFFICE Document Server](./onlyofficedocs) by default, and the settings are completed. You can edit and preview online without any settings.

Steps for setting preview and editing are as follows, acting as reference for you to have personalized modifications.

* Log in ONLYOFFICE, open:【Settings】>【Integration】>【Document Service】and you can see the settings.
  ![ONLYOFFICE document service](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-preview-websoft9.png)

* Use local browser to access：*http://Cloud Server Internet IP:9002*, and get the notice that OnlyOffice Document Server is running.
   ![ONLYOFFICE document is running ](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-dkisrunning-websoft9.png)

> Please don't modify the default settings unless you want to replace it with other document service.

### Set Language 

Log in ONLYOFFICE console, open 【Settings】>【Common】>【Customization】, set Language and time zone.

![ONLYOFFICE Language](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-lanuageset-websoft9.png)

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console
   
2. Log in ONLYOFFICE console and open: 【Settings】>【Integration】>【SMTP Settings】

3. Fill in all the fields with accurate information.
   ![ONLYOFFICE SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-smtp-1-websoft9.png)

   > 【Host】and【Send Email Address】must be consistent, otherwise the email cannot be sent.

4. Click 【Send Test Mail】to check if it works.


### Reset password

There are two common measures to reset password for ONLYOFFICE:  

**Change password**

1. Log in ONLYOFFICE console, open:【Administrator】>【Profile】and complete **email validation**.
  ![ONLYOFFICE change password](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-modifypw001-websoft9.png)

2. Return to the profile page, click the arrow next to【Administrator】, then click 【Change password】.
  ![ONLYOFFICE change password](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-modifypw002-websoft9.png)

**Forgot password**

Try to retrieve your password through email when forgot it.

1. Complete [SMTP settings](#smtp)

2. Open ONLYOFFICE login page, click【Forgot】to retrieve the password by email.
  ![ONLYOFFICE forgot password](https://libs.websoft9.com/Websoft9/DocsPicture/en/onlyoffice/onlyoffice-forgetpw-websoft9.png)


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage ONLYOFFICE 


By running `docker ps`, you can view all Containers when ONLYOFFICE is running:

```bash
CONTAINER ID   IMAGE                               COMMAND                  CREATED          STATUS          PORTS                                                                                                                                                                                          NAMES
9e404a923dbb   onlyoffice/controlpanel:3.0.3.410   "/var/www/onlyoffice…"   17 seconds ago   Up 14 seconds   80/tcp, 443/tcp                                                                                                                                                                                onlyoffice-control
e9180dd570a4   onlyoffice/communityserver:latest   "/app/run-community-…"   20 seconds ago   Up 15 seconds   3306/tcp, 5280/tcp, 9865-9866/tcp, 9871/tcp, 9882/tcp, 9888/tcp, 0.0.0.0:5222->5222/tcp, :::5222->5222/tcp, 0.0.0.0:9003->80/tcp, :::9003->80/tcp, 0.0.0.0:49153->443/tcp, :::49153->443/tcp   onlyoffice
2a191ade9b10   onlyoffice/documentserver:7.0       "/app/ds/run-documen…"   25 seconds ago   Up 16 seconds   443/tcp, 0.0.0.0:9002->80/tcp, :::9002->80/tcp                                                                                                                                                 onlyoffice-docs
c90ae46964ba   mysql:5.7                           "docker-entrypoint.s…"   25 seconds ago   Up 16 seconds   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp                                                                                                                                           onlyoffice-db
```

### Path{#path}

ONLYOFFICE Workspace installation directory: */data/apps/onlyoffice*  
ONLYOFFICE Workspace storage directory: */data/apps/onlyoffice/data/community_data*  
ONLYOFFICE Workspace log directory: */data/apps/onlyoffice/data/community_log*  
ONLYOFFICE Workspace document directory: */data/apps/onlyoffice/data/document_data*  

### Port{#port}

| Port Number | Purpose | Necessity |
| ------ | ------------------------------------------ --- | ------ |
| 9002 | ONLYOFFICE docs | optional |

### Version{#version}

```shell
# ONLYOFFICE Community Server version
docker image inspect onlyoffice/communityserver  | grep onlyoffice.community.version | sed -n 1p
```

### Service{#service}

```shell
sudo docker start | stop | restart onlyoffice
sudo docker start | stop | restart onlyoffice-db
sudo docker start | stop | restart onlyoffice-control
sudo docker start | stop | restart onlyoffice-docs
```

### CLI{#cli}

### API

[ONLYOFFICE API](https://api.onlyoffice.com/)

