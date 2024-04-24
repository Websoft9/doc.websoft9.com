---
sidebar_position: 1
slug: /huaweicloud
---

# Guide

This document is a simplified version of HUAWEI CLOUD official documentation, combined with the actual operation of the deployment, to help you quickly master The most basic skills.

## ECS

You can manage the ECS on Console, includes:  

- Start
- Stop
- Restart
- Delete
- Modify ECS Specifications

Release ECS mean delete it, suitable for a pay-as-you-go instance that is not locked  

### Create ECS

1. Login to Console, open:【Cloud Server Console】>【Elastic Cloud Server】>【Buy ECS】
   ![create ecs](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-buyecs-websoft9.png)

2. Select the billing mode, instance type like these
   ![type](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-guige-websoft9.png)

   - Subscription: Allows you to pay upfront and then use the service over a period of time.  
   - Pay-As-You-Go: A billing method based on the amount of resources you actually use.  
   - Preemptible Instance: A billing method based on the amount of resources you actually use. 

3. Select the **Image** step is very important

   - Public Image: Alibaba Cloud provides official public images. 
   - Custom Image: Created from system snapshots of yourself
   - Shared Image: Other user shared for you
   - Marketplace Image: Alibaba Cloud Marketplace provides hundreds of high-quality third-party images that have undergone a strict review process.

4. If you use the Marketplace Image, suggest use the search key "websoft9"

   ![search websoft9 image](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-selectimage-websoft9.png)

4. Select the image you want to use

5. Go to next steps, include set Networking, System Configurations and so on

6. Wait 2-3 minutes for the ECS running when completed these steps

### Create Key Pairs

You should create **Key Pairs** before create ECS if you want to use Key Pairs for ECS connection

1. Login to Console, open:【Cloud Server Console】>【Key Pairs】
   ![Key Pairs](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-createkeys-websoft9.png)

2. Set the **SSH Key Pair Name** and select **Creation Mode**

3. When you complete the creation, please download the ××××.pem to your local computer

### Connect ECS

The Command is the basic operation of the Linux system. HUAWEI CLOUD provides two web-based SSH tools that can be logged in without an account.

Log in to the HUAWEI CLOUD Console, open the ECS -> Operations, click "Remote Login"

![Run command on HUAWEI CLOUD](http://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/hwcloud-runcmd-1-websoft9.png)

![Run command on HUAWEI CLOUD](http://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/hwcloud-runcmd-2-websoft9.png)

![Run command on HUAWEI CLOUD](http://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/hwcloud-runcmd-3-websoft9.png)


### Reset Password

You can reset the ECS's password by the below method: 

1. Login to HUAWEI CLOUD console, list the ECS

2. Open the menu:【More】>【Reset Password】
   ![reset password](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-resetpw-websoft9.png)

3. Restart the ECS and it take effect

### Modify ECS Specifications

If you want to change the ECS configuration for business, you should Upgrade or Downgrade it

1. Login to HUAWEI CLOUD console, list the ECS

2. Open the 【ModifySpecifications】menu of the target ECS
   ![upgrade](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-changeecsconfigure-websoft9.png)

3. You can choose from the following upgrade or downgrade schemes

### Change/Reinstall OS

If you want to recover to ECS to the state of first installation, you need 【Change OS】operation: 

1. Login to HUAWEI CLOUD console, list the ECS

2. Stop your the target ECS

2. Open the menu: 【More】>【Manage Image/Disk】>【Change OS】
   ![Reset System disk](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-iniecs-websoft9.png)

3. Go to the next steps


## Backup

The best backup method is automatic backup, you can use the Snapshot function of HUAWEI CLOUD to backup your Disk automatically.  

You can use the HUAWEI CLOUD [**Cloud Backup and Recovery (CBR)**](https://support.huaweicloud.com/en-us/productdesc-cbr/cbr_01_0002.html) to backup your data.  

![Automatic backup](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-cbr-websoft9.png)

You can backup your disk by the below methods:  

### Cloud Disk Backups

Back up and restore cloud disks. You can use a cloud disk backup to restore data to a backup point or create a new disk.Backups of encrypted disks are automatically encrypted to ensure data security.

1. Login to Console, go to: 【Recovery Console】>【Cloud Disk Backups】

2. Then click the button 【Buy Disk Backup Vault】
   ![Buy Disk Backup Vault](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-buydkbv-websoft9.png)

3. You can select disks will be applied to this Backup Vault
   ![Buy Disk Backup Vault](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-buydkbv002-websoft9.png)

2. Suggest set the backup strategy 
   ![set the backup strategy](https://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-buydkbv003-websoft9.png)
   
   ![set the backup strategy](https://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-buydkbv004-websoft9.png)

### Cloud Server Backups

Back up and restore cloud servers, ensuring the security and consistency of your data.

1. Login to Console, go to: 【Cloud Server Console】>【Cloud Server Backups】

2. Then click the button 【Buy Disk Backup Vault】
   ![Buy Disk Backup Vault](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-buydkbv-websoft9.png)

3. You can select Servers will be applied to this Backup Vault
   ![Buy Disk Backup Vault](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-cbrbuyecsbks-websoft9.png)

4. Suggest set the backup strategy 


## Disk, Snapshot and Image

For HUAWEI CLOUD, [Elastic Volume Service (EVS)](https://support.huaweicloud.com/en-us/productdesc-evs/en-us_topic_0014580741.html) is cloud disk which is a component for ECS.  

![](https://support.huaweicloud.com/en-us/productdesc-evs/en-us_image_0205523160.png)

### Create Snapshot

You can create snapshot for disk to backup

1. Login to Console, go to: 【Cloud Server Console】>【Elastic Volume Service	】>【Disk】

2. Select one Disk which you want to create snapshot for it
   ![Create snapshot](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-dkcreatesnapshot-websoft9.png)

3. Complete the next steps

### Create Image

1. Login to Console, list all ECS from 【Cloud Server Console】

2. Open the menu: 【More】>【Manage Image/Disk】>【Create Image】
   ![Create Image](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-createimage-websoft9.png)
   
3. Complete the next steps

### Buy Disk

1. Login to Console, go to: 【Cloud Server Console】>【Elastic Volume Service 】>【Disk】

2. Click 【Buy Disk】 button
   ![购买磁盘](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-createdisk-websoft9.png)

3. Set the **Disk Type** and **Disk Size**

4. Attach the new disk to ECS
   ![Attach Disk](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-attachdisk-websoft9.png)

5. [Initialize an EVS Data Disk](https://support.huaweicloud.com/en-us/qs-evs/evs_01_0058.html)

### Detach Disk

You can detach a Disk which you don't want to use for a ECS

1. Login to Console, go to: 【Cloud Server Console】>【Elastic Volume Service 】>【Disk】

2. Go to menu: 【More】>【Detach】
   ![Detach Disk](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-ditachdisk-websoft9.png)

3. Complete the next steps

### Expand Disk

You can resize your **System Disk** and **Data Disk** online by console

> Resize most of time mean increase disk storage

1. Login to Console, go to: 【Cloud Server Console】>【Elastic Volume Service 】>【Disk】

2. Click the link 【Expand Capacity】
   ![Expand Capacity](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-changedisks-websoft9.png)
   
3. Complete the next steps

## Network and Security

### Check IP{#ip}

[Elastic IP](https://support.huaweicloud.com/en-us/productdesc-eip/overview_0001.html) is the IP address for Internet access, that mean it the same with Internet IP

1. Login to Console, list all ECS from【Cloud Server Console】

2. You can get the **EIP** from the IP Address column
   ![get EIP](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/hwcloud-getpublicip-websoft9.png)

### Change IP

1. Login to Console, list all ECS from【Cloud Server Console】

2. Go to the detail page of ECS and click 【EIPs】 tab
   ![change IP](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-bindeip-websoft9.png)

3. Click 【Bind EIP】 button to complete this solution

### Security Group{#securitygroup}

A [Security Group](https://support.huaweicloud.com/en-us/usermanual-ecs/en-us_topic_0140323157.html) acts as a virtual firewall for Elastic Compute Service (ECS) instances to control inbound and outbound traffic and improve security. You can use security groups and security group rules to define security domains in the cloud.  

Below is a sample for you how to **Enable TCP:80** port on security group:  

1. Login to console, lis all ECS by 【Cloud Server Console】>【Security Group】

2. Add a rule or modify a rule

   ![ecs Security Group](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-safegroup001-websoft9.png)
   ![ecs Security Group](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-safegroup002-websoft9.png)

4. Then, add a new rule by click the 【Add Rule】button授权对象一般为较为合适
   ![ecs Security Group](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/hwcloud-safe80-websoft9.png)

   - Destination set to **HTTP(80)**
   - Source set to **0.0.0.0/0**

5. Save it 

## Domain Name{#domain}

[Domains](https://support.huaweicloud.com/intl/en-us/dns/) is a domain name management platform that provides domain name registration, transaction, monitoring, and protection services. 

Below steps is need for you to enable domains visit of your application:  

### Resolve Domain 

Resolve Domain mean that you set a mapping relations between domain and EI{}

1. Buy your Domain and register it
   ![Buy DNS](https://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/en/huaweicloud/hwcloud-buydomain-websoft9.png)

2. Login to DNS console, lis all domains
   ![Add a record](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-dns-websoft9.png)

3. Add an **Add Record** for it
   ![Add a record](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-dnsrev-websoft9.png)

2. Save it and wait for 2-10 minute, then your DNS is take effect

### Binding Domain

The precondition for binding a domain is that HUAWEI CLOUD can accessed by domain name.

When there is only one website on the server, you can visit the website without binding domain. While considering the server security and subsequent maintenance, **Binding Domain** is necessary.

Steps for binding HUAWEI CLOUD domain are as follows:

1. Connect your Cloud Server;
2. Modify **vhost configuration file**,and change the **server_name** and **proxy_pass** if you want.
   ```text
   server
   {
   listen 80;
   server_name websoft9.yourdomain.com;  # Set your domain
       location / {
       proxy_pass  http://127.0.0.1:8880; # Set your port
   ...
   }
   ```
3. Restart Nginx service
   ```
   sudo systemctl restart nginx
   ```

### Domain Beian

If you ECS is created in China, and you want to use Domain for application, you must complete the **Domain Beian** for Government governance.

![Domain Beian](https://libs.websoft9.com/Websoft9/DocsPicture/en/huaweicloud/huaweicloud-dnsbeians-websoft9.png)

Refer to: [Domain Beian](https://beian.huaweicloud.com)