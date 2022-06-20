---
sidebar_position: 1
slug: /owncloud
tags:
  - ownCloud
  - File sync and share
  - knowledge Management
---

#  ownCloud Getting Started

[ownCloud](https://owncloud.org)  is a self-hosted file sync and share server software. It provides access to your data through a web interface, sync clients or WebDAV while providing a platform to view, sync and share across devices easily — all under your control. ownCloud’s open architecture is extensible via a simple but powerful API for applications and plugins and it works with any storage

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloudgui-websoft9.png)

If you have installed Websoft9 ownCloud, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for ownCloud
4. [Get](./user/credentials) default username and password of ownCloud


## ownCloud Initialization{#init}

### Steps for you

1. Using local Chrome or Firefox to visit the URL *https://domain* or *https://Internet IP*, start to install    
2. You need to set administrator account, then 【Storage&Database】

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-installsetadmin-websoft9.png)
3. Suggest you select **MySQL** for your database    
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-installdb001-websoft9.png)
4. Configure the MySQL database connection([Don't know password?](./user/credentials))  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-installdb002-websoft9.jpg)
5. Click 【Flish Setup】, it has been installed successfully.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-installcomplete-websoft9.png)

> Refer to [ownCloud admin_manual](https://doc.owncloud.org/server/admin_manual/) to get more details


### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  


**Does NextownCloudcloud support using object storage as a network disk? **

Yes, [reference configuration](#oss)

**Can I have online document editing and preview in ownCloud?**

The image is pre-installed with [OnlyOffice docs](./onlyofficedocs), which can realize online document editing and preview through configuration, [reference configuration](./nextcloud/solution#onlyoffice)


## ownCloud QuickStart


## ownCloud Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console
   
2. Log in ownCloud console as administrator, go to 【admin】>【Setting】>【Personal】>【General】, set send to Email address
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-smtp-1-websoft9.png)

3. Go to【Setting】>【Admin】>【General】>【Email Server】, select smtp for send mode and fill in the suitable smtp configuration
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-smtp-2-websoft9.png)

4. Click "Send email" to test your SMTP settings


### DNS Additional Configure（Modify URL）{#dns}

Complete **[Five steps for Domain](./administrator/domain_step)** ，Set the URL for Nextcloud:

1. Modify [ownCloud configuration file](#path)
   ```
   'overwrite.cli.url' => 'ownCloud.yourdomain.com', # Set it to your new domain
   ```
2. Restart PHP-FPM service


### Set Language

Log in owncloud, go to【Personal】>【General】 and set your language

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-zh-websoft9.png)

### ownCloud install apps

Owncloud [Marketplace](https://marketplace.owncloud.com/) have lots of extensions(apps), the following is the step for installing apps

1. Visit [Marketplace](https://marketplace.owncloud.com/), find the app you want to use(e.g OwnBackup)
![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-searchapps-websoft9.jpg)
2. Download and unzip it
3. Upload it to your ownCloud's apps directory: *data/wwwroot/owncloud/apps*
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-ftp-websoft9.png)
4. Enable OwnBackup
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-enableapps-websoft9.png)

> You can install Marketplace's apps online from the ownCloud console also

### ownCloud external storage{#oss}

The External Storage Support application enables you to mount external storage services and devices as secondary ownCloud storage devices. You may also allow users to mount their own external storage services.

1. Log in ownCloud console, install **External storage support** application
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-enablestorage-websoft9.png)

2. Open【Admin】>【Add storage】>【External Storage】, select an external storage service
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-enablestorage002-websoft9.png)

3. Set it
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-auth_mechanism-websoft9.png)

More details please refer to [External Storage](https://doc.owncloud.org/server/admin_manual/configuration/files/external_storage/index.html)


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Jenkins
。 

通过运行`docker ps`，可以查看到 ownCloud 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 ownCloud 本身的参数：

### Path{#path}

ownCloud installation directory： */data/wwwroot/owncloud*  
ownCloud 配置文件： */data/wwwroot/owncloud/config/config.php*  

### Port{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 80   | 通过 HTTP 访问 ownCloud | 可选   |
| 9002 | OnlyOffice Docs on Docker | 可选 |


### Version{#version}

```shell
owncloudcmd
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats owncloud
sudo docker start | stop | restart | stats onlyofficedocs
```

### CLI{#cli}

[owncloudcmd](https://doc.owncloud.com/desktop/next/advanced_usage/command_line_client.html) 命令是 ownCloud 的命令行工具

```
owncloudcmd -h
```

### API

[Provisioning API](https://doc.owncloud.com/server/next/developer_manual/core/apis/provisioning-api.html)

