---
sidebar_position: 1
slug: /alibabacloud
---

# Guide

This document is a simplified version of AlibabaCloud official documentation, combined with the actual operation of the deployment, to help you quickly master The most basic skills.

## ECS

You can change the manage ECS from Alibaba Cloud console:  

### Create ECS

1. Login to Console, open:【Elastic Compute Service】>【Instances】>【Create Instance】
   ![create ecs](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-createcs001-websoft9.png)

2. Select the payment method, instance type like these
   ![type](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-guige-websoft9.png)

   - Subscription: Allows you to pay upfront and then use the service over a period of time.  
   - Pay-As-You-Go: A billing method based on the amount of resources you actually use.  
   - Preemptive Instance: A billing method based on the amount of resources you actually use. 

3. Select the **Image** step is very important

   - Public Image: Alibaba Cloud provides official public images. 
   - Custom Image: Created from system snapshots of yourself
   - Shared Image: Other user shared for you
   - Marketplace Image: Alibaba Cloud Marketplace provides hundreds of high-quality third-party images that have undergone a strict review process.

4. If you use the Marketplace Image, suggest use the search key "websoft9"

   ![search websoft9 image](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-searchwebsoft9ls-websoft9.png)

4. Select the image you want to use

5. Go to next steps, include set Networking, System Configurations and so on

6. Wait 2-3 minutes for the ECS running when completed these steps

### Create Key Pairs

You should create **Key Pairs** before create ECS if you want to use Key Pairs for ECS connection

1. Login to Console, open:【Elastic Compute Service】>【Network and Security】>【Create Key Pairs】
   ![Key Pairs](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-createkey-websoft9.png)

2. Set the **SSH Key Pair Name** and select **Creation Mode**

3. When you complete the creation, please download the ××××.pem to your local computer

### Connect ECS

Blow are the methods for you to connect ECS of Alibaba Cloud:  

| Methods                                                   | Details                                                     |
| ------------------------------------------------------ | ------------------------------------------------------------ |
| Local SSH Connection                                   | Install [Putty](https://putty.org/) to your local computer and run it |
| [Workbench](https://ecs-workbench.aliyun.com/) Connection |An online web-based tool of AlibabaCloud  |
| VNC Connection                                           | VNC online web-based tool of AlibabaCloud, you can use it when you can not run Putty or Workbench|
| Send Remote Commands (Cloud Assistant)                   | To send remote commands, you must use the task execution feature provided by Cloud Assistant|

We use **Workbench Connection** to show you how to connect Linux:

1. Login to Console and list all you ECS, then click 【Connect】action for your target ECS
   ![Connect Action](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-remoteconnectweb-websoft9.png)

2. Then, click the 【Send Remote Call】button of 【Send Remote Commands (Cloud Assistant)】

3. Waiting for loading, and input username and password or Key Pairs to connect it


### Reset password

You can reset the ECS's password by the flowing method: 

##### Reset by Console

1. Login to AlibabaCloud console, list the ECS

2. Open the menu:【Password/Key Pair】>【Reset Password】
   ![reset password](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-resetpw-1-websoft9.png)
   ![reset password](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-resetpw-2-websoft9.png)

3. Restart the ECS and it take effect

##### Reset by Command

1. Login to AlibabaCloud console, list the ECS

2. Open the menu:【Connect】>【Send remote call】

3. Input your command like below click 【Run】 button
   ```
   echo "yourpassword" | passwd --stdin root  
   ```
4. You can receive below message when running successfully
   ```
   Changing password for user root.
   passwd: all authentication tokens updated successfully.
   ```

### Upgrade/Downgrade

If you want to change the ECS configuration for business, you should Upgrade or Downgrade it

1. Login to AlibabaCloud console, list the ECS

2. Open the 【Upgrade/Downgrade】menu of the target ECS
   ![upgrade](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-changeecsconfigure-websoft9.png)

3. You can choose from the following upgrade or downgrade schemes

### Reinitialize ECS

If you want to recover to ECS to the state of first installation, you need 【Reinitialize Disk】operation: 

1. Login to AlibabaCloud console, list the ECS

2. Stop your the target ECS

2. Open the menu: 【More】>【Disk and Image】>【Reinitialize Disk】
   ![Reset System disk](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-changesysdisk-websoft9.png)

3. Go to the next steps

> Could you distinguish **Reinitialize Disk** and **Replace System Disk**?


### Backup

The best backup method is automatic backup, you can use the Snapshot function of AlibabaCloud to backup your Disk automatically.  

You can backup your disk by the below methods:    

#### Set automatic Snapshot

1. Login to Console, open:【Elastic Compute Service】>【Storage & Snapshots】>【Snapshots】

2. Click the 【Automatic Snapshot Policies】to list and create a policy for you
    ![create Snapshot policy](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-snapshotstart-websoft9.png)

3. **Apply or Disable Automatic Snapshot Policy** for your disk
   ![Apply or Disable Automatic Snapshot](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-snapshotconf-websoft9.png)

4. Then you can see that you disk have set snapshot successfully
    ![Disk snapshot](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-snapshotsetdisk-websoft9.png)

#### Create Custom Image

If you don't want to set Snapshot, you can create a custom image for your ECS

1. Login to Console and list all ECS

2. Open the menu 【Disk and Image】>【Create Custom Image】 for your target ECS
   ![Create custom image](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-createimage-websoft9.png)

3. Go to the next steps

## Disk, Snapshot and Image

### Create Snapshot

1. Login to AlibabaCloud console, lis all disk by 【Elastic Compute Service】>【Disk】

2. Click the【Create Snapshot】 button to start it
   ![disk to snapshot](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-disktosnapshot-websoft9.png)
   
3. Go to the next steps to complete it

### Create Image

Image can be created based on snapshots, and image can be created based on ECS.

##### By ECS

1. Login to AlibabaCloud console, lis all ECS by 【Elastic Compute Service】>【Instances】

2. Click the menu 【Disk and Image】>【Create Custom Image】
   ![create image](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-createimage-websoft9.png)

3. Go to the next steps to complete it

##### By Snapshot

1. Login to AlibabaCloud console, lis all disk by 【Elastic Compute Service】>【Storage & Snapshots】>【Snapshots】

2. Select your Snapshot and create an Image for it
   ![create image](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-snapshottoimage-websoft9.png)

3. Go to the next steps to complete it

##### By local image

You can also create Image by OSS file which is your uploaded your local image

1. Login to AlibabaCloud console, lis all ECS by 【Elastic Compute Service】>【Instances and Images】>【Images】

2. Then click the **Import Image** link to create image by OSS file
   ![create image by OSS file](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/alibabacloud-importimage001-websoft9.png)

3. Set the parameters and you must select the correct **Operating System/Platform** for you image

   > What the difference between 【Others Linux】 and 【Customized Linux】? refer to [here](https://help.aliyun.com/document_detail/48226.html)

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/alibabacloud-importimage002-websoft9.png)
 

### Create Cloud disks

1. Login to Console to list all disk by 【Elastic Compute Service】>【Storage & Snapshot】>【Disk】

2. Click the 【Create Disk】 button 
   ![Create Disk](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-createdisk-websoft9.png)

3. Set the **Storage** and **Disk Name**
   ![Set the disk](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-createdisk2-websoft9.png)

4. Attach your disk to target ECS
   ![Mout Disk](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-attachdisk-websoft9.png)

5. Then create partitions and file systems after the disk is attached to the instance

   * [Linux partitions](https://www.alibabacloud.com/help/doc-detail/25426.htm)
   * [Windows partitions](https://www.alibabacloud.com/help/en/doc-detail/25418.htm)


### Detach Cloud disks

1. Login to Console to list all disk by 【Elastic Compute Service】>【Storage & Snapshot】>【Disk】

2. Click the 【More】>【Detach】
   ![Detach Disk](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-ditachdisk-websoft9.png)

3. Go to the next steps

### Resize Disks

You can resize your **System Disk** and **Data Disk** online by console

> Resize most of time mean increase disk storage

1. Login to Console to list all disk by 【Elastic Compute Service】>【Storage & Snapshot】>【Disk】

2. Click the 【More】>【Resize Disk】
   ![Resize Disk](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-changedisks-websoft9.png)

3. Check option【[Online Resizing](https://help.aliyun.com/document_detail/35095.html)】

4. Waiting for the result


### Mount Disks

If you run `df -m` to list all file system and found that there not increase disk storage, how to resolve it?  

1. Connect ECS and install `growpart` for it
   ```
   yum install -y cloud-utils-growpart
   growpart /dev/vda 1
   ```

2. Add the new added disk to the first partition
   ```
   # Attach to the first partition of first disk (System Disk)
   growpart /dev/vda 1

   # Attach to the first partition of second disk (Data Disk)
   growpart /dev/vdb 1
   ```

3. Run the file system command
   ```
   # ext
   resize2fs /dev/vda1 

   # xfs
   xfs_growfs /dev/vda1 
   ```

## Network and Security

### Check IP{#ip}

1. Login to console, lis all ECS by 【Elastic Compute Service】>【Instances and Images】>【Instances】

2. You can get the Public IP from the list table directly
   ![get ip](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-getpublicip-websoft9.png)

### Change IP

You can also change the Public IP for your ECS

1. Login to console, lis all ECS by 【Elastic Compute Service】>【Instances and Images】>【Instances】

2. Stop the ECS which you want to change IP for it

3. Open the menu: 【More】> 【Network and Security Group】>【Change Public IP Address】
   ![change ip](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-changeip-websoft9.png)

4. Go to the next steps to complete it

### Security Group{#securitygroup}

A [security group](https://www.alibabacloud.com/help/en/doc-detail/25387.html) acts as a virtual firewall for Elastic Compute Service (ECS) instances to control inbound and outbound traffic and improve security. You can use security groups and security group rules to define security domains in the cloud.  

Below is a sample for you how to **Enable TCP:80** port on security group:  

1. Login to console, lis all ECS by 【Elastic Compute Service】>【Instances and Images】>【Instances】

2. Open the menu: 【More】> 【Network and Security Group】>【Configure Security Group】
   ![ecs change security](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-modifysg-websoft9.png)

3. Click the 【Add Rules】button to list all rules
   ![ecs change security](https://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-modifysg80-websoft9.png)

4. Then, add a new rule by click the 【Add Rule】button授权对象一般为较为合适
   - Destination set to **HTTP(80)**
   - Source set to **0.0.0.0/0**

5. Save it 

## Domain Name{#domain}

[Domains](https://www.alibabacloud.com/help/product/35473.html) is a domain name management platform that provides domain name registration, transaction, monitoring, and protection services. 

Below steps is need for you to enable domains visit of your application:  

### Resolve Domain 

Resolve Domain mean that you set a mapping relations between domain and ECS's IP

1. Buy your Domain and register it

2. Login to console, lis all domains by 【AlibabaCloud DNS】
   ![Add a record](http://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-dns-websoft9.png)

3. Add an **Add Record** for it
   ![Add a record](http://libs.websoft9.com/Websoft9/DocsPicture/en/aliyun/aliyun-dnsrev-websoft9.png)

2. Save it and wait for 2-10 minute, then your DNS is take effect


### Domain Beian

If you ECS is created in China, and you want to use Domain for application, you must complete the **Domain Beian** for Government governance.

Refer to: [Domain Beian](https://beian.aliyun.com/order/index.htm)

