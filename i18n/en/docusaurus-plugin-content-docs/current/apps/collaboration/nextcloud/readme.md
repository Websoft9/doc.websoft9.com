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

1. Use local Chrome or Firefox to access the URL *https://domain* or *https://Internet IP*.

2. Create administrator account, then set 【Storage & Database】, suggest you select 【MySQL】.

3. Configure the MySQL database connection. ([Don't know password?](./user/credentials)) 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-intall-websoft9.png)
   
4. Click 【Finish Setup】and complete the installation.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-intallss-websoft9.png)

5. Begin your actions on Nextcloud Console.
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-backend-websoft9.png)

6. Go to Marketplace to get more extensions  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-app-websoft9.png)

7. Access URL *https://Internet IP:9002* to check if **OnlyOffice Document Server** has been installed.
   ![](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-documentserver-websoft9.png)

8. Complete [Nextcloud preview and edit](./nextcloud/solution#onlyoffice) settings. (Optional)

> Refer to [Nextcloud admin_manual](https://docs.nextcloud.com/server/latest/admin_manual/) to get more details.


### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**Does Nextcloud support using object storage as a network disk? **

Yes, [reference configuration](#oss)

**Can I have online document editing and preview in Nextcloud?**

The image is pre-installed with [OnlyOffice docs](./onlyofficedocs), which can realize online document editing and preview through configuration, [reference configuration](./nextcloud/solution#onlyoffice)

## Nextcloud QuickStart


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

### 手工安装扩展{#minstallplugin}

网络问题可能会导致无法在线安装扩展，此时就需要手工安装（下面以 ONLYOFFICE 为例）：

1. 到 Nextcloud [官方应用商店](https://apps.nextcloud.com/apps/onlyoffice/releases?platform=22#22)下载扩展

2. 下载到本地后，解压，通过FTP上传到服务器 Nextcloud 应用目录：/data/wwwroot/nextcloud/apps

3. 登录 Nextcloud 后台，进入应用中心，启用 ONLYOFFICE 即可进入下一步操作，开启文档在线预览和编辑

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

### 通过 WebDAV 连接 NextCloud

NextCloud 支持 WebDAV 协议，用户可以通过 WebDAV 来连接并同步文件，比如在 Windows10 系统映射磁盘到 NextCloud，用于本地访问云盘文档。

1. 获取 WebDav 连接 URL： 登录NextCloud，点击【文件】-【设置】获取 URL
  > 注意：每个用户都有自己的 URL，使用对应的 URL 和用户名登录才能正确访问文件

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-webdavurl-websoft9.jpg)

2. 配置本地连接：在 Windows10 【运行】regedit 命令，进入注册表，修改注册表项 HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WebClient\Parameters，将 BasicAuthLevel 值设为 2 ，将 FileSizeLimitInBytes 值改成十进制 50000000
3. 重启本地服务：打开 Windows PowerShell(管理员) 工具，输入命令 net start webclient 重启 webclient 服务
4. 映射本地磁盘：右击【我的电脑】，选择【映射网络驱动器】， 复制第1步中的URL，确定。在弹出的登录界面，输入NextCloud 登录账号，完成连接。
5. 完成上述操作，进入【我的电脑】，可以看见新添加的【网络位置盘符】，双击打开即可访问 NextCloud 远程文件。

## Reference sheet{#parameter}

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage NextCloud  

通过运行 `docker ps`，可以查看到 Nextcloud 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Nextcloud 本身的参数：

### Path{#path}

Nextcloud installation directory： */data/wwwroot/nextcloud*  
Nextcloud 配置文件： */data/wwwroot/nextcloud/config/config.php*  

### Port{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 80   | 通过 HTTP 访问 Nextcloud | 可选   |
| 9002 | OnlyOffice docs on Docker | 可选 |


### Version{#version}

```shell
occ -v
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats nextcloud
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
