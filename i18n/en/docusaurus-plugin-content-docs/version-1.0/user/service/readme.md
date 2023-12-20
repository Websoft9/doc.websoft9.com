---
sidebar_position: 2
slug: /user/cloud
---

import DocCardList from '@theme/DocCardList';
import {useCurrentSidebarCategory} from '@docusaurus/theme-common';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Cloud Service Guide

You should have some skills about Cloud Server when you use open source software on Cloud Platform.  

<DocCardList items={useCurrentSidebarCategory().items}/>

## Connect Server{#connect}

If you only need to connect to the Server, and you have prepared the server's [administrator account and password](../user/credentials#osaccount), Internet IP address and other information, you can refer to the following general tutorial to start connecting to the server.

### For Linux{#connectlinux}

We suggest you use SFTP to connect Linux. SFTP is an FTP mode that uses the SSH protocol, also known as security-enhanced FTP. The SFTP tool is a favorite operation mode for Linux users. The following is an example of WinSCP SFTP tool, which details the use of SFTP.

#### Configure WinSCP

1. Download [WinSCP](https://winscp.net/) and install it, then start it to create a new connection

2. The following is based on the cloud server's **password verification** and **key-key pair** verification:
   - Password authentication(the most common way)
     ![Password authentication](http://libs.websoft9.com/Websoft9/DocsPicture/en/winscp/winscp-newsite.png)
   - Key-key pair authentication
     ![Key-key pair authentication](http://libs.websoft9.com/Websoft9/DocsPicture/en/winscp/winscp-secrets-websoft9.png)

3. You may want to save your session details to a site so you do not need to type them in every time you want to connect. Press Save button and type site name.
   ![Save session](http://libs.websoft9.com/Websoft9/DocsPicture/en/winscp/winscp-sessionsave-websoft9.png)

4. Successfully connected interface
   ![WinSCP GUI](http://libs.websoft9.com/Websoft9/DocsPicture/en/winscp/websoft9-winscp-success.png)

##### Manage Files

WinSCP can easily upload and download files by dragging and dropping, and can perform various settings and operations on files (folders).

1. In general, the files on the website are placed in the */data/wwwroot* directory.
   ![upload files](http://libs.websoft9.com/Websoft9/DocsPicture/en/winscp/winscp-dragfile-websoft9.png)

2. You can perform multiple operations on the VM by right-clicking on a file or folder on the server.
   ![Setting file](http://libs.websoft9.com/Websoft9/DocsPicture/en/winscp/websoft9-winscp-youjian.png)

3. The relevant interface for modifying file permissions is as follows:

   ![Group and Owner settings](http://libs.websoft9.com/Websoft9/DocsPicture/en/winscp/websoft9-winscp-quanxian.png)

#### Run Command

WinSCP has a built-in command run function. Although the command function is limited to running non-interactive naming (that is, no feedback and process input are required during command execution), it is simple and practical for beginners.

1. WinSCP logs in to the server, click on the command window icon from the menu (shortcut Ctrl+T is also available)
   ![Command of Winscp](http://libs.websoft9.com/Websoft9/DocsPicture/en/winscp/winscp-ucmd-websoft9.png)
2. In the pop-up command run window to execute the command (one command at a time), to query the memory usage as an example, run the command `free -m`
   ![Command of Winscp](http://libs.websoft9.com/Websoft9/DocsPicture/en/winscp/wincp-showmemory-websoft9.png)

#### Putty Integration

Under certain specificities, you may need to use [Putty](https://putty.org/) to run commands. Since Putty is a command operation interface, you need to enter the root password every time you use it. If the password is complicated, it will make people feel more troublesome. In fact, WinSCP can be integrated with Putty. After integration, you can open Putty through WinSCP and log in to the server automatically.

1. Open the Preferences of WinSCP->Integration->Application, and input the local address of your Putty, click OK
   ![Putty Address](http://libs.websoft9.com/Websoft9/DocsPicture/en/winscp/websoft9-winscp-putty.png)
2. After the integration is successful, you only need to open the Putty through Winscp's window shortcut.
   ![Open Putty on WinSCP](http://libs.websoft9.com/Websoft9/DocsPicture/en/winscp/websoft9-winscp-puttyopen.png)

### For Windows{#connectwindows}

You can connect to the Window server through the Remote Desktop Tool (MSTSC) on your local computer.  

Below is the steps of MSTSC connection

1. Log in Cloud platform console, get you **Internet IP Address of Cloud Server**

2. Choose a way to open a local computer remote desktop (three-in-one):  
   - Open **Start** -> **Remote Desktop**
   - Open **Start**, input "mstsc" directly, the system will search for the Remote Desktop
   - Using the keyboard **Windows Logo** + **R** to start the command windows, input input "mstsc" to open the Remote Desktop

3. In the Remote Desktop Connection dialog, enter the Internet IP address of the instance. Then click 【Show Options】

   ![img](http://libs.websoft9.com/Websoft9/DocsPicture/en/common/windows-remote001-websoft9.png)

4. Enter the user name,check Allow me to save credentials. In this way, you do not need to manually enter the password again when you log on later.

   ![img](http://libs.websoft9.com/Websoft9/DocsPicture/en/common/windows-remote002-websoft9.png)

5. Click the Connect button to complete connection to the instance.
   ![image.png](http://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-windows2019desktop-websoft9.png)

6. After logging in remotely, you can **copy** the file directly from the local and **paste** the file to the server.
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-copyfilewin-websoft9.png)

> If you need to use FTP on Windows or Linux, you need to install the FTP Sever yourself

## FAQ

#### Forgotten Instance's password?

Please reset it in the Console of Cloud

#### What's username of Server?{#osaccount}

Most of time, the username of OS is `root` for Linux and 'administrator' for Windows, but diffrent Cloud not always  

You can refer below sheet for yourself:  

<Tabs>
  <TabItem value="linuxaccount" label="Linux" default>

   |  Cloud Platform   |  Administrator Username	   | Other|
   | --- | --- | --- |
   |  Azure   |  It was set by yourself when created instance   | [How to enable root account?](../azure#enableroot) |
   |  AWS   |  AmazonLinux is **ec2**,   CentOS is **centos**, Ubuntu is **ubuntu**, Debian is **admin**   | [How to enable root account?](../aws#enableroot)|
   |  Alibaba Cloud, Tencent Cloud, HUAWEI Cloud   |  All username is **root** except Ubuntu of Tencent is **ubuntu**   |  |

  </TabItem>
  <TabItem value="windowsaccount" label="Windows">

   |  Cloud Platform   |  Administrator Username	   | Other|
   | --- | --- | --- |
   |  Azure   |  It was set by yourself when created instance   |  |
   |  AWS, Alibaba Cloud, Tencent Cloud, HUAWEI Cloud   |   administrator    | |

  </TabItem>
</Tabs>
