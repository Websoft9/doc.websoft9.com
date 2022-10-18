---
sidebar_position: 1
slug: /owncloud
tags:
  - OwnCloud
  - File sync and share
  - knowledge Management
---

#  OwnCloud Getting Started

[OwnCloud](https://owncloud.org)  is a self-hosted file sync and share server software. It provides access to your data through a web interface, sync clients or WebDAV while providing a platform to view, sync and share across devices easily — all under your control. OwnCloud’s open architecture is extensible via a simple but powerful API for applications and plugins and it works with any storage

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloudgui-websoft9.png)

If you have installed Websoft9 OwnCloud, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for OwnCloud
4. [Get](./user/credentials) default username and password of OwnCloud


## OwnCloud Initialization{#init}

### Steps for you

1. Using local Chrome or Firefox to visit the URL *https://domain* or *https://Internet IP*, access to login page  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-init1-websoft9.png)
   
2. Fill in the login information([Don't know password?](./user/credentials))  
   
3. Click 【login】, it has been installed successfully.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-installcomplete-websoft9.png)

> Refer to [OwnCloud admin_manual](https://doc.owncloud.org/server/admin_manual/) to get more details


### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  


**Does NextOwnCloudcloud support using object storage as a network disk? **

Yes, [reference configuration](#oss)

**Can I have online document editing and preview in OwnCloud?**

The image is pre-installed with [OnlyOffice docs](./onlyofficedocs), which can realize online document editing and preview through configuration, [reference configuration](./nextcloud/solution#onlyoffice)


## OwnCloud QuickStart


## OwnCloud Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console
   
2. Log in OwnCloud console as administrator, go to 【admin】>【Setting】>【Personal】>【General】, set send to Email address
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-smtp-1-websoft9.png)

3. Go to【Setting】>【Admin】>【General】>【Email Server】, select smtp for send mode and fill in the suitable smtp configuration
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-smtp-2-websoft9.png)

4. Click "Send email" to test your SMTP settings


### DNS Additional Configure（Modify URL）{#dns}

Complete **[Five steps for Domain](./administrator/domain_step)** ，Set the URL for Nextcloud:

1. Modify [OwnCloud configuration file](#path)
   ```
   'overwrite.cli.url' => 'OwnCloud.yourdomain.com', # Set it to your new domain
   ```
2. Restart PHP-FPM service


### Set Language

Log in owncloud, go to【Personal】>【General】 and set your language

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-zh-websoft9.png)

### OwnCloud install apps

Owncloud [Marketplace](https://marketplace.owncloud.com/) have lots of extensions(apps), the following is the step for installing apps

1. Visit [Marketplace](https://marketplace.owncloud.com/), find the app you want to use(e.g OwnBackup)
![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-searchapps-websoft9.jpg)
2. Download and unzip it
3. Upload it to your OwnCloud's apps directory: *data/wwwroot/owncloud/apps*
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-ftp-websoft9.png)
4. Enable OwnBackup
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-enableapps-websoft9.png)

> You can install Marketplace's apps online from the OwnCloud console also

### OwnCloud external storage{#oss}

The External Storage Support application enables you to mount external storage services and devices as secondary OwnCloud storage devices. You may also allow users to mount their own external storage services.

1. Log in OwnCloud console, install **External storage support** application
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-enablestorage-websoft9.png)

2. Open【Admin】>【Add storage】>【External Storage】, select an external storage service
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-enablestorage002-websoft9.png)

3. Set it
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-auth_mechanism-websoft9.png)

More details please refer to [External Storage](https://doc.owncloud.org/server/admin_manual/configuration/files/external_storage/index.html)


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage OwnCloud

Run `docker ps`, view all containers when OwnCloud is running:  

```bash
CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS                    PORTS                                                  NAMES
5da52ff1d010   phpmyadmin:latest        "/docker-entrypoint.…"   18 minutes ago   Up 18 minutes             0.0.0.0:9090->80/tcp, :::9090->80/tcp                  phpmyadmin
0f4a5b87d637   owncloud/server:latest   "/usr/bin/entrypoint…"   18 minutes ago   Up 18 minutes (healthy)   0.0.0.0:9001->8080/tcp, :::9001->8080/tcp              owncloud
800709fedbfd   mysql:5.7                "docker-entrypoint.s…"   18 minutes ago   Up 18 minutes (healthy)   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   owncloud-db
c8b84fb0dca3   redis:6                  "docker-entrypoint.s…"   18 minutes ago   Up 18 minutes (healthy)   6379/tcp                                               owncloud-redis

```

### Path{#path}


OwnCloud installation directory: */data/apps/owncloud*  
OwnCloud data directory: */data/apps/owncloud/data/owncloud*  
OwnCloud configure file: */data/apps/owncloud/data/owncloud/config/config.php*  
Onlyofficedocs installation directory: */data/apps/onlyofficedocs*
  

### Port{#port}

| Port Number | Purpose | Necessity |
| ------ | ------------------------------------------ --- | ------ |
| 9002 | OnlyOffice Docs on Docker | Optional |


### Version{#version}

```shell
owncloudcmd
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats owncloud
sudo docker start | stop | restart | stats owncloud-db
sudo docker start | stop | restart | stats owncloud-redis
sudo docker start | stop | restart | stats onlyofficedocs
```

### CLI{#cli}

[owncloudcmd](https://doc.owncloud.com/desktop/next/advanced_usage/command_line_client.html) ss OwnCloud's CLI

```
owncloudcmd -h
```

### API

[Provisioning API](https://doc.owncloud.com/server/next/developer_manual/core/apis/provisioning-api.html)

