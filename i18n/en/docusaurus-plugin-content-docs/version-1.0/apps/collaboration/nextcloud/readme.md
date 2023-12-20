---
sidebar_position: 1
slug: /nextcloud
tags:
  - Nextcloud
  - File sync and share
  - knowledge Management
---

# Nextcloud Getting Started

[Nextcloud](https://nextcloud.com)  is the next generation open source Enterprise File Sync and Share started by ownCloud inventor Frank Karlitschek and a dozen experienced open source entrepreneurs and engineers to empower users to take back control over their data and communication.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-gui-websoft9.png)

If you have installed Websoft9 Nextcloud, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:9002** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Nextcloud
4. [Get](./user/credentials) default username and password of Nextcloud


## Nextcloud Initialization{#init}

### Steps for you

1. Use local Chrome or Firefox to access the URL *https://domain* or *https://Internet IP*, access install wizard page
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-wizard-websoft9.png)
   
2. Set the user name and password and keep it in mind, click [Install], and choose to install plugins or skip according to your needs
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-plugin-websoft9.png)

3. Close the pop-up window and start to experience the background
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-main-websoft9.png)

4. Go to Marketplace to get more extensions  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-app-websoft9.png)

5. Access URL *https://Internet IP:9002* to check if **OnlyOffice Document Server** has been installed.
   ![](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-documentserver-websoft9.png)

6. Complete [Nextcloud preview and edit](./nextcloud/solution#onlyoffice) settings. (Optional)

> Refer to [Nextcloud admin_manual](https://docs.nextcloud.com/server/latest/admin_manual/) to get more details.


### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**Does Nextcloud support using object storage as a network disk? **

Yes, [reference configuration](#oss)

**Can I have online document editing and preview in Nextcloud?**

The image is pre-installed with [OnlyOffice docs](./onlyofficedocs), which can realize online document editing and preview through configuration, [reference configuration](./nextcloud/solution#onlyoffice)

## Nextcloud QuickStart

This task **Nextcloud builds enterprise network disk system** is for your Nextcloud QuickStart:

## Nextcloud Setup

### Mobile apps

Steps for using Nextcloud mobile apps are as follows:

1. [Download](https://nextcloud.com/install) mobile apps.
2. [Connect](https://docs.nextcloud.com/android/) to your Nextcloud server.

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console
   
2. Log in Nextcloud console as administrator, go to 【Admin】>【Additianal settings】>【Email server】, select SMTP for send mode
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-setsmpt001-websoft9.png)

3. Fill in the suitable smtp configuration
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-setsmpt002-websoft9.png)

4. Click "Send email" to test your SMTP settings

### DNS Additional Configure（Modify URL）{#dns}

Complete **[Five steps for Domain](./administrator/domain_step)** ，Set the URL for Nextcloud:

1. Modify [Nextcloud configuration file](#path)
   ```
   'overwrite.cli.url' => 'nextcloud.yourdomain.com', # Set it to your new domain
   ```
2. Restart PHP-FPM service


### Set Language

Log in nextcloud, go to【Personal】>【Personal Info】 and set your language.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-mylanguage-websoft9.png)

### Install apps

Nextcloud integrated [Marketplace](https://marketplace.nextcloud.com/) that have lots of extensions(apps). Steps for installing apps as as follows:

1. Log in Nextcloud, go to【Apps】>【App bundles】, search the apps you want.

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-backendmk-websoft9.png)
2. Install it online.

### Manually install the extension {#minstallplugin}

Network problems may cause the extension to be unable to be installed online. In this case, manual installation is required (take ONLYOFFICE as an example below):

1. Go to Nextcloud [Official App Store](https://apps.nextcloud.com/apps/onlyoffice/releases?platform=22#22) to download the extension

2. After downloading, unzip and upload to the Nextcloud application directory via FTP: */var/lib/docker/volumes/nextcloud_nextcloud/_data/apps*, change the owner and group user of the onlyoffice directory to *www-data*  

3. Log in to the Nextcloud background, enter the application center, enable ONLYOFFICE to proceed to the next step, and enable online preview and editing of documents

### Nextcloud external storage{#oss}

The External Storage Support application enables you to mount external storage services and devices as secondary Nextcloud storage devices. You may also allow users to mount their own external storage services.

1. Log in Nextcloud console, enable **External storage support** application.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-enablestorage-websoft9.png)

2. Open【Admin】>【External Storage】, select an external storage service.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-enablestorage002-websoft9.png)

3. Set it.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-auth_mechanism-websoft9.png)

For more details, please refer to [External Storage](https://docs.nextcloud.com/server/latest/admin_manual/configuration_files/external_storage_configuration_gui.html).


### Nextcloud transfer

Nextcloud source code and data is stored in system disk by default, you can transfer them to data disk or Object storage:

**to data disk**

1. Purchase a data disk from Cloud Platform, then **attach** it to Nextcloud Server.

2. Use SFTP tool to connect Server and stop service.
   ```
   systemctl stop httpd
   ```

3. Create a new folder */data/wwwroot/nextcloud2* 

4. Initialize data disk, and **mount** it to *nextcloud2* folder

5. Copy all files in */data/wwwroot/nextcloud* to */data/wwwroot/nextcloud2* 
6. 
7. Modify the Nextcloud directory in  [vhost configuration file](./apache#virtualhost)

8. Start the service.
   ```
   systemctl start httpd
   ```

**to Object storage**

1. Purchase Object storage from Cloud Platform, then create a new **bucket**.

2. Use SFTP tool to connect Server and stop service.
   ```
   systemctl stop httpd
   ```

3. Create a new folder */data/wwwroot/nextcloud2*. 
4. Then **mount** it to *nextcloud2* folder
5. Copy all files in */data/wwwroot/nextcloud* to */data/wwwroot/nextcloud2*  
6. Modify the Nextcloud directory in  [vhost configuration file](./apache#virtualhost) 
7. Start the service
   ```
   systemctl start httpd
   ```
8. Set the object storage to boot automatically. (Different cloud platform need different operations)

> The **mount** command is very difficult for users, and there is a risk of copy failure if the data exceeds 10G.

### Connect NextCloud via WebDAV

NextCloud supports the WebDAV protocol. Users can connect and synchronize files through WebDAV, such as mapping disks to NextCloud on Windows10 systems for local access to cloud disk documents.

1. Obtain the WebDav connection URL: Log in to NextCloud, click [File] - [Settings] to obtain the URL
  > Note: Each user has their own URL, use the corresponding URL and username to log in to access the file correctly

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-webdavurl-websoft9.jpg)

2. Configure the local connection: in Windows10 [run] the regedit command, enter the registry, modify the registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WebClient\Parameters, set the BasicAuthLevel value to 2, and change the FileSizeLimitInBytes value to decimal 50000000
3. Restart the local service: Open the Windows PowerShell (Administrator) tool and enter the command net start webclient to restart the webclient service
4. Map local disk: Right-click [My Computer], select [Map Network Drive], copy the URL in step 1, and click OK. In the pop-up login interface, enter the NextCloud login account to complete the connection.
5. After completing the above operations, enter [My Computer], you can see the newly added [Network Location Drive Letter], double-click to open it to access the NextCloud remote file.
## Reference sheet{#parameter}

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage NextCloud  

Run docker ps, view all containers when Nextcloud is running:

```bash
CONTAINER ID   IMAGE                              COMMAND                  CREATED             STATUS             PORTS                                                  NAMES
c8a5fae52a35   onlyoffice/documentserver:latest   "/app/ds/run-documen…"   59 minutes ago      Up 59 minutes      443/tcp, 0.0.0.0:9002->80/tcp, :::9002->80/tcp         onlyofficedocs
5523e9c3a9bd   phpmyadmin:latest                  "/docker-entrypoint.…"   59 minutes ago      Up 59 minutes      0.0.0.0:9090->80/tcp, :::9090->80/tcp                  phpmyadmin
6ecb1771a868   nextcloud:latest                   "/entrypoint.sh apac…"   About an hour ago   Up About an hour   0.0.0.0:9001->80/tcp, :::9001->80/tcp                  nextcloud
ae358a9bb912   mysql:8.0                          "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   nextcloud-db
```

### Path{#path}

Nextcloud installation directory: */data/apps/nextcloud*  
Nextcloud data directory: */data/apps/nextcloud/data/nextcloud-data*  
Nextcloud site directory: */data/apps/nextcloud/data/nextcloud*  
Nextcloud configuration file: */data/apps/nextcloud/data/nextcloud/config/config.php*  
Onlyofficedocs installation directory: */data/apps/onlyofficedocs*  

### Port{#port}

| Port Number | Purpose | Necessity |
| ------ | ------------------------------------------ --- | ------ |
| 9002 | OnlyOffice docs on Docker | Optional |

### Version{#version}

```shell
docker exec -i nextcloud cat version.php |grep OC_VersionString |awk -F "'" '{print $2}'
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats nextcloud
sudo docker start | stop | restart | stats nextcloud-db
sudo docker start | stop | restart | stats phpmyadmin
sudo docker start | stop | restart | stats onlyofficedocs
```

### CLI{#cli}

occ 命令是 Nextcloud 的命令行界面。 OCC 可安装和升级 Nextcloud，管理用户，加密，密码管理，LDAP设置等。  

```
sudo -u www-data php occ
Nextcloud version 19.0.0

Usage:
 command [options] [arguments]

Options:
 -h, --help            Display this help message
 -q, --quiet           Do not output any message
 -V, --version         Display this application version
     --ansi            Force ANSI output
     --no-ansi         Disable ANSI output
 -n, --no-interaction  Do not ask any interactive question
     --no-warnings     Skip global warnings, show command output only
 -v|vv|vvv, --verbose  Increase the verbosity of messages: 1 for normal output,
                       2 for more verbose output and 3 for debug

Available commands:
 check                 check dependencies of the server
                       environment
 help                  Displays help for a command
 list                  Lists commands
 status                show some status information
 upgrade               run upgrade routines after installation of
                       a new release. The release has to be
                       installed before.
```

### API

[Basic APIs](https://docs.nextcloud.com/server/latest/developer_manual/client_apis/WebDAV/basic.html)
